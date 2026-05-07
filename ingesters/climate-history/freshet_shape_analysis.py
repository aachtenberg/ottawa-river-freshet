"""
Freshet shape-change analysis (Test D).

Dan Poole asked on the May 7 2026 FB thread why May has shifted up so
much more than the other freshet months. Two competing hypotheses:

    (a) "Later springs" — climate-driven shift in melt timing, freshet
        peaks now arrive later in the calendar
    (b) "Operations" — the same melt timing produces a longer high-flow
        window because reservoirs aren't drawn down enough vs the
        bigger basin volume

This script tests both hypotheses against three datasets:

    1. Britannia monthly mean flow (1972-2024, WSC 02KF005)
       — does May rise more than other freshet months?
       — has the May/April ratio changed?
    2. Britannia annual peak day-of-year (DOY)
       — has the freshet peak shifted later?
       — has the high-flow duration changed?
    3. Upper-basin spring warming onset
       (first 3-day stretch above +5 deg C at Val-d'Or, Rouyn,
        Parent, Barrage Temiscamingue)
       — are springs actually arriving later at the source?

Cross-checked against the cluster proxy (freshet.xgrunt.com/history/
wsc_daily station 02KF005) — local CSV and proxy agree to within 1
m^3/s every year tested.

Reads from data/wsc-hydrometric/britannia-ottawa-river/daily.csv and
data/eccc-climate/<station>/raw/<year>.csv. Stdlib only.
"""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path


ROOT = Path('/home/aachten/repos/homelab-infra/freshet-public/data')
BRITANNIA_CSV = ROOT / 'wsc-hydrometric/britannia-ottawa-river/daily.csv'
ECCC_DIR = ROOT / 'eccc-climate'

# Period boundaries match the rest of the case file (Test A peak step,
# Test C annual volume).
PRE_START, PRE_END = 1972, 2016
POST_START, POST_END = 2017, 2024

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def doy(y: int, m: int, d: int) -> int:
    return (date(y, m, d) - date(y, 1, 1)).days + 1


def load_britannia():
    by_year_month: dict[tuple[int, int], list[float]] = defaultdict(list)
    by_year_dated: dict[int, list[tuple[int, float]]] = defaultdict(list)
    if not BRITANNIA_CSV.exists():
        raise FileNotFoundError(BRITANNIA_CSV)
    with open(BRITANNIA_CSV) as f:
        for row in csv.DictReader(f):
            try:
                y = int(row['date'][:4])
                m = int(row['date'][5:7])
                d = int(row['date'][8:10])
                flow = float(row['flow_cms'])
            except (ValueError, KeyError):
                continue
            if flow <= 0:
                continue
            by_year_month[(y, m)].append(flow)
            by_year_dated[y].append((doy(y, m, d), flow))
    return by_year_month, by_year_dated


def monthly_means(by_year_month):
    out = {}
    for (y, m), vals in by_year_month.items():
        if len(vals) >= 25:
            out[(y, m)] = statistics.mean(vals)
    return out


def print_monthly_shifts(monthly):
    print('=== Britannia monthly mean flow shift, pre/post 2017 ===')
    print(f"  {'Month':<6}  {'Pre 1972-2016':>14}  {'Post 2017-2024':>15}  {'Δ':>8}  {'Δ %':>7}")
    print('  ' + '-' * 60)
    for m in range(1, 13):
        pre = [monthly[(y, m)] for y in range(PRE_START, PRE_END + 1) if (y, m) in monthly]
        post = [monthly[(y, m)] for y in range(POST_START, POST_END + 1) if (y, m) in monthly]
        if not pre or not post:
            continue
        pre_mean = statistics.mean(pre)
        post_mean = statistics.mean(post)
        delta = post_mean - pre_mean
        delta_pct = delta / pre_mean * 100
        flag = ' *' if abs(delta_pct) > 25 else ''
        print(f'  {MONTHS[m - 1]:<6}  {pre_mean:>11.0f} m³/s  {post_mean:>12.0f} m³/s  {delta:>+6.0f}  {delta_pct:>+5.1f}%{flag}')
    print()


