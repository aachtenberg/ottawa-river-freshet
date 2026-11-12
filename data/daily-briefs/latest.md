# Daily brief — 2026-11-12

*Generated automatically at 23:07 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 95b). ORRPB forecast HTTP 200 ✓ (probed: HTTP 200 / 128617b) — last update Nov 10 2:19 PM EST; next update Nov 17 4:00 PM EST (weekly cadence). Vigilance 1195: proxy ingest fresh T21 UTC Nov 12 (106.007 m). V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged until `lac-coulonge-daily-1990-2026.csv` is extended).*

*Nov 11 retros: Témiscaming D55 provisional **419 m³/s** → final DB **372 m³/s** (sub-400 CONFIRMED; Δ = −47 m³/s = −11.2%, within 50 m³/s tolerance — CONFIRMED numerically; streak interpretation CORRECTION: D55 is sub-400, streak continues through D55). Mattawa Nov 11: provisional 152.33 m → final **152.35 m** (+2 cm, within ±5 cm, CONFIRMED). Pembroke Nov 11: provisional 111.07 m → final **111.11 m** (+4 cm, within ±5 cm, CONFIRMED; note: prior brief characterized direction as "−4 cm from Nov 10 (111.11)"; final shows Nov 10 = Nov 11 = 111.11 m — direction was flat, not declining; minor direction correction, within tolerance).*

---

## In plain language

### Upstream — the upper basin

CORRECTION from yesterday: the outflow from Lake Timiskaming for November 11 — which yesterday's brief reported as a provisional 419 cubic metres per second, flagging the sub-400 streak as uncertain — has now finalized at 372 cubic metres per second. That is well below 400, confirming the streak continues unbroken: for 55 straight days since mid-September, daily flow through Timiskaming has remained below that round-number mark. Today is day 56 in progress, with a provisional reading of 434 cubic metres per second. Given that it is now the 23rd hour of the UTC day, the floor on what the final average can be is about 416 cubic metres per second — which is above 400. Unless the remaining hours average dramatically lower, today will likely break the streak. That said, provisional readings at this station have consistently run high and revised downward: yesterday's 419 finalized at 372, day 54's 419 finalized at 383, day 51's 417 finalized at 390. The streak's status is open until midnight UTC.

Mid-valley gauges show a modest easing. Mattawa levels dropped 12 centimetres from the finalized November 11 reading — a step down rather than a dramatic change, consistent with the modest fluctuation that has been characterizing this station through autumn. Pembroke edged 4 centimetres lower. Both stations are still above where they were a week ago, and there is no active retention signal anywhere in the upper basin: the reservoir tally is unchanged at one pool falling slightly, one pool rising slightly, and twelve holding flat.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 106.007 metres at 9 PM UTC — essentially flat, down less than half a centimetre from the same hour yesterday. The lake is in fully normal conditions: 99 centimetres below the pre-alert threshold and 149 centimetres below the minor-flood mark. The ORRPB weekly forecast, last updated two days ago, is unchanged: stable conditions expected through the coming week. The next scheduled update is November 17.

Downstream at the Bryson Generating Station — the facility reached via a long, winding channel well below the southern end of Lac Coulonge, not visible from the Mansfield/Fort-Coulonge shoreline — the turbines remain offline for a fourth consecutive day, with the full flow continuing to pass through the spillway. Total release held steady at about 397 cubic metres per second. At Carillon, the basin's terminal dam, the generation output stepped back down to about 851 cubic metres per second — reversing much of yesterday's 7-percent jump, consistent with routine dispatch management rather than any change in inflow.

---

## TL;DR

**CORRECTION: D55 (Nov 11) provisional 419 m³/s → final 372 m³/s — sub-400 CONFIRMED; streak continues through D55.** **Today (Day 194):** Lac Coulonge T21 **106.007 m** (−0.4 cm vs T21 yesterday; etat 0, 99 cm below pre-alert). Bryson Day 4 100% spill: total **396.79 m³/s** (+1.3%), turbined **0**, headpond **105.58 m** (+0 cm; Day 168 above band). §15.3.5.1 trigger INACTIVE **Day 171** (Hull 41.29 m). Carillon T19 **851.15 m³/s** (−52.68 m³/s / −5.8% vs yesterday; dispatch normalization, 0% spill). Témiscaming D56 provisional **434 m³/s** (PSPC; floor at T22 ≈ 416 m³/s — above 400; streak likely ends today, finalization pending). Mattawa **152.23 m** (−12 cm vs Nov 11 finalized 152.35 m). Pembroke **111.07 m** (−4 cm vs Nov 11 finalized 111.11 m). Reservoir balance: **1 falling · 12 steady · 1 rising** (poisson_blanc +4 cm). ORRPB forecast unchanged.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 12 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 12 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 12) | **106.007 m** |
| ORRPB daily Nov 12 (provisional) | 106.01 m |
| ORRPB daily Nov 11 (finalized) | 106.01 m |
| 24h delta (Vigilance T21 Nov 12 vs T21 Nov 11) | **−0.4 cm** (106.007 vs 106.011 m) |
| ORRPB daily delta (Nov 11 prov 106.01 → Nov 12 prov 106.01) | 0 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 99 cm below |
| Distance to minor flood (107.50 m) | 149 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Nov 12 (releases), T20 UTC Nov 12 (levels). Yesterday: T19 Nov 11 (releases), T20 Nov 11 (levels).*

