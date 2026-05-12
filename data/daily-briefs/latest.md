# Daily brief — 2026-05-12

*Generated automatically at 21:30 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

## In plain language

The lake at Fort-Coulonge (Lac Coulonge) continued its slow drop today, sitting at roughly 107.79 metres as of midnight — still in minor flood, about 29 centimetres above the minor flood level. The key news today comes from the river management board's 3:47 PM update: rain is expected to arrive over the central basin starting tomorrow (May 13), and as a result the recession at Lac Coulonge and the stretch down to the Montreal region is forecast to **slow to a halt over the next few days** before resuming gradually later next week. This is a meaningful change from yesterday's forecast, which called for gradual continuing decline. Meanwhile, the northern basin (Mattawa and above) continues to recede slowly — but the board is clear that further rises between Mattawa and Lac Coulonge still cannot be ruled out given high spring runoff vulnerability.

At the basin's terminal dam (Carillon, near Grenville), the headpond sits 40 centimetres above its spring regulatory ceiling for the eighth consecutive day. The ceiling (under the integrated watershed management plan) kicks in when the gauge at Hull is above a fixed trigger level — which it is, by 40 centimetres. The overshoot is slowly shrinking: it peaked at 44 cm on May 10 and has edged down to 40 cm today. The dam's recent release cuts are nudging the level down, but compliance is still far off. No indication from operators or the board that the ceiling exceedance is being actively addressed.

Further up the cascade, the Bryson dam (at the foot of Lac Coulonge) continued passing just over 1,120 cubic metres per second, roughly 79% of it through the spillway. The dam pond held steady at 104.30 metres, well within its normal operating range. The dam at Rapide-2, a mid-cascade station, showed a notable step-down in releases today — down about 17% — though this does not appear to have affected conditions at the property's lake.

Bottom line for property owners: the lake is dropping about 2–4 cm per day but that pace is expected to pause within the next few days due to incoming rain. Exit from minor flood (107.50 m threshold) is currently estimated at 7–15 days depending on how the precipitation plays out — at the slow end if the pause extends, faster if the rain is light and the recession resumes strongly. Watch the next ORRPB update (May 13, 4:00 PM EDT) for revised trajectory.

## TL;DR

Four items today: (1) **ORRPB forecast changed** — Lac Coulonge to Montreal region recession now expected to "slow down and come to a halt over the next few days" due to forecast rain starting May 13, before resuming later next week; previous forecast called for gradual continuing decrease. (2) Carillon §15.3.5.1 directive overshoot at **40 cm** (ORRPB midnight May 12: 40.48 m vs 40.08 m ceiling; Hull dock 43.01 m far above 42.61 m trigger) — day 8 of exceedance, slowly declining from 44 cm peak on May 10. (3) Rapide-2 (3-29) total release **−17.2%** (496 → 411 m³/s) — largest single-site change today, exceeds 5% flag threshold. (4) Première-Chute spill data restored after yesterday's null-data flag (now 438 m³/s, 43.7%).

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: cluster proxy `river_readings` station 1195. Latest: 2026-05-12T20:00 UTC. 24h comparison: 2026-05-11T20:00 UTC. ORRPB midnight values from the conditions table (Water levels at 24:00h).*

| Metric | Value |
|---|---|
| Current level (proxy, 20:00 UTC) | 107.788 m |
| ORRPB midnight May 12 (Fort-Coulonge) | 107.79 m |
| 24h delta (proxy, 20:00 May 12 vs 20:00 May 11) | −3.7 cm |
| ORRPB midnight delta (May 11 → May 12) | −2 cm (107.81 → 107.79 m) |
| Flood state | etat 4 — minor flood |
| Distance above minor threshold (107.500 m) | +28.8 cm |
| Distance below moderate threshold (108.000 m) | −21.2 cm |
| Distance below major threshold (108.500 m) | −71.2 cm |

**Recession trend (ORRPB midnight series):**

| Date | ORRPB midnight (m) | Midnight Δ | Notes |
|---|---|---|---|
| May 5 | 108.25 | | |
| May 6 | 108.18 | −7 cm | |
| May 7 | 108.10 | −8 cm | |
| May 8 | 108.01 | −9 cm | peak recession rate |
| May 9 | 107.92 | −9 cm | peak recession rate |
| May 10 | 107.86 | −6 cm | rain-induced slowdown begins |
| May 11 | 107.81 | −5 cm | |
| **May 12** | **107.79** | **−2 cm** | **recession nearly halted; forecast rain imminent** |

