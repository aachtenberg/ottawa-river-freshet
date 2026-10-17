# Daily brief — 2026-10-17

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (2494 b probe). ORRPB conditions + forecast HTTP 200 ✓ (forecast unchanged since Oct 13 21:02 UTC — next update Oct 20). Vigilance 1195 ingest stale: latest proxy record T13 UTC Oct 13 (~105h before brief runtime; upstream unverifiable from sandbox — egress-blocked); ORRPB daily Oct 17 = 105.96 m and ORRPB real-time Oct 17 15:00 ET = 105.96 m used as primary and cross-check. V3 posterior: timed out (exit 143, Day 44 consecutive); `freshet-forecast.json` restored from git HEAD unchanged (asof 2026-06-07).*

*Oct 16 retro-checks: Lac Coulonge Oct 16 daily final = **105.95 m** ✓ CONFIRMED (claimed 105.95 m ✓). Témiscaming D29 = **334 m³/s** ✓ CONFIRMED (yesterday marked "D29 in progress" — confirmed sub-400). Mid-valley Oct 16 exclusions validated: Des Joachims final 409 m³/s (provisional 432 — excluded from headlines ✓, within 6%); Otto Holden final 334 m³/s (provisional 429 — excluded ✓; NOTE: 334 is below the calculated floor of 339 from yesterday's sanity check, suggesting either the Oct 16 provisional was not a valid running mean or ORRPB/OPG will revise further — monitoring). Oct 15 Témiscaming minor revision: DB now shows 302 m³/s (was claimed 308, −6 m³/s revision, still D28 sub-400 — streak unaffected).*

---

## In plain language

### Upstream — the upper basin

The upper basin is in steady recession. Lake Timiskaming's daily outflow for October 16 posted at 334 cubic metres per second — now Day 29 in the streak of sub-400 flow that began September 18. October 17 is still accumulating (no daily average finalized yet), and both the ORRPB conditions page and the PSPC snapshot show flows in the 300 m³/s range, consistent with the recent trend. The Mattawa level gauge was reading 152.30 metres as of mid-afternoon, essentially flat from yesterday's 152.31 metres. Pembroke edged down 2 centimetres to 111.01 metres.

Reservoir storage has shifted from the cautious upward nudge seen yesterday to a broadly falling posture today: three reservoirs — Lake Timiskaming, Baskatong, and the Des Joachims pool — all ticked down by a few centimetres overnight. The other four tracked reservoirs were flat. No active basin-wide retention signals; this is normal late-season recession.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge rose 1 centimetre today to 105.96 metres and has now held in the fully normal range for many weeks — still 104 centimetres below the 107.00-metre pre-alert level.

At the Bryson Generating Station — the dam that sits well downstream of Lac Coulonge, after the lake narrows into a winding reach before reaching the dam — operators reversed much of yesterday's posture shift. Yesterday they had nearly shut down the turbines, routing almost all flow through the spillway; today the turbines came back to about 140 cubic metres per second while the spillway dropped from 377 to 226 m³/s. The overall release from the dam also fell about 11 percent to 366 m³/s. The dam pond level held essentially steady at 105.54 metres, still well above the top of its normal operating range.

At the basin's terminal dam, Carillon stepped down meaningfully from the elevated level of yesterday: the real-time release dropped from about 1,630 to 1,148 cubic metres per second, and the Hull dock gauge (the Gatineau-side trigger gauge) fell 10 centimetres to 41.23 metres — still 138 centimetres below the level at which Carillon's spring-flood operating ceiling would apply.

---

## TL;DR

Retro ✓: Lac Coulonge Oct 16 105.95 m ✓; Témiscaming D29 = 334 m³/s ✓; Oct 16 mid-valley exclusions validated (Des Joachims 409, Otto Holden 334 — NOTE: Otto Holden final below yesterday's calculated floor of 339 m³/s, may revise further). Oct 15 Témiscaming revised 308 → 302 (−6; streak unaffected). **Today:** ⚠ **Bryson posture reversal** — turbines back online (35→140 m³/s, +300%); spill back down (377→226 m³/s, −40%); total −11% to 366 m³/s. **Carillon step-down** — 1,631 → 1,148 m³/s real-time (−30%); ORRPB daily Oct 16→17: 1,194→1,148 m³/s (−3.9%). Lac Coulonge +1 cm to **105.96 m (etat 0; 104 cm below pre-alert)**. Témiscaming Oct 16 D29 = 334; Oct 17 provisional ≈307 m³/s (D30 in progress). ORRPB forecast unchanged. Day **168** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 17 daily (primary; Vigilance ingest stale at T13 UTC Oct 13 — ~105h before brief runtime; upstream unverifiable from sandbox). ORRPB real-time conditions 105.96 m at 15:00 ET as cross-check.*

| Metric | Value |
|---|---|
| Current level (ORRPB daily Oct 17) | **105.96 m** |
| ORRPB real-time (Oct 17, 15:00 ET) | 105.96 m |
| ORRPB daily Oct 16 | 105.95 m |
| 24h delta (ORRPB daily Oct 16→17) | **+1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 104 cm below |
| Distance to minor flood (107.50 m) | 154 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 17. Yesterday: T18–T19 UTC Oct 16. ⚠ Posture reversal — turbines back online from near-zero, spill reduced.*

| Metric | Today (T19 Oct 17) | Yesterday (T18–T19 Oct 16) | Δ |
|---|---|---|---|
| Total release (m³/s) | **366.31** | 412.04 | **−45.73 (−11.1%)** |
| Turbined (m³/s) | **140.46** | 35.11 | **+105.35 (+300%)** |
| Spilled (m³/s) | **225.85** | 376.93 | **−151.08 (−40.1%)** |
| Spill share (%) | **61.6%** | 91.5% | **−29.9 pp** |
| Headpond / amont (m) | **105.54** | 105.56 | −2 cm |
| Tailwater / aval (m) | **87.01** | 86.96 | +5 cm |
| Δh (head differential, m) | **18.53** | 18.60 | −7 cm |

**Headpond band status:** 105.54 m is 87 cm above the 104.67 m band ceiling — **Day 142** above band. All metrics exceed the >5% flag threshold.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 17.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 203.24 | 0% |
| Quinze (3-31) | 204.65 | 0.5% |
| Îles (3-32) | 209.79 | 0% |
| Rapide-2 (3-29) | 157.08 | 0% |
| Rapide-7 (3-28) | 155.92 | 0% |
| Bryson (3-46) | **366.31** | **61.6%** |
| Paugan — Gatineau R. (3-65) | 162.93 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 191.81 | 0% |
| Carillon — basin terminal (3-60) | **1,148.04** | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke); ORRPB conditions page real-time (14:00–15:00 ET Oct 17). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 10) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 16 final (m³/s) | **334** | 286 (Oct 10 final) | +48 | **D29 sub-400 confirmed** |
| Témiscaming Oct 17 ORRPB prov (m³/s) | ~307 (conditions 14:00, partial) | — | — | D30 in progress |
| PSPC cross-check Oct 17 T00 (m³/s) | **299** | — | — | Agrees with prov (307) within 50 m³/s ✓ |
| Quinze release → into the lake (m³/s) | **204.65** (T18) | ~202 (Oct 10) | — | Autumn dispatch; steady |
| Mattawa level (m) | **152.30** (ORRPB real-time 14:00) | 152.14 (Oct 10) | +16 cm since Oct 10 | Flat from Oct 16 (152.31); direction slightly down |
| Pembroke level (m) | **111.01** (ORRPB real-time 13:00) | 110.96 (Oct 10) | +5 cm since Oct 10 | −2 cm from Oct 16 (111.03); direction slightly down |

