#!/usr/bin/env python3
"""
Adjudicate the May-2026 Facebook-thread debate over a "MAX Elevation at
Pembroke 1913-2026" chart with actual statistics instead of eyeballed
trend lines. Three competing claims were made in the thread:

  (i)   chart author / cyclical commenter: "no long-term trend"
  (ii)  deforestation-thesis commenter:    "1927-1945 flood cluster caused
        by post-logging watershed change"
  (iii) cyclical-precipitation commenter:  "decadal-scale precip cycle"

There is no century-length Pembroke or naturalized series in the archive
(Pembroke exists only as recent ORRPB rolling levels), so this substitutes
the two longest reachable daily records and is explicit about the swap:

  - 02KF005 Ottawa River at Britannia      level 1915-2024  (main-stem proxy)
  - 02OA039 Lac St-Louis at Pointe-Claire  level 1916-2025  (independent
            far-downstream cross-check; note: confounded by St-Lawrence /
            Moses-Saunders + Great-Lakes regulation, NOT a clean Ottawa proxy)

Battery, on the annual spring (Mar-Jun) maximum level:
  1. Mann-Kendall trend + Theil-Sen slope        -> tests claim (i)
  2. Pettitt single-changepoint test             -> tests "1927-45" vs "~1960"
  3. Pre/post variance + upper-tail occupancy     -> tests "tail compressed"
  4. Periodogram vs AR(1) red-noise Monte Carlo   -> tests claim (iii)
  5. Repeat 1-2 on Pointe-Claire                  -> basin vs gauge artifact

RELATIONSHIP TO THE EXISTING CASE FILE. This is deliberately a different
instrument from `stepchange_analysis.py` (Test A) and does NOT overturn it.
Test A asks a *conditional* question on Britannia *flow* (1960+, Apr-Jul):
"given a break exists, which year maximises the pre/post median shift?" and
answers 2017 (+19.3%). This script asks an *unconditional* question on
Britannia *level* over the *full 1915-2024 record*: "is there any single
significant step / monotonic trend / periodicity at all?" The two coexist:
a sharp, recent (2017) step in a noisy 110-yr level series is exactly the
regime a whole-record Pettitt test and a near-zero Mann-Kendall tau will
fail to flag, while the recent record-breaking tail this script surfaces
(top 3 of 110 spring peaks = 2019/2017/2023) is the same post-2017
intensification Test A and the Complete Summary document. See
docs/analysis for the write-up and the reconciliation section.

Stack: numpy/scipy/matplotlib (precedent: britannia_freshet_hydrograph.py).
"""
from __future__ import annotations
import csv
import collections
from pathlib import Path

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "wsc-hydrometric"
OUTDIR = ROOT / "data" / "community-notes"
STAMP = "2026-05-17"

SPRING = (3, 6)   # max within Mar 1 - Jun 30 = the freshet event
MIN_OBS = 40      # min valid daily obs inside the spring window for a usable year


def load_spring_max(slug: str):
    """Annual spring (Mar-Jun) maximum gauge level from the consolidated CSV."""
    by_year: dict[int, list[float]] = collections.defaultdict(list)
    with open(DATA / slug / "daily.csv") as f:
        for r in csv.DictReader(f):
            lv = r.get("level_m")
            if not lv:
                continue
            try:
                v = float(lv)
            except ValueError:
                continue
            y, m = int(r["date"][:4]), int(r["date"][5:7])
            if SPRING[0] <= m <= SPRING[1]:
                by_year[y].append(v)
    yrs, vals, sparse = [], [], []
    for y in sorted(by_year):
        if len(by_year[y]) >= MIN_OBS:
            yrs.append(y)
            vals.append(max(by_year[y]))
        else:
            sparse.append(y)
    yrs, vals = np.array(yrs), np.array(vals)
    full = set(range(yrs.min(), yrs.max() + 1))
    missing = sorted(full - set(yrs.tolist()) - set(sparse))
    return yrs, vals, sparse, missing


def mann_kendall(y):
    n = len(y)
    s = sum(np.sign(y[j] - y[i]) for i in range(n - 1) for j in range(i + 1, n))
    _, cnt = np.unique(y, return_counts=True)
    tie = sum(c * (c - 1) * (2 * c + 5) for c in cnt if c > 1)
    var = (n * (n - 1) * (2 * n + 5) - tie) / 18.0
    z = (s - np.sign(s)) / np.sqrt(var) if s != 0 else 0.0
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    tau = s / (0.5 * n * (n - 1))
    return s, tau, z, p