Recession rate has slowed markedly to −2 cm/day midnight-to-midnight. The ORRPB forecast update today confirms the halt is expected to continue over the next few days due to incoming central-basin precipitation. At −2 cm/day, exit from minor flood requires ~14 days; the halt scenario extends this further. Mattawa midnight (154.23 m vs 154.35 m May 11 = −12 cm) shows the northern basin is still actively declining and flushing south.

## Bryson operating posture (HQ open-data via cluster proxy)

*Source: proxy `dam_releases` (site 3-46) and `dam_levels` (stations 1-2964 amont, 1-2965 aval). Today = 2026-05-12T19:00 UTC. Yesterday = 2026-05-11T23:00 UTC.*

| Metric | Today | Yesterday | Δ |
|---|---|---|---|
| Total release (m³/s) | 1,123.44 | 1,138.11 | −14.67 (−1.3%) |
| Turbined (m³/s) | 238.40 | 238.84 | −0.44 (−0.2%) |
| Spilled (m³/s) | 885.04 | 899.28 | −14.24 (−1.6%) |
| Spill share (%) | 78.8% | 79.0% | −0.2 pp |
| Headpond / amont (m) | 104.30 | 104.32 | −2 cm |
| Tailwater / aval (m) | 89.10 | 89.15 | −5 cm |
| Δh — head differential (m) | 15.20 | 15.17 | +0.03 m |

**Headpond operating band (104.20–104.67 m):** headpond at 104.30 m is 10 cm above the lower bound and 37 cm below the upper bound — within band. Headpond has stabilised at 104.30 m (third consecutive day near this level). No >5% threshold breach in any Bryson metric.

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: proxy `dam_releases`. Today = latest per site (2026-05-12T18–19:00 UTC). Yesterday = 2026-05-11T18–19:00 UTC (from prior brief).*

| Site | Total today | Total yest. | Δ% | Spill % today | Spill % yest. |
|---|---|---|---|---|---|
| Première-Chute (3-33) | 1,004.17 | 1,019.13 | −1.5% | 43.7% | null (data gap resolved ✓) |
| Quinze (3-31) | 964.80 | 985.62 | −2.1% | 58.1% | 60.0% |
| Îles (3-32) | 1,078.08 | 1,094.94 | −1.5% | 58.7% | 57.5% |
| Rapide-2 (3-29) | 410.82 | 496.19 | **−17.2% ⚠** | 20.2% | 34.1% |
| Rapide-7 (3-28) | 416.91 | 418.13 | −0.3% | 18.9% | 18.8% |
| Bryson (3-46) | 1,123.44 | 1,141.14 | −1.5% | 78.8% | 79.1% |
| Paugan — Gatineau R. (3-65) | 568.33 | 571.21 | −0.5% | 0.0% | 0.0% |
| Rapides-Farmers — Gatineau (3-67) | 575.62 | 599.51 | −4.0% | 17.8% | 21.1% |
| Carillon — basin terminal (3-60) | 4,651.82 | 4,743.61 | −1.9% | 36.5% | 37.4% |

**Cascade notes:**

- **Rapide-2 (3-29) −17.2% (⚠ exceeds 5% flag):** 496 → 411 m³/s; spill component roughly halved (169 → 83 m³/s, 34.1% → 20.2%). Rapide-7 immediately downstream barely changed (418 → 417 m³/s), so the Rapide-2 reduction is not propagating downstream in the same 24-hour window — likely reflecting a deliberate operational step-down at this site. This is worth watching; if the reduction is sustained it should appear in tomorrow's Rapide-7 figures.

- **Première-Chute (3-33) spill data restored:** Yesterday's null-data flag is resolved — today shows 438.35 m³/s spill (43.7%). This was a data feed gap, not a real posture change.

- **Paugan (3-65):** Remains at 0% spill (posture change established yesterday). All Paugan output is turbined.

- **Carillon −1.9%:** Within normal range. ORRPB daily average at Carillon: 4,926 m³/s (May 11) → 4,669 m³/s (May 12 from ORRPB conditions table).

## Carillon §15.3.5.1 directive check

