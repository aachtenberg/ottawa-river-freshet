"""
ORRPB main-stem flow + level ingester.

Two ORRPB tables, one cron job:
  1. "Average Daily Flows (m3/s)"     — ottawariver.ca/conditions/?display=river
     → orrpb_river_flows (7 stations: Temiscaming, Otto Holden, Des Joachims,
       Chenaux, Chats Falls, Britannia, Carillon).
  2. "Water levels at 24:00h in metres" — ottawariver.ca/conditions/ (default)
     → orrpb_river_levels (12 stations: Otto Holden, Mattawa, Des Joachims,
       Pembroke, Lake Coulonge, Chenaux, Chats Lake, Britannia, Gatineau,
       Thurso, Grenville, Carillon).

Why both exist: the OPG main-stem dams (Otto Holden, Des Joachims, Chenaux,
Chats Falls) are not in the Hydro-Québec open-data feed, and only ORRPB
publishes headwater levels for them. The "Current vs Median" flow charts in
the community ride on the flows table; the daily "Ottawa River Water Levels"
bar chart that gets re-shared on Facebook rides on the levels table.

ORRPB publishes 8-day rolling windows for both; each pull re-uploads them
cheaply (merge-duplicates upserts). Stdlib only (urllib + html.parser).

Env: POSTGREST_URL, ORRPB_RIVER_URL (override flows URL),
     ORRPB_LEVELS_URL (override levels URL), SCRAPE_USER_AGENT.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser

ORRPB_FLOWS_URL  = os.environ.get("ORRPB_RIVER_URL",
                                  "https://www.ottawariver.ca/conditions/?display=river")
ORRPB_LEVELS_URL = os.environ.get("ORRPB_LEVELS_URL",
                                  "https://www.ottawariver.ca/conditions/")
POSTGREST = os.environ.get("POSTGREST_URL", "http://postgrest.data.svc.cluster.local:3000")
USER_AGENT = os.environ.get(
    "SCRAPE_USER_AGENT",
    "freshet-xgrunt-com/1.0 (+https://freshet.xgrunt.com; community flood monitoring)")

# ORRPB row label (lower-cased substring) -> stable station slug.
FLOW_STATION_MATCH = [
    ("temiscaming", "temiscaming"),
    ("otto holden", "otto-holden"),
    ("joachim",     "des-joachims"),
    ("chenaux",     "chenaux"),
    ("chats",       "chats-falls"),
    ("britannia",   "britannia"),
    ("deschenes",   "britannia"),     # "Lake Deschenes at Britannia"
    ("carillon",    "carillon"),
]

# Levels table has 12 stations; slugs intentionally diverge slightly from
# flows where the geography differs (chats-falls = dam outflow, chats-lake =
# headpond elevation).
LEVEL_STATION_MATCH = [
    ("otto holden", "otto-holden"),
    ("mattawa",     "mattawa"),
    ("joachim",     "des-joachims"),
    ("pembroke",    "pembroke"),
    ("coulonge",    "lake-coulonge"),  # "Lake Coulonge at Fort-Coulonge"
    ("chenaux",     "chenaux"),
    ("chats lake",  "chats-lake"),
    ("deschenes",   "britannia"),      # "Lake Deschenes at Britannia (Ottawa)"
    ("britannia",   "britannia"),
    ("gatineau",    "gatineau"),
    ("thurso",      "thurso"),
    ("grenville",   "grenville"),
    ("carillon",    "carillon"),
]


class TableExtractor(HTMLParser):
    """Capture every <table>'s rows-of-cells (cell = list of text fragments)."""
    def __init__(self):
        super().__init__()
        self.tables = []
        self._t = self._r = self._c = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self._t = []; self.tables.append(self._t)
        elif tag == "tr" and self._t is not None:
            self._r = []; self._t.append(self._r)
        elif tag in ("td", "th") and self._r is not None:
            self._c = []; self._r.append(self._c)

    def handle_endtag(self, tag):
        if tag == "table": self._t = None
        elif tag == "tr": self._r = None
        elif tag in ("td", "th"): self._c = None

    def handle_data(self, data):
        if self._c is not None:
            self._c.append(data)


def cell_text(cell):
    return re.sub(r"\s+", " ", "".join(cell).strip()) if cell else ""


