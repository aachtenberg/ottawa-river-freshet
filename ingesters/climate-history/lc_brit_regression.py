"""
Lac Coulonge daily-max peak vs Britannia peak flow regression, segmented
pre-/post-2017. Tests the case-file hypothesis: did Bryson operations shift
the relationship between basin-scale inflow and lake-level peak?

Hypothesis:
  - If only intercept shifted up post-2017 → operations signature
    (lake peaks higher for a given inflow)
  - If only slope shifted → something hydraulic in the basin changed
  - If neither → no measurable per-event amplification
  - If both → mixed effect

Data sources:
  - Lac Coulonge: lac-coulonge-monthly-1972-2026.csv (daily_max column)
  - Britannia:    wsc-hydrometric/britannia-ottawa-river/daily.csv
"""

import csv, math
from collections import defaultdict
from pathlib import Path

ROOT = Path('/home/aachten/repos/homelab-infra/freshet-public/data')
LC_PATH = ROOT / 'lac-coulonge-monthly-1972-2026.csv'
BRIT_PATH = ROOT / 'wsc-hydrometric/britannia-ottawa-river/daily.csv'

# 1) Lac Coulonge annual daily_max
lc = {}
with open(LC_PATH) as f:
    for r in csv.DictReader(f):
        try:
            y = int(r['year']); v = float(r['daily_max'])
            lc[y] = v
        except (ValueError, KeyError):
            pass

# 2) Britannia annual peak (from daily flow records). Only April–July to keep
#    it specifically about the freshet event — winter/storm peaks would be
#    a different process.
brit_annual = defaultdict(lambda: 0.0)
with open(BRIT_PATH) as f:
    for r in csv.DictReader(f):
        d = r.get('date', '')
        try:
            y = int(d[:4]); m = int(d[5:7]); v = float(r['flow_cms'])
        except (ValueError, KeyError):
            continue
        if 4 <= m <= 7 and v > brit_annual[y]:
            brit_annual[y] = v

# 3) Match by year. Only include years where both have non-trivial values.
pairs = []
for y in sorted(lc):
    if y < 1972 or y > 2026:  # Britannia coverage starts 1960; LC starts 1972
        continue
    bv = brit_annual.get(y, 0)
    if bv < 500:  # filter out missing/sparse years
        continue
    pairs.append((y, lc[y], bv))

pre  = [(y, l, b) for (y, l, b) in pairs if y <= 2016]
post = [(y, l, b) for (y, l, b) in pairs if y >= 2017]

def ols(pairs):
    """Returns (slope, intercept, r2, n, residuals_at_each_point)"""
    n = len(pairs)
    if n < 3: return None
    xs = [b for (_, _, b) in pairs]
    ys = [l for (_, l, _) in pairs]
    mx = sum(xs)/n
    my = sum(ys)/n
    sxy = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
    sxx = sum((xs[i]-mx)**2 for i in range(n))
    syy = sum((ys[i]-my)**2 for i in range(n))
    slope = sxy / sxx if sxx else 0
    intercept = my - slope*mx
    yhat = [intercept + slope*x for x in xs]
    ssr = sum((yhat[i]-my)**2 for i in range(n))
    sst = syy if syy else 1
    r2 = ssr / sst
    # Per-year residual (LC observed - LC predicted by the line)
    residuals = [(pairs[i][0], ys[i] - yhat[i]) for i in range(n)]
    return slope, intercept, r2, n, residuals

print(f'Years matched: pre-2017={len(pre)}  post-2017={len(post)}')
print()

for label, data in [('PRE-2017 (1972-2016)', pre), ('POST-2017 (2017-2026)', post)]:
    res = ols(data)
    if not res:
        print(f'{label}: insufficient data')
        continue
    slope, intercept, r2, n, _ = res
    print(f'{label}:  n={n}')
    print(f'  Lac Coulonge peak (m) = {intercept:.4f} + {slope:.6f} × Britannia peak (m³/s)')
    print(f'  R² = {r2:.3f}')
    # Predict at common reference flows
    print(f'  Predicted lake peak at Britannia = 3000 m³/s: {intercept + slope*3000:.3f} m')
    print(f'  Predicted lake peak at Britannia = 5000 m³/s: {intercept + slope*5000:.3f} m')
    print()

# 4) Joint analysis: at the post-2017 mean Britannia peak, what would the
#    pre-2017 line have predicted vs. what the post-2017 line predicts?
slope_pre,  int_pre,  _, _, _ = ols(pre)
slope_post, int_post, _, _, _ = ols(post)

# Common Britannia reference flows
print('=== Direct comparison at common inflow levels ===')
for q in [2500, 3000, 3500, 4000, 4500, 5000, 5500]:
    pre_pred = int_pre + slope_pre*q
    post_pred = int_post + slope_post*q
    delta_cm = (post_pred - pre_pred) * 100
    print(f'  At Britannia = {q} m³/s:  pre-line predicts {pre_pred:.3f} m, post-line predicts {post_pred:.3f} m  →  Δ {delta_cm:+.1f} cm')

print()
print('=== Per-year residuals from the PRE-2017 line ===')
print('(positive = lake peaked higher than the pre-2017 relationship would predict for that Britannia flow)')
print()
# Compute residuals for ALL years using the pre-2017 fit
print(f"  {'year':>4}  {'Britannia':>10}  {'LC observed':>11}  {'LC predicted':>12}  {'residual':>9}")
for y, l, b in pairs:
    pred = int_pre + slope_pre * b
    resid_cm = (l - pred) * 100
    flag = ''
    if y >= 2017: flag = '  *post-2017*'
    if abs(resid_cm) >= 30: flag += '  ‹‹ large'
    print(f'  {y:>4}  {b:>10.0f}  {l:>11.2f}  {pred:>12.2f}  {resid_cm:>+8.1f} cm{flag}')

# Mean residual: post-2017 vs pre-2017
post_resid = [(l - (int_pre + slope_pre*b)) * 100 for (y,l,b) in pairs if y >= 2017]
pre_resid  = [(l - (int_pre + slope_pre*b)) * 100 for (y,l,b) in pairs if y <= 2016]
print()
print(f'Mean residual pre-2017 (by definition ~0): {sum(pre_resid)/len(pre_resid):+.1f} cm  (n={len(pre_resid)})')
print(f'Mean residual post-2017 (vs pre-2017 line): {sum(post_resid)/len(post_resid):+.1f} cm  (n={len(post_resid)})')
print()
print(f'Slope shift:     pre={slope_pre*1000:.4f} m per 1000 m³/s   post={slope_post*1000:.4f} m per 1000 m³/s   Δ={(slope_post-slope_pre)*1000:+.4f}')
print(f'Intercept shift: pre={int_pre:.3f} m                       post={int_post:.3f} m                       Δ={(int_post-int_pre)*100:+.1f} cm')
