# Daily brief — 2026-10-20

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (119 b probe). ORRPB forecast HTTP 200 ✓ (128 KB) — **updated today Oct 20 3:46 PM EDT**, next update Oct 27. Vigilance 1195: ingest fresh at T20 UTC Oct 20 (105.951 m). V3 posterior: exit 143, Day 47 consecutive timeout; `freshet-forecast.json` restored from prior commit (Oct 19), updated with today's ORRPB forecast text.*

*Oct 19 retro-checks: Oct 19 mid-valley exclusions confirmed ✓ — Des Joachims Oct 19 final = **350 m³/s** (provisional 578 excluded ✓); Otto Holden Oct 19 final = **324 m³/s** (provisional 490 excluded ✓). OPG also revised Oct 18 values after yesterday's brief ran: Des Joachims 374→**491 m³/s** (+31%), Otto Holden 328→**433 m³/s** (+32%) — both sub-400, Témiscaming sub-400 streak D31 unaffected; weekly rollup to reconcile these post-brief OPG revisions.*

---

## In plain language

### Upstream — the upper basin

The upper Ottawa River basin remains in quiet late-autumn recession. Lake Timiskaming's outflow finalized at 299 cubic metres per second for October 19 — thirty-second consecutive day below 400 m³/s, a streak that started September 18. That count is 171 days past the May 2 seasonal peak. Today's outflow reading carries a corrupted data value (negative, clearly impossible) so no same-day number is available, but the reservoir at Timiskaming rose slightly overnight — consistent with inflows in the same 270–310 m³/s range as recent days.

Mattawa dipped 1 centimetre to 152.29 metres and Pembroke fell 2 centimetres to 111.01 metres. Both have been oscillating within a few centimetres of their current values all month. Fourteen tracked reservoirs moved 2 centimetres or less overnight; the pattern is steady, with no sign of unusual inflow or drawdown anywhere in the upper basin.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge rose 1 centimetre to 105.96 metres — fully normal, 104 centimetres below the 107.00-metre pre-alert level. There is nothing to watch at the property level.

Two operational shifts at the downstream dams are worth noting, though neither affects the lake. At the Bryson Generating Station — the dam pond at the downstream end of Lac Coulonge's winding southern reach — Hydro-Québec reversed its recent dispatch mode: turbines went from 128 to 297 cubic metres per second (more than doubling), while spillway flow dropped from 225 to 46 cubic metres per second. Total flow barely changed. This is the inverse of the October 16 near-turbine-shutdown that the past week documented; operators appear to be cycling back to a turbine-preferred mode now that the mid-October precipitation pulse has passed through. At Carillon, the basin's terminal dam near Hawkesbury, releases stepped down 17 percent from 1,159 to 958 cubic metres per second.

ORRPB updated its forecast today (first update since October 13) and dropped the precipitation/possible-rise language. It now calls for levels to "remain fairly stable or slightly decrease" over the coming week — consistent with the basin's current quiet trajectory. The next update is October 27.

---

## TL;DR

Retro ✓: Oct 19 mid-valley finals DJ=350/OH=324 (exclusions correct ✓); Oct 18 OPG post-brief revision DJ 374→491 (+31%), OH 328→433 (+32%) — sub-400 unaffected; rollup to reconcile. **Today:** Lac Coulonge **+1 cm** to **105.96 m (etat 0; 104 cm below pre-alert)**. Bryson posture shift: turbines +132% (128→297 m³/s), spill −79% (225→46 m³/s), spill% 63.7%→13.5%; headpond −8 cm to 105.48 m (Day 145 above band). Carillon −17.4% (1,159→958 m³/s). Hull dock +3 cm to 41.29 m — trigger inactive Day 148. Témiscaming D32 confirmed (Oct 19 final=299); D33 in progress, PSPC today corrupted (−105 m³/s — invalid). ORRPB forecast updated Oct 20: drops precipitation/increase scenario — now "stable or slightly decrease." Day **171** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: Vigilance 1195 via proxy `river_readings` T20 UTC Oct 20 (PRIMARY); ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 20 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 20) | **105.951 m** |
| ORRPB daily Oct 20 | 105.96 m |
| 24h delta (ORRPB daily Oct 19→20) | **+1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 104 cm below |
| Distance to minor flood (107.50 m) | 154 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 20. Yesterday: T19 UTC Oct 19 (from Oct 19 brief).*

