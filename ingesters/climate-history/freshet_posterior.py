#!/usr/bin/env python3
"""
V3 — Bayesian hybrid: continuously-updating freshet posterior for Lac Coulonge.

Ties V1 and V2 together. V1 (freshet_probability.py) is the pre-freshet seasonal
prior — "going into the season, given snowpack and winter precip, what's the
chance we hit each threshold?" V2 (freshet_conditional.py) is the during-freshet
conditional likelihood — "given the lake's level/rate/day today, what peak does
that imply?" V3 combines them via Bayes into one posterior that starts at the V1
prior and tightens as the freshet unfolds.

The combination — why a likelihood RATIO, not a naive product:
    V2 already estimates P(peak | state) directly by analog matching, so it
    carries its OWN implicit prior — the analog base rate P_2(peak). Multiplying
    V2's conditional straight onto V1's prior would double-count that base rate.
    And multiplying V2 in EVERY day would massively over-tighten, because
    consecutive days are highly autocorrelated (today's level ~ yesterday's).

    So V3 uses V2 as a likelihood ratio against its own marginal, which is the
    standard way to swap one model's prior for another's:

        posterior_t(b)  ∝  P_1(b) · [ P_2(b | state_t) / P_2(b) ]

    over peak-value bins b (the gaps between the V1/V2 threshold ladder). The
    bracket is exactly the information gained by observing today's state, with
    V2's implicit base rate divided out. Computed fresh each day from state_t —
    the "continuous update" is that state_t evolves daily, not a recursive filter
    that would have to model day-to-day transitions and autocorrelation.

    Behavior this produces:
      - Pre-freshet / uninformative state: P_2(b|state) ≈ P_2(b), ratio ≈ 1,
        posterior ≈ V1 prior. Wide bands, honest "don't know yet."
      - Mid-freshet: as the level climbs the conditional concentrates, the ratio
        sharpens, the posterior moves and tightens.
      - Once the level passes a threshold, V2 floors that survival to 1 and the
        posterior mass moves above it.

Honest limits:
    - Inherits V1's (54-yr peaks, ±10pt tails) and V2's (~36 daily seasons,
      4 super-flood events) limits. The posterior is only as calibrated as its
      inputs; see each module's calibration check.
    - Per-threshold isotonic calibration in V2 can break cross-threshold
      monotonicity of the survival curve; V3 re-enforces a non-increasing
      survival before converting to a peak-bin pmf.
    - Bins are the threshold ladder, so resolution is coarse between thresholds.

Usage:
    # Posterior as of a date (V1 prior for that year × V2 likelihood for the day):
    python3 freshet_posterior.py --asof 2019-04-20

    # Tightening trajectory across one season:
    python3 freshet_posterior.py --year 2019

    # Does the posterior beat the prior alone? (Brier, leave-one-out):
    python3 freshet_posterior.py --retrospective

    # Dashboard JSON:
    python3 freshet_posterior.py --asof 2026-04-20 --json

Stdlib only.
"""

from __future__ import annotations

import argparse
import json

from freshet_probability import (
    THRESHOLDS,
    DEFAULT_POST_2017_WEIGHT,
    build_history,
    per_year_climate,
    compute_probabilities,
)
from freshet_conditional import (
    load_daily,
    build_analogs,
    compute_conditional,
    fit_calibrators,
    season_peak,
    rate_at,
    norm_doy,
    FRESHET_DOY_START,
    FRESHET_DOY_END,
    DAILY_CSV,
)
import csv

TVALS = [t for t, _ in THRESHOLDS]
LABELS = {t: lbl for t, lbl in THRESHOLDS}
PRIOR_FLOOR = 1e-3   # keeps V1-zero tail bins revivable by a strong likelihood
# Likelihood-ratio regularization. The marginal is empirical over ~36 years, so
# a leave-one-out-empty bin (e.g. the 109.17 record bin) would otherwise blow the
# ratio up. Smooth the conditional and marginal IDENTICALLY toward uniform so an
# empty bin gives ratio ~ 1 (no information), and cap the per-bin ratio so no one
# coarse bin can dominate the posterior.
SMOOTH_EPS = 0.08
RATIO_CAP = 10.0

# Season checkpoints for the --year trajectory (month, day).
CHECKPOINTS = [(3, 1), (3, 20), (4, 1), (4, 15), (5, 1), (5, 15), (6, 1)]


# ---------------------------------------------------------------------------
# Survival <-> peak-bin pmf.
#
# Bins are the gaps in the threshold ladder: bin 0 = (-inf, T0), bin k =
# [T_{k-1}, T_k) for k in 1..N-1, bin N = [T_{last}, +inf). A survival curve
# S(T)=P(peak>=T) at the N thresholds maps 1:1 to an (N+1)-bin pmf.
# ---------------------------------------------------------------------------

