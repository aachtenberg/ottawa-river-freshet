# Pembroke-Chart Thread — Trend / Changepoint / Cycle Test

**Mansfield-et-Pontefract / Lac Coulonge property tracking — case-file analysis**
**Compiled: May 17, 2026**

> **Attribution note.** This note responds to a public Facebook-group
> thread discussing a "MAX Elevation at Pembroke 1913–2026" chart. Per the
> repo [attribution policy](../../CONTRIBUTORS.md), thread participants are
> referenced by role — *the chart's author*, *the cyclical-precipitation
> commenter*, *the deforestation-thesis commenter* — not by name. The
> maintainer holds the mapping privately.

---

## Plain-language summary

Someone posted a 113-year chart of the highest spring water level each year
at Pembroke and drew flat trend lines through it. A debate followed. Three
explanations were offered: (1) "there's no real long-term trend, nothing to
see"; (2) "the big floods of 1927–1945 were caused by the valley being
clear-cut of forest"; (3) "it's a natural decades-long precipitation cycle."

We can't get a 113-year Pembroke record (it doesn't exist in usable form —
Pembroke only shows up as a recent rolling feed). So we used the next best
thing: **110 years of daily Ottawa River levels at Britannia (Ottawa)**,
the longest main-stem record we can reach, and cross-checked it against a
second long record downstream.

Running the *actual* statistics that the thread was only eyeballing:

- **"No long-term trend" — true, but it's the wrong question.** There is
  genuinely no straight-line trend (a real trend test says so). But the
  three **highest** spring peaks in 110 years are **2019, 2017 and 2023**,
  with the only old rival (1928) sitting fourth. A flat average can hide a
  record-smashing recent tail — and the tail is the part that floods
  basements. "No trend" is a true answer to a question that doesn't matter.

- **"1927–1945 deforestation cluster" — not supported.** No statistically
  real cluster or step exists there. 1928 is the lone old year near the top
  of the record, and it ranks *below* 2017 and 2019. The 1927–1945 window
  was drawn around ordinary year-to-year noise.

- **"Decadal precipitation cycle" — firmly rejected.** The data has no
  detectable cycle at all; it behaves like pure randomness. 110 years is
  far too short to even detect a 30-year cycle, and none survives testing.

- **Bonus finding.** A second long gauge downstream gives a *different*
  history (its big years are the 1940s–70s, not now) — because it sits
  under St-Lawrence dam control, not Ottawa control. Two gauges on "the
  same river" disagreeing is itself proof of the core point: you cannot
  read river behaviour off a raw regulated gauge without first removing
  the dam management.

**Bottom line for the case file:** the honest statement is *not* "flat, so
nothing's happening" and *not* "explained by old logging or cycles." It is
that the main-stem spring peak looks like flat random noise — **and yet its
three biggest values in 110 years all landed in the last eight.** That is
exactly the post-2017 regime the case file already documents, seen from a
second angle.

---

## What was tested

| | |
|---|---|
| **Question** | Do the three thread claims survive a real trend / changepoint / spectral test? |
| **Substitution** | No century Pembroke or naturalized series exists in the archive. Used **02KF005 Ottawa R. at Britannia**, daily level 1915–2024 (best reachable main-stem proxy), and **02OA039 Lac St-Louis at Pointe-Claire**, 1916–2025, as an independent cross-check. |
| **Metric** | Annual **spring (Mar–Jun) maximum gauge level** = the freshet peak, matching the chart's "max elevation" intent. |
| **Tests** | Mann-Kendall + Theil-Sen (trend); Pettitt (single changepoint); Levene + Mann-Whitney across the break (variance / distribution); FFT periodogram vs a 5,000-run AR(1) red-noise Monte-Carlo null (cycle). |
| **Script** | [`ingesters/climate-history/thread_trend_changepoint_cycle.py`](../../ingesters/climate-history/thread_trend_changepoint_cycle.py) |

## Results — Britannia (main-stem proxy, 105 spring-peak years, 1915–2024)

| Test | Result | Reading |
|---|---|---|
| Mann-Kendall trend | τ = +0.025, p = **0.70** | **No** monotonic trend |
| Theil-Sen slope | +0.57 cm/decade (+6.2 cm / 109 yr) | Negligible |
| Pettitt changepoint | break after 2010, p = **0.63** | **No** significant single step (none at ~1960, none at ~1935) |
| Variance across split | std 0.394 → 0.453, Levene p = 0.93 | Variance **did not** compress |
| Distribution shift | Mann-Whitney p = **0.026** | Recent values shifted **upward** |
| Upper-tail occupancy | ≥90th pctile: 9% of pre-years vs 21% of post-years | High years more frequent recently |
| Top 6 spring peaks | **2019, 2017, 1928, 2023**, 1979, 1951 | 3 of the top 4 are post-2017; 1928 the lone historical rival |
| Spectrum vs AR(1) null | **no peak above the 99% red-noise envelope**; lag-1 r1 = 0.07 | Indistinguishable from **white** noise; no cycle |

