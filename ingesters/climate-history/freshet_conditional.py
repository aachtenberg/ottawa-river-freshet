#!/usr/bin/env python3
"""
V2 — Real-time during-freshet conditional forecast for Lac Coulonge.

Where V1 (freshet_probability.py) is the PRE-freshet seasonal prior — "going
into the season, given snowpack and winter precip, what's the chance we hit
each threshold?" — V2 is the DURING-freshet conditional: "the lake is at level
X today, day-of-year D, rising/falling at R cm/day; what's the chance it
crosses each threshold (a) within the next 7/14/30 days, and (b) by season's
end?"

The season-end output is the one V3 (Bayesian hybrid, see GitHub issue) consumes
as the likelihood term: V1 sets the seasonal prior, V2 supplies the daily
conditional likelihood, and Bayes ties them into a posterior that tightens as
the freshet unfolds.

Method — analog matching on daily freshet trajectories:
    1. From the daily Lac Coulonge record (data/lac-coulonge-daily-1990-2026.csv,
       built by ingesters/lac-coulonge-daily/scrape.py), assemble for every
       historical year a daily level series over the freshet window (Mar 1 –
       Jun 30) plus a trailing 7-day rate of change.
    2. For the current state (day-of-year, level, rate), compute Gaussian-kernel
       similarity to every historical (year, day) point in the freshet window,
       normalized per variable. Day-of-year is a kernel dimension (bandwidth
       ~12 d), so an early-April state matches other early-Aprils most strongly
       but still borrows from late-March / mid-April across all years.
    3. Apply the same post-2017 era multiplier as V1 (current operating regime).
    4. For each threshold T and horizon N, P(cross within N days) = weighted
       fraction of analogs whose level exceeded T during their next N days.
       P(season peak >= T) = weighted fraction of analogs whose year's freshet
       peak met T. Both are hard-floored to 1.0 when the current level already
       meets T (you can't un-cross a level you're already at).

Honest limits:
    - Daily record starts ~1990 → 36 freshet seasons of trajectories (vs V1's
      54 years of annual peaks). Tail probabilities carry wide error bars.
    - v1 of V2 conditions ONLY on the level trajectory. Snowpack-remaining and
      parameterized rain-forecast inputs (which the issue lists) are deliberate
      future enhancements: they need the forecast schema parameterized first,
      and gating V2 on them would block the calibration that V3 depends on.
    - Operations introduce variance not in the level/rate state alone.

Usage:
    # Conditional forecast as of a date (leave-one-out on that year):
    python3 freshet_conditional.py --asof 2019-04-20

    # Manual state:
    python3 freshet_conditional.py --doy 110 --level 108.1 --rate 4.5

    # Leave-one-out reliability check across all years/days:
    python3 freshet_conditional.py --retrospective

    # Dashboard JSON:
    python3 freshet_conditional.py --asof 2026-04-20 --json

Stdlib only.
"""

from __future__ import annotations

import argparse
import bisect
import calendar
import csv
import json
import math
from datetime import date
from pathlib import Path
from statistics import stdev

# Reuse V1's threshold ladder and era-weight convention — single source of truth.
from freshet_probability import THRESHOLDS, DEFAULT_POST_2017_WEIGHT

ROOT = Path(__file__).resolve().parents[2]
DAILY_CSV = ROOT / "data" / "lac-coulonge-daily-1990-2026.csv"

# Freshet window as day-of-year bounds (Mar 1 – Jun 30, non-leap reference).
# Predictions and analogs are confined to this window; the annual peak lives
# inside it for every year in the record.
FRESHET_DOY_START = 60   # ~Mar 1
FRESHET_DOY_END = 181    # ~Jun 30

RATE_WINDOW_DAYS = 7     # trailing window for rate-of-change (cm/day)
DOY_BANDWIDTH = 12.0     # Gaussian bandwidth on day-of-year, in days
HORIZONS = (7, 14, 30)


def norm_doy(y: int, m: int, d: int) -> int:
    """Day-of-year normalized to a non-leap reference so the freshet window and
    DOY kernel align across years. In leap years, days after February are +1 on
    the real calendar; subtract it so Mar 1 == 60 every year. Feb 29 collapses
    onto Mar 1's slot (day 60, the window's first day) — harmless, since the
    annual peak is weeks later and a single boundary day carries no weight."""
    doy = date(y, m, d).timetuple().tm_yday
    if m > 2 and calendar.isleap(y):
        doy -= 1
    return doy


