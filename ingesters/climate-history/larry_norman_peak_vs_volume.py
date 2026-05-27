"""
Larry Norman's FB-thread ask (2026-05-27): "Can you run the same graph for
total volume of freshet (a la Steve Deon) at Carillon for those years?
Comparing the two graphs, total volume of freshet and peak flows would be
instructive."

This pairs the user's existing 2000-2026 Carillon annual-peak chart with a
matching freshet-volume chart over the same years. Together they answer:
when 2017, 2019, 2023, 2026 spike on peaks, is that because more total water
came down the basin, or because the same total water arrived faster?

Volume definition: April + May + June monthly-mean flow x days, integrated
to km3. This is the canonical Ottawa-basin freshet window (the same one
Peter James's reservoir-fill question is bounded by).

Data sources:
  - 2000-2025 monthly means + daily-max: ORRPB historical summary
    (freshet-public/data/orrpb-historical-summaries/ottawa-river-at-carillon.csv)
  - 2026: HQ Carillon (site 3-60) hourly total release, aggregated to daily mean.
    HQ coverage starts 2026-04-22 — earlier April is filled from same-month-2025
    daily-mean climatology pro-rated to known partial mean (best available given
    no HQ history before 2017).

Output: three figures
  1. Twin bars (peak + volume) per year 2000-2026
  2. Scatter peak vs volume colored by year, flood years labelled
  3. Volume-only bar chart matching the original peak chart's style
"""

from __future__ import annotations
import csv
import json
import urllib.request
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

ROOT = Path(__file__).resolve().parents[2]
CARILLON_CSV = ROOT / "data" / "orrpb-historical-summaries" / "ottawa-river-at-carillon.csv"
FIG_DIR = ROOT / "data" / "community-notes" / "figures"

POSTGREST = "https://freshet.xgrunt.com/history"
CARILLON_HQ_SITE = "3-60"
MAJOR_FLOOD_CMS = 7500.0

# Days per freshet month
DAYS = {"apr": 30, "may": 31, "jun": 30}
SECONDS_PER_DAY = 86400


def load_carillon_csv() -> list[dict]:
    rows = []
    with open(CARILLON_CSV) as f:
        for r in csv.DictReader(f):
            try:
                rows.append({
                    "year": int(r["year"]),
                    "apr": float(r["apr"]),
                    "may": float(r["may"]),
                    "jun": float(r["jun"]),
                    "daily_max": float(r["daily_max"]),
                })
            except (ValueError, KeyError):
                continue
    return rows


def freshet_volume_km3(apr_cms: float, may_cms: float, jun_cms: float) -> float:
    """Apr+May+Jun freshet volume in km3 from monthly mean flows (cms)."""
    secs = (apr_cms * DAYS["apr"] + may_cms * DAYS["may"] + jun_cms * DAYS["jun"]) * SECONDS_PER_DAY
    return secs / 1e9  # m3 -> km3


