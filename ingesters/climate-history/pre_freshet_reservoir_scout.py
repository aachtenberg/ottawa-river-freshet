#!/usr/bin/env python3
"""Pre-freshet reservoir state vs subsequent freshet peak — full analysis.

Now uses the ORRPB per-location historical archive (1990-2025, 36 years,
13 reservoirs) instead of the Wayback-mined snapshots (which were the
feasibility-scout fallback). With n ≥ 30 paired observations the regression
actually has statistical meat.

Inputs:
  - data/orrpb-location-history/orrpb_location_daily.csv  (the 170k-row archive)
  - dashboard/reservoir-limits.json                       (operating bands + capacities)
  - data/wsc-hydrometric/britannia-ottawa-river/daily.csv (response variable)

Outputs:
  - data/orrpb-location-history/april1_state_by_year.csv
  - data/community-notes/2026-05-23_pre_freshet_storage_vs_peak.png  (replaces n=3 scout)
  - data/community-notes/2026-05-23_pre_freshet_band_heatmap.png     (replaces n=3 scout)
  - data/community-notes/2026-05-23_pre_freshet_upper_river.png      (NEW: upper-river-only)
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
ORRPB_CSV = ROOT / "data" / "orrpb-location-history" / "orrpb_location_daily.csv"
LIMITS_JSON = ROOT / "dashboard" / "reservoir-limits.json"
BRITANNIA_CSV = ROOT / "data" / "wsc-hydrometric" / "britannia-ottawa-river" / "daily.csv"
OUTDIR_DATA = ROOT / "data" / "orrpb-location-history"
OUTDIR_FIG = ROOT / "data" / "community-notes"
STAMP = "2026-05-23"

# Reservoirs whose outflow reaches Lac Coulonge / Pembroke (upper-river).
# Cabonga/Kiamika/Mitchinamecus/Baskatong/Bark Lake/Poisson Blanc/Des Joachims
# join downstream of the upper-river communities so they don't change the
# Pembroke peak (matches the May-22 community-note partition).
UPPER_RIVER = {"timiskaming", "kipawa", "quinze", "rapide_7",
               "dozois", "lady_evelyn"}


def load_orrpb():
    rows = []
    with open(ORRPB_CSV) as f:
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


def load_britannia_peaks():
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


def april1_state(rows, limits):
    """{year -> {reservoir_id -> (level, pct, used_mcm, cap_mcm)}}."""
    out: dict[int, dict] = collections.defaultdict(dict)
    for r in rows:
        if r["level_m"] is None:
            continue
        d = D.fromisoformat(r["date"])
        if d.month != 4 or d.day != 1:
            continue
        rid = r["reservoir_id"]
        if rid not in limits:
            continue
        lim = limits[rid]
        low, high = lim["low_limit"], lim["high_limit"]
        pct = 100.0 * (r["level_m"] - low) / (high - low)
        cap = lim.get("capacity_mcm")
        used = (pct / 100.0) * cap if cap else None
        out[d.year][rid] = {"level": r["level_m"], "pct": pct,
                            "used_mcm": used, "cap_mcm": cap}
    return out


def aggregate(state_per_year, subset=None):
    """{year -> aggregate pct of band by mcm-weighted average}."""
    out = {}
    for y, by_res in state_per_year.items():
        used_total, cap_total = 0.0, 0.0
        pct_avg = []
        for rid, s in by_res.items():
            if subset is not None and rid not in subset:
                continue
            if s["used_mcm"] is not None and s["cap_mcm"]:
                used_total += s["used_mcm"]
                cap_total += s["cap_mcm"]
            pct_avg.append(s["pct"])
        if cap_total > 0:
            out[y] = {
                "pct_storage": 100.0 * used_total / cap_total,  # capacity-weighted
                "pct_band_avg": float(np.mean(pct_avg)),       # equal-weight
                "used_mcm": used_total, "cap_mcm": cap_total,
                "n_reservoirs": len(pct_avg),
            }
    return out


def linfit(xs, ys):
    xs, ys = np.asarray(xs), np.asarray(ys)
    r = float(np.corrcoef(xs, ys)[0, 1])
    beta = np.polyfit(xs, ys, 1)
    n = len(xs)
    # p-value for r (two-tailed t)
    if abs(r) < 1 - 1e-9 and n > 2:
        t = r * np.sqrt(n - 2) / np.sqrt(1 - r ** 2)
        from math import erf, sqrt
        # use normal approx for p-value (good enough at n=30+)
        p = 2 * (1 - 0.5 * (1 + erf(abs(t) / sqrt(2))))
    else:
        p = float("nan")
    return r, beta, n, p


def scatter(xs, ys, labels, xlabel, ylabel, title, path):
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(xs, ys, c="#2c6aa0", s=55, edgecolors="k", linewidths=0.5, zorder=3)
    for x, y, lab in zip(xs, ys, labels):
        ax.annotate(f"  {lab}", (x, y), fontsize=8, va="center", alpha=0.75)
    if len(xs) >= 3:
        r, beta, n, p = linfit(xs, ys)
        xx = np.linspace(min(xs), max(xs), 100)
        ax.plot(xx, beta[0] * xx + beta[1], "k--", alpha=0.5, linewidth=1)
        ax.set_title(f"{title}\nn={n}   r={r:+.3f}   p={p:.3f}   slope={beta[0]:+.4f} m/pct")
    else:
        ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)


def heatmap(state_per_year, res_order, path, title):
    years = sorted(state_per_year)
    H = np.full((len(res_order), len(years)), np.nan)
    for j, y in enumerate(years):
        for i, rid in enumerate(res_order):
            s = state_per_year[y].get(rid)
            if s:
                H[i, j] = s["pct"]
    fig, ax = plt.subplots(figsize=(14, 5))
    im = ax.imshow(H, aspect="auto", cmap="RdBu_r", vmin=0, vmax=100)
    ax.set_xticks(range(len(years)))
    ax.set_xticklabels(years, rotation=90, fontsize=7)
    ax.set_yticks(range(len(res_order)))
    ax.set_yticklabels(res_order, fontsize=8)
    for i in range(len(res_order)):
        for j in range(len(years)):
            v = H[i, j]
            if not np.isnan(v):
                ax.text(j, i, f"{v:.0f}", ha="center", va="center",
                        fontsize=6, color="white" if (v < 25 or v > 75) else "k")
    ax.set_title(title)
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("% of operating band")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)


def main():
    OUTDIR_DATA.mkdir(parents=True, exist_ok=True)
    OUTDIR_FIG.mkdir(parents=True, exist_ok=True)

    rows = load_orrpb()
    limits = load_limits()
    britannia = load_britannia_peaks()
    print(f"ORRPB obs: {len(rows)}")
    print(f"Reservoirs with limits: {len(limits)}")
    print(f"Britannia peaks: {len(britannia)} years ({min(britannia)}-{max(britannia)})")

    state = april1_state(rows, limits)
    print(f"\nApril-1 state computed for {len(state)} years "
          f"({min(state)}-{max(state)})")

    # ---- per-(year, reservoir) CSV
    out_rows = []
    for y in sorted(state):
        for rid in sorted(state[y]):
            s = state[y][rid]
            out_rows.append({
                "year": y, "reservoir_id": rid,
                "level_m": round(s["level"], 2),
                "pct_of_band": round(s["pct"], 2),
                "capacity_mcm": s["cap_mcm"] or "",
                "used_storage_mcm": round(s["used_mcm"], 1) if s["used_mcm"] is not None else "",
                "peak_britannia_m": round(britannia[y], 3) if y in britannia else "",
            })
    out_csv = OUTDIR_DATA / "april1_state_by_year.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "year", "reservoir_id", "level_m", "pct_of_band",
            "capacity_mcm", "used_storage_mcm", "peak_britannia_m"])
        w.writeheader()
        for r in out_rows:
            w.writerow(r)
    print(f"Wrote {len(out_rows)} rows to {out_csv.relative_to(ROOT)}")

    # ---- Aggregate (all 13) — basin-wide
    agg_all = aggregate(state)
    paired_all = [(y, d["pct_storage"], britannia[y])
                  for y, d in agg_all.items() if y in britannia]
    paired_all.sort()

    # ---- Aggregate (upper-river only) — relevant to Pembroke peak
    agg_up = aggregate(state, subset=UPPER_RIVER)
    paired_up = [(y, d["pct_storage"] if d["cap_mcm"] else d["pct_band_avg"],
                  britannia[y]) for y, d in agg_up.items() if y in britannia]
    # Use equal-weight band average for upper-river because rapide_7 has no
    # capacity figure (its storage is the upstream Decelles per ICOLD).
    paired_up = [(y, d["pct_band_avg"], britannia[y])
                 for y, d in agg_up.items() if y in britannia]
    paired_up.sort()

    print(f"\nPaired observations:")
    print(f"  basin-wide (13 reservoirs): n={len(paired_all)}")
    print(f"  upper-river  (6 reservoirs): n={len(paired_up)}")

    # ---- Headline regressions
    print(f"\n{'='*78}\nHEADLINE — pre-freshet state vs Britannia spring peak\n{'='*78}")

    for name, paired in [("BASIN-WIDE (capacity-weighted)", paired_all),
                         ("UPPER-RIVER ONLY (equal-weight avg)", paired_up)]:
        xs = [p[1] for p in paired]
        ys = [p[2] for p in paired]
        r, beta, n, p = linfit(xs, ys)
        print(f"\n{name}  n={n}")
        print(f"  r = {r:+.3f}    p = {p:.3f}")
        print(f"  slope = {beta[0]:+.4f} m per pct  "
              f"(+10 pct of band on Apr 1 → {beta[0]*10:+.2f} m on peak)")
        # show notable years
        zs = sorted(paired, key=lambda t: t[2], reverse=True)[:5]
        print(f"  top-5 peak years: " +
              ", ".join(f"{y}({x:.0f}%→{p:.2f}m)" for y, x, p in zs))
        zs = sorted(paired, key=lambda t: t[1])[:5]
        print(f"  most drawn down (low % of band): " +
              ", ".join(f"{y}({x:.0f}%→{p:.2f}m)" for y, x, p in zs))
        zs = sorted(paired, key=lambda t: t[1], reverse=True)[:5]
        print(f"  least drawn down (high % of band): " +
              ", ".join(f"{y}({x:.0f}%→{p:.2f}m)" for y, x, p in zs))

    # ---- Figures
    # Basin-wide
    scatter([p[1] for p in paired_all], [p[2] for p in paired_all],
            [p[0] for p in paired_all],
            "April-1 basin-wide aggregate storage (% of operating band, capacity-weighted)",
            "Britannia spring max level (m)",
            "Pre-freshet basin storage vs Britannia peak — all 13 ORRPB reservoirs",
            OUTDIR_FIG / f"{STAMP}_pre_freshet_storage_vs_peak.png")
    # Upper-river only
    scatter([p[1] for p in paired_up], [p[2] for p in paired_up],
            [p[0] for p in paired_up],
            "April-1 upper-river average state (% of operating band, equal-weight 6 reservoirs)",
            "Britannia spring max level (m)",
            "Pre-freshet UPPER-RIVER storage vs Britannia peak — Timiskaming/Kipawa/Quinze/Rapide-7/Dozois/Lady Evelyn",
            OUTDIR_FIG / f"{STAMP}_pre_freshet_upper_river.png")
    # Heatmap
    heatmap(state, sorted(limits), OUTDIR_FIG / f"{STAMP}_pre_freshet_band_heatmap.png",
            "April-1 % of operating band, 1990-2025 (blue = drawn down, red = high)")

    print(f"\nWrote figures to {OUTDIR_FIG.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