# ---------------------------------------------------------------------------
# Isotonic recalibration (Pool-Adjacent-Violators).
#
# The raw weighted-analog probabilities are monotonic in the underlying state
# but miscalibrated in level — leave-one-out shows e.g. the super-flood 20-40%
# band only crossing ~3% of the time. Isotonic regression fits a non-decreasing
# map from raw prob -> observed frequency, the standard low-capacity post-hoc
# calibrator. One map per threshold, fit on the LOO (raw_prob, outcome) pairs.
# ---------------------------------------------------------------------------

def _pava(values: list[float]) -> list[float]:
    """Pool-Adjacent-Violators: fit non-decreasing values to `values`
    (already ordered by the predictor). Unit weights."""
    blocks: list[list[float]] = []  # each [sum, count]
    for v in values:
        blocks.append([v, 1.0])
        while len(blocks) >= 2 and blocks[-2][0] / blocks[-2][1] > blocks[-1][0] / blocks[-1][1]:
            s2, c2 = blocks.pop()
            s1, c1 = blocks.pop()
            blocks.append([s1 + s2, c1 + c2])
    out: list[float] = []
    for s, c in blocks:
        out.extend([s / c] * int(c))
    return out


def _build_calibrator(pairs: list[tuple[float, int]]) -> tuple[list[float], list[float]]:
    """From (raw_prob, outcome 0/1) pairs, return (xs, fitted) — a monotonic
    step function usable by `_apply_cal`."""
    pairs = sorted(pairs, key=lambda p: p[0])
    xs = [p[0] for p in pairs]
    fitted = _pava([float(p[1]) for p in pairs])
    return xs, fitted


def _apply_cal(cal: tuple[list[float], list[float]], p: float) -> float:
    """Map a raw probability through the isotonic calibrator (linear interp)."""
    xs, fitted = cal
    if not xs:
        return p
    if p <= xs[0]:
        return fitted[0]
    if p >= xs[-1]:
        return fitted[-1]
    i = bisect.bisect_left(xs, p)
    x0, x1 = xs[i - 1], xs[i]
    y0, y1 = fitted[i - 1], fitted[i]
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * (p - x0) / (x1 - x0)


def fit_calibrators(
    analogs: list[dict], post_2017_weight: float = DEFAULT_POST_2017_WEIGHT
) -> dict[float, tuple[list[float], list[float]]]:
    """Fit one isotonic season-end calibrator per threshold from the full
    leave-one-out pass. Floored points (current level already >= threshold) are
    excluded — they are certainties, not predictions to recalibrate."""
    pairs: dict[float, list[tuple[float, int]]] = {t: [] for t, _ in THRESHOLDS}
    for a in analogs:
        res = compute_conditional(
            a["doy"], a["level"], a["rate"], analogs,
            exclude_year=a["year"], post_2017_weight=post_2017_weight,
        )
        if "error" in res:
            continue
        for t, _ in THRESHOLDS:
            if a["level"] >= t:
                continue
            raw = res["season_end"][f"{t:.2f}"]["prob"]
            pairs[t].append((raw, 1 if a["season_peak"] >= t else 0))
    return {t: _build_calibrator(pairs[t]) for t in pairs if pairs[t]}


def load_daily() -> dict[int, dict[int, float]]:
    """Return {year: {day_of_year: level_m}} from the daily CSV (observed only)."""
    out: dict[int, dict[int, float]] = {}
    with DAILY_CSV.open() as f:
        for r in csv.DictReader(f):
            v = r.get("level_m")
            if not v:
                continue
            try:
                y, m, d = (int(x) for x in r["date"].split("-"))
                level = float(v)
            except (ValueError, KeyError):
                continue
            doy = norm_doy(y, m, d)
            out.setdefault(y, {})[doy] = level
    return out


def season_peak(series: dict[int, float]) -> float:
    """Max observed level inside the freshet window for one year."""
    vals = [lv for doy, lv in series.items()
            if FRESHET_DOY_START <= doy <= FRESHET_DOY_END]
    return max(vals) if vals else max(series.values())


