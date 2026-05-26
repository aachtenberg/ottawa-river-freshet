"""ORRPB per-station historical-record scraper.

Pulls the 13-month "Table view, Daily" data for every monitored location
on ottawariver.ca and upserts into the orrpb_station_history hypertable
via PostgREST.

Each per-station table contains 4 data rows: Observed (current year),
Median (1991-2020 P50), Historic High (per-day max over record with year
tag), and Historic Low (per-day min with year tag). The chart's green
80% normal-range band is NOT in the table response.

The endpoint is a POST to /location/<slug>/ with form params
reading-type, data-display, data-type. We hit it twice per station
(levels and flows) for the stations that publish flows. Stations that
only publish levels (Mattawa, Pembroke, Lake Coulonge, Chats Lake,
Gatineau, Thurso, Grenville) return an empty or unchanged response on
discharge requests and are skipped.

Stdlib-only (urllib + html.parser) to match the reservoir-ingest /
orrpb-river-ingest pattern.

Env vars: POSTGREST_URL, SCRAPE_USER_AGENT, ORRPB_BASE,
          ORRPB_STATIONS (override CSV of slug:metric pairs),
          ORRPB_SLEEP_S (sleep between requests, default 1.5s).
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser

ORRPB_BASE = os.environ.get("ORRPB_BASE", "https://www.ottawariver.ca/location")
POSTGREST = os.environ.get("POSTGREST_URL", "http://postgrest:3000")
USER_AGENT = os.environ.get(
    "SCRAPE_USER_AGENT",
    "freshet-xgrunt-com/1.0 (+https://freshet.xgrunt.com; community flood monitoring)",
)
SLEEP_S = float(os.environ.get("ORRPB_SLEEP_S", "1.5"))

# (slug, metrics_to_fetch) where metrics is a subset of ('levels', 'discharges').
# Slugs match ORRPB's location-URL segments. Metric availability follows the
# conditions-page tables: every station has levels; flows are available only
# at the dam sites in the cascade.
DEFAULT_STATIONS: list[tuple[str, tuple[str, ...]]] = [
    ("temiscaming",   ("levels", "discharges")),
    ("otto-holden",   ("levels", "discharges")),
    ("mattawa",       ("levels",)),
    ("des-joachims",  ("levels", "discharges")),
    ("pembroke",      ("levels",)),
    ("coulonge",      ("levels",)),
    ("chenaux",       ("levels", "discharges")),
    ("chats-falls",   ("levels", "discharges")),
    ("britannia",     ("levels", "discharges")),
    ("hull",          ("levels",)),
    ("thurso",        ("levels",)),
    ("grenville",     ("levels",)),
    ("carillon",      ("levels", "discharges")),
]


def stations_from_env() -> list[tuple[str, tuple[str, ...]]]:
    raw = os.environ.get("ORRPB_STATIONS", "").strip()
    if not raw:
        return DEFAULT_STATIONS
    out: list[tuple[str, tuple[str, ...]]] = []
    for entry in raw.split(","):
        entry = entry.strip()
        if not entry:
            continue
        if ":" in entry:
            slug, metrics_csv = entry.split(":", 1)
            metrics = tuple(m.strip() for m in metrics_csv.split("+") if m.strip())
        else:
            slug, metrics = entry, ("levels", "discharges")
        out.append((slug.strip(), metrics))
    return out


class TableExtractor(HTMLParser):
    """Capture every <table>'s rows of cells (cell = list of text fragments)."""

    def __init__(self) -> None:
        super().__init__()
        self.tables: list[list[list[list[str]]]] = []
        self._t: list[list[list[str]]] | None = None
        self._r: list[list[str]] | None = None
        self._c: list[str] | None = None

    def handle_starttag(self, tag: str, attrs):  # type: ignore[override]
        if tag == "table":
            self._t = []
            self.tables.append(self._t)
        elif tag == "tr" and self._t is not None:
            self._r = []
            self._t.append(self._r)
        elif tag in ("td", "th") and self._r is not None:
            self._c = []
            self._r.append(self._c)

    def handle_endtag(self, tag: str) -> None:  # type: ignore[override]
        if tag == "table":
            self._t = None
        elif tag == "tr":
            self._r = None
        elif tag in ("td", "th"):
            self._c = None

    def handle_data(self, data: str) -> None:  # type: ignore[override]
        if self._c is not None:
            self._c.append(data)


def cell_text(cell: list[str]) -> str:
    if not cell:
        return ""
    return re.sub(r"\s+", " ", "".join(cell).strip())


def find_data_table(tables: list[list[list[list[str]]]]) -> list[list[list[str]]] | None:
    """Return the data table (the one whose first column lists Observed/Median rows)."""
    for tbl in tables:
        if not tbl:
            continue
        labels = {cell_text(row[0]).strip() for row in tbl if row}
        if "Observed" in labels and "Median" in labels:
            return tbl
    return None


