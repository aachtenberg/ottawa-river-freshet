#!/usr/bin/env python3
"""
Extracts daily flow and water-level data from the WSC HYDAT SQLite for the
Ottawa River basin stations relevant to the freshet analysis.

HYDAT bulk download:
    https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/

Stations of interest:
- 02KF005  OTTAWA RIVER AT BRITANNIA          (Dan's year-overlay panel; 1960-)
- 02KC017  OUTAOUAIS - CENTRALE DE BRYSON     (the dam itself; 1985-1994 only)
- 02KC011  OUTAOUAIS PRES DE PORTAGE-DU-FORT  (downstream of Lac Coulonge; 1942-1948)
- 02KG001  COULONGE PRES DE FORT-COULONGE     (Coulonge tributary; 1926-1993)
- 02KG005  COULONGE AU PONT TERRY-FOX         (at Pontefract golf course; 2004-2008)
- 02LH001  GATINEAU A MANIWAKI                (cross-check; 1925-1998)
- 02KF009  OTTAWA RIVER AT CHATS FALLS        (mid-Ottawa downstream; 1915-1994)

HYDAT stores daily data in wide form (one row per station-year-month, 31
day columns). This script un-pivots to long form, one row per day.

Output:
    data/wsc-hydrometric/manifest.csv
    data/wsc-hydrometric/<station>/daily.csv   (date, flow_cms, flow_symbol, level_m, level_symbol)

Stdlib only.
"""

from __future__ import annotations
import csv
import sqlite3
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HYDAT_DB = Path("/tmp/hydat/Hydat.sqlite3")
OUT = ROOT / "data" / "wsc-hydrometric"
HYDAT_SOURCE_URL = "https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/Hydat_sqlite3_20260417.zip"

STATIONS = [
    # number,    slug,                              note
    ("02KF005", "britannia-ottawa-river",          "Ottawa River at Britannia (Ottawa, ON) — Dan's year-overlay panel"),
    ("02KC017", "bryson-centrale",                 "Bryson generating station — discontinued 1994"),
    ("02KC011", "portage-du-fort",                 "Ottawa River at Portage-du-Fort — historical 1942-1948"),
    ("02KG001", "coulonge-fort-coulonge",          "Coulonge River near Fort-Coulonge — discontinued 1993"),
    ("02KG005", "coulonge-pontefract-golf",        "Coulonge River at Terry Fox bridge (Pontefract) — short window 2004-2008"),
    ("02LH001", "gatineau-maniwaki",               "Gatineau River at Maniwaki — level 1925-1998"),
    ("02KF009", "chats-falls-ottawa-river",        "Ottawa River at Chats Falls — discontinued 1994"),
]

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _is_leap(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def extract_long(con, station: str) -> list[dict]:
    """Pull DLY_FLOWS + DLY_LEVELS for a station and merge to long-form rows."""
    flows = {}  # (yyyy-mm-dd) -> (value, symbol)
    for row in con.execute(
        "SELECT YEAR, MONTH, NO_DAYS, "
        + ", ".join(f"FLOW{d}, FLOW_SYMBOL{d}" for d in range(1, 32))
        + " FROM DLY_FLOWS WHERE STATION_NUMBER=? ORDER BY YEAR, MONTH",
        (station,),
    ):
        year, month, ndays = row[0], row[1], row[2]
        max_day = ndays or (29 if (month == 2 and _is_leap(year)) else DAYS_IN_MONTH[month - 1])
        for d in range(1, max_day + 1):
            v = row[2 + (d - 1) * 2 + 1]
            sym = row[2 + (d - 1) * 2 + 2]
            if v is None and not sym:
                continue
            key = f"{year:04d}-{month:02d}-{d:02d}"
            flows[key] = (v, sym or "")

    levels = {}
    for row in con.execute(
        "SELECT YEAR, MONTH, NO_DAYS, "
        + ", ".join(f"LEVEL{d}, LEVEL_SYMBOL{d}" for d in range(1, 32))
        + " FROM DLY_LEVELS WHERE STATION_NUMBER=? ORDER BY YEAR, MONTH",
        (station,),
    ):
        year, month, ndays = row[0], row[1], row[2]
        max_day = ndays or (29 if (month == 2 and _is_leap(year)) else DAYS_IN_MONTH[month - 1])
        for d in range(1, max_day + 1):
            v = row[2 + (d - 1) * 2 + 1]
            sym = row[2 + (d - 1) * 2 + 2]
            if v is None and not sym:
                continue
            key = f"{year:04d}-{month:02d}-{d:02d}"
            levels[key] = (v, sym or "")

    all_dates = sorted(set(flows) | set(levels))
    out = []
    for d in all_dates:
        f = flows.get(d, (None, ""))
        l = levels.get(d, (None, ""))
        out.append({
            "date": d,
            "flow_cms": "" if f[0] is None else f"{f[0]:.3f}",
            "flow_symbol": f[1],
            "level_m": "" if l[0] is None else f"{l[0]:.4f}",
            "level_symbol": l[1],
        })
    return out


def write_manifest(meta):
    mp = OUT / "manifest.csv"
    with mp.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "station_number", "slug", "name", "province",
            "drainage_area_km2", "hyd_status",
            "flow_first_year", "flow_last_year", "flow_n",
            "level_first_year", "level_last_year", "level_n",
            "note", "source", "consolidated_csv",
        ])
        for m in meta:
            w.writerow([
                m["station"], m["slug"], m["name"], m["prov"], m["drainage"],
                m["status"], m["fmin"], m["fmax"], m["fn"],
                m["lmin"], m["lmax"], m["ln"],
                m["note"], HYDAT_SOURCE_URL, f"{m['slug']}/daily.csv",
            ])
    return mp


def main():
    if not HYDAT_DB.exists():
        sys.exit(f"HYDAT SQLite not found at {HYDAT_DB}")
    OUT.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(HYDAT_DB)
    meta = []
    for stn, slug, note in STATIONS:
        info = con.execute(
            "SELECT STATION_NAME, PROV_TERR_STATE_LOC, DRAINAGE_AREA_GROSS, HYD_STATUS "
            "FROM STATIONS WHERE STATION_NUMBER=?", (stn,)
        ).fetchone()
        if not info:
            print(f"  skip {stn}: not in HYDAT")
            continue
        name, prov, drainage, status = info
        f_yr = con.execute("SELECT MIN(YEAR),MAX(YEAR),COUNT(*) FROM DLY_FLOWS WHERE STATION_NUMBER=?", (stn,)).fetchone()
        l_yr = con.execute("SELECT MIN(YEAR),MAX(YEAR),COUNT(*) FROM DLY_LEVELS WHERE STATION_NUMBER=?", (stn,)).fetchone()
        rows = extract_long(con, stn)
        sd = OUT / slug
        sd.mkdir(parents=True, exist_ok=True)
        out_path = sd / "daily.csv"
        with out_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["date", "flow_cms", "flow_symbol", "level_m", "level_symbol"])
            w.writeheader()
            for r in rows:
                w.writerow(r)
        print(f"  {stn} {slug}: {len(rows)} daily rows -> {out_path.relative_to(ROOT)}")
        meta.append({
            "station": stn, "slug": slug, "name": name, "prov": prov,
            "drainage": drainage or "", "status": status,
            "fmin": f_yr[0] or "", "fmax": f_yr[1] or "", "fn": f_yr[2],
            "lmin": l_yr[0] or "", "lmax": l_yr[1] or "", "ln": l_yr[2],
            "note": note,
        })
    mp = write_manifest(meta)
    print(f"\nManifest: {mp.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
