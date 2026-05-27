"""
Test Jennifer Buttars' "38 years" claim from a FB thread (2026-05-27).

Her assertion: after the floods of the 1970s, public-safety reforms in the
Ottawa River basin produced ~38 years of relatively flood-free operation
(roughly 1979-2016), and then the post-2017 super-flood cluster broke
that pattern. Her location is *below Carillon* (Hawkesbury / Lake of
Two Mountains reach), which is the case-file constituency most directly
governed by the Carillon directive (Hull > 42.61 m -> 40.08 m ceiling)
and least covered by upstream-focused analysis in the case file to date.

Test:

  - Pull WSC station 02OA039 (Pointe-Calumet, on the Lac des Deux-Montagnes
    reach, below Carillon) daily level series 1915 -> present.
  - Compute the annual freshet-window peak (April 1 - July 31) per year.
  - Compare three periods:
      pre-reform:     1915 - 1976  (62 years)
      management era: 1979 - 2016  (38 years - Jennifer's claim)
      super-flood:    2017 - 2026  (10 years)
  - Run a data-implied breakpoint scan to see where the largest pre/post
    mean shift actually sits (don't assume Jennifer's 1979 / 2017
    endpoints; let the data pick).
  - Report counts of "major flood years" per period using thresholds
    derived from the full-record distribution.

Stdlib + matplotlib only.
"""

from __future__ import annotations
import json, statistics, urllib.request, datetime
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

POSTGREST = "https://freshet.xgrunt.com/history"
STATION = "02OA039"   # Pointe-Calumet, Riviere des Outaouais a Pointe-Calumet
ROOT = Path(__file__).resolve().parents[2]
FIG_OUT = ROOT / "data" / "community-notes" / "figures" / "2026-05-27_pointe_calumet_38yr.png"

# Period definitions per Jennifer's claim
PRE_REFORM_END = 1976       # 1976 was the last major pre-reform flood
MGMT_START     = 1979       # post-reform window starts
MGMT_END       = 2016       # 2017 begins the super-flood cluster
SUPER_START    = 2017
SUPER_END      = 2026       # current

# Freshet window
FRESHET_START_MONTH = 4
FRESHET_END_MONTH   = 7


UA = "Mozilla/5.0 (freshet-case-file/1.0)"