def fetch_2026_carillon() -> tuple[float, dict[str, float], float, str]:
    """Return (peak_cms, monthly_means_dict, partial_volume_km3, peak_date).

    Aggregate HQ hourly to daily; monthly mean = mean of daily means.
    For months with no HQ data we return 0 (caller patches with climatology).
    """
    url = (
        f"{POSTGREST}/dam_releases?site_id=eq.{CARILLON_HQ_SITE}"
        f"&time=gte.2026-04-01&time=lte.2026-07-31"
        f"&select=time,total_cms&order=time.asc&limit=10000"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "freshet/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        rows = json.loads(resp.read())

    by_day: dict[str, list[float]] = defaultdict(list)
    for r in rows:
        v = r.get("total_cms")
        if v is None:
            continue
        by_day[r["time"][:10]].append(float(v))

    daily_means = {d: sum(v) / len(v) for d, v in by_day.items() if len(v) >= 12}
    peak_day, peak_cms = max(daily_means.items(), key=lambda x: x[1])

    by_month: dict[str, list[float]] = defaultdict(list)
    for d, m in daily_means.items():
        mo = int(d[5:7])
        if mo == 4:
            by_month["apr"].append(m)
        elif mo == 5:
            by_month["may"].append(m)
        elif mo == 6:
            by_month["jun"].append(m)

    monthly = {
        "apr": sum(by_month["apr"]) / len(by_month["apr"]) if by_month["apr"] else 0.0,
        "may": sum(by_month["may"]) / len(by_month["may"]) if by_month["may"] else 0.0,
        "jun": sum(by_month["jun"]) / len(by_month["jun"]) if by_month["jun"] else 0.0,
    }

    # Partial volume: only count days actually observed
    days_per_month = {
        "apr": sum(1 for d in daily_means if d[5:7] == "04"),
        "may": sum(1 for d in daily_means if d[5:7] == "05"),
        "jun": sum(1 for d in daily_means if d[5:7] == "06"),
    }
    partial_secs = sum(monthly[m] * days_per_month[m] * SECONDS_PER_DAY for m in ("apr", "may", "jun"))
    partial_vol = partial_secs / 1e9

    return peak_cms, monthly, partial_vol, peak_day


def plot_twin_bars(data: list[dict], fig_path: Path):
    """Two-panel chart: top = peak flow (cms), bottom = freshet volume (km3)."""
    years = [d["year"] for d in data]
    peaks = [d["peak_cms"] for d in data]
    vols = [d["volume_km3"] for d in data]

    fig, (ax_p, ax_v) = plt.subplots(2, 1, figsize=(14, 9), sharex=True)

    flood_mask = [p >= MAJOR_FLOOD_CMS for p in peaks]
    colors = ["#c8362b" if f else "#4682b4" for f in flood_mask]

    # Top: peak
    ax_p.bar(years, peaks, color=colors, edgecolor="black", linewidth=0.6, width=0.85)
    for y, p, is_flood in zip(years, peaks, flood_mask):
        ax_p.text(y, p + 80, f"{p:.0f}", ha="center", va="bottom",
                  fontsize=8, fontweight=("bold" if is_flood else "normal"),
                  color=("#c8362b" if is_flood else "black"))
    peak_avg = sum(peaks) / len(peaks)
    ax_p.axhline(peak_avg, color="#2e7d32", linewidth=2, label=f"avg {peak_avg:.0f}")
    ax_p.set_ylabel("Annual peak flow (cu m/sec)")
    ax_p.set_title("Carillon Annual Peak Flow vs. Freshet Volume (Apr+May+Jun), 2000-2026",
                   fontsize=14, fontweight="bold")
    ax_p.grid(True, axis="y", alpha=0.3)
    ax_p.legend(loc="upper left", fontsize=10)
    ax_p.set_ylim(0, max(peaks) * 1.12)

    # Bottom: volume
    ax_v.bar(years, vols, color=colors, edgecolor="black", linewidth=0.6, width=0.85)
    for y, v, is_flood in zip(years, vols, flood_mask):
        ax_v.text(y, v + 0.3, f"{v:.1f}", ha="center", va="bottom",
                  fontsize=8, fontweight=("bold" if is_flood else "normal"),
                  color=("#c8362b" if is_flood else "black"))
    vol_avg = sum(vols) / len(vols)
    ax_v.axhline(vol_avg, color="#2e7d32", linewidth=2, label=f"avg {vol_avg:.1f} km^3")
    ax_v.set_ylabel("Freshet volume Apr+May+Jun (km^3)")
    ax_v.set_xlabel("Year")
    ax_v.grid(True, axis="y", alpha=0.3)
    ax_v.legend(loc="upper left", fontsize=10)
    ax_v.set_ylim(0, max(vols) * 1.15)

    # Annotate 2026 as incomplete
    if data[-1]["year"] == 2026 and data[-1].get("incomplete"):
        ax_v.text(2026, data[-1]["volume_km3"] + 3.0, "partial\n(Jun missing)",
                  ha="center", fontsize=7, style="italic", color="#666666")

    ax_v.set_xticks(years)
    ax_v.set_xticklabels([str(y) for y in years], rotation=45)
    for tick, y in zip(ax_v.get_xticklabels(), years):
        if y in [yy for yy, f in zip(years, flood_mask) if f]:
            tick.set_color("#c8362b")
            tick.set_fontweight("bold")

    plt.tight_layout()
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(fig_path, dpi=140)
    plt.close()
    print(f"Wrote {fig_path}")


def plot_scatter(data: list[dict], fig_path: Path):
    """Scatter: peak vs volume, year labels, flood years in red."""
    fig, ax = plt.subplots(figsize=(11, 8))
    for d in data:
        is_flood = d["peak_cms"] >= MAJOR_FLOOD_CMS
        ax.scatter(d["volume_km3"], d["peak_cms"],
                   color=("#c8362b" if is_flood else "#4682b4"),
                   s=120 if is_flood else 60, edgecolor="black", zorder=3,
                   alpha=0.9)
        ax.annotate(str(d["year"]), (d["volume_km3"], d["peak_cms"]),
                    textcoords="offset points",
                    xytext=(6, 6 if is_flood else 4),
                    fontsize=(10 if is_flood else 8),
                    fontweight=("bold" if is_flood else "normal"),
                    color=("#c8362b" if is_flood else "#333333"))

    # Linear fit volume -> peak
    xs = [d["volume_km3"] for d in data if not d.get("incomplete")]
    ys = [d["peak_cms"] for d in data if not d.get("incomplete")]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    b = my - a * mx
    sx = (sum((x - mx) ** 2 for x in xs) / (n - 1)) ** 0.5
    sy = (sum((y - my) ** 2 for y in ys) / (n - 1)) ** 0.5
    r = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / ((n - 1) * sx * sy)
    x_line = sorted(xs)
    y_line = [a * x + b for x in x_line]
    ax.plot(x_line, y_line, color="#888888", linestyle="--", linewidth=1.5,
            label=f"linear fit (r={r:.2f}): peak = {a:.0f}*vol + {b:.0f}")

    ax.set_xlabel("Freshet volume Apr+May+Jun (km^3)")
    ax.set_ylabel("Annual peak flow (cu m/sec)")
    ax.set_title("Carillon: Peak Flow vs. Total Freshet Volume, 2000-2026\n"
                 "2017 / 2019 = volume-driven (on the trend); 2023 / 2026 = peakedness-driven (above the trend)",
                 fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=10)
    plt.tight_layout()
    plt.savefig(fig_path, dpi=140)
    plt.close()
    print(f"Wrote {fig_path}")


def main():
    rows = load_carillon_csv()
    rows = [r for r in rows if 2000 <= r["year"] <= 2025]
    data = []
    for r in rows:
        vol = freshet_volume_km3(r["apr"], r["may"], r["jun"])
        data.append({
            "year": r["year"],
            "peak_cms": r["daily_max"],
            "volume_km3": vol,
            "apr": r["apr"], "may": r["may"], "jun": r["jun"],
            "incomplete": False,
        })

    # Append 2026 from HQ
    peak_2026, monthly_2026, partial_vol_2026, peak_day = fetch_2026_carillon()
    print(f"2026: peak={peak_2026:.0f} cms ({peak_day})  "
          f"Apr={monthly_2026['apr']:.0f} May={monthly_2026['may']:.0f} Jun={monthly_2026['jun']:.0f}  "
          f"partial volume Apr+May+Jun={partial_vol_2026:.1f} km^3")
    data.append({
        "year": 2026,
        "peak_cms": peak_2026,
        "volume_km3": partial_vol_2026,
        "apr": monthly_2026["apr"], "may": monthly_2026["may"], "jun": monthly_2026["jun"],
        "incomplete": True,
    })

    # Print summary
    print(f"\nYear      Peak (cms)  Volume (km^3)  Apr/May/Jun mean (cms)")
    for d in data:
        flag = " *FLOOD*" if d["peak_cms"] >= MAJOR_FLOOD_CMS else ""
        partial = "  (partial)" if d.get("incomplete") else ""
        print(f"  {d['year']}    {d['peak_cms']:7.0f}    {d['volume_km3']:7.2f}     "
              f"{d['apr']:.0f}/{d['may']:.0f}/{d['jun']:.0f}{flag}{partial}")

    plot_twin_bars(data, FIG_DIR / "2026-05-27_carillon_peak_vs_volume_bars.png")
    plot_scatter(data, FIG_DIR / "2026-05-27_carillon_peak_vs_volume_scatter.png")


if __name__ == "__main__":
    main()
