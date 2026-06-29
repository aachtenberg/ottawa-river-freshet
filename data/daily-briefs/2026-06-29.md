# Daily brief — 2026-06-29

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (freshet.xgrunt.com/history) — guardrail probe: HTTP 200 ✓ (112 b). ORRPB forecast page: HTTP 200 ✓ (130,741 b) — last updated June 23 3:43 PM EDT; next update June 30 4:00 PM EDT (weekly cadence; TOMORROW). HQ dam/cascade data via proxy, current to June 29 T19:00 UTC (3 PM EDT). ORRPB daily flow/level series current to June 29 midnight. Vigilance station 1195 current to June 29 T20:00 UTC (4 PM EDT) — data gap from T02:00–T14:00 UTC resolved; direct Vigilance API confirmed unreachable (probed: proxy 200/112b, direct Vigilance 502/0b).*

---

## In plain language

### Upstream — the upper basin

The daily flow measurement at the outlet of Lake Témiscaming came in at 495 cubic metres per second today — a third consecutive day of increase from last week's low, and a meaningful correction to yesterday's brief. The provisional "400 m³/s" reading from June 28 that prompted yesterday's sub-400 milestone announcement turned out to be a round-number estimate: when the official figure was published today, it was revised upward to 467. The sub-400 milestone never actually occurred. At 495 m³/s today, the basin is moving slightly the wrong way for recession-watchers — still well within the sub-500 range (the fourth straight day below that threshold), but edging up rather than down. The upper Ottawa is producing about 18% of its May 2 freshet-peak flow, and it appears to be responding to the recent rainfall that the planning board mentioned in its most recent forecast. The next official forecast update from the Ottawa River Regulation Planning Board is due tomorrow at 4 PM Eastern time — the first new forecast in seven days.

Partway down the valley, the overnight gauge at Mattawa showed the river at 152.17 metres — about 23 centimetres lower than yesterday's revised midnight reading of 152.40 metres. The overall pattern at Mattawa is one of general decline interrupted by occasional one-day pulses; the underlying direction is clearly down, though the daily readings at this station carry noticeable noise. Pembroke, further downstream, held essentially flat at 111.37 metres for a second straight day.

The most notable mid-valley development today is a large reduction at Des Joachims, a major generating facility operated by Ontario Power Generation. Their daily discharge dropped from about 628 to 347 cubic metres per second — roughly half the previous flow. This is a significant operational step-change; OPG appears to be holding water in the reach above the dam rather than passing it downstream. The effect ripples through: the reach above the dam (reflected at the Otto-Holden gauge, which rose 10 centimetres overnight) is backing up slightly, while downstream, the basin-terminal dam at Carillon released roughly 18% less water today than yesterday. Across the basin's storage reservoirs, several are now drawing down: Des Joachims (−13 cm), Poisson Blanc (−10 cm), Dozois (−5 cm), and Kiamika (−4 cm) all fell overnight, while Bark Lake ticked up 4 centimetres. The count is 4 falling, 9 steady, 1 rising — a normal post-freshet summer drawdown posture, not a cause for concern, but worth noting for the record.

### At the property — Lac Coulonge / Mansfield

The gauge that tracks conditions near the Mansfield waterfront properties — a Quebec government telemetry station located on the lake itself, not at the dam — came back online after a gap that started yesterday morning. As of 4 PM Eastern time today, the lake sits at 106.116 metres, essentially unchanged from the same hour yesterday (106.126 m, −1 cm). The official midnight-to-midnight reading from the planning board's published series moved from 106.13 to 106.12 metres, another 1-centimetre slip. The slow drift continues: the lake has eased about 11 centimetres over the past week and is now 88 centimetres below the pre-alert advisory threshold of 107.00 metres. Conditions are fully normal.

