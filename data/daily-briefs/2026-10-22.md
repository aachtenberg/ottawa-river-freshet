# Daily brief — 2026-10-22

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ (128 KB) — **last updated Oct 20 3:46 PM EDT**, next update Oct 27. Vigilance 1195: proxy ingest fresh T20 UTC Oct 22 (105.971 m). V3 posterior: exit 143, Day 49 consecutive timeout; `freshet-forecast.json` updated with current run timestamp, forecast content unchanged.*

*Detached HEAD at session start — 5th consecutive recurrence. Fixed before commit: `git checkout main && git pull origin main`.*

*Oct 21 retro-checks: **Oct 21 Des Joachims provisional 939 m³/s → final 406 m³/s** — exclusion confirmed correct ✓. **Oct 21 Otto Holden provisional 717 m³/s → final 367 m³/s** — exclusion confirmed correct ✓. Both exclusions right call; finals in normal range (+13% / +18% from Oct 20).*

---

## In plain language

### Upstream — the upper basin

The basin is 173 days past the May 2 seasonal peak, and the upper reach continues a very quiet late-autumn recession. The Lake Timiskaming control structure finalized at 335 cubic metres per second for October 21 — thirty-fourth consecutive day below 400 m³/s, confirming a settled low-release posture through mid-October. Pembroke crept up 2 centimetres to 111.05 metres. Mattawa nudged down 4 centimetres to 152.29 metres, reversing part of the brief rise it accumulated over October 18–21. Both mid-valley stations remain solidly in normal autumn range with no flood implications.

Twelve of fourteen tracked reservoirs fell by 1–4 cm today. Two — Lake Timiskaming and the nearby WSC gauge — rose slightly (+4 cm and +1 cm), consistent with the slightly elevated Timiskaming midnight outflow reading; this is normal post-rain settling and not a basin-wide retention signal.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge ticked up 1 centimetre to 105.97 metres — fully normal, 103 centimetres below the 107.00-metre pre-alert threshold. Nothing is happening at the property.

The dam pond at the Bryson Generating Station — located a fair distance downstream from the property reach at the end of Lac Coulonge's long, winding southern outlet — was essentially unchanged overnight. Total release and turbined flow were both flat; spillway passthrough held at about 25 cubic metres per second. The dam pond itself rose 3 centimetres. This is the fourth straight day of very low spill, with the structure running in a turbine-dominant dispatch mode.

The ORRPB forecast remains unchanged from Tuesday's update: stable or slightly decreasing flows through the coming week. Next update October 27.

---

## TL;DR

**RETRO ✓:** Oct 21 DJ=939 provisional → final 406 (+13% from Oct 20, normal); OH=717 → 367 (+18%). Exclusion was correct both days. **Today:** Lac Coulonge **+1 cm** to **105.97 m (etat 0; 103 cm below pre-alert)**. Bryson flat: total +0.6% (321→323 m³/s), spill +4.1% (24→25 m³/s), headpond **+3 cm** to **105.57 m (Day 147 above band)**. Hull dock T19 41.27 m — trigger INACTIVE **Day 150**. Carillon T19 1018 m³/s (+12% vs T19 Oct 21 909) — operational dispatch variation (intraday 945–1124). Première-Chute T18 +61% (206→332 m³/s) — arrival of yesterday's Quinze/Îles ramp. Oct 22 DJ=842 provisional EXCLUDED (fails sanity checks 2, 3, 4). D34 confirmed (Témiscaming Oct 21 PSPC = 335 m³/s); D35 in progress. Day **173** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 22 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 22 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 22) | **105.971 m** |
| ORRPB daily Oct 22 | 105.97 m |
| 24h delta (ORRPB daily Oct 21→22) | **+1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 103 cm below |
| Distance to minor flood (107.50 m) | 153 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 22. Yesterday: T19 UTC Oct 21.*