def theil_sen(x, y):
    slopes = [(y[j] - y[i]) / (x[j] - x[i])
              for i in range(len(x) - 1) for j in range(i + 1, len(x)) if x[j] != x[i]]
    sl = float(np.median(slopes))
    return sl, float(np.median(y - sl * x))


def pettitt(y):
    n = len(y)
    r = stats.rankdata(y)
    U = np.array([2 * r[:t].sum() - t * (n + 1) for t in range(1, n + 1)])
    k = int(np.argmax(np.abs(U)))
    K = abs(U[k])
    return k, K, min(2 * np.exp(-6 * K ** 2 / (n ** 3 + n ** 2)), 1.0)


def rednoise_spectrum(years, vals, sl, inter, label, png):
    """Periodogram of detrended spring-max vs a 5000-run AR(1) null."""
    full = np.arange(years.min(), years.max() + 1)
    resid = np.interp(full, years, vals) - (sl * full + inter)
    resid = resid - resid.mean()
    n = len(resid)
    r1 = float(np.corrcoef(resid[:-1], resid[1:])[0, 1])
    win = np.hanning(n)
    wnorm = np.sum(win ** 2)

    def pgram(v):
        return (np.abs(np.fft.rfft((v - v.mean()) * win)) ** 2) / wnorm

    obs = pgram(resid)
    freqs = np.fft.rfftfreq(n, d=1.0)
    with np.errstate(divide="ignore"):
        periods = np.where(freqs > 0, 1.0 / freqs, np.inf)

    rng = np.random.default_rng(42)
    sd = np.std(resid) * np.sqrt(max(1 - r1 ** 2, 1e-9))
    M = 5000
    sur = np.empty((M, len(obs)))
    for m in range(M):
        e = rng.normal(0, sd, n)
        s = np.empty(n)
        s[0] = e[0]
        for t in range(1, n):
            s[t] = r1 * s[t - 1] + e[t]
        sur[m] = pgram(s)
    p95, p99 = np.percentile(sur, 95, axis=0), np.percentile(sur, 99, axis=0)
    sig = [(round(periods[i], 1), round(obs[i], 4))
           for i in range(1, len(obs)) if obs[i] > p99[i] and 4 < periods[i] < n]

    plt.figure(figsize=(9, 5))
    m = freqs > 0
    plt.plot(periods[m], obs[m], "k-", lw=1.8, label="observed spring-max spectrum")
    plt.plot(periods[m], p95[m], "b--", lw=1, label="AR(1) red-noise 95%")
    plt.plot(periods[m], p99[m], "r--", lw=1, label="AR(1) red-noise 99%")
    plt.xscale("log")
    plt.gca().invert_xaxis()
    plt.xlabel("period (years)")
    plt.ylabel("power")
    plt.title(f"{label}: spectrum vs red-noise null (r1={r1:.2f}, n={n})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(png, dpi=120)
    plt.close()
    return r1, n, sig


def analyse(slug, code, label, png_series, png_spec=None):
    yrs, vals, sparse, missing = load_spring_max(slug)
    s, tau, z, p_mk = mann_kendall(vals)
    sl, inter = theil_sen(yrs, vals)
    k, K, p_pet = pettitt(vals)
    cp = int(yrs[k])
    pre, post = vals[:k + 1], vals[k + 1:]
    lev = stats.levene(pre, post)
    mw = stats.mannwhitneyu(pre, post, alternative="two-sided")
    thr = np.percentile(vals, 90)
    pre_x, post_x = int(np.sum(pre >= thr)), int(np.sum(post >= thr))
    top = sorted(zip(vals, yrs), reverse=True)[:6]

    print(f"\n{'='*74}\n{label}  ({code})  spring (Mar-Jun) maximum level\n{'='*74}")
    print(f"  years used {len(yrs)}  ({yrs.min()}-{yrs.max()}); gauge-datum metres")
    print(f"  sparse-spring years excluded: {sparse or 'none'}")
    print(f"  no-spring-data years (gauge gaps): {missing or 'none'}")
    print(f"\n  [1] Mann-Kendall: tau={tau:+.3f} Z={z:+.2f} p={p_mk:.3f} -> "
          f"{'SIGNIFICANT trend' if p_mk < 0.05 else 'NO significant monotonic trend'}")
    print(f"      Theil-Sen slope {sl*100*10:+.3f} cm/decade; "
          f"total {sl*(yrs.max()-yrs.min())*100:+.1f} cm over record")
    print(f"\n  [2] Pettitt: break after {cp}  K={K:.0f}  p={p_pet:.4f} -> "
          f"{'SIGNIFICANT step' if p_pet < 0.05 else 'no significant single step'}")
    print(f"      mean {pre.mean():.3f} -> {post.mean():.3f} ({post.mean()-pre.mean():+.3f} m)")
    print(f"\n  [3] Variance/tail across {cp}: std {pre.std(ddof=1):.3f} -> {post.std(ddof=1):.3f}")
    print(f"      Levene p={lev.pvalue:.4f} ({'changed' if lev.pvalue<0.05 else 'n.s.'}); "
          f"Mann-Whitney p={mw.pvalue:.4f}")
    print(f"      >=90th pctile ({thr:.3f}m): before {pre_x}/{len(pre)} "
          f"({pre_x/len(pre)*100:.0f}%)  after {post_x}/{len(post)} ({post_x/len(post)*100:.0f}%)")
    print(f"      top 6 spring peaks: {[(int(y), round(float(v),3)) for v,y in top]}")

    plt.figure(figsize=(11, 5))
    plt.scatter(yrs, vals, c="#c1543b", s=22, zorder=3, label="annual spring max")
    plt.plot(yrs, sl * yrs + inter, "g-", lw=1.5,
             label=f"Theil-Sen ({sl*100*10:+.2f} cm/decade)")
    plt.axvline(cp + 0.5, color="purple", ls="--",
                label=f"Pettitt break ~{cp} (p={p_pet:.3f})")
    plt.hlines(pre.mean(), yrs.min(), cp, color="navy", lw=2)
    plt.hlines(post.mean(), cp, yrs.max(), color="navy", lw=2, label="segment means")
    plt.axhline(thr, color="grey", ls=":", label="90th pctile")
    plt.title(f"{label} — annual spring (Mar-Jun) max level, {yrs.min()}-{yrs.max()}")
    plt.xlabel("year")
    plt.ylabel("level (m, gauge datum)")
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(png_series, dpi=120)
    plt.close()
    print(f"      [fig] {png_series.relative_to(ROOT)}")

    if png_spec:
        r1, n, sig = rednoise_spectrum(yrs, vals, sl, inter, label, png_spec)
        span = yrs.max() - yrs.min()
        print(f"\n  [4] Spectrum vs AR(1) red-noise (r1={r1:.2f}, n={n}): record resolves "
              f"~{span/20:.1f}/{span/30:.1f}/{span/40:.1f} cycles of a 20/30/40-yr period")
        print(f"      peaks above 99% red-noise envelope (4<P<n): {sig or 'NONE'}")
        print(f"      [fig] {png_spec.relative_to(ROOT)}")
    return cp, p_pet, tau, p_mk


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    b = analyse("britannia-ottawa-river", "02KF005",
                "Ottawa R. at Britannia (main-stem proxy)",
                OUTDIR / f"{STAMP}_thread_britannia_springmax.png",
                OUTDIR / f"{STAMP}_thread_britannia_spectrum.png")
    pc = analyse("pointe-claire-lac-st-louis", "02OA039",
                 "Lac St-Louis at Pointe-Claire (independent cross-check)",
                 OUTDIR / f"{STAMP}_thread_pointeclaire_springmax.png")
    print(f"\n{'='*74}\nCROSS-CHECK\n{'='*74}")
    print(f"  Britannia     break ~{b[0]} (p={b[1]:.3f}); MK tau={b[2]:+.3f} p={b[3]:.3f}")
    print(f"  Pointe-Claire break ~{pc[0]} (p={pc[1]:.3f}); MK tau={pc[2]:+.3f} p={pc[3]:.3f}")
    print(f"  -> replicates within ~6 yr on the independent gauge? "
          f"{'YES (basin signal)' if abs(b[0]-pc[0])<=6 else 'NO (gauge/regulation-specific)'}")


if __name__ == "__main__":
    main()