**The dam pond at Bryson Generating Station — a distinct location several kilometres down the narrowing south arm of Lac Coulonge from the lake gauge, accessed by following the channel to where it narrows and winds down to the dam — had significant news today.** After 15 consecutive days with all turbines shut off, Hydro-Québec restarted power generation at Bryson. The turbines came back online overnight and were producing about 35 cubic metres per second of turbined flow by this morning's readings, reducing the spillway's share from 100% to about 93% of total releases. Total outflow rose about 33 cubic metres per second to roughly 498 m³/s — a 7.3% increase that crosses the flag threshold. Despite the higher releases, the dam pond level ticked upward slightly, from 105.38 to 105.46 metres. Whether this reflects a brief inflow pulse, upstream operational changes, or measurement noise is unclear from the data. The dam pond remains 79 centimetres above the operators' permitted upper ceiling of 104.67 metres — the 32nd consecutive day of that exceedance. The turbine restart is a meaningful operational step, but the dam pond has not yet started a meaningful drawdown trajectory.

---

## TL;DR

**⚠ CORRECTION: sub-400 milestone RETRACTED — June 28 revised 400→467 m³/s; June 29=495. Day 3 consecutive rise (Jun 27=462→Jun 28=467→Jun 29=495). Day 4 sub-500; Day 7 sub-700.** ⚠ Bryson turbines restarted (15-day outage ended): total release +7.3% (464.62→498.32 m³/s ⚠ >5% flag); spill 100%→93%; headpond +8 cm (105.38→105.46 m, Day 32 breach, +79 cm above ceiling). ⚠ Carillon −17.5% (2,038→1,681 m³/s ⚠ >5% flag) — Des Joachims cut 628→347 m³/s. Lac Coulonge: Vigilance back online (T20 UTC 106.116 m, −1.0 cm same-hour; ORRPB midnight 106.12 m, −1 cm; etat 0, 88 cm below pre-alert). §15.3.5.1 INACTIVE Day 35 (Hull dock 41.39 m, −8 cm, 122 cm below 42.61 trigger). Reservoir balance: 4 falling · 9 steady · 1 rising. ORRPB forecast unchanged from June 23 — next update TOMORROW June 30 4 PM EDT. Day 59 post-primary peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Sources: proxy `river_readings` station 1195 (latest: June 29 T20:00 UTC / 4:00 PM EDT — data resumed after T14:00 UTC gap; probed: direct Vigilance 502/0b); proxy `orrpb_river_levels` station `lake-coulonge` (midnight series through June 29).*

| Metric | Value |
|---|---|
| Current level (proxy station 1195, June 29 T20:00 UTC / 4:00 PM EDT) | **106.116 m** |
| ORRPB midnight (June 29, preliminary) | **106.12 m** |
| ORRPB midnight (June 28, confirmed) | 106.13 m |
| 24h delta (same-hour: June 28 T20 106.126 → June 29 T20 106.116) | **−1.0 cm — slow decline continues** |
| 24h delta (midnight: June 28 106.13 → June 29 106.12) | **−1 cm — second day of 1-cm slips at midnight** |
| Flood state | **etat 0 — fully normal** (no threshold exceeded) |
| Distance to pre-alert (107.00 m) | **88 cm below** |
| Distance to minor flood (107.50 m) | 138 cm below |
| Distance to moderate flood (108.00 m) | 188 cm below |

**ORRPB midnight level series (from DB `orrpb_river_levels`):**

| Date | Level (m) | Midnight Δ | Notes |
|---|---|---|---|
| June 23 | 106.23 | −5 cm | Confirmed |
| June 24 | 106.19 | −4 cm | Confirmed |
| June 25 | 106.13 | −6 cm | Confirmed |
| June 26 | 106.10 | −3 cm | Confirmed |
| June 27 | 106.11 | +1 cm | (minor intraday variation — sequence not monotone) |
| June 28 | 106.13 | +2 cm | Confirmed — slight rise, possibly rounding artifact |
| **June 29** | **106.12** | **−1 cm** | Preliminary; overall trend flat-to-declining |

Note: the 106.11→106.13 variation over June 27–28 is within noise (1–2 cm) at this stage. The live Vigilance hourly readings show a consistent slow decline of ~1 cm per 24 hours at the 4 PM EDT observation hour, which is more reliable than the midnight series for day-to-day trending.

---

