# Daily brief — 2026-05-09

*Generated automatically at 11:13 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

## TL;DR

Two main stories today: (1) Lac Coulonge crossed below the moderate-flood threshold (108.000 m) overnight — now at 107.986 m, transitioning from etat 5 (moderate) to etat 4 (minor flood), exactly as the May 8 brief forecast. (2) The entire upper Ottawa cascade surged simultaneously (+7.5% to +13.6% across all five upstream HQ sites), consistent with preemptive drawdown ahead of ORRPB-forecast weekend rain in the northern basin, while Carillon fell 8.3% — a sharp upstream/downstream divergence. The §15.3.5.1 Carillon overshoot worsened by 3 cm to 44 cm above the spring-flood ceiling, with the headpond rising (+3 cm) while releases were cut.

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: cluster proxy `river_readings` station 1195. Latest observation: 2026-05-09T09:00 UTC.*

| Metric | Value |
|---|---|
| Current level | 107.986 m (at 09:00 UTC) |
| 24h delta | −9.5 cm (108.081 m at 2026-05-08T10:00 UTC) |
| Flood state | etat 4 — **minor flood** (just crossed below moderate threshold) |
| Distance to moderate threshold | 1.4 cm below simoy-niv 108.000 m — **just transitioned** |
| Distance to minor threshold | 48.6 cm above sim-niv 107.500 m |
| Distance to major threshold | 51.4 cm below simaj-niv 108.500 m |

**Threshold reference (station 1195):**

| Code | Level (m) | Meaning |
|---|---|---|
| simaj-niv | 108.500 | Major flood |
| simoy-niv | 108.000 | Moderate flood |
| sim-niv | 107.500 | Minor flood |
| spa-niv | 107.000 | Pre-alert |

**State transition:** The lake crossed below the 108.000 m moderate-flood threshold between the May 8 brief (108.084 m at 09:00 UTC) and today. The May 8 brief predicted this transition around May 9–10 at the ~7.9 cm/day rate; it occurred on schedule. Lake is now in minor flood.

**Recession trend (from prior briefs):** −5.8 cm (May 5), −6.6 cm (May 6), −7.7 cm (May 7), −7.9 cm (May 8), **−9.5 cm (May 9)**. Rate is slightly accelerating. At this pace (≈9–10 cm/day) the lake crosses below minor flood (107.500 m) in ~49 days — no near-term threat to exit minor flood absent a stall from weekend rain. Actual ORRPB gauge reading at Fort-Coulonge: 107.99 m at 03:00 UTC May 9 (consistent with Vigilance).

**Weekend-rain test:** Mattawa gauge (WSC) leveled at 154.37 m for both May 8 and May 9 (ORRPB river table), consistent with the ORRPB forecast that the Mattawa-Pembroke corridor decline is slowing. Rain has not yet visibly affected Vigilance 1195 (lake continues falling), but northern-basin verification is underway.

## Bryson operating posture (HQ open-data via cluster proxy)

*Source: cluster proxy `dam_releases` (site 3-46) and `dam_levels` (stations 1-2964 amont, 1-2965 aval). Today = 2026-05-08T19:00 UTC (latest available, ~16 h lag); yesterday = 2026-05-07T18:00 UTC.*

| Metric | Today | Yesterday | Δ |
|---|---|---|---|
| Total release (m³/s) | 1,224.14 | 1,222.89 | +1.25 (+0.1%) |
| Turbined (m³/s) | 239.12 | 235.73 | +3.39 (+1.4%) |
| Spilled (m³/s) | 985.03 | 987.16 | −2.13 (−0.2%) |
| Spill share (%) | 80.5% | 80.7% | −0.2 pp |
| Headpond / amont (m) | **104.52** | **104.32** | **+0.20 m (+20 cm) ⚠** |
| Tailwater / aval (m) | 89.35 | 89.39 | −0.04 m (−4 cm) |
| Δh — head differential (m) | 15.17 | 14.93 | +0.24 m |

**Headpond operating band (104.20–104.67 m):** headpond at 104.52 m is 32 cm above lower bound and 15 cm below upper bound — within band, no breach. However, the 20 cm rise is notable; if the rise continues at this pace the upper bound would be reached within ~1.5 days.

