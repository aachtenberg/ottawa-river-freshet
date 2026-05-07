# Why is May the worst month? A look at the Britannia flow record

*Companion brief, 2026-05-07. Suitable for sharing in the Northern
Reservoirs / Ottawa River / Tourism / Wildlife / Flood Watch group's
Files section. All numbers reproducible from public Water Survey of
Canada and ECCC station records — see the full case file at
[github.com/aachtenberg/ottawa-river-freshet](https://github.com/aachtenberg/ottawa-river-freshet)*

---

## The question

On the May 6 CBC explainer thread, Dan Poole pushed on a specific
observation: across both Pembroke and Lac Coulonge, the post-2017
spring water-level shifts concentrate in May more than any other
month. Why?

Two competing explanations come up:

1. **Later springs** — climate change is shifting the snowmelt
   schedule, so the freshet peak that used to fall in late April now
   falls in mid-May.
2. **Operations + volume** — the basin is genuinely carrying more
   water annually, and the operating rules at the dams haven't
   adapted, so reservoirs fill faster and are forced into bigger May
   releases.

This brief tests both against the public Water Survey of Canada flow
record at Britannia (1972–2024) and Environment Canada temperature
data at four upper-basin stations.

---

## Result 1 — May is genuinely the standout month

Comparing 1972–2016 average monthly flows at Britannia to 2017–2024:

| Month | Pre-2017 (m³/s) | Post-2017 (m³/s) | Change |
|---|---:|---:|---:|
| March | 1,351 | 1,438 | **+6 %** |
| April | 2,150 | 2,367 | **+10 %** |
| **May** | **2,068** | **2,765** | **+34 %** ← |
| June | 1,306 | 1,537 | **+18 %** |

May has shifted by 700 m³/s — about 3× the percent shift of April,
5× the shift of March. In the freshet window, May is in a different
category from the other months.

---

## Result 2 — May has overtaken April in the years that matter

Pre-2017, the ratio of May flow to April flow averaged **0.99** —
they were essentially equivalent magnitudes, with May usually being
the start of the recession. Post-2017, the ratio is **1.20** — May
routinely exceeds April.

Year by year since 2017:

| Year | April flow | May flow | May ÷ April |
|---|---:|---:|---:|
| 2017 (super-flood) | 3,115 | 3,855 | 1.24 |
| 2018 | 1,234 | 2,918 | 2.36 |
| 2019 (super-flood) | 2,851 | 5,174 | 1.81 |
| 2020 | 2,768 | 1,908 | 0.69 |
| 2021 | 1,386 | 922 | 0.67 |
| 2022 | 2,488 | 2,287 | 0.92 |
| 2023 (super-flood) | 2,824 | 3,291 | 1.17 |
| 2024 | 2,271 | 1,763 | 0.78 |

In every super-flood year (2017, 2019, 2023), May exceeded April by a
meaningful margin. Pre-2017, the freshet peaked in April and started
receding in May. Post-2017, in the years that flood, May *is* the
peak month. **This is a change in the shape of the freshet itself,
not just its magnitude.**

---

## Result 3 — Springs are NOT arriving later

If "later snowmelt" were the explanation, three things should shift
later post-2017: the day the river first crosses high-flow, the day
of the annual peak, and the day upper-basin temperatures cross
springtime thresholds.

None of them have:

| What | Pre-2017 | Post-2017 | Change |
|---|---|---|---|
| Annual peak day at Britannia | median May 1 | median May 1 | **unchanged** |
| First day above 3,000 m³/s at Britannia | mean April 20 | mean April 19 | **unchanged** |
| Spring warming at Val-d'Or (first 3-day stretch above +5 °C) | mean DOY 127 | mean DOY 111 | **−16 days (earlier)** |
| Same at Parent | mean DOY 118 | mean DOY 114 | **−4 days (earlier)** |
| Same at Barrage Témiscamingue | mean DOY 108 | mean DOY 105 | **−3 days (earlier)** |
| Same at Rouyn | mean DOY 108 | mean DOY 109 | unchanged |

Across all four upper-basin stations that actually feed the Lac
Coulonge freshet, springs are not arriving later. They're either
earlier or unchanged. The "later springs" hypothesis is refuted at
the source.

---

## Result 4 — But the high-flow window has stretched 11 days longer

The same Britannia record shows the recession ending later:

| What | Pre-2017 | Post-2017 | Change |
|---|---|---|---|
| Last day above 2,000 m³/s in spring | mean DOY 143 | mean DOY 148 | **+5 days later** |
| **High-flow duration (3,000-onset → 2,000-end)** | **35.8 days** | **47.1 days** | **+11.3 days longer** |

Same onset day, same peak day, but the back end of the high-flow
window now reaches 11 days further into May/June than it used to.
That's the difference that produces the +34 % May shift.

---

## What the data shows

The freshet now follows this shape post-2017:

- It starts on the same day as it always did.
- It peaks on the same day as it always did.
- But it stays high for ~11 days longer, with most of those extra
  days falling in May.

The mechanism that fits all four results:

1. The basin is genuinely carrying about 17 % more total water per
   year (separate finding, also confirmed at downstream gauges).
   This is climate / land-use driven and not the operators' fault.
2. The pre-freshet drawdown rule sets reservoirs to roughly the same
   April 1 baseline as it always did.
3. Same baseline + 17 % more inflow → reservoirs fill faster during
   the freshet, are forced into bigger releases through May to avoid
   overtopping.
4. Snowmelt arrives on its historical schedule, but the high-flow
   window can't end on its historical schedule because there's more
   total water to clear.

It's neither pure climate nor pure operations. It's climate-driven
inflow being routed through an operating rule that wasn't designed
for the bigger river.

---

## What this means for the policy ask

Earlier and deeper drawdown wouldn't change the freshet onset day or
the peak day — those aren't the problem. What it would do is reduce
the back-end May overshoot by giving reservoirs more buffer to
absorb the surge instead of having to release it.

The load-bearing month for the "drawdown earlier" argument is **May,
not March**. March is up 6 %; May is up 34 %. The decision to drop
the reservoirs has to happen before May becomes the problem — which
means before April 1 in any year with significant upper-basin
snowpack.

---

## Sources and reproducibility

- **Britannia daily flow** (WSC station 02KF005, 1960–2024):
  Open Government Licence, available at
  [collaboration.cmc.ec.gc.ca](https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/).
  Local archive: `data/wsc-hydrometric/britannia-ottawa-river/daily.csv`.
- **Upper-basin temperature** (Environment Canada daily climate, 4 stations
  Val-d'Or, Rouyn, Parent, Barrage Témiscamingue):
  [climate.weather.gc.ca](https://climate.weather.gc.ca/).
  Local archive: `data/eccc-climate/<station>/raw/<year>.csv`.
- **Reproduction script**:
  `ingesters/climate-history/freshet_shape_analysis.py`.
  Stdlib only, runs in ~3 seconds, prints all the numbers in this
  brief. Cross-checked against the cluster proxy at
  `freshet.xgrunt.com/history/wsc_daily` — agrees to within 1 m³/s
  every year tested.
- **Full case file**:
  [`docs/analysis/Freshet_2026_Complete_Summary.md`](https://github.com/aachtenberg/ottawa-river-freshet/blob/main/docs/analysis/Freshet_2026_Complete_Summary.md)
  § "Test D — freshet shape change at Britannia".
- **Plain-language summary of the broader case-file argument**:
  [`docs/exhibits/Exhibit_0_Plain_Language.html`](https://github.com/aachtenberg/ottawa-river-freshet/blob/main/docs/exhibits/Exhibit_0_Plain_Language.html).

This brief was compiled in response to a community-thread question.
The findings are open to review and refutation — the data is public,
the script is public, the case file is public.
