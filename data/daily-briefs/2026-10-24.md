# Daily brief — 2026-10-24

*Generated automatically at 22:02 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **last updated Oct 20 3:46 PM EDT**, next update Oct 27. Vigilance 1195: proxy ingest fresh T20 UTC Oct 24 (105.993 m). V3 posterior: exit 124 (Day 52 consecutive timeout); `freshet-forecast.json` not updated — keeping last-valid output.*

*Oct 23 retro-checks: **Oct 23 Témiscaming provisional 477 m³/s → final 345 m³/s** — sub-400 streak CONTINUES at D36 (provisional did not finalize >400 as conditionally flagged). Oct 23 Des Joachims excluded 837 → final 403 m³/s ✓. Oct 23 Chenaux excluded 721 → final 486 m³/s ✓. Oct 23 Otto Holden 412 provisional → final 368 m³/s (within normal range, no anomaly). All Oct 23 exclusions correct.*

---

## In plain language

### Upstream — the upper basin

The basin's upper end remains in quiet late-autumn recession. The control structure at Lake Timiskaming — operated by Public Services and Procurement Canada — posted a finalized daily release of 345 cubic metres per second for October 23, continuing an unbroken 36-day run of releases below 400 m³/s. That streak began September 18. Yesterday's provisional reading of 477 m³/s, flagged as a potential streak-ender, finalized 27% lower than the provisional — the streak held. No October 24 figure has posted yet.

The mid-valley gauges were essentially flat. Mattawa held at 152.30 metres — level with the prior day, after a modest multi-day rise earlier in the month. Pembroke eased 1 centimetre. All but one of the 14 tracked storage reservoirs landed within 2 centimetres of their previous-day reading; the Timiskaming reservoir slipped 3 centimetres, consistent with the ongoing controlled outflow exceeding natural inflow at the sub-400 m³/s release rate. Nothing unusual in the upstream picture.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge ticked up 2 centimetres to 106.00 metres per today's daily reading — continuing the gentle creep of roughly 1 centimetre per day seen since October 21. The level remains solidly normal: 100 centimetres below the 107.00-metre pre-alert threshold, 150 centimetres below minor-flood. Etat 0.

The dam pond at the Bryson Generating Station — located well downstream from the property, at the end of Lac Coulonge's winding southern outlet — showed a small operational adjustment: total release rose to 334 m³/s from 322 m³/s, but almost all of the increase went through the spillway (up 46%) rather than the turbines, which were essentially unchanged. The headpond stayed flat at 105.56 metres, so there is no headpond-pressure story here — operators appear to be routing a modest increase in inflow through the spillway while keeping turbine output steady. ORRPB forecast is unchanged: stable or slightly decreasing flows through the coming week. Next update October 27.

---

## TL;DR

**RETRO ✓:** Oct 23 Témiscaming provisional 477 → **final 345 m³/s** — sub-400 streak CONTINUES, **D36 confirmed** (D35 did not break as provisional suggested possible). Oct 23 DJ=837 → final 403; Chenaux=721 → final 486: both exclusions correct. **Today:** Lac Coulonge **+2 cm** to **106.00 m ORRPB daily** (Vigilance T20: 105.993 m; etat 0, 100 cm below pre-alert). Bryson: total +3.7% to **334 m³/s**, spill **+46%** (24.83→36.32 m³/s), spill share **10.9%** (≥5% flag; headpond flat — dispatch adjustment); headpond **105.56 m (Day 149 above band)**. Hull dock T19 41.27 m — trigger INACTIVE **Day 152**. Oct 24 DJ provisional 730 EXCLUDED (fails checks 1,3,4); Chenaux provisional 719 EXCLUDED (fails check 4). Témiscaming Oct 24 not yet posted — sub-400 D37 in progress. Day **175** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 24 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 24 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 24) | **105.993 m** |
| ORRPB daily Oct 24 | 106.00 m (provisional same-day) |
| 24h delta (ORRPB daily Oct 23→24) | **+2 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 100 cm below |
| Distance to minor flood (107.50 m) | 150 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 24. Yesterday: T19 UTC Oct 23.*

