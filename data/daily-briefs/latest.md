# Daily brief — 2026-11-13

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 116b). ORRPB forecast HTTP 200 ✓ (`ottawariver.ca/forecasts/` + conditions page; no four-day forecast active outside freshet season — weekly-notice mode); last update Nov 10 2:19 PM EST, next update Nov 17 (Tuesdays outside freshet). Vigilance 1195: proxy ingest fresh T21 UTC Nov 13 (106.011 m). V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged until `lac-coulonge-daily-1990-2026.csv` is extended).*

*Nov 12 retros: Témiscaming D56 provisional **434 m³/s** → final DB **397 m³/s** (sub-400 CONFIRMED; streak continues through D56 — CORRECTION: yesterday's brief predicted "streak likely ends D56"). Mattawa Nov 12: provisional 152.23 m → final **152.35 m** (+12 cm revision; Nov 12 was flat vs Nov 11 finalized 152.35 m, not "step down" as described). Pembroke Nov 12: provisional 111.07 m → final **111.11 m** (+4 cm, confirmed from yesterday's brief — no direction correction needed).*

---

## In plain language

### Upstream — the upper basin

CORRECTION from yesterday: the outflow from Lake Timiskaming for November 12 — which yesterday's brief reported as a provisional 434 cubic metres per second, calling the sub-400 streak's end likely — has now finalized at 397 cubic metres per second. That is below 400, extending the streak for a fifty-seventh consecutive day. Yesterday's projection was wrong for the third time in this monitoring period: each of the previous three above-400 provisional readings (days 49, 55, and 56) has resolved below 400 upon finalization, by margins of 44, 47, and 37 cubic metres per second respectively.

Today is day 57 in progress, with a provisional daily mean of 428 cubic metres per second — above 400 as it stands. The floor at 22 hours in (the minimum possible 24-hour final, calculated as if flow dropped to zero for the last two hours) is about 392 cubic metres per second, still below 400. The honest uncertainty is in the provisional's reliability: each of the last three provisionals above 400 has finalized below it. Tomorrow's retro will confirm whether the streak extends to 57 days or ends here.

Mattawa levels rose 13 centimetres from a finalized 152.35 metres on November 12 to 152.48 metres on November 13 — a correction to yesterday's characterization of a "step down," which rested on a provisional value that subsequently revised upward by 12 centimetres. Pembroke edged 1 centimetre lower. The reservoir balance shows no active retention: all fourteen pools are within 3 centimetres of yesterday, with Poisson Blanc the sole riser at plus 3 centimetres.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 106.011 metres at 9 PM UTC — essentially flat, up less than half a centimetre from the same hour yesterday. The lake is in fully normal conditions: 99 centimetres below the pre-alert threshold and 149 centimetres below the minor-flood mark. The ORRPB weekly forecast, last updated three days ago on November 10, is unchanged: stable conditions expected through the coming week. Next update November 17.

The notable change today is at the Bryson Generating Station — the facility reached via a long, winding channel well below the southern end of Lac Coulonge, not visible from the Mansfield/Fort-Coulonge shoreline. After four days of running entirely through the spillway, the turbines came back online. By 6 PM UTC, the turbines were carrying about 298 cubic metres per second (84 percent of the total flow), with only 57 cubic metres per second through the spillway. Total release also decreased by about 42 cubic metres per second (nearly 11 percent). This is a generation dispatch decision by Hydro-Québec; run-of-river operations mean total flow is conserved regardless of the turbine/spillway split. At Carillon, the basin's terminal dam, the generation output stepped up to nearly 1,000 cubic metres per second — a 17 percent increase from yesterday, also consistent with routine daily dispatch management.

---

## TL;DR

**CORRECTION: D56 (Nov 12) provisional 434 m³/s → final 397 m³/s — sub-400 CONFIRMED; streak continues through D56.** **Today (Day 195):** Lac Coulonge T21 **106.011 m** (+0.4 cm vs T21 yesterday; etat 0, 99 cm below pre-alert). **Bryson turbines ONLINE** after 4-day 100% spill: total **354.89 m³/s** (−41.90/−10.6%), turbined **297.53**, spilled **57.36** (16.2% spill), headpond **105.57 m** (−1 cm; Day 169 above band). §15.3.5.1 trigger INACTIVE **Day 172** (Hull 41.27 m). Carillon T18 **997.40 m³/s** (+146.25/+17.2% — above 5% flag; dispatch step, 0% spill). Témiscaming D57 provisional **428 m³/s** (PSPC; floor at T22 ≈ 392 m³/s — below 400; streak status OPEN — provisional pattern suggests possible 3rd consecutive sub-400 resolution). Mattawa **152.48 m** (+13 cm vs Nov 12 finalized 152.35 m; retro correction from yesterday). Pembroke **111.10 m** (−1 cm vs Nov 12 finalized 111.11 m). Reservoir balance: **0 falling · 13 steady · 1 rising** (poisson_blanc +3 cm). ORRPB forecast unchanged.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 13 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 13 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 13) | **106.011 m** |
| ORRPB daily Nov 13 (provisional) | 106.01 m |
| ORRPB daily Nov 12 (finalized) | 106.01 m |
| 24h delta (Vigilance T21 Nov 13 vs T21 Nov 12) | **+0.4 cm** (106.011 vs 106.007 m) |
| ORRPB daily delta (Nov 12 prov 106.01 → Nov 13 prov 106.01) | 0 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 99 cm below |
| Distance to minor flood (107.50 m) | 149 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T18 UTC Nov 13 (releases + levels). Yesterday: T19 Nov 12 (releases), T20 Nov 12 (levels).*

