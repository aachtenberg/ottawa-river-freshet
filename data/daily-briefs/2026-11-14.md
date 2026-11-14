# Daily brief — 2026-11-14

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 351b). ORRPB forecast HTTP 200 ✓ (`ottawariver.ca/conditions/?display=forecast`; weekly-notice mode, last update Nov 10 2:19 PM EST, next update Nov 17 4:00 PM). Vigilance 1195: proxy ingest fresh T21 UTC Nov 14 (106.036 m). V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged until `lac-coulonge-daily-1990-2026.csv` is extended).*

*Nov 13 retros: Témiscaming D57 provisional **428 m³/s** → final DB **387 m³/s** (sub-400 CONFIRMED; 4th consecutive above-400 provisional resolving sub-400; floor estimate at T22 ≈ 392 m³/s was again violated — final was below the floor, reinforcing W45 HQ item 1 methodology concern). D56 secondary revision: **397 → 385 m³/s** (12 m³/s minor post-run revision; both sub-400, streak unaffected). Mattawa Nov 13: provisional **152.48 m** (+13 cm claimed) → finalized **152.36 m** (+1 cm vs Nov 12 finalized 152.35 m — the +13 cm was a provisional artifact). Pembroke Nov 13: provisional 111.10 m → finalized **111.12 m** (+1 cm vs Nov 12 final 111.11 m; direction corrected from −1 cm to +1 cm).*

---

## In plain language

### Upstream — the upper basin

CORRECTION from yesterday: the Mattawa reading for November 13 — which yesterday's brief reported as a provisional rise of 13 centimetres to 152.48 metres — has finalized at 152.36 metres, only one centimetre above the November 12 baseline. The claimed rise was a provisional artifact that revised back overnight, the same pattern as the Mattawa November 12 reading a week ago. Today's finalized Mattawa level (152.46 metres) represents a genuine 10-centimetre rise from the corrected November 13 baseline.

