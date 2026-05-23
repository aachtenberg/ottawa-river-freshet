# Pre-freshet reservoir state vs subsequent peak — feasibility scout

**Companion to *Volume vs Peak Flow at Pembroke* — case-file note**
**Compiled: May 23, 2026**

> **Attribution note.** This note responds to the same May-2026 Facebook
> thread treated in [`Freshet_Volume_vs_Peakedness.md`](Freshet_Volume_vs_Peakedness.md).
> One participant argued that the chart-author's "Des Joachims volume →
> Pembroke peak" framing ignores a separate variable: how full the upper-
> basin reservoirs were *entering* the freshet. The same downstream peak,
> the argument goes, is a very different operating outcome depending on
> how much headroom the system carried in. This note tests how much of
> that question is answerable from the *public* record, and what is
> conclusively gated behind operator-held data. Per the repo
> [attribution policy](../../CONTRIBUTORS.md), thread participants are
> referred to by role, not by name.

---

## Plain-language summary

The reservoir-state commenter is right that pre-freshet storage is a
separate variable from total volume and from hydrograph shape — and the
case-file's existing
[reservoir-drawdown community note](../../data/community-notes/2026-05-22_reservoir_drawdown.md)
already used the same "% of operating band" methodology to adjudicate
the 2026 case. Here we ask: **can we extend that test across multiple
years of pre-freshet snapshots, and link each year's pre-freshet state
to the subsequent freshet peak?**

The honest answer is **partly, and not for the years that motivate the
question**:

- **What we got.** The Internet Archive's Wayback Machine captured
  ORRPB's `conditions/?display=reservoir` page from approximately April
  2020 onward. Mining those snapshots reconstructs daily reservoir
  levels for **14 reservoirs across 2020–2025 (5,216 obs)**. From that
  we can compute the same "% of operating band" indicator the May-22
  note used, on **April 1 ± 7 days** of each year.
- **What we couldn't get.** Wayback has **no coverage of the 2017–2019
  freshets** — exactly the high-peak years the commenter pointed at.
  2021 and 2022 are in Wayback's index but have no snapshot inside the
  April-1 ± 7-day window, so they drop out too.
- **What survives.** Three paired (pre-freshet aggregate state, Britannia
  spring peak) observations — 2020, 2023, 2024. That is **enough to
  document the method on the public record and expose what the gap
  looks like; not enough to draw any conclusion about whether more
  buffer would have lowered recent peaks.**

The n = 3 result is reported below for completeness. It runs opposite
to the commenter's hypothesis (more buffer associated with *higher*
peak, r = −0.68) but is non-significant and almost certainly dominated
by 2024's wet basin + high storage co-occurrence — a forcing/storage
confound that needs the unregulated-inflow control the commenter
himself called for.

The substantive output of this note is therefore not a result but
**a list of data acquisitions that would actually move the question**,
in priority order — see the *Roadmap* section at the bottom.

---

## Three thread arguments, three readings (extended)

The same three pushbacks tabulated in
[`Freshet_Volume_vs_Peakedness.md`](Freshet_Volume_vs_Peakedness.md),
re-read with what this scout adds:

| Pushback | Author's role | Reading after this scout |
|---|---|---|
| "Total cumulative flow is irrelevant to water height — that is caused by instantaneous flow." | timing-pushback commenter | Addressed in the companion note: V's marginal contribution beyond Q_pk is +0.01 pp. **Unchanged here.** |
| "Pre-freshet reservoir levels should be normalised for." | reservoir-state commenter | **The variable is now operationalised.** Aggregate % of band across 13 principal reservoirs is the natural normalisation; we computed it for 2020/2023/2024/2025 from Wayback. **But the years that motivate the argument (2017/2018/2019) are not in the public record.** A proper test needs ORRPB historical reservoir data or an OPG-side source. |
| "Total volume captures most of it (R² = 0.72), so it is statistically very relevant." | chart's author | Addressed in the companion note: R² = 0.72 is a 0.892² correlation, not evidence that V causes the peak. **Unchanged here.** |

---

## What was tested

For each year 2020–2025:

| | |
|---|---|
| **pct_of_band**  | (level − low_limit) / (high_limit − low_limit), per reservoir, on April 1 ± 7 d |
| **used_mcm**     | Linear stage-storage approximation: pct_of_band × capacity_mcm (ICOLD 2020) |
| **aggregate %**  | Σ used_mcm / Σ capacity_mcm across the 13 principal reservoirs that have a capacity figure |
| **peak**         | Britannia spring (Mar–Jun) maximum gauge level (m), same year |

**Methodology source.** Same as the
[reservoir-drawdown community note (2026-05-22)](../../data/community-notes/2026-05-22_reservoir_drawdown.md):
operating bands from ORRPB System Constraints tables (per-location
pages); capacities from ICOLD-Canada (2020) cascade case study, Table 1
— a single authoritative source covering all 13 principal Ottawa-basin
reservoirs. Britannia daily levels from the local WSC daily archive.