| Metric | Today (T19 Nov 12) | Yesterday (T19 Nov 11) | Δ |
|---|---|---|---|
| Total release (m³/s) | **396.79** | 391.69 | +5.10 (+1.3%) |
| Turbined (m³/s) | **0** | 0 | 0 (Day 4 offline) |
| Spilled (m³/s) | **396.79** | 391.69 | +5.10 (+1.3%) |
| Spill share (%) | **100%** | 100% | 0 pp |
| Headpond / amont (m) | **105.58** (T20) | 105.58 (T20 Nov 11) | 0 cm |
| Tailwater / aval (m) | **87.07** (T20) | 87.06 (T20 Nov 11) | +1 cm |
| Δh (head differential, m) | **18.51** | 18.52 | −1 cm |

Day 4 of 100% spillway routing — no change in posture. Headpond 105.58 m = **91 cm above** the 104.67 m band ceiling (Day 168 above band). No values changed >5%. All normal.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 12.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **260.54** T19 | 0% |
| Quinze (3-31) | **254.00** T20 | 0.3% (0.87 m³/s) |
| Îles (3-32) | **254.36** T20 | 0% |
| Rapide-2 (3-29) | **156.70** T20 | 0% |
| Rapide-7 (3-28) | **154.23** T19 | 0% |
| Bryson (3-46) | **396.79** T19 | **100%** (Day 4 turbines offline) |
| Paugan — Gatineau R. (3-65) | **159.74** T19 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **180.92** T20 | 0% |
| Carillon — basin terminal (3-60) | **851.15** T19 | 0% (−52.68 / −5.8% vs yesterday 903.83 m³/s) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 5) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 12 provisional — PSPC (m³/s) | **434** | 397 (Nov 5) | +37 | D56 provisional; floor at T22 ≈ 416 m³/s — streak likely ends today; finalization pending (see note) |
| Témiscaming Nov 12 — PSPC reservoir cross-check (m³/s) | **434** | — | — | Level 178.67 m (+1 cm vs yesterday 178.66 m); PSPC outflow = PSPC reservoir flow, consistent |
| Quinze release → into lake (m³/s) | **254.00** (T20) | — | — | Steady baseload |
| Mattawa level (m) | **152.23** (Nov 12 prov) | 152.26 (Nov 5) | −3 cm | −12 cm vs Nov 11 finalized 152.35 m; declining |
| Pembroke level (m) | **111.07** (Nov 12 prov) | 111.11 (Nov 5) | −4 cm | Direction: declining (−4 cm vs Nov 11 finalized 111.11 m); direction only |

**Témiscaming D56 provisional note:** PSPC daily average for Nov 12 = 434 m³/s. Change vs D55 finalized (372 m³/s): +62 m³/s = +16.7% — below the 25%/150 m³/s mandatory-guardrail thresholds; no enhanced sanity check required. Floor at T22 (22/24 × 434 ≈ 398 m³/s) — barely sub-400 possible at T22, but at T23 (23/24 × 434 ≈ 416 m³/s) the floor rises clearly above 400. The brief runs at ~23:00 UTC so the floor is likely above 400 by now. Historical pattern: PSPC provisionals have consistently revised downward (D55: 419→372; D54: provisional 419→383; D51: 417→390), but revisions large enough to bring 434 below 400 would require a −34+ m³/s revision — possible but would be on the larger side. Streak status open until finalization; anticipate D56 above 400 and end of streak.

**CORRECTION — Témiscaming D55 (Nov 11):** Yesterday's TL;DR headlined "D55 provisional 419 m³/s — above 400, streak status open." Today's DB shows Nov 11 finalized PSPC = **372 m³/s** (sub-400). D55 CONFIRMED sub-400. The provisional 419 → final 372 delta (−47 m³/s = −11.2%) is within the 50 m³/s / 25% tolerance thresholds: verdict CONFIRMED. Streak extends to at least D55 (Nov 11, 372 m³/s). D56 (today) is the first genuine open question for streak termination.

**Reservoir balance (T00 Nov 12 vs T00 Nov 11):**