def _enforce_monotone(surv: list[float]) -> list[float]:
    """Clamp a survival curve to be non-increasing in threshold and within
    [0,1]. Per-threshold isotonic calibration in V2 can introduce small
    violations; this restores a valid survival function."""
    out = []
    prev = 1.0
    for s in surv:
        s = min(max(s, 0.0), prev)
        out.append(s)
        prev = s
    return out


def survival_to_pmf(surv: list[float]) -> list[float]:
    """N-threshold survival -> normalized (N+1)-bin pmf."""
    s = _enforce_monotone(surv)
    pmf = [max(0.0, 1.0 - s[0])]
    for i in range(1, len(s)):
        pmf.append(max(0.0, s[i - 1] - s[i]))
    pmf.append(max(0.0, s[-1]))
    total = sum(pmf) or 1.0
    return [p / total for p in pmf]


def pmf_to_survival(pmf: list[float]) -> dict[float, float]:
    """(N+1)-bin pmf -> survival dict {threshold: P(peak>=threshold)}."""
    return {TVALS[j]: sum(pmf[j + 1:]) for j in range(len(TVALS))}


# ---------------------------------------------------------------------------
# The three ingredients.
# ---------------------------------------------------------------------------

def v1_prior_pmf(year: int, history: list[dict]) -> list[float] | None:
    """V1 seasonal prior for `year` (leave-one-out), as a peak-bin pmf.
    None if that year lacks the snowpack/precip climate inputs V1 needs."""
    c = per_year_climate(year)
    if c["peak_sog_cm"] is None or c["cold_precip_mm"] is None:
        return None
    res = compute_probabilities(
        c["peak_sog_cm"], c["cold_precip_mm"], history, exclude_year=year
    )
    surv = [res["probabilities"][f"{t:.2f}"]["prob"] for t in TVALS]
    return survival_to_pmf(surv)


def v2_marginal_pmf(
    daily: dict[int, dict[int, float]],
    exclude_year: int | None,
    post_2017_weight: float,
) -> list[float]:
    """V2's implicit climatological base rate over peak bins — the era-weighted
    frequency of each season-peak bin across the daily record. This is the
    denominator the V2 conditional is divided by."""
    items = [(y, season_peak(s)) for y, s in daily.items() if y != exclude_year]

    def w(y):
        return post_2017_weight if y >= 2017 else 1.0

    total = sum(w(y) for y, _ in items) or 1.0
    surv = [sum(w(y) for y, pk in items if pk >= t) / total for t in TVALS]
    return survival_to_pmf(surv)


def v2_likelihood_pmf(
    doy: int, level: float, rate: float,
    analogs: list[dict], calibrators, exclude_year: int | None,
    post_2017_weight: float,
) -> list[float]:
    """V2 conditional P(peak | state today), as a peak-bin pmf."""
    res = compute_conditional(
        doy, level, rate, analogs, exclude_year=exclude_year,
        post_2017_weight=post_2017_weight, calibrators=calibrators,
    )
    surv = [res["season_end"][f"{t:.2f}"]["prob"] for t in TVALS]
    return survival_to_pmf(surv)


# Upper edge of each peak bin: bin i = [edge_{i-1}, BIN_UPPERS[i]). A bin whose
# upper edge is at/below the current level is physically impossible — the season
# peak is always >= today's level — so it is zeroed regardless of the models.
BIN_UPPERS = TVALS + [float("inf")]

# Once the lake has receded this far below its season-max-to-date, the freshet
# has crested and the season peak IS that max — Lac Coulonge's regulated freshet
# is single-crested at the half-metre scale, so no higher crest follows. The
# margin sits safely above 2019's 0.37 m mid-double-crest dip, so a genuine
# second crest is never collapsed prematurely.
CREST_DROP_M = 0.50


def _bin_index(level: float) -> int:
    """Index of the peak bin containing `level`."""
    for i, upper in enumerate(BIN_UPPERS):
        if level < upper:
            return i
    return len(BIN_UPPERS) - 1