*Source: proxy `dam_levels` (station 1-2968 Carillon amont, station 1-3675 Hull dock). Latest proxy: 2026-05-12T19:00 UTC. ORRPB midnight (May 12T00:00 UTC) from river conditions table.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (1-3675, proxy 19:00 UTC May 12) | 43.01 m | 42.61 m servitude | **ABOVE — trigger active** (+40 cm) |
| Hull dock (ORRPB midnight May 12) | 43.01 m | 42.61 m servitude | **ABOVE — trigger active** (+40 cm) |
| Carillon amont (1-2968, proxy 19:00 UTC May 12) | 40.48 m | 40.08 m spring-flood ceiling | **OVERSHOOT — 40 cm above ceiling ⚠** |
| Carillon amont (ORRPB midnight May 12) | 40.48 m | 40.08 m spring-flood ceiling | **OVERSHOOT — 40 cm above ceiling ⚠** |

The IWMP §15.3.5.1 spring-flood operating ceiling of 40.08 m remains formally in effect at Carillon (Hull dock 40 cm above the 42.61 m servitude trigger). The headpond is in directive exceedance for the eighth consecutive day.

**24h changes (proxy to proxy, May 11 23:00 → May 12 19:00 UTC):**
- Hull dock: 43.11 → 43.01 m (−10 cm)
- Carillon amont: 40.49 → 40.48 m (−1 cm)

**ORRPB midnight series at Carillon amont:**

| Date | Level (m) | Overshoot vs 40.08 m |
|---|---|---|
| May 5 | 40.50 | 42 cm |
| May 6 | 40.50 | 42 cm |
| May 7 | 40.51 | 43 cm |
| May 8 | 40.51 | 43 cm |
| May 9 | 40.51 | 43 cm |
| May 10 | 40.52 | **44 cm — peak** |
| May 11 | 40.51 | 43 cm |
| May 12 | 40.48 | **40 cm — third consecutive decline** |

The overshoot has declined three consecutive days from the 44 cm peak on May 10 to 40 cm today. The incoming rain forecast may slow or temporarily reverse this improvement if Carillon operators are forced to hold back additional inflow. Compliance (40.08 m) remains 40 cm away.

*See `docs/analysis/Freshet_2026_Complete_Summary.md` § "The Carillon directive enforcement gap" for regulatory context.*

## Reservoir storage (latest_reservoir_readings)