| Metric | Today (T19 Oct 24) | Yesterday (T19 Oct 23) | Δ |
|---|---|---|---|
| Total release (m³/s) | **334.33** | 322.33 | +12.00 (+3.7%) |
| Turbined (m³/s) | **298.01** | 297.50 | +0.51 (+0.2%) |
| Spilled (m³/s) | **36.32** | 24.83 | **+11.49 (+46%)** |
| Spill share (%) | **10.9%** | 7.7% | +3.2 pp |
| Headpond / amont (m) | **105.56** | 105.56 | 0 cm |
| Tailwater / aval (m) | **86.90** | 86.86 | +4 cm |
| Δh (head differential, m) | **18.66** | 18.70 | −4 cm |

Spill increased 46%, exceeds 5% flag threshold. Headpond flat at 105.56 m — routine dispatch re-routing, not headpond-pressure response. **Headpond band status:** 105.56 m is 89 cm above the 104.67 m band ceiling — **Day 149** above band (ongoing status).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 24. Yesterday comparison: T18–T19 UTC Oct 23.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **220.90** T19 | 0% | +11 (+5.4%) |
| Quinze (3-31) | **209.13** T19 | 0.5% | flat |
| Îles (3-32) | **211.58** T19 | 0% | flat |
| Rapide-2 (3-29) | **157.55** T18 | 0% | flat |
| Rapide-7 (3-28) | **156.86** T19 | 0% | flat |
| Bryson (3-46) | **334.33** T19 | 10.9% | +12 (+3.7%) |
| Paugan — Gatineau R. (3-65) | **151.28** T19 | 0% | −10 (−6.5%) |
| Rapides-Farmers — Gatineau mouth (3-67) | **169.98** T19 | 0% | −11 (−6.3%) |
| Carillon — basin terminal (3-60) | **937.16** T19 | 0% | +120 (+14.7%) |

Première-Chute +5.4% and Paugan/Rapides-Farmers −6%+: intraday Gatineau tributary dispatch variation. Carillon real-time T19 +14.7%; ORRPB Oct 24 partial-day running mean = 911 m³/s (vs Oct 23 final 852, +7%) — routine dispatch, not a river-level event.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 17) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 23 final (m³/s) | **345** *(Oct 24 not yet posted)* | 309 (Oct 17) | +36 | **D36 confirmed (Oct 23=345); D37 in progress** |
| Timiskaming PSPC cross-check Oct 24 T00 | level 178.73 m (no flow yet) | — | level −3 cm | Level decline consistent with continued sub-400 outflow |
| Quinze release → into the lake (m³/s) | **209.13** (T19) | ~309 (Oct 17) | — | Steady baseload |
| Mattawa level (m) | **152.30** (Oct 24 daily) | 152.19 (Oct 17) | +11 cm | Flat from Oct 23 (152.30); multi-day rise levelled off |
| Pembroke level (m) | **111.05** (Oct 24 daily) | 111.03 (Oct 17) | +2 cm | −1 cm from Oct 23 (111.06); slow drift |

**Reservoir balance (T00 Oct 23 → T00 Oct 24):**
timiskaming −3 cm (falling); all others within ±2 cm. baskatong 0 · cabonga 0 · rapide_7 0 = **3 steady** · bark_lake −1 · kipawa −1 · lady_evelyn −1 · quinze −1 = **4 steady** · des_joachims −1 · dozois −2 · kiamika −2 · mitchinamecus −2 · timiskaming_haileybury −1 = **5 steady** · poisson_blanc +2 = **1 steady**. **1 falling · 13 steady · 0 rising.** Late-autumn equilibrium; Timiskaming decline consistent with controlled outflow at sub-400 rate.

**Milestone bookkeeping (W42 anchor Oct 18 + Oct 19–24 extension):**

