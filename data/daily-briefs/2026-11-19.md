# Daily brief — 2026-11-19

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 95b). ORRPB conditions forecast HTTP 200 ✓ (page fetched; forecast unchanged — last update Nov 17). Vigilance 1195: proxy ingest fresh T21 UTC Nov 19. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 19.*

*Nov 18 retro: Témiscaming provisional 341 m³/s → finalized **381 m³/s** (+40 m³/s, within 50 m³/s threshold — CONFIRMED sub-400; D3 confirmed). Nov 18 Mattawa ORRPB daily revised 152.37 → **152.31 m** (−6 cm, outside ±5 cm threshold — REVISED; no flood significance; direction unchanged).*

---

## In plain language

### Upstream — the upper basin

The upper basin remains in a quiet late-autumn posture, 201 days past the May 2 freshet peak of 2,741 cubic metres per second. Outflow from Lake Timiskaming — the first major pinch point below the northern headwaters — came in at 334 cubic metres per second today in the preliminary reading, confirmed by the independent operator measurement at 329 m³/s (a 5 m³/s gap, well within the normal agreement range). That is Day 4 of the current sub-400 m³/s streak that began November 16. Yesterday's provisional reading of 341 m³/s revised upward to 381 m³/s once finalized — still sub-400, streak continues.

All fourteen storage reservoirs across the basin are essentially flat, with thirteen holding within two centimetres of yesterday and one (Poisson Blanc) edging up three centimetres. This is normal late-November behaviour; no active refill surge or unusual retention.

Mattawa declined five centimetres overnight (152.26 m today vs 152.31 m yesterday finalized), continuing the gentle oscillatory pattern of recent weeks. Pembroke slipped two centimetres to 111.07 m. Neither move has flood significance.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge recorded 106.009 metres at 9 PM UTC on November 19, about half a centimetre below the same reading yesterday. The lake sits nearly a full metre below the first alert threshold — firmly in normal, non-event conditions.

The generating station at Bryson — reached by the long channel winding south from Lac Coulonge — held essentially unchanged overnight: total release 351 m³/s, turbines producing 297 m³/s, with the remaining 54 m³/s passing through the spillway (about 15% of the total). The dam pond behind Bryson edged down two centimetres to 105.54 metres, now 87 centimetres above the normal operating ceiling. This is Day 175 of the headpond sitting above that band; it is an ongoing baseline condition, not a new development.

The ORRPB weekly forecast, last updated Monday November 17, calls for flows to "remain fairly stable or slightly decrease over the coming week, depending on locations." Next update is expected November 24. No change from yesterday.

---

## TL;DR

**RETRO: Nov 18 Témiscaming prov 341 → final 381 m³/s (CONFIRMED sub-400, D3); Nov 18 Mattawa prov 152.37 → final 152.31 m (REVISED −6 cm, outside ±5 cm threshold; no flood significance).** **Today (Day 201):** Lac Coulonge T21 **106.009 m** (−0.7 cm vs T21 yesterday; etat 0, 99 cm below pre-alert). Bryson T20: total **351.03 m³/s** (−0.1%), spill **53.71** (15.3%, −0.1%), headpond **105.54 m** (−2 cm; Day 175 above band). §15.3.5.1 trigger INACTIVE **Day 178** (Hull 41.26 m). Carillon T19 **851.31 m³/s** (−16.4% vs yesterday T20 1018.9 — continuing dispatch step-down; flag). Témiscaming sub-400 streak: D3 finalized (Nov 18=381), D4 provisional (Nov 19=334). Reservoir balance: **0 falling · 13 steady · 1 rising**. ORRPB weekly forecast unchanged from Nov 17; next update Nov 24.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 19 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 19 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 19) | **106.009 m** |
| ORRPB daily Nov 19 (provisional) | 106.01 m |
| ORRPB daily Nov 18 (finalized) | 106.02 m |
| 24h delta (Vigilance T21 Nov 19 vs T21 Nov 18) | **−0.7 cm** (106.009 vs 106.016 m) |
| ORRPB daily delta (Nov 18 final 106.02 → Nov 19 prov 106.01) | −1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 99 cm below |
| Distance to minor flood (107.50 m) | 149 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 (releases) / T20 (levels) UTC Nov 19. Yesterday: T19/T20 Nov 18 (from prior brief).*

| Metric | Today (T20 Nov 19) | Yesterday (T19/T20 Nov 18) | Δ |
|---|---|---|---|
| Total release (m³/s) | **351.03** | 351.43 | −0.40 (−0.1%) |
| Turbined (m³/s) | **297.33** | 297.66 | −0.33 (−0.1%) |
| Spilled (m³/s) | **53.71** | 53.78 | −0.07 (−0.1%) |
| Spill share (%) | **15.3%** | 15.3% | 0 pp |
| Headpond / amont (m) | **105.54** (T20) | 105.56 (T20 Nov 18) | −2 cm |
| Tailwater / aval (m) | **86.94** (T20) | 86.94 (T20 Nov 18) | 0 cm |
| Δh (head differential, m) | **18.60** | 18.62 | −2 cm |

