# Pre-freshet reservoir state vs subsequent peak — 36-year test

**Companion to *Volume vs Peak Flow at Pembroke* — case-file note**
**Compiled: May 23, 2026**

> **Attribution note.** This note responds to the same May-2026 Facebook
> thread treated in [`Freshet_Volume_vs_Peakedness.md`](Freshet_Volume_vs_Peakedness.md).
> One participant argued that the chart-author's "Des Joachims volume →
> Pembroke peak" framing ignores a separate variable: how full the upper-
> basin reservoirs were *entering* the freshet. The same downstream peak,
> the argument goes, is a very different operating outcome depending on
> how much headroom the system carried in. Per the repo
> [attribution policy](../../CONTRIBUTORS.md), thread participants are
> referred to by role, not by name.

---

## Plain-language summary

The reservoir-state commenter argued that pre-freshet storage is a
separate variable from total volume — that the same downstream peak is
a different operating outcome depending on how much headroom the system
carried in. **The variable is operationally well-defined and now
testable on 30 years of public data. Across that record, April-1
storage state does not predict the Britannia spring peak.**

- **Basin-wide** (13 ORRPB reservoirs, capacity-weighted % of operating
  band): **r = −0.12, p = 0.53, n = 30** (1990–2024). Slope ≈ −0.005 m
  per percentage point — a +10 pp shift in pre-freshet storage state
  associates with −0.05 m on the Britannia peak. Statistically zero.
- **Upper-river only** (Timiskaming, Kipawa, Quinze, Rapide-7, Dozois,
  Lady Evelyn — the six reservoirs whose outflow reaches Pembroke):
  **r = −0.01, p = 0.96, n = 30.** Slope effectively zero. The peaks
  the commenter pointed to (2019, 2017, 2023) all entered the freshet
  with upper-river reservoirs **drawn down hard** (18–24 % of band) —
  the operating outcome the commenter said *should* have produced a
  lower peak.
- **2012 sanity check.** The single year with abnormally high
  pre-freshet storage (74 % upper-river / 70 % basin-wide) produced a
  *low* peak (59.51 m). High storage and high peak are decoupled in
  both directions.

**Reading.** The peak years are wet, not full-reservoir years. The
operators were drawn down on Apr 1 of every top-3 peak in the record.
This is consistent with the companion note's finding that **peak flow
itself** (not pre-freshet storage, not total volume) is what drives
peak level. If there is an operator-discretion lever, it acts at peak
time — opening/closing gates during the event — not at Apr-1 storage
position.

The methodology, datasets, and figures are below; the unlock that made
this possible (ORRPB per-location historical archive) is documented in
[`ingesters/orrpb-location-history/scrape.py`](../../ingesters/orrpb-location-history/scrape.py).

---

## What changed since the May-23 feasibility scout