def rate_at(series: dict[int, float], doy: int) -> float | None:
    """Trailing RATE_WINDOW_DAYS rate of change in cm/day at day-of-year `doy`.

    Returns None if the prior reference day is missing.
    """
    cur = series.get(doy)
    prev = series.get(doy - RATE_WINDOW_DAYS)
    if cur is None or prev is None:
        return None
    return (cur - prev) * 100.0 / RATE_WINDOW_DAYS  # m -> cm, per day


def future_max(series: dict[int, float], doy: int, n: int) -> float | None:
    """Max level over (doy, doy + n] for one year, or None if no future days."""
    vals = [series[d] for d in range(doy + 1, doy + n + 1) if d in series]
    return max(vals) if vals else None


def build_analogs(daily: dict[int, dict[int, float]]) -> list[dict]:
    """Flatten the record into one analog point per (year, day-in-window) that
    has a defined level, rate, and season peak."""
    analogs: list[dict] = []
    for year, series in daily.items():
        peak = season_peak(series)
        for doy in range(FRESHET_DOY_START, FRESHET_DOY_END + 1):
            level = series.get(doy)
            if level is None:
                continue
            rate = rate_at(series, doy)
            if rate is None:
                continue
            analogs.append({
                "year": year,
                "doy": doy,
                "level": level,
                "rate": rate,
                "season_peak": peak,
                "future_max": {n: future_max(series, doy, n) for n in HORIZONS},
            })
    return analogs


def _season_entry(thresh, label, raw_prob, level, calibrators):
    """Build one season_end entry, applying isotonic calibration when available
    and not floored (a level already >= threshold is a certainty, not a
    prediction to recalibrate)."""
    entry = {"prob": round(raw_prob, 3), "label": label}
    if calibrators and level < thresh and thresh in calibrators:
        cal = round(_apply_cal(calibrators[thresh], raw_prob), 3)
        entry["prob_raw"] = entry["prob"]
        entry["prob"] = cal
    return entry


def compute_conditional(
    doy: int,
    level: float,
    rate: float,
    analogs: list[dict],
    exclude_year: int | None = None,
    post_2017_weight: float = DEFAULT_POST_2017_WEIGHT,
    calibrators: dict[float, tuple[list[float], list[float]]] | None = None,
) -> dict:
    """Weighted-analog conditional forecast for the given state.

    Returns per-threshold P(season peak >= T) and P(cross within N days) for
    each horizon N, plus the top analogs for inspection. When `calibrators` is
    supplied, the season-end "prob" is isotonic-recalibrated and the raw value
    is kept as "prob_raw".
    """
    pool = [a for a in analogs if a["year"] != exclude_year]
    if len(pool) < 2:
        return {"error": "insufficient analog data"}

    level_sd = stdev([a["level"] for a in pool])
    rate_sd = stdev([a["rate"] for a in pool])
    # Guard against degenerate spread.
    level_sd = level_sd or 1.0
    rate_sd = rate_sd or 1.0

    weights = []
    for a in pool:
        d_doy = (a["doy"] - doy) / DOY_BANDWIDTH
        d_lvl = (a["level"] - level) / level_sd
        d_rate = (a["rate"] - rate) / rate_sd
        d2 = d_doy * d_doy + d_lvl * d_lvl + d_rate * d_rate
        w = math.exp(-d2 / 2)
        if a["year"] >= 2017:
            w *= post_2017_weight
        weights.append(w)

    total = sum(weights)
    if total == 0:
        return {"error": "zero total weight"}

    season_probs = {}
    horizon_probs = {n: {} for n in HORIZONS}
    for thresh, _label in THRESHOLDS:
        if level >= thresh:
            # Already at/above this level — season peak trivially crosses it,
            # and it is "crossed within" any horizon.
            season_probs[thresh] = 1.0
            for n in HORIZONS:
                horizon_probs[n][thresh] = 1.0
            continue
        season_probs[thresh] = sum(
            w for a, w in zip(pool, weights) if a["season_peak"] >= thresh
        ) / total
        for n in HORIZONS:
            num = sum(
                w for a, w in zip(pool, weights)
                if a["future_max"][n] is not None and a["future_max"][n] >= thresh
            )
            den = sum(
                w for a, w in zip(pool, weights) if a["future_max"][n] is not None
            )
            horizon_probs[n][thresh] = (num / den) if den else None

    top = sorted(zip(pool, weights), key=lambda p: -p[1])[:8]
    top_analogs = [
        {
            "year": a["year"],
            "doy": a["doy"],
            "weight": round(w, 3),
            "level": round(a["level"], 2),
            "rate_cm_d": round(a["rate"], 1),
            "season_peak": round(a["season_peak"], 2),
        }
        for a, w in top
    ]

    return {
        "input": {"doy": doy, "level_m": round(level, 2), "rate_cm_d": round(rate, 1)},
        "n_analogs": len(pool),
        "post_2017_weight": post_2017_weight,
        "season_end": {
            f"{t:.2f}": _season_entry(t, lbl, season_probs[t], level, calibrators)
            for t, lbl in THRESHOLDS
        },
        "horizons": {
            f"{n}d": {
                f"{t:.2f}": {
                    "prob": None if horizon_probs[n][t] is None else round(horizon_probs[n][t], 3),
                    "label": lbl,
                }
                for t, lbl in THRESHOLDS
            }
            for n in HORIZONS
        },
        "top_analogs": top_analogs,
    }


