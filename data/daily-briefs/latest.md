# Daily brief — 2026-10-13

*Generated automatically at 22:10 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB conditions + forecast HTTP 200 ✓ (new forecast published today at 21:02 UTC). Vigilance ingest fresh (station 1195 T13 UTC latest). V3 posterior: timed out again (exit 143, Day 40); `freshet-forecast.json` updated with new forecast JSON, V3 posterior unchanged (asof 2026-06-07).*

*Oct 12 retro-checks: Témiscaming Oct 12 prov 300 → final **302 m³/s** (D25 confirmed ✓). Lac Coulonge Oct 12 Vigilance T21 105.858 m → ORRPB daily final **105.85 m** (confirmed ✓). Mid-valley Oct 12 (Des Joachims 144, Otto Holden 129, Chats Falls 566) all excluded — no headlines to retro-check.*

*CORRECTIONS (uncorrected since Oct 9 brief; flagged by W41 rollup as Human Queue items 1 & 2): **Des Joachims Oct 7 final = 332 m³/s, not 476 as stated in the Oct 9 TL;DR** (ORRPB/OPG revised further after Oct 9 ran; DB settled at 332). **Otto Holden Oct 7 final = 331 m³/s, not 423 as stated in the Oct 9 TL;DR** (same post-run revision; DB settled at 331).*

---

## In plain language

### Upstream — the upper basin

The Ottawa River basin continues in steady late-autumn recession. Lake Timiskaming's outflow finalized at 302 cubic metres per second for October 12 — the 25th consecutive day below 400 m³/s — and October 13 is on course to extend that streak to a 26th day (the figure will be confirmed when ORRPB posts it tomorrow). Levels at Mattawa and Pembroke are drifting fractionally downward, consistent with the gentle recession of recent weeks.

Reservoir storage is essentially unchanged across the basin: 13 of the 14 tracked reservoirs are holding flat, with only Kipawa down 3 centimetres. The basin's storage posture is neutral — operators are neither actively retaining nor passing large volumes.

The afternoon brought a significant operational event at the Carillon Generating Station at the lower end of the river: HQ ramped its dispatch from around 734 cubic metres per second at noon up to 1,257 cubic metres per second by 2 pm Eastern. This is a routine afternoon peaking operation tied to Ontario and Quebec power demand — it draws down the Lac des Deux Montagnes headpond briefly and is not a signal of changing basin hydrology.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge remains at roughly 105.86 metres — essentially unchanged from yesterday — and is fully in normal status, 114 centimetres below the 107-metre pre-alert level. There is nothing of concern at the property.

The most notable development today is in the ORRPB forecast, which was updated this afternoon (its first revision since October 6). The new forecast adds a mention of precipitation expected over the coming days: levels and flows "are expected to increase gradually or remain fairly stable depending on location over the coming week." This is the first precipitation-driven language in the ORRPB forecast in several weeks. It is a moderate signal — levels may tick up, but the forecast text does not indicate significant flooding concern, and Lac Coulonge at 114 centimetres below pre-alert has ample buffer for a modest rise.

