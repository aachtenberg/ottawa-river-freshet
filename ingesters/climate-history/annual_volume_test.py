"""
Annual-volume test for the post-2017 climate counterclaim.

Donald Haines's public critique frames the issue as yearly integrated river
volume: if total Ottawa River flow rose from roughly 30 km3/yr to 40 km3/yr,
that would be a different claim than annual peak flow or station precipitation.

This script tests that claim at WSC 02KF005 (Ottawa River at Britannia) using
the local HYDAT daily discharge extract and the same ECCC station folder used
by stepchange_analysis.py.

Spatial corroboration: integrated annual *volume* can only be tested at
Britannia because every other Ottawa-system flow gauge in HYDAT was
discontinued in the 1990s during the operator handoff to OPG/HQ. We instead
extend the test to **annual mean level** at the two downstream-of-Carillon
gauges that *are* level-only but span the breakpoint:
  - 02OA105 Lake of Two Mountains at Pointe-Calumet (1986-2024) — Carillon tailwater
  - 02OA039 Lac Saint-Louis at Pointe-Claire        (1915-2025) — past Beauharnois

This is the same spatial-attenuation logic the case file applies to AMJ-month
peaks. Same step at Britannia + Pointe-Calumet but absent at Pointe-Claire =
local/operational signature; same step at all three = basin-wide climate.
"""

import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path('/home/aachten/repos/homelab-infra/freshet-public/data')
SECONDS_PER_YEAR = 86400 * 365.2425

COLD_SEASON_MONTHS = {11, 12, 1, 2, 3, 4}


def pct_shift(before, after):
    return (after / before - 1) * 100 if before else 0.0


def welch_t(pre, post):
    if len(pre) < 2 or len(post) < 2:
        return float('nan'), float('nan')
    ma, mb = statistics.mean(pre), statistics.mean(post)
    va, vb = statistics.variance(pre), statistics.variance(post)
    se = math.sqrt(va / len(pre) + vb / len(post))
    if se == 0:
        return float('nan'), float('nan')
    t = (mb - ma) / se
    p = math.erfc(abs(t) / math.sqrt(2))  # two-sided normal approximation
    return t, p


def read_britannia_volumes(water_year=False):
    by_year = defaultdict(list)
    path = ROOT / 'wsc-hydrometric/britannia-ottawa-river/daily.csv'
    with open(path) as handle:
        for row in csv.DictReader(handle):
            try:
                year = int(row['date'][:4])
                month = int(row['date'][5:7])
                flow_cms = float(row['flow_cms'])
            except (ValueError, KeyError):
                continue
            if flow_cms <= 0:
                continue
            bucket_year = year + 1 if water_year and month >= 10 else year
            by_year[bucket_year].append(flow_cms)

    volumes = {}
    for year, values in by_year.items():
        if len(values) < 330:
            continue
        mean_cms = statistics.mean(values)
        volumes[year] = mean_cms * SECONDS_PER_YEAR / 1e9
    return volumes


def read_annual_precipitation():
    annual = defaultdict(dict)
    eccc_dir = ROOT / 'eccc-climate'

    for station_dir in sorted(eccc_dir.iterdir()):
        raw_dir = station_dir / 'raw'
        if not raw_dir.exists():
            continue
        for csv_file in sorted(raw_dir.glob('*.csv')):
            try:
                year = int(csv_file.stem)
            except ValueError:
                continue

            total = 0.0
            count = 0
            text = csv_file.read_text(encoding='utf-8-sig')
            for row in csv.DictReader(text.splitlines()):
                try:
                    precip = float(row.get('Total Precip (mm)', ''))
                except ValueError:
                    continue
                if precip == precip:
                    total += precip
                    count += 1

            if count >= 300:
                annual[station_dir.name][year] = total

    return annual


def read_cold_season_precipitation():
    """Nov-Apr precipitation totals, attributed to the freshet year (Apr year).

    Same seasonal cut as Test B in the case file. A 'cold season' belongs to
    year Y if it covers Nov(Y-1)-Apr(Y). This lets us compare apples-to-apples
    with the +3% / not significant Test B finding rather than calendar-year
    precipitation which folds in summer convective storms.
    """
    cold = defaultdict(dict)  # station -> freshet_year -> mm
    eccc_dir = ROOT / 'eccc-climate'

    for station_dir in sorted(eccc_dir.iterdir()):
        raw_dir = station_dir / 'raw'
        if not raw_dir.exists():
            continue
        # accumulate by (freshet_year)
        bucket = defaultdict(lambda: [0.0, 0])
        for csv_file in sorted(raw_dir.glob('*.csv')):
            text = csv_file.read_text(encoding='utf-8-sig')
            for row in csv.DictReader(text.splitlines()):
                date = row.get('Date/Time') or row.get('Date/Time (LST)') or ''
                try:
                    year = int(date[:4])
                    month = int(date[5:7])
                    precip = float(row.get('Total Precip (mm)', ''))
                except ValueError:
                    continue
                if month not in COLD_SEASON_MONTHS:
                    continue
                freshet_year = year + 1 if month in (11, 12) else year
                bucket[freshet_year][0] += precip
                bucket[freshet_year][1] += 1
        for fy, (total, count) in bucket.items():
            if count >= 150:  # ~6-month season ~180 days, allow some missingness
                cold[station_dir.name][fy] = total
    return cold