Also correcting: the Lake Timiskaming outflow for November 13 — yesterday described as a provisional 428 cubic metres per second with the sub-400 streak status open — has finalized at 387 cubic metres per second, extending the sub-400 streak through a 57th consecutive day. This is the fourth time in succession that an above-400 provisional has resolved below 400 upon finalization, by margins of 44, 37, 41 (today's retro), and previously 47 cubic metres per second. For today, November 14, the two data sources disagree: the ORRPB reporting system shows 377 cubic metres per second (sub-400), while the PSPC operator cross-check shows 435 cubic metres per second (above 400). The gap of 58 cubic metres per second exceeds the 50 cubic metres per second flag threshold. Neither value alone constitutes a large day-over-day change, and both are provisional. The streak's status for today will only be confirmed once tomorrow's finalization resolves the discrepancy.

The fourteen storage reservoirs across the basin show a quiet posture: twelve are within a couple of centimetres of yesterday's readings, while Fort-Coulonge's local Poisson Blanc reservoir and the Des Joachims pool each rose modestly. One apparent outlier — the Rapide-7 reservoir — showed a one-day data artifact on November 13 (a spurious drop to 286 metres that corrected back to 309 metres today), consistent with an erroneous row rather than any real storage event.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 106.036 metres at 9 PM UTC on November 14, up roughly 2.5 centimetres from the same hour yesterday. The lake remains comfortably in normal conditions: 96 centimetres below the first alert threshold and 146 centimetres below the minor-flood mark. The ORRPB weekly forecast, last updated November 10, is unchanged: the river is running near seasonal norms and stable conditions are expected through the coming week. Next update is November 17.

Well downstream of the lake, the Bryson Generating Station — reached via a long, winding channel from the southern end of Lac Coulonge — saw its spillway routing increase modestly. The spillway share rose from about 16 to 20 percent of total flow, with the spilled volume up roughly 31 percent. The turbines remained at essentially the same output. Total release edged up about 5 percent. These changes are within normal dispatch variability and have no bearing on the lake's level. At the basin's terminal dam at Carillon, the total generation output stepped down by about 6 percent from yesterday's elevated level — again routine dispatch management. The dam pond behind Bryson (the headpond) remains 90 centimetres above its normal operating ceiling for the 170th consecutive day, unchanged from yesterday.

---

## TL;DR

**CORRECTIONS: D57 (Nov 13) provisional 428 m³/s → final 387 m³/s (sub-400 CONFIRMED, streak through D57); Mattawa Nov 13 provisional 152.48 m → finalized 152.36 m (+1 cm, not +13 cm).** **Today (Day 196):** Lac Coulonge T21 **106.036 m** (+2.5 cm vs T21 yesterday; etat 0, 96 cm below pre-alert). Bryson T20: total **371.93 m³/s** (+17.04/+4.8%), turbined **297.04**, spilled **74.88** (20.1% spill share, +30.5% — flag), headpond **105.57 m** (0 cm; Day 170 above band). §15.3.5.1 trigger INACTIVE **Day 173** (Hull 41.25 m). Carillon T19 **934.12 m³/s** (−63.28/−6.3% — flag; 0% spill). Témiscaming D58 provisional: **ORRPB 377 m³/s** / **PSPC 435 m³/s** (discrepancy 58 m³/s > 50 m³/s threshold — streak status UNCERTAIN for D58; both provisional). Mattawa Nov 14: **152.46 m** (+10 cm vs Nov 13 finalized 152.36 m). Pembroke Nov 14: **111.11 m** (−1 cm vs Nov 13 finalized 111.12 m). Reservoir balance: **0 falling · 12 steady · 2 rising** (poisson_blanc +5 cm, des_joachims +7 cm; rapide_7 Nov 13 artifact excluded). ORRPB forecast unchanged.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 14 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 14 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 14) | **106.036 m** |
| ORRPB daily Nov 14 (provisional) | 106.03 m |
| ORRPB daily Nov 13 (finalized) | 106.01 m |
| 24h delta (Vigilance T21 Nov 14 vs T21 Nov 13) | **+2.5 cm** (106.036 vs 106.011 m) |
| ORRPB daily delta (Nov 13 final 106.01 → Nov 14 prov 106.03) | +2 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 96 cm below |
| Distance to minor flood (107.50 m) | 146 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 UTC Nov 14 (releases + levels). Yesterday: T18 Nov 13 (releases), T18 Nov 13 (levels).*

| Metric | Today (T20 Nov 14) | Yesterday (T18 Nov 13) | Δ |
|---|---|---|---|
| Total release (m³/s) | **371.93** | 354.89 | +17.04 (+4.8%) |
| Turbined (m³/s) | **297.04** | 297.53 | −0.49 (−0.2%) |
| Spilled (m³/s) | **74.88** | 57.36 | +17.52 (**+30.5%** — flag) |
| Spill share (%) | **20.1%** | 16.2% | +3.9 pp |
| Headpond / amont (m) | **105.57** (T20) | 105.57 (T18 Nov 13) | 0 cm |
| Tailwater / aval (m) | **87.03** (T20) | 86.98 (T18 Nov 13) | +5 cm |
| Δh (head differential, m) | **18.54** | 18.59 | −5 cm |

Spill increased 30.5% (flag: >5%). Total release +4.8% (borderline, below 5% threshold — not flagged). Headpond flat at 105.57 m = **90 cm above** the 104.67 m band ceiling (Day 170 above band). Turbine output essentially unchanged. Run-of-river: routing decision only.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 14.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **248.59** T19 | 0% |
| Quinze (3-31) | **249.32** T19 | 0.4% (1.09 m³/s) |
| Îles (3-32) | **250.26** T20 | 0% |
| Rapide-2 (3-29) | **240.14** T19 | 0% |
| Rapide-7 (3-28) | **158.13** T19 | 0% |
| Bryson (3-46) | **371.93** T20 | **20.1%** (74.88 m³/s) |
| Paugan — Gatineau R. (3-65) | **160.25** T20 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **174.20** T19 | 0% |
| Carillon — basin terminal (3-60) | **934.12** T19 | 0% (−63.28/−6.3% vs yesterday 997.40 m³/s — flag) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 7) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 14 provisional — ORRPB (m³/s) | **377** | 389 (Nov 7) | −12 | D58 provisional; sub-400 on ORRPB side — streak continuation likely but PSPC disagrees (see note) |
| Témiscaming Nov 14 — PSPC cross-check (m³/s) | **435** | — | — | **⚑ Discrepancy 58 m³/s > 50 m³/s threshold** (level 178.70 m; +1 cm vs Nov 13 178.69 m) |
| Quinze release → into lake (m³/s) | **249.32** (T19) | — | — | Steady baseload |
| Mattawa level (m) | **152.46** (Nov 14 prov) | 152.20 (Nov 7) | +26 cm | +10 cm vs Nov 13 finalized 152.36 m; rising; retro correction: Nov 13 was +1 cm (not +13 cm) |
| Pembroke level (m) | **111.11** (Nov 14 prov) | — | — | Direction: declining (−1 cm vs Nov 13 finalized 111.12 m); direction only |