## Bryson operating posture (HQ proxy)

*Source: proxy `dam_releases` (site 3-46, latest June 29 T18:00 UTC / 2 PM EDT) and `dam_levels` (stations 1-2964 amont, 1-2965 aval, June 29 T19:00 UTC / 3 PM EDT). "Yesterday" = June 28 T19 UTC values.*

**⚠ Major posture change: turbines restarted after 15-day outage (June 15–June 29).**

| Metric | Today (June 29) | Yesterday (June 28 T19) | Δ |
|---|---|---|---|
| Total release (m³/s) | **498.32** | 464.62 | **+33.70 (+7.3%) ⚠ >5% flag** |
| Turbined (m³/s) | **35.07** | 0 | **+35.07 — turbines RESTARTED Day 1** |
| Spilled (m³/s) | **463.25** | 464.62 | −1.37 (−0.3%) — essentially unchanged |
| Spill share (%) | **93.0%** | 100% | **−7 pp** |
| Headpond / amont (1-2964, m) | **105.46** | 105.38 | **+8 cm — rising despite higher releases** |
| Tailwater / aval (1-2965, m) | **87.15** | 87.34 | −19 cm |
| Δh (head differential, m) | **18.31** | 18.04 | +27 cm |

Total release +7.3% — ⚠ exceeds 5% flag. Turbines back online at 35 m³/s turbined. Headpond at 105.46 m is 79 cm above 104.67 m operating ceiling — **Day 32 breach continues**. Headpond rose +8 cm despite higher total release; this may reflect upstream inflow variation or intraday measurement noise (T17=105.38, T18=105.50, T19=105.46 — ±12 cm intraday swing). The headpond has not begun a sustained drawdown trajectory.

**Headpond series (key breach milestones):**

| Date (T19 UTC) | Headpond (m) | vs. band ceiling 104.67 m | Δ day-over-day |
|---|---|---|---|
| May 29 | 104.92 | +25 cm — Day 1 breach | — |
| June 9 | 105.44 | +77 cm — Day 12 | — |
| June 15 | 105.47 | +80 cm — turbine outage Day 1 | — |
| June 21 | 105.56 | +89 cm — ALL-TIME HIGH | +1 cm |
| June 22 | 105.47 | +80 cm | −9 cm |
| June 23 | 105.35 | +68 cm — major retreat | −12 cm |
| June 24 | 105.41 | +74 cm — rebound | +6 cm |
| June 25 | 105.37 | +70 cm | −4 cm |
| June 26 | 105.38 | +71 cm | +1 cm |
| June 27 | 105.39 | +72 cm | +1 cm |
| June 28 | 105.38 | +71 cm | −1 cm |
| **June 29** | **105.46** | **+79 cm** | **+8 cm — turbines restarted; headpond rising** |

Seven consecutive days (June 22–28) in the 105.35–105.39 m band; June 29 broke upward to 105.46 m on turbine restart day. Drawdown has not commenced.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: proxy `latest_dam_releases` (all readings June 29 T18–T19 UTC). "Yesterday" = June 28 T18–T19 values. Spill % = spilled / total × 100.*

| Site | Total (m³/s) | Spill % | Δ vs June 28 | Notes |
|---|---|---|---|---|
| Première-Chute (3-33) | 308.01 → **316.29** | 0% | +2.7% | Upper cascade slightly up |
| Quinze (3-31) | 308.72 → **307.72** | 0.4% (1.13 m³/s) | −0.3% | Trace spill continues |
| Îles (3-32) | 304.47 → **306.13** | 0% | +0.5% | |
| Rapide-2 (3-29) | 238.25 → **237.86** | 0% | −0.2% | **Gap to Des Joachims (347 m³/s today) persists ~109 m³/s; narrowed from ~186 m³/s (Des Joachims cut)** |
| Rapide-7 (3-28) | 241.29 → **241.66** | 0% | +0.2% | Steady |
| Bryson (3-46) | 464.62 → **498.32** | **93.0%** | **+7.3% ⚠ >5%** | Turbines restarted; Day 32 breach; 100%→93% spill |
| Paugan — Gatineau R. (3-65) | 301.41 → **295.84** | 0% | −1.8% | |
| Rapides-Farmers — Gatineau mouth (3-67) | 315.62 → **304.74** | 0% | −3.4% | Gatineau R. easing |
| Carillon — basin terminal (3-60) | 2,037.96 → **1,681.21** | 0% | **−17.5% ⚠ >5%** | **Major drop — Des Joachims cut 628→347 m³/s upstream** |

