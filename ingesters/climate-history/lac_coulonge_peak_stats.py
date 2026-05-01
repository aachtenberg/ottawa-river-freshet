#!/usr/bin/env python3
"""
Re-derives decade-by-decade and 5-year rolling-window statistics for Lac
Coulonge annual peaks, using the canonical CSV (data/lac-coulonge-monthly-
1972-2025.csv) as the source of truth.

The previous web-client analysis used a Python peaks dict that diverged
from the CSV at several years (notably 1985/1986). This script gives the
authoritative numbers for inclusion in Freshet_2026_Complete_Summary.md.

The 2026 peak (108.633 m on 2026-04-20, per the summary doc) is added
in-memory; it is NOT yet in the CSV — the CSV needs a 2026 row.

Stdlib only. Prints a markdown report to stdout.
"""

from __future__ import annotations
import csv
import math
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "lac-coulonge-monthly-1972-2026.csv"
# 2026 peak (108.633 m on 2026-04-20) was added to the CSV in May 2026;
# other 2026 monthly columns are NA pending ORRPB's annual summary.


def load_peaks():
    peaks = {}
    with CSV_PATH.open() as f:
        for row in csv.DictReader(f):
            year = int(row["year"])
            v = row.get("daily_max")
            if v and v.upper() != "NA":
                peaks[year] = float(v)
    return dict(sorted(peaks.items()))


def decade_table(peaks):
    """Same period bins as the analysis in the summary doc."""
    bins = [
        ("1972-1979", range(1972, 1980)),
        ("1980s",     range(1980, 1990)),
        ("1990s",     range(1990, 2000)),
        ("2000s",     range(2000, 2010)),
        ("2010-2016", range(2010, 2017)),
        ("2017-2026", range(2017, 2027)),
    ]
    rows = []
    for label, yrs in bins:
        vals = [peaks[y] for y in yrs if y in peaks]
        if not vals: continue
        rows.append((label, len(vals), statistics.mean(vals), statistics.median(vals), min(vals), max(vals)))
    return rows


def rolling5(peaks):
    years = sorted(peaks)
    out = []
    for i in range(len(years) - 4):
        window = years[i:i+5]
        vals = [peaks[y] for y in window]
        out.append((f"{window[0]}-{window[-1]}", statistics.mean(vals)))
    return out


def welch_t(a, b):
    """Welch's t-test (unequal variances). Returns (t, df, two-sided p approx)."""
    na, nb = len(a), len(b)
    ma, mb = statistics.mean(a), statistics.mean(b)
    va, vb = statistics.variance(a), statistics.variance(b)
    se = math.sqrt(va / na + vb / nb)
    t = (mb - ma) / se
    df = (va / na + vb / nb) ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
    # crude two-sided p via Student-t survival; use normal approx for df>30, else table-ish
    # for df ~10-50 the normal approx is rough; we'll just print t and df and let the reader judge
    return t, df


def main():
    peaks = load_peaks()
    print(f"# Lac Coulonge annual peaks — re-derived from canonical CSV")
    print()
    print(f"Source: `{CSV_PATH.relative_to(ROOT)}` ({len(peaks)} years with daily_max).")
    print()

    print("## Decade-by-decade table")
    print()
    print("| Period | N | Mean | Median | Min | Max |")
    print("|---|---:|---:|---:|---:|---:|")
    for label, n, mean, med, lo, hi in decade_table(peaks):
        print(f"| {label} | {n} | {mean:.2f} | {med:.2f} | {lo:.2f} | {hi:.2f} |")
    print()

    print("## 5-year rolling-window means")
    print()
    print("| Window | Mean |")
    print("|---|---:|")
    for label, mean in rolling5(peaks):
        print(f"| {label} | {mean:.2f} |")
    print()

    print("## Pre-2017 vs 2017-2026 (Welch's t-test)")
    print()
    pre = [v for y, v in peaks.items() if y < 2017]
    post = [v for y, v in peaks.items() if y >= 2017]
    pre_mean = statistics.mean(pre)
    post_mean = statistics.mean(post)
    t, df = welch_t(pre, post)
    print(f"- Pre-2017 (1972-2016): N={len(pre)}, mean={pre_mean:.3f} m, sd={statistics.stdev(pre):.3f}")
    print(f"- 2017-2026:            N={len(post)}, mean={post_mean:.3f} m, sd={statistics.stdev(post):.3f}")
    print(f"- Difference: **+{(post_mean - pre_mean)*100:.0f} cm**")
    print(f"- Welch's t = {t:.2f}, df ≈ {df:.1f}")
    # compare to the summary-doc claim
    print()
    print("## Comparison to current summary-doc numbers")
    print()
    print(f"| Statistic | Summary doc (handoff dict) | Canonical CSV (re-derived) |")
    print(f"|---|---:|---:|")
    print(f"| Pre-2017 mean | 107.40 | {pre_mean:.2f} |")
    print(f"| 2017-2026 mean | 108.01 | {post_mean:.2f} |")
    print(f"| Step | +61 cm | +{(post_mean - pre_mean)*100:.0f} cm |")
    print(f"| t-statistic | 2.39 | {t:.2f} |")


if __name__ == "__main__":
    main()