| Metric | Today (T19 Oct 22) | Yesterday (T19 Oct 21) | Δ |
|---|---|---|---|
| Total release (m³/s) | **322.99** | 321.20 | +1.79 (+0.6%) |
| Turbined (m³/s) | **298.14** | 297.33 | +0.81 (+0.3%) |
| Spilled (m³/s) | **24.85** | 23.87 | +0.98 (+4.1%) |
| Spill share (%) | **7.7%** | 7.4% | +0.3 pp |
| Headpond / amont (m) | **105.57** | 105.54 | +3 cm |
| Tailwater / aval (m) | **86.85** | 86.86 | −1 cm |
| Δh (head differential, m) | **18.72** | 18.68 | +4 cm |

No threshold breaches today. All changes below the 5% flag threshold. **Headpond band status:** 105.57 m is 90 cm above the 104.67 m band ceiling — **Day 147** above band (ongoing status).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 22. Yesterday comparison: T18–T19 UTC Oct 21.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **331.89** T18 | 12.4% | +125 (**+61%**) ⚠ |
| Quinze (3-31) | **232.44** T19 | 0.4% | −127 (−35%) |
| Îles (3-32) | **295.22** T19 | 0% | −52 (−15%) |
| Rapide-2 (3-29) | **157.85** T19 | 0% | −12 (−7%) |
| Rapide-7 (3-28) | **156.56** T18 | 0% | −1 (−0.5%) |
| Bryson (3-46) | **322.99** T19 | 7.7% | +2 (+0.6%) |
| Paugan — Gatineau R. (3-65) | **161.74** T19 | 0% | +0.1 (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **178.73** T19 | 0% | −1 (−0.6%) |
| Carillon — basin terminal (3-60) | **1,018.12** T19 | 0% | +109 (**+12%**) ⚠ |

Quinze and Îles are returning to baseload after yesterday's late-afternoon dispatch ramp (+78%/+68%). Première-Chute's +61% reflects that same ramp arriving downstream today (HQ telemetry, not ORRPB provisional). Carillon intraday dispatch today: T16=1,124 → T17=1,064 → T18=945 → T19=1,018 — operational variation, not a hydrological wave.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 15) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 21 PSPC final (m³/s) | **335** (D34 confirmed ✓) | 307 (Oct 15) | +28 | **D34 confirmed sub-400**; D35 in progress |
| Timiskaming PSPC cross-check Oct 22 T00 (m³/s) | **390** (reservoir_readings) | — | — | Different date from ORRPB daily; no same-day discrepancy flag |
| Quinze release → into lake (m³/s) | **232.44** (T19) | ~206 (Oct 15) | — | Returns to baseload after yesterday's dispatch ramp |
| Mattawa level (m) | **152.29** (Oct 22 daily) | 152.21 (Oct 15) | +8 cm | Fell 4 cm from Oct 21 high (152.33); still above Oct 18 low (152.17) |
| Pembroke level (m) | **111.05** (Oct 22 daily) | 111.00 (Oct 15) | +5 cm | Direction: +2 cm from Oct 21 (111.03); gradual rise |

**Reservoir balance (T00 Oct 21 → T00 Oct 22):**
Baskatong −1 · bark_lake −1 · des_joachims −4 · dozois −3 · kiamika −1 · kipawa −1 · lady_evelyn −1 · mitchinamecus −1 · quinze −2 = **9 falling** · cabonga 0 · poisson_blanc +2 · rapide_7 0 = **3 steady** · timiskaming +4 · timiskaming_haileybury +1 = **2 rising**. **9 falling · 3 steady · 2 rising.** Normal autumn recession pattern; Timiskaming +4 cm likely reflects slightly higher inflows at midnight rather than a retention posture shift.

**Milestone bookkeeping (W42 anchor Oct 18 + Oct 19–22 extension):**

| Milestone | W42 close (Oct 18) | Oct 19 | Oct 20 | Oct 21 | **Oct 22** |
|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 169 | 170 | 171 | 172 | **173** |
| Bryson amont above band (104.67 m) | 143 | 144 | 145 | 146 | **147** |
| §15.3.5.1 trigger INACTIVE | 146 | 147 | 148 | 149 | **150** |
| Témiscaming sub-400 | D31 (295) | D32 (299) | D33 (312 ✓) | D34 (335 ✓) | D35 in progress |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 22.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 150** (134 cm below trigger; −1 cm from Oct 21) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull dock and Carillon amont both flat.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 22.*

