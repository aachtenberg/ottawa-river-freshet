# Daily brief — 2026-10-21

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (119 b probe). ORRPB forecast HTTP 200 ✓ (128 KB) — **last updated Oct 20 3:46 PM EDT**, next update Oct 27. Vigilance 1195: ingest fresh at T20 UTC Oct 21 (105.961 m). V3 posterior: exit 143, Day 48 consecutive timeout; `freshet-forecast.json` updated with current run timestamp, forecast content unchanged.*

*Oct 20 retro-checks: Oct 20 Témiscaming PSPC (previously corrupted, −105 m³/s invalid) resolved to **312 m³/s** — D33 sub-400 confirmed ✓. Oct 19 retro previously confirmed (DJ=350, OH=324). Oct 21 mid-valley provisionals (Des Joachims 939 m³/s, Otto Holden 717 m³/s) EXCLUDED from headlines — fail sanity checks 2 (mass balance: Petawawa 17 m³/s; no source) and 4 (downstream: Chenaux +47 m³/s vs claimed +578 at DJ; Carillon flat). See Notes.*

*(Detached HEAD at session start — recurrence. Fixed before commit: `git checkout main && git pull origin main`.)*

---

## In plain language

### Upstream — the upper basin

The Ottawa River basin continues in quiet late-autumn recession, now 172 days past the seasonal peak of May 2. Lake Timiskaming's outflow through the Témiscaming control structure finalized at 312 cubic metres per second for October 20 — this corrects the corrupted reading in yesterday's brief (which showed an invalid negative value) and confirms the thirty-third consecutive day below 400 m³/s. Today's Témiscaming outflow has not yet been published by ORRPB.

Mattawa continued a gradual rise, reaching 152.35 metres provisionally (+5 cm from October 20). This extends a three-day rising trend from the October 18 low of 152.17 — up 18 cm over three days, likely the tail end of the mid-October precipitation pulse draining through the mid-valley reach. Pembroke held flat at 111.02 metres. Fourteen tracked reservoirs showed no significant movement overnight — thirteen steady and one (Des Joachims) down 7 centimetres — fully consistent with quiet autumn operations.

In the afternoon, Hydro-Québec ramped up dispatch at the upper cascade: releases at the Quinze station rose 78 percent (202 to 359 cubic metres per second) and at the Îles station rose 68 percent (206 to 347 m³/s) between noon and 3 PM EDT. The intraday data shows both sites running at baseload levels (~202 m³/s) through midday and then stepping up, consistent with late-afternoon electricity peak demand. There is no downstream response at Carillon yet — this is expected given travel time.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge nudged up 1 centimetre to 105.96 metres — fully normal and 104 centimetres below the 107.00-metre pre-alert level. Nothing to watch at the property.

At the Bryson Generating Station — the dam pond at the downstream end of Lac Coulonge's long winding southern reach, well removed from the properties — Hydro-Québec continued the trend toward turbine-dominant dispatch that began yesterday afternoon. Spillway flow was cut roughly in half again (46 to 24 cubic metres per second), while turbined flow held almost exactly constant. Total release fell 6 percent. The dam pond itself rose 6 centimetres as a result. This continues the reversal of the mid-October spill surge and is now the third straight day of spill reduction.

ORRPB's forecast remains unchanged from Tuesday's update: "fairly stable or slightly decrease" through the week. Next update October 27.

---

## TL;DR

Retro ✓: Oct 20 Témiscaming PSPC (was corrupted −105 m³/s) → D33 confirmed 312 m³/s sub-400 ✓. Oct 21 DJ=939/OH=717 provisional — EXCLUDED (fails sanity checks; see Notes). **Today:** Lac Coulonge **+1 cm** to **105.96 m (etat 0; 104 cm below pre-alert)**. Bryson: spill −48.4% (46→24 m³/s), total −6.4% (343→321 m³/s); headpond **+6 cm** to **105.54 m (Day 146 above band)**. Quinze/Îles afternoon dispatch ramp: +78%/+68% vs yesterday (T19; intraday ramp from ~202 m³/s starting T18; demand dispatch). Carillon T18 −5.0% (958→909 m³/s). Hull dock T19 41.28 m — trigger inactive **Day 149**. Mattawa provisional +5 cm (152.30→152.35, +18 cm since Oct 18). D34 in progress (no Oct 21 Témiscaming provisional yet). Day **172** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: Vigilance 1195 via proxy `river_readings` T20 UTC Oct 21 (PRIMARY); ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 21 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 21) | **105.961 m** |
| ORRPB daily Oct 21 | 105.96 m |
| 24h delta (ORRPB daily Oct 20→21) | **+1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 104 cm below |
| Distance to minor flood (107.50 m) | 154 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 21. Yesterday: T19 UTC Oct 20.*

