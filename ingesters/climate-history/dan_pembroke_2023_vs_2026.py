#!/usr/bin/env python3
"""Dan Poole 2023 vs 2026 sanity check — Pembroke peak shape comparison.

Dan's claim (Facebook thread, May 2026):
  * Des Joachims peak outflow Q matched exactly between 2023 and 2026 (3324 m³/s)
  * Petawawa contributed +65 m³/s more in 2026 than 2023
  * Yet Pembroke peak level fell 14 cm (113.31 → 113.17 m)
  * Visual hydrograph shape: 2023 = sharp upward rise; 2026 = incremental smaller rises
  * Implication: rate-of-rise / hydrograph shape matters beyond peak Q

What we can audit publicly:
  - Pembroke daily level history (ORRPB per-location history — same form-scrape)
  - Des Joachims headpond level history (already in our ORRPB archive — proxy for
    DJ outflow gate operations, not flow itself)
  - Petawawa daily flow (WSC HYDAT for 2023; WSC real-time CSV for 2026)

What we can NOT audit:
  - Des Joachims OUTFLOW (cms) — OPG-internal, not in any public feed we have
  - The exact 3324 m³/s figure Dan cites for both years

Outputs:
  data/community-notes/2026-05-23_dan_pembroke_2023_vs_2026.png
  data/community-notes/2026-05-23_dan_pembroke_2023_vs_2026_summary.txt
"""
from __future__ import annotations
import csv
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from datetime import date as D
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
ORRPB_CSV = ROOT / "data" / "orrpb-location-history" / "orrpb_location_daily.csv"
HYDAT_DB = Path("/tmp/hydat/Hydat.sqlite3")
OUTDIR = ROOT / "data" / "community-notes"
STAMP = "2026-05-23"
USER_AGENT = "freshet/1.0 (+https://github.com/aachtenberg/ottawa-river-freshet)"

# --- ORRPB Pembroke daily level ---------------------------------------------

def fetch_orrpb_location(slug: str, y_from: int, y_to: int) -> dict:
    """{date_iso -> level_m} for Observed row."""
    cache = ROOT / "data" / "orrpb-location-history" / "raw" / f"{slug}_{y_from}_{y_to}.html"
    if cache.exists() and cache.stat().st_size > 1000:
        html = cache.read_text(encoding="utf-8", errors="replace")
    else:
        body = urllib.parse.urlencode({
            "data-type": "daily",
            "date-start": f"{y_from}-01-01",
            "date-end": f"{y_to}-12-31",
            "data-display": "table",
        }).encode("utf-8")
        req = urllib.request.Request(
            f"https://www.ottawariver.ca/location/{slug}/",
            data=body, method="POST",
            headers={"User-Agent": USER_AGENT,
                     "Content-Type": "application/x-www-form-urlencoded"})
        with urllib.request.urlopen(req, timeout=60) as r:
            html = r.read().decode("utf-8", errors="replace")
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(html, encoding="utf-8")
        time.sleep(1.0)

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
    dates = header[1:]
    by_label: dict[str, list[str]] = {}
    for r in rows[1:]:
        cs = cells(r)
        if not cs:
            continue
        by_label[re.sub(r"\s+", " ", cs[0]).strip().lower()] = cs[1:]
    obs = by_label.get("observed", [])
    out: dict[str, float] = {}
    for i, d in enumerate(dates):
        if i >= len(obs):
            break
        s = re.sub(r"\s+", " ", obs[i]).strip()
        mm = re.match(r"^([\d.]+)", s)
        if mm:
            try:
                out[d] = float(mm.group(1))
            except ValueError:
                pass
    return out


# --- Petawawa daily flow from HYDAT -----------------------------------------

def hydat_daily_flow(station: str, year: int) -> dict:
    """{date_iso -> flow_cms} for a station-year."""
    if not HYDAT_DB.exists():
        return {}
    db = sqlite3.connect(HYDAT_DB)
    rows = db.execute(
        "SELECT MONTH, " + ",".join(f"FLOW{i}" for i in range(1, 32)) +
        " FROM DLY_FLOWS WHERE STATION_NUMBER=? AND YEAR=? ORDER BY MONTH",
        (station, year)).fetchall()
    out: dict[str, float] = {}
    for r in rows:
        month = r[0]
        for day, v in enumerate(r[1:], start=1):
            if v is None:
                continue
            try:
                d = D(year, month, day)
            except ValueError:
                continue
            out[d.isoformat()] = float(v)
    return out