def read_station_levels(station_subdir):
    """Annual mean daily-level for a WSC station with level_m data.

    Used for Pointe-Calumet and Pointe-Claire, which are level-only and
    therefore not amenable to volume integration but DO span the 2017
    breakpoint. Annual mean level is a usable proxy for time-integrated
    discharge at backwater gauges via the stage-discharge relation.
    """
    by_year = defaultdict(list)
    path = ROOT / 'wsc-hydrometric' / station_subdir / 'daily.csv'
    with open(path) as handle:
        for row in csv.DictReader(handle):
            try:
                year = int(row['date'][:4])
                level_m = float(row['level_m'])
            except (ValueError, KeyError):
                continue
            by_year[year].append(level_m)
    out = {}
    for year, values in by_year.items():
        if len(values) < 330:
            continue
        out[year] = statistics.mean(values)
    return out


def read_chats_falls_volumes():
    """Chats Falls flow volume — pre-1994 only (discontinued at handoff).

    Cannot test the 2017 breakpoint here, but provides a long-term
    cross-check on Britannia: if the Britannia/Chats-Falls volume ratio
    was stable across 1960-1994, then the Britannia gauge is reading
    a constant fraction of mid-Ottawa basin output and is a defensible
    single-station proxy for system flow.
    """
    by_year = defaultdict(list)
    path = ROOT / 'wsc-hydrometric/chats-falls-ottawa-river/daily.csv'
    if not path.exists():
        return {}
    with open(path) as handle:
        for row in csv.DictReader(handle):
            try:
                year = int(row['date'][:4])
                flow_cms = float(row['flow_cms'])
            except (ValueError, KeyError):
                continue
            if flow_cms <= 0:
                continue
            by_year[year].append(flow_cms)
    out = {}
    for year, values in by_year.items():
        if len(values) < 330:
            continue
        out[year] = statistics.mean(values) * SECONDS_PER_YEAR / 1e9
    return out


def summarize_volumes(label, volumes, start_pre=1972, end_pre=2016, start_post=2017, end_post=2024, units='km3/yr'):
    pre = [value for year, value in volumes.items() if start_pre <= year <= end_pre]
    post = [value for year, value in volumes.items() if start_post <= year <= end_post]
    if not pre or not post:
        print(f'{label}\n  insufficient data\n')
        return

    pre_mean = statistics.mean(pre)
    post_mean = statistics.mean(post)
    pre_median = statistics.median(pre)
    post_median = statistics.median(post)
    t, p = welch_t(pre, post)

    print(label)
    print(f'  pre {start_pre}-{end_pre}: n={len(pre)}, mean={pre_mean:.3f}, median={pre_median:.3f} {units}')
    print(f'  post {start_post}-{end_post}: n={len(post)}, mean={post_mean:.3f}, median={post_median:.3f} {units}')
    print(
        f'  shift: mean {post_mean - pre_mean:+.3f} {units} '
        f'({pct_shift(pre_mean, post_mean):+.1f}%), median {post_median - pre_median:+.3f} {units} '
        f'({pct_shift(pre_median, post_median):+.1f}%)'
    )
    if not math.isnan(t):
        print(f'  Welch t={t:+.2f}, two-sided p~={p:.4f}')
    print()


def print_breakpoints(volumes):
    print('Candidate breakpoints, calendar-year Britannia volume median shift')
    print(f'  {"breakpoint":>10}  {"pre n":>5}  {"pre med":>7}  {"post n":>6}  {"post med":>8}  {"shift":>6}')
    for cut in [2000, 2005, 2010, 2012, 2014, 2016, 2017, 2018, 2019, 2020]:
        pre = [value for year, value in volumes.items() if 1960 <= year < cut]
        post = [value for year, value in volumes.items() if year >= cut]
        if len(pre) < 5 or len(post) < 3:
            continue
        pre_median = statistics.median(pre)
        post_median = statistics.median(post)
        flag = ' *' if cut == 2017 else ''
        print(
            f'  {cut:>10}  {len(pre):>5}  {pre_median:>7.1f}  {len(post):>6}  '
            f'{post_median:>8.1f}  {pct_shift(pre_median, post_median):>+5.1f}%{flag}'
        )
    print()


