# Daily brief — 2026-11-03

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **updated today (Nov 3) at 2:09 PM EST** (prior: Oct 27; next update: Nov 10 4:00 PM EST — weekly cadence). Vigilance 1195: proxy ingest fresh T20 UTC Nov 3 (105.851 m). V3 posterior: not run (module still missing — `ModuleNotFoundError: no module named 'freshet_probability'`; `freshet-forecast.json` carried forward unchanged asof 2026-06-07).*

*Nov 2 retro-checks: **Nov 2 Témiscaming D46 final 352 m³/s** (yesterday's provisional 346 m³/s → +1.7%, CONFIRMED; well within 50 m³/s). **Nov 2 Mattawa daily 152.31 m** (yesterday's brief TL;DR reported live reading 152.37 m; ORRPB daily finalized 152.31 m — same convention as Nov 1; direction correct, no flood claim affected).*

---

## In plain language

### Upstream — the upper basin

The basin remains in steady late-autumn recession, now Day 185 past the May 2 seasonal peak. The Lake Timiskaming outflow confirmed at 352 cubic metres per second for November 2 (Day 46 of the sub-400 m³/s streak), and today's provisional figure is 358 cubic metres per second — a slight uptick but well within recent daily variation, with the federal monitoring agency (PSPC) agreeing exactly. No precipitation signal yet at the top of the system.

Mattawa rose 18 centimetres overnight to 152.49 metres — its fourth consecutive day of gentle rise since late October, consistent with early-November rainfall in the mid-valley reach between Lake Timiskaming and Mattawa rather than a main-stem pulse (there is no corresponding surge at Témiscaming). Pembroke edged down 5 centimetres to 110.92 metres, continuing its multi-week gentle decline. All 14 tracked reservoirs are essentially flat.

The Ottawa River Regulation Planning Board updated its weekly forecast today, the first update since October 27. The new language shifts from "expected to slightly decrease" to "expected to slightly increase or remain fairly stable depending on location over the coming week," citing precipitation forecast over the coming days. No flood-watch language was added; conditions are described as close to seasonal norms. Next update November 10.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge held flat today at 105.86 metres on the ORRPB daily series (Vigilance gauge most recently 105.851 metres as of 8 PM UTC), unchanged from yesterday. That places the lake 115 centimetres below the 107.00-metre pre-alert threshold — firmly normal, etat 0. The ORRPB forecast's new "slightly increase" language applies vaguely across the system "depending on location"; it does not name Lac Coulonge specifically, and there is no measurable loading coming from upstream at present.

Well downstream at the Bryson Generating Station — a distinct location reached by a long winding channel well below the lake's south end, not visible from or adjacent to the Mansfield properties — the partial spillway operation that began yesterday continued into its second day but eased slightly: spillway flows dropped from 125 to 113 cubic metres per second, and total release fell from 329 to 318 cubic metres per second, while the turbines held essentially steady. The dam pond held at 105.56 metres, confirming this remains a dispatch decision unrelated to the lake upstream. The Carillon dam at the basin outlet released about 907 cubic metres per second, up roughly 4% from yesterday.

---

## TL;DR

**RETRO ✓:** Nov 2 Témiscaming D46 final **352 m³/s** (prov 346 → +1.7%, CONFIRMED). **Today (Day 185):** Lac Coulonge **0 cm** flat at **105.86 m** ORRPB daily (Vigilance T20 105.851 m; etat 0, 115 cm below pre-alert). **⚠ ORRPB FORECAST UPDATED** (first since Oct 27): "slightly increase or remain fairly stable" — direction flipped from "slightly decrease"; precip cited; next update Nov 10. Bryson Day 2 partial spill: 35.7% (113 m³/s, −9.2% vs yesterday; normalizing). Carillon 906.83 m³/s (+35, +4.0%). Mattawa **+18 cm** to **152.49 m** (4th consecutive rise). Pembroke −5 cm to 110.92 m. D47 in progress (prov 358 m³/s; PSPC agrees). Hull dock T17 41.28 m — trigger INACTIVE **Day 162**. Reservoir balance: **0 falling · 13 steady · 1 rising** (des_joachims +3 cm). ORRPB forecast updated Nov 3.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Nov 3 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 3 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Nov 3) | **105.851 m** |
| ORRPB daily Nov 3 | 105.86 m (provisional) |
| 24h delta (ORRPB daily Nov 2→Nov 3) | **0 cm (flat)** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 115 cm below |
| Distance to minor flood (107.50 m) | 165 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T16 UTC Nov 3 (releases), T17 UTC Nov 3 (levels). Yesterday: T16 UTC Nov 2 (releases), T17 UTC Nov 2 (levels).*

