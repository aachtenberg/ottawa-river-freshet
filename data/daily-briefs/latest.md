# Daily brief — 2026-05-10

*Generated automatically at 11:11 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

## TL;DR

Four items today: (1) Lac Coulonge continued receding at −8 cm to 107.91 m, still in etat 4 (minor flood), pace slightly slower than yesterday's −9.5 cm. (2) The ORRPB northern-basin rain forecast is now partially verifying — Mattawa rose +6 cm to 154.41 m, its first rise after two flat days, consistent with the weekend-rain prediction; watch for downstream propagation over the next 24–48 h. (3) Active basin-wide retention flag triggered: Baskatong (+12 cm/day) and Dozois (+10 cm/day) both at or above the 10 cm/day threshold, meaning headwater operators are absorbing inflow rather than passing it. (4) Carillon §15.3.5.1 directive overshoot edged to 45 cm (from 44 cm yesterday) as the headpond ticked up 1 cm while releases fell a further 4.4%. The predicted routing-lag surge from yesterday's upper-cascade drawdown (+7–14% at five sites) has not yet arrived at Bryson or Carillon; watch tomorrow.

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: cluster proxy `river_readings` station 1195. Latest observation: 2026-05-10T09:00 UTC. 24h comparison: 107.986 m at 2026-05-09T09:00 UTC (from May 9 brief).*

| Metric | Value |
|---|---|
| Current level | 107.906 m (at 09:00 UTC) |
| 24h delta | −8.0 cm |
| ORRPB midnight reading (May 10) | 107.91 m (consistent) |
| Flood state | etat 4 — minor flood |
| Distance above minor threshold | +40.6 cm above sim-niv 107.500 m |
| Distance below moderate threshold | −9.4 cm below simoy-niv 108.000 m |
| Distance to major threshold | −59.4 cm below simaj-niv 108.500 m |

**Threshold reference (station 1195):**

| Code | Level (m) | Meaning |
|---|---|---|
| simaj-niv | 108.500 | Major flood |
| simoy-niv | 108.000 | Moderate flood |
| sim-niv | 107.500 | Minor flood |
| spa-niv | 107.000 | Pre-alert |

**Recession trend (from prior briefs):**

| Date | Daily delta | Level at reading |
|---|---|---|
| May 5 | −5.8 cm | ~108.384 m |
| May 6 | −6.6 cm | ~108.320 m |
| May 7 | −7.7 cm | ~108.246 m |
| May 8 | −7.9 cm | ~108.168 m |
| May 9 | −9.5 cm | 107.986 m |
| **May 10** | **−8.0 cm** | **107.906 m** |

Rate slowed slightly from yesterday's −9.5 cm to −8.0 cm. At −8 cm/day, the lake would exit minor flood (107.500 m) in ~5 days — but the Mattawa rise (see ORRPB section) may slow or stall the descent over the next several days.

## Bryson operating posture (HQ open-data via cluster proxy)

*Source: cluster proxy `dam_releases` (site 3-46) and `dam_levels` (stations 1-2964 amont, 1-2965 aval). Today = 2026-05-09T19:00 UTC (latest available, ~16 h lag). Yesterday = 2026-05-08T19:00 UTC.*

| Metric | Today | Yesterday | Δ |
|---|---|---|---|
| Total release (m³/s) | 1,179.24 | 1,224.14 | −44.90 (−3.7%) |
| Turbined (m³/s) | 238.58 | 239.12 | −0.54 (−0.2%) |
| Spilled (m³/s) | 940.66 | 985.03 | −44.37 (−4.5%) |
| Spill share (%) | 79.8% | 80.5% | −0.7 pp |
| Headpond / amont (m) | **104.35** | **104.52** | **−17 cm** |
| Tailwater / aval (m) | 89.22 | 89.35 | −13 cm |
| Δh — head differential (m) | 15.13 | 15.17 | −0.04 m |

**Headpond operating band (104.20–104.67 m):** headpond at 104.35 m is 15 cm above lower bound and 32 cm below upper bound — within band. Yesterday's concern (rising 20 cm toward 104.67 m upper bound) resolved; headpond reversed and fell 17 cm. No band breach.

