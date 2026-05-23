#!/usr/bin/env python3
"""
Test whether spring freshet *shape* (peakedness, timing) explains peak stage
beyond what total *volume* alone does, and whether that shape has shifted in
the post-2016 regime.

Motivation: a public Facebook-thread argument (May 2026) claimed that the
1951-2015 relationship between "total freshet volume passing Des Joachims"
and "peak spring level at Pembroke" is unchanged in 2016-2026, and therefore
dam-management changes can't have caused recent flooding. A thread commenter
correctly pushed back that the cumulative-volume metric throws away timing
and concentration. This script runs that pushback as actual statistics.

Data constraint: the local wsc_daily archive has only ~7-10 years of daily
flow at Bryson / Portage-du-Fort. The only Ottawa main-stem gauge with a
multi-decade daily flow series is Britannia (02KF005, 1960-2024). So:

  - Predictor "hydrograph" = Britannia daily flow, Mar 15 - Jun 15.
  - Response               = Britannia spring max level same year.
  - Window robustness pass = Apr 1 - Jun 15 (the conventional WMP date).

This is a same-gauge fit, so the flow-to-level link is essentially a rating
curve at high stage. That is exactly the regime where the question is sharp:
holding volume fixed, does shape add explanatory power, and has the shape
distribution shifted at given volume since 2016?

Tests:
  [A] Replicate Steve's univariate: poly2(V) -> level_max. Report R^2 and
      pre/post (1960-2015 vs 2016-2024) residual distributions.
  [B] Add Qpk: level_max ~ V + Qpk. Partial F, adj-R^2, AIC vs [A].
  [C] Add peakedness Qpk/Qmean instead of Qpk: same comparison.
  [D] Test whether peakedness | V has shifted post-2016 (residuals from
      peakedness ~ poly2(V); pre/post Mann-Whitney + t).
  [E] Test whether COM (center-of-mass DOY) has shifted post-2016.
  [F] Repeat [A]-[C] with Apr 1 - Jun 15 window as robustness.

Stack: numpy/scipy/matplotlib (precedent: thread_trend_changepoint_cycle.py).
"""
from __future__ import annotations
import csv
import collections
from datetime import date as Date
from pathlib import Path

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "wsc-hydrometric"
OUTDIR = ROOT / "data" / "community-notes"
STAMP = "2026-05-23"

SPRING_LEVEL = (3, 6)          # Mar-Jun for annual peak level
WINDOWS = {                    # (start_md, end_md) inclusive
    "mar15_jun15": ((3, 15), (6, 15)),  # Steve's window
    "apr01_jun15": ((4, 1),  (6, 15)),  # WMP convention (Dan Poole)
}
MIN_FRAC = 0.85                # min fraction of window days with flow obs
POST_2016_FROM = 2016


# ----------------------------------------------------------------------
# Loaders
# ----------------------------------------------------------------------
def load_daily_flow(slug: str):
    """Return {date -> flow_cms} ignoring blanks."""
    out: dict[Date, float] = {}
    with open(DATA / slug / "daily.csv") as f:
        for r in csv.DictReader(f):
            q = r.get("flow_cms") or ""
            if not q:
                continue
            try:
                v = float(q)
            except ValueError:
                continue
            d = Date.fromisoformat(r["date"])
            out[d] = v
    return out


def load_spring_max_level(slug: str):
    """{year -> max level (m)} over SPRING_LEVEL inclusive."""
    by_year: dict[int, list[float]] = collections.defaultdict(list)
    with open(DATA / slug / "daily.csv") as f:
        for r in csv.DictReader(f):
            lv = r.get("level_m") or ""
            if not lv:
                continue
            try:
                v = float(lv)
            except ValueError:
                continue
            d = Date.fromisoformat(r["date"])
            if SPRING_LEVEL[0] <= d.month <= SPRING_LEVEL[1]:
                by_year[d.year].append(v)
    return {y: max(vs) for y, vs in by_year.items() if len(vs) >= 40}


# ----------------------------------------------------------------------
# Freshet metrics per (year, window)
# ----------------------------------------------------------------------
def gini(x: np.ndarray) -> float:
    x = np.sort(np.asarray(x, float))
    if x.sum() == 0 or len(x) == 0:
        return 0.0
    n = len(x)
    cum = np.cumsum(x)
    return float((n + 1 - 2 * np.sum(cum) / cum[-1]) / n)