No change exceeds 5% threshold. Headpond 105.54 m = **87 cm above** the 104.67 m band ceiling (Day 175 above band). Stable run-of-river dispatch.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 19.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **219.04** T19 | 0% |
| Quinze (3-31) | **217.69** T19 | 0.5% (1.01 m³/s) |
| Îles (3-32) | **222.19** T20 | 0% |
| Rapide-2 (3-29) | **157.72** T20 | 0% |
| Rapide-7 (3-28) | **157.71** T19 | 0% |
| Bryson (3-46) | **351.03** T20 | **15.3%** (53.71 m³/s) |
| Paugan — Gatineau R. (3-65) | **~159** T20 (turbine only; total_cms null) | n/a |
| Rapides-Farmers — Gatineau mouth (3-67) | **170.75** T20 | 0% |
| Carillon — basin terminal (3-60) | **851.31** T19 | 0% (**−16.4%** vs yesterday T20 1018.9 m³/s — continuing dispatch step-down; flag) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 12) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 19 — ORRPB/PSPC provisional (m³/s) | **334** | 380 (Nov 12) | −46 | D4 provisional sub-400 (below 380 — reliable); D1=Nov 16 (366), D2=Nov 17 (375), D3=Nov 18 (381 fin) |
| Témiscaming PSPC cross-check (m³/s) | **329** T00 Nov 19 | — | — | 5 m³/s gap vs ORRPB (consistent; <50 m³/s threshold) |
| Quinze release → into lake (m³/s) | **217.69** (T19) | — | — | Steady baseload; trace spill 1.0 m³/s |
| Mattawa level (m) | **152.26** (Nov 19) | 152.13 (Nov 12) | +13 cm | −5 cm vs Nov 18 finalized (152.31); oscillatory pattern |
| Pembroke level (m) | **111.07** (Nov 19) | 111.16 (Nov 12) | −9 cm | −2 cm vs Nov 18 (111.09); slowly declining |

**Reservoir balance (T00 Nov 18 → T00 Nov 19):**

| Reservoir | Nov 18 (T00) | Nov 19 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.27 m | **219.26 m** | −1 cm | Steady |
| Dozois | 342.09 m | **342.10 m** | +1 cm | Steady |
| Témiscaming | 178.63 m | **178.62 m** | −1 cm | Steady |
| Bark Lake | 313.53 m | **313.53 m** | 0 cm | Steady |
| Des Joachims | 152.09 m | **152.07 m** | −2 cm | Steady |
| Poisson Blanc | 200.31 m | **200.34 m** | +3 cm | Rising (below 10 cm/day flag) |
| Rapide-7 | 309.00 m | **309.01 m** | +1 cm | Steady |
| Others (7) | — | — | −2 to +1 cm | Steady |

**Balance: 0 falling · 13 steady · 1 rising (Poisson Blanc +3 cm, below 10 cm/day flag).** Normal late-season holding posture.

**Milestone bookkeeping (W46 rollup Nov 15 anchor + corrected daily chain via DB):**

| Milestone | W46 close (Nov 15) | Nov 16 | Nov 17 | Nov 18 | **Nov 19** |
|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 197 | 198 | 199 | 200 | **201** |
| Bryson amont above band (104.67 m) | 171 | 172 | 173 | 174 | **175** |
| §15.3.5.1 trigger INACTIVE | 174 | 175 | 176 | 177 | **178** |
| Témiscaming sub-400 streak | *prior streak broke Nov 13 (412)* | D1: 366 | D2: 375 fin | D3: 381 fin (prov 341→fin 381) | **D4 prov: 334** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 19.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.26 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 178** (135 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 19.*

| Reservoir | Nov 18 (T00) | Nov 19 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.27 m | **219.26 m** | −1 cm | Steady |
| Témiscaming | 178.63 m | **178.62 m** | −1 cm | Steady |
| Dozois | 342.09 m | **342.10 m** | +1 cm | Steady |
| Bark Lake (OPG) | 313.53 m | **313.53 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (page fetched). Last Update: 2026-11-17 2:49 PM EST (2026-11-17T19:49:00Z UTC). Next Update: 2026-11-24 4:00 PM EST (2026-11-24T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` updated with mode=`weekly-notice`.*

**Unchanged from Nov 17 brief (no new ORRPB update expected until Nov 24):**

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums.*

---

## Anomaly flags

1. **Carillon dispatch step-down continuing.** T19 851.31 vs yesterday T20 1018.9 m³/s = −167.59 (−16.4%; flag: >5%). Turbines handling all flow (0% spill). Third consecutive day of flagged decline (−12.1% Nov 18, −16.4% Nov 19). Routine HQ dispatch adjustment; no flood implication, no headpond or regulatory consequence.
2. **RETRO — Nov 18 Mattawa REVISED.** ORRPB daily Nov 18 reported 152.37 m in yesterday's brief; finalized 152.31 m (−6 cm revision, outside ±5 cm threshold). Direction unchanged (Mattawa is declining), no flood significance.
3. **RETRO — Nov 18 Témiscaming CONFIRMED.** Provisional 341 → finalized 381 m³/s (+40 m³/s; within 50 m³/s threshold). Sub-400 streak D3 confirmed at 381 m³/s.

No flood-risk implications. Lac Coulonge etat 0, 99 cm below pre-alert. §15.3.5.1 trigger inactive.

---

## Notes

- **Day 201** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (165 days stale). `freshet-forecast.json` regenerated without change. W46 HQ item 4 remains open.
- **Témiscaming PSPC/ORRPB agreement:** 329 vs 334 m³/s for Nov 19 (5 m³/s gap; within 50 threshold — consistent).
- **Paugan (3-65):** `total_cms` null in `latest_dam_releases`; turbined 159 m³/s available. Spill share indeterminate. Likely 0% spill (consistent with low-flow season and turbine-only record).