def posterior_pmf(
    prior: list[float], cond: list[float], marg: list[float], level: float
) -> list[float]:
    """Bayes: posterior(b) ∝ prior(b) · cond(b)/marg(b), with the likelihood
    ratio regularized (identical uniform smoothing of cond and marg, plus a
    cap) so climatologically-empty bins contribute no information rather than
    exploding, and with bins below the current level zeroed as impossible."""
    n = len(prior)
    u = 1.0 / n
    post = []
    for i, (p, c, m) in enumerate(zip(prior, cond, marg)):
        if BIN_UPPERS[i] <= level:
            post.append(0.0)  # peak can't fall in a bin entirely below today
            continue
        cs = (1.0 - SMOOTH_EPS) * c + SMOOTH_EPS * u
        ms = (1.0 - SMOOTH_EPS) * m + SMOOTH_EPS * u
        lr = min(max(cs / ms, 1.0 / RATIO_CAP), RATIO_CAP)
        post.append((p + PRIOR_FLOOR) * lr)
    total = sum(post) or 1.0
    return [p / total for p in post]


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------

def compute_posterior_for_state(
    year: int, doy: int, level: float, rate: float,
    history, daily, analogs, calibrators, post_2017_weight: float,
) -> dict | None:
    """Full V3 posterior for one (year, state). None if V1 inputs are missing."""
    prior = v1_prior_pmf(year, history)
    if prior is None:
        return None
    marg = v2_marginal_pmf(daily, year, post_2017_weight)
    cond = v2_likelihood_pmf(doy, level, rate, analogs, calibrators, year, post_2017_weight)
    # The season peak is at least the highest level seen so far this season, not
    # just today's level — so on the receding limb the posterior still respects
    # the peak already achieved.
    series = daily[year]
    seen = [v for dd, v in series.items() if FRESHET_DOY_START <= dd <= doy]
    # Before the freshet window opens there's no in-season history yet; fall
    # back to today's level as the floor.
    max_to_date = max(seen) if seen else level
    if max_to_date - level >= CREST_DROP_M:
        # Freshet has crested and clearly receded — the season peak is the
        # max-to-date. Collapse the posterior to that bin (point mass).
        post = [0.0] * len(prior)
        post[_bin_index(max_to_date)] = 1.0
    else:
        post = posterior_pmf(prior, cond, marg, max_to_date)
    return {
        "prior_survival": pmf_to_survival(prior),
        "likelihood_survival": pmf_to_survival(cond),
        "posterior_survival": pmf_to_survival(post),
    }


def _state_on(daily, year: int, m: int, d: int):
    """(doy, level, rate) for a calendar date, or None if unavailable."""
    series = daily.get(year)
    if not series:
        return None
    doy = norm_doy(year, m, d)
    level = series.get(doy)
    if level is None:
        return None
    rate = rate_at(series, doy)
    if rate is None:
        return None
    return doy, level, rate


def _fmt_row(label_left, surv):
    cells = " ".join(f"{surv[t]:>6.0%}" for t in TVALS)
    return f"  {label_left:<12} {cells}"


def _threshold_header():
    cells = " ".join(f"{t:>6.2f}" for t in TVALS)
    return f"  {'':<12} {cells}"


def print_trajectory(year, daily, history, analogs, calibrators, post_2017_weight):
    actual = season_peak(daily[year]) if year in daily else None
    print(f"\nV3 posterior trajectory — {year}"
          + (f"  (actual season peak: {actual:.2f} m)" if actual else ""))
    print(_threshold_header())
    prior = v1_prior_pmf(year, history)
    if prior is not None:
        print(_fmt_row("PRIOR (V1)", pmf_to_survival(prior)))
    print("  " + "-" * 64)
    for (m, d) in CHECKPOINTS:
        st = _state_on(daily, year, m, d)
        if st is None:
            continue
        doy, level, rate = st
        res = compute_posterior_for_state(
            year, doy, level, rate, history, daily, analogs, calibrators, post_2017_weight)
        if res is None:
            continue
        print(_fmt_row(f"{m:02d}-{d:02d} L{level:.2f}", res["posterior_survival"]))
    if actual is not None:
        crossed = {t: ("cross" if actual >= t else "") for t in TVALS}
        cells = " ".join(f"{crossed[t]:>6}" for t in TVALS)
        print("  " + "-" * 64)
        print(f"  {'ACTUAL':<12} {cells}")


