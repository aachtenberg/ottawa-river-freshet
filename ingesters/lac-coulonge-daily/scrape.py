"""Lac Coulonge daily-level historical scraper (ORRPB station 1195).

The ORRPB per-location page for the cascade river station "Lake Coulonge at
Fort-Coulonge" (https://www.ottawariver.ca/location/coulonge/) accepts a POST
with reading-type=levels / data-type=daily / date-start / date-end /
data-display=table and returns a daily table with rows: Observed, Median,
Historic High, Historic Low. The form returns at most ~3 years (1095 days)
per request, so we chunk.

This produces the DAILY Lac Coulonge level series that V2 (during-freshet
conditional forecast) needs for analog-on-trajectory matching. V1's seasonal
prior only needs the annual peak, which lives in the monthly CSV back to 1972;
the per-location daily table only goes back to ~1990 (probed: a 1972-1974
request returns no observed table), so daily coverage is 1990-present (~36
freshet seasons). The observed values (~106-109 m geodetic) match the monthly
CSV, confirming this is the same station 1195.

Same scraper pattern, politeness, and raw-HTML caching as the sibling
orrpb-location-history scraper (which does the 13 reservoirs); the only
differences are slug="coulonge", the explicit reading-type=levels form field,
and a single-station output file.

Output:
  data/lac-coulonge-daily-1990-2026.csv
    (date, level_m, median_m, hist_high_m, hist_high_year,
     hist_low_m, hist_low_year)
  data/lac-coulonge-daily/raw/coulonge_<start>_<end>.html  (cached HTML)

Stdlib only.
"""
from __future__ import annotations
import csv
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "freshet-public" / "data"
RAW_DIR = DATA_DIR / "lac-coulonge-daily" / "raw"
OUT_CSV = DATA_DIR / "lac-coulonge-daily-1990-2026.csv"

SLUG = "coulonge"

USER_AGENT = (
    "freshet/1.0 (+https://github.com/aachtenberg/ottawa-river-freshet; "
    "Lac Coulonge daily-level historical archive)"
)
SLEEP_BETWEEN = 1.0

YEAR_START = 1990
YEAR_END = 2026
CHUNK_YEARS = 3  # max accepted by the form


def chunks(y0: int, y1: int, span: int):
    y = y0
    while y <= y1:
        end = min(y + span - 1, y1)
        yield y, end
        y = end + 1


def fetch_chunk(y_from: int, y_to: int) -> str:
    cache = RAW_DIR / f"{SLUG}_{y_from}_{y_to}.html"
    if cache.exists() and cache.stat().st_size > 1000:
        return cache.read_text(encoding="utf-8", errors="replace")
    body = urllib.parse.urlencode({
        "reading-type": "levels",
        "data-type": "daily",
        "date-start": f"{y_from}-01-01",
        "date-end": f"{y_to}-12-31",
        "data-display": "table",
    }).encode("utf-8")
    req = urllib.request.Request(
        f"https://www.ottawariver.ca/location/{SLUG}/",
        data=body, method="POST",
        headers={"User-Agent": USER_AGENT,
                 "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", errors="replace")
    cache.write_text(html, encoding="utf-8")
    time.sleep(SLEEP_BETWEEN)
    return html


def parse_table(html: str) -> dict[str, dict]:
    """Return {date_str -> {level, median, hist_high, hist_low, hh_yr, hl_yr}}.

    Returns empty dict if no observed row present (older years return only an
    operating-limits table without observed values).
    """
    m = re.search(r"<table[^>]*>(.*?)</table>", html, re.DOTALL)
    if not m:
        return {}
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(1), re.DOTALL)
    if not rows:
        return {}

    def cells(row):
        return [re.sub(r"<[^>]+>", "", c).strip()
                for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.DOTALL)]

    header = cells(rows[0])
    if not header or "date" not in header[0].lower():
        return {}
    dates = header[1:]

    by_label: dict[str, list[str]] = {}
    for r in rows[1:]:
        cs = cells(r)
        if not cs:
            continue
        label = re.sub(r"\s+", " ", cs[0]).strip().lower()
        by_label[label] = cs[1:]

    if "observed" not in by_label:
        return {}

    def parse_val_year(s: str) -> tuple[float | None, str]:
        # "178.79 (1997)" -> (178.79, "1997")
        s = re.sub(r"\s+", " ", s).strip()
        if not s or s == "-":
            return None, ""
        mm = re.match(r"^([\d.]+)\s*(?:\((\d{4})\))?", s)
        if not mm:
            return None, ""
        try:
            return float(mm.group(1)), mm.group(2) or ""
        except ValueError:
            return None, ""

    obs = by_label.get("observed", [])
    med = by_label.get("median", [])
    hh = by_label.get("historic high", [])
    hl = by_label.get("historic low", [])

    out: dict[str, dict] = {}
    for i, d in enumerate(dates):
        obs_v, _ = parse_val_year(obs[i]) if i < len(obs) else (None, "")
        med_v, _ = parse_val_year(med[i]) if i < len(med) else (None, "")
        hh_v, hh_y = parse_val_year(hh[i]) if i < len(hh) else (None, "")
        hl_v, hl_y = parse_val_year(hl[i]) if i < len(hl) else (None, "")
        if obs_v is None and med_v is None:
            continue
        out[d] = {"level_m": obs_v, "median_m": med_v,
                  "hist_high_m": hh_v, "hist_high_year": hh_y,
                  "hist_low_m": hl_v, "hist_low_year": hl_y}
    return out


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    all_rows: dict[str, dict] = {}
    for y0, y1 in chunks(YEAR_START, YEAR_END, CHUNK_YEARS):
        cache_path = RAW_DIR / f"{SLUG}_{y0}_{y1}.html"
        cached = cache_path.exists() and cache_path.stat().st_size > 1000
        try:
            html = fetch_chunk(y0, y1)
        except Exception as e:
            print(f"  {y0}-{y1}: ERR {e}", file=sys.stderr)
            continue
        data = parse_table(html)
        tag = "[cache]" if cached else "[fetch]"
        print(f"  {y0}-{y1} {tag} {len(data)} obs")
        all_rows.update(data)  # later chunks win on the overlapping rolling tail

    fields = ["date", "level_m", "median_m",
              "hist_high_m", "hist_high_year", "hist_low_m", "hist_low_year"]
    ordered = sorted(all_rows.items())
    with OUT_CSV.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for d, vals in ordered:
            row = {"date": d, **vals}
            w.writerow({k: ("" if row.get(k) is None else row[k]) for k in fields})
    print(f"\nWrote {len(ordered)} rows to {OUT_CSV.relative_to(REPO_ROOT)}")

    # Coverage summary
    obs_dates = [d for d, v in ordered if v.get("level_m") is not None]
    if obs_dates:
        years = sorted({d[:4] for d in obs_dates})
        print(f"Observed-level coverage: {len(obs_dates)} obs  "
              f"{obs_dates[0]} → {obs_dates[-1]}  ({len(years)} yrs)")


if __name__ == "__main__":
    main()
