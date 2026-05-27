"""
Kathy Black's FB-thread ask (2026-05-27): produce 25-year Carillon annual-peak
charts for 1950-1974 and 1975-1999 in the same visual style as the existing
2000-2026 chart, so the post-2017 super-flood cluster can be compared against
two prior 25-year windows.

Data sources:
  - 1964-2025 Carillon outflow daily-max: ORRPB historical summary CSV
    (freshet-public/data/orrpb-historical-summaries/ottawa-river-at-carillon.csv)
  - 1950-1963 Carillon equivalent: regressed from WSC 02KF009 Ottawa River at
    Chats Falls daily flows (record 1915-1994). Britannia flow data starts
    only 1960, so Chats Falls is the only long-record Ottawa main-stem flow
    gauge that covers the entire 1950-1963 window. Overlap regression on
    Chats x Carillon (1964-1994) sets the scaling.
  - 2026 peak: HQ Carillon (site 3-60) daily-mean total release; Apr 23 = 7677 cms

Output: two PNGs matching the user's existing chart style.
"""

from __future__ import annotations
import csv
import datetime
import json
import statistics
import urllib.request
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
CARILLON_CSV = ROOT / "data" / "orrpb-historical-summaries" / "ottawa-river-at-carillon.csv"
CHATS_DAILY = ROOT / "data" / "wsc-hydrometric" / "chats-falls-ottawa-river" / "daily.csv"
FIG_DIR = ROOT / "data" / "community-notes" / "figures"

POSTGREST = "https://freshet.xgrunt.com/history"
CARILLON_HQ_SITE = "3-60"

# Major-flood threshold (cms). Picked to match the 4 red bars in the user's
# 2000-2026 chart (2017, 2019, 2023, 2026 = 9094 / 9217 / 8015 / 7615+).
MAJOR_FLOOD_CMS = 7500.0

# Freshet window months (inclusive)
FRESHET_MONTHS = {4, 5, 6}


def load_carillon_csv() -> dict[int, float]:
    """{year: annual daily-max flow cms} from ORRPB historical summary."""
    out: dict[int, float] = {}
    with open(CARILLON_CSV) as f:
        for row in csv.DictReader(f):
            try:
                out[int(row["year"])] = float(row["daily_max"])
            except (ValueError, KeyError):
                continue
    return out


def load_chats_annual_peaks() -> dict[int, float]:
    """Chats Falls annual peak daily flow (cms) from WSC HYDAT extract."""
    by_year: dict[int, float] = {}
    with open(CHATS_DAILY) as f:
        for row in csv.DictReader(f):
            try:
                year = int(row["date"][:4])
                flow = float(row["flow_cms"])
            except (ValueError, KeyError):
                continue
            if flow <= 0:
                continue
            if flow > by_year.get(year, 0.0):
                by_year[year] = flow
    return by_year


def fit_proxy_to_carillon(proxy: dict[int, float], car: dict[int, float],
                          proxy_name: str) -> tuple[float, float]:
    """Linear regression Carillon_peak = a * proxy_peak + b on overlap years."""
    xs, ys = [], []
    for y, p in proxy.items():
        if y in car:
            xs.append(p)
            ys.append(car[y])
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    a = num / den
    b = my - a * mx
    sx = (sum((x - mx) ** 2 for x in xs) / (n - 1)) ** 0.5
    sy = (sum((y - my) ** 2 for y in ys) / (n - 1)) ** 0.5
    r = num / ((n - 1) * sx * sy)
    print(f"{proxy_name} -> Carillon regression on {n} overlap years:")
    print(f"  Carillon_peak = {a:.4f} * {proxy_name}_peak + {b:.1f}")
    print(f"  Pearson r = {r:.4f}")
    return a, b