def fetch_daily() -> list[tuple[datetime.date, float]]:
    """Pull full wsc_daily series for STATION via PostgREST."""
    url = f"{POSTGREST}/wsc_daily?station_code=eq.{STATION}&select=time,level_m&limit=50000"
    req = urllib.request.Request(url, headers={
        "Range-Unit": "items", "Range": "0-49999", "User-Agent": UA,
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        rows = json.loads(resp.read())
    out = []
    for r in rows:
        if r["level_m"] is None:
            continue
        d = datetime.date.fromisoformat(r["time"][:10])
        out.append((d, float(r["level_m"])))
    out.sort()
    return out


def fetch_2026_peak() -> tuple[datetime.date, float] | None:
    """Pull 2026 freshet peak from wsc_readings (real-time)."""
    url = (
        f"{POSTGREST}/wsc_readings?station_code=eq.{STATION}"
        f"&time=gte.2026-04-01&time=lte.2026-07-31"
        f"&select=time,level_m&order=level_m.desc&limit=1"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        rows = json.loads(resp.read())
    if not rows or rows[0]["level_m"] is None:
        return None
    d = datetime.date.fromisoformat(rows[0]["time"][:10])
    return d, float(rows[0]["level_m"])


def annual_freshet_peaks(daily: list[tuple[datetime.date, float]]) -> dict[int, tuple[datetime.date, float]]:
    """Max level per year over the freshet window (April-July)."""
    by_year: dict[int, tuple[datetime.date, float]] = {}
    for d, lvl in daily:
        if not (FRESHET_START_MONTH <= d.month <= FRESHET_END_MONTH):
            continue
        prev = by_year.get(d.year)
        if prev is None or lvl > prev[1]:
            by_year[d.year] = (d, lvl)
    return by_year


def period_stats(peaks: dict[int, float], lo: int, hi: int, threshold: float) -> dict:
    vals = [v for y, v in peaks.items() if lo <= y <= hi]
    if not vals:
        return {"n": 0}
    return {
        "n": len(vals),
        "mean": statistics.mean(vals),
        "median": statistics.median(vals),
        "stdev": statistics.stdev(vals) if len(vals) > 1 else 0.0,
        "max": max(vals),
        "max_year": [y for y, v in peaks.items() if lo <= y <= hi and v == max(vals)][0],
        "min": min(vals),
        "n_above_threshold": sum(1 for v in vals if v >= threshold),
        "pct_above_threshold": 100.0 * sum(1 for v in vals if v >= threshold) / len(vals),
    }


def breakpoint_scan(peaks: dict[int, float], yr_lo: int, yr_hi: int,
                    candidate_range=(1970, 2020)) -> list[tuple[int, float, float, float]]:
    """For each candidate breakpoint year y, compute the difference in mean
    between (1915..y-1) and (y..2026). Largest abs(diff) flags the data-
    implied breakpoint."""
    ys = sorted(y for y in peaks.keys() if yr_lo <= y <= yr_hi)
    out = []
    for y_break in range(candidate_range[0], candidate_range[1] + 1):
        pre = [peaks[y] for y in ys if y < y_break]
        post = [peaks[y] for y in ys if y >= y_break]
        if len(pre) < 10 or len(post) < 5:
            continue
        out.append((y_break, statistics.mean(pre), statistics.mean(post),
                    statistics.mean(post) - statistics.mean(pre)))
    return out


def main():
    print(f"Pulling {STATION} (Pointe-Calumet) daily levels...")
    daily = fetch_daily()
    print(f"  {len(daily)} non-null daily observations")
    print(f"  range: {daily[0][0]} -> {daily[-1][0]}")

    peaks = annual_freshet_peaks(daily)
    peak_2026 = fetch_2026_peak()
    if peak_2026:
        peaks[2026] = peak_2026
        print(f"  added 2026 peak from real-time: {peak_2026[1]:.3f} m on {peak_2026[0]}")

    peaks_lvl = {y: v for y, (d, v) in peaks.items()}

    # Identify "major flood" threshold from the full-record top decile
    all_peaks = sorted(peaks_lvl.values(), reverse=True)
    top_decile_cutoff = all_peaks[len(all_peaks) // 10]
    print(f"\nTop-decile flood threshold (90th percentile of full record): {top_decile_cutoff:.3f} m")

    # Three-period stats
    pre = period_stats(peaks_lvl, 1915, PRE_REFORM_END, top_decile_cutoff)
    mgmt = period_stats(peaks_lvl, MGMT_START, MGMT_END, top_decile_cutoff)
    sf = period_stats(peaks_lvl, SUPER_START, SUPER_END, top_decile_cutoff)

    print(f"\n=== Three-period comparison at Pointe-Calumet ({STATION}) ===")
    for label, p in [
        (f"Pre-reform   1915-{PRE_REFORM_END}", pre),
        (f"Management   {MGMT_START}-{MGMT_END} (Jennifer's '38 years')", mgmt),
        (f"Super-flood  {SUPER_START}-{SUPER_END}", sf),
    ]:
        if p["n"] == 0:
            print(f"  {label}: no data")
            continue
        print(f"  {label}: n={p['n']:3d}  mean={p['mean']:.3f} m  median={p['median']:.3f}  "
              f"sd={p['stdev']:.3f}  max={p['max']:.3f} ({p['max_year']})  "
              f"floods>=Q90={p['n_above_threshold']:2d} ({p['pct_above_threshold']:.0f}%)")

    # Data-implied breakpoint
    print(f"\n=== Data-implied breakpoint scan (post-2017 transition) ===")
    bp = breakpoint_scan(peaks_lvl, 1915, SUPER_END, candidate_range=(2000, 2024))
    if bp:
        bp_sorted = sorted(bp, key=lambda r: -abs(r[3]))[:5]
        print("  Top 5 candidates by |mean shift|:")
        for y_break, pre_m, post_m, diff in bp_sorted:
            print(f"    breakpoint {y_break}: pre_mean={pre_m:.3f}  post_mean={post_m:.3f}  "
                  f"diff={diff:+.3f} m")

    print(f"\n=== Data-implied breakpoint scan (1970s reform transition) ===")
    bp2 = breakpoint_scan(peaks_lvl, 1915, MGMT_END, candidate_range=(1965, 1990))
    if bp2:
        bp2_sorted = sorted(bp2, key=lambda r: -abs(r[3]))[:5]
        print("  Top 5 candidates by |mean shift|:")
        for y_break, pre_m, post_m, diff in bp2_sorted:
            print(f"    breakpoint {y_break}: pre_mean={pre_m:.3f}  post_mean={post_m:.3f}  "
                  f"diff={diff:+.3f} m")

    # Plot
    years = sorted(peaks_lvl.keys())
    vals = [peaks_lvl[y] for y in years]

    fig, ax = plt.subplots(figsize=(12, 6))

    # Era shading
    ax.axvspan(1915, PRE_REFORM_END, color="#cccccc", alpha=0.25, label=f"Pre-reform 1915-{PRE_REFORM_END}")
    ax.axvspan(MGMT_START, MGMT_END, color="#86c5da", alpha=0.30, label=f"Management {MGMT_START}-{MGMT_END}")
    ax.axvspan(SUPER_START, SUPER_END, color="#e8895a", alpha=0.35, label=f"Super-flood {SUPER_START}-{SUPER_END}")

    # Era mean lines
    if pre["n"]:
        ax.hlines(pre["mean"], 1915, PRE_REFORM_END, colors="#444444", linewidth=2)
    if mgmt["n"]:
        ax.hlines(mgmt["mean"], MGMT_START, MGMT_END, colors="#1f6f8b", linewidth=2)
    if sf["n"]:
        ax.hlines(sf["mean"], SUPER_START, SUPER_END, colors="#a8431f", linewidth=2)

    # Top-decile threshold
    ax.axhline(top_decile_cutoff, color="#888888", linestyle=":", linewidth=1, alpha=0.6,
               label=f"Q90 flood threshold ({top_decile_cutoff:.2f} m)")

    # Peaks
    ax.plot(years, vals, "o-", color="#222222", markersize=4, linewidth=0.8, alpha=0.85)

    # Highlight years above threshold
    flood_years = [y for y in years if peaks_lvl[y] >= top_decile_cutoff]
    flood_vals = [peaks_lvl[y] for y in flood_years]
    ax.scatter(flood_years, flood_vals, color="#c8362b", zorder=5, s=60,
               edgecolor="black", linewidth=0.5, label="Q90 flood years")

    # Label notable super-flood and pre-reform flood years
    notable = [(y, peaks_lvl[y]) for y in [1974, 1976, 2017, 2019, 2023] if y in peaks_lvl]
    for y, v in notable:
        ax.annotate(f"{y}", (y, v), textcoords="offset points", xytext=(0, 8),
                    ha="center", fontsize=8, color="#444444")

    ax.set_xlabel("Year")
    ax.set_ylabel("Annual freshet peak level (m, local datum)")
    ax.set_title(
        f"Pointe-Calumet (WSC {STATION}, below Carillon)\n"
        f"Annual freshet peak 1915 - {SUPER_END}: testing Jennifer's '38 years of management' claim"
    )
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3)

    # Annotation: period means
    note_lines = []
    if pre["n"]:
        note_lines.append(f"Pre-reform mean: {pre['mean']:.2f} m (Q90 floods {pre['n_above_threshold']}/{pre['n']} = {pre['pct_above_threshold']:.0f}%)")
    if mgmt["n"]:
        note_lines.append(f"Management mean: {mgmt['mean']:.2f} m (Q90 floods {mgmt['n_above_threshold']}/{mgmt['n']} = {mgmt['pct_above_threshold']:.0f}%)")
    if sf["n"]:
        note_lines.append(f"Super-flood mean: {sf['mean']:.2f} m (Q90 floods {sf['n_above_threshold']}/{sf['n']} = {sf['pct_above_threshold']:.0f}%)")
    ax.text(0.99, 0.02, "\n".join(note_lines), transform=ax.transAxes, fontsize=9,
            ha="right", va="bottom", bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.85))

    plt.tight_layout()
    FIG_OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIG_OUT, dpi=140)
    print(f"\nWrote {FIG_OUT}")


if __name__ == "__main__":
    main()