**Posture note:** No single metric exceeds the 5% flag threshold (spilled at −4.5% is the closest). The headpond reversal is notable — yesterday's 20 cm rise with flat releases implied elevated inflow to the Bryson forebay; today's 17 cm fall with a similar 3.7% release reduction suggests that inflow pulse subsided. Turbine share: 238.58 / 1,179.24 = 20.2%, essentially unchanged from 19.5% yesterday.

## Main-stem cascade (HQ centrales via cluster proxy, m³/s total release)

*Source: cluster proxy `dam_releases`. Today = 2026-05-09T19:00 UTC; yesterday = 2026-05-08T18–19:00 UTC (from May 9 brief). Spill % = spilled / total. Note: Rapide-7 spilled_cms reported as null in proxy; derived as total − turbined = 79.80 m³/s.*

| Site | Total today | Total yest. | Δ% | Spill % today | Spill % yest. |
|---|---|---|---|---|---|
| Première-Chute (3-33) | 1,025.05 | 1,015.03 | +1.0% | 44.2% | 43.5% |
| Quinze (3-31) | 986.67 | 973.94 | +1.3% | 58.9% | 58.3% |
| Îles (3-32) | 1,094.59 | 1,084.16 | +1.0% | 55.9% | 55.3% |
| Rapide-2 (3-29) | 494.02 | 495.60 | −0.3% | 33.9% | 33.9% |
| Rapide-7 (3-28) | 420.54 | 420.09 | +0.1% | ~19.0% (derived) | 19.0% |
| Bryson (3-46) | 1,179.24 | 1,224.14 | −3.7% | 79.8% | 80.5% |
| **Paugan — Gatineau R. (3-65)** | **611.06** | **660.28** | **−7.5% ⚠** | **5.8%** | **12.2%** |
| Rapides-Farmers — Gatineau (3-67) | 629.20 | 648.10 | −2.9% | 24.8% | 27.2% |
| Carillon — basin terminal (3-60) | 5,313.25 | 5,557.25 | −4.4% | 42.4% | 44.8% |

**Cascade notes:**

- **Upper Ottawa (Première-Chute through Rapide-7) stabilized:** All five sites are flat to +1.3% after yesterday's massive coordinated surge (+6–14%). The drawdown pulse is plateauing at these elevated levels. Spill shares are also essentially flat, consistent with post-drawdown steady state.

- **Predicted routing pulse has not arrived at Bryson or Carillon:** Yesterday's brief forecast that the upper-cascade surge would propagate to Bryson (~24 h travel time) and Carillon (~24–48 h) by today. Instead, both fell further (Bryson −3.7%, Carillon −4.4%). The pulse may be attenuated by mid-cascade storage or may arrive later today or in the May 11 brief. Reservoir data (Baskatong, Dozois rising) suggests some of the upstream volume is being absorbed at headwater reservoirs rather than routed through (see Reservoir section).

- **Paugan (3-65) −7.5% ⚠:** Exceeds the 5% flag threshold. Spill share dropped from 12.2% to 5.8% (−6.4 pp), absolute spill falling from 80.55 to 35.52 m³/s. This is a Gatineau tributary site; the reduction likely reflects deliberate generation dispatch adjustment rather than a basin inflow change.

- **Carillon continuing decline:** Basin terminal now at 5,313.25 m³/s, down from 6,060.80 m³/s three days ago (−12.3% over three days). ORRPB flow gauge confirms: Carillon averaged 5,292 m³/s on May 10.

## Carillon §15.3.5.1 directive check

*Source: cluster proxy `river_readings` (station 1-3675, Hull dock) and `dam_levels` (station 1-2968, Carillon amont). Both latest: 2026-05-09T19:00 UTC.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (station 1-3675) | 43.33 m | 42.61 m servitude | **ABOVE — trigger active** (+72 cm above) |
| Carillon amont (station 1-2968) | 40.53 m | 40.08 m spring-flood ceiling | **OVERSHOOT — 45 cm above ceiling ⚠** |

Hull dock at 43.33 m is 72 cm above the 42.61 m servitude — the IWMP §15.3.5.1 spring-flood operating ceiling of 40.08 m at Carillon remains formally in effect. Carillon headpond at 40.53 m is 45 cm above that ceiling, a continuing directive exceedance.

**24 h change:**
- Hull dock: fell −3 cm (43.363 m → 43.330 m). ORRPB midnight reading (May 10): 43.28 m (Hull), consistent.
- Carillon amont: rose +1 cm (40.52 m → 40.53 m). Overshoot: 44 cm → **45 cm** (continuing to worsen, though slowly).
- Note: ORRPB midnight reading confirms Carillon at 40.52 m (May 10), consistent with proxy.