**Témiscaming D58 discrepancy note:** ORRPB `orrpb_river_flows` = 377 m³/s (sub-400); PSPC `reservoir_readings` = 435 m³/s (above 400). Gap: 58 m³/s, above the 50 m³/s flag threshold. Neither value alone triggers the ≥25%/≥150 m³/s mandatory sanity check (377 is −2.6% and 435 is +12.4% from D57 final 387 m³/s). Both are provisional for today. If ORRPB finalizes at ~377, D58 is sub-400 and the streak extends to 58 days. If the PSPC value better captures today's reality and finalizes above 400, the streak ends at D57 (57 consecutive days since Sep 18). Tomorrow's retro will confirm. ORRPB is typically the primary for `orrpb_river_flows` finalized values; the routine preference is PSPC for the current-day provisional when available.

**Mattawa retro — Nov 13:** Yesterday's brief reported provisional 152.48 m (+13 cm from Nov 12 finalized 152.35 m). Today's DB shows Nov 13 finalized = 152.36 m — only +1 cm. The +13 cm rise was a provisional artifact. Today's Nov 14 reading (152.46 m, +10 cm from Nov 13 final) is from the corrected baseline; it appears real but should be verified tomorrow.

**D56 secondary revision:** Yesterday's brief stated Nov 12 finalized = 397 m³/s. Today's DB shows Nov 12 = 385 m³/s — a 12 m³/s minor post-run revision (both sub-400; streak status unchanged).

**Reservoir balance (T00 Nov 13 → T00 Nov 14):**

| Reservoir | Nov 13 (T00) | Nov 14 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.28 m | **219.27 m** | −1 cm | Steady |
| Dozois | 342.09 m | **342.09 m** | 0 cm | Steady |
| Témiscaming | 178.69 m | **178.70 m** | +1 cm | Steady |
| Bark Lake | 313.56 m | **313.56 m** | 0 cm | Steady |
| Des Joachims | 152.13 m | **152.20 m** | +7 cm | Rising |
| Poisson Blanc | 200.12 m | **200.17 m** | +5 cm | Rising |
| Rapide-7 | 286.47 m | **309.00 m** | — | **Data artifact** (Nov 13 row is spurious; Nov 12 and Nov 14 both ≈309 m — excluded from balance) |
| Others (7) | — | — | 0 to −1 cm | Steady |

**Balance (excluding rapide_7 artifact): 0 falling · 12 steady · 2 rising** (des_joachims +7 cm, poisson_blanc +5 cm). Normal late-season posture; no active retention signal.

**Milestone bookkeeping (W45 rollup anchor Nov 8 + 6 days via DB):**

| Milestone | W45 close (Nov 8) | Nov 9 | Nov 10 | Nov 11 | Nov 12 | Nov 13 | **Nov 14** |
|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 190 | 191 | 192 | 193 | 194 | 195 | **196** |
| Bryson amont above band (104.67 m) | 164 | 165 | 166 | 167 | 168 | 169 | **170** |
| §15.3.5.1 trigger INACTIVE | 167 | 168 | 169 | 170 | 171 | 172 | **173** |
| Témiscaming sub-400 streak | D52 (376) | D53 (382) | D54 (383) | D55 (331) | D56 (385†) | D57 (387 — retro confirmed) | **D58 prov ORRPB 377 / PSPC 435 — streak UNCERTAIN** |

