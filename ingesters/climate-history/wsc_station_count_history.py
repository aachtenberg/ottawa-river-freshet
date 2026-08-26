#!/usr/bin/env python3
"""How many Ottawa-basin gauges are in the federal public record, year by year.

Community claim (Dan, Ottawa River Flood Watch, 2026-08-25): the number of
federal/public Water Survey of Canada gauge records in the Ottawa River basin
fell noticeably around 1994, many stations moved to provincial or utility
responsibility (particularly in Quebec), and pre-1994 flow records that used
to be in one place now have to be reconstructed from HQ / OPG / provincial
sources.

This script counts, for every year, the stations in the Ottawa River basin
that have at least one day of published daily flow or daily level in HYDAT
(tables DLY_FLOWS / DLY_LEVELS), split by the operator class HYDAT records
for the station and by province, plus the subset on the Ottawa main stem.

Basin definition: HYDAT station prefixes 02J (upper Ottawa above Mattawa),
02K (middle Ottawa and Ontario tributaries) and 02L (Rideau, Gatineau,
Lievre, lower Ottawa). Pass --prefixes to change.

Inputs:  /tmp/hydat/Hydat.sqlite3 (or --db)
Outputs: data/wsc-hydrometric/ottawa-basin-station-counts.csv
         data/community-notes/figures/2026-08-25_wsc_station_count_1994.png
"""
from __future__ import annotations

import argparse
import csv
import sqlite3
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
STAMP = "2026-08-25"
CSV_OUT = ROOT / "data" / "wsc-hydrometric" / "ottawa-basin-station-counts.csv"
FIG_OUT = ROOT / "data" / "community-notes" / "figures" / f"{STAMP}_wsc_station_count_1994.png"

# Operator classes, fixed order (also the stacking + colour order)
CLASSES = ["WSC (federal)", "Provincial", "Utility", "Unrecorded"]
COLOURS = {"WSC (federal)": "#2a78d6", "Provincial": "#eb6834",
           "Utility": "#1baf7a", "Unrecorded": "#9a9890"}
TEXT, MUTED, GRID = "#1f1f1e", "#5f5e58", "#e2e1dc"


def op_class(name: str | None) -> str:
    if not name:
        return "Unrecorded"
    n = name.upper()
    if n.startswith("WATER SURVEY"):
        return "WSC (federal)"
    if "MINISTERE" in n or "MINISTRY" in n or "ENVIRONMENT" in n:
        return "Provincial"
    return "Utility"


