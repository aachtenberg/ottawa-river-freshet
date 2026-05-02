"""
Stress-test the 'it's climate' explanation for the post-2017 freshet
intensification. Three tests:

  1. Where does the breakpoint actually sit in the Britannia annual peak
     series? Try multiple candidate years; the one with the largest
     pre/post mean shift is the data-implied breakpoint.

  2. Climate forcing: did April+May precipitation across watershed ECCC
     stations also step-change in the same year? If precip is flat and
     flow stepped, climate is not the cause.

  3. Snow on ground (peak season): same comparison.

If climate forcing is flat across the breakpoint year but flow stepped,
then the +19% median Britannia peak is not climate-driven.
"""

import csv, statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path('/home/aachten/repos/homelab-infra/freshet-public/data')

# 1. Britannia annual peak (April-July only — freshet event)
brit = defaultdict(lambda: 0.0)
with open(ROOT / 'wsc-hydrometric/britannia-ottawa-river/daily.csv') as f:
    for r in csv.DictReader(f):
        try:
            y = int(r['date'][:4]); m = int(r['date'][5:7]); v = float(r['flow_cms'])
        except (ValueError, KeyError):
            continue
        if 4 <= m <= 7 and v > brit[y]:
            brit[y] = v
brit = {y: v for y, v in brit.items() if v > 500 and y >= 1960}

# 2. ECCC climate stations: April + May precipitation totals per year, per station
eccc_dir = ROOT / 'eccc-climate'
station_dirs = [d for d in eccc_dir.iterdir() if d.is_dir() and (d / 'raw').exists()]

precip_by_station_year = defaultdict(lambda: defaultdict(float))
peak_snow_by_station_year = defaultdict(lambda: defaultdict(float))
n_precip_days = defaultdict(lambda: defaultdict(int))

for sdir in station_dirs:
    raw = sdir / 'raw'
    for csv_file in sorted(raw.glob('*.csv')):
        try:
            year = int(csv_file.stem)
        except ValueError:
            continue
        try:
            with open(csv_file) as f:
                # Skip BOM
                txt = f.read()
                if txt.startswith('﻿'):
                    txt = txt[1:]
                lines = txt.splitlines()
                if not lines:
                    continue
                reader = csv.DictReader(lines)
                for row in reader:
                    dt = row.get('Date/Time', '')
                    if not dt or len(dt) < 10:
                        continue
                    try:
                        m = int(dt[5:7])
                    except ValueError:
                        continue
                    # April+May precip — that's the freshet-driving rain
                    if m in (4, 5):
                        try:
                            p = float(row.get('Total Precip (mm)', '') or 'nan')
                            if p == p:  # not nan
                                precip_by_station_year[sdir.name][year] += p
                                n_precip_days[sdir.name][year] += 1
                        except ValueError:
                            pass
                    # Peak snow on ground (March highest reading)
                    if m == 3:
                        try:
                            s = float(row.get('Snow on Grnd (cm)', '') or 'nan')
                            if s == s and s > peak_snow_by_station_year[sdir.name][year]:
                                peak_snow_by_station_year[sdir.name][year] = s
                        except ValueError:
                            pass
        except Exception as e:
            print(f'  WARN {csv_file}: {e}')

# Filter station-years with reasonable coverage (≥40 daily records means full Apr+May)
def filter_coverage(d, n_days_d, min_days=40):
    out = {}
    for s, yd in d.items():
        out[s] = {y: v for y, v in yd.items() if n_days_d[s].get(y, 0) >= min_days}
    return out

precip_by_station_year = filter_coverage(precip_by_station_year, n_precip_days)

print('=== Test 1: Where is the Britannia step-change? ===')
print('(median annual peak, m³/s, partitioned at each candidate year)')
print()
print(f'  {"breakpoint":>10}  {"pre n":>5}  {"pre med":>7}  {"post n":>6}  {"post med":>8}  {"shift":>6}')
years_sorted = sorted(brit)
for cut in [2000, 2005, 2010, 2012, 2014, 2016, 2017, 2018, 2019, 2020]:
    pre = [v for y, v in brit.items() if y < cut]
    post = [v for y, v in brit.items() if y >= cut]
    if len(pre) < 5 or len(post) < 3: continue
    med_pre = statistics.median(pre); med_post = statistics.median(post)
    shift = (med_post - med_pre) / med_pre * 100
    flag = ' *' if cut == 2017 else ''
    print(f'  {cut:>10}  {len(pre):>5}  {med_pre:>7.0f}  {len(post):>6}  {med_post:>8.0f}  {shift:>+5.1f}%{flag}')

print()
print('=== Test 2: Did April+May precipitation step-change in 2017? ===')
print('(by-station median total April+May precip, mm)')
print()
print(f'  {"station":<26}  {"pre 17":>7}  {"post 17":>7}  {"shift":>6}  {"n_pre":>5}/{"n_post":>5}')
for s in sorted(precip_by_station_year):
    yd = precip_by_station_year[s]
    pre = [v for y, v in yd.items() if y < 2017 and 1972 <= y]
    post = [v for y, v in yd.items() if y >= 2017]
    if len(pre) < 10 or len(post) < 4: continue
    med_pre = statistics.median(pre); med_post = statistics.median(post)
    shift = (med_post - med_pre) / med_pre * 100 if med_pre else 0
    flag = ''
    if abs(shift) > 15: flag = '  ‹‹ large'
    print(f'  {s:<26}  {med_pre:>7.0f}  {med_post:>7.0f}  {shift:>+5.1f}%  {len(pre):>5}/{len(post):>5}{flag}')

print()
print('=== Test 3: Did peak March snow on ground step-change? ===')
print('(by-station median peak March snow on ground, cm)')
print()
print(f'  {"station":<26}  {"pre 17":>7}  {"post 17":>7}  {"shift":>6}  {"n_pre":>5}/{"n_post":>5}')
for s in sorted(peak_snow_by_station_year):
    yd = peak_snow_by_station_year[s]
    pre = [v for y, v in yd.items() if y < 2017 and 1972 <= y and v > 0]
    post = [v for y, v in yd.items() if y >= 2017 and v > 0]
    if len(pre) < 10 or len(post) < 4: continue
    med_pre = statistics.median(pre); med_post = statistics.median(post)
    shift = (med_post - med_pre) / med_pre * 100 if med_pre else 0
    flag = ''
    if abs(shift) > 15: flag = '  ‹‹ large'
    print(f'  {s:<26}  {med_pre:>7.0f}  {med_post:>7.0f}  {shift:>+5.1f}%  {len(pre):>5}/{len(post):>5}{flag}')

print()
print('=== Britannia annual peak — full year-by-year ===')
print('(to eyeball trend vs step)')
print()
for y in sorted(brit):
    if y < 1985: continue
    bar = '█' * int(brit[y] / 200)
    flag = '  *' if y >= 2017 else ''
    print(f'  {y}: {brit[y]:>5.0f}  {bar}{flag}')

# Also: count of "extreme years" (>4500 m³/s) per decade
print()
print('=== Extreme freshet years (Britannia peak ≥ 4500 m³/s) per decade ===')
print()
for dec_start in range(1970, 2030, 10):
    n = sum(1 for y, v in brit.items() if dec_start <= y < dec_start + 10 and v >= 4500)
    n_total = sum(1 for y in brit if dec_start <= y < dec_start + 10)
    print(f'  {dec_start}s: {n} of {n_total} years')