**Posture note:** Releases are essentially flat (±0.1%), so the 20 cm headpond rise implies inflow to Lac Coulonge increased substantially relative to outflow at Bryson. This is consistent with the ORRPB northern-basin rain narrative beginning to manifest at the Lac Coulonge watershed, or with residual melt inflow from sub-basins between Fort-Coulonge (Vigilance 1195) and the Bryson headpond. No generation-mode change: turbine share remains at ~19.5% of release.

## Main-stem cascade (HQ centrales via cluster proxy, m³/s total release)

*Source: cluster proxy `dam_releases`. Today = 2026-05-08T18–19:00 UTC; yesterday = 2026-05-07T18:00 UTC. Spill % = spilled / total.*

| Site | Total today | Total yest. | Δ% | Spill % today | Spill % yest. |
|---|---|---|---|---|---|
| **Première-Chute (3-33)** | **1,015.03** | 944.26 | **+7.5% ⚠** | 43.5% | 38.4% |
| **Quinze (3-31)** | **973.94** | 899.34 | **+8.3% ⚠** | 58.3% | 54.6% |
| **Îles (3-32)** | **1,084.16** | 998.60 | **+8.6% ⚠** | 55.3% | 41.0% |
| **Rapide-2 (3-29)** | **495.60** | 436.21 | **+13.6% ⚠** | 33.9% | 24.6% |
| **Rapide-7 (3-28)** | **420.09** | 394.86 | **+6.4% ⚠** | 19.0% | 13.5% |
| Bryson (3-46) | 1,224.14 | 1,222.89 | +0.1% | 80.5% | 80.7% |
| Paugan — Gatineau R. (3-65) | 660.28 | 662.78 | −0.4% | 12.2% | 12.1% |
| Rapides-Farmers — Gatineau (3-67) | 648.10 | 667.54 | −2.9% | 27.2% | 29.2% |
| **Carillon — basin terminal (3-60)** | **5,557.25** | **6,060.80** | **−8.3% ⚠** | 44.8% | 48.1% |

**Cascade notes:**

- **All five upper Ottawa sites surged simultaneously (+6.4% to +13.6%):** Première-Chute, Quinze, Îles, Rapide-2, and Rapide-7 all increased substantially in a single 24 h window. This is coordinated basin-wide release behaviour. Given the ORRPB weekend rain forecast for the northern basin, the most likely interpretation is preemptive drawdown to create storage headroom before inflows rise. Spill shares rose sharply at Îles (+14.3 pp, 41→55%) and Rapide-2 (+9.3 pp, 25→34%).

- **Carillon −8.3% simultaneous with upper cascade surge:** The basin terminal is releasing significantly less at the same moment the upstream operators are releasing more. This is an apparent routing-lag effect — water released at upper-cascade sites takes 12–36 h to propagate to Carillon. Expect Carillon throughput to rise over the next 1–2 days as this volume arrives. Alternatively (or additionally), retentive dispatch at mid-cascade sites could be buffering some of the upper-cascade increase.

- **Bryson flat (+0.1%):** No response to upper cascade surge yet. Bryson sits at the foot of Lac Coulonge, downstream of Rapide-7. The upper-cascade pulse has not yet reached Bryson in today's data.

- **Îles spill share +14.3 pp (41→55%):** Largest single-period spill share change in cascade. Combined with the +8.6% total, this site is now passing 599.77 m³/s in spill alone.

## Carillon §15.3.5.1 directive check

*Source: cluster proxy `river_readings` (station 550, Hull dock) and `dam_levels` (station 1-2968, Carillon amont). Hull dock latest: 2026-05-09T11:00 UTC. Carillon amont latest: 2026-05-08T19:00 UTC.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (station 550) | 43.363 m | 42.61 m servitude | **ABOVE — trigger active** (75.3 cm above) |
| Carillon amont (station 1-2968) | 40.52 m | 40.08 m spring-flood ceiling | **OVERSHOOT — 44 cm above ceiling ⚠** |

Hull dock at 43.363 m is 75.3 cm above the 42.61 m servitude — the IWMP §15.3.5.1 spring-flood operating ceiling of 40.08 m at Carillon is formally in effect. Carillon headpond at 40.52 m is 44 cm above that ceiling, constituting a continuing and **worsening** directive exceedance.

