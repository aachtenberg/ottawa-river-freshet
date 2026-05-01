#!/usr/bin/env python3
"""
Pulls full station-history context from WSC HYDAT for every station in the
Ottawa River basin (02K* and 02L*). Used to investigate the discontinuation
patterns documented in the freshet case file.

Outputs:
    data/wsc-hydrometric/ottawa-basin-stations.csv   (one row per station)
    data/wsc-hydrometric/ottawa-basin-remarks.csv    (one row per remark text)
    data/wsc-hydrometric/ottawa-basin-summary.md     (human-readable overview)

Stdlib only.
"""

from __future__ import annotations
import csv
import sqlite3
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HYDAT_DB = Path("/tmp/hydat/Hydat.sqlite3")
OUT = ROOT / "data" / "wsc-hydrometric"


def main():
    con = sqlite3.connect(HYDAT_DB)
    OUT.mkdir(parents=True, exist_ok=True)

    # Resolve agency IDs
    agencies = {r[0]: r[1] for r in con.execute("SELECT AGENCY_ID, AGENCY_EN FROM AGENCY_LIST")}
    statuses = {r[0]: r[1] for r in con.execute("SELECT * FROM STN_STATUS_CODES")}
    op_codes = {r[0]: r[1] for r in con.execute("SELECT * FROM OPERATION_CODES")}
    meas_codes = {r[0]: r[1] for r in con.execute("SELECT * FROM MEASUREMENT_CODES")}
    data_types = {r[0]: r[1] for r in con.execute("SELECT * FROM DATA_TYPES")}
    remark_codes = {r[0]: r[1] for r in con.execute("SELECT * FROM STN_REMARK_CODES")}

    # All Ottawa-basin stations
    stations = list(con.execute("""
        SELECT STATION_NUMBER, STATION_NAME, PROV_TERR_STATE_LOC,
               LATITUDE, LONGITUDE, DRAINAGE_AREA_GROSS, HYD_STATUS,
               REAL_TIME, CONTRIBUTOR_ID, OPERATOR_ID
        FROM STATIONS
        WHERE STATION_NUMBER LIKE '02K%' OR STATION_NUMBER LIKE '02L%'
        ORDER BY STATION_NUMBER
    """))
    print(f"{len(stations)} stations in Ottawa basin (02K* + 02L*)")

    # Per-station collection / regulation / remarks
    rows = []
    remark_rows = []
    for s in stations:
        stn = s[0]
        # Data collection (gives us flow/level coverage and operation type)
        dc = con.execute("""
            SELECT DATA_TYPE, YEAR_FROM, YEAR_TO, MEASUREMENT_CODE, OPERATION_CODE
            FROM STN_DATA_COLLECTION WHERE STATION_NUMBER=? ORDER BY DATA_TYPE, YEAR_FROM
        """, (stn,)).fetchall()
        # Regulation
        regs = con.execute("""
            SELECT YEAR_FROM, YEAR_TO, REGULATED FROM STN_REGULATION
            WHERE STATION_NUMBER=? ORDER BY YEAR_FROM
        """, (stn,)).fetchall()
        # Remarks
        rems = con.execute("""
            SELECT REMARK_TYPE_CODE, YEAR, REMARK_EN FROM STN_REMARKS
            WHERE STATION_NUMBER=? ORDER BY YEAR, REMARK_TYPE_CODE
        """, (stn,)).fetchall()

        # Compose flow/level coverage strings
        flow_periods = [d for d in dc if d[0] == "Q"]
        level_periods = [d for d in dc if d[0] == "H"]
        flow_str = "; ".join(f"{d[1]}-{d[2]} ({meas_codes.get(d[3], d[3])}, {op_codes.get(d[4], d[4])})" for d in flow_periods)
        level_str = "; ".join(f"{d[1]}-{d[2]} ({meas_codes.get(d[3], d[3])}, {op_codes.get(d[4], d[4])})" for d in level_periods)
        reg_str = "; ".join(f"{r[0] or ''}-{r[1] or ''} reg={r[2]}" for r in regs)

        rows.append({
            "station_number": stn,
            "name": s[1],
            "province": s[2],
            "lat": s[3],
            "lon": s[4],
            "drainage_km2": s[5] or "",
            "status": statuses.get(s[6], s[6]),
            "real_time": s[7],
            "contributor": agencies.get(s[8], f"id={s[8]}"),
            "operator": agencies.get(s[9], f"id={s[9]}"),
            "flow_coverage": flow_str,
            "level_coverage": level_str,
            "regulation": reg_str,
            "n_remarks": len(rems),
        })
        for code, year, txt in rems:
            remark_rows.append({
                "station_number": stn,
                "name": s[1],
                "remark_type": remark_codes.get(code, f"code={code}"),
                "year": year if year and year != -999 else "",
                "remark": (txt or "").strip(),
            })

    # Write stations CSV
    sp = OUT / "ottawa-basin-stations.csv"
    with sp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {sp.relative_to(ROOT)} ({len(rows)} rows)")

    # Write remarks CSV
    rp = OUT / "ottawa-basin-remarks.csv"
    with rp.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["station_number", "name", "remark_type", "year", "remark"])
        w.writeheader()
        w.writerows(remark_rows)
    print(f"  wrote {rp.relative_to(ROOT)} ({len(remark_rows)} remark rows)")

    # Build the human-readable summary
    md_path = OUT / "ottawa-basin-summary.md"
    write_summary(md_path, rows, remark_rows, agencies)
    print(f"  wrote {md_path.relative_to(ROOT)}")