| Metric | Today (T19 Oct 21) | Yesterday (T19 Oct 20) | Δ |
|---|---|---|---|
| Total release (m³/s) | **321.20** | 343.17 | −21.97 (**−6.4%**) ⚠ |
| Turbined (m³/s) | **297.33** | 296.94 | +0.39 (+0.1%) |
| Spilled (m³/s) | **23.87** | 46.23 | −22.36 (**−48.4%**) ⚠ |
| Spill share (%) | **7.4%** | 13.5% | −6.1 pp |
| Headpond / amont (m) | **105.54** | 105.48 | +6 cm |
| Tailwater / aval (m) | **86.86** | 86.95 | −9 cm |
| Δh (head differential, m) | **18.68** | 18.53 | +15 cm |

Total and spill both exceed the >5% flag threshold. Turbined is essentially unchanged — the spill reduction is not offset by additional turbine dispatch but by a total release decrease. **Headpond band status:** 105.54 m is 87 cm above the 104.67 m band ceiling — **Day 146** above band.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 21.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | 206.40 | 2.5% | +4.0 (+2.0%) |
| Quinze (3-31) | **359.36** | 0.3% | +157.54 (**+78%**) ⚠ |
| Îles (3-32) | **347.22** | 0% | +140.83 (**+68%**) ⚠ |
| Rapide-2 (3-29) | 170.04 | 0% | +13.33 (+8.5%) |
| Rapide-7 (3-28) | 157.15 | 0% | +0.79 (+0.5%) |
| Bryson (3-46) | **321.20** | **7.4%** | −21.97 (−6.4%) |
| Paugan — Gatineau R. (3-65) | 161.68 | 0% | — |
| Rapides-Farmers — Gatineau mouth (3-67) | 179.82 | 0% | — |
| Carillon — basin terminal (3-60) | **909.43** | 0% | −48.16 (−5.0%) ⚠ |

Quinze and Îles increases represent an afternoon peak-demand dispatch ramp (intraday data shows both sites at ~202 m³/s through T17 UTC / noon EDT, stepping up to 330–360 m³/s at T18–T19). No downstream response at Carillon within this snapshot — expected given travel time.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 14) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 20 PSPC final (m³/s) | **312** (D33 confirmed ✓) | 305 (Oct 14) | +7 | **D33 confirmed sub-400** (was corrupted −105 yesterday) |
| Témiscaming Oct 21 (m³/s) | **not yet published** | — | — | D34 in progress |
| Timiskaming reservoir Oct 21 T00 (m) | **178.76** (−2 cm, WSC; flow=null) | — | — | Steady; no PSPC outflow figure today |
| Quinze release → into lake (m³/s) | **359.36** (T19) | ~202 (Oct 14) | — | Afternoon dispatch ramp (see cascade table) |
| Mattawa level (m) | **152.35** (Oct 21 daily, provisional) | ~152.30 (Oct 14) | — | +5 cm from Oct 20; +18 cm from Oct 18 low (152.17) |
| Pembroke level (m) | **111.02** (Oct 21 daily) | ~111.0 (Oct 14) | — | Flat vs Oct 20; direction steady |

**Reservoir balance (T00 Oct 20 → T00 Oct 21):**
Des Joachims −7 cm = 1 **falling** · Baskatong −2 · Timiskaming −2 · Mitchinamecus −2 · Kiamika −2 · Dozois −1 · Bark Lake −1 · Cabonga −1 · Rapide-7 +1 · Lady Evelyn +1 · Poisson Blanc +1 · Quinze 0 · Kipawa 0 · Timiskaming-Haileybury 0 = 13 **steady** · 0 rising. **1 falling · 13 steady · 0 rising.** Quiet autumn recession pattern.

**Milestone bookkeeping (W42 anchor Oct 18 + Oct 19–21 extension):**