# --- Petawawa real-time (2026) ---------------------------------------------

def wsc_realtime_daily_flow(station: str, start: str, end: str) -> dict:
    """{date_iso -> mean daily flow cms} from the real-time CSV endpoint.
    Aggregates 5-min observations to daily mean."""
    params = {
        "stations[]": station,
        "parameters[]": "47",
        "start_date": f"{start} 00:00:00",
        "end_date": f"{end} 23:59:59",
    }
    qs = urllib.parse.urlencode(params).replace("%5B%5D", "[]")
    url = f"https://wateroffice.ec.gc.ca/services/real_time_data/csv/inline?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        txt = r.read().decode("utf-8", errors="replace")
    by_day: dict[str, list[float]] = {}
    for line in txt.splitlines()[1:]:
        if not line:
            continue
        parts = line.split(",")
        if len(parts) < 4:
            continue
        ts = parts[1]
        try:
            v = float(parts[3])
        except ValueError:
            continue
        d = ts[:10]
        by_day.setdefault(d, []).append(v)
    return {d: float(np.mean(vs)) for d, vs in by_day.items()}


# --- Des Joachims headpond level from local archive -------------------------

def load_des_joachims_levels() -> dict:
    """{date_iso -> level_m}."""
    out: dict[str, float] = {}
    with open(ORRPB_CSV) as f:
        for r in csv.DictReader(f):
            if r["reservoir_id"] != "des_joachims":
                continue
            if not r["level_m"]:
                continue
            try:
                out[r["date"]] = float(r["level_m"])
            except ValueError:
                pass
    return out