def retrospective_calibration(
    daily: dict[int, dict[int, float]], analogs: list[dict]
) -> None:
    """Leave-one-out reliability check on the SEASON-END forecast.

    For each historical (year, day) state, predict P(season peak >= T) using the
    OTHER years, then bin predictions and report observed crossing frequency per
    bin. A well-calibrated model has observed frequency ~ bin midpoint.
    """
    print("=" * 78)
    print("RETROSPECTIVE CALIBRATION — leave-one-out, season-end peak")
    print("=" * 78)

    calibrators = fit_calibrators(analogs)

    # Three representative thresholds across the ladder.
    cal_thresholds = [107.50, 108.00, 108.50]
    bins = [(0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0001)]
    # tally[thresh]["raw"|"cal"][bin] = [n_crossed, n_total]
    tally = {t: {"raw": [[0, 0] for _ in bins], "cal": [[0, 0] for _ in bins]}
             for t in cal_thresholds}
    # Brier score per threshold, raw vs calibrated.
    brier = {t: {"raw": 0.0, "cal": 0.0, "n": 0} for t in cal_thresholds}

    def binof(p):
        for bi, (lo, hi) in enumerate(bins):
            if lo <= p < hi:
                return bi
        return len(bins) - 1

    for a in analogs:
        res = compute_conditional(
            a["doy"], a["level"], a["rate"], analogs,
            exclude_year=a["year"], calibrators=calibrators,
        )
        if "error" in res:
            continue
        for t in cal_thresholds:
            if a["level"] >= t:
                continue  # floored certainty — exclude from reliability
            entry = res["season_end"][f"{t:.2f}"]
            p_cal = entry["prob"]
            p_raw = entry.get("prob_raw", p_cal)
            o = 1 if a["season_peak"] >= t else 0
            for kind, p in (("raw", p_raw), ("cal", p_cal)):
                bi = binof(p)
                tally[t][kind][bi][1] += 1
                if o:
                    tally[t][kind][bi][0] += 1
            brier[t]["raw"] += (p_raw - o) ** 2
            brier[t]["cal"] += (p_cal - o) ** 2
            brier[t]["n"] += 1

    for t in cal_thresholds:
        label = next(l for th, l in THRESHOLDS if th == t)
        n = brier[t]["n"]
        br_raw = brier[t]["raw"] / n if n else float("nan")
        br_cal = brier[t]["cal"] / n if n else float("nan")
        print(f"\nThreshold {t:.2f} m — {label}")
        print(f"  Brier: raw {br_raw:.4f} → calibrated {br_cal:.4f} "
              f"({'better' if br_cal < br_raw else 'worse'})  [n={n}, floored excluded]")
        print(f"  {'predicted bin':>14} {'n(raw)':>7} {'obs(raw)':>9} "
              f"{'n(cal)':>7} {'obs(cal)':>9}")
        print("  " + "-" * 50)
        for bi, (lo, hi) in enumerate(bins):
            cr, nr = tally[t]["raw"][bi]
            cc, nc = tally[t]["cal"][bi]
            fr = f"{cr / nr:.0%}" if nr else "—"
            fc = f"{cc / nc:.0%}" if nc else "—"
            print(f"  {f'{lo:.0%}-{hi:.0%}':>14} {nr:>7} {fr:>9} {nc:>7} {fc:>9}")