**24 h change:** Hull dock fell −21.2 cm (43.575 m → 43.363 m). Carillon amont **rose +3 cm** (40.49 m → 40.52 m). Overshoot went from 41 cm (yesterday's brief) to 44 cm today — direction reversed from yesterday's slight improvement trend (was −1 cm/day). Carillon simultaneously reduced its release by 8.3%; this may explain the headpond rise (inflow not matched by output). The combination of reduced release and rising headpond, when the headpond is already 44 cm above its regulatory ceiling, is anomalous.

*See `docs/analysis/Freshet_2026_Complete_Summary.md` § "The Carillon directive enforcement gap" for regulatory context.*

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings`. Snapshot date: 2026-05-08T00:00 UTC (~35 h ago at brief generation time — within 48 h window). Day-over-day deltas computed against values reported in the 2026-05-08 daily brief (which used the 2026-05-07T00:00 UTC snapshot).*

| Reservoir | Level (m) | 24h delta | Agency | Trend |
|---|---|---|---|---|
| Baskatong | 220.91 | **+8 cm** | HQ | Rising (near 10 cm/day threshold) |
| Dozois | 344.75 | +6 cm | HQ | Rising |
| Cabonga | 360.13 | +1 cm | HQ | Stable |
| Bark Lake | 313.49 | +4 cm | OPG | Rising modestly |

No individual reservoir exceeds 10 cm/day; the "2+ reservoirs rising >10 cm/day" basin-wide active-retention flag is **not triggered**. Baskatong at +8 cm is the closest to threshold. Given the upper-cascade coordinated surge documented above, operators appear to be releasing stored water rather than absorbing inflow at these headwaters — consistent with preemptive drawdown ahead of weekend rain, not a refill posture. The reservoir levels rising despite increased releases above suggests strong continuing inflow at headwater basins.

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. Last Update: **2026-05-08 3:43 PM EDT** (19:43 UTC). Next Update: 2026-05-09 4:15 PM EDT.*

**Forecast updated** since yesterday's brief (which cited the 2026-05-07 4:16 PM EDT version). Text is substantively unchanged but with one notable edit:

| Element | May 8 brief (May 7 4:16 PM EDT) | Today (May 8 3:43 PM EDT) |
|---|---|---|
| Duration qualifier for "generally high" | "over the **next week**" | "over the **next few days**" |
| Northern basin rain language | unchanged | unchanged |
| Mattawa–Pembroke | unchanged | unchanged |
| Lake Coulonge to Montreal | unchanged | unchanged |

The shortening of the "generally high" horizon from "next week" to "next few days" may signal that ORRPB has modestly less conviction in prolonged high levels, though the core messaging (northern rain expected, Mattawa-Pembroke may stall) is unchanged.

**Full current forecast text (2026-05-08 3:43 PM EDT):**

> Spring runoff in the northern part of the basin is expected to rise this weekend due to forecast rain. As a result, the decline in water levels and flows between Mattawa and Pembroke is expected to slow down and may come to a stop, depending on the amount of rain received. Elsewhere along the river from Lake Coulonge to the Montreal Region, water levels and flows should continue to decrease gradually in all locations over the coming week. Because large volumes of water continue to come from the northern part of the basin, water levels along the main stem of the river are expected to remain generally high over the next few days. The northern part of the basin will remain vulnerable to heavy rainfall events in the coming weeks; therefore, further increases in water levels from Mattawa to Lake Coulonge due to high spring runoff cannot be ruled out.

**Mattawa verification:** ORRPB river table shows Mattawa (WSC) flat at 154.37 m for both May 8 and May 9 — the forecast slowing in the Mattawa-Pembroke corridor is already verifying. Pembroke was declining at ~0.03–0.04 m/day earlier in the week and appears to be slowing per ORRPB table (113.12→112.86 over 7 days, rate decelerating).

**ORRPB river gauge snapshot for May 9:**

| Location | Level (m) | Flow (m³/s) | As of (UTC) |
|---|---|---|---|
| Lake Coulonge, Fort-Coulonge | 107.99 | — | 03:00 |
| Carillon amont | 40.48 | 5,549 | 00:00 |
| Britannia (Deschenes) | 59.69 | 3,670 | 02:00 |
| Chats Falls | 75.17 | 3,714 | 03:00 |
| Chenaux | 85.70 | 3,259 | 03:00 |
| Pembroke | 112.86 | — | 00:00 |
| Des Joachims | 150.49 | 2,812 | 03:00 |
| Mattawa | 154.37 | — | 02:00 |
| Otto Holden | 176.64 | 2,589 | 03:00 |

## Anomaly flags

1. **Lac Coulonge etat 5→4 transition (moderate→minor flood):** Lake crossed below the 108.000 m moderate-flood threshold overnight; now at 107.986 m. Transition was forecast in the May 8 brief. Next watch point: minor-flood threshold at 107.500 m, currently 48.6 cm below.

2. **Upper Ottawa cascade coordinated surge (+6.4% to +13.6% across all five sites):** Five HQ centrales (Première-Chute, Quinze, Îles, Rapide-2, Rapide-7) all exceeded the 5% flag threshold in the same 24 h window. This is the largest coordinated release increase observed in this monitoring record. Likely preemptive drawdown ahead of weekend rain forecast. Expect Bryson and Carillon throughput to respond in next 24–48 h.

3. **Îles (3-32) spill share +14.3 pp (41.0→55.3%):** Exceeds 5 pp change threshold. Absolute spill at Îles rose from 409.62 to 599.77 m³/s (+46.4%). This site is now passing more in spill than turbine.

4. **Carillon (3-60) −8.3%:** Exceeds flag threshold. Basin terminal at 5,557.25 m³/s, down from 6,060.80 m³/s. Combined with upstream surge (flag 2 above), this creates a 1–2 day buffer period where the basin terminal is restraining while upstream operators release — watch for Carillon throughput spike in next brief.

5. **Carillon §15.3.5.1 directive overshoot worsened: 41 cm → 44 cm (+3 cm):** Hull dock trigger active (43.363 m >> 42.61 m). Carillon amont rose 3 cm (40.49→40.52 m) while Carillon release fell 8.3%. The combination of reduced output and rising headpond above a binding regulatory ceiling is a directive compliance red flag. See exhibit documentation.

6. **Bryson headpond rose 20 cm** (104.32→104.52 m) with flat releases. Implies inflow to the Bryson forebay increased substantially. Still 15 cm below upper operating band limit (104.67 m). If rising trend continues at this rate, upper band breach could occur within ~36 h.

7. **ORRPB rain forecast partially verifying:** Mattawa flat for 2 consecutive days (May 8-9), confirming the forecast slowdown in the Mattawa-Pembroke corridor. Rain impact on Lac Coulonge watershed not yet visible (lake still declining at 9.5 cm/day). Monitor Vigilance 1195 through May 10–11 for any stall or reversal.

## Notes

- **Cascade routing lag:** Today's sharp upper-cascade surge (+7–14%) coinciding with Carillon's −8.3% is almost certainly a routing-lag artefact. Travel time from Quinze/Îles to Carillon via Rapide-7, Rapide-2, and Bryson (which is itself flat) is estimated at 24–48 h. The May 10 brief should show Bryson responding first, then Carillon.

- **Carillon posture note for case file:** The Carillon operator is simultaneously above its §15.3.5.1 ceiling by 44 cm AND reducing throughput (−8.3%), causing the headpond to rise further above that ceiling. This is the opposite of what a compliance-oriented operator would do — a compliant posture would maximize within-capacity release to draw down the headpond toward 40.08 m. The headpond at 40.52 m remains well within the structural safe range, but the regulatory direction of travel is away from compliance. Record for the case file.

- **Flood state milestone:** The moderate-to-minor flood transition at Lac Coulonge is the first major downward state change since peak flood. Flood state has gone: major (above 108.500) → moderate (108.000–108.500) → **minor (107.500–108.000, today)**. The property is still in minor flood but the trajectory is clearly positive absent rain.

- **Next ORRPB snow-water-equivalent map:** 2026-05-15. The ORRPB May 8 conditions page does not mention a new precipitation update; next forecast update expected 2026-05-09 ~4:15 PM EDT.