**Reservoir balance (T00 Oct 16 → T00 Oct 17):** Baskatong −4 cm · Témiscaming −3 cm · Des Joachims −2 cm (3 falling) · Dozois −1 cm · Kiamika 0 · Quinze −1 cm · Bark Lake +1 cm (4 steady) · 0 rising. Shift from yesterday's 3-rising / 3-steady to 3-falling / 4-steady — normal late-season recession posture. No active retention.

**Milestone bookkeeping (W41 anchor Oct 11 + Oct 12–17 extension):**

| Milestone | W41 close (Oct 11) | Oct 12 | Oct 13 | Oct 14 | Oct 15 | Oct 16 | **Oct 17** |
|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 162 | 163 | 164 | 165 | 166 | 167 | **168** |
| Bryson amont above band (104.67 m) | 136 | 137 | 138 | 139 | 140 | 141 | **142** |
| §15.3.5.1 trigger INACTIVE | 139 | 140 | 141 | 142 | 143 | 144 | **145** |
| Temiscaming sub-400 | D24 (308) | D25 (304) | D26 (309) | D27 (306) | D28 (302 rev.) | D29 (334) | **D30 in progress** |

*Oct 15 Témiscaming revised from 308 → 302 in DB; D28 confirmed sub-400 regardless.*

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 17.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.23 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 145** (138 cm below trigger; −10 cm from Oct 16) |
| Carillon amont (1-2968) | **41.11 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull falling 10 cm today, consistent with Carillon headpond drawing down.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 17.*

