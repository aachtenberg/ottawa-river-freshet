# Daily brief — 2026-11-23

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200/116b). ORRPB conditions forecast HTTP 200 ✓ (probed: HTTP 200/128664b; forecast unchanged — last update Nov 17; next update Nov 24). Vigilance 1195: proxy ingest fresh T21 UTC Nov 23. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (169 days stale — unchanged). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 23.*

*Nov 22 retro: Témiscaming ORRPB D7 prov 325 → finalized **349 m³/s** (+24 m³/s, within 50 threshold — CONFIRMED sub-400 D7); PSPC T00 Nov 22 revised 363 → 349 m³/s (both sources now 349 m³/s — converged, same as Nov 21 pattern). Mattawa Nov 22 prov 152.19 m → finalized **152.33 m** (+14 cm — ARTIFACT CONFIRMED as predicted). Pembroke Nov 22 prov 111.05 m → finalized **111.08 m** (+3 cm — CONFIRMED ±5 cm).*

---

## In plain language

### Upstream — the upper basin

The upper basin is on Day 205 past the May 2 freshet peak. The outflow from Lake Timiskaming edged down to 335 cubic metres per second in today's provisional ORRPB figure, while the midnight PSPC snapshot sits at 398 m³/s — right at the boundary of the 400 m³/s mark that has defined the sub-400 streak since November 16. The two sources are 63 m³/s apart, which exceeds the alert threshold of 50 m³/s, so today's streak count must be treated as uncertain until tomorrow's finalization. The mid-valley gauge at Pembroke holds essentially flat (a drop of two centimetres), while Mattawa edged up four centimetres from its finalized value — a small genuine rise consistent with the overnight inflow increase described below.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge recorded 105.978 metres at 9 PM UTC on November 23 — essentially unchanged from yesterday, drifting up by less than a centimetre. The lake sits more than a metre below the first alert threshold and remains in a fully normal state. The ORRPB daily figure for today (105.98 m) is flat relative to yesterday.

The main story today is not at Lac Coulonge itself but at the basin-terminal Carillon dam, well downstream of the property. The generating station at Carillon — a large Hydro-Québec facility at the mouth of the Ottawa River — ramped up sharply through the afternoon, reaching a peak of roughly 1,437 cubic metres per second between mid-afternoon and 7 PM UTC (around 2 to 3 PM Eastern), up from about 843 m³/s last evening. This is an HQ dispatch increase — consistent with cold autumn days when electricity demand rises — and is not connected to any flood risk at the property reach. By 8 PM UTC it had already stepped back down to 1,208 m³/s and continues to ease. The generating station at Bryson, reached via the long channel south from Lac Coulonge, made a minor corresponding adjustment: its total release dipped two percent as HQ slightly reduced the spill component (spill dropped from about 54 to 43 cubic metres per second, a 19 percent decrease), while the turbines continued at nearly the same pace. The dam pond behind Bryson rose nine centimetres to 105.58 metres — still roughly 91 centimetres above the normal operating ceiling, a continuing baseline condition now on Day 179.

The ORRPB weekly forecast, last updated Monday November 17, calls for flows to "remain fairly stable or slightly decrease over the coming week." Next update is expected tomorrow (November 24).

---

## TL;DR