def write_summary(path, rows, remarks, agencies):
    # Group operators
    operator_counts = defaultdict(lambda: {"active": 0, "discontinued": 0})
    for r in rows:
        operator_counts[r["operator"]][r["status"].lower()] += 1

    # Group discontinuation years for each measurement type
    disco_years = defaultdict(int)
    for r in rows:
        if r["status"] != "Discontinued":
            continue
        # Extract the latest YEAR_TO from flow or level coverage
        for blob in (r["flow_coverage"], r["level_coverage"]):
            if not blob:
                continue
            for part in blob.split("; "):
                yr = part.split("-")[1].split(" ")[0]
                if yr.isdigit():
                    disco_years[int(yr)] += 1

    # Identify the explicit-narrative remarks (free text, not just codes)
    narrative = [r for r in remarks if r["remark"] and len(r["remark"]) > 20]

    # Power-Plant-measured stations (the operator-fed flow gauges)
    pp_stations = [r for r in rows if "Power Plant" in r["flow_coverage"]]

    with path.open("w", encoding="utf-8") as f:
        f.write("# Ottawa basin WSC station history\n\n")
        f.write(f"Generated from HYDAT SQLite (one-shot inventory of 02K* + 02L* stations). ")
        f.write(f"Total: **{len(rows)} stations** with **{len(remarks)} remarks** ({len(narrative)} narrative).\n\n")

        f.write("## Status by operator\n\n")
        f.write("| operator | active | discontinued |\n|---|---:|---:|\n")
        for op in sorted(operator_counts, key=lambda o: -(operator_counts[o]["active"] + operator_counts[o]["discontinued"])):
            d = operator_counts[op]
            f.write(f"| {op} | {d['active']} | {d['discontinued']} |\n")
        f.write("\n")

        f.write("## Discontinuation years (count of stations whose Q or H series ended in that year)\n\n")
        f.write("| year | count |\n|---:|---:|\n")
        for yr in sorted(disco_years, reverse=True)[:25]:
            f.write(f"| {yr} | {disco_years[yr]} |\n")
        f.write("\n*(top 25 years; rows include both Q and H series, so a station can appear under multiple years)*\n\n")

        f.write("## Power-Plant-measured stations (operator-fed flow gauges)\n\n")
        f.write("These are flow gauges where the dam operator did the measurement (`measurement_code = P`) ")
        f.write("and fed the data to WSC. When the operator stops sharing publicly, the WSC series ends but the operator retains the data.\n\n")
        f.write("| station | name | operator | flow coverage | status |\n|---|---|---|---|---|\n")
        for r in pp_stations:
            f.write(f"| `{r['station_number']}` | {r['name']} | {r['operator']} | {r['flow_coverage']} | {r['status']} |\n")
        f.write("\n")

        f.write("## Stations with narrative remarks (text annotations from WSC)\n\n")
        f.write("Only remarks longer than 20 characters are shown. Codes-only remarks are in the CSV.\n\n")
        # Group narrative remarks by station
        by_stn = defaultdict(list)
        for r in narrative:
            by_stn[(r["station_number"], r["name"])].append(r)
        for (stn, name), rs in sorted(by_stn.items()):
            f.write(f"### `{stn}` — {name}\n\n")
            for rem in rs:
                yr = f" ({rem['year']})" if rem["year"] else ""
                f.write(f"- **[{rem['remark_type']}]**{yr} {rem['remark']}\n")
            f.write("\n")


if __name__ == "__main__":
    main()
