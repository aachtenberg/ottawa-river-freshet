"""
Seasonal-window precipitation analysis — tests whether ORRPB's May 6 2026
CBC-article claim ("preliminary assessment of precipitation received between
March 1 and April 15 shows the total amount was the highest recorded in the
last 50 years") is window-cherry-picked.

The freshet is driven by the *full* fall-winter-spring precipitation
accumulation, not a 6-week spring slice. We compute basin-mean precipitation
across the same ECCC stations used by stepchange_analysis.py and
annual_volume_test.py for five windows:

    Mar 1 - Apr 15   (ORRPB's chosen window)
    Oct 1 - Feb 28   (fall+winter, BEFORE ORRPB's window)
    Oct 1 - Apr 15   (full pre-freshet season)
    Nov 1 - Apr 15   (standard cold-season; matches Test B)
    Dec 1 - Apr 15   (winter + spring)

Each window is attributed to the freshet year (Oct/Nov/Dec data belongs to
the *next* year's spring freshet). Basin-mean requires at least 4 stations
reporting in the year. Per-station inclusion requires at least 85% of the
window's days observed.

If 2026's record holds across *all* windows: ORRPB framing is honest.
If 2026 ranks high only in Mar 1 - Apr 15 and middling elsewhere: cherry-pick.

Source: stdlib only; reads from data/eccc-climate/.
"""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path('/home/aachten/repos/homelab-infra/freshet-public/data/eccc-climate')

WINDOWS = {
    'mar1-apr15': {
        'label': 'Mar 1 - Apr 15  (ORRPB chosen window)',
        'days_total': 46,
    },
    'oct1-feb28': {
        'label': 'Oct 1 - Feb 28  (fall+winter, BEFORE ORRPB window)',
        'days_total': 151,
    },
    'oct1-apr15': {
        'label': 'Oct 1 - Apr 15  (full pre-freshet season)',
        'days_total': 197,
    },
    'nov1-apr15': {
        'label': 'Nov 1 - Apr 15  (standard cold-season, matches Test B)',
        'days_total': 167,
    },
    'dec1-apr15': {
        'label': 'Dec 1 - Apr 15  (winter + spring)',
        'days_total': 136,
    },
}


def in_window(month: int, day: int, window: str) -> bool:
    if window == 'mar1-apr15':
        return month == 3 or (month == 4 and day <= 15)
    if window == 'oct1-feb28':
        return month in (10, 11, 12, 1, 2)
    if window == 'oct1-apr15':
        return month in (10, 11, 12, 1, 2) or month == 3 or (month == 4 and day <= 15)
    if window == 'nov1-apr15':
        return month in (11, 12, 1, 2) or month == 3 or (month == 4 and day <= 15)
    if window == 'dec1-apr15':
        return month in (12, 1, 2) or month == 3 or (month == 4 and day <= 15)
    raise ValueError(f'unknown window {window}')


def collect_window(station_dir: Path, window: str) -> dict[int, float]:
    """Return {freshet_year: total_mm} where Oct/Nov/Dec data belongs to next year."""
    by_year = defaultdict(lambda: [0.0, 0])
    raw = station_dir / 'raw'
    if not raw.exists():
        return {}
    for f in sorted(raw.glob('*.csv')):
        text = f.read_text(encoding='utf-8-sig')
        for row in csv.DictReader(text.splitlines()):
            date = row.get('Date/Time') or row.get('Date/Time (LST)') or ''
            try:
                year = int(date[:4]); month = int(date[5:7]); day = int(date[8:10])
                precip = float(row.get('Total Precip (mm)', ''))
            except (ValueError, KeyError):
                continue
            if not in_window(month, day, window):
                continue
            freshet_year = year + 1 if month >= 10 else year
            by_year[freshet_year][0] += precip
            by_year[freshet_year][1] += 1

    min_days = int(WINDOWS[window]['days_total'] * 0.85)
    return {fy: total for fy, (total, n) in by_year.items() if n >= min_days}