| Metric | Today (T19 Oct 20) | Yesterday (T19 Oct 19) | Δ |
|---|---|---|---|
| Total release (m³/s) | **343.17** | 352.80 | −9.63 (−2.7%) |
| Turbined (m³/s) | **296.94** | 127.97 | +168.97 (**+132%**) ⚠ |
| Spilled (m³/s) | **46.23** | 224.82 | −178.59 (**−79.4%**) ⚠ |
| Spill share (%) | **13.5%** | 63.7% | **−50.2 pp** ⚠ |
| Headpond / amont (m) | **105.48** | 105.56 | −8 cm |
| Tailwater / aval (m) | **86.95** | 86.94 | +1 cm |
| Δh (head differential, m) | **18.53** | 18.62 | −9 cm |

Turbined and spilled both exceed the >5% flag threshold. Total release is within 5% (−2.7%). **Headpond band status:** 105.48 m is 81 cm above the 104.67 m band ceiling — **Day 145** above band. Note: mid-day T18 reading was total 371.30 / turbined 211.51 / spilled 159.80 — the spill-to-turbine shift occurred in the T18→T19 window (~2–3 PM EDT Oct 20).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 20.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 202.43 | 0% |
| Quinze (3-31) | 201.82 | 0.5% |
| Îles (3-32) | 206.39 | 0% |
| Rapide-2 (3-29) | 156.71 | 0% |
| Rapide-7 (3-28) | 156.36 | 0% |
| Bryson (3-46) | **343.17** | **13.5%** |
| Paugan — Gatineau R. (3-65) | 162.35 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | ~179 (turbined only) | — |
| Carillon — basin terminal (3-60) | **957.59** | 0.6% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 13) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 19 ORRPB final (m³/s) | **299** | 309 (Oct 13) | −10 | **D32 sub-400 confirmed** |
| Témiscaming Oct 20 PSPC (m³/s) | **−105 (corrupted — invalid)** | — | — | D33 in progress; value unavailable |
| PSPC cross-check Oct 19 vs ORRPB | 295 PSPC / 299 ORRPB | — | — | Agree within 4 ✓ |
| Quinze release → into the lake (m³/s) | **201.82** (T19) | ~200 (Oct 13) | — | Autumn dispatch; steady |
| Mattawa level (m) | **152.29** (Oct 20 daily) | 152.27 (Oct 13) | +2 cm over 7 d | −1 cm from Oct 19 (152.30); direction flat |
| Pembroke level (m) | **111.01** (Oct 20 daily) | 110.98 (Oct 13) | +3 cm over 7 d | −2 cm from Oct 19 (111.03); direction flat |

**Reservoir balance (T00 Oct 19 → T00 Oct 20):**
Kipawa −4 cm · Lady Evelyn −3 cm = 2 **falling** · Rapide-7 +1 · Bark Lake +1 · Poisson Blanc +1 · Quinze 0 · Timiskaming-Haileybury −1 · Baskatong −2 · Mitchinamecus −1 · Kiamika 0 · Dozois −1 = 10 **steady** · Timiskaming +2 · Des Joachims +2 = 2 **rising**. **2 falling · 10 steady · 2 rising.** Normal quiet autumn dispatch pattern.

**Milestone bookkeeping (W42 anchor Oct 18 + Oct 19–20 extension):**

| Milestone | W42 close (Oct 18) | Oct 19 | **Oct 20** |
|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 169 | 170 | **171** |
| Bryson amont above band (104.67 m) | 143 | 144 | **145** |
| §15.3.5.1 trigger INACTIVE | 146 | 147 | **148** |
| Temiscaming sub-400 | D31 (295) | D32 (299) | D33 in progress |

*Oct 18 OPG values revised post-brief: Des Joachims 374→491 m³/s, Otto Holden 328→433 m³/s (both sub-400; streak D31 unaffected). Weekly rollup to reconcile.*

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 20.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.29 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 148** (132 cm below trigger; +3 cm from Oct 19) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Carillon amont unchanged at 41.12 m.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 20.*