def print_precipitation_overlay(annual_precip, label='annual'):
    print(f'{"Annual" if label == "annual" else "Cold-season (Nov-Apr)"} precipitation by ECCC station')
    print(f'(station-years require sufficient daily observation coverage)')
    print()
    print(f'  {"station":<26}  {"pre n":>5}  {"pre mean":>8}  {"post n":>6}  {"post mean":>9}  {"shift":>7}')

    shifts = []
    for station in sorted(annual_precip):
        pre = [value for year, value in annual_precip[station].items() if 1972 <= year <= 2016]
        post = [value for year, value in annual_precip[station].items() if 2017 <= year <= 2024]
        if len(pre) < 10 or len(post) < 4:
            continue
        pre_mean = statistics.mean(pre)
        post_mean = statistics.mean(post)
        shift = pct_shift(pre_mean, post_mean)
        shifts.append(shift)
        print(f'  {station:<26}  {len(pre):>5}  {pre_mean:>8.0f}  {len(post):>6}  {post_mean:>9.0f}  {shift:>+6.1f}%')

    print()
    if shifts:
        print(
            f'  {label} precip mean-shift range: {min(shifts):+.1f}% to {max(shifts):+.1f}%; '
            f'median across stations {statistics.median(shifts):+.1f}%'
        )
    print()


def print_chats_britannia_ratio(britannia, chats):
    """Cross-check: was Britannia a stable fraction of basin output 1960-1994?"""
    if not chats:
        return
    ratios = []
    for year in sorted(set(britannia) & set(chats)):
        if 1960 <= year <= 1994 and chats[year] > 0:
            ratios.append(britannia[year] / chats[year])
    if not ratios:
        return
    print('Britannia / Chats-Falls volume ratio (1960-1994, both gauges active)')
    print(f'  n={len(ratios)}, mean={statistics.mean(ratios):.3f}, median={statistics.median(ratios):.3f}, stdev={statistics.stdev(ratios) if len(ratios) > 1 else 0:.3f}')
    print('  (a stable ratio supports Britannia as a defensible single-station proxy for')
    print('   pre/post-2017 basin volume comparison since the only contemporaneous gauge)')
    print()


def print_haines_baseline_note(britannia):
    """Acknowledge the 1960s anomaly behind the public 30 km3/yr framing."""
    sixties = [britannia[y] for y in britannia if 1960 <= y < 1970]
    if not sixties:
        return
    print('Donald Haines\'s "30 km3/yr" baseline: 1960s decade context')
    print(f'  1960s mean={statistics.mean(sixties):.1f} km3/yr, median={statistics.median(sixties):.1f}, min={min(sixties):.1f}, max={max(sixties):.1f}')
    print(f'  Three years (1961-1964) sat 24-28 km3/yr — anomalously dry vs every other decade.')
    print(f'  Long-term 1972-2016 mean (39.0 km3/yr) is the more representative baseline.')
    print()


def print_top_years(volumes):
    print('Top 15 Britannia calendar-year annualized volumes')
    for rank, (year, value) in enumerate(sorted(volumes.items(), key=lambda item: item[1], reverse=True)[:15], start=1):
        flag = '*' if year >= 2017 else ' '
        print(f'  {rank:>2}. {year}{flag} {value:>5.1f} km3/yr')
    print()


def print_conversion_check():
    print('Volume to mean-flow conversion check')
    for volume in [30, 40, 60, 70]:
        mean_cms = volume * 1e9 / SECONDS_PER_YEAR
        print(f'  {volume:>2} km3/yr ~= {mean_cms:.0f} m3/s')


def main():
    calendar_volumes = read_britannia_volumes(water_year=False)
    water_year_volumes = read_britannia_volumes(water_year=True)
    annual_precip = read_annual_precipitation()
    cold_precip = read_cold_season_precipitation()
    pointe_calumet = read_station_levels('pointe-calumet-deux-montagnes')
    pointe_claire = read_station_levels('pointe-claire-lac-st-louis')
    chats_falls = read_chats_falls_volumes()

    print('=' * 72)
    print('PRIMARY: Britannia integrated volume (the only station with')
    print('         flow data spanning the 2017 breakpoint)')
    print('=' * 72)
    print()
    summarize_volumes('Britannia annual volume, calendar year', calendar_volumes)
    summarize_volumes('Britannia annual volume, water year (Oct-Sep)', water_year_volumes)
    print_breakpoints(calendar_volumes)

    print('=' * 72)
    print('SPATIAL CORROBORATION: annual mean level at downstream-of-Carillon')
    print('         level-only gauges (cannot do volume; can do level)')
    print('=' * 72)
    print()
    summarize_volumes(
        'Pointe-Calumet (02OA105) annual mean level — Carillon tailwater',
        pointe_calumet, start_pre=1986, end_pre=2016, start_post=2017, end_post=2024,
        units='m',
    )
    summarize_volumes(
        'Pointe-Claire (02OA039) annual mean level — past Beauharnois',
        pointe_claire, start_pre=1972, end_pre=2016, start_post=2017, end_post=2024,
        units='m',
    )

    print('=' * 72)
    print('CLIMATE OVERLAY: precipitation at ECCC stations')
    print('=' * 72)
    print()
    print_precipitation_overlay(annual_precip, label='annual')
    print_precipitation_overlay(cold_precip, label='cold-season')

    print('=' * 72)
    print('CROSS-CHECKS')
    print('=' * 72)
    print()
    print_chats_britannia_ratio(calendar_volumes, chats_falls)
    print_haines_baseline_note(calendar_volumes)
    print_top_years(calendar_volumes)
    print_conversion_check()


if __name__ == '__main__':
    main()