Two sites exceed the 5% change threshold: Bryson (+7.3%, turbine restart) and Carillon (−17.5%, operational step-change driven by Des Joachims cut). All other sites within ±4%.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: proxy `orrpb_river_flows` (station `temiscaming`); proxy `reservoir_readings` (`reservoir_id=timiskaming`, PSPC cross-check); proxy `orrpb_river_levels` (`mattawa`, `pembroke`, et al.).*

**⚠ CORRECTION from June 28 brief: sub-400 milestone retracted.** June 28 value revised from provisional 400 m³/s → confirmed 467 m³/s. June 29 = 495 m³/s (3rd consecutive day of rise from June 27 local low of 462 m³/s). The sub-500 streak continues unbroken (Day 4); the system never crossed sub-400.

| Metric | Today (June 29) | 7 d ago (June 22) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming outflow — ORRPB (m³/s) | **495** | 761 | −266 | **Day 59 post-primary peak; Day 7 sub-700 (Jun 23–29); Day 5 sub-600 (Jun 25–29); Day 4 sub-500 (Jun 26–29); sub-400 RETRACTED (Jun 28 = 467 revised; Jun 29 = 495 — 3rd consecutive rise)** |
| Témiscaming outflow — PSPC cross-check (m³/s) | **475** | — | — | Delta vs ORRPB = −20 m³/s — within 50 m³/s threshold; no flag |
| Quinze release → into Lake Témiscaming (m³/s) | **307.72** (Jun 29 T19) | ~761 (approx.) | ~−453 | Quinze inflow (308) < Témiscaming outflow (495); lake draining at ~187 m³/s; Lake Témiscaming level −2 cm (179.23→179.21) |
| Mattawa level (m) | **152.17** *(June 29 midnight)* | 152.68 | −51 cm | Jun 28 revised UP from 152.26 → 152.40; Jun 29 = 152.17 (−23 cm from revised Jun 28); declining |
| Pembroke level (m) | **111.37** *(June 29 midnight)* | ~111.63 | ~−26 cm | Flat vs Jun 28 (111.37 = 0 cm); direction: steady; no threshold data |

**Main-stem level snapshot (ORRPB midnight series, from DB `orrpb_river_levels`):**

| Station | June 26 | June 27 | June 28 | June 29 | Δ (Jun 28→29) | Notes |
|---|---|---|---|---|---|---|
| Mattawa | 152.43 | 152.41 | **152.40** | **152.17** | **−23 cm** | Jun 28 revised 152.26→152.40; Jun 29 preliminary |
| Des Joachims | 152.10 | 152.10 | 152.07 | **152.03** | **−4 cm** | Slow decline |
| Otto-Holden | 177.15 | 177.17 | 177.15 | **177.25** | **+10 cm** | Rising — consistent with Des Joachims upstream retention |
| Pembroke | 111.47 | 111.40 | 111.37 | **111.37** | 0 cm | Flat — no threshold data |
| Chenaux | 86.00 | 85.94 | 86.09 | **86.18** | **+9 cm** | Rising — consistent with Carillon holding back water |
| Lake Coulonge | 106.10 | 106.11 | 106.13 | **106.12** | −1 cm | Flat-to-declining; consistent with Vigilance hourly |
| Britannia | 58.34 | 58.29 | 58.18 | **58.09** | −9 cm | Declining |
| Carillon GS | 41.09 | 41.09 | 41.05 | **41.00** | −5 cm | Declining; headpond easing |

**Témiscaming flow series (PSPC, with revision tracking):**