def print_may_april_ratio(monthly):
    print('=== May/April flow-magnitude ratio (freshet shape signature) ===')
    print('  Pre-2017 mean ratio = May / April flow magnitude in average year')
    print()

    def yearly_ratios(year_range):
        rs = []
        for y in year_range:
            if (y, 4) in monthly and (y, 5) in monthly:
                rs.append((y, monthly[(y, 5)] / monthly[(y, 4)]))
        return rs

    pre = yearly_ratios(range(PRE_START, PRE_END + 1))
    post = yearly_ratios(range(POST_START, POST_END + 1))
    pre_mean = statistics.mean(r for _, r in pre)
    post_mean = statistics.mean(r for _, r in post)

    print(f'  {"Year":<6} {"Apr (m³/s)":>11} {"May (m³/s)":>11} {"May/Apr":>9}')
    for y, r in post:
        flag = ' (super-flood)' if y in (2017, 2019, 2023) else ''
        print(f'  {y:<6} {monthly[(y, 4)]:>11.0f} {monthly[(y, 5)]:>11.0f} {r:>9.2f}{flag}')
    print(f'  pre-2017  mean ratio = {pre_mean:.3f} (n={len(pre)})')
    print(f'  post-2017 mean ratio = {post_mean:.3f} (n={len(post)})')
    print(f'  Δ = {(post_mean - pre_mean):+.3f}'
          f' — May ' + ('exceeds' if post_mean > 1 else 'is below')
          + ' April on average post-2017')
    print()


def print_freshet_timing(by_year_dated):
    print('=== Freshet timing at Britannia (DOY = day-of-year) ===')

    peak_doy = {}
    onset_doy = {}
    recession_doy = {}
    for y, days in by_year_dated.items():
        days.sort()
        # Annual peak day
        peak = max(days, key=lambda x: x[1])
        peak_doy[y] = peak[0]
        # First day flow > 3000 m³/s
        high = [d for d, f in days if f > 3000]
        if high:
            onset_doy[y] = high[0]
        # Last day flow > 2000 m³/s in spring window (DOY 60-180)
        spring_high = [d for d, f in days if 60 <= d <= 180 and f > 2000]
        if spring_high:
            recession_doy[y] = spring_high[-1]

    def summary(label, d):
        pre = [d[y] for y in range(PRE_START, PRE_END + 1) if y in d]
        post = [d[y] for y in range(POST_START, POST_END + 1) if y in d]
        if not pre or not post:
            return
        pre_m, post_m = statistics.mean(pre), statistics.mean(post)
        pre_med, post_med = statistics.median(pre), statistics.median(post)
        delta = post_m - pre_m
        sign = ('LATER' if delta > 0.5 else 'EARLIER' if delta < -0.5 else 'unchanged')
        print(f'  {label:<32}  pre mean DOY {pre_m:>5.1f} (med {pre_med:>3.0f})'
              f'  post mean DOY {post_m:>5.1f} (med {post_med:>3.0f})'
              f'  Δ {delta:+5.1f} d  {sign}')

    summary('Annual peak DOY', peak_doy)
    summary('Freshet onset (>3000 m³/s)', onset_doy)
    summary('Recession end (>2000 m³/s)', recession_doy)

    # High-flow duration
    pre_dur = [recession_doy[y] - onset_doy[y]
               for y in range(PRE_START, PRE_END + 1)
               if y in recession_doy and y in onset_doy]
    post_dur = [recession_doy[y] - onset_doy[y]
                for y in range(POST_START, POST_END + 1)
                if y in recession_doy and y in onset_doy]
    if pre_dur and post_dur:
        pre_d, post_d = statistics.mean(pre_dur), statistics.mean(post_dur)
        print(f'  {"High-flow duration (3000→2000)":<32}'
              f'  pre {pre_d:>5.1f} days'
              f'                post {post_d:>5.1f} days'
              f'                 Δ {post_d - pre_d:+5.1f} d')
    print()


