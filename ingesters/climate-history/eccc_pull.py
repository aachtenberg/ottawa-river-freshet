#!/usr/bin/env python3
"""
Pulls daily climate data from ECCC bulk CSV endpoint for the watershed
stations relevant to Lac Coulonge freshet analysis.

Endpoint pattern (timeframe=2 = daily, one request per station per year
returns all 365 days):

    https://climate.weather.gc.ca/climate_data/bulk_data_e.html
        ?format=csv&stationID={ID}&Year={YYYY}&Month=1&Day=1&timeframe=2

Output:
    data/eccc-climate/manifest.csv
    data/eccc-climate/<slug>/daily-<first>-<last>.csv     (consolidated)
    data/eccc-climate/<slug>/raw/<year>.csv               (per-year cache)

Re-runs are idempotent: per-year files in raw/ are skipped if non-empty.
Stdlib only — matches the existing ingester convention.
"""

from __future__ import annotations
import csv
import io
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "eccc-climate"

ENDPOINT = (
    "https://climate.weather.gc.ca/climate_data/bulk_data_e.html"
    "?format=csv&stationID={sid}&Year={year}&Month=1&Day=1&timeframe=2"
)

# Throttle ECCC — they're public-funded, be polite.
SLEEP_SECONDS = 1.0
USER_AGENT = "freshet-public/eccc-pull (github.com/aachtenberg/ottawa-river-freshet)"

STATIONS = [
    # slug,                  station_id, climate_id, name,                     province, watershed,                              first, last
    ("ottawa-cda",           4333,  "6105976", "OTTAWA CDA",              "ON", "reference (south basin, replicates web session)", 1972, 2026),
    ("maniwaki-ua",          5607,  "7034480", "MANIWAKI UA",             "QC", "Gatineau (historical)",                            1972, 2018),
    ("maniwaki-airport",     5606,  "7034482", "MANIWAKI AIRPORT",        "QC", "Gatineau (recent)",                                1993, 2026),
    ("barrage-temiscamingue",5977,  "7080468", "BARRAGE TEMISCAMINGUE",   "QC", "Upper Ottawa main feeder of Lac Coulonge",         1972, 2026),
    ("mont-laurier",         5615,  "7035160", "MONT LAURIER",            "QC", "Lievre/Cabonga (Baskatong feed)",                  1972, 2025),
    ("parent",               5966,  "7075800", "PARENT",                  "QC", "Cabonga headwaters (north)",                       1972, 2026),
    ("val-dor-a",            6081,  "7098600", "VAL-D'OR A",              "QC", "Upper Ottawa headwaters (high north basin)",       1972, 2025),
    ("val-dor",              30172, "7098603", "VAL-D'OR",                "QC", "Upper Ottawa (recent overlap)",                    2008, 2026),
    ("rouyn",                10849, "7086716", "ROUYN",                   "QC", "Temiscaming watershed",                            1994, 2026),
    ("north-bay-a-old",      4201,  "6085700", "NORTH BAY A (legacy)",    "ON", "mid-basin wave-passage (historical)",              1972, 2013),
    ("north-bay-a-new",      52318, "6085680", "NORTH BAY A",             "ON", "mid-basin wave-passage (recent)",                  2014, 2026),
    ("pembroke-climate",     49068, "6106367", "PEMBROKE CLIMATE",        "ON", "mid-basin south near Lac Coulonge",                2010, 2026),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def pull_year(slug: str, station_id: int, year: int) -> tuple[int, int]:
    """Fetch one station-year. Returns (rows_written, http_status_or_0)."""
    raw_dir = OUT / slug / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    out_path = raw_dir / f"{year}.csv"
    if out_path.exists() and out_path.stat().st_size > 200:
        with out_path.open() as f:
            rows = sum(1 for _ in f) - 1
        return rows, 0  # cached
    url = ENDPOINT.format(sid=station_id, year=year)
    try:
        body = fetch(url)
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} for {slug} {year}", file=sys.stderr)
        return 0, e.code
    except Exception as e:
        print(f"  ERROR for {slug} {year}: {e}", file=sys.stderr)
        return 0, -1
    out_path.write_bytes(body)
    time.sleep(SLEEP_SECONDS)
    with out_path.open(encoding="utf-8") as f:
        rows = sum(1 for _ in f) - 1
    return rows, 200


def consolidate(slug: str, first: int, last: int) -> Path:
    """Concatenate raw/<year>.csv files into one daily-<first>-<last>.csv."""
    raw_dir = OUT / slug / "raw"
    out_path = OUT / slug / f"daily-{first}-{last}.csv"
    header_written = False
    total_rows = 0
    with out_path.open("w", encoding="utf-8", newline="") as out:
        writer = None
        for year in range(first, last + 1):
            yp = raw_dir / f"{year}.csv"
            if not yp.exists() or yp.stat().st_size < 200:
                continue
            with yp.open(encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)
                if header is None:
                    continue
                if not header_written:
                    writer = csv.writer(out)
                    writer.writerow(header)
                    header_written = True
                for row in reader:
                    writer.writerow(row)
                    total_rows += 1
    return out_path, total_rows


def write_manifest():
    mp = OUT / "manifest.csv"
    with mp.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "slug", "station_id", "climate_id", "name", "province",
            "watershed", "first_year", "last_year", "source_url_pattern",
            "consolidated_csv",
        ])
        for slug, sid, cid, name, prov, ws, first, last in STATIONS:
            w.writerow([
                slug, sid, cid, name, prov, ws, first, last,
                ENDPOINT.format(sid=sid, year="{year}"),
                f"{slug}/daily-{first}-{last}.csv",
            ])
    return mp


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"Output dir: {OUT}")
    print(f"Stations: {len(STATIONS)}{' (filtered: ' + only + ')' if only else ''}")
    print()

    summary = []
    for slug, sid, cid, name, prov, ws, first, last in STATIONS:
        if only and only != slug:
            continue
        print(f"=== {slug}  (stn {sid}, clim {cid}, {first}-{last}) ===")
        per_year_rows = 0
        cached = 0
        fetched = 0
        for year in range(first, last + 1):
            rows, status = pull_year(slug, sid, year)
            per_year_rows += rows
            if status == 0:
                cached += 1
            elif status == 200:
                fetched += 1
        out_path, total = consolidate(slug, first, last)
        print(f"  -> {out_path.relative_to(ROOT)}: {total} daily rows  (fetched {fetched}, cached {cached})")
        summary.append((slug, total, fetched, cached))
        print()

    mp = write_manifest()
    print(f"Manifest: {mp.relative_to(ROOT)}")
    print()
    print("Summary:")
    print(f"  {'slug':<25} {'rows':>8} {'fetched':>8} {'cached':>8}")
    for slug, total, fetched, cached in summary:
        print(f"  {slug:<25} {total:>8} {fetched:>8} {cached:>8}")


if __name__ == "__main__":
    main()
