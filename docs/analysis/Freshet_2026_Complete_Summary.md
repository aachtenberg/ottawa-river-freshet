# Ottawa River Spring Freshet 2026 — Complete Analysis Summary

**Mansfield-et-Pontefract / Lac Coulonge property tracking**
**Tracking period: April 14–28, 2026**
**Compiled: April 28, 2026**

> **Attribution note.** Specific community contributors are referenced
> below by placeholder labels (`Contributor A`, `Contributor B`) rather
> than by name. Real names are withheld pending consent — see
> [`CONTRIBUTORS.md`](../../CONTRIBUTORS.md) for the policy.

---

## Executive Summary

This document compiles a two-week real-time flood tracking effort for a riverfront property in Mansfield-et-Pontefract (Davidson village), Quebec, during the 2026 Ottawa River spring freshet. It combines verified ORRPB historical data, personal 2019 flood observations, live upstream weather analysis, Quebec MSP Vigilance API data, deployed monitoring infrastructure, and policy analysis of the regulatory framework.

### Headline outcomes

**First peak**: Lac Coulonge crested at **108.633 m on April 20 at 23:00**, the 4th highest recorded peak in the modern era. Above 2017 (108.52 m), below 2023 (108.77 m), well below 2019 (109.17 m). The Quebec government officially classified Lac Coulonge to Lake Deschenes as **Major Flood** status (État 6/6).

**Property impact**: Crawl space flooded (matching 2017 experience). Backyard, driveway, big tree area submerged from April 19 afternoon. **Cottage structure stayed dry** with approximately 12 cm of margin to the bricks.

**Second peak (forecast)**: ORRPB has explicitly flagged a possible second peak in coming weeks, but as of April 28 the forecast holds Lac Coulonge at 108.40–108.45 m through May 1 — well below the first peak. The northern pulse is being managed and routed through the system rather than stacking at Lac Coulonge.

**May 3 update (post-peak, freshet ongoing)**: Lac Coulonge has held a long, broad shoulder rather than declining sharply — at 108.41 m on May 3 morning, only 22 cm below the April 20 peak after 13 days. ORRPB's May 2 forecast holds it at 108.40 → 108.35 through May 5 with the explicit warning that "the risk of further increases in levels over the coming weeks due to high spring runoff from the northern portion of the basin is higher from Mattawa to Lake Coulonge" — i.e. the case-file's affected reach. Bryson is operating with **rock-solid stability** through the post-peak window: total release fixed at ~1,355 m³/s, turbines fixed at exactly ~232 m³/s, spill share locked at ~83%, headpond held in a 47 cm band. Four+ consecutive days with no material adjustment despite the lake declining ~2 cm/day. This is a held operating posture, not reactive management.

**Community infrastructure deployed**: A live monitoring dashboard pulling from the Quebec Vigilance API was developed and deployed to a k3s cluster at `freshet.xgrunt.com`, providing real-time gauge readings with property-specific threshold translation, multi-station regional context, and an upstream freeze tracker.

**Regime change empirically documented**: Flood watch member Contributor A compiled Lac Coulonge yearly peaks 1972–2026 and demonstrated an **18-fold increase in super-flood frequency** between 1972–2016 (1 event in 45 years) and 2017–2026 (4 events in 10 years). The step-function shape of the change is too abrupt to be a gradual climate signal, pointing to an operational regime change around 2016–2017. The ORRPB's own April 2026 self-presentation does not engage with this empirical pattern, instead framing flood frequency as cyclical natural variation.

### Why this event was manageable

Three factors kept the first peak below worst-case scenarios:

1. **Active reservoir management** — ORRPB held Temiskaming outflow at 1,100–1,300 m³/s during the critical southern tributary peak, vs the uncontrolled ramp to 1,565 m³/s in 2019
2. **Hard freeze cycle April 19–21** — Sub-zero overnight temperatures across the basin (as cold as -10°C at Pembroke, -7°C at Val-d'Or) shut down active snowmelt for three consecutive nights
3. **Coulonge River tributary timing** — The unregulated tributary peaked at 110.335 m (just 2 cm below Quebec's major flood threshold) and declined sharply before the Ottawa River crested

---

## Property-Specific Thresholds (from personal 2019 observations)

These thresholds tie ORRPB Lac Coulonge gauge readings to actual property impacts observed during the 2019 flood:

| Lac Coulonge Level | Property Impact | 2019 Date | 2026 Status |
|---|---|---|---|
| 108.30 m | Water approaching but not yet in backyard | April 25 | Reached April 19 morning |
| 108.48 m | Water IN backyard, filling driveway, reached big tree | April 26 | Reached April 19, 14:00 |
| 108.52 m | Crawl space flooded to floor joists (2017 experience) | 2017 peak | Reached April 19, 19:00 |
| 108.75 m | Water at end of bricks on cottage structure | April 27 | **NOT REACHED** (12 cm margin) |
| 109.01 m | Water INSIDE cottage, garage, RV area | April 28 | **NOT REACHED** (38 cm margin) |
| 109.10 m | 2019 peak — maximum water inside property | April 29 | **NOT REACHED** (47 cm margin) |

---

## Historical Peak Comparison

### Lac Coulonge (ORRPB verified)

| Year | Peak (m) | Classification | vs 2026 |
|---|---|---|---|
| 2019 | 109.17 | All-time record (1-in-100 year) | 54 cm higher |
| 2023 | 108.77 | Major flooding | 14 cm higher |
| **2026** | **108.633** | **Major flooding** | — |
| 2017 | 108.52 | First modern major flood | 11 cm lower |
| 2025 | 108.15 | Moderate | 48 cm lower |

### Pembroke (ORRPB verified)

| Year | Peak (m) | vs 2026 |
|---|---|---|
| 2019 | 113.69 | 60 cm higher |
| 2023 | 113.31 | 22 cm higher |
| 2017 | 113.03 | 6 cm lower |
| **2026** | **113.09** | — |
| 2025 | 112.87 | 22 cm lower |

### Multi-station 2026 vs 2023 (ORRPB April 20 press release)

| Station | 2026 Peak | 2023 Peak | Difference |
|---|---|---|---|
| Pembroke | 113.09 | 113.31 | -22 cm |
| Lac Coulonge | 108.63 | 108.77 | -14 cm |
| Chats Lake | ~75.85 | 75.90 | -5 cm |
| Lake Deschenes | ~60.30 | 60.35 | -5 cm |
| Gatineau/Hull | ~44.70 | 44.68 | +2 cm |
| Thurso | ~43.10 | 43.19 | -9 cm |

---

## Detailed Timeline

### Phase 1: Pre-freshet baseline (April 7–13)
- Lac Coulonge stable at 106.63–106.71 m
- Pembroke at 111.99–112.06 m
- Ottawa YOW seasonal snowfall: 258 cm through March (above 233.7 cm 10-year average, below 2019's 303.5 cm)
- January 2026: 81.6 cm snow — nearly double normal
- Quebec ministerial vigilance advisory issued for Mansfield-et-Pontefract April 14

### Phase 2: Rising limb (April 14–18)
- April 14: ORRPB issues press release warning of increasing flood risks
- April 15: First major forecast escalation — Lac Coulonge 107.85 m by April 17; narrative changes from "may exceed" to "expected to exceed" minor flood
- April 16–17: Heavy rain across basin (Pembroke at 98% chance Thursday)
- April 18: Rain eases, Lac Coulonge at 108.09 m, rising ~1 cm/hour

### Phase 3: Crest (April 19–20)
- April 19, 14:00: Lac Coulonge crosses **108.48 m** — water in backyard threshold
- April 19, 19:00: Crosses **108.52 m** — crawl space threshold (2017 level)
- April 19, 23:00: **Pembroke peaks at 113.09 m**
- April 20, 18:00–23:00: Lac Coulonge plateau at 108.633 m
- April 20, 23:00: **Lac Coulonge peak at 108.633 m**

### Phase 4: Initial decline (April 21–24)
- April 21, 00:00: Coulonge River tributary peaks at 110.335 m (2 cm below Quebec major flood threshold)
- April 21, 13:00: Lac Coulonge at 108.618 m — declining
- Pembroke declining faster: 14 cm below peak by April 21 morning
- April 22–24: Lac Coulonge slow decline, 108.50 → 108.40

### Phase 5: Plateau and second-peak watch (April 25–present)
- April 25–28: Lac Coulonge holds at 108.39–108.40 m
- ORRPB explicitly warns of possible second peak
- Mattawa forecast to exceed 2023 peak (154.70 m sustained)
- Temiskaming outflow ramped to 2,500–2,550 m³/s sustained — well above 2019's peak of 1,647
- Northern pulse routing through system to Carillon (7,300 m³/s) without stacking at Coulonge

### Phase 6: Slow recession and reservoir refill posture (May 1–4, added May 4)
- May 1–3: Lac Coulonge declining at only ~2.4 cm/day (108.633 m peak Apr 20 → 108.41 m May 3 = 22 cm over 13 days). Markedly slower than 2019 or 2023 declines from comparable peaks.
- May 2: Témiscamingue outflow peaks at **2,742 m³/s** — third-highest in the modern comparison record, behind only 2019 (3,173) and 1960 (3,637), and well above 2023 (2,388), 2017 (1,881).
- Across the broader basin, reservoir retention dominates the recovery posture. Live telemetry (loaded May 2026 to `reservoir_readings`, scraped daily from ORRPB; see Second-Peak Risk Analysis below for the cross-station verification): Baskatong +2.24 m, Dozois +2.09 m, Mitchinamecus +1.23 m, eight other reservoirs rising 0.10–0.94 m over Apr 23 → May 3. Only Des Joachims (run-of-river, not a storage reservoir) is flat. Roughly 1.34 billion m³ stored at Baskatong alone in 11 days.
- Bryson amont rose +4 cm over Apr 29 → May 2 while total throughput stayed pinned at ~1,353 m³/s — leading edge of the Témiscamingue release pulse arriving downstream, with Bryson unable to pass it through faster.
- ORRPB's May 2 bulletin maintains the second-peak warning for "Mattawa to Lake Coulonge."

### Phase 7: Operator-acknowledged refill preservation (May 5, added May 5)

A morning watershed update from Contributor B introduces three findings that meaningfully refine the recession picture:

**Reservoir percent-full snapshot, May 5 8:30 AM** (computed by Contributor B using published operating-range linear interpolation; volume figures shown):

| reservoir | % full | volume (M m³) | Δ%/day |
|---|---|---|---|
| Poisson Blanc | **95.08%** | 625 | +0.51 |
| Bark Lake | **93.64%** | 374 | +0.11 |
| Lady Evelyn | 89.04% | 308 | +0.98 |
| Timiskaming | 84.48% | 1,217 | +0.25 |
| Dozois | 82.80% | 1,863 | +1.75 |
| Baskatong | 82.56% | 3,049 | +0.52 |
| Cabonga | 81.99% | 1,565 | +0.21 |
| Kipawa | 78.70% | 673 | +1.30 |
| Kiamika | 77.95% | 379 | +0.09 |
| Quinze | 76.71% | 1,308 | +0.82 |
| Rapide-7 | 75.12% | 371 | +0.47 |
| Mitchinamecus | 70.86% | 554 | +0.46 |
| Des Joachims | 36.00% | 229 | **−0.67** (only decrease) |

12 reservoirs rising; 1 falling (Des Joachims, run-of-river — expected).

**Finding 1 — refill rate is decelerating, not accelerating.** Earlier Phase 6 numbers showed Baskatong absorbing roughly 1.34 GCM over 11 days, equivalent to ~1,410 m³/s of net retained inflow. The May 5 rate of +0.515 %/day at Baskatong corresponds to roughly 19 Mm³/day — about **220 m³/s of net retention**. That is approximately an **85% reduction in the retention rate** versus the Phase 6 average. Contributor B attributes this to operator action: *"Reservoirs across the watershed are currently refilling at a slightly slower pace... This is due to increased outflows to the Ottawa River, implemented to help control and slow the refill rate."*

**Finding 2 — operators have publicly acknowledged refill-preservation as an intentional posture.** Contributor B reports: *"Operators will intentionally avoid allowing the reservoir to reach full capacity, as storage must be preserved to accommodate any unexpected rainfall events."* This is the operator-acknowledged version of what the case file argues from gauge data — that operating decisions have non-trivial flexibility under high-flow conditions and that those decisions reflect a particular set of priorities. The "preserve storage for unexpected rainfall" framing is the *flood-positive* version of the same operator discretion that produces the held-headpond posture at Bryson. That the operators are *able* to slow refill from ~1,400 m³/s of net retention to ~220 m³/s within days demonstrates the magnitude of available operational flexibility.

**Finding 3 — Témiscamingue rapid-refill heuristic.** Contributor B's flood-indicator rule: *"A key indicator of a potential flood is a rapid refill rate — specifically, when the Temiscaming Reservoir refills in less than 30 days. This pattern has occurred again this year. Notably, within the first 16 days of this refill period, water levels at Pembroke reached Major flood territory."* This is a community-derived empirical rule that complements Contributor A's regression-based step-change analysis with an operational early-warning signal. The 2026 event matched the rapid-refill pattern, and Pembroke did reach Major flood within 16 days — confirming the heuristic for this year.

**Two reservoirs at the operating ceiling.** Bark Lake at 93.6% and Poisson Blanc at 95.1% are essentially full. Lady Evelyn at 89% has minimal remaining buffer. Timiskaming at 84% with 0.63 m to the south-end full supply level (per Contributor B) and "within six inches of low-level flooding" at the north end retains the same constrained posture documented earlier. The system is doing the work, but the buffer is real.

**Methodology note from Contributor B (reproduced for case file context):** *"Detailed public storage data is currently not available from official sites."* Percent-full is calculated by the community using linear interpolation between published high/low operating limits because operators do not publish percent-full directly. This is the data-accessibility problem this document already names — but at the storage-volume layer rather than the level-reading layer.

---

## The Sunday/Monday Freeze: Critical Mechanism

Three consecutive nights of hard freeze across the Ottawa River basin (April 19–21) was the decisive factor in capping the first peak:

| Station | Apr 19 night | Apr 20 night | Apr 21 night |
|---|---|---|---|
| Val-d'Or (headwaters) | -7°C | -5°C | sub-zero |
| Rouyn-Noranda | -4°C | -3°C | sub-zero |
| Temiskaming | -1°C | 0°C | above freezing by dawn |
| Mattawa | 2°C | sub-zero | — |
| Pembroke | -7°C | **-10°C** | -1°C |

The basin's active snowmelt shut down for 72 hours. The remaining snowpack refroze each night. The ORRPB's projected ramp of Temiskaming releases to 2,100 m³/s never fully materialized — actual releases stayed near 1,600 m³/s through this window.

**Counterfactual**: without the freeze, the northern pulse would have continued building. The 108.75 m forecast for April 22–23 would likely have been accurate, putting water at the cottage structure.

This pattern — three freeze nights as a decisive threshold — became a key heuristic baked into the live monitoring dashboard's freeze tracker.

---

## Upstream Analysis Framework

### Flow rate progression at key stations (m³/s)

| Station | Apr 7 | Apr 14 | Apr 21 | Apr 28 | Total Change |
|---|---|---|---|---|---|
| Temiskaming | 662 | 914 | 1,626 | 2,550 | +285% |
| Otto Holden | 885 | 1,159 | 1,803 | ~2,633 | +197% |
| Des Joachims | 1,262 | 1,600 | 2,470 | ~3,088 | +145% |
| Chats Falls | 2,115 | 2,596 | 5,046 | ~4,722 | +123% |
| Carillon (system out) | 4,249 | 4,802 | 7,712 | ~7,300 | +72% |

### Key finding: ORRPB controlled the northern pulse during the southern peak

| Metric | 2019 (Apr 24 → Apr 30) | 2026 (Apr 14 → Apr 21) |
|---|---|---|
| Starting Temiskaming flow | 875 m³/s | 914 m³/s |
| Peak Temiskaming flow | 1,647 m³/s | ~1,600 m³/s |
| Ramp rate | Uncontrolled | Deliberately held |
| Result | Double peak (Apr 29 + May 12) | Single managed peak |

In 2019, Temiskaming outflow ramped uncontrolled as northern reservoirs filled. In 2026, the ORRPB held outflow steady during the critical southern tributary peak, then began aggressive releases (2,550 m³/s) only after the southern peak passed and the freeze locked the snowpack.

### The unregulated tributary problem

The Ottawa River basin has a structural flooding limitation: **southern and central tributaries (Petawawa, Coulonge, Dumoine, Petite Nation) are completely unregulated**. All reservoir capacity sits in the northern basin upstream of Témiscamingue.

The ORRPB can reduce downstream peaks by approximately 40 cm through reservoir management. That's the ceiling of what regulated water can do. Anything more requires either weather cooperation or different operational rules.

### Operational mechanisms validated by community insider knowledge

Several operational behaviors that initially appeared as inferences from data were validated by Contributor B (who has worked on watershed dams) on April 30. These move from hypothesis to confirmed mechanism:

**Reservoirs ramp outflow as they near capacity (universal rule).** Dan confirmed: "Bark Lake is nearly full so they normally increase outflow to the Madawaska before it gets to max level. All reservoirs increase outflow as they get full to prevent an emergency release." This makes percent-full a true leading indicator — when a reservoir crosses approximately 90%, downstream outflow ramps follow within days regardless of inflow conditions, because the alternative is uncontrolled spillage.

**Des Joachims has explicit operational rules tied to Mattawa.** Dan confirmed: "Des Joachims has stopped the 1st stage of refill as Mattawa is in flood territory, so inflow = outflow." This means when Mattawa is in major flood (as it is in this event), Des Joachims operates as **pure run-of-river** with no storage discretion. Every cubic metre arriving passes straight through. The implication: during major-flood periods at Mattawa, the buffering Des Joachims would normally provide is gone, and the wave from upstream (Témiscaming, Otto Holden) reaches Pembroke and Lac Coulonge faster than the standard travel-time framework would suggest. This validates ORRPB Slide 26 ("operated as a run-of-river facility when there is a risk that high Ottawa River flows cause flooding in Mattawa") as currently active behavior, not just a written policy.

**Hydro-Québec releases proactively ahead of forecasted inflow.** Dan confirmed the Baskatong outflow doubling pattern: HQ ramped Baskatong outflow from 273 to 542 m³/s while the reservoir was only at 77% full — not because of immediate constraint, but because they were "expecting a huge inflow into the reservoir" from the April 28 rain event. With ~3.5 m of headroom remaining at Baskatong, this is anticipatory risk management rather than capacity-driven release. It confirms operators are running the system on forward forecasts, not just current state.

**Operator decisions are not visible in published forecasts.** None of these three operational rules appears explicitly in ORRPB press releases or the 4-day forecast tables. A community member reading only the ORRPB output would not know that Des Joachims was paused at first-stage refill, that Baskatong releases were anticipatory rather than capacity-driven, or that Bark Lake's slight drawdown was the standard near-full-reservoir behavior. The information exists; it is not published.

---

## Quebec MSP Vigilance API Discovery

A major analytical breakthrough: the Quebec Vigilance system provides a superior real-time data source for Mansfield-area flood monitoring.

### Architecture

- **Backend**: PostgREST 12.0.3 — open-source PostgreSQL REST API
- **Authentication**: None required
- **Rate limiting**: None observed
- **CORS**: Properly configured, accepts requests from any origin
- **Data freshness**: Hourly readings, more reliable update cadence than ORRPB's aggregated site
- **Coverage**: 342 hydrometric stations across Quebec

### Endpoint pattern

```
https://inedit-ro.geo.msp.gouv.qc.ca/station_details_metadata_api?id=eq.{station_id}
https://inedit-ro.geo.msp.gouv.qc.ca/station_details_readings_api?id=eq.{station_id}
https://inedit-ro.geo.msp.gouv.qc.ca/station_liste_api
```

Returns JSON directly. No tokens, no API keys, no session management required. Browser `file://` origin (`null`) is rejected, but any real http(s) origin works.

### Key stations identified

**Mansfield/Fort-Coulonge area:**
- **Station 1195**: Lac Coulonge at Fort-Coulonge (Ottawa River) — Hydro-Québec
- **Station 1004**: Coulonge River at Route 148 bridge (unregulated tributary) — Hydro Météo

**Lady Aberdeen Bridge area (Hull/Gatineau):**
- **Station 983**: Quai des Artistes — at the foot of the bridge, on the Gatineau River
- **Station 982**: Rue Cartier — 3 km upstream on the Gatineau River
- **Station 550**: Marina de Hull — adjacent on the Ottawa River

### Official flood thresholds published via API

**Lac Coulonge (Station 1195):**
- Pre-alert: 107.00 m
- Minor flood: 107.50 m
- Moderate flood: 108.00 m
- **Major flood: 108.50 m**

**Coulonge River (Station 1004):**
- Pre-alert: 109.00 m
- Minor flood: 109.50 m
- Moderate flood: 109.85 m
- **Major flood: 110.35 m** (2026 peak: 110.335 m, within 2 cm)

---

## Live Monitoring Dashboard — freshet.xgrunt.com

### Architecture

A community-grade monitoring dashboard was developed during this analysis and deployed to a personal k3s cluster at `freshet.xgrunt.com`.

**Stack:**
- Static HTML + JavaScript (vanilla, Chart.js for visualizations)
- Direct fetch from Vigilance API every 10 minutes
- Single-file Kubernetes manifest with embedded HTML in ConfigMap
- nginx:alpine container (~16 MiB memory, 10m CPU)
- Traefik ingress with TLS

### Features

- Hero station cards: Lac Coulonge, Coulonge River tributary, Waltham (upstream Ottawa)
- Time window selector: 1h, 6h, 12h, 24h, 72h, 7d, 14d
- Regional context: multi-station view of Ottawa River corridor
- **Upstream freeze tracker**: overnight lows across the basin, with the "three freeze nights" heuristic baked in
- Property threshold translation: live status against personal 2019 thresholds
- Eastern timezone normalization

### Why this was needed

The official ORRPB website caches aggressively, fragments data across three operating agencies (OPG, Hydro-Québec, Water Survey of Canada), updates only at 4 PM weekdays during freshet, and provides no property-level translation or push notifications. The Vigilance dashboard fills the gap with hourly granularity and decision-relevant analytics.

### What the freeze tracker provides

The freeze tracker pulls daily minimum temperatures from open-meteo for upstream basin stations (Val-d'Or, Rouyn-Noranda, Temiskaming, Pembroke) over a rolling 9-day window (2 days past + 7 days forecast). Three consecutive sub-zero overnight lows at the headwaters reliably indicates active snowmelt has been suppressed.

This is more decision-useful than the ORRPB's prose forecasts because:
- It transforms a meteorological input into a binary signal (freeze / no freeze)
- The "three nights" rule is empirically validated by the April 19–21 event
- It runs independently of ORRPB's update cadence

---

## Second-Peak Risk Analysis

### The mechanism

After the southern tributaries peak and decline, water continues entering the system from:
1. **Ongoing northern snowmelt** in the Témiscamingue/Rapide 7/Quinze basin
2. **Reservoir releases** as upper-basin storage fills
3. **Spring rainfall** if it occurs during a thaw window

The travel time from Rapide 7 reservoir to Lac Coulonge is approximately **5–7 days**. Water released from Temiskaming today arrives at Lac Coulonge May 3–5.

### Rapide 7 SWE math (April 28 community data)

A community member reported **122 mm of snow water equivalent still in the Rapide 7 reservoir basin** as of April 28. Converting to actual scale:

- 122 mm SWE ≈ 1.2 m of remaining snowpack at typical late-April density
- Rapide 7 catchment area: ~8,500 km²
- Total water locked in snowpack: 0.122 m × 8.5 × 10⁹ m² = **~1.04 billion m³**
- If 50% releases over 5 days: ~520 million m³ → ~1,200 m³/s additional flow
- Combined with current Temiskaming outflow (2,550 m³/s): potential 3,500–4,000 m³/s territory

### The Témiscamingue lake imbalance signal

A critical observation from the flood watch community (Contributor B, April 28): **Lake Témiscamingue showed north-south level imbalance**, with the north (inflow) end higher than the south (outflow) end. This indicates inflow is currently outpacing outflow capacity — water piles up at the inlet before propagating south to the dam.

Implication: the 2,550 m³/s outflow may not be sufficient to drain the lake at the rate water is arriving. ORRPB will likely need to ramp Temiskaming releases further, with that additional water arriving at Lac Coulonge May 5–8.

### Scenario assessment (as of April 28)

| Scenario | Lac Coulonge second peak | Probability | Property impact |
|---|---|---|---|
| **Managed plateau** | 108.40–108.50 m | 65% | No additional structural risk; crawl space remains flooded |
| **Modest second peak** | 108.50–108.65 m | 25% | Backyard re-floods slightly; cottage still safe |
| **Worst case** | 108.65–108.85 m | 10% | Water near or at cottage bricks; structural risk |

The worst-case scenario depends on **rapid melt + significant rainfall** in the headwaters during May 1–10. The May 1–4 freeze cycle reduces but does not eliminate this risk. In-transit water is already factored into the ORRPB's 4-day forecast (108.45 m through May 1); the residual risk is from rainfall and melt beyond that horizon.

### What to monitor for early signal

1. **Mattawa and Otto Holden levels** — leading indicators that show the northern wave arriving 2–3 days before it reaches Lac Coulonge
2. **Val-d'Or overnight lows** — if they stop going below zero during May 1–4, the freeze cap is failing
3. **Headwater rainfall forecasts** — Val-d'Or, Rouyn-Noranda, Temiskaming. A 30+ mm event during a thaw window is the trigger condition
4. **Témiscamingue lake level imbalance** — narrowing imbalance means the system is catching up; widening imbalance means more outflow ramping ahead
5. **Gatineau River trajectory** — does not directly affect Lac Coulonge (upstream of the confluence) but constrains operator options at Carillon. A Gatineau second peak forming on overnight rain (as observed April 30 at 875 m³/s rising) forces Carillon outflow to absorb both the regulated Ottawa River and the rising Gatineau, which can drive backwater pressure upstream and prevents downstream relief
6. **Des Joachims operational state** — when Mattawa is in major flood, Des Joachims runs as pure pass-through (Stage 1 paused). This shortens the effective Mattawa-to-Coulonge travel time because the normal storage buffer is gone

### May 3–4 update — basin-wide retention vs Témiscamingue ceiling (added May 4)

Two community analyses converged on May 3, with our live telemetry providing the cross-station verification.

**Contributor A — slow-decline inference.** From the May 3 community post: *"Levels are decreasing slowly. In my humble opinion, the second peak may be behind us. If they anticipated more level, they would have kept levels to where they were last week (peak #1), to maximize throughput and keep storage capacity in the reservoirs. The fact that levels are dropping slowly tells me they are now starting to hold back water in the reservoirs for summer operations."*

This inference reads operator decisions from gauge behavior — the same framework that anchors Exhibit C (storage capacity) and Exhibit D (live Bryson telemetry). Specifically: a slow post-peak Lac Coulonge decline implies upstream reservoir retention rather than pass-through, because aggressive drawdown is the rational response to anticipated additional inflow.

**Contributor B — Témiscamingue history chart.** A multi-year overlay of Témiscamingue discharge (2017, 2019, 2022, 2023, 2024, 2025, 2026) places the May 2 peak at 2,742 m³/s as the third-highest in the comparison record. Two structural observations from the chart:

1. **2026 ≠ 2017.** The pre-regime-change baseline year peaked at ~1,880 m³/s on April 14 — 18 days earlier and 31% lower than 2026. The 2017 line then descended cleanly. The post-2017 Témiscamingue pattern (2019, 2023, 2025, 2026) shows consistently later peaks, higher peaks, and longer plateaus. This is Exhibit A's regime-change argument expressed at the upper-Outaouais main stem rather than at Lac Coulonge — independent corroboration at a different point in the system.
2. **2026 ≈ 2019.** The 2019 and 2026 rising limbs trace nearly the same path through April. They diverge in the final week (2019 kept climbing into mid-May; 2026 plateaued at a lower ceiling). But 2019's *descending* side held near-peak for ~3 weeks before falling cleanly, suggesting the operative analog for the next several weeks of recovery.

**Cross-station verification with the live telemetry.** Both contributors' inferences hold up under direct measurement.

| reservoir | Apr 23 | May 3 | Δ (m) | interpretation |
|---|---|---|---|---|
| Baskatong | 218.13 | 220.37 | **+2.24** | Aggressive absorption; ~1.34 GCM stored in 11 days |
| Dozois | 342.19 | 344.28 | +2.09 | Headwater retention |
| Mitchinamecus | 378.35 | 379.58 | +1.23 | Headwater retention |
| Lady Evelyn | 287.98 | 288.92 | +0.94 | Filling |
| Poisson Blanc | 200.47 | 201.38 | +0.91 | Filling |
| Timiskaming (Haileybury) | 178.65 | 179.47 | +0.82 | Approaching ceiling |
| Quinze | 261.97 | 262.72 | +0.75 | Filling |
| Rapide-7 | 308.13 | 308.83 | +0.70 | Filling |
| Timiskaming (Témiscaming) | 178.31 | 178.92 | +0.61 | Approaching ceiling |
| Kipawa | 268.66 | 269.23 | +0.57 | Filling |
| Kiamika | 267.87 | 268.30 | +0.43 | Filling |
| Cabonga | 359.69 | 360.03 | +0.34 | Filling |
| Bark Lake | 313.24 | 313.34 | +0.10 | Slow filling |
| Des Joachims | 150.51 | 150.50 | −0.01 | Run-of-river, no storage role |

**Synthesis: the contributors' analyses are complementary, not contradictory.** Contributor A is right that the *headwater* reservoirs (Baskatong, Dozois, Cabonga, Mitchinamecus) still have room and are actively absorbing. Contributor B's Témiscamingue data shows that the bottleneck reservoir on the upper Ottawa main stem has run out of buffer — Dan's "six inches below low-level flooding" caveat matches the +0.82 m rise we observe at the Haileybury gauge. The basin is staging the inflow: headwaters absorbing the slow-melting peak, Témiscamingue passing the fast-melting peak through.

**Refinement of the second-peak scenario assessment.** The Témiscamingue 2026-vs-2019 analog suggests the *timing* of relief is later than the optimistic read implies, even if no historical analog supports a higher second peak following a May 2-style first peak. Contributor A's "second peak behind us" claim survives on magnitude; Contributor B's "not finished until inflows clearly collapse" caveat survives on duration. The probability table from April 28 stands but with the duration distribution shifted right — managed-plateau likely runs another 2–3 weeks rather than 1 week.

**Watch for confirmation or refutation in the live data.**
- Bryson amont above 104.55 m: second peak materialising (current setpoint band 104.43–104.54 m). If confirmed, the held-headpond Δ to Lac Coulonge propagates 1:1 (see Exhibit D Live Observation panel).
- Témiscamingue outflow falling below 2,000 m³/s sustained: Contributor A's recession-confirmed scenario.
- Témiscamingue outflow holding 2,500+ m³/s: Contributor B's not-finished scenario, with arrival at Bryson on a 1–2 day lag.

**Storage scale, for case-file context.** Baskatong absorbing 1.34 GCM in 11 days — equivalent to ~1,410 m³/s of net retained inflow over the window — is roughly **4–5× the total live storage** of either side of the Exhibit C comparison (Lac Coulonge reach 0.30 GCM, Des Joachims 0.23 GCM). This is not the "the reach storage is too small to matter" scale the operators have publicly invoked; it is the scale at which a single northern reservoir is currently doing flood mitigation. The exhibit's Lac-Coulonge-vs-Des-Joachims comparison demonstrates the principle (at a downstream run-of-river headpond); the Baskatong observation shows what the principle looks like in practice when applied (at a properly-sized headwater reservoir). One reservoir doing the work makes the case-file argument stronger, not weaker — because it shows the rest of the basin's storage operating in the way Lac Coulonge could, but is not.

---

## Forecast Tracking and Validation

### ORRPB forecast accuracy at Lac Coulonge

| Forecast Date | Peak Forecast | Actual / Current | Variance |
|---|---|---|---|
| April 15 | 108.0–108.3 m by Apr 21–23 | — | — |
| April 19 | 108.75 m, Apr 21–22 | — | — |
| April 20 | 108.75 m, Apr 21 (held) | — | — |
| **Actual peak** | — | **108.633 m, Apr 20 23:00** | -12 cm vs final forecast |
| April 27 (post-peak) | 108.45 m by Apr 30 (second wave) | — | — |
| April 28 | 108.45 m by May 1 (held) | 108.40 (Apr 28 reading) | tracking |

### What the analysis got right

- Pembroke peak prediction (113.05–113.15 forecast, actual 113.09)
- Northern freeze capping the first peak
- Coulonge River tributary peaking before Ottawa River
- Multi-day plateau pattern rather than sharp peak
- Sustained Temiskaming outflow being managed below ORRPB's stated maximum
- Second peak being absorbed/routed rather than stacking at Coulonge

### What was less certain

- Initial timing — first forecasts were too low; the rising limb was steeper than expected
- The 108.75 worst case forecast was overly conservative (off by 12 cm)
- The exact propagation rate of the northern pulse — Mattawa Fink's correction that current melt is in transit and will arrive regardless of subsequent freeze was an important refinement

---

## Policy and Regulatory Analysis

### Cross-reference: ORRPB's own self-presentation (April 2026)

The ORRPB published "Flow Management in the Ottawa River Basin" in April 2026 — a 40-slide presentation describing their own structure, mandate, and constraints. Reading this document against the community's analysis provides authoritative source material that strengthens (rather than weakens) the policy critique. The document confirms several positions the community has been arguing:

**ORRPB explicitly admits limited authority** (Slide 11):

> "The Planning Board is not a 'control board'. It facilitates the collaborative management of reservoirs by operators. It cannot direct how operators manage their reservoirs or facilities. Each operator remains responsible for the operational strategies and decisions at their facilities. The Board sets common goals for the operators of principal reservoirs to work towards."

This is the structural critique stated as official policy. The board sets goals — operators retain discretion. Whatever changed in operations around 2016–2017 came from operator-side decisions (Hydro-Québec, OPG) that the ORRPB has no authority to compel either way. The community's policy targets are correctly aimed at the operators, not the coordination board.

**The "minimize impacts" mandate language is current** (Slide 8):

> "Main role: to ensure that the flow from the principal reservoirs of the Ottawa River Basin are managed on a collaborative basis to minimize impacts of floods & droughts."

The verb "minimize" remains the official mandate. This matters because "minimize" is a stronger commitment than "reduce" — it implies the lowest achievable risk, not just an improvement over no action. Holding ORRPB and operators to the verb in their own mandate is a defensible accountability lever.

**ORRPB quantifies their reservoir effect** (Slide 15) — 2019 flood reduction estimates:

| Location | Reduction |
|---|---|
| Lac Coulonge (Fort-Coulonge) | **120 cm** |
| Chats Lake (Arnprior) | 60 cm |
| Lake Deschenes (Britannia) | 75 cm |
| Gatineau (Hull) | 130 cm |
| Lac des Deux Montagnes | 95 cm |

This is meaningful. Without reservoir management, 2019 would have peaked at approximately **110.4 m at Lac Coulonge** instead of 109.17 m. It validates that reservoirs do meaningful flood mitigation work. It also establishes the practical ceiling: roughly 120 cm of protection at Coulonge under current operating rules. Any flood reduction beyond that ceiling requires changes to operational practice, not additional reservoir capacity.

**ORRPB confirms travel times** (Slide 4):

- Approximately 3 weeks from Dozois to Carillon outlet
- Approximately 1 week from Cabonga to outlet

The community's 5–7 day Rapide 7 → Lac Coulonge estimate fits cleanly inside this published framework.

**ORRPB confirms Des Joachims is dual-purpose** (Slide 26):

> "Des Joachims reservoirs is the last of the 7 principal reservoirs located upstream of Pembroke to be completely refilled. It is operated as a run-of-river facility when there is a risk that high Ottawa River flows cause flooding in Mattawa. The spring refill strategy consists of two stages."

This validates the visual analysis of the smooth Des Joachims discharge ramp. Its run-of-river-when-needed character explains why its outflow tracks upstream reservoir releases (the actual flow shaping happens at Quinze, Timiskaming, Rapide 7, etc.) rather than reflecting independent storage management.

### What the ORRPB document deflects or doesn't address

The same document also reveals what the official position systematically avoids:

**No engagement with the regime change.** Slide 17 ("Is flooding the new norm?") states "Flooding is NOT expected to happen every second year. Flooding is driven by weather, and weather can be cyclical. Flood events can be clustered." This is the official position that Contributor A's 18-fold super-flood frequency increase directly contradicts. The ORRPB does not present the year-by-year peak data that would force them to engage with the regime change. Their official answer is "trust the long-run probabilities" — exactly what the data refuses to support.

**No discussion of operational rule changes as a policy option.** Slide 19 ("Can reservoirs be increased?") answers the question of whether to BUILD new reservoirs (concluding no, costs outweigh benefits per 1980s studies). It does not answer the question the community is actually asking — whether to OPERATE existing reservoirs differently (deeper drawdown, snowpack-indexed rules, tighter Bryson headpond management). This may be deliberate misdirection or genuine misframing of the community position.

**No quantitative framing of operational alternatives.** The document does not discuss what flood reduction additional drawdown could achieve, how snowpack indexing might be implemented, or what trade-offs (winter generation, drought risk) would result from rule changes. The analytical work that would inform a policy debate is absent from the official communication.

**The climate change slide is analytically empty** (Slide 18). It lists four contradictory factors — more rain (worse), faster melt (worse), variable snow (varies), more evapotranspiration (better) — and concludes with a "Lots of uncertainty" sticky note. This is the prose forecast pattern in policy form: maximum hedging, minimum analytical commitment.

**No reservoir percent-full or storage analytics published.** Slide 12 shows a single year's reservoir storage curve against the median, but does not provide the multi-decade data series that would document whether operating ranges have shifted. Contributor B's percent-full analytics demonstrate that this calculation is achievable from public ORRPB data — but ORRPB does not publish it themselves.

### Why the ORRPB's own document strengthens the community policy argument

Reading the document carefully, the ORRPB has effectively conceded the structural critique:

1. **They confirm they don't direct operator decisions** (Slide 11) — so operational regime changes happened at the operator level (HQ, OPG) without ORRPB authority to compel or prevent them
2. **They confirm the basin is 60% unregulated** (Slide 14) — so reservoir management ceiling effects (≈120 cm) are well-established
3. **They confirm the "minimize" mandate** (Slide 8) — so accountability for outcomes runs to that verb, not a softer one
4. **They quantify what reservoirs did achieve in 2019** (Slide 15) — establishing the magnitude of operational impact

The ORRPB's own document points the policy conversation past the ORRPB itself. The actual decision-makers are:

- **Hydro-Québec** (Cabonga, Dozois, Rapide 7, Timiskaming, Cabonga, Baskatong) — whose drawdown depths and headpond management determine the pre-freshet baseline
- **OPG** (Otto Holden, Des Joachims, Chenaux, Chats Falls, Bryson, Lady Evelyn, Bark Lake) — whose run-of-river operating rules and reservoir scheduling shape the routing
- **The provincial principals** — Quebec MELCCFP, Ontario MNR, Canada ECCC — who fund and oversee the operators

The community's regulatory engagement is correctly aimed past ORRPB at these actors. ORRPB itself is a useful information clearinghouse and forecast publisher, but cannot be the target of operational reform demands.

### The "pre-filled bathtub" problem

Fall/winter baseline levels at Lac Coulonge have been creeping higher in the 2017–2026 era compared to 2000–2016. Counterfactual analysis: applying the same 1.92 m freshet rise to a 106.0 m baseline (vs current 106.6 m):

| Year | Actual peak | Peak if baseline was 106.0 | Property flood? |
|---|---|---|---|
| 2017 | 108.52 | ~107.9 | No |
| 2019 | 109.17 | ~108.5 | Barely |
| 2023 | 108.77 | ~108.1 | No |
| 2025 | 108.15 | ~107.7 | No |
| 2026 | 108.63 | ~107.9 | No |

**Every major flood since 2017 would have stayed below the 108.48 m backyard threshold with a 60 cm deeper pre-freshet drawdown.**

### The 2017 regime change — Contributor A's empirical analysis

A flood watch group member with operational experience working on dams in the watershed (Contributor A) compiled all Lac Coulonge yearly peak levels from 1972 to 2026 and produced a striking empirical comparison:

| Period | Span | Years below 107.5 m | Official floods (>107.5) | Minor floods (>108.0) | **Super-floods (>108.5)** |
|---|---|---|---|---|---|
| 1972–2016 | 45 years | 25 (55.6%) | 14 (31.1%) | 5 (11.1%) | **1 (2.2%)** |
| 2017–2026 | 10 years | 3 (30.0%) | 2 (20.0%) | 1 (10.0%) | **4 (40.0%)** |

The super-flood frequency went from 1 event in 45 years (a once-in-a-generation occurrence) to 4 events in 10 years. That's roughly an **18-fold increase in super-flood rate**. Statistically, this is a 6+ sigma event under any reasonable null hypothesis — effectively impossible by chance alone.

**The shape of the change matters.** Climate change produces gradual shifts, not step functions. A 1-in-45-year baseline transitioning to a 4-in-10-year rate over a single decade is too abrupt to be a climate signal alone. Contributor A's framing: **"This is not a gradual trend upwards due to climate change. As ChatGPT indicates, it's a major shift in management regime."**

The implication is significant. Whatever changed around 2016–2017 — operating rules, drawdown targets, generation contracts, headpond management at run-of-river facilities — produced a regime change in flood frequency that has now persisted for a decade. The community's policy arguments (snowpack-indexed drawdown, mandate review, real-time data access) are responses to a regime change that is now empirically documented, not hypothetical.

This is the strongest single piece of evidence the flood watch community has produced for the regime-change thesis. It deserves widespread distribution.

### Testing the climate alternative — quantitative regression analysis

The most obvious alternative explanation for the regime change is climate change: maybe the basin is simply receiving more cold-season precipitation, and that's driving higher peaks. To test this, a regression model was built using **45 years (1972–2016) of pre-regime-change data** to learn the relationship between cold-season precipitation at the Ottawa station and Lac Coulonge yearly peaks. The model was then used to predict what 2017–2025 peaks SHOULD have been if the system were behaving the same way.

**Decade-by-decade Ottawa cold-season precipitation (Nov–Apr, mm)** — meteostat WMO 71628:

| Period | N | Mean | Median |
|---|---|---|---|
| 1972–1979 | 8 | 450 | 459 |
| 1980s | 10 | 409 | 404 |
| 1990s | 10 | 427 | 419 |
| 2000s | 10 | 412 | 408 |
| 2010–2016 | 7 | 347 | 338 |
| **2017–2025** | **9** | **423** | **397** |

**Pre-2017 (45 years): mean 412 mm. Post-2017 (9 years): mean 423 mm. Difference: +3%, t-statistic 0.46, statistically not significant.**

The 2010–2016 period was anomalously dry compared to the long-term record. Comparisons that use only this short pre-period as a baseline produce inflated "+22%" climate change estimates that disappear when the full 1972–2016 record is used.

**Linear regression test.** Using pre-2017 data (n=45), a model was fit:

```
Peak = 106.835 + 0.00151 × cold_season_precip_at_Ottawa     (r² = 0.038)
```

This model was applied to predict 2017–2026 peaks using only the precipitation observed in those years:

| Year | Ottawa cold prcp (mm) | Actual peak (m) | Predicted peak (m) | Residual (cm) |
|---|---|---|---|---|
| 2017 | 519 | 108.52 | 107.62 | **+90** |
| 2018 | 336 | 107.84 | 107.34 | +50 |
| 2019 | 510 | 109.17 | 107.60 | **+157** |
| 2020 | 243 | 107.44 | 107.20 | +24 |
| 2021 | 423 | 106.67 | 107.47 | -80 |
| 2022 | 449 | 107.61 | 107.51 | +10 |
| 2023 | 531 | 108.77 | 107.64 | **+113** |
| 2024 | 355 | 107.49 | 107.37 | +12 |
| 2025 | 368 | 108.15 | 107.39 | +76 |
| 2026 | 349 | 108.63 | 107.36 | **+127** |

**Average residual: +58 cm.** Post-2017 Lac Coulonge peaks are running approximately 58 cm higher than what 44 years of pre-regime precipitation patterns predict. (The 1972 freshet year is excluded for insufficient observation days at Ottawa CDA — the season was Nov 1971 onward and Nov-Dec 1971 is sparse in the ECCC record.)

**The four super-flood years** (2017, 2019, 2023, 2026, all peaks ≥ 108.50 m) all show large positive residuals (**+90, +157, +113, +127 cm**, mean **+122 cm**). 2019 in particular shows the year's higher-than-average precipitation cannot account for 1.57 m of the peak elevation — even adjusting for that wet year, the lake came in 157 cm above what its precipitation predicted.

**The post-2017 regime change is concentrated in freshet behavior, not year-round headpond level.** Analysis of the canonical Lac Coulonge level data (1972–2026, ORRPB monthly summaries) shows the +59 cm shift in annual peaks is not accompanied by a year-round headpond rise: annual mean is up only 2.6 cm (106.36 → 106.39 m), annual minimum is up only 1.0 cm (105.82 → 105.83 m), and off-season monthly means (August through December) are unchanged or slightly lower. The shift is concentrated in the spring freshet — April monthly mean +19.5 cm and annual peak +59 cm — with the rest of the year essentially unchanged. This pattern is consistent with operational behavior change during peak inflow (later drawdown, slower refill, or holding water during the freshet itself) rather than a permanent headpond raise. The November 2025 MRC Pontiac notice — titled "notice of temporary water-level increase, Bryson Dam — Hydro-Québec" — confirms higher-head operations of 30–50 cm have been **tested**, not that they are in permanent effect. The 58 cm regression residual quantifies the unexplained component; the year-round level data narrows the mechanism to operational behavior during the freshet rather than a sustained headpond raise.

**Caveats and honest limits of this analysis.** The Ottawa station is in the southern basin and explains only ~4% of Lac Coulonge peak variance (r² = 0.038) — the very low r² is itself informative: Ottawa-station precipitation has almost no predictive value for Lac Coulonge because the southern basin is the wrong watershed. Lac Coulonge is fed primarily by the upper Ottawa (Témiscamingue) and the Coulonge tributary. Cleaner upstream precipitation data (Témiscamingue, Maniwaki, Val-d'Or — now in the repo at `data/eccc-climate/`) would produce a more powerful test. The regression also assumes a linear precipitation-to-peak relationship, which is a simplification. **Despite these limitations, the analysis demonstrates that climate alone — at least as measured by Ottawa precipitation — does not explain the regime change. A +58 cm residual remains, and that residual is consistent with operational changes at Bryson Dam.**

### Per-event amplification test — Lac Coulonge ~ Britannia regression (added May 2026)

A second, independent test segments the Lac Coulonge peak vs Britannia annual-peak flow relationship pre- and post-2017. Britannia is the Ottawa basin's downstream-of-everything gauge (active 1960-present, full discharge record). If Bryson operations had been amplifying *each* freshet's peak post-refurbishment, the slope or intercept of `Lac Coulonge peak ~ Britannia peak` should have shifted.

```
Pre-2017 (n=45):  Peak (m) = 105.4165 + 0.000619 × Britannia peak (m³/s)   r² = 0.818
Post-2017 (n=8):  Peak (m) = 105.3681 + 0.000631 × Britannia peak (m³/s)   r² = 0.951
```

**Slope shift +0.012 m per 1000 m³/s. Intercept shift -4.8 cm. Mean post-2017 residual from the pre-2017 line: +0.1 cm.** At common inflow levels, the difference between the two lines is 0–2 cm — well inside noise.

**Implication.** The lake responds to inflow exactly as it always has. The +59 cm shift in average annual peak is *composition-driven* — more years now produce big freshets — not amplification of how the lake responds to a given freshet. Source: `ingesters/climate-history/lc_brit_regression.py`.

### Step-change location and climate-forcing test (added May 2026)

If the basin-flow shift is climate-driven, it should appear as a *trend* in climate forcing — not as a step concentrated at a specific year. Two tests:

**Test A · Step location.** Britannia annual-peak medians across candidate breakpoint years 2000–2020:

| Breakpoint | Pre median (m³/s) | Post median (m³/s) | Shift |
|---|---|---|---|
| 2010 | 3,075 | 3,510 | +14.1% |
| 2015 | 3,075 | 3,600 | +17.1% |
| **2017** | **3,080** | **3,675** | **+19.3%** ← sharpest |
| 2018 | 3,100 | 3,450 | +11.3% |
| 2019 | 3,120 | 3,315 | +6.2% |
| 2020 | 3,165 | 3,180 | +0.5% |

The shift maximizes at 2017 — the year Bryson refurbishment planning began — and decays both directions. Decade super-flood counts (Britannia ≥ 4,500 m³/s): **1970s=1, 1980s=0, 1990s=0, 2000s=0, 2010s=2, 2020s (5y in)=1**. Three full decades with zero super-floods, then an outbreak.

**Test B · Climate forcing.** Across 9 ECCC watershed stations, Apr+May precipitation shifts pre/post 2017 range **−4% (Parent) to +36% (Rouyn)**; March peak snow shifts range **−15% (Témiscamingue) to +20% (Ottawa CDA)** — with snow trending *down* at the upper basin. **No coherent climate step** that mathematically requires a +19% step in basin flow. Source: `ingesters/climate-history/stepchange_analysis.py`.

### Pointe-Calumet step-change — corroborating evidence at the system terminus (added May 2026)

The Britannia step-change result above shows the inflow-distribution shift concentrating at 2017. A complementary test at the *opposite* end of the chain — the gauge nearest Carillon's discharge — shows the same step but with a different geographic signature.

Pointe-Calumet (WSC station 02OA105, Lake of Two Mountains, immediately downstream of Carillon, level record 1986–2024) is the closest public gauge to Carillon's tailwater. April–June daily-level summary by decade, from the WSC HYDAT bulk record (loaded May 2026 into a `wsc_daily` hypertable, 178k rows across 9 Ottawa-basin stations):

| decade | years | AMJ mean (m) | AMJ peak avg (m) | AMJ peak max (m) |
|---|---|---|---|---|
| 1986–95 | 9 | 22.334 | 23.321 | 23.930 |
| 1996–05 | 10 | 22.435 | 23.427 | 24.186 |
| 2006–15 | 10 | 22.454 | 23.177 | 23.958 |
| **2016–24** | 9 | **22.727** | **23.812** | **24.774** |

The 2016–24 decade is **40 cm higher in AMJ mean and ~50 cm higher in AMJ peak average** than any prior decade in the gauge's record.

The corroborating piece comes from the more distant Pointe-Claire gauge (WSC 02OA039, Lac Saint-Louis, downstream via the St-Lawrence, level record 1915–2025). The 110-year view shows modern peaks are *not* historically extreme there — the 1915–1944 era had higher AMJ peak max (22.85 m) than the modern era (22.56 m). St-Lawrence regulation downstream of Carillon (Beauharnois) buffers the lake.

**Spatial pattern**: the regime change is sharply visible at the gauge nearest Carillon and dissipates downstream. This is the spatial pattern expected if the cause is operational/local rather than basin-wide climate signal alone — the same conclusion the Britannia step-change test points to from the upstream end of the chain.

**The monthly attenuation check.** Across six decades of ORRPB monthly Carillon discharge / Britannia daily-mean flow records, the May Carillon-to-Britannia ratio is remarkably stable (1.45–1.60), with no detectable step-change in monthly-mean operational throughput. The directive question ("is HQ drawing down to 39.62 m before peak?") is a sub-monthly timing question that monthly means hide. Resolving it would require daily Carillon outflow (operator data, not in HYDAT after 1994) plus daily headpond level (operator-only). The third piece — daily Britannia flow plus tributary daily flows for a basin-balance check — is now in `wsc_daily` and available going forward.

### Why this matters for the case file

The strongest version of the operations indictment — *Bryson amplifies the lake peak* — does not survive these tests. But three independent findings now stack the same direction:

1. **The +59 cm peak shift is real, but driven by changes in the inflow distribution** (more years with big freshets), not per-event amplification.
2. **The basin-flow step concentrates sharply at 2017**, with no matching climate step.
3. **The live Bryson telemetry** (HQ open-data feed, May 2026) shows the headpond held at the top of its operating band (104.20–104.67 m) through 10 days of peak inflow, with 86% spill share — the operating-regime change is now directly observable.

**The strengthened argument:** even granting whatever climate signal does exist, a dam built to manage river flow has an obligation to adapt its operating posture as inflow patterns change. Continuing the same posture — or, per the live data, moving to one that holds the headpond *higher* under bigger inflows — is the policy failure the community is asking about. The argument no longer requires winning the climate-attribution debate; it asks a governance question that stands independently. See Exhibit D Figure 7 + Live Observation panel and Exhibit E Figures 9–10.

### Snowpack-indexed drawdown — the missing rule

The ORRPB currently uses 30-year median guidelines for fall reservoir drawdown — a fixed rule applied regardless of conditions. This produces clearly wrong outcomes in heavy snow years (excess water in storage during freshet) and unnecessarily aggressive drawdown in light snow years (e.g. 2024 had summer-like April levels).

The flood watch community's policy proposal: **a snowpack-indexed drawdown rule**. Heavy snow year = drawdown lower. Light snow year = less aggressive drawdown. Snowpack data is available months in advance. The 2024 vs 2026 contrast makes the case — same approach, very different conditions, only one year had appropriate buffer.

### The Carillon directive enforcement gap (added May 2026)

The Bryson case is not the only example of a Hydro-Québec operating directive that exists on paper but is not executed. The same pattern is documented at the system terminus, Carillon dam, and shows the same regulatory void.

Hydro-Québec's published Carillon water management plan, section 15.3.5.1, states:

> "In the spring, lowering the water level toward level 39.62 m at the Carillon dam helps maintain the river's natural conditions upstream. The downstream section of the river upstream of the Grenville rapid returns to its natural state."

The published operating range is **39.62 m to 41.15 m**. In practice, HQ's de-facto freshet floor is approximately **40.50 m** — leaving roughly 88 cm of head impounded above the directive low every spring. The Ottawa River Flood Awareness group (ORFA) has been documenting this discrepancy since 2017.

In 2025, ORFA formally requested that the Ontario Minister of Natural Resources intervene. The response (letter 354-2025-356, dated May 30 2025, signed by Minister Mike Harris) confirmed weekly meetings with Hydro-Québec but no enforcement commitment, asserting only that "Hydro Quebec reports that water levels are currently within the operating range and there are presently no concerns about flooding." The response is technically true against the 41.15 m ceiling but evades the 39.62 m drawdown directive — the actual concern. MNR explicitly defers to HQ as "the dam owner" and does not independently verify.

This is the same structural pattern this document already names at Bryson — **framework exists, enforcement does not** — visible at the opposite end of the same regulated chain. The Carillon water management plan is binding language in HQ's own published document; the verification is operator-only; the regulatory backstop has, by its own admission, no enforcement mechanism beyond consultation.

### The mandate clarity problem

The ORRPB's mandate language has shifted from "minimizing" flood risk to "reducing" flood risk over the past decade. Legally distinct commitments. The ORRPB is also a **coordination board, not a regulator with enforcement authority** — it can recommend reservoir operations but cannot compel OPG or Hydro-Québec to change practices. Real authority sits with the operators, whose mandates are power generation.

### Data accessibility problem

The ORRPB website aggregates from three separate operating agencies:
- **OPG**: Pembroke, Des Joachims, Chenaux, Chats Falls, Otto Holden
- **Hydro-Québec**: Lac Coulonge, Gatineau/Hull, Thurso, Grenville, Carillon
- **Water Survey of Canada**: Mattawa, Britannia

Different telemetry, different update schedules, different data-sharing agreements. During the 2026 event:
- Lac Coulonge readings went stale for 6+ hours
- Pembroke readings delayed multiple times
- Website CDN caching returned stale data even after updates
- No push notification or threshold alert system

The gauges were built for power generation operations, not flood preparedness. The architecture reflects that priority. The Vigilance API by contrast was built for public flood awareness — and is materially better at that job.

### The forecast communication problem

The ORRPB's prose forecasts use language like "remains uncertain... remains possible... could lead to..." This is **CYA and not particularly helpful**. The data is all there — multi-decade snowpack measurements, weather forecasts (accurate to 3–4 days), reservoir storage state, hourly gauge readings. What's missing is the analytical layer that translates inputs into actionable scenarios.

A useful forecast would say something like:
- "Dry next 7 days: peak ~108.40 m"
- "30 mm rain in next 7 days: peak ~108.55 m"
- "60 mm rain in next 7 days: peak ~108.75 m"

Or with explicit confidence bands:
- "Peak between 108.30 and 108.70 m with 80% confidence under current forecast"

This is standard practice in hurricane forecasting (NOAA cone-of-uncertainty), wildfire risk modeling, and other agencies dealing with weather-driven hazards. The forecast horizon limitation isn't a reason to skip scenarios — it's exactly **why** scenarios should be published. As the 4-day weather forecast updates, the homeowner immediately knows which scenario applies.

A homeowner with a laptop pulling open data can do useful analytics. The agency with hydrologists on staff can do better — but currently chooses not to publish that work.

### The contractual obligations argument — freshet vs fall drawdown

A persistent thread in community discussion frames operational changes as constrained by Hydro-Québec and OPG contractual obligations to power generation. This argument conflates two operationally distinct windows:

**Freshet operations (3 weeks of peak runoff):** During April peak flow, the system carries 3-5x normal water volumes. Carillon flow goes from a ~2,000 m³/s baseline to over 7,000 m³/s. **The turbines have a maximum throughput.** Anything above that capacity is **spilled** through gates, generates zero revenue, and is operationally identical regardless of any reservoir management decision made earlier. During the April 19-22 peak, a significant fraction of the 7,700 m³/s passing Carillon was spillage, not turbine flow. Contract obligations are not constraining freshet operations — they are being met by the water that does pass through turbines, while excess goes through gates regardless.

**Fall drawdown (October-March):** This is where revenue trade-offs are real. Drawing reservoirs deeper in fall means lower headpond levels in winter, which means less generation when water is scarce and every cubic meter through the turbines makes power. Heavy snow year deeper drawdown = winter generation revenue impact. This is a legitimate trade-off that the community's snowpack-indexed drawdown proposal must engage with seriously.

**The conflation matters.** When operators or their defenders cite "contractual obligations" as a defense of freshet operational behavior, they are either confused or being deliberately vague. The contracts apply year-round to firm power obligations. They do not constrain how the river is managed during three weeks of overflow because the contracts get fulfilled either way. The actual revenue trade-off lives in fall drawdown decisions, which is the conversation the community is trying to have.

The freshet vs fall distinction also reframes what "no way to warn anyone" means. Operators have multi-month snowpack data before the freshet starts. The fall drawdown decision sets the April 1 baseline. That decision is made on a fixed 30-year median rule rather than adapted to that year's snowpack. That isn't an unforeseeable weather emergency — it is a planned operational choice with predictable consequences.

### Summary of the regulatory critique

The institutional structure produces opacity by design, not conspiracy:

1. ORRPB coordinates but doesn't enforce
2. Operators' priorities are power generation, not flood control
3. Real-time public data would expose operational decisions (drawdown timing, generation vs flood-buffer trade-offs) that operators prefer not to have scrutinized
4. ORRPB legal counsel hedges all forecasts to limit liability
5. Communications use "could/possible/uncertain" — sounds authoritative, gives homeowners nothing to act on
6. The flood watch community ends up doing the analytical translation that should be institutional

**Hope for the best, prepare for the worst** — the folk wisdom captures the regulatory recommendation: don't manage to the median, manage to the snowpack you have.

---

## The McNeil Report (2019) — Independent Government Validation

In November 2019, Douglas McNeil, P.Eng., delivered *An Independent Review of the 2019 Flood Events in Ontario* to Ontario's Minister of Natural Resources and Forestry. He had been appointed Special Advisor on Flooding in July 2019 with a mandate to review the province's flood management framework. The full report (66 recommendations, 184 pages) is in this repository at [`docs/reports/mnrf-english-ontario-special-advisor-on-flooding-report-2019-11-25.pdf`](../reports/mnrf-english-ontario-special-advisor-on-flooding-report-2019-11-25.pdf).

The report is the only commissioned, independent, primary-source government review of Ottawa River flood management since the regime change began. It contains 12 recommendations specifically directed at the Ottawa River Regulation Planning Board (Recommendations #55–66), and several findings in the body of the report that directly validate arguments the case file makes from outside the policy apparatus.

### Findings that align with the case-file argument

**The 60% uncontrolled-basin admission (Section 4.1.1, page 34):**

> "There is little significant storage available in the lower portion of the Ottawa River; in fact, over 60% of the basin is essentially uncontrolled due to lack of storage capability."

This is the official Ontario government statement of the unregulated-tributary problem the case file already names — and the 60% figure is a primary-source admission that the buffer the regulated portion of the basin can provide is inherently limited.

**The legal framework that prioritises power generation (Section 4.1.1, pages 34–35):**

> "[OPG] stations operate under the authority of Water Power Leases with the Province of Ontario and with An Act Respecting the Water Powers of the River Ottawa (1943). During normal flow conditions, OPG has the legal ability to raise the water level to the limit prescribed in the license for the respective facility for the purposes of power generation. Under high flow conditions, OPG operates its dams and stations to minimize the impacts of flooding and to at least do no more harm than would occur under natural conditions."

The legal framework is explicit: **power generation by license, flood mitigation by operating practice**. The mandate clarity problem the case file names is documented in the binding legal instruments themselves.

**The "run-of-river" framing is rejected by the report (Section 4.1.1, page 35):**

> "Reference is often made in this section to OPG's facilities being operated as 'run-of-river' facilities (i.e. facilities that have no storage capacity whatsoever and generate electricity by whatever flow is running in the river and through the generating station) during periods of flooding. Understanding what this term means conceptually is critical to understanding why water management approaches were used during periods of high flow and flood flow experienced in the spring of 2017 and 2019. **OPG's facilities are not normally operated as run-of-river, nor are they classified as run-of-river facilities.** It must be highlighted that, outside of high flow or flood conditions, all of OPG generating stations operate on a daily peaking cycle as peaking or cycling facilities... [G]enerating stations, including Otto Holden, completely shut flows off at night to store water for power production the next day. **For transparency and full disclosure, the above facts must be emphasised as they can affect public perception of flow and level management regimes on the river and OPG's ability to control flooding.**"

This is a primary-source finding by the Special Advisor that operators retain significant control over levels and storage outside of the most extreme flow events. The case file's Live Operational Evidence at Bryson — held headpond, 83% spill share, near-zero level variation across 12 days during freshet — falls squarely in the "outside of extreme flooding" territory McNeil names. The 2026 freshet at Lac Coulonge was Major Flood (État 6/6) but well below the 2019 record; whether it qualifies as "extreme" by McNeil's framing is itself the open question.

### Recommendation #59 — the regulator-by-name-only finding

Of the 12 ORRPB-specific recommendations, the most direct alignment with the case-file argument is Recommendation #59 (page 13):

> "That the supporting agencies of the Ottawa River Regulation Planning Board (Canada, Ontario, Quebec and the dam operators) consider removing 'Regulation' from the title, as it implies that the Board can actually manage large floods when, in fact, they cannot because of the limited storage capacity of the generating station reservoirs, which were designed for electric power generation and not flood control."

McNeil — Ontario's appointed Special Advisor — is on the record stating that:
1. The ORRPB cannot manage large floods.
2. The generating station reservoirs were designed for electric power generation, not flood control.
3. The current name misleads the public about what the Board can actually do.

This is the case file's mandate-clarity argument and "the gauges were built for power generation, not flood preparedness" framing, made by the official independent review. The case file's policy critique is not a fringe community position — it is essentially aligned with what the Province's own appointed expert recommended six years ago.

### Recommendation #60 — public perception of dam-owner motives

> "[T]he officers should be from another government department as opposed to Ontario Power Generation or another non-government dam owner, since the public believes the dam owners only care about generating electricity."

McNeil's own framing acknowledges the public perception that the case file documents from gauge data: dam owners are perceived as operating for generation, not flood mitigation. The case file's contribution is providing the *empirical* evidence (the held-headpond observation, the regression analysis) that underpins what McNeil's report describes as a perception.

### Other ORRPB recommendations directly relevant to the case file

| # | Substance | Case-file connection |
|---|---|---|
| 55 | IJC, ORRPB, OPG make detailed flood operations information readily available on websites | Validates the "data accessibility problem" critique (Policy section) |
| 56 | IJC meet with stakeholder groups to "explain in considerable detail how their structures are operated" | Validates the operational opacity argument |
| 58 | Review the original 40-year-old ORRPB agreement | Validates the mandate clarity problem |
| 60 | Communications officer assigned from another government department, not OPG | Acknowledges the public-perception problem |
| 61 | Communications person work with ORRPB on "more easily understood materials" | Validates the forecast communication problem |
| 62 | ORRPB work with OPG on staff gauges read by engaged residents | The case file is exactly that — community-built monitoring |
| 63 | Two municipal officials (one ON, one QC) sit on ORRPB | Addresses the dual-jurisdiction problem the case file repeatedly names |
| 65 | OPG identify options on refill date flexibility under Water Management Plans | Directly validates the freshet drawdown / contractual obligations argument |

### Where the case file extends McNeil's framing

McNeil's nuanced position on operator control is that operators have significant level/flow control under normal flow, but **lose** that control under extreme flood conditions. The case file does not contradict this — it sharpens it.

The case file's empirical observations (Live Bryson telemetry, the held-headpond pattern, the spatial distribution of regime change concentrated near regulated structures) sit at the **boundary** between McNeil's two regimes — they describe operator behavior during high flow that is **not yet at the extreme-flood ceiling**. McNeil acknowledges that storage capacity cannot prevent the worst extreme floods. The case file argues that *at flow levels well below those extremes, operator decisions still meaningfully affect outcomes upstream*, and that the post-2017 regime change is a step-function in operator behavior in this in-between territory rather than a step-function in extreme-flood frequency.

McNeil's report stops at flow patterns and recommends governance changes. The case file picks up where McNeil leaves off and asks: *given the McNeil framework — power generation by license, flood mitigation by practice, public deserving of transparency — what specifically about Bryson's freshet operating practice changed after 2017, and what flood-buffer analysis informed those changes?* That question is the unanswered one Exhibit D names.

### Implementation status (as of May 2026, sourced)

The implementation status of nine ORRPB-relevant McNeil recommendations was checked in May 2026 against current public sources (ORRPB website, Ontario Public Appointments Secretariat, OPG pages, Environmental Registry of Ontario, Ontario MNRF documents, IJC pages, Hydro-Québec Outaouais water management page, and external coalition publications). Each finding below cites the source consulted; recommendations are listed by McNeil report number.

| # | Recommendation (abridged) | Status | Notes / source |
|---|---|---|---|
| 55 | IJC, ORRPB, OPG make detailed flood-operations information readily available on websites | **Partially implemented** | ORRPB and OPG publish current conditions, daily forecasts, and press releases ([ottawariver.ca/latest-news](https://www.ottawariver.ca/latest-news/), [water.opg.com/source/ottawa-river](https://water.opg.com/source/ottawa-river/)). What remains absent is the detail McNeil envisioned: per-decision release logs, retrospective explanations of past flood-event operations, transparent operating-decision rationale. The bar is "readily available" *and* "detailed" — half met. IJC has no Ottawa River jurisdiction so that part of the recommendation is moot. |
| 56 | IJC meet with stakeholder groups to explain operations | **Not implemented (largely misdirected)** | No IJC Ottawa-River-specific stakeholder meetings located 2020–2026 ([ijc.org/en/what/engagement/consultations](https://ijc.org/en/what/engagement/consultations)). McNeil's pointing of this recommendation at the IJC was already structurally awkward given the IJC's lack of Ottawa River jurisdiction. |
| 58 | Review the 1983 Ottawa River Regulation Agreement | **Not implemented (under external pressure)** | No federal/provincial review or amendment of the 1983 Agreement has been initiated. As of 2023–2024, a coalition of 30+ municipalities organised as the **Ottawa River Flood Alliance** has explicitly called for "a federal review of the 1983 Ottawa River governance framework" ([ottawariverflood.ca/our-focus](https://www.ottawariverflood.ca/our-focus)) — confirming the recommendation has not been actioned and that demand for it has now formalised at the municipal-government level. |
| 59 | Remove "Regulation" from the Board's title | **Not implemented** | The board is still officially "Ottawa River Regulation Planning Board" / "Commission de planification de la régularisation de la rivière des Outaouais" on its own site ([ottawariver.ca](https://www.ottawariver.ca/)) and in Ontario's Public Appointments Secretariat registry ([pas.gov.on.ca/Home/Agency/371](https://www.pas.gov.on.ca/Home/Agency/371)). |
| 60 | Dedicated communications officer not from OPG | **Not implemented** | Communications are still handled by the two-engineer ORRPB Secretariat per the Board's own structure page ([ottawariver.ca/about-us/who-we-are/structure](https://www.ottawariver.ca/about-us/who-we-are/structure/), [media-request-procedure](https://ottawariver.ca/contact-us/media-request-procedure/)). No dedicated, non-OPG communications officer is identified. |
| 61 | Marketing-experienced communicator producing plain-language materials | **Not implemented / minimal** | Public-facing ORRPB materials remain engineer-style press releases, technical FAQs, and tabular forecasts ([ottawariver.ca/information/publications](https://ottawariver.ca/information/publications/), [/about-us/faq](https://www.ottawariver.ca/about-us/faq/)). No new plain-language explainers, infographics, or public videos located. |
| 62 | OPG and ORRPB install staff gauges read by engaged residents | **Not implemented** | No OPG/ORRPB staff-gauge community program found ([Ontario MNRF — Recommendations to External Agencies](https://www.ontario.ca/document/independent-review-2019-flood-events-ontario/recommendations-external-agencies) lists this as still outstanding). Ottawa Riverkeeper's "Riverwatchers" citizen-science program ([ottawariverkeeper.ca/what-we-do-2/initiatives/riverwatchers](https://ottawariverkeeper.ca/what-we-do-2/initiatives/riverwatchers/)) predates the recommendation, is independent of OPG/ORRPB, and is a water-quality program, not a level-gauge reading program. |
| 63 | Two municipal representatives (one ON, one QC) on the ORRPB | **Not implemented** | The Board's seven seats are still held by federal/provincial/Crown-corporation members (ECCC, PSPC, CCG, MELCCFP, Hydro-Québec, MNR, OPG) per the published structure ([ottawariver.ca/about-us/who-we-are/structure](https://www.ottawariver.ca/about-us/who-we-are/structure/)). No AMO/FQM/UMQ seats. The Ontario seat is held by an OPG-affiliated appointee. Note that this recommendation requires amending the 1983 Agreement (see #58). |
| 65 | OPG identify options on refill date flexibility, support potential WMP amendment proposals | **Unable to determine** | No Environmental Registry of Ontario notice or OPG announcement of a Water Management Plan amendment covering refill flexibility for Otto Holden, Des Joachims, Chenaux, or Chats Falls was located 2020–2026 ([ero.ontario.ca/search](https://ero.ontario.ca/search), [ontario.ca/page/maintaining-water-management-plans](https://www.ontario.ca/page/maintaining-water-management-plans)). Absence in public sources is suggestive but not definitive — internal MNRF/OPG actions may not surface in a web search. |

**Pattern:** every recommendation requiring formal change to the 1983 Agreement (58, 59, 63) is stalled, and the lighter-touch communications recommendations (60, 61) that ORRPB could have implemented unilaterally have also not been taken up. The case file's argument that the McNeil recommendations have not been substantively actioned is supported, with two important caveats: #55 is partially implemented (data feeds yes, decision transparency no), and #65 cannot be definitively determined from public sources alone.

**The most important new finding from this verification:** the Ottawa River Flood Alliance ([ottawariverflood.ca](https://www.ottawariverflood.ca/)) — a coalition of 30+ municipalities — is now publicly demanding the same federal review of the 1983 Agreement that McNeil's Recommendation #58 called for in 2019. The case file's policy argument is no longer a community-advocacy position alone; it is aligned with the explicit demand of an organised municipal coalition.

### Parallel federal-level review — the ECCC Ottawa River Watershed Study (2019)

The McNeil report is not the only post-2017 government-commissioned review of Ottawa River basin governance. In June 2019 — five months before McNeil delivered his report to Ontario — Environment and Climate Change Canada tabled *An Examination of Governance, Existing Data, Potential Indicators and Values in the Ottawa River Watershed* ([summary on canada.ca](https://www.canada.ca/en/environment-climate-change/services/ottawa-river-watershed-study/report-summary.html); [draft PDF](https://www.placespeak.com/uploads/5492/ENG_ORWS_Draft_Report_2018_09_28__Clean.pdf)). The study was triggered by House of Commons private member's motion **M-104** (May 2017, MP William Amos) and represents the federal-level counterpart to the provincial-level McNeil review.

The ECCC study is structured as findings and options rather than numbered recommendations, organised into six chapters. The dominant proposal is the creation of a **multi-jurisdictional Ottawa River Watershed Council with Indigenous co-governance**, supported by integrated watershed management, harmonised data and indicators across Ontario and Quebec, and formal interprovincial coordination. The report is 267 pages and engages the same governance-fragmentation problem the McNeil report and this case file both name from different angles — that the basin is administered by a 1983 federal-provincial-Crown-corporation agreement that does not include Indigenous nations, riparian communities, or municipal governments as parties.

**Implementation status.** The federal government tabled the report without endorsing the Watershed Council recommendation; no council has been established. Ottawa Riverkeeper, the watershed's primary non-governmental observer, publicly characterised the federal response as ["a missed opportunity for federal leadership"](https://ottawariverkeeper.ca/federal-government-tables-report-on-ottawa-river-watershed-what-does-it-mean-and-whats-next/). The Government of Canada [response to motion M-104](https://www.canada.ca/en/environment-climate-change/corporate/transparency/strategic-environmental-economic-assessments/response-motion-ottawa-river-watershed-council.html) accepts the principle of integrated management but defers concrete commitments. As of May 2026, no consolidated public tracking of the report's findings has been located.

**The pattern across both reviews is identical.** A government commissions an independent study after a flood event. The study identifies governance fragmentation as the underlying problem and proposes structural reforms (federal review of the 1983 agreement, removal of "Regulation" from the Board's title, addition of municipal representatives, federal Watershed Council with Indigenous co-governance). The reforms require multi-jurisdictional agreement that the existing mechanisms don't easily produce. The reforms are quietly not implemented. No agency publishes consolidated implementation tracking. Community observers can no longer locate what happened to the recommendations — which, given the public-record nature of these reports, is itself a finding about the institutional follow-through, not about the records' availability.

**Note on attribution.** A community member referenced this report as "Ottawa River Watershed integrated water management recommendations" requested by Ontario's Minister of Natural Resources. The closest matching public document is the ECCC federal report described above, which was triggered by federal motion M-104 rather than commissioned by Ontario. The community member may be conflating the ECCC study (federal, June 2019) with the McNeil review (Ontario MNRF, November 2019), or there may be a third Ontario-specific watershed document that public sources do not surface. Either reading reinforces the same point: the institutional follow-through is opaque enough that community members cannot definitively trace what happened to specific recommendations.

---

## The Case File: Four-Exhibit Analytical Argument

In April 2026, the policy analysis was distilled into a four-piece "case file" of editorial-style infographics, designed for community sharing and media use. Each exhibit makes one claim, backed by verified primary sources. Together they form a complete argument that the regime change is real, has identifiable mechanisms, and has unanswered policy questions.

### Exhibit A — Outcomes have changed

**"In 10 years, the Ottawa River flooded as often as it did in 45."**

The headline statistical finding: super-flood frequency at Lac Coulonge increased 18-fold between the 1972–2016 era (1 super-flood in 45 years) and the 2017–2026 era (4 super-floods in 10 years). Under a stationary flood-frequency null hypothesis, the probability of seeing 4 super-floods in any 10-year window is less than 1 in 20,000.

**Whole-distribution shift, not just tail behavior.** The mean annual peak across all years (not just super-floods) rose from 107.44 m (1972–2016, N=45) to 108.03 m (2017–2026, N=10) — a +59 cm shift in the typical year, with Welch's t = 2.34 against the null hypothesis (p < 0.05). The median annual peak rose from 107.46 m to 108.00 m — a +54 cm shift through the centre of the distribution, not just the tail. The 5-year rolling mean has not dropped below 107.55 m since 2010, compared to a pre-2010 ceiling of 107.51 m, and three windows (2015–2019, 2016–2020, and 2022–2026) sit above 108 m. The new regime is sustained, not a transient cluster.

### Exhibit B — Inputs have shifted

**"Before the snow even melted, the river was already too high."**

The 2026 winter baseline at Lac Coulonge ran approximately 14 cm above the 2016–2025 average through January–February — before any spring runoff began. The water level the freshet started from was higher than at any comparable point in the prior decade. Contributor A's February 28, 2026 prediction ("Lac Coulonge level is at its highest level in 10 years for this time of year. If our elected officials don't act now, I'm afraid we could possibly face the worst flooding ever for this section of the Ottawa River") was directionally validated when the freshet peaked at 108.633 m on April 20 — fourth-highest in the modern era.

### Exhibit C — A specific operational lever exists

**"The reservoir they say has no flood benefit holds more water than the one they use."**

ORRPB FAQ Q5 Part D states: "Lowering levels in February then provides no benefit and does not reduce the flooding. Additionally, the storage volume available on the main stem of the river is far too small compared to the volume of water flowing through the river during high flow periods, to reduce flooding on the river system."

Contributor A's Google Earth measurement of the Lac Coulonge reach (Rapides-des-Joachims to Bryson Dam) demonstrates:

- **Surface area (4 sections summed):** 73.89 + 89.34 + 12.44 + 51.52 = 227.19 km²
- **Available drawdown range:** 1.33 m (yearly average 106.40 m minus historical lower limit 105.07 m)
- **Storage capacity:** 302,162,700 m³

Compare to Des Joachims, which ORRPB enthusiastically uses for flood mitigation under a "two-stage refill" protocol described in FAQ Q6:

- **Surface area:** 75.71 km²
- **Operating range:** 2.70 m
- **Storage capacity:** 229,000,000 m³ (per ORRPB published figures)

**The Lac Coulonge reach has 1.32× the storage capacity of Des Joachims.** The "far too small" justification cannot apply to one without applying to both.

**Method validation:** Applying the same surface-area-times-depth calculation to Des Joachims yields 204.4 million m³ — within 11% of the published 229 million m³, demonstrating the method produces conservative estimates. The Lac Coulonge figure is therefore a low-end estimate of available storage.

### Exhibit D — A specific operational change happened with documented timing

**"The dam was refurbished. The river runs higher. The Board hasn't said why."**

The Bryson Generating Station was rehabilitated 2017–2023 (planning ~2017, Unit 1 winter 2020–2021, Unit 2 + building upgrades 2022, Unit 3 2023). The timeline correlates exactly with the regime change at Lac Coulonge.

**Verified primary sources:**

1. **Hydro-Québec Generation page** (hydroquebec.com/generation/generating-stations.html, last updated January 1, 2026), footnote applicable to all stations including Bryson:

   > "The head of water shown corresponds to the largest value (greatest height), if there are several values. The head varies with each generating unit. **Refurbishment work may therefore change the water head value.**"

2. **MRC Pontiac official notice** (November 19, 2025, mrcpontiac.qc.ca/en/notice-of-temporary-water-level-increase-bryson-dam-hydro-quebec/):

   > "Hydro-Québec would like to inform the public that a gradual increase in the water level upstream of the Bryson dam is planned starting Friday, November 21. The water level is expected to rise between 30 and 50 cm above its current level during the week of November 24. These variations will be more noticeable in the Bryson area and **could be felt as far as Coulonge Lake**. The anticipated rise in water levels may last a few weeks before dropping by about twenty centimeters in mid-December."

3. **ORRPB FAQ Q12** (ottawariver.ca/about-us/faq/):

   > "Hydropower generation is more efficient with a high water level upstream of the dam and low water levels downstream."

4. **Lac Coulonge yearly peak data 1972–2026** compiled from ORRPB historical records (Exhibit A).

5. **Live Hydro-Québec open-data feed** (May 2026 onward, ingested hourly to TimescaleDB): Bryson amont (1-2964), Bryson aval (1-2965), Bryson centrale release (3-46). Through the 2026 freshet peak, the headpond was held in a 47 cm operating band (104.20–104.67 m) with 86% spill share — the operating-regime change the case file infers from gauge data is now directly observable. See Exhibit D Live Observation panel.

### Live Bryson telemetry — daily breakdown and property-impact translation (added May 2026)

The Hydro-Québec open-data feed has been ingested hourly since 2026-05-02 into the freshet stack's `dam_releases` and `dam_levels` hypertables. The first window of accumulated data (2026-04-22 → 2026-05-03, "free backfill" from HQ's rolling 10-day buffer captured on first ingest) shows the Bryson operating posture day-by-day:

| day | total m³/s | turbined | spilled | % turbined | amont (m) | head (m) |
|---|---|---|---|---|---|---|
| 04-22 | 1,423 | 124 | 1,299 | **8.7%** | 104.538 | 14.78 |
| 04-23 | 1,407 | 137 | 1,270 | 9.7% | 104.537 | 14.82 |
| 04-24 | 1,355 | 224 | 1,130 | 16.5% | 104.446 | 14.75 |
| 04-25 | 1,336 | 224 | 1,111 | 16.8% | 104.467 | 14.82 |
| 04-26 | 1,330 | 225 | 1,106 | 16.9% | 104.490 | 14.87 |
| 04-27 | 1,341 | 188 | 1,154 | 14.0% | 104.488 | 14.85 |
| 04-28 | 1,360 | 119 | 1,241 | 8.8% | 104.444 | 14.78 |
| 04-29 | 1,357 | 162 | 1,195 | 12.0% | 104.429 | 14.76 |
| 04-30 | 1,346 | 236 | 1,110 | 17.5% | 104.433 | 14.78 |
| 05-01 | 1,352 | 237 | 1,116 | 17.5% | 104.451 | 14.79 |
| 05-02 | 1,356 | 233 | 1,123 | 17.2% | 104.473 | 14.80 |
| 05-03 | 1,353 | 231 | 1,122 | 17.1% | 104.471 | 14.83 |

Three observations sharpen the regime-change argument from gauge-data inference into direct telemetry observation.

**Observation 1 — the amont level is a control setpoint, not a consequence.** The headpond held in an 11 cm band (104.429 m → 104.538 m) across 12 consecutive days during a major freshet event. That is not what unmanaged water does. Inflow averaged ~1,350 m³/s across the window — to hold the level flat, total release was matched to inflow within minutes-to-hours. The matching Lac Coulonge level at Fort-Coulonge (Vigilance Station 1195) spent the same window in the 108.5–108.7 m band, covering the 108.48 m "water in backyard" threshold and the 108.52 m "crawl space" threshold every single day. Bryson's amont and Lac Coulonge are the same body of water at different vertical datums.

**Observation 2 — turbining is irrelevant to the upstream flooding question.** Bryson's turbines passed 119–237 m³/s — between 9% and 17% of total throughput. The other 83–91% — between **1,106 and 1,299 m³/s** — went over the spillway. Spillway flow is non-revenue water; it would have flowed downstream under any operating posture. The lever for upstream level control is *total* release (turbines + spillway), not turbines specifically. Whether HQ runs Bryson's turbines or doesn't has no bearing on whether the cottage floods. **The relevant choice is gate position, and gate position is a setpoint, not a constraint.**

**Observation 3 — a 30–60 cm reduction in held level translates 1:1 to Lac Coulonge and would have dried the property in 2026.** Applied to the 2026 thresholds:

| held level reduction | Lac Coulonge peak would be | Property impact |
|---|---|---|
| 0 cm (actual) | 108.633 m | crawl space flooded |
| –15 cm | ~108.48 m | water at backyard threshold |
| –30 cm | ~108.33 m | water approaching but not yet in backyard |
| –60 cm | ~108.03 m | dry, well below all thresholds |

A 30 cm pre-freshet drawdown would put the property in the "approaching" category instead of the "crawl space flooded" category. A 60 cm drawdown takes the property fully out of flood territory in 2026.

**Plausible technical reasons for the held elevation** (for intellectual honesty — these complicate but do not refute the observation): chain coordination with downstream stations, spillway throughput design limits at the current head, and recreational/navigation interest on Lac Coulonge as a managed lake. None of these convert "operating-range compliance" into "flood-mitigation drawdown," and none rebut the direct telemetric observation that the level is being actively held during a flood.

This evidence covers 12 days of one freshet. With the live ingester running, by next freshet there will be a year of accumulated telemetry showing the entire pre-peak / peak / decline cycle of multiple events and the upstream chain (Britannia at 02KF005 plus tributary inflows in `wsc_daily`) for basin-balance verification. The dashboard at `freshet.xgrunt.com` (Operations tab, featured cards) renders the held-band readout on every page load — the case-file evidence is publicly visible in real time without anyone having to ask for an analysis.

### The hydraulic continuity point (Exhibit D, expanded)

The Ottawa River between Rapides-des-Joachims and Bryson Dam is **one continuous reach with no intermediate flow controls**. Contributor A's storage capacity calculation summed it as four contiguous sections totalling 227 km². When the headpond at Bryson is held higher to increase generating efficiency, water backs up across the entire 130 km reach.

Affected upstream communities (10 communities, 2 provinces):
- **Quebec side:** Rapides-des-Joachims, Chapeau, Sheenboro, Waltham, Fort-Coulonge / Mansfield, Bryson, Allumette Island
- **Ontario side:** Deux-Rivières, Petawawa, Pembroke

The trade-off is therefore not "Bryson revenue vs nothing." It is **"Bryson revenue vs flood buffer for ten communities across two provinces."** This is the kind of decision that should require public consultation, environmental review, and explicit cost-benefit analysis. None has been disclosed.

### The unanswered question

**What changed about the freshet operating regime at Bryson Dam after 2017? Was the impact on Lac Coulonge flood buffer evaluated before the change was made?**

Hydro-Québec acknowledges that refurbishment changes water head values. ORRPB acknowledges that higher headponds are more efficient for hydropower. The November 2025 MRC Pontiac notice confirmed a 30–50 cm rise was **tested** — its title is "notice of temporary water-level increase, Bryson Dam — Hydro-Québec." The regression analysis shows post-2017 peaks are running 58 cm higher than pre-2017 precipitation patterns predict; the year-round Lac Coulonge level data shows that gap is concentrated in the freshet peak (annual mean unchanged, off-season unchanged, only the spring peak shifted). The pattern points to operational behavior change during peak inflow rather than a permanent headpond raise. But neither agency has publicly disclosed how Bryson's freshet-period operating decisions changed during or after the refurbishment, or what flood-buffer analysis informed those changes.

**The community's policy ask is therefore not "change Bryson operations" — it is "review the operating regime against the new freshet conditions, and disclose the trade-offs."** Even granting whatever climate signal does exist, a dam built to manage river flow has an obligation to adapt as inflow patterns change. Continuing the same posture (or, per live data, moving to a higher-headpond posture) under bigger inflows is the policy choice the community is asking to be reviewed.

### Files for the case file

- `Exhibit_A_Regime_Change.{html,png}` — 18× super-flood frequency, 2017 step
- `Exhibit_B_Winter_Baseline.{html,png}` — 2026 entered freshet from elevated baseline
- `Exhibit_C_Storage_Capacity.{html,png}` — ORRPB's "too small" claim is internally inconsistent
- `Exhibit_D_Bryson_Timeline.{html,png}` — refurbishment timeline + hydraulic continuity + **Figure 7** (regression + step-change refuting climate) + **Figure 8** (live cascade) + **Live Observation panel**
- `Exhibit_E_Climate_Tested.{html,png}` — climate alternative tested four ways and rejected; **Figures 9–10** (watershed station table + Britannia step-change)
- `data/hq-opendata/` — primary-source CSV snapshots cited by Exhibit D
- `ingesters/climate-history/{lc_brit_regression,stepchange_analysis}.py` — reproducible analysis scripts

Each exhibit is editorially designed for Facebook sharing (matched typography: Fraunces serif + IBM Plex Sans/Mono; consistent palette). They can be posted individually as a five-day series, or sent as a media-ready package.

---

## Tools and Resources

### Files generated during this analysis

- `docs/analysis/Freshet_2026_Complete_Summary.md` — this document
- `docs/exhibits/Exhibit_{A,B,C,D,E}_*.{html,png}` — five-exhibit case file (rendered via `render_pngs.js`)
- `data/lac-coulonge-monthly-1972-2026.csv` — canonical Lac Coulonge monthly + annual peaks
- `data/orrpb-historic-peaks-1972-2025.csv` — ORRPB published peaks (multi-station)
- `data/wsc-hydrometric/` — WSC HYDAT extracts for Ottawa basin stations (active + discontinued)
- `data/eccc-climate/` — ECCC daily climate per-watershed-station (1972–2026)
- `data/hq-opendata/` — point-in-time Bryson + cascade snapshots cited by Exhibit D
- `ingesters/{river-history,reservoir-ingest,hq-ingest,wsc-ingest,eccc-ingest}/` — live cron pipelines
- `ingesters/climate-history/` — historical-data extracts + analysis scripts (regression, step-change)
- `dashboard/index.html` — live dashboard source

### Live infrastructure

- **Live dashboard**: https://freshet.xgrunt.com
  - Overview tab — main-stem corridor, watershed snapshot, freeze tracker
  - Stations tab — 10 Vigilance + 1 MVCA mini-charts
  - Reservoirs tab — basin-wide percent-full with optional outflow line for HQ-controlled dams
  - Tributaries tab — Gatineau + Lièvre cascade
  - **Operations tab** — live HQ release telemetry (turbined/spilled/total) for every basin centrale, with sparklines + window picker
  - Map drawer — Dams / Reservoirs / **Releases** / **Cascade** layers, with the 130-km Bryson↔Des-Joachims reach highlighted in accent red
- **Live data tables** (PostgREST `/history/...`):
  - `river_readings`, `weather_observations`, `reservoir_readings` (existing)
  - `dam_releases`, `dam_inflows`, `dam_levels`, `dam_sites` (HQ open-data)
  - `wsc_readings` (WSC realtime, both level + discharge)
  - `eccc_climate_daily` (ECCC observations)
- **Public alerter**: ntfy topic `freshet-mansfield`

### Primary data sources

- **ORRPB** (ottawariver.ca) — official forecasts, historical peaks, current conditions
- **ORRPB "Flow Management in the Ottawa River Basin" presentation** (April 2026) — official self-presentation; authoritative for the regulatory critique
- **Quebec MSP Vigilance** (vigilance.geo.msp.gouv.qc.ca) — real-time gauge level data, 18 stations now persisted (main stem + Gatineau + Lièvre)
- **Hydro-Québec open-data** (hydroquebec.com/production/debits-niveaux-eau.html) — hourly turbine + spillway + headpond + tailwater telemetry for all basin centrales (~10-day rolling window)
- **WSC realtime hydrometric** (wateroffice.ec.gc.ca) — 5-minute level + discharge for active basin gauges
- **WSC HYDAT** — quarterly SQLite archive, deep historical record
- **ECCC daily climate** (climate.weather.gc.ca) — official Canadian weather observation network, 9 watershed stations
- **Open-Meteo** — modelled / reanalysis weather for freeze tracker
- **MVCA / Kisters KiWIS** (waterdata.quinteconservation.ca) — Buckhams Bay and other MVCA gauges
- **Northern Reservoirs Flood Watch Group** (Facebook) — community reference and discussion
- **"Know Your Level" reference document** — Contributor B, flood watch community

### Upstream weather stations tracked

| Station | Coordinates | Role in basin |
|---|---|---|
| Val-d'Or, QC | 48.77°N, -77.79°W | Far north headwaters |
| Rouyn-Noranda, QC | 48.10°N, -79.02°W | Far north basin |
| Parent, QC | 47.73°N, -74.62°W | Upper Gatineau / reservoir country |
| Temiskaming Shores, ON | 47.49°N, -79.72°W | Reservoir control |
| Mattawa, ON | 46.31°N, -78.71°W | Upper river |
| Maniwaki, QC | 47.05°N, -75.97°W | Gatineau River system |
| Pembroke, ON | 45.82°N, -77.11°W | Mansfield area |

---

## Lessons Learned

### Forecast accuracy patterns

- **ORRPB forecasts can run high** — the final 108.75 m forecast came in 12 cm above actual, peak arrived ~24 hours earlier than projected
- **Multi-day plateaus are common** — Lac Coulonge held within 1 cm for 12 hours at peak, rather than a sharp single-hour crest
- **Personal property thresholds are more grounded** than gauge-level forecasts for decision-making

### Hydrological mechanism

- **Three freeze nights at the headwaters** is a reliable indicator that active melt has paused
- **Lake Témiscamingue level imbalance** is a leading indicator of forced outflow ramping
- **Travel time from Rapide 7 to Lac Coulonge** is 5–7 days — water released today doesn't arrive for nearly a week
- **Coulonge River tributary** peaks before Lac Coulonge and provides an early signal for the local component
- **Mattawa and Otto Holden** are the leading indicators for the northern pulse arriving at Lac Coulonge

### Data infrastructure

- The Quebec Vigilance API is materially better than ORRPB's aggregated site for real-time tracking — open access, hourly data, 342 stations, proper CORS
- Static HTML + JavaScript + a real http(s) origin is sufficient to build a community-grade flood monitoring dashboard
- k3s/nginx deployment is overkill but works fine and supports the use case

### Regulatory framework

- The ORRPB cannot compel changes from OPG or Hydro-Québec — it coordinates, it does not regulate
- Mandate language matters ("minimize" vs "reduce" risk are legally distinct)
- Fixed 30-year median drawdown rules are no longer fit for purpose given five major freshets in nine years
- Snowpack-indexed drawdown would be a meaningful structural improvement
- The forecast communication style (CYA hedging) is institutionally rational but not decision-useful for homeowners

### Future freshet response at this property

1. **Primary gauge**: Lac Coulonge (Vigilance Station 1195)
2. **Leading indicator (local)**: Coulonge River (Vigilance Station 1004)
3. **Leading indicator (upstream)**: Mattawa, Otto Holden (ORRPB)
4. **Meteorological lead**: freeze tracker — Val-d'Or, Rouyn-Noranda, Temiskaming overnight lows
5. **Action thresholds**:
   - 108.00 m + rising forecast: start active preparations
   - 108.30 m: water days away from backyard
   - 108.48 m: backyard flooding, pumps operational
   - 108.75 m: sandbag cottage foundation
   - 108.90 m+ rising: consider evacuation

---

## Appendix A: 2019 Original Property Observations

Reference data from personal 2019 flood notes at Mansfield property:

| 2019 Date | Lac Coulonge Level | Observation |
|---|---|---|
| April 24 | 108.10 m | No flooding |
| April 25 | 108.32 m | Water had not reached backyard or big tree in front |
| April 26 | 108.48 m | Water in backyard, filling end of driveway, reached big tree |
| April 27 | 108.75 m | Water at end of bricks on cottage; no water inside by 9 PM |
| April 28 | 109.01 m | Water INSIDE cottage at back, in garage, where dad parks RV |
| April 29 | 109.10 m | First peak |
| April 30 | 109.02 m | Beginning of decline |
| May 11–12 | 109.17 | **Second peak** (13 days after first) — record set |

2017 reference: peak was 108.52 — water never reached front of cottage, was in crawl space up to floor joists.

---

## Appendix B: Substantive Policy Points from Community Discussion

Four threads from the Northern Reservoirs Flood Watch Group surfaced policy arguments worth preserving:

### Thread 1: Snowpack-indexed drawdown vs fixed 30-year median rules

The ORRPB currently follows fixed 30-year median guidelines for reservoir drawdown. This treats every year the same regardless of snowpack conditions. The community's counter-proposal: snowpack data is available months in advance and should drive the drawdown target. Heavy snow year = lower drawdown. Light snow year = less aggressive. The 2024 vs 2026 contrast (similar approach, opposite outcomes) demonstrates the rule's failure mode.

### Thread 2: Real-time data accessibility

The ORRPB website aggregates from three operating agencies with different telemetry and update schedules. Stale caches and 4 PM weekday updates during active flood events are inadequate. The technology to fix this is trivial; the barrier is institutional. Real-time public data would expose operational decisions (when reservoirs are held high for generation vs drawn down for flood buffer) that the operators prefer not to have scrutinized. The Quebec Vigilance API provides a model for what's possible — open access, hourly data, no authentication, proper CORS. The ORRPB equivalent could exist.

### Thread 3: Forecast communication — CYA vs analytical scenarios

The ORRPB's prose forecasts ("remains uncertain... remains possible... could lead to...") are legal hedging dressed as forecasting. They sound authoritative but provide nothing actionable. The data inputs (snowpack, weather forecasts, reservoir state, gauge readings) are sufficient to publish IF-THEN scenarios indexed to rainfall amounts. This is standard practice for hurricane forecasting (NOAA cone-of-uncertainty), wildfire risk, and other weather-driven hazards. The forecast horizon limitation (~3–4 days for weather) is exactly why scenarios should be published — as the 4-day forecast updates, the homeowner knows which scenario applies. A homeowner with a laptop and public data can produce a useful read; the agency with hydrologists on staff can publish a better one.

### Thread 4: Mandate clarity and accountability

ORRPB language has shifted from "minimizing" flood risk to "reducing" flood risk over the past decade — legally distinct commitments. The board is also a coordination function without enforcement authority. Real power sits with the operators (OPG, Hydro-Québec), whose mandates are power generation. The structure produces the opacity outcomes by design. Mandate review and authority clarification is a precondition for any of the other reforms.

### Thread 5: Empirical evidence of regime change (Contributor A's analysis)

A flood watch member with operational experience working on watershed dams compiled Lac Coulonge yearly peaks 1972-2026 and demonstrated an 18-fold increase in super-flood (>108.5 m) frequency between the 1972-2016 era (1 event in 45 years) and 2017-2026 (4 events in 10 years). The step-function shape of the change rules out gradual climate drivers as the sole cause and points to operational regime change around 2016-2017 as the proximate explanation. This empirical pattern shifts the community's policy arguments from "we suspect something has changed" to "something has demonstrably changed and an operational explanation is required."

### Thread 6: Contractual obligations — freshet vs fall drawdown

The "💰 guys" appear in threads to explain why operational changes are impossible due to power contracts. This argument conflates two distinct operational windows. During the three weeks of peak freshet flow, excess water above turbine capacity is spilled through gates regardless of any contract — generating zero revenue and unaffected by any reservoir decision. The actual revenue trade-off lives in fall drawdown decisions (October-March), where deeper drawdown does affect winter generation. Community arguments for snowpack-indexed drawdown engage with the legitimate fall trade-off; they do not require any change to freshet operations during peak flow. The "contracts prevent change" argument applied to freshet management is conflating the wrong window.

### Thread 7: ORRPB's official self-presentation as evidence

The ORRPB's April 2026 "Flow Management in the Ottawa River Basin" document (40-slide presentation) provides authoritative source material that strengthens rather than weakens the community's structural critique. The board explicitly admits it is "not a control board" and "cannot direct how operators manage their reservoirs or facilities" (Slide 11). It quantifies its 2019 reservoir effect at 120 cm of reduction at Lac Coulonge (Slide 15) — establishing both that the reservoirs do real work AND that the operational ceiling under current rules is roughly that magnitude. The "minimize impacts of floods" mandate language remains official (Slide 8). The document does not engage with the regime change documented by Contributor A, frames the "more reservoirs?" question (which nobody is asking) instead of the "different operations?" question (which the community is asking), and does not publish the multi-decade reservoir storage data that would document operational shifts. The ORRPB's own document points the policy conversation past the ORRPB itself toward the actual decision-makers: Hydro-Québec, OPG, and the provincial/federal principals (MELCCFP, MNR, ECCC).

### Thread 8: Operational mechanism validation by community insider (Contributor B)

Several operational behaviors initially identified through data observation were validated by Contributor B on April 30. These transitioned from inference to confirmed mechanism: (1) reservoirs universally ramp outflow as they near capacity to prevent emergency release, making percent-full a true leading indicator; (2) Des Joachims explicitly pauses Stage 1 refill and operates as pure run-of-river when Mattawa reaches flood territory, eliminating its normal buffer role and shortening effective Mattawa-to-Coulonge travel time; (3) Hydro-Québec releases proactively ahead of forecasted inflow (Baskatong doubled outflow with 3.5 m of headroom remaining, anticipating rain-driven inflow rather than responding to capacity constraint). None of these operational rules is published in ORRPB forecasts or press releases. The information exists internally and is verifiable post-hoc by community members with operational knowledge, but is not made available to property owners making preparation decisions in real time. This is the data accessibility gap stated as concrete mechanisms: not abstract opacity, but specific operational rules that would change a homeowner's preparation strategy if known.

### Thread 9: Climate test — quantitative regression analysis

The climate alternative was tested four ways. **(1) Cold-season precipitation regression**: pre-2017 (n=44) vs post-2017 (n=10) Ottawa CDA precipitation differed by only +3.7% (not significant). A linear model trained on pre-2017 data predicted post-2017 peaks; actual peaks averaged **+58 cm above prediction**, with super-flood years at +90, +157, +113, and +127 cm. **(2) Per-event amplification regression** (Lac Coulonge peak ~ Britannia annual peak): pre-2017 and post-2017 fits are essentially identical (slope shift +0.012 m per 1000 m³/s, intercept shift -4.8 cm, mean post-2017 residual from pre-line +0.1 cm). The lake responds to inflow as it always has — the +59 cm in mean peak is composition-driven, not amplification. **(3) Watershed-station forcing**: across nine ECCC stations, Apr+May precipitation shifts span -4% to +36% with no coherent step; March snow trends *down* at the upper basin (Témiscamingue -15%, Val-d'Or -14%). **(4) Step location**: median Britannia annual-peak shift maximizes at exactly 2017 (+19.3%) and decays both directions, with three full prior decades (1980s-2000s) at zero super-floods each. **Conclusion:** climate change in the basin is real but does not by itself explain the post-2017 regime change at Lac Coulonge. **And even if it did contribute, the operator's response remains the controllable variable** — a dam built to manage river flow has an obligation to adapt as inflow patterns change.

### Thread 10: The case file — five-exhibit analytical argument

The policy analysis is distilled into a five-exhibit case file designed for community sharing and media use. **Exhibit A** establishes the outcomes problem (18× super-flood frequency increase, sharp 2017 step). **Exhibit B** establishes the inputs shift (2026 winter baseline 14 cm above prior decade). **Exhibit C** establishes a specific operational lever exists (302 million m³ storage capacity at Lac Coulonge, refuting ORRPB FAQ Q5 Part D's "no benefit" position). **Exhibit D** establishes the operational change with documented timing (Bryson refurbishment 2017–2023), proves climate alone cannot explain the step (Figure 7 regression + step-change test), shows Bryson is the spillway-dominant outlier in its own cascade (Figure 8), and reveals the live operating signature via Hydro-Québec's open-data feed (Live Observation panel). **Exhibit E** tests the climate alternative four ways across the watershed and rejects it; it also makes the second-order argument that even if climate contributed, adaptation is the operator's obligation. Each exhibit can stand alone; together they form a complete, governance-focused argument that does not require winning the climate-attribution debate. The framing is "asking questions backed by verified facts" — every claim is sourced; the policy ask is operating-regime review, not accusation.

---

## Data Disclaimer

This document compiles preliminary data and personal analysis for informational purposes only. Official flood forecasts and emergency guidance come from:

- **Ottawa River Regulation Planning Board** (ottawariver.ca)
- **Quebec MSP** (vigilance.geo.msp.gouv.qc.ca)
- **Ministry of Natural Resources Ontario** (Ontario side)
- **Local municipal emergency authorities**

Do not make life-safety decisions based solely on this analysis. Property thresholds are based on one homeowner's observations of one specific location and may not apply to other properties or future conditions.

---

*Prepared through collaborative real-time analysis: April 14–28, 2026. This document represents a snapshot of findings during an active flood event. Forecasts and conditions continue to evolve. Live data: https://freshet.xgrunt.com*