| Metric | Today (T18 Nov 13) | Yesterday (T19 Nov 12) | Δ |
|---|---|---|---|
| Total release (m³/s) | **354.89** | 396.79 | −41.90 (−10.6%) |
| Turbined (m³/s) | **297.53** | 0 | +297.53 (turbines ONLINE — Day 1 resumed) |
| Spilled (m³/s) | **57.36** | 396.79 | −339.43 (−85.5%) |
| Spill share (%) | **16.2%** | 100% | −83.8 pp |
| Headpond / amont (m) | **105.57** (T18) | 105.58 (T20 Nov 12) | −1 cm |
| Tailwater / aval (m) | **86.98** (T18) | 87.07 (T20 Nov 12) | −9 cm |
| Δh (head differential, m) | **18.59** | 18.51 | +8 cm |

Turbines back online after 4 days of 100% spillway routing. Total release down 10.6%; turbined/spilled split flipped from 0%/100% to 84%/16%. Headpond 105.57 m = **90 cm above** the 104.67 m band ceiling (Day 169 above band). Run-of-river: flow conserved, routing decision only. All changes flagged (>5% on total, >5% on spill by definition).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T18 UTC Nov 13.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **245.27** T18 | 0% |
| Quinze (3-31) | **242.91** T18 | 0.4% (1.03 m³/s) |
| Îles (3-32) | **242.50** T18 | 0% |
| Rapide-2 (3-29) | **156.39** T18 | 0% |
| Rapide-7 (3-28) | **158.81** T18 | 0% |
| Bryson (3-46) | **354.89** T18 | **16.2%** (turbines back online after Day 4+ 100% spill) |
| Paugan — Gatineau R. (3-65) | **160.01** T18 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **175.09** T18 | 0% |
| Carillon — basin terminal (3-60) | **997.40** T18 | 0% (+146.25/+17.2% vs yesterday 851.15 m³/s) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 6) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 13 provisional — PSPC (m³/s) | **428** | 382 (Nov 6) | +46 | D57 provisional; floor at T22 ≈ 392 m³/s — streak status open (see note) |
| Témiscaming Nov 13 — PSPC reservoir cross-check (m³/s) | **428** | — | — | Level 178.69 m (+2 cm vs Nov 12 178.67 m); PSPC agrees |
| Quinze release → into lake (m³/s) | **242.91** (T18) | — | — | Steady baseload |
| Mattawa level (m) | **152.48** (Nov 13 prov) | 152.26 (Nov 6) | +22 cm | +13 cm vs Nov 12 finalized 152.35 m; rising (retro correction: Nov 12 was flat, not "step down") |
| Pembroke level (m) | **111.10** (Nov 13 prov) | 111.07 (Nov 6) | +3 cm | Direction: declining (−1 cm vs Nov 12 finalized 111.11 m); direction only |

**Témiscaming D57 provisional note:** PSPC daily average for Nov 13 = 428 m³/s. Change vs D56 finalized (397 m³/s): +31 m³/s = +7.8% — below the 25%/150 m³/s mandatory-guardrail thresholds; no enhanced sanity check required. Floor at T22 (22/24 × 428 ≈ 392.3 m³/s) — below 400. The honest uncertainty is in the provisional's reliability: for the final to stay below 400, a downward revision of ≥29 m³/s would be required; the last two provisionals revised down 37 and 47 m³/s respectively. Streak status open.

**CORRECTION — Témiscaming D56 (Nov 12):** Yesterday's TL;DR predicted "D56 provisional 434 m³/s — streak likely ends today." Today's DB shows Nov 12 PSPC (orrpb_river_flows) = **397 m³/s** (sub-400). D56 CONFIRMED sub-400. Streak extends through D56. This is the third provisional-above-400 reading (following D49/Nov 5 and D55/Nov 11) to resolve sub-400. The revision pattern (−47, −37, and now −37 m³/s) is consistent.

**Mattawa retro — Nov 12:** Yesterday's brief reported provisional 152.23 m (a "step down" of −12 cm from Nov 11 finalized 152.35). Today's DB shows Nov 12 finalized = 152.35 m — same as Nov 11, flat. The provisional captured a temporary low that revised up 12 cm overnight. Today Nov 13 = 152.48 m: a genuine +13 cm rise vs the Nov 12 final.

**Reservoir balance (T00 Nov 13 vs T00 Nov 12):**