def metrics_for_year(year: int, flow_by_date: dict[Date, float], window):
    (m0, d0), (m1, d1) = window
    start = Date(year, m0, d0)
    end = Date(year, m1, d1)
    window_days = (end.toordinal() - start.toordinal()) + 1
    days = []
    qs = []
    cur = start
    while cur <= end:
        if cur in flow_by_date:
            days.append(cur)
            qs.append(flow_by_date[cur])
        cur = Date.fromordinal(cur.toordinal() + 1)
    if len(qs) < int(window_days * MIN_FRAC):
        return None
    qs = np.array(qs, float)
    V = float(qs.sum() * 86400.0)              # m^3 over window
    qpk = float(qs.max())
    qmean = float(qs.mean())
    peakedness = qpk / qmean if qmean > 0 else np.nan
    g = gini(qs)
    cum = np.cumsum(qs)
    half_idx = int(np.searchsorted(cum, cum[-1] / 2.0))
    com_doy = days[min(half_idx, len(days) - 1)].timetuple().tm_yday
    return dict(V=V, qpk=qpk, qmean=qmean, peakedness=peakedness, gini=g,
                com_doy=com_doy, n_days=len(qs))


# ----------------------------------------------------------------------
# Stats helpers
# ----------------------------------------------------------------------
def fit_ols(X: np.ndarray, y: np.ndarray):
    """Return (beta, yhat, resid, R2, adjR2, AIC). X must include intercept col."""
    n, k = X.shape
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ beta
    resid = y - yhat
    ss_res = float((resid ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    adj = 1.0 - (1.0 - r2) * (n - 1) / max(n - k, 1)
    sig2 = ss_res / n
    aic = n * np.log(sig2) + 2 * k if sig2 > 0 else float("nan")
    return beta, yhat, resid, r2, adj, aic


def partial_F(rss_small, rss_big, df_small, df_big, n):
    # df = number of parameters (incl intercept)
    num = (rss_small - rss_big) / (df_big - df_small)
    den = rss_big / (n - df_big)
    f = num / den
    p = 1.0 - stats.f.cdf(f, df_big - df_small, n - df_big)
    return float(f), float(p)


# ----------------------------------------------------------------------
# Core analysis on a single window
# ----------------------------------------------------------------------
def run_window(label_window: str, window, flow_by_date, level_max):
    years = sorted(y for y in level_max if y >= 1960)
    rows = []
    for y in years:
        m = metrics_for_year(y, flow_by_date, window)
        if m is None:
            continue
        rows.append({"year": y, "level": level_max[y], **m})
    yrs = np.array([r["year"] for r in rows])
    Z = np.array([r["level"] for r in rows])
    V = np.array([r["V"] for r in rows]) / 1e9          # billions m^3
    Qpk = np.array([r["qpk"] for r in rows])
    Qmn = np.array([r["qmean"] for r in rows])
    PK = np.array([r["peakedness"] for r in rows])
    G = np.array([r["gini"] for r in rows])
    COM = np.array([r["com_doy"] for r in rows])
    n = len(yrs)
    post = yrs >= POST_2016_FROM
    print(f"\n{'='*76}\nWindow: {label_window}   years used: {n}  ({yrs.min()}-{yrs.max()})")
    print(f"  pre-2016: {(~post).sum()}    post-2016: {post.sum()}")

    # --- [A] Steve's model: poly2(V) -> level
    ones = np.ones(n)
    X_A = np.column_stack([ones, V, V ** 2])
    betaA, yhatA, resA, r2A, adjA, aicA = fit_ols(X_A, Z)
    rss_A = float((resA ** 2).sum())
    print(f"\n  [A] level ~ poly2(V):           R^2={r2A:.4f}  adjR^2={adjA:.4f}  AIC={aicA:.2f}")

    # --- [B] add Qpk
    X_B = np.column_stack([ones, V, V ** 2, Qpk])
    betaB, yhatB, resB, r2B, adjB, aicB = fit_ols(X_B, Z)
    rss_B = float((resB ** 2).sum())
    fB, pB = partial_F(rss_A, rss_B, 3, 4, n)
    print(f"  [B] + Qpk:                      R^2={r2B:.4f}  adjR^2={adjB:.4f}  AIC={aicB:.2f}"
          f"  partial F={fB:.2f} p={pB:.4g}")

    # --- [C] add peakedness Qpk/Qmean instead
    X_C = np.column_stack([ones, V, V ** 2, PK])
    betaC, yhatC, resC, r2C, adjC, aicC = fit_ols(X_C, Z)
    rss_C = float((resC ** 2).sum())
    fC, pC = partial_F(rss_A, rss_C, 3, 4, n)
    print(f"  [C] + peakedness Qpk/Qmean:     R^2={r2C:.4f}  adjR^2={adjC:.4f}  AIC={aicC:.2f}"
          f"  partial F={fC:.2f} p={pC:.4g}")

    # --- proxy-variable diagnostic: marginal R^2 of V given Qpk, and vice versa
    X_Qonly = np.column_stack([ones, Qpk, Qpk ** 2])
    _, _, _, r2_Qonly, _, _ = fit_ols(X_Qonly, Z)
    X_VQ = np.column_stack([ones, V, V ** 2, Qpk, Qpk ** 2])
    _, _, _, r2_VQ, _, _ = fit_ols(X_VQ, Z)
    r_VQ = float(np.corrcoef(V, Qpk)[0, 1])
    delta_V_given_Q = r2_VQ - r2_Qonly
    delta_Q_given_V = r2_VQ - r2A
    print(f"\n  Proxy-variable diagnostic (does V add anything beyond Qpk?):")
    print(f"      R^2(V only, poly2)                 = {r2A:.4f}")
    print(f"      R^2(Qpk only, poly2)               = {r2_Qonly:.4f}")
    print(f"      R^2(V + Qpk, both poly2)           = {r2_VQ:.4f}")
    print(f"      V unique add-value beyond Qpk      = {delta_V_given_Q:+.4f}  ({delta_V_given_Q*100:+.2f} pp)")
    print(f"      Qpk unique add-value beyond V      = {delta_Q_given_V:+.4f}  ({delta_Q_given_V*100:+.2f} pp)")
    print(f"      correlation V vs Qpk               = {r_VQ:.3f}")

    # --- pre/post residual structure from [A]
    pre_res = resA[~post]
    post_res = resA[post]
    if post.sum() >= 3:
        t = stats.ttest_ind(pre_res, post_res, equal_var=False)
        u = stats.mannwhitneyu(pre_res, post_res, alternative="two-sided")
        print(f"\n  pre/post residuals from [A]:    pre mean {pre_res.mean():+.3f} m  "
              f"post mean {post_res.mean():+.3f} m   "
              f"t-p={t.pvalue:.3f}  MW-p={u.pvalue:.3f}")
    else:
        print(f"\n  pre/post residuals from [A]:    post n={post.sum()} too small")

    # --- [D] Has peakedness | V shifted post-2016?
    Xpk = np.column_stack([ones, V, V ** 2])
    bpk, *_ = np.linalg.lstsq(Xpk, PK, rcond=None)
    pk_pred = Xpk @ bpk
    pk_res = PK - pk_pred
    if post.sum() >= 3:
        t = stats.ttest_ind(pk_res[~post], pk_res[post], equal_var=False)
        u = stats.mannwhitneyu(pk_res[~post], pk_res[post], alternative="two-sided")
        print(f"\n  [D] peakedness residuals | V:   pre mean {pk_res[~post].mean():+.3f}  "
              f"post mean {pk_res[post].mean():+.3f}   "
              f"t-p={t.pvalue:.3f}  MW-p={u.pvalue:.3f}")
        print(f"      raw peakedness:             pre median {np.median(PK[~post]):.2f}  "
              f"post median {np.median(PK[post]):.2f}")

    # --- [E] Has COM shifted?
    if post.sum() >= 3:
        t = stats.ttest_ind(COM[~post], COM[post], equal_var=False)
        u = stats.mannwhitneyu(COM[~post], COM[post], alternative="two-sided")
        print(f"\n  [E] freshet center-of-mass DOY: pre median {np.median(COM[~post]):.0f}  "
              f"post median {np.median(COM[post]):.0f}   "
              f"t-p={t.pvalue:.3f}  MW-p={u.pvalue:.3f}")

    # --- plot 1: Steve-style scatter, our gauge
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(V[~post], Z[~post], c="#c1543b", s=28, label=f"1960-2015 (n={(~post).sum()})")
    ax.scatter(V[post], Z[post], c="#2c6aa0", s=46,
               edgecolors="k", linewidths=0.4, label=f"2016-2024 (n={post.sum()})")
    Vline = np.linspace(V.min(), V.max(), 100)
    Zline = betaA[0] + betaA[1] * Vline + betaA[2] * Vline ** 2
    ax.plot(Vline, Zline, "k--", lw=1.2, label=f"poly2(V) fit  R^2={r2A:.2f}")
    for i, yr in enumerate(yrs):
        if Z[i] >= np.percentile(Z, 92) or yr >= 2017:
            ax.annotate(str(int(yr)), (V[i], Z[i]), fontsize=7,
                        xytext=(3, 2), textcoords="offset points")
    ax.set_xlabel(f"freshet volume at Britannia, {label_window} (billions m³)")
    ax.set_ylabel("annual spring max level at Britannia (m)")
    ax.set_title(f"Britannia: volume vs peak level, {label_window} ({yrs.min()}-{yrs.max()})")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTDIR / f"{STAMP}_peakedness_volume_{label_window}.png", dpi=120)
    plt.close(fig)

    # --- plot 2: peakedness vs V, pre/post
    if post.sum() >= 3:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(V[~post], PK[~post], c="#c1543b", s=28, label=f"1960-2015")
        ax.scatter(V[post], PK[post], c="#2c6aa0", s=46,
                   edgecolors="k", linewidths=0.4, label=f"2016-2024")
        PKline = bpk[0] + bpk[1] * Vline + bpk[2] * Vline ** 2
        ax.plot(Vline, PKline, "k--", lw=1.2, label="poly2(V) fit to peakedness")
        for i, yr in enumerate(yrs):
            if yr >= 2017:
                ax.annotate(str(int(yr)), (V[i], PK[i]), fontsize=7,
                            xytext=(3, 2), textcoords="offset points")
        ax.set_xlabel(f"freshet volume (billions m³)")
        ax.set_ylabel("peakedness = Qpk / Qmean")
        ax.set_title(f"Britannia peakedness vs volume, {label_window}")
        ax.grid(alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(OUTDIR / f"{STAMP}_peakedness_vs_V_{label_window}.png", dpi=120)
        plt.close(fig)

    # --- plot 3: residuals from [A] by year
    fig, ax = plt.subplots(figsize=(10, 4.2))
    cmask = yrs < POST_2016_FROM
    ax.bar(yrs[cmask], resA[cmask], color="#c1543b", label="1960-2015")
    ax.bar(yrs[~cmask], resA[~cmask], color="#2c6aa0", label="2016-2024")
    ax.axhline(0, color="k", lw=0.7)
    ax.set_xlabel("year")
    ax.set_ylabel("residual (m): observed − poly2(V) prediction")
    ax.set_title(f"Pre vs post 2016 residuals from poly2(V), {label_window}")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTDIR / f"{STAMP}_residuals_{label_window}.png", dpi=120)
    plt.close(fig)

    return dict(n=n, r2A=r2A, r2B=r2B, r2C=r2C, aicA=aicA, aicB=aicB, aicC=aicC,
                pB=pB, pC=pC, post_n=int(post.sum()))


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    flow = load_daily_flow("britannia-ottawa-river")
    lvl = load_spring_max_level("britannia-ottawa-river")
    print(f"Britannia daily-flow records: {len(flow)}  "
          f"({min(flow):%Y-%m-%d} - {max(flow):%Y-%m-%d})")
    print(f"Britannia spring-max levels:  {len(lvl)} years  "
          f"({min(lvl)}-{max(lvl)})")

    results = {}
    for label, win in WINDOWS.items():
        results[label] = run_window(label, win, flow, lvl)

    print(f"\n{'='*76}\nSUMMARY")
    print(f"  window           n  R²(V)   R²(V+Qpk)  R²(V+peak)   partial-F p (Qpk)  (peak)")
    for label, r in results.items():
        print(f"  {label:16s} {r['n']:3d}  {r['r2A']:.3f}     {r['r2B']:.3f}      "
              f"{r['r2C']:.3f}       {r['pB']:.4g}        {r['pC']:.4g}")


if __name__ == "__main__":
    main()