def retrospective(daily, history, analogs, calibrators, post_2017_weight):
    """Leave-one-out: at a mid-freshet checkpoint each year, is the V3 posterior
    better calibrated / sharper than the V1 prior alone? Brier on season-peak
    outcomes at three thresholds."""
    print("=" * 70)
    print("V3 RETROSPECTIVE — posterior vs prior at Apr 15 (leave-one-out)")
    print("=" * 70)
    cal_t = [107.50, 108.00, 108.50]
    agg = {t: {"prior": 0.0, "post": 0.0, "n": 0} for t in cal_t}
    for year in sorted(daily):
        st = _state_on(daily, year, 4, 15)
        if st is None:
            continue
        res = compute_posterior_for_state(
            year, *st, history, daily, analogs, calibrators, post_2017_weight)
        if res is None:
            continue
        peak = season_peak(daily[year])
        for t in cal_t:
            o = 1 if peak >= t else 0
            agg[t]["prior"] += (res["prior_survival"][t] - o) ** 2
            agg[t]["post"] += (res["posterior_survival"][t] - o) ** 2
            agg[t]["n"] += 1
    print(f"  {'threshold':>22} {'n':>4} {'Brier prior':>12} {'Brier post':>12} {'':>8}")
    print("  " + "-" * 60)
    for t in cal_t:
        n = agg[t]["n"] or 1
        bp = agg[t]["prior"] / n
        bo = agg[t]["post"] / n
        verdict = "sharper" if bo < bp else "worse"
        print(f"  {f'{t:.2f} {LABELS[t]}':>22} {agg[t]['n']:>4} "
              f"{bp:>12.4f} {bo:>12.4f} {verdict:>8}")


def latest_dated_day() -> str:
    """The newest calendar date with an observed level in the daily CSV — lets a
    routine regenerate the dashboard forecast with `--asof latest`."""
    last = None
    with DAILY_CSV.open() as f:
        for r in csv.DictReader(f):
            if r.get("level_m"):
                last = r["date"]
    return last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", help="As-of date YYYY-MM-DD, or 'latest' for the newest day on record (prior from that year, likelihood from that day)")
    ap.add_argument("--year", type=int, help="Print the posterior trajectory across one season")
    ap.add_argument("--post-2017-weight", type=float, default=DEFAULT_POST_2017_WEIGHT)
    ap.add_argument("--retrospective", action="store_true", help="LOO: posterior vs prior Brier at Apr 15")
    ap.add_argument("--json", action="store_true", help="JSON only (dashboard)")
    args = ap.parse_args()

    if not args.json:
        print("Loading V1 history + V2 daily record…")
    history = build_history()
    daily = load_daily()
    analogs = build_analogs(daily)
    calibrators = fit_calibrators(analogs, args.post_2017_weight)

    if args.retrospective:
        retrospective(daily, history, analogs, calibrators, args.post_2017_weight)
        return

    if args.year is not None:
        print_trajectory(args.year, daily, history, analogs, calibrators, args.post_2017_weight)
        return

    if not args.asof:
        print("ERROR: provide --asof, --year, or --retrospective")
        return

    asof = latest_dated_day() if args.asof == "latest" else args.asof
    y, m, d = (int(x) for x in asof.split("-"))
    st = _state_on(daily, y, m, d)
    if st is None:
        print(f"ERROR: no usable state for {asof} (missing level or rate)")
        return
    doy, level, rate = st
    res = compute_posterior_for_state(
        y, doy, level, rate, history, daily, analogs, calibrators, args.post_2017_weight)
    if res is None:
        print(f"ERROR: no V1 climate inputs for {y}")
        return

    if args.json:
        # The season is "resolved" once we're past the freshet window — the
        # posterior has collapsed onto the (now-known) actual peak.
        actual = round(season_peak(daily[y]), 2) if y in daily else None
        out = {
            "asof": asof,
            "season_resolved": doy >= FRESHET_DOY_END,
            "actual_peak_m": actual,
            "state": {"doy": doy, "level_m": round(level, 2), "rate_cm_d": round(rate, 1)},
            "thresholds": [
                {
                    "threshold_m": t,
                    "label": LABELS[t],
                    "prior": round(res["prior_survival"][t], 3),
                    "likelihood": round(res["likelihood_survival"][t], 3),
                    "posterior": round(res["posterior_survival"][t], 3),
                }
                for t in TVALS
            ],
        }
        print(json.dumps(out, indent=2))
        return

    print(f"\nV3 Bayesian posterior — as of {asof}")
    print(f"State: doy {doy} | level {level:.2f} m | rate {rate:+.1f} cm/day")
    print(f"\n  {'Threshold':<26} {'prior':>7} {'likelihood':>11} {'posterior':>10}")
    print("  " + "-" * 58)
    for t in TVALS:
        print(f"  {f'{t:.2f} {LABELS[t]}':<26} "
              f"{res['prior_survival'][t]:>7.0%} "
              f"{res['likelihood_survival'][t]:>11.0%} "
              f"{res['posterior_survival'][t]:>10.0%}")
    if y in daily:
        peak = season_peak(daily[y])
        print(f"\n  Actual {y} season peak: {peak:.2f} m")


if __name__ == "__main__":
    main()