| Reservoir | Oct 19 (T00) | Oct 20 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.48 m | **219.46 m** | −2 cm | Steady |
| Témiscaming | 178.76 m | **178.78 m** | +2 cm | Steady; rising pool consistent with continued ~299 m³/s inflow range |
| Dozois | 342.39 m | **342.38 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.81 m | **313.82 m** | +1 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓, 128 KB. **Last Update: 2026-10-20 3:46 PM EDT** (2026-10-20T19:46:00Z UTC). **Next Update: 2026-10-27 4:00 PM EDT** (2026-10-27T20:00:00Z UTC). Cadence: weekly.*

**Updated today** — forecast text changed from the Oct 13 version. Previous: "With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week." New (verbatim):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

Key change: precipitation/increase scenario removed. "Stable or slightly decrease" replaces "increase gradually or remain fairly stable." `further_increases_possible`: false. Mode: `weekly-notice`.

---

## Anomaly flags

1. **Bryson posture shift — turbines +132%, spill −79%** (T19 Oct 20 vs T19 Oct 19). Turbined 128→297 m³/s, spilled 225→46 m³/s; total barely changed (−2.7%). Spill share 63.7%→13.5%. Intraday shift visible: T18 was 372/212/160 (43% spill); by T19 had shifted to 343/297/46 (13.5% spill). Reverses the Oct 16 near-turbine-shutdown that initiated the spill-dominant phase. Physical interpretation: mid-October precipitation runoff has passed through; turbines resume preferred dispatch mode. Headpond −8 cm (105.56→105.48 m) — still Day 145 above band.

2. **Carillon −17.4%** (1,159→958 m³/s). Exceeds >5% flag threshold. Coordinated with Bryson turbine-dominant shift in afternoon EDT. Spill remains negligible (0.6%).

3. **Témiscaming Oct 20 PSPC value corrupted**: −105 m³/s in `orrpb_river_flows` and `reservoir_readings`. A negative value is impossible for main-stem daily flow — this is a data artifact. Timiskaming reservoir level +2 cm T00→T00 confirms continued positive inflow; D33 in progress. Do not report this value as a headline figure.

4. **ORRPB forecast update (Oct 20)**: drops precipitation/rise scenario; now "stable or slightly decrease." `further_increases_possible` flipped to false in `forecast/latest.json`. This is the first forecast change since Oct 13.

5. **OPG Oct 18 post-brief revision**: Des Joachims 374→491 (+31%), Otto Holden 328→433 (+32%). Occurred after yesterday's Oct 19 brief confirmed these as finals. Both remain sub-400 (Témiscaming D31 streak unaffected). Same pattern as the Oct 16 revisions documented in W42 rollup. Weekly rollup (Mon Oct 26) to reconcile.

---

## Notes

- **Oct 19 retro confirmed:** DJ final 350 (provisional 578 excluded ✓), OH final 324 (provisional 490 excluded ✓). No correction required.
- **Oct 20 mid-valley provisionals (DJ 284, OH 258):** changes of −19% and −20% vs Oct 19 finals (350, 324) — below the ≥25%/≥150 m³/s mandatory-check threshold. Reported in data tables only (provisional partial-day). Des Joachims pool +2 cm T00 (rising pool with lower outflow consistent with normal OPG autumn dispatch).
- **Bryson shift context:** Sequence since Oct 14 — Oct 14–15: precipitation pulse, spill rising; Oct 16: turbine near-shutdown (spill 91.5%); Oct 17: partial turbine recovery (spill 63%); Oct 18–19: spill remained 63–64%; Oct 20: turbines fully restored (spill 13.5%). Full reversal cycle in 4 days.
- **Carillon trend:** HQ real-time Oct 20 T19 = 958 m³/s, down from 1,159 T19 Oct 19. ORRPB Oct 20 daily provisional = 975 m³/s (partial-day). Consistent direction.
- **V3 posterior:** Day 47 consecutive timeout (exit 143). `freshet-forecast.json` updated with new ORRPB forecast text and updated timestamps; all other V3 posterior fields restored from prior commit (asof 2026-06-07, season_resolved=false). Dashboard `further_increases_possible` now correctly reflects false.
- **ORRPB Oct 20 mid-valley provisionals (from ORRPB flow table):** Chenaux 542 m³/s, Chats Falls 571 m³/s — these match the declining pattern from Oct 19 finals (499, 539 respectively → up slightly today, but these are partial-day means).
