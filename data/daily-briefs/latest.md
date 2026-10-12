# Daily brief — 2026-10-12

*Generated automatically at 22:20 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB conditions + forecast HTTP 200 ✓. Vigilance ingest fresh (station 1195 T21:00 UTC). V3 posterior: timed out again (exit 124, Day 39); `freshet-forecast.json` carried forward unchanged.*

*Oct 11 retro-checks: All confirmed. Temiscaming prov 278 → final **308 m³/s** (+30 m³/s; D24 confirmed ✓). Des Joachims prov 145 (excluded) → final **334** (exclusion ✓). Otto Holden prov 130 (excluded) → final **308** (exclusion ✓). Chenaux prov 539 (excluded) → final **419** (exclusion ✓). Chats Falls prov 558 (excluded) → final **403** (exclusion ✓). Mattawa prov 152.17 → final **152.26 m** (+9 cm; within artifact range ✓).*

---

## In plain language

### Upstream — the upper basin

The basin remains in steady autumn recession. Lake Timiskaming's outflow finalized at 308 cubic metres per second for October 11 — the 24th consecutive day below 400 m³/s — and today's running figure is near 300 m³/s, consistent with a 25th. Levels at Mattawa and Pembroke are drifting slowly downward with no sign of change, in line with the gentle recession of recent weeks.

Reservoir storage is largely stable: thirteen of the fourteen tracked reservoirs are flat or marginally declining. Lake Timiskaming's pool rose 8 centimetres overnight, reflecting slightly more inflow than outflow during that window. This falls short of the 10-centimetre threshold that signals active basin-wide retention — it is day-to-day operator variation, not a trend.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge is at 105.86 metres — essentially unchanged, fully in normal status, 114 centimetres below the 107-metre pre-alert level. There is nothing of concern at the property reach.