| Reservoir | Oct 16 (T00) | Oct 17 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.55 m | **219.51 m** | **−4 cm** | Falling; recession posture |
| Témiscaming | 178.81 m | **178.78 m** | **−3 cm** | Falling; Oct 16 outflow 334 m³/s confirming draw |
| Dozois | 342.46 m | **342.45 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.77 m | **313.78 m** | +1 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-13 5:02 PM EDT** (2026-10-13T21:02:00Z UTC). **Next Update: 2026-10-20 4:00 PM EDT** (2026-10-20T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: true (precipitation language still current). Mode: `weekly-notice`.

---

## Anomaly flags

1. **⚠ Bryson posture reversal.** Turbines back online (35→140 m³/s, +300%); spill reduced (377→226 m³/s, −40.1%); total −11.1% to 366 m³/s; spill share 91.5%→61.6%. All exceed >5% flag threshold. Second straight day of large posture change at Bryson (yesterday: turbine near-shutdown; today: turbine recovery). Headpond stable (105.54 m, −2 cm). Management cause not stated in public data.

2. **⚠ Carillon step-down.** HQ real-time 1,631 (T18–19 Oct 16) → 1,148 m³/s (T19 Oct 17), −30%. ORRPB daily Oct 16→17: 1,194→1,148 m³/s (−3.9%, not a provisional). Hull dock −10 cm (41.33→41.23); Carillon amont −2 cm (41.13→41.11). No directive issue (trigger inactive at 138 cm below servitude).

3. **Mid-valley provisional discrepancy (data quality note).** `orrpb_river_flows` Oct 17 provisionals: Des Joachims 275 m³/s, Otto Holden 255 m³/s. These are the partial-day running daily means. ORRPB conditions real-time at 15:00 ET: Des Joachims 486 m³/s, Otto Holden 491 m³/s. Downstream response (Chenaux 541, Chats Falls 594 — both elevated vs Oct 16 finals of 490/536) is inconsistent with the provisional daily means. Per sanity check guardrail: Des Joachims provisional −32.5% vs Oct 16 final fails check 4 (downstream elevated, not reduced). Provisionals excluded from headlines; finals expected Oct 18.

None further.

---

## Notes

- **Vigilance ingest staleness:** Latest proxy record for station 1195 is T13 UTC Oct 13 (~105h before brief runtime). ORRPB daily Oct 17 (105.96 m) and real-time (105.96 m at 15:00 ET) used as primary and cross-check. Upstream reachability unverifiable (egress-blocked sandbox). Not an upstream outage claim.
- **Oct 16 Otto Holden floor check failure:** Yesterday's brief calculated the feasibility floor for the Oct 16 provisional (429 m³/s at T19) as ≥339 m³/s minimum final. The posted Oct 16 final is 334 m³/s — 5 m³/s below the floor. This indicates either the Oct 16 provisional was not a valid running mean at T19, or ORRPB/OPG will revise the final upward in the coming days (consistent with W41 rollup observation that OPG revises for 2–3 days). Monitoring for further revisions.
- **Carillon real-time vs daily context:** Yesterday's TL;DR cited HQ real-time 1,631 m³/s (T18–19 Oct 16); the ORRPB daily Oct 16 final is 1,194 m³/s (daily average). Today's HQ real-time at T19 = 1,148 m³/s, matching the ORRPB provisional daily Oct 17 = 1,148 m³/s. No inconsistency — the Oct 16 intraday peak of 1,631 was real, and the daily average settled at 1,194.
- **V3 posterior:** Day 44 consecutive timeout (exit 143, 40-second limit). `freshet-forecast.json` restored from git HEAD (asof 2026-06-07, season_resolved=false, unchanged). Dashboard continues to serve the Jun 7 posterior.
- **ORRPB flows Oct 1–17 (Témiscaming):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=306, Oct 7=315, Oct 8=296, Oct 9=311, Oct 10=286, Oct 11=308, Oct 12=304, Oct 13=309, Oct 14=306, Oct 15=302 (revised), Oct 16=334. Oct 17 not yet posted (~307 partial).