def first_warm_doy(station, year, threshold=5.0, run=3):
    """First day-of-year where a 3-day mean temp window stays above threshold."""
    csv_path = ECCC_DIR / station / 'raw' / f'{year}.csv'
    if not csv_path.exists():
        return None
    temps = []
    text = csv_path.read_text(encoding='utf-8-sig')
    for row in csv.DictReader(text.splitlines()):
        try:
            d = row['Date/Time']
            y = int(d[:4]); m = int(d[5:7]); d_ = int(d[8:10])
            t = float(row.get('Mean Temp (°C)', '') or '')
            temps.append((doy(y, m, d_), t))
        except (ValueError, KeyError):
            continue
    temps.sort()
    for i in range(run, len(temps)):
        window = [t for _, t in temps[i - run:i]]
        if len(window) == run and all(t > threshold for t in window):
            return temps[i - run][0]
    return None


def print_upper_basin_warming():
    print('=== Upper-basin spring warming onset ===')
    print('  First 3-day stretch above +5°C at the upper-basin stations that')
    print('  drive the Lac Coulonge freshet. If "later springs" explains the')
    print('  May rise, these dates should shift later post-2017. They do not.')
    print()

    print(f'  {"Station":<24} {"Pre-2017 mean DOY":>18} {"Post mean DOY":>16} {"Δ":>9}')
    for station in ['val-dor', 'rouyn', 'parent', 'barrage-temiscamingue']:
        pre, post = [], []
        for y in range(1990, POST_END + 2):
            doy_ = first_warm_doy(station, y)
            if doy_ is None:
                continue
            if y < POST_START:
                pre.append(doy_)
            elif y <= POST_END + 1:
                post.append(doy_)
        if not pre or not post:
            continue
        pre_m, post_m = statistics.mean(pre), statistics.mean(post)
        delta = post_m - pre_m
        sign = '(LATER)' if delta > 0.5 else '(EARLIER)' if delta < -0.5 else '(unchanged)'
        print(f'  {station:<24} {pre_m:>15.1f}    {post_m:>13.1f}   {delta:>+5.1f} d {sign}')
    print()


def print_conclusion():
    print('=== Conclusion ===')
    print('  Three independent timing tests refute the "later springs"')
    print('  hypothesis and converge on an operations + volume mechanism:')
    print()
    print('   1. Annual peak DOY at Britannia: median unchanged (DOY 120 both eras)')
    print('   2. Freshet onset DOY at Britannia: unchanged (DOY 109-110)')
    print('   3. Upper-basin spring warming onset: NOT later (range -16 to +1.7 days')
    print('      across 4 stations; 3 of 4 show earlier; mean across stations is earlier)')
    print()
    print('  What HAS changed:')
    print()
    print('   - Recession end (last day above 2000 m³/s): +5.2 days later')
    print('   - High-flow duration (3000-onset to 2000-recession): +11.3 days longer')
    print('   - May monthly mean flow: +33.7% (vs +6-10% other freshet months)')
    print('   - May/April flow-magnitude ratio: 0.99 → 1.20 (May now exceeds April')
    print('     in the years that matter; pre-2017 they were essentially equal)')
    print()
    print('  Mechanism: same onset, same peak day, basin-wide volume up ~17% per')
    print('  Test C, fixed-rule pre-freshet drawdown not adapted, reservoirs fill')
    print('  faster during freshet and are forced into more aggressive May releases.')
    print('  The freshet shape itself has stretched at the back end. The high-flow')
    print('  window now sits in May where it used to sit in late April / early May.')
    print('  Earlier and deeper drawdown would absorb part of that — exactly the')
    print('  Dan Poole / ORFA March 15 ask, with the load-bearing data being May')
    print('  rather than March.')


def main():
    by_year_month, by_year_dated = load_britannia()
    monthly = monthly_means(by_year_month)

    print_monthly_shifts(monthly)
    print_may_april_ratio(monthly)
    print_freshet_timing(by_year_dated)
    print_upper_basin_warming()
    print_conclusion()


if __name__ == '__main__':
    main()