def _state_for_date(daily: dict[int, dict[int, float]], iso: str):
    """Return (doy, level, rate, year) for an as-of date, or None if unavailable."""
    y, m, d = (int(x) for x in iso.split("-"))
    doy = norm_doy(y, m, d)
    series = daily.get(y)
    if not series or doy not in series:
        return None
    rate = rate_at(series, doy)
    if rate is None:
        return None
    return doy, series[doy], rate, y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--asof", help="As-of date YYYY-MM-DD; uses that day's state (leave-one-out)")
    ap.add_argument("--doy", type=int, help="Day-of-year override")
    ap.add_argument("--level", type=float, help="Current level (m) override")
    ap.add_argument("--rate", type=float, help="Trailing rate (cm/day) override")
    ap.add_argument("--post-2017-weight", type=float, default=DEFAULT_POST_2017_WEIGHT)
    ap.add_argument("--retrospective", action="store_true", help="LOO calibration across all years/days")
    ap.add_argument("--raw", action="store_true", help="Skip isotonic recalibration (show raw analog probs)")
    ap.add_argument("--json", action="store_true", help="JSON only (dashboard)")
    args = ap.parse_args()

    print("Loading daily Lac Coulonge record…") if not args.json else None
    daily = load_daily()
    analogs = build_analogs(daily)
    if not args.json:
        yrs = sorted(daily)
        print(f"  {len(analogs)} analog day-points across {len(yrs)} years "
              f"({yrs[0]}–{yrs[-1]})")

    if args.retrospective:
        retrospective_calibration(daily, analogs)
        return

    excl = None
    if args.doy is not None and args.level is not None and args.rate is not None:
        doy, level, rate = args.doy, args.level, args.rate
        label = "custom state"
    elif args.asof:
        st = _state_for_date(daily, args.asof)
        if st is None:
            print(f"ERROR: no usable state for {args.asof} (missing level or rate)")
            return
        doy, level, rate, excl = st
        label = f"as of {args.asof}"
    else:
        print("ERROR: provide --asof, or --doy/--level/--rate, or --retrospective")
        return

    calibrators = None if args.raw else fit_calibrators(analogs, args.post_2017_weight)
    res = compute_conditional(doy, level, rate, analogs,
                              exclude_year=excl, post_2017_weight=args.post_2017_weight,
                              calibrators=calibrators)

    if args.json:
        print(json.dumps(res, indent=2))
        return

    print(f"\nDuring-freshet conditional forecast — {label}")
    print(f"State: doy {doy} | level {level:.2f} m | rate {rate:+.1f} cm/day")
    cal_note = "raw analog" if args.raw else "isotonic-calibrated"
    print(f"Era weight: post-2017 × {args.post_2017_weight} | analogs: {res['n_analogs']} "
          f"| season-end: {cal_note}")

    print(f"\n{'Threshold (m)':<14} {'season-end':>11} "
          + " ".join(f'{str(n)+"d":>7}' for n in HORIZONS) + "  Label")
    print("-" * 78)
    for t, lbl in THRESHOLDS:
        se = res["season_end"][f"{t:.2f}"]["prob"]
        hz = []
        for n in HORIZONS:
            p = res["horizons"][f"{n}d"][f"{t:.2f}"]["prob"]
            hz.append("   —  " if p is None else f"{p:>6.0%} ")
        print(f"  {t:<11.2f} {se:>10.0%} " + " ".join(hz) + f"  {lbl}")

    print(f"\nTop analogs:")
    print(f"  {'year':>6} {'doy':>4} {'wt':>6} {'level':>7} {'rate':>6} {'peak':>7}")
    for a in res["top_analogs"]:
        era = "post-2017" if a["year"] >= 2017 else "pre-2017"
        print(f"  {a['year']:>6} {a['doy']:>4} {a['weight']:>6.3f} "
              f"{a['level']:>7.2f} {a['rate_cm_d']:>6.1f} {a['season_peak']:>7.2f}  ({era})")

    if excl is not None:
        peak = season_peak(daily[excl])
        print(f"\nActual {excl} season peak: {peak:.2f} m")
        for t, lbl in THRESHOLDS:
            crossed = "✓" if peak >= t else "✗"
            print(f"  {t:<11.2f} {crossed}  ({res['season_end'][f'{t:.2f}']['prob']:.0%} predicted season-end)")


if __name__ == "__main__":
    main()
