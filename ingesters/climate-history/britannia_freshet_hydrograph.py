#!/usr/bin/env python3
"""
Britannia spring-hydrograph overlay — "is this freshet big?" the honest way.

Companion to community note data/community-notes/2026-05-12.md. Replaces the
circulating "current flow vs. 30-year median" bar charts (a single post-peak
snapshot against a context-free median) with the climatology view:

  - 10-90th and 25-75th percentile bands of daily flow at the Ottawa River at
    Britannia (WSC 02KF005), 1960-2024
  - the long-term median and the record daily maximum
  - the three modern super-flood years (2017, 2019, 2023)
  - the live 2026 curve (ECCC real-time discharge, daily-averaged)

Britannia (Lac Deschenes) is used because it has the longest continuous *flow*
record in the basin and is the case file's index station; daily Carillon flow
is not public after 1994.

Data sources (no auth, no local files):
  - History/analog years: PostgREST proxy  freshet.xgrunt.com/history/wsc_daily
    station_code 02KF005  (same series the other climate-history scripts
    cross-check against; agrees with HYDAT to ~1 m^3/s)
  - 2026 line: ECCC OGC API  api.weather.gc.ca  collection hydrometric-realtime
    (retains ~30 days; covers the April crest + recession, not the March rise)

Run from the freshet-public/ directory:
    python3 ingesters/climate-history/britannia_freshet_hydrograph.py
Writes data/community-notes/2026-05-12_britannia_hydrograph.png
"""
import datetime as dt
import json
import os
import urllib.request
from collections import defaultdict

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

PG = "https://freshet.xgrunt.com/history/wsc_daily"
OGC = "https://api.weather.gc.ca/collections/hydrometric-realtime/items"
OUT = "data/community-notes/2026-05-12_britannia_hydrograph.png"
STATION = "02KF005"
CLIMO_START, CLIMO_END = 1960, 2024
DOY_LO, DOY_HI = 60, 200  # ~Mar 1 .. mid-Jul
ANALOG = {2017: ("#8e44ad", "2017 super-flood"),
          2019: ("#c0392b", "2019 — record flood"),
          2023: ("#e67e22", "2023 super-flood")}


def get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (freshet-hydrograph)",
        "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch_history():
    rows, offset, page = [], 0, 10000
    while True:
        u = (f"{PG}?station_code=eq.{STATION}&flow_cms=not.is.null"
             f"&select=time,flow_cms&order=time.asc&limit={page}&offset={offset}")
        chunk = get(u)
        rows += chunk
        if len(chunk) < page:
            break
        offset += page
    return {dt.date.fromisoformat(r["time"][:10]): float(r["flow_cms"]) for r in rows}


def fetch_2026():
    rows, offset, page = [], 0, 10000
    while True:
        u = (f"{OGC}?STATION_NUMBER={STATION}&datetime=2026-03-01/2026-12-31"
             f"&limit={page}&offset={offset}&f=json&properties=DATETIME,DISCHARGE")
        feats = get(u).get("features", [])
        rows += feats
        if len(feats) < page:
            break
        offset += page
    by_day = defaultdict(list)
    for f in rows:
        q = f["properties"].get("DISCHARGE")
        if q is None:
            continue
        by_day[dt.date.fromisoformat(f["properties"]["DATETIME"][:10])].append(float(q))
    return {d: float(np.mean(v)) for d, v in by_day.items()}


def doy_series(daily, year):
    xs, ys = [], []
    for d, q in sorted(daily.items()):
        if d.year != year:
            continue
        doy = d.timetuple().tm_yday
        if DOY_LO <= doy <= DOY_HI:
            xs.append(doy)
            ys.append(q)
    return np.array(xs), np.array(ys)


def to_date(doy):  # render on a dummy non-leap year for clean month ticks
    return dt.date(2025, 1, 1) + dt.timedelta(days=int(doy) - 1)