| Reservoir | Nov 12 (T00) | Nov 13 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.28 m | **219.28 m** | 0 cm | Steady |
| Dozois | 342.09 m | **342.09 m** | 0 cm | Steady |
| Témiscaming | 178.67 m | **178.69 m** | +2 cm | Steady |
| Bark Lake | 313.56 m | **313.56 m** | 0 cm | Steady |
| Des Joachims | 152.11 m | **152.10 m** | −1 cm | Steady |
| Poisson Blanc | 200.09 m | **200.12 m** | +3 cm | Rising |
| Others (8) | — | — | 0 to −1 cm | Steady |

**Balance: 0 falling · 13 steady · 1 rising** (poisson_blanc +3 cm). Normal late-season posture; no active retention signal.

**Milestone bookkeeping (W45 rollup anchor Nov 8 + 5 days via DB):**

| Milestone | W45 close (Nov 8) | Nov 9 | Nov 10 | Nov 11 | Nov 12 | **Nov 13** |
|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 190 | 191 | 192 | 193 | 194 | **195** |
| Bryson amont above band (104.67 m) | 164 | 165 | 166 | 167 | 168 | **169** |
| §15.3.5.1 trigger INACTIVE | 167 | 168 | 169 | 170 | 171 | **172** |
| Témiscaming sub-400 streak | D52 (376) | D53 (382) | D54 (383) | D55 (364) | D56 (397 — CONFIRMED) | **D57 prov 428 — streak open** |

Note: D55 (Nov 11) orrpb_river_flows PSPC = 364 m³/s; yesterday's brief used reservoir_readings PSPC value of 372 m³/s (8 m³/s discrepancy, within 50 m³/s tolerance; both sub-400).

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T18 UTC Nov 13.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 172** (134 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 13.*

| Reservoir | Nov 12 (T00) | Nov 13 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.28 m | **219.28 m** | 0 cm | Steady |
| Témiscaming | 178.67 m | **178.69 m** | +2 cm | Steady (consistent with PSPC outflow 428 provisional) |
| Dozois | 342.09 m | **342.09 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.56 m | **313.56 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/forecasts/` + `/conditions/?display=forecast`, HTTP 200 ✓. Last Update: **2026-11-10 2:19 PM EST** (2026-11-10T19:19:00Z UTC). Next Update: 2026-11-17 EST (Tuesdays, weekly outside freshet). Cadence: weekly.*

No four-day forecasts active (outside freshet season). **Unchanged from yesterday's brief** (last update remains Nov 10 2:19 PM ET):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Water levels and flows are expected to remain fairly stable over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Bryson turbines back online** after 4 days of 100% spillway routing. T18 Nov 13: turbined 297.53 m³/s (84%), spilled 57.36 m³/s (16.2%), total 354.89 m³/s. Total release down 10.6% vs yesterday; spill share dropped from 100% to 16.2%. Generation dispatch decision; run-of-river means flow is conserved. No flood implications. Day 169 of headpond above 104.67 m band continues.
2. **Carillon T18: +146.25 m³/s / +17.2%** (997.40 vs 851.15 m³/s yesterday). Above the 5% change threshold. All turbined, 0% spill. Routine dispatch at the terminal dam; passes mandatory-sanity-check thresholds check (146 < 150 m³/s and 17.2% < 25%). No flood implications.

None of the above have flood-risk implications. Lac Coulonge etat 0, 99 cm below pre-alert.

---

## Notes

- **Témiscaming provisional reliability:** Three consecutive provisional-above-400 readings (D49: 441→397; D55: 419→372; D56: 434→397) have all resolved sub-400, by margins of 44, 47, and 37 m³/s respectively. For D57 (today, 428 provisional), the floor is ~392 m³/s — the minimum possible final if flows dropped to zero in the last two hours, which is physically impossible. In practice, the final will almost certainly land close to 428 unless there is a substantial downward revision matching the recent pattern. Tomorrow's retro will confirm.
- **Mattawa provisional volatility:** The Nov 12 provisional (152.23 m) revised up 12 cm to 152.35 m overnight. Same pattern as ORRPB Témiscaming provisional instability: same-day readings are noisy before the daily value locks in. Today's Mattawa rise (+13 cm) is from the finalized Nov 12 baseline; it appears real, but should be verified tomorrow against the finalized Nov 13 value.
- **V3 posterior CSV stale:** Script runs (exit 0) but anchors on asof 2026-06-07. `freshet-forecast.json` regenerated without change.

---

## HQ capture table addendum (Nov 13)

*Extends W45 rollup table. Per-day single-hour from `dam_levels` for the case-file level series. T18 UTC Nov 13.*

| Date | Bryson amont 1-2964 (m) | Carillon amont 1-2968 (m) | Hull dock 1-3675 (m) |
|---|---|---|---|
| 2026-11-13 | 105.57 (T18) | 41.12 (T18) | 41.27 (T18) |

Bryson amont 105.57 m = 90 cm above 104.67 m ceiling. Hull max ≤41.27 m (trigger 42.61 m; 134 cm clearance). No threshold breach.
