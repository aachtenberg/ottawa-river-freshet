#!/usr/bin/env python3
"""
Feasibility scout: pre-freshet reservoir state vs subsequent freshet peak.

The Facebook-thread argument (Steve LeGault, May 2026) is that the
chart-author's "DJ volume → Pembroke peak" analysis ignores the
counterfactual on pre-freshet reservoir storage — i.e., the same downstream
peak could be very different if the reservoirs had entered the freshet with
more buffer. This is a separate variable from total volume and from
hydrograph shape (which our companion note "Volume vs Peak Flow at
Pembroke" has already addressed).

This script does *not* attempt a definitive multi-decade answer — the data
to do that doesn't exist in the public record. It assembles what we *can*
reach (April-1 reservoir state for 4 years from Wayback-mined ORRPB
snapshots), computes "% of operating band" per reservoir per year (the same
methodology as the 2026-05-22 community note), and pairs each year with the
subsequent Britannia spring peak. With n = 3-4 paired (state, peak)
observations the result is illustrative rather than conclusive — but it
establishes the methodology and exposes precisely which data we still need.

Inputs:
  - Wayback-mined reservoir CSV  (data/wayback-orrpb-reservoirs/wayback_reservoir_levels.csv)
  - Operating-band JSON          (dashboard/reservoir-limits.json)
  - Britannia daily levels       (data/wsc-hydrometric/britannia-ottawa-river/daily.csv)

Outputs:
  - data/wayback-orrpb-reservoirs/april1_state_by_year.csv   (per-reservoir % of band)
  - data/community-notes/2026-05-23_pre_freshet_*.png        (figures)
  - stdout: text summary

Stack: numpy/matplotlib only (stdlib elsewhere).
"""
from __future__ import annotations
import csv
import json
import collections
from datetime import date as D
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
WAYBACK_CSV = ROOT / "data" / "wayback-orrpb-reservoirs" / "wayback_reservoir_levels.csv"
LIMITS_JSON = ROOT / "dashboard" / "reservoir-limits.json"
BRITANNIA_CSV = ROOT / "data" / "wsc-hydrometric" / "britannia-ottawa-river" / "daily.csv"
OUTDIR_DATA = ROOT / "data" / "wayback-orrpb-reservoirs"
OUTDIR_FIG = ROOT / "data" / "community-notes"
STAMP = "2026-05-23"


def load_wayback():
    rows = []
    with open(WAYBACK_CSV) as f:
        for r in csv.DictReader(f):
            try:
                lvl = float(r["level_m"]) if r["level_m"] else None
            except ValueError:
                lvl = None
            rows.append({"date": r["date"], "reservoir_id": r["reservoir_id"],
                         "level_m": lvl})
    return rows


def load_limits():
    with open(LIMITS_JSON) as f:
        return json.load(f)["reservoirs"]


def load_britannia_spring_peaks():
    """{year -> max spring (Mar–Jun) level (m)}."""
    by_year = collections.defaultdict(list)
    with open(BRITANNIA_CSV) as f:
        for r in csv.DictReader(f):
            lv = r.get("level_m") or ""
            if not lv:
                continue
            try:
                v = float(lv)
            except ValueError:
                continue
            d = D.fromisoformat(r["date"])
            if 3 <= d.month <= 6:
                by_year[d.year].append(v)
    return {y: max(vs) for y, vs in by_year.items() if len(vs) >= 40}


def april1_state(rows, year, window_days=7):
    """{reservoir_id -> (date, level)} nearest April 1 of year, within ±N days."""
    target = D(year, 4, 1)
    candidates = collections.defaultdict(list)
    for r in rows:
        if not r["level_m"]:
            continue
        d = D.fromisoformat(r["date"])
        if d.year != year:
            continue
        gap = (d - target).days
        if abs(gap) <= window_days:
            candidates[r["reservoir_id"]].append((abs(gap), gap, r["date"], r["level_m"]))
    out = {}
    for rid, lst in candidates.items():
        lst.sort()                 # smallest abs-gap first
        _, _, date_str, lvl = lst[0]
        out[rid] = (date_str, lvl)
    return out


