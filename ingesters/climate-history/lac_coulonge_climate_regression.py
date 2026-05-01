#!/usr/bin/env python3
"""
Re-derives the climate-vs-peak regression for Lac Coulonge.

Method:
1. Per "freshet year" (Nov of year N-1 through Apr of year N), sum Ottawa CDA
   daily precipitation. This is "cold-season precipitation" in mm.
2. Pair with that year's Lac Coulonge annual peak (daily_max).
3. Train OLS on the pre-regime era (freshet years 1972-2016, N=45).
4. Predict each 2017-2026 peak from its cold-season precip; residual is
   actual peak minus predicted peak (in cm).

Stdlib only.
"""

from __future__ import annotations
import csv
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PEAKS_CSV = ROOT / "data" / "lac-coulonge-monthly-1972-2026.csv"
OTTAWA_CSV = ROOT / "data" / "eccc-climate" / "ottawa-cda" / "daily-1972-2026.csv"


def load_peaks():
    peaks = {}
    with PEAKS_CSV.open() as f:
        for row in csv.DictReader(f):
            v = row.get("daily_max")
            if v and v.upper() != "NA":
                peaks[int(row["year"])] = float(v)
    return peaks


def load_ottawa_daily_precip():
    """Returns dict[(year, month, day)] = total_precip_mm (or None if missing)."""
    out = {}
    with OTTAWA_CSV.open(encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                y = int(row["Year"]); m = int(row["Month"]); d = int(row["Day"])
            except (ValueError, KeyError, TypeError):
                continue
            v = row.get("Total Precip (mm)")
            if v and v.strip():
                try:
                    out[(y, m, d)] = float(v)
                except ValueError:
                    pass
    return out


def cold_season_total(daily_precip: dict, freshet_year: int) -> tuple[float, int]:
    """Sum Nov-of-(N-1) through Apr-of-N. Returns (total_mm, days_with_data)."""
    total = 0.0
    n = 0
    for m in (11, 12):
        for d in range(1, 32):
            v = daily_precip.get((freshet_year - 1, m, d))
            if v is not None:
                total += v
                n += 1
    for m in (1, 2, 3, 4):
        for d in range(1, 32):
            v = daily_precip.get((freshet_year, m, d))
            if v is not None:
                total += v
                n += 1
    return total, n


def ols(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    syy = sum((y - my) ** 2 for y in ys)
    b = sxy / sxx
    a = my - b * mx
    r2 = (sxy ** 2) / (sxx * syy) if syy > 0 else 0.0
    return a, b, r2


def main():
    peaks = load_peaks()
    daily = load_ottawa_daily_precip()

    rows = []
    for year in sorted(peaks):
        total, n = cold_season_total(daily, year)
        rows.append({
            "year": year, "peak_m": peaks[year],
            "cold_precip_mm": total, "obs_days": n,
        })

    print("# Lac Coulonge — climate regression (re-derived from canonical data)")
    print("Source: ECCC Ottawa CDA daily Total Precip + ORRPB Lac Coulonge daily_max.")
    print("Cold-season window: Nov(N-1) through Apr(N). N is the freshet year.\n")

    train = [r for r in rows if r["year"] <= 2016 and r["obs_days"] >= 150]
    test = [r for r in rows if r["year"] >= 2017]

    print(f"Training: {len(train)} years (1972-2016 with ≥150 days obs)")
    print(f"Test:     {len(test)} years (2017-{max(r['year'] for r in test)})\n")

    xs = [r["cold_precip_mm"] for r in train]
    ys = [r["peak_m"] for r in train]
    a, b, r2 = ols(xs, ys)
    train_mean_precip = sum(xs) / len(xs)
    train_mean_peak = sum(ys) / len(ys)
    train_sd_precip = statistics.stdev(xs)

    print(f"Pre-regime mean cold-season precip: {train_mean_precip:.1f} mm (sd {train_sd_precip:.1f})")
    print(f"Pre-regime mean peak:               {train_mean_peak:.3f} m")
    print(f"OLS:  peak = {a:.4f} + {b:.6f} * precip   (r² = {r2:.3f})\n")

    test_precip = [r["cold_precip_mm"] for r in test]
    test_mean_precip = sum(test_precip) / len(test_precip)
    test_sd_precip = statistics.stdev(test_precip) if len(test_precip) > 1 else 0
    pct = (test_mean_precip - train_mean_precip) / train_mean_precip * 100
    se = (train_sd_precip ** 2 / len(xs) + test_sd_precip ** 2 / len(test_precip)) ** 0.5
    t_precip = (test_mean_precip - train_mean_precip) / se if se > 0 else float('nan')
    print(f"Post-regime mean cold-season precip: {test_mean_precip:.1f} mm  ({pct:+.1f}% vs baseline)")
    print(f"  Welch's t (precip): {t_precip:.2f}\n")

    print("Per-year residuals (actual peak − precip-predicted peak):")
    print(f"  {'year':<6}{'precip mm':>12}{'predicted m':>14}{'actual m':>12}{'residual cm':>14}{'super-flood':>13}")
    residuals = []
    super_flood_threshold = 108.50
    for r in test:
        pred = a + b * r["cold_precip_mm"]
        resid_cm = (r["peak_m"] - pred) * 100
        is_sf = r["peak_m"] >= super_flood_threshold
        residuals.append((r["year"], resid_cm, is_sf))
        marker = " ★" if is_sf else ""
        print(f"  {r['year']:<6}{r['cold_precip_mm']:>12.1f}{pred:>14.3f}{r['peak_m']:>12.3f}{resid_cm:>14.1f}{marker:>13}")

    avg_resid = sum(rr[1] for rr in residuals) / len(residuals)
    print(f"\nMean residual across {len(residuals)} post-regime years: {avg_resid:+.1f} cm")
    sf_resids = [rr[1] for rr in residuals if rr[2]]
    print(f"Super-flood years ({len(sf_resids)}): mean residual {sum(sf_resids)/len(sf_resids):+.1f} cm")
    nonsf = [rr[1] for rr in residuals if not rr[2]]
    if nonsf:
        print(f"Non-super-flood years ({len(nonsf)}): mean residual {sum(nonsf)/len(nonsf):+.1f} cm")

    print("\n# JS array for Exhibit E Figure 8:")
    print("const residuals = [")
    for r in test:
        pred = a + b * r["cold_precip_mm"]
        resid_cm = round((r["peak_m"] - pred) * 100)
        is_sf = r["peak_m"] >= super_flood_threshold
        print(f"  {{ year: {r['year']}, value: {resid_cm:+d}, sf: {str(is_sf).lower()} }},")
    print("];")


if __name__ == "__main__":
    main()
