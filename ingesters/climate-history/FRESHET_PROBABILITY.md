# Freshet probability model — Lac Coulonge

Three layered models answer "what's the chance the lake crosses each flood
threshold this freshet?" at increasing levels of information, culminating in a
single Bayesian posterior that tightens through the season. All three are
stdlib-only, reproducible, and share one threshold ladder and era-weighting
convention.

| Layer | Script | Answers | Inputs | Horizon |
|---|---|---|---|---|
| **V1** | `freshet_probability.py` | *Going into the season,* chance of crossing each threshold | basin snowpack + cold-season precip | seasonal prior (run in March) |
| **V2** | `freshet_conditional.py` | *Given the lake's state today,* chance of crossing within 7/14/30 d **and** by season's end | daily level + 7-day rate + day-of-year | during-freshet, daily |
| **V3** | `freshet_posterior.py` | *One posterior* that starts at V1 and tightens as V2 evidence arrives | V1 prior × V2 likelihood | continuous, whole season |

## Shared conventions

- **Thresholds** (`THRESHOLDS` in `freshet_probability.py`) — the property /
  vigilance ladder for Lac Coulonge station 1195, 107.50 m (minor flood) up to
  109.17 m (the 2019 record). V2 and V3 import this list; it is the single
  source of truth.
- **Era weight** — post-2017 years count ×3 (`DEFAULT_POST_2017_WEIGHT`). The
  case file documents a 2017 step-change in Bryson operating practice;
  independently, all four super-flood years on the daily record (2017, 2019,
  2023, 2026) are post-2017, so the up-weight is empirically supported.
- **Calibration** — every layer self-checks with leave-one-out:
  `--retrospective` on each script. Reliability is reported as observed
  crossing frequency per predicted-probability bin (and Brier scores for V2/V3).

## V1 — pre-freshet seasonal prior

Gaussian-kernel analog matching. For the current `(snowpack, cold-precip)`
state, weight every historical year (1972–2026) by similarity, and the
probability of crossing threshold T is the weighted fraction of analog years
that crossed it. Honest about ±10pt tail noise from a 54-year record.

```
python3 freshet_probability.py --year 2026        # leave-one-out retrospective
python3 freshet_probability.py --retrospective    # full calibration table
```

## V2 — during-freshet conditional likelihood

Analog matching on **daily freshet trajectories** (daily Lac Coulonge record
1990–2026, built by `../lac-coulonge-daily/scrape.py`). State vector
`(day-of-year, level, 7-day rate)`, Gaussian kernel over all three dims + era
weight. Outputs per-horizon crossing probabilities and a season-end survival
curve. The season-end output is **isotonic-recalibrated** (Pool-Adjacent-
Violators) against leave-one-out outcomes, which improves Brier on all three
calibration thresholds and removes the raw model's tail overconfidence.

Day-of-year is normalized to a non-leap reference so the freshet window and DOY
kernel align across leap/non-leap years.

```
python3 freshet_conditional.py --asof 2019-04-20  # conditional forecast for a day
python3 freshet_conditional.py --retrospective    # raw vs calibrated reliability + Brier
```

Honest limits: daily record starts ~1990 (the super-flood tail rests on 4
events); this first iteration of V2 conditions on the level trajectory only —
snowpack-remaining and parameterized rain-forecast inputs are future
enhancements.

## V3 — Bayesian hybrid (continuously-updating posterior)

Combines V1 and V2 over peak-value bins (the gaps in the threshold ladder):

```
posterior_t(b)  ∝  P_1(b) · [ P_2(b | state_t) / P_2(b) ]
```

**Why a likelihood ratio, not a naive product.** V2 already estimates
`P(peak | state)`, so it carries its own implicit prior — the analog base rate
`P_2(peak)`. Dividing by that marginal swaps V2's implicit prior for V1's richer
54-year prior without double-counting, and multiplying V2 in *every* day would
massively over-tighten because consecutive days are highly autocorrelated. So
V3 evaluates one fresh posterior from each day's state; the "continuous update"
is that the state evolves daily, not a recursive filter.

**Behavior.** Uninformative early-season state → ratio ≈ 1 → posterior ≈ V1
prior (wide, honest). As the level climbs, the conditional sharpens, the ratio
moves the posterior up and tightens it. Validated: at a mid-freshet checkpoint
the posterior beats the V1 prior on Brier across all thresholds (leave-one-out),
and the gap widens later in the season.

Two correctness guards worth knowing about:
- **Empty-marginal regularization** — a leave-one-out-empty bin (e.g. the 109.17
  record) would blow up the ratio; the conditional and marginal are smoothed
  identically toward uniform and the per-bin ratio is capped, so empty bins
  contribute no information rather than exploding.
- **Season-max-to-date floor** — the peak is always ≥ the highest level seen so
  far this season, so peak bins below the running max are zeroed as impossible.
  This enforces "already crossed → 100%" exactly and keeps the posterior correct
  on the receding limb.

```
python3 freshet_posterior.py --asof 2026-04-25    # prior / likelihood / posterior
python3 freshet_posterior.py --year 2019          # tightening trajectory across a season
python3 freshet_posterior.py --retrospective      # posterior vs prior Brier (leave-one-out)
python3 freshet_posterior.py --asof 2026-04-25 --json   # dashboard output
```

### Dashboard fit

V3's single survival curve — "today's chance of crossing each threshold by
season's end," with a band that visibly tightens through the freshet — is the
intended replacement for the static threshold bar. `--json` emits the
prior/likelihood/posterior triple per threshold for direct consumption.