| Date | PSPC value (m³/s) | Revision vs prior brief | Notes |
|---|---|---|---|
| June 23 | 673 | 0 | Confirmed — Day 1 sub-700 |
| June 24 | 608 | 0 | Confirmed |
| June 25 | 551 | 0 | Confirmed — Day 1 sub-600 |
| June 26 | 482 | 0 | Confirmed — Day 1 sub-500 |
| June 27 | 462 | 0 | Confirmed — local low |
| June 28 | 467 | **+67 (was provisional 400 → revised 467)** | **Sub-400 milestone RETRACTED; confirmed 467** |
| **June 29** | **495** | N/A (today, preliminary) | New — UP from 467; 3rd consecutive day rising |

**Milestone bookkeeping:**

| Milestone | Date first crossed | Day count / status (June 29) |
|---|---|---|
| Primary freshet peak (~2,741 m³/s at Témiscaming) | ~May 2 | **Day 59** |
| Sub-1,000 | June 3 (974 m³/s) | Day 27 sub-1,000 |
| Sub-700 | June 23 (673 m³/s) | **Day 7 sub-700** (Jun 23–29) |
| Sub-600 | June 25 (551 m³/s) | **Day 5 sub-600** (Jun 25–29) |
| Sub-500 | June 26 (482 m³/s) | **Day 4 sub-500** (Jun 26–29); Jun 29 = 495 (rising but still <500) |
| **Sub-400** | ~~June 28 (400 m³/s, provisional)~~ | **RETRACTED — Jun 28 revised to 467; sub-400 never crossed** |
| Local low | June 27 (462 m³/s) | Jun 27 = local low; Jun 28 = 467 (+5), Jun 29 = 495 (+28) — 3-day rising trend |
| Mattawa consecutive decline | Jun 28 (new, post-pulse) | Resumed Jun 29 (152.17, −23 cm from revised Jun 28); Day 1 new streak confirmed (Jun 28 revised) |
| Bryson headpond breach Day 1 | May 29 (104.92 m) | **Day 32 (105.46 m; 79 cm above 104.67 m ceiling)** |
| Bryson turbine outage | Jun 15–Jun 29 (15 days) | **Outage ENDED June 29; turbines restarted at 35 m³/s** |
| §15.3.5.1 trigger INACTIVE | ~May 26 | **Day 35** |
| ORRPB weekly cadence | June 23 (first weekly update) | **Next update TOMORROW: June 30 4:00 PM EDT** |

**Reservoir balance (June 28 midnight → June 29 midnight, 13 comparable reservoir IDs):**

| Reservoir | June 28 (m) | June 29 (m) | Δ | Direction | Notes |
|---|---|---|---|---|---|
| Bark Lake | 313.72 | 313.76 | +4 cm | **Rising** | OPG; slight uptick |
| Baskatong | 221.56 | 221.55 | −1 cm | Steady | Largest QC storage; flat |
| Cabonga | 360.36 | 360.34 | −2 cm | Steady | At ±2 cm boundary |
| Des Joachims | 152.07 | 152.03 | **−13 cm** | **Falling** | OPG cut outflow 628→347; upstream level also falling |
| Dozois | 345.01 | 344.96 | **−5 cm** | **Falling** | |
| Kiamika | 267.99 | 267.95 | **−4 cm** | **Falling** | |
| Kipawa | 269.50 | 269.49 | −1 cm | Steady | |
| Lady Evelyn | 289.15 | 289.14 | −1 cm | Steady | |
| Mitchinamecus | 381.43 | 381.43 | 0 cm | Steady | |
| Poisson Blanc | 201.29 | 201.19 | **−10 cm** | **Falling** | EG; notable drop |
| Rapide-7 | 309.05 | 309.03 | −2 cm | Steady | At ±2 cm boundary |
| Timiskaming (PSPC) | 179.23 | 179.21 | −2 cm | Steady | Within noise; outflow (495) > Quinze inflow (308); lake draining |
| Timiskaming Haileybury (WSC) | 179.17 | 179.16 | −1 cm | Steady | |

**Balance (±2 cm = steady; 13 comparable reservoir IDs): 4 falling · 9 steady · 1 rising**