def basin_mean_by_year(window: str) -> tuple[dict[int, float], dict[int, int]]:
    all_years = defaultdict(list)
    for station_dir in sorted(ROOT.iterdir()):
        if not station_dir.is_dir():
            continue
        for fy, value in collect_window(station_dir, window).items():
            all_years[fy].append(value)
    means = {fy: sum(values) / len(values)
             for fy, values in all_years.items() if len(values) >= 4}
    counts = {fy: len(values) for fy, values in all_years.items()}
    return means, counts


def print_window_ranking(window: str) -> None:
    means, counts = basin_mean_by_year(window)
    if not means:
        print(f'--- {WINDOWS[window]["label"]} ---  no data')
        return
    sorted_years = sorted(means.items(), key=lambda x: -x[1])

    print(f'--- {WINDOWS[window]["label"]} ---')
    if 2026 not in means:
        print('  2026 not in record (insufficient station coverage)')
        print()
        return

    rank = next(i for i, (y, _) in enumerate(sorted_years, 1) if y == 2026)
    print(f'  2026 basin-mean: {means[2026]:.0f} mm')
    print(f'  Rank: {rank} / {len(means)} (record back to {min(means)})')
    print('  Top 5:')
    for i, (year, value) in enumerate(sorted_years[:5], 1):
        flag = ' *' if year == 2026 else ''
        print(f'    {i}. {year}: {value:.0f} mm  (n={counts[year]} stations){flag}')
    print()


def print_share_of_season() -> None:
    """Per-station: what % of total Oct 1 - Apr 15 precip fell in Mar 1 - Apr 15?"""
    print('CHERRY-PICK CHECK')
    print('Per-station: 2026 Mar 1 - Apr 15 share of total Oct 1 - Apr 15 precip')
    print('vs historical median share of season.')
    print()
    print(f'  {"station":<26}  {"2026 share":>11}  {"hist median":>11}  {"above by":>9}')
    for station_dir in sorted(ROOT.iterdir()):
        if not station_dir.is_dir():
            continue
        full = collect_window(station_dir, 'oct1-apr15')
        spring = collect_window(station_dir, 'mar1-apr15')
        if 2026 not in full or 2026 not in spring:
            continue
        historical_shares = [spring[fy] / full[fy] * 100
                             for fy in full if fy in spring and fy != 2026]
        if not historical_shares:
            continue
        share_2026 = spring[2026] / full[2026] * 100
        hist_median = statistics.median(historical_shares)
        delta = share_2026 - hist_median
        print(f'  {station_dir.name:<26}  {share_2026:>10.1f}%  {hist_median:>10.1f}%  {delta:>+8.1f} pp')
    print()


def print_summary_finding() -> None:
    print('=' * 72)
    print('SUMMARY')
    print('=' * 72)
    print()
    rankings = {}
    for window in WINDOWS:
        means, _ = basin_mean_by_year(window)
        if 2026 in means:
            rank = sum(1 for v in means.values() if v >= means[2026])
            rankings[window] = (rank, len(means), means[2026])

    print('  2026 basin-mean rank by window:')
    for window, (rank, n, value) in rankings.items():
        print(f'    {WINDOWS[window]["label"]:<55}  rank {rank}/{n}  ({value:.0f} mm)')

    print()
    print('  Interpretation: if 2026 were a genuinely exceptional precipitation')
    print('  year, it should rank near the top across multiple seasonal windows.')
    print('  If it only ranks #1 in the narrow ORRPB-selected window and is')
    print('  middling-to-low in the standard climatological windows, the ORRPB')
    print('  framing has selected the only window in which the year looks')
    print('  exceptional.')


def main() -> None:
    for window in WINDOWS:
        print_window_ranking(window)
    print_share_of_season()
    print_summary_finding()


if __name__ == '__main__':
    main()