**Trend:** The overshoot has now worsened for two consecutive days (+3 cm May 8→9, +1 cm May 9→10) as Carillon simultaneously reduced releases (−8.3% yesterday, −4.4% today). Net result: releases declining, headpond rising, ceiling not approached. Upstream trigger (Hull dock) is declining slowly but remains far above the 42.61 m threshold.

*See `docs/analysis/Freshet_2026_Complete_Summary.md` § "The Carillon directive enforcement gap" for regulatory context.*

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings`. Snapshot: 2026-05-09T00:00 UTC (~35 h before brief generation — within 48 h validity window). Day-over-day deltas vs May 9 brief (2026-05-08T00:00 UTC snapshot).*

| Reservoir | Level (m) | 24h delta | Agency | Trend |
|---|---|---|---|---|
| Baskatong | 221.03 | **+12 cm ⚠** | HQ | Rising — exceeds 10 cm/day threshold |
| Dozois | 344.85 | **+10 cm ⚠** | HQ | Rising — at 10 cm/day threshold |
| Cabonga | 360.15 | +2 cm | HQ | Stable |
| Bark Lake | 313.52 | +3 cm | OPG | Rising modestly |

**Active basin-wide retention flag TRIGGERED.** Two reservoirs (Baskatong +12 cm, Dozois +10 cm) meet the "2+ reservoirs rising ≥10 cm/day" criterion. This is a reversal from the May 9 assessment (Baskatong +8 cm, Dozois +6 cm — below threshold). Rising reservoir levels during this phase indicate operators are absorbing inflow rather than routing it downstream. This explains why the expected upstream-cascade routing pulse has not yet appeared at Bryson/Carillon: the upper-cascade releases are partly being stored at headwaters.

Other reservoirs for reference (2026-05-09T00:00 UTC snapshot): Timiskaming 178.88 m, Quinze 263.10 m, Rapide-7 308.93 m, Kiamika 268.28 m.

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. **Last Update: 2026-05-09 2:33 PM EDT** (18:33 UTC). Next Update: 2026-05-10 4:00 PM EDT (scheduled update later today).*

The forecast was updated May 9 at 2:33 PM EDT (earlier than expected — the May 9 brief anticipated a 4:15 PM EDT update). The text is substantively unchanged from the May 8 version:

> Spring runoff in the northern part of the basin is expected to rise this weekend due to forecast rain. As a result, the decline in water levels and flows between Mattawa and Pembroke is expected to slow down and may come to a stop, depending on the amount of rain received. Elsewhere along the river from Lake Coulonge to the Montreal Region, water levels and flows should continue to decrease gradually in all locations over the coming week. Because large volumes of water continue to come from the northern part of the basin, water levels along the main stem of the river are expected to remain generally high over the next few days. The northern part of the basin will remain vulnerable to heavy rainfall events in the coming weeks; therefore, further increases in water levels from Mattawa to Lake Coulonge due to high spring runoff cannot be ruled out.

**Weekend rain forecast partially verified (as of May 10 morning):**

| Location | May 9 | May 10 | Δ | Notes |
|---|---|---|---|---|
| Mattawa (WSC) | 154.35 m | **154.41 m** | **+6 cm** ↑ | First rise after flat 154.35 for two days — rain signal |
| Otto Holden (OPG) | 176.66 m | 176.69 m | +3 cm | Slight rise |
| Des Joachims (OPG) | 150.49 m | 150.47 m | −2 cm | Flat to slight fall |
| Pembroke (OPG) | 112.85 m | 112.85 m | 0 cm | Flat (forecast verified — slowdown confirmed) |
| Lake Coulonge, Fort-Coulonge | 107.95 m | 107.91 m | −4 cm | Continued fall, rain not yet reached here |
| Lake Deschenes / Britannia | 59.67 m | 59.65 m | −2 cm | Continued gradual fall |
| Carillon amont (HQ) | 40.51 m | 40.52 m | +1 cm | Slight headpond rise |

**Summary:** The forecast's prediction that Mattawa-Pembroke would slow and potentially stall is verifying. Mattawa is now rising (+6 cm). Pembroke is flat. These are the first northern-basin rises in this monitoring record. Downstream effects (Lake Coulonge, Carillon) have not yet manifested. The ORRPB update expected today at 4:00 PM EDT may revise the outlook given this early-weekend verification.

**Average Daily Flows at Carillon (ORRPB):** 5,292 m³/s on May 10 (down from 5,352 on May 9, 5,623 on May 8, 5,859 on May 7) — consistent with a continuing but decelerating decline.

## Anomaly flags

1. **Carillon §15.3.5.1 directive overshoot worsened to 45 cm:** Hull dock trigger active (43.33 m >> 42.61 m servitude). Carillon amont rose +1 cm to 40.53 m while Carillon release fell 4.4%. Overshoot magnitude: 45 cm above 40.08 m ceiling (+1 cm from yesterday's 44 cm, +4 cm from day before's 41 cm). Trajectory of compliance continues away from the regulatory limit.

2. **Active basin-wide retention flag TRIGGERED (Baskatong +12 cm/day, Dozois +10 cm/day):** Two headwater reservoirs are rising at or above the 10 cm/day threshold. Last brief had Baskatong at +8 cm (below threshold). Consistent with operators absorbing the weekend-precipitation inflow surge at the headwaters rather than routing it downstream. Partially explains why the upstream-cascade surge predicted to arrive at Bryson/Carillon has not materialized.

3. **Mattawa +6 cm (rain signal — forecast verification):** First Mattawa level rise since at least May 3. The ORRPB forecast of northern-basin precipitation this weekend is now showing up in gauge data. Downstream propagation to Lake Coulonge / Bryson is expected in 24–96 h depending on routing. Current Lac Coulonge recession could stall or reverse within 2–5 days.

4. **Paugan (3-65) release fell −7.5% ⚠:** Exceeds the 5% flag threshold. Spill share dropped from 12.2% to 5.8% (−6.4 pp). This is a Gatineau tributary site.

5. **Predicted routing-lag pulse (from May 9 upper-cascade surge) has not arrived:** Both Bryson (−3.7%) and Carillon (−4.4%) declined again today. The pulse appears to be partly absorbed by rising headwater reservoirs (Baskatong, Dozois). Monitor for delayed arrival in May 11 brief.

6. **Bryson headpond 17 cm reversal:** After rising 20 cm yesterday toward the 104.67 m upper operating-band limit, the headpond fell 17 cm today to 104.35 m. Upper-band breach concern from yesterday's brief is resolved for now.

## Notes

- **Routing-pulse outlook for May 11:** The upper-cascade surge released May 8→9 (+7–14% across five sites) appears to be buffered at headwater reservoirs (Baskatong, Dozois filling). The residual pulse that does route through will arrive at Bryson and Carillon over the next 24–72 h. The May 11 brief should watch for Bryson total release rising toward or above 1,224 m³/s, and Carillon rising above 5,313 m³/s.

- **Rain arrival at Lac Coulonge:** Mattawa (upstream) is now rising. Travel time from Mattawa to Lake Coulonge is approximately 2–4 days depending on routing. If the rise persists, Lake Coulonge should feel it around May 12–14. Current recession rate (−8 cm/day) gives a comfortable 40 cm buffer above minor-flood threshold (107.500 m), but a 3–5 day stall would leave the lake still in minor flood through mid-May.

- **Reservoir retention interpretation:** Rising headwater reservoir levels while upper-cascade centrales also release more is unusual. Both signals are simultaneous: Baskatong/Dozois rising while Quinze/Îles/Première-Chute also releasing more. This suggests total inflow at headwaters exceeds both what is being passed and what is being stored — or that storage is absorbing the difference between the very high inflows and already-elevated releases. Either way, the northern basin is in an active-inflow state, consistent with the weekend rain.

- **ORRPB next update today at 4:00 PM EDT:** The scheduled update will likely adjust the "this weekend" language now that the weekend rain is verifying and Mattawa is rising. Check for any revised forecasts at Lac Coulonge or downstream gauges in the May 11 brief.

- **Case-file update:** Carillon overshoot at 45 cm is now the highest observed in this monitoring record (was 41 cm on May 7, 44 cm on May 9, now 45 cm on May 10). The operator continues to reduce throughput at a headpond 45 cm above its regulatory spring-flood ceiling, rather than maximizing release to approach compliance. Record.