def fetch_html(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def find_table(tables, needles):
    """Return the first table whose first row's text contains any needle."""
    for tbl in tables:
        if not tbl or not tbl[0]:
            continue
        first = " ".join(cell_text(c) for c in tbl[0]).lower()
        if any(n in first for n in needles):
            return tbl
    return None


def parse_dates(header_row):
    out = []
    today = datetime.now(timezone.utc)
    for cell in (cell_text(c) for c in header_row[1:]):
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", cell)
        if m:
            out.append(datetime(int(m[1]), int(m[2]), int(m[3]), tzinfo=timezone.utc))
            continue
        m = re.match(r"^([A-Za-z]{3,})\s+(\d{1,2})$", cell)
        if m:
            try:
                mon = datetime.strptime(m[1][:3], "%b").month
            except ValueError:
                continue
            d = datetime(today.year, mon, int(m[2]), tzinfo=timezone.utc)
            if d - today > timedelta(days=10):
                d = d.replace(year=today.year - 1)
            out.append(d)
    return out


def slug_for(label, matches):
    low = label.lower()
    for needle, slug in matches:
        if needle in low:
            return slug
    return None


def parse_value_table(tbl, matches, value_key):
    """Generic ORRPB rolling-window-table parser.

    Each station row has a label cell at column 0 with optional 'Agency: X'
    text, then 8 daily value cells. Returns rows keyed for orrpb_river_flows
    / orrpb_river_levels (controlled by `value_key`: 'flow_cms' or 'level_m').
    """
    if len(tbl) < 2:
        return []
    dates = parse_dates(tbl[0])
    if not dates:
        print(f"no dates parsed from header: {tbl[0]!r}", file=sys.stderr)
        return []
    rows = []
    for row in tbl[1:]:
        if len(row) < 2:
            continue
        c0 = cell_text(row[0])
        name = re.sub(r"Graph View.*", "", c0).strip()
        agm = re.search(r"Agency:\s*([A-Za-z/.\- ]+)", c0)
        agency = agm.group(1).strip() if agm else None
        slug = slug_for(name, matches)
        if not slug:
            continue
        for i, cell in enumerate(row[1:]):
            if i >= len(dates):
                break
            txt = cell_text(cell)
            if not txt or txt in ("—", "-", "N/A"):
                continue
            try:
                val = float(txt.replace(",", ""))
            except ValueError:
                continue
            rows.append({
                "time": dates[i].date().isoformat(),
                "station": slug,
                value_key: val,
                "agency": agency,
            })
    return rows


def post_rows(table, rows):
    if not rows:
        print(f"  nothing to post to {table}", file=sys.stderr)
        return
    body = json.dumps(rows).encode("utf-8")
    req = urllib.request.Request(
        f"{POSTGREST}/{table}", data=body, method="POST",
        headers={"Content-Type": "application/json", "Prefer": "resolution=merge-duplicates"})
    with urllib.request.urlopen(req, timeout=60) as r:
        print(f"  POST /{table} -> HTTP {r.status} ({len(rows)} rows)")


def latest_per_station(rows):
    by = {}
    for r in rows:
        if r["station"] not in by or r["time"] > by[r["station"]]["time"]:
            by[r["station"]] = r
    return by


def scrape_flows():
    print(f"Fetching {ORRPB_FLOWS_URL}")
    html = fetch_html(ORRPB_FLOWS_URL)
    ex = TableExtractor(); ex.feed(html)
    tbl = find_table(ex.tables, ["average daily flow"])
    if not tbl:
        print("ORRPB river page: 'Average Daily Flows' table not found — layout change?",
              file=sys.stderr)
        return False
    rows = parse_value_table(tbl, FLOW_STATION_MATCH, "flow_cms")
    if not rows:
        print("parsed 0 flow rows", file=sys.stderr)
        return False
    by = latest_per_station(rows)
    for slug, r in sorted(by.items()):
        print(f"  flow  {slug:14s} {r['time']}  {r['flow_cms']:>7.0f} m³/s  ({r['agency']})")
    post_rows("orrpb_river_flows", rows)
    return True


def scrape_levels():
    print(f"Fetching {ORRPB_LEVELS_URL}")
    html = fetch_html(ORRPB_LEVELS_URL)
    ex = TableExtractor(); ex.feed(html)
    tbl = find_table(ex.tables, ["water levels", "water level at"])
    if not tbl:
        print("ORRPB conditions page: 'Water levels at 24:00h' table not found — layout change?",
              file=sys.stderr)
        return False
    rows = parse_value_table(tbl, LEVEL_STATION_MATCH, "level_m")
    if not rows:
        print("parsed 0 level rows", file=sys.stderr)
        return False
    by = latest_per_station(rows)
    for slug, r in sorted(by.items()):
        print(f"  level {slug:14s} {r['time']}  {r['level_m']:>7.2f} m    ({r['agency']})")
    post_rows("orrpb_river_levels", rows)
    return True


def main():
    ok_flows  = scrape_flows()
    ok_levels = scrape_levels()
    # Allow one half to fail without failing the whole job — ORRPB sometimes
    # ships only one of the two tables on transitional days.
    if not (ok_flows or ok_levels):
        sys.exit(1)
    print("Done.")


if __name__ == "__main__":
    main()