| Reservoir | Oct 21 (T00) | Oct 22 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.44 m | **219.43 m** | −1 cm | Steady decline |
| Témiscaming | 178.76 m | **178.80 m** | +4 cm | Slight rise; PSPC flow 390 m³/s at midnight |
| Dozois | 342.35 m | **342.32 m** | −3 cm | Gradual decline |
| Bark Lake (OPG) | 313.80 m | **313.79 m** | −1 cm | Steady decline |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓, 128 KB. **Last Update: 2026-10-20 3:46 PM EDT** (2026-10-20T19:46:00Z UTC). **Next Update: 2026-10-27 4:00 PM EDT** (2026-10-27T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false. Mode: `weekly-notice`.

---

## Anomaly flags

1. **Oct 21 provisional exclusions confirmed correct (retro):** Des Joachims 939 → final 406 (+13% from Oct 20; normal range). Otto Holden 717 → final 367 (+18%; normal range). Both exclusions validated.

2. **Oct 22 Des Joachims provisional 842 m³/s EXCLUDED (mandatory sanity check).** Check 1: floor 702 m³/s (h=20); same mechanism as yesterday (implied remaining = −2,259 m³/s for Oct 21 provisional — physically impossible) may apply. Check 2 FAIL: Timiskaming PSPC = 390 m³/s; Petawawa = 16.7 m³/s; no source for +402 m³/s net pool drawdown implied. Check 3 FAIL: Des Joachims pool fell only 4 cm (T00 Oct 22), but claimed net outflow of ~402 m³/s over 24h would require ~868 km² reservoir area for that drop — implausibly large. Check 4 FAIL: Chenaux shows +55% but Chats Falls shows only +1% (wave would transit Chenaux→Chats Falls in hours). Three of four checks fail. Raw value reported in table only, marked provisional. Chenaux Oct 22 provisional (725 m³/s, +55%) derives from the same upstream chain; also excluded from headlines pending finalization.

3. **Première-Chute T18 +61% (206→332 m³/s; 12.4% spill).** HQ real-time telemetry (not provisional). This is the downstream arrival of yesterday's Quinze/Îles afternoon dispatch ramp (+78%/+68%); expected given cascade travel time.

4. **Carillon HQ T19 +12% (909→1018 m³/s).** Operational dispatch, not a hydrological wave. Today's intraday pattern: T16=1,124 → T17=1,064 → T18=945 → T19=1,018 — typical peak-demand cycling. ORRPB daily Oct 22 shows 1,000 m³/s (partial-day average consistent with this range).

---

## Notes

- **Oct 22 mid-valley sanity check — DJ FAIL:** Des Joachims Oct 22 provisional = 842 m³/s vs Oct 21 final = 406 m³/s (+107%). Check 1: floor=(20/24)×842=702 m³/s; yesterday's Oct 21 provisional at T19 was 939 but finalized to 406, implying remaining-hours flow of −2,259 m³/s — physically impossible; same corruption mechanism may be active today. Check 2 FAIL: Timiskaming PSPC 390 + ~50 m³/s tributaries ≈ 440 total inflow; implied net drawdown 402 m³/s — no identified source. Check 3 FAIL: Des Joachims pool at T00: 152.10 m (−4 cm from 152.14). Net outflow of 402 m³/s × 86,400 s = 34.7 Mm³; would require ~868 km² reservoir surface area for 4 cm drop. Check 4 FAIL: Chenaux 468→725 (+55%) but Chats Falls 560→566 (+1%); wave would arrive at Chats Falls within hours of Chenaux signal. Three clear failures; exclusion applied.
- **V3 posterior:** Day 49 consecutive timeout (exit 143). `freshet-forecast.json` updated with Oct 22 run timestamp; forecast content unchanged.
- **Détached HEAD recurrence (5th):** Git session started in detached HEAD state again. Self-corrected before commit. W42 Human Queue item 2 (pipeline fix investigation) remains unresolved.
- **Carillon dispatch variability:** Intraday range today 945–1,124 m³/s over T16–T19, all turbined. ORRPB Oct 22 daily (partial) = 1,000 m³/s. Not a river-level event.