def fetch_2026_carillon_peak() -> tuple[float, str]:
    """Daily-mean peak Carillon outflow for 2026 from HQ hourly feed."""
    url = (
        f"{POSTGREST}/dam_releases?site_id=eq.{CARILLON_HQ_SITE}"
        f"&time=gte.2026-04-01&time=lte.2026-07-31"
        f"&select=time,total_cms&order=time.asc&limit=5000"
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
    daily_means = [(d, sum(v) / len(v)) for d, v in by_day.items() if len(v) >= 12]
    daily_means.sort(key=lambda x: -x[1])
    return daily_means[0][1], daily_means[0][0]


def plot_combined(car_extended: dict[int, float], estimated: set[int], fig_path: Path):
    """All 76 years on one chart with three window-average lines (matching the user's
    original 2000-2026 chart legend style)."""
    years = sorted(y for y in car_extended if 1950 <= y <= 2026)
    vals = [car_extended[y] for y in years]

    # Window averages
    def avg(lo, hi):
        ws = [car_extended[y] for y in years if lo <= y <= hi]
        return sum(ws) / len(ws), len(ws)

    avg_1, n1 = avg(1950, 1974)
    avg_2, n2 = avg(1975, 1999)
    avg_3, n3 = avg(2000, 2026)
    avg_all, n_all = avg(1950, 2026)

    flood_years = [y for y, v in zip(years, vals) if v >= MAJOR_FLOOD_CMS]

    fig, ax = plt.subplots(figsize=(20, 7))

    for y, v in zip(years, vals):
        is_flood = v >= MAJOR_FLOOD_CMS
        color = "#c8362b" if is_flood else "#4682b4"
        hatch = "//" if y in estimated else None
        ax.bar(y, v, color=color, edgecolor="black", linewidth=0.4, hatch=hatch,
               width=0.85, zorder=3)
        if is_flood:
            ax.text(y, v + 80, f"{v:.0f}", ha="center", va="bottom",
                    fontsize=8, fontweight="bold", color="#c8362b", zorder=4)

    # Three window-average lines, like the user's original chart legend style
    ax.hlines(avg_1, 1949.5, 1974.5, colors="#f4a261", linewidth=3, zorder=2,
              label=f"1950-1974 avg {avg_1:.0f} (n={n1})")
    ax.hlines(avg_2, 1974.5, 1999.5, colors="#2a9d8f", linewidth=3, zorder=2,
              label=f"1975-1999 avg {avg_2:.0f} (n={n2})")
    ax.hlines(avg_3, 1999.5, 2026.5, colors="#7b3294", linewidth=3, zorder=2,
              label=f"2000-2026 avg {avg_3:.0f} (n={n3})")
    ax.hlines(avg_all, 1949.5, 2026.5, colors="#444444", linewidth=1.5,
              linestyles="--", zorder=2,
              label=f"76-yr avg {avg_all:.0f} (n={n_all})")

    # Flood legend marker
    if flood_years:
        ax.bar(years[0], 0, color="#c8362b",
               label=f"Major floods (>= {MAJOR_FLOOD_CMS:.0f} cms) -> {', '.join(str(y) for y in flood_years)}")

    if estimated:
        ax.bar(years[0], 0, color="#cccccc", hatch="//", edgecolor="black",
               label="Hatched = estimated from upstream gauge (pre-Carillon-dam years)")

    ax.set_xlim(1949.2, 2026.8)
    ax.set_ylim(0, max(vals) * 1.1)
    ax.set_xlabel("Year")
    ax.set_ylabel("Flow (cu m/sec)")
    ax.set_title("76-Year Average Annual Peak - Carillon Flow (1950-2026)",
                 fontsize=15, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.3, zorder=0)
    ax.set_axisbelow(True)

    # X ticks every 5 years + flood years + endpoints
    tick_years = sorted(set([1950, 2026] + [y for y in years if y % 5 == 0] + flood_years))
    ax.set_xticks(tick_years)
    ax.set_xticklabels([str(y) for y in tick_years], rotation=45)
    for tick, y in zip(ax.get_xticklabels(), tick_years):
        if y in flood_years:
            tick.set_color("#c8362b")
            tick.set_fontweight("bold")

    # Period shading boundaries
    for x in (1974.5, 1999.5):
        ax.axvline(x, color="#999999", linestyle=":", linewidth=1, alpha=0.6, zorder=1)

    ax.legend(loc="upper left", fontsize=10, framealpha=0.95, ncol=2)
    plt.tight_layout()
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(fig_path, dpi=140)
    plt.close()
    print(f"Wrote {fig_path}")


def plot_window(years, vals, window_label, fig_path, prior_window_avg_label=None,
                prior_window_avg_value=None, this_window_color="#4682b4",
                estimated_years: set[int] | None = None):
    """Render a 25-year peak-flow chart matching the user's 2000-2026 style."""
    estimated_years = estimated_years or set()
    fig, ax = plt.subplots(figsize=(14, 6.5))

    flood_years = [y for y, v in zip(years, vals) if v >= MAJOR_FLOOD_CMS]
    flood_label = (
        f"Major floods - {', '.join(str(y) for y in flood_years)}"
        if flood_years else f"Major floods (>= {MAJOR_FLOOD_CMS:.0f} cms): none"
    )

    bars = []
    for y, v in zip(years, vals):
        is_flood = v >= MAJOR_FLOOD_CMS
        color = "#c8362b" if is_flood else this_window_color
        # Estimated (Britannia-regressed) bars get a hatched edge to flag them
        hatch = "//" if y in estimated_years else None
        b = ax.bar(y, v, color=color, edgecolor="black", linewidth=0.6, hatch=hatch,
                   width=0.85, zorder=3)
        bars.append(b)
        # Value label
        label_color = "white" if is_flood else "black"
        offset = -180 if is_flood else 80
        va = "top" if is_flood else "bottom"
        ax.text(y, v + offset, f"{v:.0f}", ha="center", va=va, fontsize=9,
                fontweight=("bold" if is_flood else "normal"),
                color=label_color, zorder=4)

    # Average lines
    window_avg = sum(vals) / len(vals)
    ax.hlines(window_avg, years[0] - 0.5, years[-1] + 0.5,
              colors="#2e7d32", linewidth=2.5, zorder=2,
              label=f"{window_label} avg {window_avg:.0f}")
    if prior_window_avg_value is not None:
        ax.hlines(prior_window_avg_value, years[0] - 0.5, years[-1] + 0.5,
                  colors="#7b3294", linewidth=2.5, linestyles="--", zorder=2,
                  label=f"{prior_window_avg_label} avg {prior_window_avg_value:.0f}")

    # Flood legend marker
    ax.bar(years[0], 0, color="#c8362b", label=flood_label)

    # Estimated marker for legend
    if estimated_years:
        ax.bar(years[0], 0, color="#cccccc", hatch="//", edgecolor="black",
               label="Hatched = estimated from upstream gauge (pre-Carillon-dam years)")

    ax.set_xlim(years[0] - 0.7, years[-1] + 0.7)
    ax.set_ylim(0, max(vals + [9500]) * 1.08)
    ax.set_xlabel("Year")
    ax.set_ylabel("Flow (cu m/sec)")
    ax.set_title(f"25-Year Average Annual Peak - Carillon Flow ({window_label})",
                 fontsize=14, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.3, zorder=0)
    ax.set_axisbelow(True)

    # X-tick labels: every 5 years + endpoints + flood years bolded red
    tick_years = sorted(set([years[0], years[-1]]
                            + [y for y in years if y % 5 == 0]
                            + flood_years))
    ax.set_xticks(tick_years)
    labels = []
    for y in tick_years:
        labels.append(str(y))
    ax.set_xticklabels(labels, rotation=0)
    for tick, y in zip(ax.get_xticklabels(), tick_years):
        if y in flood_years:
            tick.set_color("#c8362b")
            tick.set_fontweight("bold")

    ax.legend(loc="upper left", fontsize=10, framealpha=0.95)
    plt.tight_layout()
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(fig_path, dpi=140)
    plt.close()
    print(f"Wrote {fig_path}")
    print(f"  window avg = {window_avg:.0f} cms, flood years = {flood_years}")


def main():
    car = load_carillon_csv()
    print(f"Loaded {len(car)} Carillon years from ORRPB CSV ({min(car)}-{max(car)})")

    # Add 2026 from HQ
    peak_2026, day_2026 = fetch_2026_carillon_peak()
    car[2026] = peak_2026
    print(f"Added 2026 Carillon peak from HQ: {peak_2026:.0f} cms ({day_2026})")

    chats = load_chats_annual_peaks()
    print(f"Loaded {len(chats)} Chats Falls years ({min(chats)}-{max(chats)})")

    # Fit regression on overlap (Chats 1964-1994 vs Carillon 1964-1994)
    a, b = fit_proxy_to_carillon(chats, car, "ChatsFalls")

    # Extend Carillon back to 1950 via regression
    car_extended = dict(car)
    estimated = set()
    for y in range(1950, 1964):
        if y in chats:
            est = a * chats[y] + b
            car_extended[y] = est
            estimated.add(y)
            print(f"  estimated Carillon {y}: {est:.0f} cms (Chats {chats[y]:.0f})")

    # Window 1: 1950-1974
    win1 = sorted(y for y in car_extended if 1950 <= y <= 1974)
    vals1 = [car_extended[y] for y in win1]
    # Window 2: 1975-1999
    win2 = sorted(y for y in car_extended if 1975 <= y <= 1999)
    vals2 = [car_extended[y] for y in win2]
    # Modern: 2000-2026 (already in user's existing chart, used here only for comparison)
    winm = sorted(y for y in car if 2000 <= y <= 2026)
    valsm = [car[y] for y in winm]
    modern_avg = sum(valsm) / len(valsm)

    print(f"\nWindow averages:")
    print(f"  1950-1974: {sum(vals1)/len(vals1):.0f} cms (n={len(vals1)})")
    print(f"  1975-1999: {sum(vals2)/len(vals2):.0f} cms (n={len(vals2)})")
    print(f"  2000-2026: {modern_avg:.0f} cms (n={len(valsm)})")

    # Count flood years per window
    for label, ys, vs in [
        ("1950-1974", win1, vals1),
        ("1975-1999", win2, vals2),
        ("2000-2026", winm, valsm),
    ]:
        n_flood = sum(1 for v in vs if v >= MAJOR_FLOOD_CMS)
        flood_yrs = [y for y, v in zip(ys, vs) if v >= MAJOR_FLOOD_CMS]
        print(f"  {label}: {n_flood} flood years (>= {MAJOR_FLOOD_CMS:.0f} cms) -> {flood_yrs}")

    # Plots
    plot_window(win1, vals1, "1950-1974",
                FIG_DIR / "2026-05-27_carillon_peaks_1950_1974.png",
                prior_window_avg_label="2000-2026",
                prior_window_avg_value=modern_avg,
                estimated_years=estimated)
    plot_window(win2, vals2, "1975-1999",
                FIG_DIR / "2026-05-27_carillon_peaks_1975_1999.png",
                prior_window_avg_label="2000-2026",
                prior_window_avg_value=modern_avg)
    plot_combined(car_extended, estimated,
                  FIG_DIR / "2026-05-27_carillon_peaks_1950_2026_combined.png")


if __name__ == "__main__":
    main()