† D56 (Nov 12): secondary revision 397→385 m³/s; both sub-400.

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 14.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.25 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 173** (136 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 14.*

| Reservoir | Nov 13 (T00) | Nov 14 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.28 m | **219.27 m** | −1 cm | Steady |
| Témiscaming | 178.69 m | **178.70 m** | +1 cm | Steady (PSPC cross-check outflow 435 m³/s; ORRPB 377 m³/s — see discrepancy note) |
| Dozois | 342.09 m | **342.09 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.56 m | **313.56 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. Last Update: **2026-11-10 2:19 PM EST** (2026-11-10T19:19:00Z UTC). Next Update: 2026-11-17 4:00 PM EST (2026-11-17T21:00:00Z UTC). Cadence: weekly.*

No four-day forecasts active (outside freshet season). **Unchanged from prior brief** (last update remains Nov 10 2:19 PM ET):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Water levels and flows are expected to remain fairly stable over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Bryson spill +30.5%** (74.88 vs 57.36 m³/s). Spill share up from 16.2% to 20.1%. Total release +4.8% (below 5% flag; not flagged independently). Turbine output essentially flat. Routine dispatch adjustment; run-of-river means total flow is conserved. Day 170 of headpond above 104.67 m band continues (no change to that streak).
2. **Carillon −6.3%** (934.12 vs 997.40 m³/s, −63.28 m³/s). Partial reversal of yesterday's +17.2% step-up. Routine dispatch at the terminal dam; passes mandatory sanity check (63 < 150 m³/s and 6.3% < 25%). No flood implications.
3. **Témiscaming D58 PSPC/ORRPB discrepancy: 435 vs 377 m³/s** (58 m³/s gap > 50 m³/s threshold). Streak status for D58 uncertain pending finalization. No enhanced sanity check required (neither value constitutes ≥25% or ≥150 m³/s change from D57 final 387 m³/s). Report in data tables only until confirmed.
4. **Rapide-7 reservoir artifact** (Nov 13 row: 286.47 m vs Nov 12/Nov 14 both ≈309 m). One-day data error; excluded from balance calculation.

None of the above have flood-risk implications. Lac Coulonge etat 0, 96 cm below pre-alert.

---

## Notes

- **Floor-feasibility test reliability:** D57 provisional 428 m³/s had an estimated floor at T22 of ≈392 m³/s. The final came in at 387 m³/s — below the floor. This is physically impossible if the floor formula is correct (a running mean cannot go below the floor if the remaining hours average zero or more). The recurrence of this pattern (D49: floor ~404 actual 397; D57: floor ~392, actual 387) suggests the PSPC provisional is not a simple running average of hourly readings, or the reporting hour attribution is inconsistent. The floor calculation is unreliable for distinguishing "streak ends" vs "streak continues" when the provisional is only modestly above 400. W45 HQ item 1 (floor methodology) remains open.
- **Mattawa provisional volatility** continues: Nov 12 provisional revised +12 cm, Nov 13 provisional revised −12 cm. Same-day readings at Mattawa are systematically noisy. Today's Nov 14 provisional (+10 cm) should be treated as directionally indicative only.
- **V3 posterior CSV stale:** Script runs (exit 0) but anchors on asof 2026-06-07. `freshet-forecast.json` regenerated without change.

---

## HQ capture table addendum (Nov 14)

*Extends W45 rollup table. Per-day single-hour from `dam_levels` for the case-file level series. T20 UTC Nov 14.*

| Date | Bryson amont 1-2964 (m) | Carillon amont 1-2968 (m) | Hull dock 1-3675 (m) |
|---|---|---|---|
| 2026-11-14 | 105.57 (T20) | 41.12 (T20) | 41.25 (T20) |

Bryson amont 105.57 m = 90 cm above 104.67 m ceiling. Hull max ≤41.25 m (trigger 42.61 m; 136 cm clearance). No threshold breach.
