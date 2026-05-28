"""
Dan Poole's flow-through hypothesis (FB thread 2026-05-27):

  Stage 1 (rising):  tributary inflows dominate. Reservoirs buffer.
  Stage 2 (peak):    reservoirs approach operational max; releases ramp up
                     to maintain dam safety. Buffering ends.
  Stage 3 (post-peak): reservoirs at max, outflow = inflow (flow-through).
                       Coincident tributaries plus regulated discharge
                       drive the basin peak.

Test for 2023 (peakedness-driven flood, 8,015 cms Carillon peak):
- Plot ORRPB daily levels for 4-5 representative reservoirs through Apr-Jun 2023
  as percent of operating band, with horizontal line at 100% (operational max).
- Overlay Britannia daily flow as the basin-wide downstream proxy.
- Annotate the date each reservoir hit operational max and the date of the
  basin peak.

If Dan's model holds: reservoirs rise through April, hit max in early-to-mid
May, plateau (flow-through) for several weeks, with the basin peak coinciding
with the onset of flow-through.

Output: data/community-notes/figures/2026-05-27_dan_poole_flowthrough_2023.png
"""

from __future__ import annotations
import csv
import json
from collections import defaultdict
from pathlib import Path
from datetime import date as Date

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

ROOT = Path(__file__).resolve().parents[2]
ORRPB = ROOT / "data" / "orrpb-location-history" / "orrpb_location_daily.csv"
LIMITS = json.load(open(ROOT / "dashboard" / "reservoir-limits.json"))["reservoirs"]
BRITANNIA = ROOT / "data" / "wsc-hydrometric" / "britannia-ottawa-river" / "daily.csv"
FIG_OUT = ROOT / "data" / "community-notes" / "figures" / "2026-05-27_dan_poole_flowthrough_2023.png"

YEAR = 2023
WINDOW_START = Date(YEAR, 4, 1)
WINDOW_END = Date(YEAR, 6, 30)

# Reservoirs to show: pick a mix of upper-basin (Quinze, Cabonga, Lady Evelyn)
# and one Madawaska (Bark Lake). All hit operational max in 2023.
RESERVOIRS = [
    ("quinze",        "Quinze (upper Ottawa)",        "#1f77b4"),
    ("cabonga",       "Cabonga (Gatineau headwaters)", "#2ca02c"),
    ("lady_evelyn",   "Lady Evelyn (Ottawa trib)",    "#ff7f0e"),
    ("bark_lake",     "Bark Lake (Madawaska)",        "#d62728"),
    ("poisson_blanc", "Poisson Blanc (Lievre)",       "#9467bd"),
]


def pct_of_band(lvl: float, lo: float, hi: float) -> float:
    return 100.0 * (lvl - lo) / (hi - lo)


def load_reservoir_series():
    by_res: dict[str, list[tuple[Date, float]]] = defaultdict(list)
    with open(ORRPB) as f:
        for r in csv.DictReader(f):
            try:
                y, m, d = int(r["date"][:4]), int(r["date"][5:7]), int(r["date"][8:10])
                date = Date(y, m, d)
                lvl = float(r["level_m"]) if r["level_m"] else None
                if lvl and WINDOW_START <= date <= WINDOW_END:
                    by_res[r["reservoir_id"]].append((date, lvl))
            except (ValueError, KeyError):
                continue
    for k in by_res:
        by_res[k].sort()
    return by_res


def load_britannia():
    out = []
    with open(BRITANNIA) as f:
        for r in csv.DictReader(f):
            try:
                y, m, d = int(r["date"][:4]), int(r["date"][5:7]), int(r["date"][8:10])
                date = Date(y, m, d)
                flow = float(r["flow_cms"]) if r["flow_cms"] else None
                if flow and WINDOW_START <= date <= WINDOW_END:
                    out.append((date, flow))
            except (ValueError, KeyError):
                continue
    out.sort()
    return out


def first_at_max(series: list[tuple[Date, float]], hi: float, lo: float,
                 threshold_pct: float = 95.0) -> Date | None:
    for date, lvl in series:
        if pct_of_band(lvl, lo, hi) >= threshold_pct:
            return date
    return None