def window(series: dict, year: int) -> tuple[list, list]:
    xs, ys = [], []
    for d, v in series.items():
        dt = D.fromisoformat(d)
        if dt.year == year and 3 <= dt.month <= 6:
            xs.append(dt)
            ys.append(v)
    pairs = sorted(zip(xs, ys))
    return [p[0] for p in pairs], [p[1] for p in pairs]


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)

    print("Fetching ORRPB Pembroke 2023…")
    pem23 = fetch_orrpb_location("pembroke", 2023, 2023)
    print(f"  {len(pem23)} days")
    print("Fetching ORRPB Pembroke 2026…")
    pem26 = fetch_orrpb_location("pembroke", 2024, 2026)
    print(f"  {len(pem26)} days (filtering to 2026)")
    pem26 = {d: v for d, v in pem26.items() if d.startswith("2026")}
    print(f"  {len(pem26)} days in 2026")

    print("Loading Des Joachims headpond from local archive…")
    dj = load_des_joachims_levels()
    print(f"  {len(dj)} days total (archive ends 2025)")
    # Local archive ends 2025; fetch DJ 2026 directly from ORRPB.
    print("Fetching Des Joachims 2026 from ORRPB…")
    dj26 = fetch_orrpb_location("des-joachims", 2024, 2026)
    for d, v in dj26.items():
        if d.startswith("2026"):
            dj[d] = v
    print(f"  added {sum(1 for d in dj if d.startswith('2026'))} 2026 days")

    print("Pulling Petawawa flow — 2023 from HYDAT…")
    pet23 = hydat_daily_flow("02KB001", 2023)
    print(f"  {len(pet23)} days")
    print("Pulling Petawawa flow — 2026 from WSC real-time…")
    pet26 = wsc_realtime_daily_flow("02KB001", "2026-03-01", "2026-06-15")
    print(f"  {len(pet26)} days")

    # --- find peak day per year, per series
    def peak(xs, ys):
        if not ys:
            return None, None
        i = int(np.argmax(ys))
        return xs[i], ys[i]

    px23, py23 = window(pem23, 2023)
    px26, py26 = window(pem26, 2026)
    dx23, dy23 = window(dj, 2023)
    dx26, dy26 = window(dj, 2026)
    qx23, qy23 = window(pet23, 2023)
    qx26, qy26 = window(pet26, 2026)

    print(f"\n{'='*70}")
    print("Peak values in each series (Mar-Jun window)")
    print(f"{'='*70}")
    for label, x23, y23, x26, y26, unit in [
        ("Pembroke level (m)",      px23, py23, px26, py26, "m"),
        ("Des Joachims level (m)",  dx23, dy23, dx26, dy26, "m"),
        ("Petawawa flow (m³/s)",    qx23, qy23, qx26, qy26, "m³/s"),
    ]:
        d23, v23 = peak(x23, y23)
        d26, v26 = peak(x26, y26)
        diff = (v26 - v23) if (v23 is not None and v26 is not None) else None
        print(f"\n{label}")
        print(f"  2023 peak: {v23 and f'{v23:.2f} {unit}'} on {d23}")
        print(f"  2026 peak: {v26 and f'{v26:.2f} {unit}'} on {d26}")
        if diff is not None:
            print(f"  Δ (2026 − 2023): {diff:+.2f} {unit}")

    # --- rate-of-rise diagnostic
    def rise_rate(xs, ys, days_before_peak=7):
        if len(ys) < 2:
            return None
        i = int(np.argmax(ys))
        j = max(0, i - days_before_peak)
        if j == i:
            return None
        return (ys[i] - ys[j]) / (i - j)

    print(f"\n{'='*70}")
    print("Rate of rise — 7 days into the peak (m/day or cms/day)")
    print(f"{'='*70}")
    for label, x23, y23, x26, y26, unit in [
        ("Pembroke level",      px23, py23, px26, py26, "m/day"),
        ("Des Joachims level",  dx23, dy23, dx26, dy26, "m/day"),
        ("Petawawa flow",       qx23, qy23, qx26, qy26, "cms/day"),
    ]:
        r23 = rise_rate(x23, y23)
        r26 = rise_rate(x26, y26)
        print(f"\n{label}")
        print(f"  2023: {r23 and f'{r23:+.3f} {unit}'}")
        print(f"  2026: {r26 and f'{r26:+.3f} {unit}'}")

    # --- plot
    fig, axes = plt.subplots(3, 1, figsize=(11, 11), sharex=False)
    for ax, (title, x23, y23, x26, y26, unit) in zip(axes, [
        ("Pembroke — daily level (m)",  px23, py23, px26, py26, "m"),
        ("Des Joachims — headpond level (m)", dx23, dy23, dx26, dy26, "m"),
        ("Petawawa River near Petawawa — daily flow (m³/s)",
         qx23, qy23, qx26, qy26, "m³/s"),
    ]):
        # plot both years overlaid on same day-of-year x-axis
        if x23:
            doys = [(d - D(2023, 1, 1)).days for d in x23]
            ax.plot(doys, y23, "-", color="#cc3a21", label="2023", linewidth=1.6)
            i = int(np.argmax(y23))
            ax.plot(doys[i], y23[i], "o", color="#cc3a21", markersize=8,
                    markeredgecolor="k")
        if x26:
            doys = [(d - D(2026, 1, 1)).days for d in x26]
            ax.plot(doys, y26, "-", color="#2c6aa0", label="2026", linewidth=1.6)
            i = int(np.argmax(y26))
            ax.plot(doys[i], y26[i], "o", color="#2c6aa0", markersize=8,
                    markeredgecolor="k")
        ax.set_title(title)
        ax.set_ylabel(unit)
        ax.legend(loc="upper left")
        ax.grid(alpha=0.3)
        # x-axis: month labels
        ax.set_xticks([(D(2023, m, 1) - D(2023, 1, 1)).days for m in range(3, 7)])
        ax.set_xticklabels(["Mar", "Apr", "May", "Jun"])
        ax.set_xlim(58, 180)

    fig.suptitle("Dan Poole's 2023 vs 2026 comparison — Pembroke, Des Joachims, Petawawa\n"
                 "(public-data audit; Des Joachims outflow Q is operator-internal)",
                 fontsize=11)
    fig.tight_layout()
    out_png = OUTDIR / f"{STAMP}_dan_pembroke_2023_vs_2026.png"
    fig.savefig(out_png, dpi=120)
    print(f"\nWrote {out_png.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