*Source: proxy `latest_reservoir_readings`. Snapshot timestamp: 2026-05-11T00:00 UTC (~45 h before brief generation — within 48 h validity window but same snapshot as yesterday's brief). No day-over-day delta available (data has not refreshed since yesterday).*

| Reservoir | Level (m) | 24h delta | Agency | Note |
|---|---|---|---|---|
| Baskatong | 221.22 | — (no new snapshot) | HQ | Was +13 cm/day in prior brief |
| Dozois | 344.95 | — | HQ | Was +7 cm/day in prior brief |
| Cabonga | 360.19 | — | HQ | Stable |
| Bark Lake | 313.62 | — | OPG | Normal |

Reservoir data has not refreshed since the May 11T00:00 UTC snapshot; delta computation is not possible today. The prior brief's flags (Baskatong +13 cm/day, Dozois +7 cm/day) remain the most recent known state. Watch for snapshot refresh in tomorrow's brief.

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. Last Update: **2026-05-12 3:47 PM EDT** (19:47 UTC). Next Update: **2026-05-13 4:00 PM EDT**.*

**Forecast text changed significantly from prior brief** (May 11 3:26 PM EDT version):

| Region | May 11 3:26 PM version | May 12 3:47 PM version |
|---|---|---|
| Mattawa–Pembroke | "expected to slow down" | "continue to decline slowly" (language strengthened — now unambiguously declining) |
| Lake Coulonge to Montreal | "should continue to **decrease gradually** in all locations over the coming week" | "expected to **slow down and come to a halt** over the next few days, before **resuming gradually later next week**" |
| Cause | (no new forcing mentioned) | "forecast precipitation over the **central** portion of the basin starting tomorrow" |

Full current forecast text (verbatim):

> *Spring runoff in the northern part of the basin is slowly receding but remains high. Between Mattawa and Pembroke, water levels and flows along the Ottawa River continue to decline slowly. With forecast precipitation over the central portion of the basin starting tomorrow, the decline in water levels and flows from Lake Coulonge to the Montreal Region is expected to slow down and come to a halt over the next few days, before resuming gradually later next week. Because large volumes of water continue to come from the northern part of the basin, water levels along the main stem of the river are expected to remain generally high over the next few days. The northern part of the basin will remain vulnerable to heavy rainfall events in the coming weeks; therefore, further increases in water levels from Mattawa to Lake Coulonge due to high spring runoff cannot be ruled out.*

The central distinction from yesterday: Lac Coulonge and downstream are no longer forecast to "decrease gradually" — they are forecast to **halt** before recovering. This is driven by rain expected in the central basin starting May 13.

**ORRPB midnight table (May 12 values from conditions page):**

| Location | May 11 midnight (m) | May 12 midnight (m) | Δ |
|---|---|---|---|
| Mattawa | 154.35 | 154.23 | −12 cm |
| Otto Holden GS | 176.70 | 176.69 | −1 cm |
| Pembroke | 112.82 | 112.80 | −2 cm |
| Fort-Coulonge | 107.81 | 107.79 | −2 cm |
| Britannia (Ottawa) | 59.54 | 59.52 | −2 cm |
| Gatineau / Hull | 43.08 | 43.01 | −7 cm |
| Carillon GS | 40.51 | 40.48 | −3 cm |

Basin-wide recession continuing, but Mattawa's −12 cm midnight-to-midnight is the northern basin flushing southward. Central and lower basin deltas are modest (−2 cm range). Des Joachims +1 cm (150.51 → 150.52 m) — very slight uptick mid-river, could be early signal of the rain arriving.

**ORRPB average daily flows at Carillon:** 5,859 (May 7), 5,543 (May 8), 5,235 (May 9), 5,136 (May 10), 4,926 (May 11), 4,669 (May 12).

## Anomaly flags

1. **ORRPB forecast change — recession halt expected at Lac Coulonge:** Today's 3:47 PM EDT update changes the Lac Coulonge to Montreal forecast from "decrease gradually over the coming week" to "slow down and come to a halt over the next few days, before resuming gradually later next week." Cause: forecast precipitation in the central basin starting tomorrow (May 13). This directly affects the recession timeline for the property gauge and extends the time to exit minor flood beyond prior estimates.

2. **Carillon §15.3.5.1 directive overshoot at 40 cm — day 8:** Hull dock 43.01 m (trigger active, +40 cm above 42.61 m servitude). Carillon amont 40.48 m vs 40.08 m ceiling = 40 cm overshoot. Third consecutive daily decline from 44 cm peak (May 10). The incoming precipitation may slow further improvement if operators are compelled to retain more inflow. Still far from compliance.

3. **Rapide-2 (3-29) −17.2% ⚠:** 496 → 411 m³/s total release; spill roughly halved (169 → 83 m³/s). Exceeds the 5% flag threshold. Rapide-7 downstream shows near-zero change, so the step-down has not propagated yet. Watch tomorrow for downstream signal.

4. **Reservoir snapshot stale — no new delta available:** `latest_reservoir_readings` still at 2026-05-11T00:00 UTC (~45 h old). Day-over-day deltas for Baskatong and others unavailable. Will resolve when the ingester picks up the May 12 snapshot.

5. **ORRPB precipitation claim flagged for follow-up:** ORRPB's forecast references "forecast precipitation over the central portion of the basin starting tomorrow." No window-record or historical-comparison claim made, so no immediate testability flag against `seasonal_window_analysis.py`. Monitor if any operator or board press release characterises the upcoming rain event historically.

## Notes

- **Carillon directive trend and rain interaction:** The overshoot has declined three consecutive days (44 → 43 → 40 cm ORRPB midnight). If the incoming rain forces operators to increase Carillon releases to prevent further headpond rise from inflow, the overshoot could stall or re-expand. Conversely, if operators hold or reduce releases, the headpond may drift further above the ceiling. Either scenario represents a regulatory test — watch the May 13 proxy readings.

- **Forecast halt at Lac Coulonge — implications for property timing:** Prior trajectory (May 12 brief) estimated exit from minor flood in ~10 days at −3 cm/day. Today's −2 cm/day rate and the forecast "halt" push that estimate to 15+ days if the halt materialises. At −6 cm/day recovery (optimistic post-rain) it would take ~5 days from whenever the recession resumes.

- **Mattawa −12 cm midnight-to-midnight:** This is a large overnight drop for Mattawa — larger than the −4 cm from the prior brief, possibly reflecting a data revision or a genuine flush. This volume is moving downstream; its arrival at Pembroke/Fort-Coulonge would be gradual over days.

- **Première-Chute data gap resolved:** Yesterday's flag 4 (null spill data at 3-33) is resolved — today's reading shows 438 m³/s spill (43.7%). Confirms the −1.5% change is real and the earlier null was a feed artifact.