def is_mainstem(name: str) -> bool:
    n = name.upper()
    return n.startswith("OTTAWA RIVER") or n.startswith("OUTAOUAIS")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="/tmp/hydat/Hydat.sqlite3")
    ap.add_argument("--prefixes", default="02J,02K,02L")
    ap.add_argument("--y0", type=int, default=1950)
    ap.add_argument("--y1", type=int, default=2023,
                    help="last complete year in HYDAT; 2024-25 are still being loaded")
    a = ap.parse_args()
    prefixes = [p.strip() for p in a.prefixes.split(",")]
    con = sqlite3.connect(a.db)
    agencies = dict(con.execute("SELECT AGENCY_ID, AGENCY_EN FROM AGENCY_LIST"))
    where = " OR ".join("STATION_NUMBER LIKE ?" for _ in prefixes)
    params = [p + "%" for p in prefixes]

    stations = {}
    for stn, name, prov, da, op_id in con.execute(
            f"SELECT STATION_NUMBER, STATION_NAME, PROV_TERR_STATE_LOC, "
            f"DRAINAGE_AREA_GROSS, OPERATOR_ID FROM STATIONS WHERE {where}", params):
        stations[stn] = dict(name=name, prov=prov, da=da or 0.0,
                             op=op_class(agencies.get(op_id)))
    print(f"{len(stations)} stations with prefixes {prefixes}")

    # (station, year) pairs with any published daily data
    flow_years = defaultdict(set)
    level_years = defaultdict(set)
    for stn, yr in con.execute(
            f"SELECT DISTINCT STATION_NUMBER, YEAR FROM DLY_FLOWS WHERE {where}", params):
        flow_years[stn].add(yr)
    for stn, yr in con.execute(
            f"SELECT DISTINCT STATION_NUMBER, YEAR FROM DLY_LEVELS WHERE {where}", params):
        level_years[stn].add(yr)

    years = list(range(a.y0, a.y1 + 1))
    rows = []
    for y in years:
        c = defaultdict(int)
        for stn, s in stations.items():
            f, l = y in flow_years[stn], y in level_years[stn]
            if not (f or l):
                continue
            c["all"] += 1
            c[s["prov"]] += 1
            c[s["op"]] += 1
            if f:
                c["flow"] += 1
                c["flow_" + s["prov"]] += 1
            if is_mainstem(s["name"]):
                c["mainstem"] += 1
                if f:
                    c["mainstem_flow"] += 1
        rows.append(dict(year=y, all=c["all"], ON=c["ON"], QC=c["QC"],
                         flow=c["flow"], flow_ON=c["flow_ON"], flow_QC=c["flow_QC"],
                         mainstem=c["mainstem"], mainstem_flow=c["mainstem_flow"],
                         **{k: c[k] for k in CLASSES}))

    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {CSV_OUT}")

    # --- console summary --------------------------------------------------
    by = {r["year"]: r for r in rows}
    peak = max(rows, key=lambda r: r["all"])
    print(f"peak: {peak['year']} with {peak['all']} stations")
    for y in (1977, 1985, 1990, 1993, 1994, 1995, 1996, 2000, 2010, 2020, years[-1]):
        r = by[y]
        print(f"{y}: all={r['all']:3d} ON={r['ON']:3d} QC={r['QC']:3d} flow={r['flow']:3d} "
              f"mainstem={r['mainstem']:2d}/{r['mainstem_flow']:2d} | "
              + " ".join(f"{k.split()[0]}={r[k]}" for k in CLASSES))

    print("\n02J stations (basin membership check):")
    for stn, s in sorted(stations.items()):
        if stn.startswith("02J"):
            print(f"  {stn} {s['prov']} {s['da']:>8.0f} km2  {s['name']}")

    print("\nStations whose last published year is 1994:")
    for stn, s in sorted(stations.items()):
        ys = flow_years[stn] | level_years[stn]
        if ys and max(ys) == 1994:
            kind = "flow" if 1994 in flow_years[stn] else "level"
            print(f"  {stn} {s['prov']} {s['op']:14s} {kind:5s} {min(ys)}-1994 {s['name']}")

    print(f"\nMain-stem stations published in 1985 vs {years[-1]}:")
    for y in (1985, years[-1]):
        names = [f"{stn} ({'Q' if y in flow_years[stn] else ''}{'H' if y in level_years[stn] else ''})"
                 for stn, s in sorted(stations.items())
                 if is_mainstem(s["name"]) and (y in flow_years[stn] or y in level_years[stn])]
        print(f"  {y}: {len(names)} -> {', '.join(names)}")

    # --- figure -----------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9.5),
                                   gridspec_kw={"height_ratios": [3, 1.6]}, sharex=True)
    fig.patch.set_facecolor("#fcfcfb")
    stacks = [[by[y][k] for y in years] for k in CLASSES]
    ax1.stackplot(years, stacks, labels=CLASSES, colors=[COLOURS[k] for k in CLASSES],
                  alpha=0.9, edgecolor="#fcfcfb", linewidth=0.8)
    ax1.plot(years, [by[y]["all"] for y in years], color=TEXT, linewidth=1.6)
    for ax in (ax1, ax2):
        ax.set_facecolor("#fcfcfb")
        ax.axvline(1994.5, color=MUTED, linestyle="--", linewidth=1.2)
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        ax.spines["left"].set_color(GRID)
        ax.spines["bottom"].set_color(GRID)
        ax.tick_params(colors=MUTED, labelsize=10)
    p, r94, r95, last = peak, by[1994], by[1995], by[years[-1]]
    ax1.annotate(f"{p['year']}: {p['all']} stations", (p["year"], p["all"]),
                 xytext=(p["year"] + 3, p["all"] + 16), fontsize=10, color=TEXT,
                 arrowprops=dict(arrowstyle="-", color=MUTED))
    ax1.annotate(f"1994 → 1995: {r94['all']} → {r95['all']}", (1995, r95["all"]),
                 xytext=(1997, r95["all"] + 26), fontsize=10, color=TEXT,
                 arrowprops=dict(arrowstyle="-", color=MUTED))
    ax1.annotate(f"{last['year']}: {last['all']}", (last["year"], last["all"]),
                 xytext=(last["year"] - 9, last["all"] + 20), fontsize=10, color=TEXT,
                 arrowprops=dict(arrowstyle="-", color=MUTED))
    ax1.set_ylabel("Stations with published daily data in HYDAT", color=MUTED, fontsize=10)
    ax1.set_title("Ottawa River basin gauges in the federal public record (HYDAT), by operator, "
                  f"{years[0]}–{years[-1]}", loc="left", fontsize=13, color=TEXT, pad=12)
    ax1.legend(loc="upper left", frameon=False, fontsize=10, labelcolor=TEXT)
    ax1.set_ylim(0, max(r["all"] for r in rows) * 1.2)

    ax2.step(years, [by[y]["mainstem"] for y in years], where="mid", color="#2a78d6",
             linewidth=2, label="Ottawa main stem: any published data")
    ax2.step(years, [by[y]["mainstem_flow"] for y in years], where="mid", color="#eb6834",
             linewidth=2, label="Ottawa main stem: published flow")
    ms85, ms25 = by[1985], by[years[-1]]
    ax2.annotate(f"1985: {ms85['mainstem']} stations, {ms85['mainstem_flow']} with flow",
                 (1985, ms85["mainstem"]), xytext=(1954, ms85["mainstem"] + 2.5),
                 fontsize=10, color=TEXT, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax2.annotate(f"{years[-1]}: {ms25['mainstem']} stations, {ms25['mainstem_flow']} with flow",
                 (years[-1], ms25["mainstem"]), xytext=(2003, ms25["mainstem"] + 6),
                 fontsize=10, color=TEXT, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax2.set_ylabel("Main-stem stations", color=MUTED, fontsize=10)
    ax2.set_ylim(0, max(r["mainstem"] for r in rows) * 1.6)
    ax2.legend(loc="upper left", frameon=False, fontsize=10, labelcolor=TEXT)
    ax2.text(1994.8, ax2.get_ylim()[1] * 0.93, "1994", color=MUTED, fontsize=9)
    ax2.set_xlim(years[0], years[-1] + 1)
    fig.text(0.01, 0.01,
             f"Source: Water Survey of Canada HYDAT (Hydat_sqlite3_20260717), stations 02J*/02K*/02L*, "
             f"DLY_FLOWS + DLY_LEVELS, through {years[-1]} (last year fully loaded). Operator class is the one HYDAT records for the station today. "
             "Main stem = station name begins 'Ottawa River' / 'Outaouais'.",
             fontsize=8, color=MUTED)
    plt.tight_layout(rect=(0, 0.03, 1, 1))
    FIG_OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIG_OUT, dpi=140, facecolor=fig.get_facecolor())
    print(f"wrote {FIG_OUT}")


if __name__ == "__main__":
    main()