**Linear stage-storage caveat.** Converting % of band to Mm³ assumes
storage is linear in elevation between the operating limits. That is a
first-order approximation; the operators hold the true stage-storage
curves. The aggregate % of band is robust to this; the Mm³ figures are
the convenient "human numbers" for sanity-checking against the operators'
own statements.

**Script:**
[`ingesters/climate-history/pre_freshet_reservoir_scout.py`](../../ingesters/climate-history/pre_freshet_reservoir_scout.py)
**Miner:**
[`ingesters/wayback-reservoir-mine/mine.py`](../../ingesters/wayback-reservoir-mine/mine.py)

---

## Data scouted

| Source | What it has | Useful here? |
|---|---|---|
| **ORRPB live conditions** (`/conditions/?display=reservoir`) | Rolling 8-day window of current reservoir levels | Only current — already ingested daily; no history |
| **ORRPB historical summaries** ([hub](https://www.ottawariver.ca/information/historical-data-summaries-water-levels-and-flows/)) | Monthly mean *river-gauge* values back to ~1950s | River gauges only — **no reservoir history published** |
| **ORRPB per-location pages** | Daily for the recent rolling window per location | Same coverage limitation as conditions page |
| **HQ open-data feeds** ([reference](../../README_HQ_OPENDATA.md)) | Daily dam releases (cms) and headpond levels for HQ-operated stations | Live + ~weeks history; **doesn't extend backwards** |
| **Internet Archive Wayback Machine** | Snapshots of `/conditions/?display=reservoir` from ~Apr 2020 | **Yes — used here.** 5,216 obs reconstructed 2020–2025 |
| **Ottawa River Regulating Secretariat** | Operational reservoir history (the authoritative archive) | **Gated.** Public-records request would be the formal route |
| **OPG / HQ / MELCC / PSPC** archives per-operator | Per-dam telemetry, each operator's own record | Mostly internal; some ATIP-able for federal operators |

---

## What the Wayback miner recovered

After mining all 200-status snapshots of the conditions page from
2018-01-01 through 2025-12-31 (Wayback returned 132 captures starting
2020-03-28), we kept all Jan–Jun snapshots plus one per month otherwise,
fetched and cached each snapshot's HTML, parsed it with the same table
extractor the live ingester uses, and de-duplicated by (reservoir_id,
date) preferring the freshest snapshot.

```
14 reservoirs, 2020-03-28 → 2025-09-30 — 5,216 daily observations
```

**April-1 ± 7-day coverage by year:**

| Year | Reservoirs hit | Note |
|---|---|---|
| 2020 | 14 of 14 | ✓ paired with peak |
| 2021 | 0 | no pre-freshet snapshot — only later-spring captures |
| 2022 | 0 | no pre-freshet snapshot |
| 2023 | 14 of 14 | ✓ paired with peak |
| 2024 | 14 of 14 | ✓ paired with peak |
| 2025 | 14 of 14 | state captured; no Britannia peak loaded yet for 2025 in local archive |

**Years entirely missing from Wayback:** 2017, 2018, 2019 — every
snapshot of the conditions page in the Archive is from April 2020 or
later.

---

## Sample analysis (n = 3) — not a result, an illustration

| Year | Apr-1 aggregate (% of band) | Used storage (Mm³) | Britannia spring max (m) |
|---|---|---|---|
| 2020 | **24.4 %** | 2,957 / 12,144 | **59.586** |
| 2023 | **23.0 %** | 2,791 / 12,144 | **60.342** |
| 2024 | **47.6 %** | 5,775 / 12,144 | **59.420** |
| 2025 | 37.6 % | 4,570 / 12,144 | (n/a) |

- **Pearson r (aggregate %, peak) = −0.676**, n = 3, **not significant**.
- **OLS slope: −0.024 m per pct** — every +10 % of band on April 1 is
  associated with −0.24 m on the Britannia spring peak.

**Reading.** The slope direction is the *opposite* of what the
reservoir-state commenter hypothesised — more pre-freshet storage,
lower peak. With three paired observations this number is essentially
noise, but the *physical reason* it might come out backwards is worth
naming: **pre-freshet storage and incoming forcing are themselves
correlated**. A wetter-than-average late winter both fills reservoirs
(operators take in inflow they can't pass without breaching the
operating floor) *and* produces a higher subsequent freshet. Without an
exogenous-forcing control (snow water equivalent + cold-season
precipitation + April rain) the bivariate scatter cannot separate
operator discretion from hydrologic forcing — the exact issue raised
in [`Freshet_Volume_vs_Peakedness.md`](Freshet_Volume_vs_Peakedness.md)
about V being on the wrong axis.

This is the structural reason the n needs to be larger and the
covariates need to be present before this regression speaks to the
operator question. The methodology runs; the data needed to *answer*
the commenter's question still needs to be acquired.

### Figures (`data/community-notes/`)

- `2026-05-23_pre_freshet_storage_vs_peak.png` — aggregate %-of-band vs
  Britannia spring max, n = 3
- `2026-05-23_pre_freshet_band_heatmap.png` — per-reservoir × year
  heatmap of April-1 ± 7d % of band (blue = drawn down, red = high)

### Outputs

- `data/wayback-orrpb-reservoirs/wayback_reservoir_levels.csv` — 5,216
  rows, the daily mined record itself
- `data/wayback-orrpb-reservoirs/april1_state_by_year.csv` — 51 rows,
  per-(year, reservoir) April-1 state + paired peak
- `data/wayback-orrpb-reservoirs/cdx_index.json` — cached Wayback CDX
  listing (re-run-free)
- `data/wayback-orrpb-reservoirs/raw/<timestamp>.html` — every fetched
  Wayback snapshot, checked in so the miner never re-fetches

---

## Roadmap — what data would actually move this question

In priority order:

1. **ORRPB / Secretariat historical reservoir record (2010 onward, all
   13 reservoirs, daily).** This is the authoritative archive the
   public record is missing. A formal records request is the route;
   the commenter's "want to see the contracts" framing converges with
   this in practical terms.
2. **Basin snow water equivalent + cold-season precipitation, 1960
   onward.** ECCC / MSC station data + reanalysis. This is the
   exogenous-forcing control without which any pre-freshet-state vs
   peak regression confounds operator discretion with hydrology.
3. **OPG operational daily flow at Pembroke or Des Joachims.** Same ask
   as the companion note; resolves the Pembroke-replication caveat.
4. **HYDAT extension for Outaouais reservoir-headpond gauges.** The
   federal HYDAT archive may carry some reservoir gauges further back
   than ORRPB's web record; worth checking station-by-station.
5. **Pre-2020 Wayback for HQ feed pages or per-location ORRPB pages.**
   Less likely to be useful (the per-location pages weren't structured
   the same way before ~2022) but a one-shot check would close the
   loop.

The May-22 community note's substantive findings on the 2026 freshet
(9 of 13 reservoirs at ≤ 33 % on April 1; the upper-river ones at the
floor; Lac Coulonge held high all winter at the Bryson dam) **do not
depend on the multi-year regression this note attempts**. They are a
single-year audit, and the operating-band methodology used there is
the same one this note extends across years. The audit is sound; the
n-of-3 regression is preparatory work pending the data above.

---

## Relationship to existing case-file findings

| | Test A | Britannia top-3 (May 17) | Volume vs Peakedness | This scout |
|---|---|---|---|---|
| Variable | Britannia **flow** | Britannia **level** | Britannia **flow → level** | Reservoir **storage** |
| Window | 1960+, Apr–Jul | full 1915–2024 | 1960+, Mar–Jun | Apr 1 ± 7d, 2020–2025 |
| Question | given a break, which year? | any single step / cycle? | does volume cause peak height? | does pre-freshet storage predict peak? |
| Answer | 2017 (+19.3 % median) | none unconditional; top-3 = 2019/2017/2023 | no — peak flow does; V is a proxy | **method works, n = 3 not enough; data acquisition needed** |

---

## Caveats

- **n = 3.** Cannot reject anything. Reported for methodology, not
  conclusion.
- **Linear stage-storage.** First-order approximation; aggregate % of
  band is robust, Mm³ figures are illustrative.
- **Britannia, not Pembroke.** Same reach choice as the companion note;
  same caveat — variable-structure findings generalise, specific
  numbers do not transfer one-to-one.
- **Aggregate vs upper-river-only.** The May-22 note distinguished
  reservoirs that feed the upper Ottawa (and reach Lac Coulonge /
  Pembroke) from the Gatineau/Lièvre/Madawaska reservoirs (which join
  downstream). This scout uses a basin-aggregate % for the regression;
  an upper-river-only version is a one-line code change once n is
  large enough to make it worth doing.
- **Wayback snapshot timing.** Each captured snapshot's 8-day window
  is *around* the snapshot date, not strictly before, so a snapshot
  from (e.g.) April 5 typically contains levels from April 1–April 8.
  We pick the observation whose own date falls within ±7 days of
  April 1.

---

## Sources

- **Wayback Machine CDX API** — snapshot index for
  `ottawariver.ca/conditions/?display=reservoir`
- **ORRPB System Constraints tables** — operating limits per reservoir
  (per-location pages on ottawariver.ca)
- **ICOLD-Canada (2020), Ottawa River Watershed case study**, Table 1 —
  usable storage capacities in Mm³ for all 13 principal cascade
  reservoirs.
  https://ottawariver.ca/wp-content/uploads/2020/10/ICOLD-CANADA-CASE_STUDY_OTTAWA_RIVER_WATERSHED.pdf
- **Britannia (02KF005) daily levels** — local WSC daily archive
  (`data/wsc-hydrometric/britannia-ottawa-river/daily.csv`)
- **Companion note** — *Volume vs Peak Flow at Pembroke*
  ([`Freshet_Volume_vs_Peakedness.md`](Freshet_Volume_vs_Peakedness.md))
- **Single-year 2026 audit** — *Two questions, not one* (community note,
  2026-05-22)