| Milestone | W42 close (Oct 18) | Oct 19 | Oct 20 | **Oct 21** |
|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 169 | 170 | 171 | **172** |
| Bryson amont above band (104.67 m) | 143 | 144 | 145 | **146** |
| §15.3.5.1 trigger INACTIVE | 146 | 147 | 148 | **149** |
| Témiscaming sub-400 | D31 (295) | D32 (299) | D33 (312 ✓) | D34 in progress |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 21.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.28 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 149** (133 cm below trigger; −1 cm from Oct 20) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull dock and Carillon amont both flat.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 21.*

| Reservoir | Oct 20 (T00) | Oct 21 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.46 m | **219.44 m** | −2 cm | Steady |
| Témiscaming | 178.78 m | **178.76 m** | −2 cm | Steady; PSPC Oct 20 = 312 m³/s outflow |
| Dozois | 342.37 m | **342.36 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.82 m | **313.81 m** | −1 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓, 128 KB. **Last Update: 2026-10-20 3:46 PM EDT** (2026-10-20T19:46:00Z UTC). **Next Update: 2026-10-27 4:00 PM EDT** (2026-10-27T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from yesterday.** Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false. Mode: `weekly-notice`.

---

## Anomaly flags

1. **Bryson total −6.4%, spill −48.4%** (T19 Oct 21 vs T19 Oct 20). Total 343→321 m³/s, spilled 46→24 m³/s; turbined virtually unchanged. Third consecutive day of spill reduction (Oct 19: 225→46 m³/s; Oct 20: 46 m³/s flat; Oct 21: 46→24 m³/s). Spill share now 7.4%, approaching baseload passthrough levels only. Headpond +6 cm (105.48→105.54 m) — Day 146 above band.

2. **Quinze +78%, Îles +68%** (T19 Oct 21 vs T19 Oct 20). Real-time HQ telemetry (not ORRPB provisional). Intraday profile: both at ~202 m³/s through T17 UTC (noon EDT), stepped up at T18–T19 (2–3 PM EDT). Consistent with afternoon peak-demand dispatch. No downstream signal at Carillon within this snapshot (expected — travel time ~1–2 days to Carillon).

3. **Carillon T18 −5.0%** (909 vs 958 m³/s at T19 Oct 20). At the flag threshold; continuing the directional decline from Oct 20's −17%.

4. **Des Joachims Oct 21 provisional 939 m³/s, Otto Holden 717 m³/s — EXCLUDED from headlines (mandatory sanity check FAIL).** See Notes for check results.

---

## Notes

- **Oct 21 mid-valley provisional sanity check — FAIL:** Des Joachims Oct 21 provisional = 939 m³/s vs Oct 20 final = 361 m³/s (+578, +160%). Otto Holden Oct 21 provisional = 717 m³/s vs Oct 20 final = 310 m³/s (+407, +131%). Check results: (1) Feasibility floor (h≈22h): min final ≥ 860/657 m³/s — feasible in principle but unprecedented vs recent finals. (2) Mass balance FAIL: Petawawa (02KB001) = 17 m³/s; no mid-valley tributary source for +578 m³/s. (3) Downstream FAIL: Chenaux Oct 21 provisional = 544 vs Oct 20 final = 497 (+47, +9.5%); Chats Falls 566 vs 559 (+7); Carillon 967 vs 972 (flat). If Des Joachims were truly averaging 939 m³/s, Chenaux immediately downstream would show far larger increase. Not all four checks passed — figures excluded. Pattern mirrors Aug 5, 2026 incident.
- **Retro confirmed:** Oct 20 Témiscaming PSPC resolved 312 m³/s (D33 ✓). Oct 19 DJ=350/OH=324 confirmed.
- **Mattawa rising trend (provisional):** Oct 18=152.17 → Oct 19=152.22 → Oct 20=152.30 → Oct 21=152.35 (+18 cm in 3 days). Chronic underread caveat applies (provisionals typically 5–12 cm below finals). Likely tail of mid-October precipitation pulse.
- **V3 posterior:** Day 48 consecutive timeout (exit 143). `freshet-forecast.json` updated with Oct 21 run timestamp; forecast content unchanged from Oct 20 (weekly-notice, further_increases_possible=false).
- **Detached HEAD recurrence:** Fourth occurrence (W40, W41, W42 Oct 15, today Oct 21). Self-corrected before commit. W42 Human Queue item 2 unresolved.