| Reservoir | Nov 11 | Nov 12 | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.27 m | **219.27 m** | 0 cm | Steady |
| Dozois | 342.08 m | **342.09 m** | +1 cm | Steady |
| Témiscaming | 178.66 m | **178.67 m** | +1 cm | Steady |
| Bark Lake | 313.57 m | **313.56 m** | −1 cm | Steady |
| Des Joachims | 152.11 m | **152.07 m** | −4 cm | Falling |
| Poisson Blanc | 200.04 m | **200.08 m** | +4 cm | Rising |
| Others (8) | — | — | 0 to +1 cm | Steady |

**Balance: 1 falling · 12 steady · 1 rising** (poisson_blanc +4 cm). Normal late-season posture; no active retention signal (all well below 10 cm/day threshold).

**Milestone bookkeeping (W45 rollup anchor Nov 8 + 4 days via DB):**

| Milestone | W45 close (Nov 8) | Nov 9 | Nov 10 | Nov 11 | **Nov 12** |
|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 190 | 191 | 192 | 193 | **194** |
| Bryson amont above band (104.67 m) | 164 | 165 | 166 | 167 | **168** |
| §15.3.5.1 trigger INACTIVE | 167 | 168 | 169 | 170 | **171** |
| Témiscaming sub-400 streak | D52 (376) | D53 (382) | D54 (383) | D55 (372 — CONFIRMED) | **D56 prov 434 — streak likely ends today** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 12.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.29 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 171** (132 cm below trigger) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 12.*

| Reservoir | Nov 11 (T00) | Nov 12 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.27 m | **219.27 m** | 0 cm | Steady |
| Témiscaming | 178.66 m | **178.67 m** | +1 cm | Steady (consistent with PSPC outflow 434 provisional) |
| Dozois | 342.08 m | **342.09 m** | +1 cm | Steady |
| Bark Lake (OPG) | 313.57 m | **313.56 m** | −1 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓ (probed: HTTP 200 / 128617b). Last Update: **2026-11-10 2:19 PM EST** (2026-11-10T19:19:00Z UTC). Next Update: 2026-11-17 4:00 PM EST (2026-11-17T21:00:00Z UTC). Cadence: weekly.*

**Unchanged from yesterday's brief** (last update remains Nov 10 2:19 PM ET):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Water levels and flows are expected to remain fairly stable over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Carillon T19: −52.68 m³/s / −5.8%** (851.15 vs 903.83 m³/s yesterday). Above the 5% change threshold; this reverses yesterday's +6.7% dispatch spike. Routine generation dispatch adjustment, all turbined, 0% spill. No flood implications; dispatch has normalized.
2. **Témiscaming D56 streak watch:** Floor at T23 ≈ 416 m³/s (above 400). The 55-day sub-400 streak will likely end today when D56 finalizes. Watch tomorrow's retro. Not a flood-risk event — Lac Coulonge etat 0, 99 cm below pre-alert.

None of the above have flood-risk implications. Lac Coulonge etat 0, 99 cm below pre-alert.

---

## Notes

- **Carillon dispatch reversal:** Yesterday's +6.7% (847→904 m³/s) reversed to −5.8% (904→851 m³/s) today. Both moves are within the range of routine daily generation dispatch management at the terminal dam. The two-day net change is negligible (847→851 m³/s, +4 m³/s).
- **D56 streak:** The floor argument at T23 gives ≈416 m³/s (above 400). However, PSPC provisionals have shown consistent downward revision this autumn (average downward revision: D51 −27, D52 −42, D53 N/A, D54 N/A, D55 −47). A revision of −35+ m³/s would bring D56 below 400. That's larger than average but not unprecedented. Tomorrow's retro will confirm.
- **V3 posterior CSV stale:** Script runs (exit 0) but anchors on asof 2026-06-07. `freshet-forecast.json` regenerated without change.
- **Pembroke direction note:** Yesterday's brief characterized Nov 11 Pembroke as "−4 cm from Nov 10 (111.11 m)." The DB finalized Nov 11 at 111.11 m — same as Nov 10. Direction was flat, not declining. The claim is within tolerance (+4 cm from provisional 111.07) but the direction note was incorrect. Today's DB confirms the Dec 11 → Nov 12 step is a genuine −4 cm (111.11 → 111.07 m).

---

## HQ capture table addendum (Nov 12)

*Extends W45 rollup table. Per-day single-hour max/min from `dam_levels` for the case-file level series. T20 UTC Nov 12.*

| Date | Bryson amont 1-2964 (m) | Carillon amont 1-2968 (m) | Hull dock 1-3675 (m) |
|---|---|---|---|
| 2026-11-12 | 105.58 (T20) | 41.13 (T20) | 41.29 (T20) |

Bryson amont 105.58 m = 91 cm above 104.67 m ceiling. Hull max ≤41.29 m (trigger 42.61 m; 132 cm clearance). No threshold breach.