HI_LO_RE = re.compile(r"(-?[\d,]+(?:\.\d+)?)\s*\(?(\d{4})\)?")
NUM_RE = re.compile(r"^-?[\d,]+(?:\.\d+)?$")


def _to_float(s: str) -> float:
    """Parse a numeric cell allowing thousands separators (e.g. '2,200')."""
    return float(s.replace(",", ""))


def parse_table(
    tbl: list[list[list[str]]],
    station: str,
    metric_col: str,
) -> list[dict]:
    """Walk the table and emit one row per calendar date with all four series.

    metric_col is 'level_m' or 'flow_cms'. We collapse the four parallel rows
    (Observed/Median/Historic High/Historic Low) into a single record per date.
    """
    if not tbl or not tbl[0]:
        return []

    # Header row carries date columns. The first cell may be 'Date/Time' or empty.
    header = tbl[0]
    dates: list[str] = []
    for cell in header[1:]:
        txt = cell_text(cell)
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", txt)
        if m:
            dates.append(txt)
        else:
            dates.append("")  # placeholder so column index stays aligned

    if not any(dates):
        return []

    # Index data rows by their label.
    row_by_label: dict[str, list[list[str]]] = {}
    for row in tbl[1:]:
        if not row:
            continue
        label = cell_text(row[0])
        row_by_label[label] = row[1:]

    out_by_date: dict[str, dict] = {}
    for i, d in enumerate(dates):
        if not d:
            continue
        rec = {
            "time": d,
            "station": station,
            "metric": metric_col,
            "observed": None,
            "median": None,
            "historic_high_value": None,
            "historic_high_year": None,
            "historic_low_value": None,
            "historic_low_year": None,
        }
        for label, values in row_by_label.items():
            if i >= len(values):
                continue
            txt = cell_text(values[i])
            if not txt:
                continue
            if label == "Observed":
                if NUM_RE.match(txt):
                    rec["observed"] = _to_float(txt)
            elif label == "Median":
                if NUM_RE.match(txt):
                    rec["median"] = _to_float(txt)
            elif label == "Historic High":
                m = HI_LO_RE.search(txt)
                if m:
                    rec["historic_high_value"] = _to_float(m.group(1))
                    rec["historic_high_year"] = int(m.group(2))
            elif label == "Historic Low":
                m = HI_LO_RE.search(txt)
                if m:
                    rec["historic_low_value"] = _to_float(m.group(1))
                    rec["historic_low_year"] = int(m.group(2))
        # Skip dates with no usable data at all.
        if any(rec[k] is not None for k in
               ("observed", "median", "historic_high_value", "historic_low_value")):
            out_by_date[d] = rec
    return list(out_by_date.values())


def fetch_table_html(slug: str, reading_type: str) -> str:
    url = f"{ORRPB_BASE}/{slug}/"
    body = urllib.parse.urlencode({
        "reading-type": reading_type,    # levels | discharges
        "data-display": "table",
        "data-type":    "daily",
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def post_rows(table: str, rows: list[dict]) -> int:
    if not rows:
        return 0
    body = json.dumps(rows).encode("utf-8")
    req = urllib.request.Request(
        f"{POSTGREST}/{table}",
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates,return=minimal",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return len(rows)


def scrape_station(slug: str, reading_type: str) -> list[dict]:
    metric_col = "level_m" if reading_type == "levels" else "flow_cms"
    html = fetch_table_html(slug, reading_type)
    parser = TableExtractor()
    parser.feed(html)
    tbl = find_data_table(parser.tables)
    if tbl is None:
        return []
    return parse_table(tbl, slug, metric_col)


def main() -> int:
    stations = stations_from_env()
    print(f"Scraping {len(stations)} stations from {ORRPB_BASE} "
          f"(sleep {SLEEP_S:.1f}s between requests)")
    total_rows = 0
    failures: list[str] = []
    for slug, metrics in stations:
        for reading_type in metrics:
            label = f"{slug}/{reading_type}"
            try:
                rows = scrape_station(slug, reading_type)
            except Exception as exc:
                failures.append(label)
                print(f"  [FAIL] {label}: {type(exc).__name__}: {exc}", file=sys.stderr)
                time.sleep(SLEEP_S)
                continue
            if not rows:
                print(f"  [SKIP] {label}: no data rows parsed")
            else:
                posted = post_rows("orrpb_station_history", rows)
                total_rows += posted
                print(f"  [OK]   {label}: {posted} rows upserted "
                      f"(dates {rows[0]['time']} -> {rows[-1]['time']})")
            time.sleep(SLEEP_S)

    print(f"\nTotal upserted: {total_rows} rows across "
          f"{sum(len(m) for _, m in stations)} (station, metric) pairs")
    if failures:
        print(f"Failures: {len(failures)} -> {', '.join(failures)}", file=sys.stderr)
        # Don't exit nonzero on partial failure; ORRPB occasionally returns
        # 500s for individual locations. The whole-job fail mode is "got
        # zero rows for everything".
    if total_rows == 0:
        print("Got zero rows across all stations - bailing nonzero.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