At the Bryson Generating Station dam pond (several kilometres downstream of the lake's south end — not adjacent to the Mansfield properties), HQ backed off its turbine throughput significantly overnight: total release dropped from 317 to 283 cubic metres per second, with turbine flow falling 16 percent. Spillway flow held steady, so the change reflects a turbine adjustment rather than a flood-control posture shift.

---

## TL;DR

CORRECTIONS (W41 rollup uncorrected items): **Des Joachims Oct 7 final = 332 m³/s** (not 476 as claimed Oct 9); **Otto Holden Oct 7 final = 331 m³/s** (not 423 as claimed Oct 9). Retro ✓: Oct 12 Témiscaming D25 final 302 ✓. Today: Lac Coulonge **105.86 m** (flat; etat 0; 114 cm below pre-alert). Témiscaming D26 in progress (prov not yet posted; Oct 12 final 302 m³/s). Bryson dispatch step-down: total −10.8% (317→283 m³/s), turbined −16.8%. ORRPB forecast UPDATED (21:02 UTC): first precipitation mention in weeks; "increase gradually or remain fairly stable depending on location." Carillon afternoon peaking ramp 734→991→1257 m³/s (normal operation). Day **164** since May 2 peak. Mid-valley Oct 13 provisionals (Des Joachims 701, Otto Holden 652) all failed sanity checks — excluded.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: cluster proxy `river_readings?station_id=eq.1195` T13 UTC Oct 13 (latest available; routine cutoff 22:00 UTC) + `orrpb_river_levels?station=eq.lake-coulonge`.*

| Metric | Value |
|---|---|
| Current level (Vigilance T13 UTC Oct 13) | **105.863 m** |
| ORRPB daily level Oct 13 | 105.86 m |
| ORRPB daily level Oct 12 | 105.85 m |
| 24h delta (ORRPB daily Oct 12→13) | **+1 cm** (flat) |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 114 cm below |
| Distance to minor flood (107.50 m) | 164 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` — T19 UTC Oct 13 vs T23 UTC Oct 12 (most recent prior-day snapshot).*

| Metric | Today (T19 Oct 13) | Yesterday (T23 Oct 12) | Δ |
|---|---|---|---|
| Total release (m³/s) | **282.87** | 317.49 | **−34.6 (−10.9%)** |
| Turbined (m³/s) | **170.14** | 204.79 | **−34.6 (−16.9%)** |
| Spilled (m³/s) | **112.73** | 112.70 | +0.03 (flat) |
| Spill share (%) | **39.9%** | 35.5% | **+4.4 pp** |
| Headpond / amont (m) | **105.57** | 105.56 | +1 cm |
| Tailwater / aval (m) | **86.68** | 86.67 | +1 cm |
| Δh (head differential, m) | **18.89** | 18.89 | 0 cm |

**Headpond band status:** 105.57 m is 90 cm above the 104.67 m band ceiling — **Day 138** above band. **ANOMALY: total release −10.9%, turbined −16.9% from yesterday — both exceed the >5% flag threshold.** Spill held constant; headpond flat. This is a turbine dispatch step-down, not a flood-management posture change.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 13.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 203.69 | 0% |
| Quinze (3-31) | 203.46 | 0.5% |
| Îles (3-32) | 205.36 | 0% |
| Rapide-2 (3-29) | 157.31 | 0% |
| Rapide-7 (3-28) | 155.39 | 0% |
| Bryson (3-46) | **282.87** | **39.9%** |
| Paugan — Gatineau R. (3-65) | 154.21 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 165.58 | 0% |
| Carillon — basin terminal (3-60) | **1,257** (T18 UTC; peaking ramp in progress) | 0% |

*Note: Carillon T16=734, T17=991, T18=1257 m³/s — an active afternoon peaking ramp. The ORRPB daily running mean for Oct 13 (496 m³/s) covers most of the day before the ramp and understates the evening dispatch; the Oct 13 daily final will be significantly higher than 496. HQ real-time value (1,257) is used in the table.*

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All via cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 6) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 12 final (m³/s) | **302** | 306 (Oct 6 final) | −4 | D25 confirmed ✓; **D26 in progress** (Oct 13 not yet posted) |
| Témiscaming Oct 13 prov (m³/s) | **not posted** (ORRPB); PSPC flow null | — | — | D26 in progress; value expected tomorrow |
| PSPC cross-check Oct 12 (m³/s) | **302** (matches ORRPB final exactly) | — | — | Agreement confirmed |
| Quinze release → into the lake (m³/s) | **203.46** (T19 HQ) | ~306 (Oct 6) | — | Autumn low dispatch; normal |
| Mattawa level (m) | **152.20** (Oct 13 prov — artifact caution: finalizes ~5–12 cm higher; Oct 12 final = 152.25 m) | ~152.26 (Oct 6) | ~flat | Direction DOWN (marginal); provisional |
| Pembroke level (m) | **110.96** (Oct 13) | ~110.97 (Oct 6 est.) | ~flat | Direction flat; no threshold data |

**Reservoir balance (Oct 12 T00 → Oct 13 T00, 14 reservoirs):** 1 falling (Kipawa −3 cm) · 13 steady · 0 rising. Fully neutral — no active retention, no drainage pulse.

**Milestone bookkeeping (W41 anchor Oct 11 + Oct 12–13 extension):**

| Milestone | W41 close (Oct 11) | Oct 12 | **Oct 13** |
|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 162 | 163 | **164** |
| Bryson amont above band (104.67 m) | 136 | 137 | **138** |
| §15.3.5.1 trigger INACTIVE | 139 | 140 | **141** |
| Temiscaming sub-400 | D24 (308) | D25 (302) | **D26 (in progress)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 13.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.33 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 141** (128 cm below trigger) |
| Carillon amont (1-2968) | **41.11 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull at 41.33 m, up 15 cm from Oct 12 T18 (41.18 m). Rise is consistent with reduced Carillon morning dispatch backing up the lower-river pool before the afternoon peaking ramp.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 13.*

| Reservoir | Oct 12 (T00) | Oct 13 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.63 m | **219.62 m** | −1 cm | Normal autumn drainage |
| Témiscaming (WSC gauge) | 178.76 m | **178.76 m** | 0 cm | Flat; PSPC Oct 12 flow final = 302 m³/s |
| Dozois | 342.57 m | **342.56 m** | −1 cm | Normal drawdown |
| Bark Lake (OPG) | 313.71 m | **313.72 m** | +1 cm | Steady |

Full balance: 1 falling (Kipawa −3 cm) · 13 steady across 14 tracked reservoirs. No reservoir rising >10 cm/day.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-13 5:02 PM EDT** (2026-10-13T21:02:00Z UTC). **Next Update: 2026-10-20 4:00 PM EDT** (2026-10-20T20:00:00Z UTC). Cadence: weekly.*

**UPDATED TODAY.** Prior forecast (Oct 6) said: "Water levels and flows are expected to remain fairly stable in most locations over the coming week."

New forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

**Key change:** Added "With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location." This is the first mention of anticipated precipitation-driven increases in the ORRPB forecast in several weeks. The language is hedged ("depending on location"); no flood-state change is implied.

`further_increases_possible`: true. Mode: `weekly-notice`.

---

## Anomaly flags

1. **Bryson turbine dispatch step-down: total −10.9%, turbined −16.9%.**
   Total release 317.49 (Oct 12 T23) → 282.87 (Oct 13 T17-19). Spill held constant (~112.7 m³/s throughout). Headpond flat (+1 cm). This is a deliberate HQ turbine dispatch reduction, not a flood-response posture change. Day-over-day change exceeds the >5% flag threshold for both total and turbined.

2. **ORRPB forecast updated with precipitation language.** First mention of "precipitation forecast over the coming days" and "expected to increase gradually" since at least early October. Level change signal present but no specific gauge forecast posted; not triggering any flood-state concern at current basin levels.

3. **Mid-valley Oct 13 provisionals — structural recurring artifact, all sanity checks failed; excluded from headlines.**
   - **Des Joachims 701 m³/s prov** (Oct 12 final 319; +120%): (1) Feasibility at 22h: floor (22/24)×701 = 642 m³/s; Oct 12 final was 319. A 642+ final would be nearly double any recent day. FAILS. (2) Mass balance: Bryson upstream at 282.87 m³/s; Des Joachims pool would need to draw ~360+ m³/s from storage on top of river inflow. Pool level Oct 12 T00 → Oct 13 T00 = 0 cm change (152.11→152.11). A genuine 700 m³/s sustained daily avg with only 0 cm pool drop is physically implausible. FAILS. (3) Level: Otto Holden pool ROSE +3 cm (177.15→177.18), which contradicts sustained high upstream dispatch. FAILS. (4) Downstream: Chenaux 358 m³/s daily avg vs Des Joachims 701 implies 343 m³/s absorbed into Chenaux storage, yet Chenaux level rose only +2 cm. FAILS.
   - **Otto Holden 652 m³/s prov** (Oct 12 final 304; +115%): Otto Holden pool rose +3 cm (177.15→177.18) — contradicts 652 m³/s dispatch when upstream is ~320 m³/s. All 4 checks fail.
   - Petawawa cross-check (T20:35 UTC): **8.16 m³/s**. No mid-valley tributary contribution.

4. **Carillon afternoon peaking to 1,257 m³/s** — noted for record; not a basin-state anomaly. T16=734, T17=991, T18=1257 m³/s. Normal autumn peak-demand dispatch. ORRPB daily avg (496 m³/s, partial day) significantly understates today's actual dispatch; Oct 13 final will be higher than 668 (Oct 12 final).

---

## Notes

- **CORRECTIONS issued today (W41 Human Queue items 1 & 2):** Des Joachims Oct 7 = 332 m³/s (DB-confirmed; Oct 9 TL;DR stated 476); Otto Holden Oct 7 = 331 m³/s (DB-confirmed; Oct 9 TL;DR stated 423). Both values settled after two rounds of post-publication ORRPB/OPG revisions. These corrections were due in the Oct 10 brief and carried forward uncorrected through Oct 12; issued today from the W41 rollup human-queue flags.
- **Vigilance station 1195 latest record:** T13 UTC Oct 13 (105.863 m). Ingest lag versus the brief's 22:00 UTC runtime is ~9 hours today. Level is stable and ORRPB daily confirms 105.86 m.
- **V3 posterior:** Day 40 consecutive timeout (exit 143, 35s limit). `freshet-forecast.json` updated with new ORRPB forecast data; V3 posterior section unchanged (asof 2026-06-07; all probabilities = 1.0 for season-resolved thresholds).
- **ORRPB flows table (Oct 1–13):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=306, Oct 7=315, Oct 8=296, Oct 9=311, Oct 10=286, Oct 11=308, Oct 12=302. Oct 13 temiscaming not yet posted.
- **Carillon daily final (Oct 13):** Will be substantially higher than the ORRPB partial-day avg (496 m³/s) given the 1257 m³/s peaking ramp running at the brief time. Next brief will retro-check.