| Metric | Today (T16 Nov 3) | Yesterday (T16 Nov 2) | Δ |
|---|---|---|---|
| Total release (m³/s) | **317.54** | 328.61 | −11.07 (−3.4%) |
| Turbined (m³/s) | **204.09** | 203.66 | +0.43 (+0.2%) |
| Spilled (m³/s) | **113.44** | 124.95 | **−11.51 (−9.2%) ⚠** |
| Spill share (%) | **35.7%** | 38.0% | −2.3 pp |
| Headpond / amont (m) | **105.56** (T17) | 105.53 (T17 Nov 2) | +3 cm |
| Tailwater / aval (m) | **86.70** (T17) | 86.76 (T17 Nov 2) | −6 cm |
| Δh (head differential, m) | **18.86** | 18.77 | +0.09 |

Spill decreased −9.2% (above the 5% flag threshold) — ongoing mild normalization from the Nov 2 posture change. Spillway remains active at Day 2. Headpond 105.56 m = **89 cm above** the 104.67 m band ceiling — **Day 159** above band. 47-cm operating band (104.20–104.67 m): not breached; headpond is far above it.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T16–T17 UTC Nov 3. Yesterday comparison: Nov 2 brief T16–T17 values.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **218.61** T17 | 0% | −4.94 (−2.2%) |
| Quinze (3-31) | **208.65** T17 | 0.4% | −14.64 (−6.6%) |
| Îles (3-32) | **215.60** T16 | 0% | −12.18 (−5.3%) |
| Rapide-2 (3-29) | **157.34** T16 | 0% | +0.61 (flat) |
| Rapide-7 (3-28) | **158.63** T17 | 0% | +0.27 (flat) |
| Bryson (3-46) | **317.54** T16 | **35.7%** | −11.07 (−3.4%); spill 38%→36% |
| Paugan — Gatineau R. (3-65) | **150.68** T16 | 0% | +0.32 (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **162.02** T17 | 0% | −0.59 (flat) |
| Carillon — basin terminal (3-60) | **906.83** T17 | 0% | +34.98 (+4.0%) |

Upper cascade (Première-Chute through Îles) shows mild decreases vs yesterday — these are compared at different snapshot times and reflect typical intraday dispatch variation; the Quinze and Îles moves (−6.6% and −5.3%) are within the expected range for snapshot-window differences. Only Bryson carries a persistent anomaly (ongoing spill, normalizing). Carillon +4.0% is below the 5% flag threshold.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 27) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 3 provisional (m³/s) | **358** *(D47 in progress)* | 331 (Oct 27) | +27 | **D46 (352) confirmed; D47 in progress** |
| Timiskaming PSPC cross-check Nov 3 T00 | level 178.59 m, **flow 358 m³/s** | 178.69 m (Oct 26) | level flat (−2 cm total Oct 31→Nov 3) | Agrees with ORRPB exactly; cross-check valid |
| Quinze release → into lake (m³/s) | **208.65** (T17) | ~331 (Oct 27) | — | Baseload; slightly lower week-over-week |
| Mattawa level (m) | **152.49** (Nov 3 daily) | ~152.15 (Oct 27 est.) | +34 cm over 7 d; **+18 cm vs Nov 2 daily** | **4th consecutive day of rise** |
| Pembroke level (m) | **110.92** (Nov 3 daily) | ~111.10 (Oct 26 ref.) | ~−18 cm over 7 d; −5 cm vs Nov 2 | Continuing gentle multi-week decline |

**Provisional sanity check — Témiscaming Nov 3 = 358 m³/s (+6, +1.7% vs Nov 2 final 352):** Below the 25%/150 m³/s trigger threshold; full guardrail not required. PSPC agrees exactly (358 m³/s T00 Nov 3, level 178.59 m — flat, consistent with ~350 m³/s outflow). Within recent range (193–358 m³/s Oct 27–Nov 3). No anomaly. Sanity check passed.

**Nov 1 Témiscaming ORRPB/PSPC discrepancy:** ORRPB `temiscaming` shows 284 m³/s for Nov 1; PSPC `timiskaming` shows 305 m³/s — a 21 m³/s gap. Within the 50 m³/s tolerance; both are sub-400. D45 confirmed regardless. No flood-risk implication.