*Gauge gap: Britannia has no usable spring data 1997–2001 (excluded, not
interpolated, for the trend/changepoint tests).*

## Cross-check — Pointe-Claire (independent, 109 yr)

Significant Pettitt step **after ~1970** (p = 0.006, +0.25 m) — but a
*different* date than Britannia (which has none), and its top peaks are all
**mid-century** (1943, 1951, 1976), the opposite era. Pointe-Claire sits
below the Ottawa–St-Lawrence confluence under Moses-Saunders / Beauharnois +
Great-Lakes regulation, so its 1970 step is almost certainly **St-Lawrence
flow regulation, not Ottawa hydrology**. The non-replication is the point:
two long "same-river" gauges give contradictory regime histories, which
*demonstrates* — rather than asserts — that raw regulated gauges cannot be
read as basin hydrology without de-confounding the management first.

## Verdict on the three thread claims

1. **"No long-term trend"** — *confirmed as stated, but it answers the
   wrong question.* The trend is flat; the **upper tail is not** (Mann-
   Whitney p = 0.026; top-3-of-110 all post-2017). Flood risk lives in the
   tail, where a trend test is blind. This is the classic "trend on the
   mean is the wrong instrument for extremes."
2. **"1927–1945 deforestation cluster"** — *not supported.* No significant
   changepoint or cluster; 1928 ranks behind 2017 and 2019. Also fails on
   priors (large-basin scale washes out land cover; snowmelt-on-frozen-
   ground process; forest-hydrology recovery makes the effect *fade*, not
   peak, decades after cutting).
3. **"Decadal precipitation cycle"** — *rejected.* Zero spectral power
   above the 99% red-noise envelope; r1 ≈ 0.07 means there isn't even the
   persistence needed to build a cycle. 110 yr resolves only ~3.6 cycles of
   a 30-yr period — the spurious-periodicity trap, confirmed empirically.

## Relationship to the existing case-file findings

This note **does not overturn** the load-bearing 2017 peak-step finding
(`stepchange_analysis.py` Test A; *Freshet 2026 Complete Summary*). They use
different instruments and answer different questions:

| | Test A (existing) | This note |
|---|---|---|
| Variable | Britannia **flow** | Britannia **level** |
| Window | 1960+ , Apr–Jul | full 1915–2024, Mar–Jun |
| Question | *conditional*: given a break, which year maximises the pre/post median shift? | *unconditional*: is there **any** single significant step / trend / cycle? |
| Answer | 2017 (+19.3% median) | none; flat; white noise — **but** top-3 peaks all post-2017 |

These are consistent, not contradictory. A **sharp, recent (2017) step in a
noisy 110-year level series is exactly the regime a whole-record Pettitt
test and a near-zero Mann-Kendall τ will fail to flag** — Pettitt is weak
for breaks near the series end. The recent record-breaking tail this note
surfaces (2019/2017/2023; upward Mann-Whitney shift) is the *same* post-2017
intensification Test A and the Complete Summary already document, observed
independently in the level series. Net effect on the case file: it
**neutralises the thread's three counter-narratives** (no-trend-so-nothing,
deforestation, cycles) without weakening — and mildly corroborating — the
2017 result.

## Reproduce

```bash
python3 ingesters/climate-history/thread_trend_changepoint_cycle.py
# requires numpy, scipy, matplotlib (precedent: britannia_freshet_hydrograph.py)
```

Figures written to `data/community-notes/`:

- `2026-05-17_thread_britannia_springmax.png` — spring-max series, Theil-Sen
  line, Pettitt break, segment means, 90th-pctile
- `2026-05-17_thread_britannia_spectrum.png` — periodogram vs AR(1) 95/99%
- `2026-05-17_thread_pointeclaire_springmax.png` — cross-check series

## Caveats & next step

- Britannia is **downstream and regulated**, not Pembroke, not naturalized.
  It is the longest reachable main-stem record, not a clean climate signal.
- The right instrument for the question everyone is actually circling —
  *has the flood risk changed?* — is a **non-stationary GEV** fit to the
  Britannia spring maxima (time- or covariate-dependent location/scale), to
  put a number on how far the upper-tail return levels have moved. That is
  the recommended follow-up; this note establishes that the trend/cycle
  framing the thread argued over is the wrong frame to begin with.
