# The 1970s precedent: a near-twin decade for 2017-2026, except at the top tail

**Compiled 2026-05-27. Companion to [Carillon peaks + volume narrative](2026-05-27_carillon_peaks_volume_narrative.md). Sidecar finding from a rolling-window scan that nuances the main doc's "factor-of-5 clustering" framing.**

## In one line

**The rolling 10-year mean is not unprecedented. The magnitude at the top is.**

The rate of "wet years" the Ottawa basin produces in a decade has not changed since the 1970s. What has changed is the ceiling on what a wet year can produce.

## Plain language summary

The main exhibit says the recent decade (2017-2026) is unusual because it has four flood years (peak ≥ 7,500 cms) where the prior 50 years had four total. That is true at the strict flood threshold. **But if we loosen the threshold even one notch, the 1970s match or exceed the recent decade on every measure except the absolute extremes.** The recent decade is not without precedent at the body of the distribution; it is distinctive at the top tail.

Concretely:
- Rolling 10-year mean peak: 2017-2026 is 6,551 cms; 1972-1981 is 6,208 cms. Difference ~340 cms, well inside year-to-year variability.
- Max peak: 9,217 cms (2019) vs 8,190 cms (1976). +13%.
- Floods at the strict ≥7,500 cms threshold: 4 vs 2. +100%.
- New phenomenon in 2017-2026 with no clear 1970s analog: peakedness-driven floods (2023, 2026), where ordinary total water produced extreme peak flow.

This note saves the rolling-window numbers so we can reference them without re-running the scan.

## Head-to-head: 1972-1981 vs 2017-2026

| Metric | 1972-1981 | 2017-2026 |
|---|---|---|
| 10-year mean peak | 6,208 cms | 6,551 cms |
| 10-year median peak | 6,222 cms | 5,860 cms |
| Max peak | 8,190 cms (1976) | 9,217 cms (2019) |
| Min peak | 4,668 cms | 4,224 cms |
| Years above long-run 76-yr mean (5,481 cms) | 7 of 10 | 7 of 10 |
| Floods at ≥7,500 cms | 2 (1974, 1976) | 4 (2017, 2019, 2023, 2026) |
| High-peak years at ≥6,052 cms (top-quintile threshold) | 5 (1972, 1974, 1976, 1979, 1981) | 4 (2017, 2019, 2023, 2026) |

At top-quintile threshold, **1972-1981 has more clustered high-peak years than 2017-2026.** It is only at the strict 7,500-cms threshold that the recent decade pulls ahead.

## Rolling 10-year mean peak: leaderboard

The eight most-elevated 10-year windows across the full 1950-2026 record, by mean annual peak above the long-run 5,481 cms:

| Rank | Window | 10-yr mean | Above long-run |
|---|---|---|---|
| 1 | 2017-2026 | 6,551 cms | +1,070 |
| 2 | 2016-2025 | 6,367 cms | +886 |
| 3 | 2014-2023 | 6,352 cms | +870 |
| 4 | 2015-2024 | 6,253 cms | +771 |
| **5** | **1972-1981** | **6,208 cms** | **+727** |
| **6** | **1971-1980** | **6,157 cms** | **+675** |
| **7** | **1974-1983** | **6,154 cms** | **+673** |
| **8** | **1970-1979** | **6,123 cms** | **+641** |

Four of the top-eight elevated-mean decades are inside the 1970s. The other four are inside the recent decade. The 76 intervening years contain no comparable elevation period.

## Years above long-run mean, per decade

Share of years in each decade where annual peak exceeded the long-run mean (5,481 cms):

| Decade | Share above mean | Years above |
|---|---|---|
| **1970s** | **7 of 10 (70%)** | 1971, 1972, 1973, 1974, 1975, 1976, 1979 |
| 2020s (partial) | 4 of 7 (57%) | 2020, 2023, 2025, 2026 |
| 1950s | 4 of 10 (40%) | 1951, 1953, 1955, 1957 |
| 1980s | 4 of 10 (40%) | 1981, 1983, 1984, 1985 |
| 1990s | 4 of 10 (40%) | 1991, 1996, 1997, 1998 |
| 2010s | 4 of 10 (40%) | 2016, 2017, 2018, 2019 |
| 2000s | 3 of 10 (30%) | 2002, 2008, 2009 |
| 1960s | 1 of 10 (10%) | 1960 |

The 1970s lead. The 1960s are the driest decade on record.

## Reading this against the main exhibit

The main exhibit's "factor-of-5 clustering" claim is correct **at the 7,500-cms flood threshold.** Four such floods in 10 years (2017-2026) vs four in 50 years (1950-1999) is a real 5x rate increase, and is the answer to "how often have we seen flood-level peaks recently."

But "is the recent decade unprecedented" is a different question and admits a different answer. By 10-year-mean peak, by share-of-years-above-average, and by top-quintile-clustering, the 1970s are a near-twin. What is distinctive about 2017-2026 is the **top tail** of the distribution: more years crossing the strict flood threshold (4 vs 2), a higher absolute max (9,217 vs 8,190 cms), and the appearance of peakedness-driven floods like 2023 and 2026 (Figure 4 in the main exhibit) that do not have an obvious precedent in the 1970s record.

So: the body of the distribution is comparable to the 1970s. The extremes have moved. Both observations are correct simultaneously and the framing of the answer depends on which one the questioner is actually asking about.

## Method

- Data: same source as the main exhibit (ORRPB 1964-2025 Carillon outflow, plus 1950-1963 estimates from WSC 02KF009 Chats Falls regression, plus 2026 HQ daily-mean peak).
- Rolling windows: every 10-year window with start year from 1950 to 2017 inclusive (68 windows).
- Thresholds: 7,500 cms (main-exhibit flood threshold), 7,677 cms (90th percentile), 6,052 cms (80th percentile).
- "Long-run mean" = 5,481 cms, computed over the full 1950-2026 record (n=77).
- Source script for these numbers is the inline ad-hoc analysis from the 2026-05-27 working session; can be re-run from `data/orrpb-historical-summaries/ottawa-river-at-carillon.csv` + the Chats Falls regression in `kathy_black_historical_carillon.py`.
