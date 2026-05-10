#!/usr/bin/env python3
"""
V1 — Pre-freshet seasonal probability forecast for Lac Coulonge.

Given basin-mean peak snowpack and cold-season precipitation
accumulated to date, returns the probability that this year's Lac
Coulonge annual peak will cross each property / vigilance threshold,
based on historical analog matching against the 1972-2026 record.

This is a SEASONAL prior — it answers "based on snowpack and winter
precip, what's the chance the lake hits each threshold this freshet?"
It does NOT incorporate during-freshet level trajectories or rain
forecasts (those are V2 — see GitHub issue).

Method:
    1. For each historical year, compute (snowpack, cold-season precip,
       annual peak).
    2. For the current year's input state, compute Gaussian-kernel
       similarity weights to every historical year, normalized by a
       per-variable bandwidth (1 standard deviation of the historical
       distribution).
    3. Apply an era multiplier — post-2017 years count more heavily
       because they reflect current operating regime (the case file
       documents a 2017 step-change in operating practice).
    4. For each threshold T, the probability of crossing is the
       sum-weight of historical years that crossed T divided by the
       sum-weight of all historical years.
    5. Returns a dict {threshold_m: probability}.

Honest limits:
    - 55 years of data → tail probabilities (super-flood) carry ±10
      percentage points of statistical noise. Don't read single-percent
      precision into the output.
    - Operations introduce variance not captured in pure climate inputs.
      Two years with identical snowpack + precip can produce different
      peaks depending on operator decisions.
    - Pre-2017 vs post-2017 weighting is a value judgment, not a
      derived quantity. Default 3× post-2017 is a reasonable starting
      point; sensitivity analysis is in the print output.

Usage:
    # Retrospective for 2026 (run in March-2026 hindsight):
    python3 freshet_probability.py --year 2026

    # Custom inputs:
    python3 freshet_probability.py --snowpack 65 --cold-precip 280

Stdlib only.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from statistics import mean, stdev

ROOT = Path(__file__).resolve().parents[2]
PEAKS_CSV = ROOT / "data" / "lac-coulonge-monthly-1972-2026.csv"
ECCC_DIR = ROOT / "data" / "eccc-climate"

# Same upper-basin stations as snowpack_overlay_analysis.py — causally
# upstream of Lac Coulonge.
STATIONS = [
    ("val-dor-a", "daily-1972-2025.csv"),
    ("parent", "daily-1972-2026.csv"),
    ("barrage-temiscamingue", "daily-1972-2026.csv"),
]

# Property and Vigilance thresholds for Lac Coulonge (m, station 1195).
THRESHOLDS = [
    (107.50, "minor flood (Vigilance)"),
    (108.00, "moderate flood (Vigilance)"),
    (108.30, "water approaching property"),
    (108.48, "water in backyard"),
    (108.50, "super-flood threshold (case-file)"),
    (108.75, "cottage bricks"),
    (109.01, "water inside cottage"),
    (109.17, "2019 record"),
]

# Post-2017 operating-regime weight multiplier. The case file documents
# a step-change in Bryson operating practice at 2017; post-2017 years
# better reflect the current operating regime than pre-2017 years.
DEFAULT_POST_2017_WEIGHT = 3.0


def load_peaks() -> dict[int, float]:
    out = {}
    with PEAKS_CSV.open() as f:
        for row in csv.DictReader(f):
            v = row.get("daily_max")
            if v and v.upper() != "NA":
                try:
                    out[int(row["year"])] = float(v)
                except ValueError:
                    continue
    return out


def per_year_climate(year: int) -> dict:
    """Returns basin-mean peak snowpack (Feb-Mar max Snow-on-Ground)
    and basin-mean cold-season precipitation (Nov of year-1 through Feb
    of year, inclusive) across upper-basin ECCC stations."""
    sog_per_station = []
    cold_per_station = []
    for slug, csv_name in STATIONS:
        path = ECCC_DIR / slug / csv_name
        if not path.exists():
            continue
        sog_feb_mar = []
        cold_precip = []
        with path.open(encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                try:
                    y = int(r["Year"])
                    m = int(r["Month"])
                except (KeyError, ValueError, TypeError):
                    continue
                # Snow-on-ground in Feb-Mar of target year
                if y == year and m in (2, 3):
                    sog = (r.get("Snow on Grnd (cm)") or "").strip()
                    if sog:
                        try: sog_feb_mar.append(float(sog))
                        except ValueError: pass
                # Cold-season precip: Nov of year-1 through Feb of year
                if (y == year - 1 and m in (11, 12)) or (y == year and m in (1, 2)):
                    p = (r.get("Total Precip (mm)") or "").strip()
                    if p:
                        try: cold_precip.append(float(p))
                        except ValueError: pass
        # Coverage thresholds
        if len(sog_feb_mar) >= 30:
            sog_per_station.append(max(sog_feb_mar))
        if len(cold_precip) >= 90:  # ~120 days expected, allow some gaps
            cold_per_station.append(sum(cold_precip))
    return {
        "peak_sog_cm": mean(sog_per_station) if sog_per_station else None,
        "cold_precip_mm": mean(cold_per_station) if cold_per_station else None,
        "n_stations_sog": len(sog_per_station),
        "n_stations_cold": len(cold_per_station),
    }


def build_history(min_year: int = 1972, max_year: int = 2026) -> list[dict]:
    """Returns list of {year, peak, snowpack, cold_precip} for every
    year with all three values available."""
    peaks = load_peaks()
    out = []
    for year in range(min_year, max_year + 1):
        if year not in peaks:
            continue
        c = per_year_climate(year)
        if c["peak_sog_cm"] is None or c["cold_precip_mm"] is None:
            continue
        out.append({
            "year": year,
            "peak_m": peaks[year],
            "peak_sog_cm": c["peak_sog_cm"],
            "cold_precip_mm": c["cold_precip_mm"],
        })
    return out


def compute_probabilities(
    snowpack_cm: float,
    cold_precip_mm: float,
    history: list[dict],
    exclude_year: int | None = None,
    post_2017_weight: float = DEFAULT_POST_2017_WEIGHT,
) -> dict:
    """For the given (snowpack, cold_precip) input state, return P(peak >= T)
    for every threshold in THRESHOLDS, computed as Gaussian-kernel-weighted
    fraction of historical years that crossed each threshold.

    `exclude_year`: leave-one-out — when running retrospective for year Y,
    exclude year Y from the historical set so we're not predicting Y from
    Y itself.
    """
    yrs = [h for h in history if h["year"] != exclude_year]
    if not yrs:
        return {"error": "no historical data"}

    # Bandwidth = 1 SD of each variable in history
    sog_sd = stdev([h["peak_sog_cm"] for h in yrs])
    cold_sd = stdev([h["cold_precip_mm"] for h in yrs])

    weights = []
    for h in yrs:
        # Gaussian kernel in normalized 2D space
        d_sog = (h["peak_sog_cm"] - snowpack_cm) / sog_sd
        d_cold = (h["cold_precip_mm"] - cold_precip_mm) / cold_sd
        d2 = d_sog * d_sog + d_cold * d_cold
        w = math.exp(-d2 / 2)
        # Era multiplier — post-2017 years count more heavily
        if h["year"] >= 2017:
            w *= post_2017_weight
        weights.append(w)

    total_weight = sum(weights)
    if total_weight == 0:
        return {"error": "zero total weight"}

    probs = {}
    for thresh, label in THRESHOLDS:
        crossed_weight = sum(
            w for h, w in zip(yrs, weights) if h["peak_m"] >= thresh
        )
        probs[thresh] = crossed_weight / total_weight

    # Top analogs — for inspection
    sorted_pairs = sorted(zip(yrs, weights), key=lambda p: -p[1])[:8]
    top_analogs = [
        {
            "year": p[0]["year"],
            "weight": round(p[1], 3),
            "snowpack_cm": p[0]["peak_sog_cm"],
            "cold_precip_mm": round(p[0]["cold_precip_mm"], 1),
            "peak_m": p[0]["peak_m"],
        }
        for p in sorted_pairs
    ]

    return {
        "input": {"snowpack_cm": snowpack_cm, "cold_precip_mm": round(cold_precip_mm, 1)},
        "n_history_years": len(yrs),
        "post_2017_weight": post_2017_weight,
        "probabilities": {
            f"{t:.2f}": {"prob": round(p, 3), "label": label}
            for (t, label), p in zip(THRESHOLDS, [probs[t] for t, _ in THRESHOLDS])
        },
        "top_analogs": top_analogs,
    }


def retrospective_calibration(history: list[dict]) -> None:
    """Leave-one-out calibration check — for each historical year,
    predict probabilities using the OTHER years' data, then compare
    predicted probability to actual outcome (crossed / didn't)."""
    print("=" * 78)
    print("RETROSPECTIVE CALIBRATION — leave-one-out")
    print("=" * 78)
    print(f"{'year':>6} {'pk_m':>7} {'snow':>5} {'cold':>5} | "
          f"{'P(108.5)':>10} {'P(108.0)':>10} {'P(107.5)':>10}")
    print("-" * 78)

    # Compute LOO probabilities at three key thresholds
    crossed_at_p_bins = {0.5: {"yes": 0, "no": 0}, 0.85: {"super-yes": 0, "super-no": 0}}
    for h in history:
        result = compute_probabilities(
            snowpack_cm=h["peak_sog_cm"],
            cold_precip_mm=h["cold_precip_mm"],
            history=history,
            exclude_year=h["year"],
        )
        p_super = result["probabilities"]["108.50"]["prob"]
        p_mod = result["probabilities"]["108.00"]["prob"]
        p_minor = result["probabilities"]["107.50"]["prob"]
        actual_super = "✓" if h["peak_m"] >= 108.5 else " "
        actual_mod = "✓" if h["peak_m"] >= 108.0 else " "
        actual_minor = "✓" if h["peak_m"] >= 107.5 else " "
        print(f"{h['year']:>6} {h['peak_m']:>7.2f} {h['peak_sog_cm']:>5.0f} "
              f"{h['cold_precip_mm']:>5.0f} | "
              f"  {p_super:>5.0%}{actual_super:>2} "
              f"  {p_mod:>5.0%}{actual_mod:>2} "
              f"  {p_minor:>5.0%}{actual_minor:>2}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, help="Run as if predicting this year (uses leave-one-out)")
    ap.add_argument("--snowpack", type=float, help="Override basin-mean peak snowpack (cm)")
    ap.add_argument("--cold-precip", type=float, help="Override basin-mean cold-season precip (mm)")
    ap.add_argument("--post-2017-weight", type=float, default=DEFAULT_POST_2017_WEIGHT)
    ap.add_argument("--retrospective", action="store_true", help="Run leave-one-out calibration check across all years")
    ap.add_argument("--json", action="store_true", help="Output JSON only (for dashboard consumption)")
    args = ap.parse_args()

    print("Loading historical record…")
    history = build_history()
    print(f"  {len(history)} years with complete (peak, snowpack, cold-precip) data")

    if args.retrospective:
        retrospective_calibration(history)
        return

    # Single prediction
    if args.snowpack is not None and args.cold_precip is not None:
        snow, cold = args.snowpack, args.cold_precip
        excl = None
        label = f"custom inputs"
    elif args.year is not None:
        c = per_year_climate(args.year)
        if c["peak_sog_cm"] is None or c["cold_precip_mm"] is None:
            print(f"ERROR: incomplete climate data for {args.year}")
            return
        snow, cold = c["peak_sog_cm"], c["cold_precip_mm"]
        excl = args.year
        label = f"retrospective for {args.year}"
    else:
        # Default: most recent year in history
        latest = max(h["year"] for h in history)
        c = per_year_climate(latest)
        snow, cold = c["peak_sog_cm"], c["cold_precip_mm"]
        excl = latest
        label = f"retrospective for {latest} (default)"

    result = compute_probabilities(snow, cold, history, exclude_year=excl, post_2017_weight=args.post_2017_weight)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(f"\nFreshet probability forecast — {label}")
    print(f"Inputs: snowpack {snow:.1f} cm | cold-season precip {cold:.1f} mm")
    print(f"Era weight: post-2017 years × {args.post_2017_weight}")
    print(f"History size: {result['n_history_years']} years")

    print(f"\n{'Threshold (m)':<14}  {'Probability':>11}  {'Label'}")
    print("-" * 70)
    for t_str, info in result["probabilities"].items():
        print(f"  {t_str:<11}  {info['prob']:>10.0%}  {info['label']}")

    print(f"\nTop analogs:")
    print(f"  {'year':>6}  {'weight':>7}  {'snow':>5}  {'cold':>5}  {'peak':>7}")
    for a in result["top_analogs"]:
        era = "post-2017" if a["year"] >= 2017 else "pre-2017"
        print(f"  {a['year']:>6}  {a['weight']:>7.3f}  {a['snowpack_cm']:>5.0f}  {a['cold_precip_mm']:>5.0f}  {a['peak_m']:>7.2f}  ({era})")

    # If we have an actual outcome (retrospective), show it
    if excl is not None:
        peaks = load_peaks()
        if excl in peaks:
            actual = peaks[excl]
            print(f"\nActual {excl} peak: {actual:.2f} m — crossed:")
            for t_str, info in result["probabilities"].items():
                t = float(t_str)
                crossed = "✓" if actual >= t else "✗"
                print(f"  {t_str:<11}  {crossed}  ({info['prob']:.0%} predicted)")


if __name__ == "__main__":
    main()