At the Bryson Generating Station dam pond (several kilometres downstream of the lake's south end — not adjacent to the Mansfield properties), operations are unchanged from yesterday: total release, turbine throughput, and spillway share are all flat within one percent. The ORRPB forecast (last published October 6, next update expected tomorrow) calls for stable water levels and flows through the coming week.

---

## TL;DR

Retro ✓: Oct 11 all confirmed — Temiscaming D24 final 308 ✓; all four mid-valley exclusions ✓. Today: Lac Coulonge **105.86 m** (flat; etat 0; 114 cm below pre-alert). Temiscaming D25 in progress (300 prov). Bryson flat. ORRPB update due tomorrow. Day **163** since May 2 peak. Mid-valley Oct 12 provisionals (Des Joachims 144, Otto Holden 129, Chats Falls 566) all failed sanity checks — excluded from headlines.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: cluster proxy `river_readings?station_id=eq.1195` T21:00 UTC Oct 12 + `orrpb_river_levels?station=eq.lake-coulonge`.*

| Metric | Value |
|---|---|
| Current level (Vigilance T21:00 UTC Oct 12) | **105.858 m** |
| ORRPB daily level Oct 12 | 105.85 m |
| ORRPB daily level Oct 11 | 105.85 m |
| 24h delta (Vigilance T21 to T21) | **+0.5 cm** (flat) |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 114 cm below |
| Distance to minor flood (107.50 m) | 164 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)` — T18:00 UTC Oct 12 vs T18:00 UTC Oct 11.*

| Metric | Today (T18 Oct 12) | Yesterday (T18 Oct 11) | Δ |
|---|---|---|---|
| Total release (m³/s) | **317.05** | 317.03 | +0.02 (flat) |
| Turbined (m³/s) | **204.41** | 205.33 | −0.92 (flat) |
| Spilled (m³/s) | **112.65** | 111.70 | +0.95 (flat) |
| Spill share (%) | **35.5%** | 35.2% | +0.3 pp (flat) |
| Headpond / amont (m) | **105.56** | 105.55 | +1 cm |
| Tailwater / aval (m) | **86.67** | 86.65 | +2 cm |
| Δh (head differential, m) | **18.89** | 18.90 | −1 cm |

**Headpond band status:** 105.56 m is 89 cm above the 104.67 m band ceiling — **Day 137** above band. No change >5% in any series. Operations stable.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — T18:00 UTC Oct 12.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 209.01 | 0% |
| Quinze (3-31) | 203.25 | 0.5% |
| Îles (3-32) | 208.11 | 0% |
| Rapide-2 (3-29) | 157.40 | 0% |
| Rapide-7 (3-28) | 155.84 | 0% |
| Bryson (3-46) | **317.05** | **35.5%** |
| Paugan — Gatineau R. (3-65) | 154.69 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 168.82 | 0% |
| Carillon — basin terminal (3-60) | **695.5** | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke, lake-coulonge). All via cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 5) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 11 final (m³/s) | **308** | 315 (Oct 5 final) | −7 | D24 confirmed ✓; **D25 in progress** (300 prov Oct 12) |
| Témiscaming Oct 12 prov (m³/s) | **300** (PSPC T00 UTC) | — | — | Sub-400 D25 in progress; provisional, directional only |
| PSPC cross-check (m³/s) | **300** (timiskaming reservoir flow Oct 12 T00) | — | — | Agrees with Oct 11 ORRPB final (308 vs 300 prov — <50 m³/s gap, normal) |
| Quinze release → into the lake (m³/s) | **203.25** (T18 HQ) | ~315 (Oct 5) | — | Quinze dispatching at autumn low; normal |
| Mattawa level (m) | **152.14** (Oct 12 prov — artifact caution: typically finalizes 5–12 cm higher; Oct 11 final = 152.26 m) | ~152.26 (Oct 5 est.) | ~flat | Direction DOWN; provisional |
| Pembroke level (m) | **110.96** (Oct 12) | ~110.97 (Oct 5 est.) | ~flat | Direction DOWN (marginal); no threshold data |

**Reservoir balance (Oct 11 T00 → Oct 12 T00, 14 reservoirs):** 3 falling · 10 steady · 1 rising (Timiskaming +8 cm). Timiskaming at +8 cm approaches but does not cross the 10-cm active-retention flag threshold. Normal day-to-day variation; no active basin-wide retention.

**Milestone bookkeeping (W40 anchor Oct 4 + Oct 5–12 extension):**

| Milestone | W40 close (Oct 4) | Oct 5 | Oct 6 | Oct 7 | Oct 8 | Oct 9 | Oct 10 | Oct 11 | **Oct 12** |
|---|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 155 | 156 | 157 | 158 | 159 | 160 | 161 | 162 | **163** |
| Bryson amont above band (104.67 m) | 129 | 130 | 131 | 132 | 133 | 134 | 135 | 136 | **137** |
| §15.3.5.1 trigger INACTIVE | 132 | 133 | 134 | 135 | 136 | 137 | 138 | 139 | **140** |
| Temiscaming sub-400 | D17 (316) | D18 (315) | D19 (306) | D20 (315) | D21 (296) | D22 (311) | D23 (286) | D24 (308) | **D25 (300 prov)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T18:00 UTC Oct 12.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.18 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 140** (143 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull at 41.18 m, down 6 cm from Oct 11 T19 (41.24 m).

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00:00 UTC Oct 12.*

| Reservoir | Oct 11 | Oct 12 | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.65 m | **219.63 m** | −2 cm | Normal autumn drainage |
| Témiscaming (PSPC) | 178.72 m | **178.80 m** | **+8 cm** | Consistent with inflow > 300 m³/s outflow this day; single-day variation, not retention trend |
| Dozois | 342.62 m | **342.57 m** | −5 cm | Normal drawdown |
| Bark Lake (OPG) | 313.71 m | **313.71 m** | 0 cm | Steady |

Full balance: 3 falling · 10 steady · 1 rising across 14 tracked reservoirs. No reservoir rising >10 cm/day.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-06 2:57 PM EDT** (2026-10-06T18:57:00Z UTC). **Next Update: 2026-10-13 4:00 PM EDT** (2026-10-13T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Oct 6 publication.** Next update expected tomorrow (Oct 13). Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year resulting from below-normal precipitation across the watershed over recent weeks. Water levels and flows are expected to remain fairly stable in most locations over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false. Mode: `weekly-notice`.

---

## Anomaly flags

1. **Mid-valley Oct 12 provisionals — structural recurring artifact, all sanity checks failed; excluded from headlines.**
   - **Des Joachims 144 m³/s prov** (Oct 11 final 334; −57%): (1) Feasibility: floor (22/24)×144 = 132 m³/s — to reach a 334 final, last 2h would need ~2,424 m³/s avg. Physically impossible. FAILS. (2) Mass balance: Bryson upstream at 317 m³/s; Des Joachims cannot average 144 while receiving 317. FAILS. (3) Level: pool flat at 152.11 m — contradicts rapid storage that would accompany a real 144 m³/s dispatch. FAILS. (4) Downstream: Chenaux 355 m³/s vs Des Joachims 144 — implies 211 m³/s unexplained tributary gain. FAILS.
   - **Otto Holden 129 m³/s prov** (Oct 11 final 308; −58%): Same upstream contradiction; all 4 checks fail.
   - **Chats Falls 566 m³/s prov** (Oct 11 final 403; +40.4%): (1) Feasibility: floor 518 m³/s — plausible if operators increased dispatch, but not confirmed. (2) Mass balance: Bryson (317) + Petawawa (9.6) + small tribs (~15) ≈ 342 expected; 566 implies +224 m³/s from no identified source. FAILS. (3) Level: Des Joachims pool flat at 152.11 m — contradicts rapid drawdown that would accompany 566 dispatch while Des Joachims shows 144. FAILS. (4) Downstream: Carillon 695.5 vs Chats (566) + Gatineau (169) = 735 — 40 m³/s gap, borderline but not decisive.
   - All three in data tables only (§ ORRPB forecast/flow section), marked provisional/excluded. Same pattern confirmed Oct 11 (finals: Des Joachims 334, Otto Holden 308, Chenaux 419, Chats 403 — all exclusions retroactively correct).

2. **Petawawa WSC cross-check (mass balance):** T20:35 UTC Oct 12 = 9.63 m³/s. Confirms minimal mid-valley tributary inflow.

None of the above represent genuine river-state anomalies; all are data-quality flags.

---

## Notes

- **ORRPB flows table (Oct 1–12):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=306, Oct 7=315, Oct 8=296, Oct 9=311, Oct 10=286, Oct 11=308. Oct 12 temiscaming not yet posted; PSPC cross-check = 300 m³/s.
- **Mattawa chronic artifact:** Oct 11 prov 152.17 → final 152.26 m (+9 cm, confirmed within typical range). Oct 12 prov 152.14 m likely understates the final by a similar margin.
- **V3 posterior:** Day 39 consecutive timeout (exit 124, 35s limit). `freshet-forecast.json` unchanged (asof 2026-06-07). Probabilities = 1.0 for all season-resolved thresholds.
- **ORRPB update expected tomorrow Oct 13.** Any new forecast text will be reported in the Oct 13 brief.
- **Carillon T18 vs ORRPB Oct 12 prov:** HQ dam release = 695.5 m³/s vs ORRPB daily prov = 717 m³/s. Timing difference (HQ value is real-time T18; ORRPB accumulates through the day). HQ value used throughout this brief.