**RETRO: Nov 22 Témiscaming ORRPB prov 325 → final 349 m³/s (CONFIRMED sub-400 D7, +24 m³/s within 50 threshold); PSPC T00 363 → 349 (converged). Mattawa prov 152.19 m → final 152.33 m (ARTIFACT CONFIRMED +14 cm, as predicted). Pembroke 111.05 → 111.08 m (CONFIRMED ±5 cm).**
**Today (Day 205):** Lac Coulonge T21 **105.978 m** (+0.8 cm vs T21 Nov 22; etat 0, 102 cm below pre-alert; ORRPB daily prov 105.98 m — flat). Bryson T19: total **341.42 m³/s** (−2.27%), spill **43.23 m³/s** (12.7%, **−19.2% ← flag**), headpond T20 **105.58 m** (+9 cm; Day 179 above band). **⚠ Carillon T20: 1208.09 m³/s (+43.5% vs Nov 22 T19 842.1 m³/s; peak 1437 m³/s at T16–T19; all turbined, 0% spill — real HQ hourly dispatch step-up, not provisional).** §15.3.5.1 trigger INACTIVE **Day 182** (Hull 41.15 m). **⚠ Témiscaming D8 prov: ORRPB daily 335 m³/s, PSPC T00 398 m³/s (gap 63 m³/s — EXCEEDS 50 threshold; PSPC T00 at 398 is 2 m³/s below 400; streak status UNCERTAIN).** Mattawa prov 152.37 m (+4 cm vs finalized 152.33 m — genuine; Pembroke −2 cm essentially flat). Cascade flags: Première-Chute **+17.6%** (321.4 m³/s, spill 7.9%); Quinze **−17.6%** (257.75 m³/s, partially reversing yesterday's step-up); Îles **+7.4%** (336.56 m³/s). **⚠ Des Joachims ORRPB daily 500 m³/s (+28.2% vs yesterday 390; provisional — all 4 sanity checks pass — see cascade section).** Reservoir balance: **3 falling · 9 steady · 2 rising** (Baskatong −3 cm, Dozois −4 cm, Quinze −3 cm falling; Poisson Blanc +3 cm, Timiskaming +4 cm rising). ORRPB weekly forecast unchanged from Nov 17; next update Nov 24.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 23 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 23 provisional (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 23) | **105.978 m** |
| ORRPB daily Nov 23 (provisional) | 105.98 m |
| ORRPB daily Nov 22 (finalized) | 105.98 m |
| 24h delta (Vigilance T21 Nov 23 vs T21 Nov 22) | **+0.8 cm** (105.978 vs 105.970 m) |
| ORRPB daily delta (Nov 22 fin 105.98 → Nov 23 prov 105.98) | 0 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 102 cm below |
| Distance to minor flood (107.50 m) | 152 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 (releases) / T20 (levels) UTC Nov 23. Yesterday: T20 Nov 22 (from prior brief).*

| Metric | Today (T19/T20 Nov 23) | Yesterday (T20 Nov 22) | Δ |
|---|---|---|---|
| Total release (m³/s) | **341.42** | 349.36 | −7.94 (−2.27%) |
| Turbined (m³/s) | **298.19** | 295.84 | +2.35 (+0.79%) |
| Spilled (m³/s) | **43.23** | 53.52 | −10.29 (**−19.2% ← flag**) |
| Spill share (%) | **12.7%** | 15.3% | −2.6 pp |
| Headpond / amont (m) | **105.58** (T20) | 105.49 (T20 Nov 22) | +9 cm |
| Tailwater / aval (m) | **86.92** (T20) | 86.93 (T20 Nov 22) | −1 cm |
| Δh (head differential, m) | **18.66** | 18.56 | +10 cm |

Spill decreased −19.2% (53.52 → 43.23 m³/s): HQ increased turbine output slightly while reducing spill, net total release down 2.3%. Headpond +9 cm = consistent with slightly reduced total release. Headpond 105.58 m = **91 cm above** the 104.67 m band ceiling (Day 179 above band). No other threshold changes.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 23. Carillon: hourly series from `dam_releases` for intraday context.*

| Site | Total (m³/s) | Spill % | Δ vs yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **321.4** T20 | 7.9% (25.42 m³/s) | **+17.6% (flag; spill share 1.7%→7.9%)** |
| Quinze (3-31) | **257.75** T20 | 0.4% (1.01 m³/s) | **−17.6% (flag; stepping back from yesterday's +41.6%)** |
| Îles (3-32) | **336.56** T19 | 0% | **+7.4% (flag)** |
| Rapide-2 (3-29) | **157.18** T20 | 0% | −0.2% (flat) |
| Rapide-7 (3-28) | **158.75** T19 | 0% | +0.7% (flat) |
| Bryson (3-46) | **341.42** T19 | **12.7%** (43.23 m³/s) | −2.3% total; spill −19.2% (flag) |
| Paugan — Gatineau R. (3-65) | **160.75** T19 | 0% | +1.1% |
| Rapides-Farmers — Gatineau mouth (3-67) | **171.86** T19 | 0% | +0.9% |
| **Carillon — basin terminal (3-60)** | **1208.09** T20 | 0% | **+43.5% vs yesterday T19 (842.1 m³/s) — real HQ hourly dispatch; peak 1437 m³/s at T16–T19 UTC** |

### Carillon intraday step-up (HQ hourly telemetry — not provisional)

Carillon peaked at **1,437 m³/s** at T16–T19 UTC Nov 23, up from 843 m³/s last evening. This is confirmed HQ real-time telemetry over 5 consecutive hours; not subject to the provisional-flow guardrail.

| UTC hour | Carillon release (m³/s) |
|---|---|
| Nov 22 T21 | 843 |
| Nov 23 T00 | 937 |
| Nov 23 T13 | 927 |
| Nov 23 T14 | 1,096 |
| Nov 23 T15 | 1,369 |
| Nov 23 T16 | 1,436 |
| Nov 23 T17–T19 | 1,437–1,438 (plateau) |
| Nov 23 T20 | 1,208 (stepping down) |

All flow is turbined (0% spill throughout). Consistent with heating-season HQ demand dispatch; similar step-ups occurred at Quinze/Îles/Première-Chute yesterday. Operational event only — no flood implication at any point in the basin.

### Provisional-flow sanity check — Des Joachims +28.2%

ORRPB daily Nov 23: **500 m³/s** (provisional) vs Nov 22 finalized: **390 m³/s** (+110 m³/s, +28.2%). Guardrail triggered (≥25%). All four checks run:

1. **Feasibility back-out** (~19 h through the day at 500 m³/s): minimum 24-h final even if remaining 5 h return to 390 m³/s = (19×500 + 5×390)/24 ≈ **477 m³/s**. Real increase confirmed at minimum ~22%. ✓ PASS
2. **Mass balance**: OPG dispatch step-up at Des Joachims consistent with coordinated mid-valley generation increase. `latest_reservoir_readings` des_joachims T00 Nov 23 = 624 m³/s outflow (midnight snapshot — predates main intraday step-up; confirms elevated dispatch was underway overnight). Downstream stations all slightly up: Chenaux Nov 23 prov 532 vs 510 (+4.3%), Chats Falls 566 vs 544 (+4%), Britannia 635 vs 607 (+4.6%). ✓ PASS
3. **Pool consistency**: Des Joachims pool T00 Nov 23 = 152.10 m vs T00 Nov 22 = 152.09 m (+1 cm). T00 measurement predates the main intraday step-up visible in Carillon hourly data at T13–T15 UTC. No contradiction. ✓ PASS
4. **Downstream response**: Carillon HQ hourly confirms major step-up (842→1437 m³/s); Chenaux, Chats Falls, Britannia all modestly elevated. Consistent with mid-valley dispatch wave propagating downstream. ✓ PASS

**Result: all 4 checks pass. Des Joachims +28% is real and provisional; minimum confirmed increase ≈ +22%. Report in table only; not headlined as a surge. Final expected in tomorrow's retro.**

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 16) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 23 — ORRPB daily provisional (m³/s) | **335** | 366 (Nov 16 fin) | −31 | D8 provisional sub-400; D1=Nov 16 (366 fin) |
| Témiscaming PSPC cross-check T00 Nov 23 (m³/s) | **398** | — | — | **63 m³/s gap vs ORRPB daily — EXCEEDS 50 threshold; PSPC T00 at 398 is 2 m³/s below 400; streak status UNCERTAIN** |
| Quinze release → into lake (m³/s) | **257.75** (T20) | — | −17.6% vs yesterday | Stepping back from yesterday's +41.6% dispatch step-up |
| Mattawa level (m) | **152.37** (Nov 23 prov) | — | +4 cm vs Nov 22 fin (152.33 m) | Genuine rise; Nov 22 artifact confirmed corrected (+14 cm) |
| Pembroke level (m) | **111.06** (Nov 23) | 111.13 (Nov 16 fin) | −7 cm over 7d | −2 cm vs Nov 22 fin (111.08 m); essentially flat |

**Reservoir balance (T00 Nov 22 → T00 Nov 23):**

| Reservoir | Nov 22 (T00) | Nov 23 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.24 m | **219.21 m** | −3 cm | Falling |
| Dozois | 342.08 m | **342.04 m** | −4 cm | Falling |
| Quinze | 262.94 m | **262.91 m** | −3 cm | Falling |
| Témiscaming | 178.58 m | **178.62 m** | +4 cm | Rising |
| Poisson Blanc | 200.43 m | **200.46 m** | +3 cm | Rising |
| Cabonga | 359.65 m | **359.67 m** | +2 cm | Steady |
| Des Joachims | 152.09 m | **152.10 m** | +1 cm | Steady |
| Bark Lake | 313.50 m | **313.51 m** | +1 cm | Steady |
| Rapide-7 | 308.99 m | **308.97 m** | −2 cm | Steady |
| Mitchinamecus | 379.35 m | **379.33 m** | −2 cm | Steady |
| Kipawa | 268.89 m | **268.87 m** | −2 cm | Steady |
| Kiamika | 266.58 m | **266.57 m** | −1 cm | Steady |
| Lady Evelyn | 289.02 m | **289.02 m** | 0 cm | Steady |
| Timiskaming (Haileybury) | 178.54 m | **178.54 m** | 0 cm | Steady |

**Balance: 3 falling · 9 steady · 2 rising** (Baskatong −3 cm, Dozois −4 cm, Quinze −3 cm falling; Témiscaming +4 cm, Poisson Blanc +3 cm rising; both below 10 cm/day flag). Normal late-season holding posture; no active retention signal.

**Milestone bookkeeping (W46 rollup Nov 15 anchor + corrected daily chain via DB):**

| Milestone | W46 close (Nov 15) | Nov 16 | Nov 17 | Nov 18 | Nov 19 | Nov 20 | Nov 21 | Nov 22 | **Nov 23** |
|---|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 197 | 198 | 199 | 200 | 201 | 202 | 203 | 204 | **205** |
| Bryson amont above band (104.67 m) | 171 | 172 | 173 | 174 | 175 | 176 | 177 | 178 | **179** |
| §15.3.5.1 trigger INACTIVE | 174 | 175 | 176 | 177 | 178 | 179 | 180 | 181 | **182** |
| Témiscaming sub-400 streak (D1=Nov 16) | *above 400 (401 DB final)* | D1: 366 | D2: 375 | D3: 381 | D4: 365 | D5: 358 | D6: 356 | D7: 349 (prov 325→fin 349) | **D8 prov: 335 ORRPB / 398 PSPC T00 (UNCERTAIN — PSPC 398 is 2 m³/s below 400; gap 63 m³/s >50 threshold)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 23.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.15 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 182** (146 cm below trigger) |
| Carillon amont (1-2968) | **41.09 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. The 1,437 m³/s Carillon dispatch peak today is entirely within normal turbine operations; it is an electricity-demand event, not a water-management regulatory event.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 23.*

| Reservoir | Nov 22 (T00) | Nov 23 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.24 m | **219.21 m** | −3 cm | Falling |
| Témiscaming | 178.58 m | **178.62 m** | +4 cm | Rising (below 10 cm/day flag) |
| Dozois | 342.08 m | **342.04 m** | −4 cm | Falling |
| Bark Lake (OPG) | 313.50 m | **313.51 m** | +1 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (probed: HTTP 200/128664b). Last Update: 2026-11-17 2:49 PM EST (2026-11-17T19:49:00Z UTC). Next Update: 2026-11-24 4:00 PM EST (2026-11-24T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` updated with mode=`weekly-notice`, fetched_at updated to 2026-11-23T22:00:00Z.*

**Unchanged from Nov 17 brief (no new ORRPB update expected until Nov 24 — tomorrow):**

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **⚠ Carillon HQ dispatch step-up: T16–T19 plateau at 1,437 m³/s (+70% vs last evening's 843 m³/s; +43.5% vs yesterday's T19 value).** Real HQ hourly telemetry; not provisional. All flow turbined (0% spill). Stepping back down: T20 = 1,208 m³/s. Heating-season demand-response dispatch, consistent with the Nov 22 upper-cascade step-up (Quinze/Îles/Première-Chute). No flood implication.
2. **⚠ Témiscaming PSPC/ORRPB gap 63 m³/s — EXCEEDS 50 threshold.** ORRPB daily prov Nov 23 = 335 m³/s; PSPC T00 Nov 23 = 398 m³/s. Gap = 63 m³/s. PSPC T00 is 2 m³/s below the 400 m³/s threshold — streak status for D8 is UNCERTAIN. Prefer PSPC T00 as stated in operating instructions; flag gap. Expect resolution tomorrow.
3. **Bryson spill −19.2% (53.52 → 43.23 m³/s).** Exceeds 5% flag threshold. HQ reduced spill while slightly increasing turbined output; headpond rose 9 cm (105.49 → 105.58 m). Operational rebalancing within normal parameters.
4. **Première-Chute +17.6% (273.3 → 321.4 m³/s); spill share 1.7%→7.9%.** Spill at Première-Chute went from trace (4.56 m³/s) to moderate (25.42 m³/s), driven by the dispatch step-up. Exceeds 5% flag. In context of coordinated HQ heating-season dispatch, no anomaly.
5. **Quinze −17.6% (312.78 → 257.75 m³/s).** Reversing part of yesterday's +41.6% step-up. Exceeds 5% flag. Normal HQ scheduling.
6. **Îles +7.4% (313.27 → 336.56 m³/s).** Exceeds 5% flag. Same HQ dispatch context.
7. **Des Joachims ORRPB daily provisional +28.2% (390 → 500 m³/s).** All 4 sanity checks pass (see cascade section). Minimum confirmed increase ≈ +22%. Report in table; final expected tomorrow.

No flood-risk implications at any point in the basin. Lac Coulonge etat 0, 102 cm below pre-alert. §15.3.5.1 trigger inactive Day 182.

---

## Notes

- **Day 205** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (169 days stale). `freshet-forecast.json` regenerated without change.
- **Témiscaming streak caution.** The PSPC T00 Nov 23 = 398 m³/s is 2 m³/s below 400. If it finalizes at or above 400, D8 is not sub-400 and the streak started Nov 16 runs only 7 days. If it stays below, D8 extends to 8 days. Tomorrow's retro will resolve this. The ORRPB daily (335) is well below 400 but a 63 m³/s gap means PSPC T00 is preferred per operating instructions.
- **ORRPB next update Nov 24.** Tomorrow's brief will capture the first weekly forecast update since Nov 17.
- **Carillon T20 stepping down.** The 1,208 m³/s at T20 represents a 229 m³/s decline from the T19 plateau of 1,437 m³/s. If the step-down continues through the evening, tomorrow's ORRPB daily for Carillon may be close to yesterday's (869 m³/s) since the daily average will blend the low overnight values with the afternoon peak.