This note was originally drafted as a feasibility scout with n = 3
(Wayback-mined 2020/2023/2024). Between draft and publication an
unlock landed: each ORRPB per-location page (e.g.
[ottawariver.ca/location/timiskaming/](https://www.ottawariver.ca/location/timiskaming/))
exposes a POST form that returns daily observed levels for the full
1990–2025 record. Scraping that across all 13 principal reservoirs
yielded **170,651 daily observations** — and with it, 30 paired
(pre-freshet state, spring peak) observations, the statistical meat
the feasibility note lacked.

The doc you are reading is the finding doc that replaces the n = 3
draft. The Wayback miner is retained for completeness but no longer
the primary source for this question.

---

## Three thread arguments, three readings

The same three pushbacks tabulated in
[`Freshet_Volume_vs_Peakedness.md`](Freshet_Volume_vs_Peakedness.md),
re-read with the 30-year test in hand:

| Pushback | Author's role | Reading after this note |
|---|---|---|
| "Total cumulative flow is irrelevant to water height — that is caused by instantaneous flow." | timing-pushback commenter | Addressed in the companion note: V's marginal contribution beyond Q_pk is +0.01 pp. **Unchanged here.** |
| "Pre-freshet reservoir levels should be normalised for." | reservoir-state commenter | **The variable is well-defined and tested.** r ≈ 0, p ≈ 1 on n = 30 — pre-freshet storage state does **not** predict Britannia spring peak across 1990–2024. The three top peaks in the record (2019/2017/2023) all entered the freshet with upper-river reservoirs drawn down hard, opposite to the hypothesis. |
| "Total volume captures most of it (R² = 0.72), so it is statistically very relevant." | chart's author | Addressed in the companion note: R² = 0.72 is a 0.892² correlation, not evidence that V causes the peak. **Unchanged here.** |

---

## What was tested

For each year 1990–2025:

| | |
|---|---|
| **pct_of_band**  | (level − low_limit) / (high_limit − low_limit), per reservoir, on April 1 |
| **used_mcm**     | Linear stage-storage approximation: pct_of_band × capacity_mcm (ICOLD 2020) |
| **basin-wide aggregate %**  | Σ used_mcm / Σ capacity_mcm across 13 principal reservoirs (capacity-weighted) |
| **upper-river aggregate %** | Equal-weight mean of % of band across the 6 upper-river reservoirs (used because Rapide-7 has no separate capacity figure in ICOLD — its storage is the upstream Decelles) |
| **peak**         | Britannia spring (Mar–Jun) maximum gauge level (m), same year |

Regression: OLS y = β·x + α, Pearson r, two-tailed t-test on r with
normal approximation (n ≥ 30 makes the normal approx fine).

**Methodology source.** Same operating-bands + ICOLD capacities as the
[reservoir-drawdown community note (2026-05-22)](../../data/community-notes/2026-05-22_reservoir_drawdown.md).
Britannia daily levels from the local WSC daily archive.

**Linear stage-storage caveat.** Converting % of band to Mm³ assumes
storage is linear in elevation between the operating limits. Aggregate
% of band is robust to this; Mm³ figures are illustrative.

**Upper-river partition.** Six reservoirs whose outflow reaches
Lac Coulonge / Pembroke: Timiskaming, Kipawa, Quinze, Rapide-7,
Dozois, Lady Evelyn. The other seven (Cabonga, Kiamika, Mitchinamecus,
Baskatong, Bark Lake, Poisson Blanc, Des Joachims) join downstream of
the upper-river communities and don't change the Pembroke peak —
matches the [May-22 community note partition](../../data/community-notes/2026-05-22_reservoir_drawdown.md).

**Script:**
[`ingesters/climate-history/pre_freshet_reservoir_scout.py`](../../ingesters/climate-history/pre_freshet_reservoir_scout.py)
**Ingester:**
[`ingesters/orrpb-location-history/scrape.py`](../../ingesters/orrpb-location-history/scrape.py)

---

## Headline regressions

### Basin-wide (13 reservoirs, capacity-weighted)

```
n = 30        (1990–2024 with Britannia peak)
r = −0.117    p = 0.534
slope = −0.0051 m per percentage point
        (+10 pp on Apr 1 → −0.05 m on peak)
```

### Upper-river only (6 reservoirs, equal-weight % of band)

```
n = 30
r = −0.009    p = 0.961
slope = −0.0003 m per percentage point
        (+10 pp on Apr 1 → −0.00 m on peak)
```

The upper-river-only version is the relevant one for the Pembroke /
Lac Coulonge reach. r ≈ 0 with p ≈ 1 is about as null as a regression
result gets at n = 30.

---

## Year-by-year — the years that motivate the question

**Top-5 peak years and their pre-freshet upper-river storage:**

| Year | Apr-1 upper-river (% of band) | Britannia spring max (m) |
|---|---|---|
| **2019** | **18 %** | **60.68** |
| **2017** | **24 %** | **60.44** |
| **2023** | **23 %** | **60.34** |
| 2002 | 24 % | 59.97 |
| 1996 | 15 % | 59.82 |

Every one of the top-5 peaks entered the freshet with upper-river
reservoirs drawn down to 15–24 % of band — i.e. the operators
discharged through winter exactly as the operating directive
requires. The argument that "more headroom would have lowered the
peak" requires more headroom than the operators in fact carried into
those Aprils, and the record does not contain a year where they
carried less.

**Most drawn-down Aprils:**

| Year | Apr-1 upper-river (% of band) | Britannia spring max (m) |
|---|---|---|
| 1994 | 10 % | 58.93 |
| 1992 | 11 % | 59.52 |
| 1993 | 14 % | 58.75 |
| 1996 | 15 % | 59.82 |
| 2018 | 17 % | 59.80 |

**Least drawn-down Aprils:**

| Year | Apr-1 upper-river (% of band) | Britannia spring max (m) |
|---|---|---|
| **2012** | **74 %** | **59.51** |
| 2024 | 48 % | 59.42 |
| 2021 | 38 % | 59.07 |
| 2016 | 34 % | 59.61 |
| 2004 | 26 % | 59.38 |

**2012 is the inverse experiment.** The single year where upper-river
storage was carried *high* (74 %, two to three times the typical 15-25 %)
the spring peak came in at 59.51 m — below the 60-year median. High
storage and high peak are decoupled in both directions of the variable.

---

## Figures (`data/community-notes/`)

- `2026-05-23_pre_freshet_storage_vs_peak.png` — basin-wide aggregate
  % of band vs Britannia spring max, n = 30
- `2026-05-23_pre_freshet_upper_river.png` — upper-river-only mean
  % of band vs Britannia spring max, n = 30
- `2026-05-23_pre_freshet_band_heatmap.png` — per-reservoir × year
  heatmap of April-1 % of band, 1990–2025 (blue = drawn down, red = high)

## Outputs

- `data/orrpb-location-history/orrpb_location_daily.csv` — the 170,651-row
  daily archive (1990–2025, 13 reservoirs)
- `data/orrpb-location-history/april1_state_by_year.csv` — 468 rows,
  per-(year, reservoir) April-1 state + paired Britannia peak
- `data/orrpb-location-history/raw/*.html` — every fetched ORRPB
  historical-table HTML, checked in so the ingester never re-fetches

---

## What this rules out, what it doesn't

**Rules out:** the strong form of the reservoir-state argument — that
the operators chose to carry too much storage into 2017/2018/2019 and
that this caused the high peaks. They did not. They drew down hard.
The peaks happened anyway. Across 30 years, pre-freshet storage state
explains zero variance in the spring peak.

**Doesn't rule out:** the operator-discretion question *at peak time* —
how gates are operated during the event itself, which is the variable
analysed in the [companion note](Freshet_Volume_vs_Peakedness.md) and
the [Carillon directive note](Carillon_Directive_Compliance.md).
"Pre-freshet state did not cause the peak" is not the same statement
as "no operator discretion exists." It just says the question lives
elsewhere — at peak time, not at Apr 1.

**Doesn't address:** the exogenous-forcing decomposition (snow water
equivalent, late-winter precipitation, April rain). Adding these as
controls is a follow-on; the bivariate null result here is already
strong enough that pre-freshet state is not a contender.

---

## Relationship to existing case-file findings

| | Test A | Britannia top-3 | Volume vs Peakedness | This note |
|---|---|---|---|---|
| Variable | Britannia **flow** | Britannia **level** | Britannia **flow → level** | Reservoir **storage** |
| Window | 1960+, Apr–Jul | full 1915–2024 | 1960+, Mar–Jun | Apr 1, 1990–2024 |
| Question | given a break, which year? | any single step / cycle? | does volume cause peak height? | does pre-freshet storage predict peak? |
| Answer | 2017 (+19.3 % median) | none unconditional; top-3 = 2019/2017/2023 | no — peak flow does; V is a proxy | **no — r ≈ 0, p ≈ 1 on n = 30** |

---

## Caveats

- **Linear stage-storage.** First-order approximation; aggregate % of
  band is robust, Mm³ figures are illustrative.
- **Britannia, not Pembroke.** Same reach choice as the companion note;
  same caveat — variable-structure findings generalise, specific
  numbers do not transfer one-to-one. The Pembroke replication is a
  pending item shared with the companion note.
- **ORRPB observed-level coverage starts 1990.** The form returns an
  operating-limits "Category" table for 1987–1989 instead of observed
  values, so the record begins at 1990. This is the same archive the
  operators publish on their website; it is the most extensive public
  record available.
- **Bryson dam / Lac Coulonge gauge** is not in the ORRPB archive — it
  is the local headpond level managed by Energy Ottawa, not ORRPB.
  The [reservoir-drawdown community note](../../data/community-notes/2026-05-22_reservoir_drawdown.md)
  treats it separately. Including or excluding it does not change the
  Apr-1 upper-river finding here.

---

## Sources

- **ORRPB per-location historical archive** — POST form on each
  `ottawariver.ca/location/<slug>/` page, returns daily observed levels
  1990–2025 (this note's primary source; see
  [`ingesters/orrpb-location-history/scrape.py`](../../ingesters/orrpb-location-history/scrape.py))
- **ORRPB System Constraints tables** — operating limits per reservoir
  (per-location pages on ottawariver.ca)
- **ICOLD-Canada (2020), Ottawa River Watershed case study**, Table 1 —
  usable storage capacities in Mm³ for the 13 principal cascade
  reservoirs.
  https://ottawariver.ca/wp-content/uploads/2020/10/ICOLD-CANADA-CASE_STUDY_OTTAWA_RIVER_WATERSHED.pdf
- **Britannia (02KF005) daily levels** — local WSC daily archive
  (`data/wsc-hydrometric/britannia-ottawa-river/daily.csv`)
- **Companion note** — *Volume vs Peak Flow at Pembroke*
  ([`Freshet_Volume_vs_Peakedness.md`](Freshet_Volume_vs_Peakedness.md))
- **Single-year 2026 audit** — *Two questions, not one* (community note,
  2026-05-22)