Falling reservoirs: Des Joachims (−13 cm), Poisson Blanc (−10 cm), Dozois (−5 cm), Kiamika (−4 cm). Active retention flag (2+ reservoirs rising >10 cm/day): **not triggered** (only Bark Lake +4 cm). Basin posture: modest net drawdown across secondary reservoirs; normal summer pattern.

---

## Carillon §15.3.5.1 directive check

*Source: proxy `dam_levels` (station 1-3675 Hull dock T19:00 UTC, station 1-2968 Carillon amont T19:00 UTC, June 29).*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (1-3675, June 29 T19 UTC / 3 PM EDT) | **41.39 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 35** (122 cm below 42.61 m; −8 cm vs Jun 28 41.47 m) |
| Carillon amont (1-2968, June 29 T19 UTC) | **40.99 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | **Ceiling NOT in effect — trigger inactive.** |

Hull dock is 122 centimetres below the servitude threshold and drifting lower (−8 cm today from 41.47 m). Carillon amont at 40.99 m also drifting lower (−4 cm from 41.03 m). §15.3.5.1 operating envelope has been inactive for **35 consecutive days**. The ceiling (40.08 m for Carillon amont) is not in force.

Note: Carillon headpond (amont) drifting lower is consistent with the large reduction in releases (2,038→1,681 m³/s today). Less water is being moved through the dam, so the upstream reservoir level is easing.

---

## Reservoir storage (latest_reservoir_readings)

*Source: proxy `latest_reservoir_readings` (June 29 midnight for all). Δ is vs June 28 midnight.*

| Reservoir | June 28 (m) | June 29 (m) | Δ | Flow (m³/s) | Notes |
|---|---|---|---|---|---|
| Baskatong | 221.56 | 221.55 | −1 cm | 196 | Largest QC storage; flat |
| Timiskaming (PSPC) | 179.23 | 179.21 | −2 cm | 475 | Outflow (475) > Quinze inflow (308); lake draining; within noise |
| Dozois | 345.01 | 344.96 | **−5 cm** | 158 | Falling |
| Bark Lake | 313.72 | 313.76 | +4 cm | 16 | Rising (OPG; small but notable) |

Active basin-wide retention flag (2+ reservoirs rising >10 cm/day): **not triggered.** Dozois falling at −5 cm/day is the most notable of the major reservoirs.

---

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast, confirmed HTTP 200 ✓ (130,741 b). **Last Update: 2026-06-23 3:43 PM EDT** (2026-06-23T19:43:00Z). **Next Update: 2026-06-30 4:00 PM EDT** (2026-06-30T20:00:00Z) — 7-day cadence; weekly summer monitoring.*

**Unchanged from prior briefs** (no new ORRPB update — as expected; the June 23 update cycle ends tomorrow). Forecast text:

> *Flows and water levels along the main stem of the Ottawa River are within seasonal values for this time of year. Water levels and flows have increased over the past week following recent rainfall, and are expected to decrease gradually or remain fairly stable over the coming week depending on location. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

No numeric location-specific forecasts for Lac Coulonge, Britannia, or Carillon. **Next update TOMORROW, June 30 4:00 PM EDT.** This will be the seventh consecutive day without an update; tomorrow's forecast will be the first new guidance since June 23.

---

## Anomaly flags

1. **⚠ CORRECTION: sub-400 milestone RETRACTED.** June 28 Témiscaming value revised from provisional 400 m³/s → confirmed 467 m³/s. The "Day 1 sub-400" announced in the June 28 brief and "Day 2 sub-400" in the early June 29 brief were based on a round-number estimate that did not survive revision. The basin never crossed 400 m³/s. The sub-500 streak (Day 4) continues; June 29 = 495 m³/s is the third consecutive rising day from the local low of 462 m³/s on June 27.

2. **⚠ Bryson turbines restarted: Day 1 back online (15-day outage ended June 29).** Total release +7.3% (464.62→498.32 m³/s ⚠ >5% flag). Spill share fell from 100% to 93%. Headpond rose +8 cm to 105.46 m despite higher releases — no drawdown commenced; breach continues at Day 32 (+79 cm above 104.67 m ceiling).