| Milestone | W42 close (Oct 18) | Oct 19 | Oct 20 | Oct 21 | Oct 22 | Oct 23 | **Oct 24** |
|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 169 | 170 | 171 | 172 | 173 | 174 | **175** |
| Bryson amont above band (104.67 m) | 143 | 144 | 145 | 146 | 147 | 148 | **149** |
| §15.3.5.1 trigger INACTIVE | 146 | 147 | 148 | 149 | 150 | 151 | **152** |
| Témiscaming sub-400 | D31 (295) | D32 (307) | D33 (312) | D34 (335) | D35 (378) | D36 (345 ✓) | D37? |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 24.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 152** (134 cm below trigger; −1 cm from Oct 23) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 24.*

| Reservoir | Oct 23 (T00) | Oct 24 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.43 m | **219.43 m** | 0 cm | Steady |
| Témiscaming | 178.76 m | **178.73 m** | −3 cm | Falling; consistent with sub-400 PSPC outflow |
| Dozois | 342.30 m | **342.28 m** | −2 cm | Steady decline |
| Bark Lake (OPG) | 313.76 m | **313.75 m** | −1 cm | Steady decline |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-20 3:46 PM EDT** (2026-10-20T19:46:00Z UTC). **Next Update: 2026-10-27 4:00 PM EDT** (2026-10-27T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false. Mode: `weekly-notice`.

---

## Anomaly flags

1. **Bryson spill +46%** (24.83 → 36.32 m³/s): exceeds 5% flag threshold. Total release +3.7% only; turbines flat. Headpond unchanged at 105.56 m — routine dispatch re-routing, no headpond pressure. Spill share 7.7% → 10.9%.

2. **Oct 24 Des Joachims provisional 730 m³/s EXCLUDED (mandatory sanity check).** Oct 23 final = 403 m³/s → +81% ≥ 25%. Check 1 FAIL: floor = (22/24)×730 = 669 m³/s; recent finals 361–406 m³/s — floor nearly double any recent final. Check 3 FAIL: Des Joachims pool T00 Oct 24 = 152.11 m (only −1 cm from Oct 23 = 152.12 m); net outflow at 730 m³/s vs inflow ~400 m³/s would require a pool drop of ~920 cm — impossible vs observed −1 cm. Check 4 FAIL: Chats Falls Oct 24 provisional = 590 m³/s (Oct 23 final = 550, +7%); a real +81% Des Joachims surge would move Chats Falls >7%. Raw value in data tables only.

3. **Oct 24 Chenaux provisional 719 m³/s EXCLUDED (mandatory sanity check).** Oct 23 final = 486 → +48% ≥ 25%. Check 4 FAIL: Chats Falls Oct 24 = 590 m³/s (+7% from Oct 23 final 550); a +48% Chenaux surge would move Chats Falls more than +7%. Raw value excluded.

None beyond above.

---

## Notes

- **Oct 23 Témiscaming provisional resolution:** Yesterday's TL;DR reported 477 m³/s provisional (pass/inconclusive on all sanity checks) with appropriate hedging. Finalized at 345 m³/s — a 27% downward revision, larger than typical PSPC revision range (~10–20%). Streak D36 confirmed. The value passed sanity checks because PSPC Témiscaming is operator-controlled (single-dam release) and large day-to-day swings are plausible operational decisions. The higher-than-normal provisional revision variance at this station is worth tracking.
- **Oct 24 mid-valley:** Des Joachims 730 and Chenaux 719 excluded (same artifact mechanism as Aug 5, Oct 22–23). Otto Holden Oct 24 provisional = 439 m³/s (+19% from Oct 23 final 368) — below 25% threshold, reported without exclusion. Chats Falls Oct 24 provisional = 590 m³/s (+7% from Oct 23 final 550) — below threshold.
- **Carillon dispatch Oct 24:** T19 real-time = 937.16 m³/s; ORRPB Oct 24 partial-day mean = 911 m³/s. Intraday dispatch variation.
- **V3 posterior:** Day 52 consecutive timeout (exit 124). `freshet-forecast.json` not updated — last-valid output retained (asof 2026-06-07).