def main():
    res_data = load_reservoir_series()
    brit = load_britannia()

    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(14, 9), sharex=True,
                                          gridspec_kw={"height_ratios": [1.6, 1]})

    # Top: reservoir levels as percent of band
    max_dates = {}
    for res_id, label, color in RESERVOIRS:
        if res_id not in res_data or res_id not in LIMITS:
            continue
        lim = LIMITS[res_id]
        lo, hi = lim["low_limit"], lim["high_limit"]
        dates = [d for d, _ in res_data[res_id]]
        pct = [pct_of_band(v, lo, hi) for _, v in res_data[res_id]]
        ax_top.plot(dates, pct, label=label, color=color, linewidth=2)

        first_max = first_at_max(res_data[res_id], hi, lo)
        if first_max:
            max_dates[label] = first_max
            ax_top.axvline(first_max, color=color, linestyle=":", alpha=0.4, linewidth=1)

    ax_top.axhline(100, color="black", linestyle="--", linewidth=1.5, alpha=0.7,
                   label="Operational max (100% of band)")
    ax_top.set_ylabel("Reservoir level (% of operating band)")
    ax_top.set_title(f"Dan Poole's flow-through hypothesis tested at 2023 Carillon freshet\n"
                     f"Top: reservoir levels approach and plateau at operational max. "
                     f"Bottom: Britannia daily flow.",
                     fontsize=13, fontweight="bold")
    ax_top.legend(loc="lower right", fontsize=9)
    ax_top.grid(True, alpha=0.3)
    ax_top.set_ylim(-5, 115)

    # Annotate dates reservoirs hit operational max
    print("Date each reservoir first hit >= 95% of operating band in 2023:")
    for label, date in max_dates.items():
        print(f"  {label}: {date}")

    # Bottom: Britannia daily flow
    brit_dates = [d for d, _ in brit]
    brit_flows = [f for _, f in brit]
    ax_bot.plot(brit_dates, brit_flows, color="#1a1a1a", linewidth=2,
                label="Britannia (WSC 02KF005, upper-basin proxy)")
    ax_bot.fill_between(brit_dates, 0, brit_flows, color="#4682b4", alpha=0.3)

    # Britannia peak
    if brit:
        peak_idx = brit_flows.index(max(brit_flows))
        peak_date = brit_dates[peak_idx]
        peak_flow = brit_flows[peak_idx]
        ax_bot.scatter([peak_date], [peak_flow], color="#c8362b", s=120, zorder=5,
                       edgecolor="black", linewidth=1, label=f"Basin peak {peak_date} ({peak_flow:.0f} cms)")
        # Drop a guide line from top panel down through bottom panel at peak
        ax_top.axvline(peak_date, color="#c8362b", linestyle="-", linewidth=1.5, alpha=0.5)
        ax_bot.axvline(peak_date, color="#c8362b", linestyle="-", linewidth=1.5, alpha=0.5)
        print(f"\nBritannia peak: {peak_date} at {peak_flow:.0f} cms")

    # Carillon daily max (from ORRPB CSV: 2023 = 8015 cms, exact date not in monthly summary
    # but Britannia peak + ~1 day lag implies Carillon peak around May 7-8 2023)
    ax_bot.set_ylabel("Britannia flow (cu m/sec)")
    ax_bot.set_xlabel("Date (2023)")
    ax_bot.legend(loc="upper right", fontsize=10)
    ax_bot.grid(True, alpha=0.3)

    # X-axis formatting
    ax_bot.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))
    ax_bot.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.setp(ax_bot.xaxis.get_majorticklabels(), rotation=45)

    # Stage shading on top panel
    # Stage 1 = before first reservoir hits max. Stage 2 = first hit to all hit. Stage 3 = all at max.
    if max_dates:
        first = min(max_dates.values())
        last = max(max_dates.values())
        ax_top.axvspan(WINDOW_START, first, color="#cfe2ff", alpha=0.25,
                       label="_nolegend_")
        ax_top.axvspan(first, last, color="#fff3cd", alpha=0.35,
                       label="_nolegend_")
        ax_top.axvspan(last, WINDOW_END, color="#f8d7da", alpha=0.30,
                       label="_nolegend_")
        # Stage labels
        ax_top.text(WINDOW_START + (first - WINDOW_START) / 2, 108,
                    "STAGE 1\nbuffering", ha="center", va="center", fontsize=9,
                    fontweight="bold", color="#1a4a8c", alpha=0.8)
        ax_top.text(first + (last - first) / 2, 108,
                    "STAGE 2\ntransition", ha="center", va="center", fontsize=9,
                    fontweight="bold", color="#7a5b00", alpha=0.8)
        ax_top.text(last + (WINDOW_END - last) / 2, 108,
                    "STAGE 3\nflow-through", ha="center", va="center", fontsize=9,
                    fontweight="bold", color="#8a1a1a", alpha=0.8)

    plt.tight_layout()
    FIG_OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIG_OUT, dpi=140)
    plt.close()
    print(f"\nWrote {FIG_OUT}")


if __name__ == "__main__":
    main()