def pct_of_band(level, low, high):
    if high == low:
        return None
    return 100.0 * (level - low) / (high - low)


def usable_storage_used_mcm(level, low, high, capacity_mcm):
    """Estimate storage above the operating floor, in Mm³.

    Assumes linear stage-storage between low/high limits — a reasonable
    first-order approximation for the cascade-regulating reservoirs but
    not the precise stage-storage curve (which the operators hold)."""
    if not capacity_mcm or high == low:
        return None
    frac = max(0.0, min(1.0, (level - low) / (high - low)))
    return frac * capacity_mcm


def main():
    OUTDIR_DATA.mkdir(parents=True, exist_ok=True)
    OUTDIR_FIG.mkdir(parents=True, exist_ok=True)

    rows = load_wayback()
    limits = load_limits()
    britannia = load_britannia_spring_peaks()
    print(f"Wayback rows: {len(rows)}")
    print(f"Reservoirs with operating-band limits: {len(limits)}")
    print(f"Britannia spring peaks loaded: {len(britannia)} years "
          f"({min(britannia)}-{max(britannia)})")

    YEARS = [2020, 2021, 2022, 2023, 2024, 2025]

    # ----- collect April-1 state per (year, reservoir)
    print(f"\n{'='*78}\nAPRIL-1 ± 7-DAY STATE BY YEAR\n{'='*78}")
    rows_out = []
    year_totals: dict[int, dict] = {}
    for y in YEARS:
        state = april1_state(rows, y, window_days=7)
        if not state:
            print(f"\n--- {y}: no data within ±7d of April 1 ---")
            continue
        peak = britannia.get(y)
        peak_str = f"{peak:.3f}" if peak else "n/a"
        print(f"\n--- {y} (Britannia spring max: {peak_str} m) ---")
        cap_total, used_total = 0.0, 0.0
        for rid in sorted(limits):
            if rid not in state:
                continue
            date_str, lvl = state[rid]
            lim = limits[rid]
            pct = pct_of_band(lvl, lim["low_limit"], lim["high_limit"])
            cap = lim.get("capacity_mcm")
            used = usable_storage_used_mcm(lvl, lim["low_limit"],
                                            lim["high_limit"], cap)
            if cap and used is not None:
                cap_total += cap
                used_total += used
            print(f"    {rid:25s} {date_str}  level={lvl:7.2f}m  "
                  f"low={lim['low_limit']:7.2f}  high={lim['high_limit']:7.2f}  "
                  f"pct={pct:5.1f}%  cap={str(cap) if cap else '—':>6}Mm³  "
                  f"used={used:.0f}Mm³" if used is not None else
                  f"    {rid:25s} {date_str}  level={lvl:7.2f}m  pct={pct:5.1f}%")
            rows_out.append({"year": y, "reservoir_id": rid, "date": date_str,
                             "level_m": lvl, "low_limit_m": lim["low_limit"],
                             "high_limit_m": lim["high_limit"],
                             "pct_of_band": round(pct, 2) if pct is not None else "",
                             "capacity_mcm": cap if cap else "",
                             "used_storage_mcm": round(used, 1) if used is not None else "",
                             "peak_britannia_m": round(peak, 3) if peak else ""})
        if cap_total > 0:
            pct_full = 100.0 * used_total / cap_total
            print(f"    {'TOTAL':25s} usable_capacity={cap_total:.0f}Mm³  "
                  f"used={used_total:.0f}Mm³  ({pct_full:.1f}% of total band)")
            year_totals[y] = {"used_mcm": used_total, "cap_mcm": cap_total,
                              "pct": pct_full, "peak": peak}

    # ----- write per-(year, reservoir) CSV
    out_csv = OUTDIR_DATA / "april1_state_by_year.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "year", "reservoir_id", "date", "level_m", "low_limit_m", "high_limit_m",
            "pct_of_band", "capacity_mcm", "used_storage_mcm", "peak_britannia_m"])
        w.writeheader()
        for r in rows_out:
            w.writerow(r)
    print(f"\nWrote {len(rows_out)} rows to {out_csv.relative_to(ROOT)}")

    # ----- scatter: aggregate pre-freshet storage % vs Britannia peak
    paired = [(y, d["pct"], d["peak"]) for y, d in year_totals.items()
              if d["peak"] is not None]
    if paired:
        fig, ax = plt.subplots(figsize=(8, 6))
        xs = [p[1] for p in paired]
        ys = [p[2] for p in paired]
        labels = [p[0] for p in paired]
        ax.scatter(xs, ys, c="#2c6aa0", s=80, edgecolors="k", linewidths=0.6, zorder=3)
        for x, y, lab in zip(xs, ys, labels):
            ax.annotate(f"  {lab}", (x, y), fontsize=10, va="center")
        ax.set_xlabel("April-1 aggregate usable storage at 13 principal reservoirs (% of total operating band)")
        ax.set_ylabel("Britannia spring max level (m)")
        ax.set_title(f"Pre-freshet reservoir state vs subsequent peak — feasibility scout (n={len(paired)})")
        ax.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(OUTDIR_FIG / f"{STAMP}_pre_freshet_storage_vs_peak.png", dpi=120)
        plt.close(fig)
        print(f"Wrote scatter (n={len(paired)}): {STAMP}_pre_freshet_storage_vs_peak.png")

    # ----- per-reservoir × year heatmap
    res_ids = sorted(set(r["reservoir_id"] for r in rows_out))
    years_with = sorted(set(r["year"] for r in rows_out))
    if res_ids and years_with:
        H = np.full((len(res_ids), len(years_with)), np.nan)
        for r in rows_out:
            i = res_ids.index(r["reservoir_id"])
            j = years_with.index(r["year"])
            if r["pct_of_band"] != "":
                H[i, j] = r["pct_of_band"]
        fig, ax = plt.subplots(figsize=(6, 8))
        im = ax.imshow(H, aspect="auto", cmap="RdBu_r", vmin=0, vmax=100)
        ax.set_xticks(range(len(years_with)))
        ax.set_xticklabels(years_with)
        ax.set_yticks(range(len(res_ids)))
        ax.set_yticklabels(res_ids)
        for i in range(len(res_ids)):
            for j in range(len(years_with)):
                v = H[i, j]
                if not np.isnan(v):
                    ax.text(j, i, f"{v:.0f}", ha="center", va="center",
                            fontsize=8, color="white" if (v < 25 or v > 75) else "k")
        ax.set_title(f"April-1 ± 7d % of operating band\n(blue = drawn down, red = high)")
        cbar = fig.colorbar(im, ax=ax)
        cbar.set_label("% of operating band")
        fig.tight_layout()
        fig.savefig(OUTDIR_FIG / f"{STAMP}_pre_freshet_band_heatmap.png", dpi=120)
        plt.close(fig)
        print(f"Wrote heatmap: {STAMP}_pre_freshet_band_heatmap.png")

    # ----- annotated summary
    print(f"\n{'='*78}\nSUMMARY\n{'='*78}")
    print(f"  paired (state, peak) observations: {len(paired)}")
    print(f"  years missed (no Apr-1 ±7d Wayback snapshot): "
          f"{sorted(set(YEARS) - {p[0] for p in paired})}")
    print(f"  years pre-2020 (no Wayback coverage at all): 2017, 2018, 2019")
    if len(paired) >= 2:
        xs = np.array([p[1] for p in paired])
        ys = np.array([p[2] for p in paired])
        r = float(np.corrcoef(xs, ys)[0, 1])
        print(f"  corr(pre-freshet aggregate %, Britannia peak) = {r:+.3f}  (n={len(paired)} — not significant)")
        if len(paired) >= 3:
            beta = np.polyfit(xs, ys, 1)
            print(f"  OLS slope: {beta[0]:+.4f} m per pct  "
                  f"(every +10% of band on April 1 → {beta[0]*10:+.2f} m on peak)")


if __name__ == "__main__":
    main()