def print_thread_followup(hist, cur):
    """Numbers backing the "Follow-up" section of the community note:
    peak ranking, freshet-volume ranking, and the median-by-baseline-window
    comparison. All from the same 02KF005 daily series the chart uses."""
    print("\n=== Follow-up numbers (Britannia 02KF005) ===")

    # spring (Apr-Jun) peak daily-mean flow, ranked
    peaks = {}
    for d, q in hist.items():
        if 4 <= d.month <= 6:
            peaks[d.year] = max(peaks.get(d.year, 0.0), q)
    ranked = sorted(peaks.items(), key=lambda kv: -kv[1])
    print("Spring (Apr–Jun) peak daily-mean flow, top 8:")
    for i, (y, v) in enumerate(ranked[:8], 1):
        print(f"  {i:2d}. {y}  {v:,.0f} m³/s")
    r1976 = next((i for i, (y, _) in enumerate(ranked, 1) if y == 1976), None)
    print(f"  (1976 ranks #{r1976})")
    if cur:
        cpk = max(cur.values())
        print(f"  2026 crest so far: {cpk:,.0f} m³/s → would rank "
              f"#{sum(1 for v in peaks.values() if v > cpk) + 1}")

    # freshet volume = integral of daily mean flow, Mar 1 – Jun 30, in km³
    vol = defaultdict(float)
    for d, q in hist.items():
        if 3 <= d.month <= 6:
            vol[d.year] += q * 86400.0 / 1e9
    volr = sorted(vol.items(), key=lambda kv: -kv[1])
    print("Freshet volume (∫ daily mean flow, Mar 1 – Jun 30), top 8 + 2023:")
    for i, (y, v) in enumerate(volr[:8], 1):
        print(f"  {i:2d}. {y}  {v:4.1f} km³")
    r2023v = next((i for i, (y, _) in enumerate(volr, 1) if y == 2023), None)
    print(f"  (2023 ranks #{r2023v} by volume at {vol.get(2023, 0):.1f} km³)")
    if cur:
        v26 = sum(q * 86400.0 / 1e9 for d, q in cur.items() if 3 <= d.month <= 6)
        lo = min(d for d in cur if d.month >= 3)
        hi = max(cur)
        v19 = sum(q * 86400.0 / 1e9 for d, q in hist.items()
                  if d.year == 2019 and dt.date(2019, lo.month, lo.day) <= d <= dt.date(2019, hi.month, hi.day))
        print(f"  2026 PARTIAL ({lo} – {hi}): {v26:.1f} km³  | 2019 same window: {v19:.1f} km³")

    # "median for this day" under three baseline windows
    def med(doy, y0, y1):
        v = [q for d, q in hist.items() if y0 <= d.year <= y1 and d.timetuple().tm_yday == doy]
        return float(np.median(v)) if v else float("nan")
    print("'Median for this day' by baseline window (m³/s):")
    for label, mm, dd in [("Apr 22", 4, 22), ("May 1", 5, 1), ("May 12", 5, 12)]:
        doy = dt.date(2025, mm, dd).timetuple().tm_yday
        print(f"  {label:<7} full(1960-2024)={med(doy,1960,2024):,.0f}  "
              f"WMO(1991-2020)={med(doy,1991,2020):,.0f}  recent(2016-2024)={med(doy,2016,2024):,.0f}")
    sf = sorted(y for y, v in peaks.items() if v >= 4500)
    print(f"Spring peaks ≥4500 m³/s — full record: {sf}; "
          f"within 1991-2020: {[y for y in sf if 1991 <= y <= 2020]}; "
          f"pre-1990: {[y for y in sf if y < 1990]}")


def main():
    print("fetching 1960-2024 history ...")
    hist = fetch_history()
    print(f"  {len(hist)} daily values, {min(hist).year}-{max(hist).year}")
    print("fetching 2026 realtime ...")
    cur = fetch_2026()
    print(f"  {len(cur)} days ({min(cur)} .. {max(cur)})" if cur else "  none")

    bucket = defaultdict(list)
    for d, q in hist.items():
        if CLIMO_START <= d.year <= CLIMO_END:
            doy = d.timetuple().tm_yday
            if DOY_LO <= doy <= DOY_HI:
                bucket[doy].append(q)
    doys = np.array(sorted(bucket))
    pct = {p: np.array([np.percentile(bucket[x], p) for x in doys])
           for p in (10, 25, 50, 75, 90)}
    pmax = np.array([np.max(bucket[x]) for x in doys])
    X = np.array([to_date(x) for x in doys])

    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.fill_between(X, pct[10], pct[90], color="#3a7d44", alpha=0.16,
                    label=f"10th–90th percentile ({CLIMO_START}–{CLIMO_END})")
    ax.fill_between(X, pct[25], pct[75], color="#3a7d44", alpha=0.28,
                    label="25th–75th percentile")
    ax.plot(X, pct[50], color="#2e7d32", lw=2.2, label=f"Median ({CLIMO_START}–{CLIMO_END})")
    ax.plot(X, pmax, color="#9e9e9e", lw=1.0, ls=":", label="Record daily max")

    for yr, (c, lab) in ANALOG.items():
        xs, ys = doy_series(hist, yr)
        if len(xs):
            ax.plot([to_date(x) for x in xs], ys, color=c, lw=1.6, alpha=0.9, label=lab)

    if cur:
        xs, ys = doy_series(cur, 2026)
        if len(xs):
            ax.plot([to_date(x) for x in xs], ys, color="#1565c0", lw=3.2,
                    label="2026 (live, last ~30 d, daily mean)", zorder=10)
            ip = int(np.argmax(ys))
            ax.scatter([to_date(xs[ip])], [ys[ip]], color="#1565c0", s=45, zorder=11)
            ax.annotate(f"2026 peak so far\n~{ys[ip]:,.0f} m³/s ({to_date(xs[ip]):%b %d})",
                        (to_date(xs[ip]), ys[ip]), xytext=(8, 6),
                        textcoords="offset points", color="#1565c0",
                        fontsize=8.5, fontweight="bold", va="bottom")
            ax.scatter([to_date(xs[-1])], [ys[-1]], color="#1565c0", s=55, zorder=11)
            ax.annotate(f"  {ys[-1]:,.0f} ({to_date(xs[-1]):%b %d})",
                        (to_date(xs[-1]), ys[-1]), color="#1565c0",
                        fontsize=8.5, fontweight="bold", va="center")

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    ax.set_xlim(to_date(DOY_LO), to_date(DOY_HI))
    ax.set_ylim(0, None)
    ax.set_ylabel("Daily mean flow (m³/s)")
    ax.set_title("Ottawa River at Britannia — 2026 freshet vs. the 1960–2024 record\n"
                 "Water Survey of Canada station 02KF005", fontsize=13)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    ax.text(0.005, -0.13,
            "Bands / median / record-max: WSC HYDAT daily means 1960–2024 (via freshet.xgrunt.com/history). "
            "2026 line: ECCC real-time discharge, daily-averaged. Analog years are full HYDAT daily series.",
            transform=ax.transAxes, fontsize=7.2, color="#555")
    fig.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, dpi=150, bbox_inches="tight")
    print("wrote", OUT)

    print_thread_followup(hist, cur)


if __name__ == "__main__":
    main()