3. **⚠ Carillon −17.5% (2,037.96→1,681.21 m³/s ⚠ >5% flag).** Driven by Des Joachims (OPG) cutting outflow from 628 to 347 m³/s (−45%). This is a large operational step-change mid-cascade; upstream effects are visible at Otto-Holden (+10 cm) and Chenaux (+9 cm). Carillon headpond (41.00 m at ORRPB midnight, −5 cm) and Hull dock (41.39 m, −8 cm) drifting lower in response.

4. **Bryson headpond flat-to-rising — Day 32 breach, 79 cm above ceiling.** Despite turbine restart (+35 m³/s) and higher total releases (+33.7 m³/s), headpond rose +8 cm. This is unexpected and may reflect upstream inflow variability or intraday gauge noise (T17=105.38, T18=105.50, T19=105.46). Without a sustained increase in total throughput, the timeline for returning to the operating range remains unclear.

5. **§15.3.5.1 trigger INACTIVE Day 35** (Hull dock 41.39 m, 122 cm below 42.61 m trigger; −8 cm today). Both Hull dock and Carillon amont drifting lower.

6. **ORRPB forecast next update TOMORROW (June 30 4 PM EDT).** Seven-day cycle ends tomorrow. New forecast may revise "decrease gradually or remain fairly stable" language given the Témiscaming uptick and Bryson/Des Joachims operational changes. Watch for any further-increase language at Lac Coulonge reach.

7. **Vigilance station 1195 direct API remains unreachable** (probed: 502/0b). Proxy data for station 1195 is available and current (June 29 T20 UTC). No data impact, but the direct-API outage has now persisted for a second consecutive day.

---

## Notes

- **Témiscaming rising for 3 days:** The local low was June 27 at 462 m³/s. The June 28 provisional 400 was an anomalous round-number estimate; the confirmed figure (467) and today's reading (495) show the system is actually edging up. This is likely a response to the "recent rainfall" mentioned in the ORRPB's June 23 forecast. The magnitude is modest (+33 m³/s over 2 days), and the system remains firmly in the sub-500 range. Whether this is a brief pulse or the start of a sustained secondary minor uptick will be clearer in tomorrow's data.

- **Bryson turbine restart context:** The 15-day outage (June 15–29) is unusual. The restart at just 35 m³/s turbined (out of ~498 m³/s total) is a token restart — perhaps a test or partial resumption. If operators increase turbined flow toward normal operating levels (the Bryson turbine capacity is ~410 m³/s when the headpond is at full operating level), the total release would increase substantially and the headpond could begin drawing down. No such step-up is visible in today's data.

- **Des Joachims cut and downstream effects:** The ~281 m³/s reduction at Des Joachims is the proximate cause of Carillon's large release reduction today. The effects propagate with travel-time delays: Otto-Holden (above Des Joachims) backed up +10 cm as expected; Chenaux (between Des Joachims and Carillon) rose +9 cm; and the Carillon headpond level fell 5 cm as less water arrived. This is a coordinated operational posture, likely related to downstream conditions (lower Carillon demand, weekend timing, or system balancing).

- **Rapide-2 mid-reach gap:** Rapide-2 (HQ, 238 m³/s) vs Des Joachims (OPG, 347 m³/s) gap has narrowed from ~186 m³/s (June 28) to ~109 m³/s (June 29) as Des Joachims reduced output. The gap likely reflects different operators' scheduling windows rather than hydraulic obstruction. Rapide-2 at 238 m³/s is still notably lower than the ~307 m³/s at Rapide-7 just upstream of Bryson.

- **Guardrail probe results:** Proxy (freshet.xgrunt.com/history): HTTP 200 ✓ (112 b) — healthy. ORRPB forecast: HTTP 200 ✓ (130,741 b) — healthy. Vigilance direct API: 502 Bad Gateway — source unreachable (confirmed; noted as Day 2 outage, no data impact via proxy).