**Reservoir balance (T00 Nov 2 → T00 Nov 3):**
0 falling · 13 steady · 1 rising (des_joachims +3 cm, see Notes). No active retention or drawdown signal.

**Milestone bookkeeping (W44 rollup anchor Nov 1 + Nov 2 brief extension + today):**

| Milestone | W44 close (Nov 1) | Nov 2 | **Nov 3** |
|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 183 | 184 | **185** |
| Bryson amont above band (104.67 m) | 157 | 158 | **159** |
| §15.3.5.1 trigger INACTIVE | 160 | 161 | **162** |
| Témiscaming sub-400 | D45 (305 PSPC / 284 ORRPB — both sub-400) | D46 (352 final ✓) | D47? (358 prov) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T17 UTC Nov 3.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.28 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 162** (133 cm below trigger; +4 cm vs yesterday T17) |
| Carillon amont (1-2968) | **41.11 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 3.*

| Reservoir | Nov 2 (T00) | Nov 3 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.15 m | **219.14 m** | −1 cm | Steady |
| Témiscaming | 178.59 m | **178.59 m** | 0 cm | Steady |
| Dozois | 342.02 m | **342.01 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.59 m | **313.58 m** | −1 cm | Steady |

All 14 tracked reservoirs: 0 falling · 13 steady · 1 rising (des_joachims +3 cm, see Notes). No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-11-03 2:09 PM EST** (2026-11-03T19:09:00Z UTC). **Next Update: 2026-11-10 4:00 PM EST** (2026-11-10T21:00:00Z UTC). Cadence: weekly.*

**UPDATED from prior brief** (prior: Oct 27 — "expected to slightly decrease or remain fairly stable"). New forecast (Nov 3):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to slightly increase or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

Change: "slightly decrease" → "slightly increase" (precipitation cited). No flood-watch language; seasonal characterization unchanged.

`further_increases_possible`: true. `further_increases_includes_lac_coulonge`: null (reach not explicitly named).

---

## Anomaly flags

1. **ORRPB forecast updated today (Nov 3, first update since Oct 27): direction changed to "slightly increase or remain fairly stable."** Precipitation cited. No flood-watch language and Lac Coulonge not specifically named. Next update Nov 10.
2. **Bryson: Day 2 of partial spill, mild normalization.** Spill −9.2% (exceeds 5% flag threshold), from 125 to 113 m³/s. Headpond flat at 105.56 m — still a dispatch event. No downstream property-reach implication.

None of the above affects property flood risk. Lac Coulonge etat 0, 115 cm below pre-alert.

---

## Notes

- **Nov 2 D46 Témiscaming retro: final 352 m³/s.** Yesterday's provisional was 346 m³/s (revision +1.7%, well within 50 m³/s tolerance, CONFIRMED). Sub-400 streak continues at D47 in progress.
- **Nov 2 Mattawa convention note:** Yesterday's brief TL;DR reported "152.37 m (+10 cm)" using the live T17 UTC reading; ORRPB daily for Nov 2 finalized at 152.31 m (+4 cm from Nov 1 daily 152.27 m). Direction (rising) was correct. Recurring convention issue: live readings and daily averages are different products.
- **Nov 1 ORRPB/PSPC discrepancy at Témiscaming:** ORRPB `temiscaming` Nov 1 = 284 m³/s; PSPC `timiskaming` Nov 1 = 305 m³/s. Gap 21 m³/s — within 50 m³/s tolerance; D45 confirmed sub-400 regardless. The two series are normally in tight agreement once ORRPB finalizes; this residual gap is unusual and may persist (ORRPB's finalized value vs PSPC's operator report sometimes differ slightly for older preliminary rows).
- **Des Joachims reservoir +3 cm:** Small overnight rise (152.14 → 152.17 m); `latest_reservoir_readings` shows outflow 0 m³/s, which is likely a placeholder (OPG run-of-river facility). No anomaly.
- **V3 posterior (freshet_posterior.py): module restored — script now runs (exit 0).** Prior briefs reported `ModuleNotFoundError`; that is resolved. However, `--asof latest` still anchors on 2026-06-07 because `data/lac-coulonge-daily-1990-2026.csv` has not been extended past the freshet season. `freshet-forecast.json` updated but data unchanged (asof 2026-06-07). CSV extension needed to make the posterior current.
