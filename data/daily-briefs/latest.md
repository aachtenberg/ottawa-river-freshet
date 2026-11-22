# Daily brief — 2026-11-21

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 105b). ORRPB conditions forecast HTTP 200 ✓ (page fetched; forecast unchanged — last update Nov 17). Vigilance 1195: proxy ingest fresh T21 UTC Nov 21. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 21.*

*Nov 20 retro: Témiscaming PSPC prov 386 → finalized **358 m³/s** (−28 m³/s, within 50 threshold — CONFIRMED sub-400 D5). ORRPB prov 377 → finalized **358 m³/s** (−19 m³/s, within 50 — CONFIRMED). Mattawa prov 152.30 → finalized **152.34 m** (+4 cm, within ±5 cm — CONFIRMED). Pembroke prov 111.06 → finalized **111.09 m** (+3 cm, within ±5 cm — CONFIRMED).*

---

## In plain language

### Upstream — the upper basin

The upper basin remains in a quiet late-autumn posture, 203 days past the May 2 freshet peak of 2,741 cubic metres per second. Outflow from Lake Timiskaming — the first major pinch point below the northern headwaters — came in today at 384 cubic metres per second in the PSPC operator measurement (midnight snapshot), which remains solidly below 400 m³/s for a sixth provisional day in a row. Yesterday's provisional of 386 m³/s finalized at 358 m³/s, confirming that fifth day of the current below-400 streak.

All fourteen storage reservoirs continue their quiet late-season holding posture: thirteen are within two centimetres of yesterday, with only Poisson Blanc edging up three centimetres again. Pembroke edged up four centimetres to 111.13 metres today. The provisional Mattawa reading for today (152.19 m) shows a large apparent drop of 15 centimetres from yesterday's finalized 152.34 m; this is inconsistent with Pembroke's uptick downstream, and the magnitude is similar to provisional artifacts seen in prior weeks — treat as preliminary and expect revision.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge recorded 105.987 metres at 9 PM UTC on November 21, about one centimetre below yesterday's reading. The lake sits just over a metre below the first alert threshold — firmly in normal, non-event conditions.

The generating station at Bryson — reached by the long channel winding south from Lac Coulonge — held essentially unchanged: total release 350 m³/s, turbines producing 297 m³/s, with 54 m³/s passing through the spillway (15% of the total). The dam pond behind Bryson eased back four centimetres to 105.51 metres, now 84 centimetres above the normal operating ceiling. This is Day 177 of the headpond sitting above that band; it is an ongoing baseline condition.

The ORRPB weekly forecast, last updated Monday November 17, calls for flows to "remain fairly stable or slightly decrease over the coming week, depending on locations." Next update is expected November 24. No change from yesterday.

---

## TL;DR

**RETRO: Nov 20 Témiscaming PSPC prov 386 → final 358 m³/s (CONFIRMED sub-400, D5); ORRPB prov 377 → final 358 (CONFIRMED); Mattawa prov 152.30 → 152.34 m (CONFIRMED ±5 cm); Pembroke prov 111.06 → 111.09 m (CONFIRMED).** **Today (Day 203):** Lac Coulonge T21 **105.987 m** (−1.3 cm vs T21 Nov 20; etat 0, 101 cm below pre-alert). Bryson T20: total **350.34 m³/s** (−0.23%), spill **53.60** (15.3%), headpond **105.51 m** (−4 cm; Day 177 above band). §15.3.5.1 trigger INACTIVE **Day 180** (Hull 41.28 m). Carillon T19 **879.49 m³/s** (−13.1% vs yesterday T20 1011.99 — step-down reversing yesterday's step-up; flag). Témiscaming D6 prov: ORRPB daily **317 m³/s**, PSPC T00 **384 m³/s** (gap 67 m³/s >50 threshold — flag; both sub-400, streak continuing). Mattawa prov 152.19 m (−15 cm vs final 152.34 — large; likely provisional artifact; Pembroke +4 cm inconsistent). Reservoir balance: **0 falling · 13 steady · 1 rising** (Poisson Blanc +3 cm). ORRPB weekly forecast unchanged from Nov 17; next update Nov 24.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 21 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 21 provisional (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 21) | **105.987 m** |
| ORRPB daily Nov 21 (provisional) | 105.99 m |
| ORRPB daily Nov 20 (finalized) | 106.00 m |
| 24h delta (Vigilance T21 Nov 21 vs T21 Nov 20) | **−1.3 cm** (105.987 vs 106.000 m) |
| ORRPB daily delta (Nov 20 final 106.00 → Nov 21 prov 105.99) | −1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 101 cm below |
| Distance to minor flood (107.50 m) | 151 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 (releases and levels) UTC Nov 21. Yesterday: T19/T20 Nov 20 (from prior brief).*

| Metric | Today (T20 Nov 21) | Yesterday (T19/T20 Nov 20) | Δ |
|---|---|---|---|
| Total release (m³/s) | **350.34** | 351.15 | −0.81 (−0.23%) |
| Turbined (m³/s) | **296.74** | 297.41 | −0.67 (−0.23%) |
| Spilled (m³/s) | **53.60** | 53.73 | −0.13 (−0.24%) |
| Spill share (%) | **15.3%** | 15.3% | 0 pp |
| Headpond / amont (m) | **105.51** (T20) | 105.55 (T20 Nov 20) | −4 cm |
| Tailwater / aval (m) | **86.98** (T20) | 86.94 (T20 Nov 20) | +4 cm |
| Δh (head differential, m) | **18.53** | 18.61 | −8 cm |

No change exceeds 5% threshold. Headpond 105.51 m = **84 cm above** the 104.67 m band ceiling (Day 177 above band). Stable run-of-river dispatch.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 21.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **219.52** T20 | 0% |
| Quinze (3-31) | **220.89** T20 | 0.5% (1.05 m³/s) |
| Îles (3-32) | **225.41** T20 | 0% |
| Rapide-2 (3-29) | **157.55** T19 | 0% |
| Rapide-7 (3-28) | **157.95** T19 | 0% |
| Bryson (3-46) | **350.34** T20 | **15.3%** (53.60 m³/s) |
| Paugan — Gatineau R. (3-65) | **159.29** T20 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **171.00** T19 | 0% |
| Carillon — basin terminal (3-60) | **879.49** T19 | 0% (**−13.1%** vs yesterday T20 1011.99 m³/s — step-down reversing yesterday's step-up; flag) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 14) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 21 — ORRPB daily provisional (m³/s) | **317** | 389 (Nov 14 fin) | −72 | D6 provisional sub-400; D1=Nov 16 (366 fin), D2=Nov 17 (375 fin), D3=Nov 18 (381 fin), D4=Nov 19 (365 fin), D5=Nov 20 (358 fin) |
| Témiscaming PSPC cross-check (m³/s) | **384** T00 Nov 21 | — | — | 67 m³/s gap vs ORRPB daily (>50 threshold — flag; comparing midnight snapshot vs partial-day running mean; both sources sub-400) |
| Quinze release → into lake (m³/s) | **220.89** (T20) | — | — | Steady baseload; trace spill 1.1 m³/s |
| Mattawa level (m) | **152.19** (Nov 21 prov) | 152.34 (Nov 20 fin) | — | −15 cm vs Nov 20 finalized (152.34); **large provisional drop — likely artifact** (Pembroke +4 cm downstream is inconsistent; similar to Nov 13 −12 cm artifact, corrected Nov 14) |
| Pembroke level (m) | **111.13** (Nov 21) | 111.09 (Nov 20 fin) | +4 cm | +4 cm vs Nov 20 finalized (111.09); slight uptick |

**Reservoir balance (T00 Nov 20 → T00 Nov 21):**

| Reservoir | Nov 20 (T00) | Nov 21 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.26 m | **219.25 m** | −1 cm | Steady |
| Dozois | 342.08 m | **342.08 m** | 0 cm | Steady |
| Témiscaming | 178.62 m | **178.60 m** | −2 cm | Steady |
| Bark Lake | 313.52 m | **313.52 m** | 0 cm | Steady |
| Des Joachims | 152.12 m | **152.13 m** | +1 cm | Steady |
| Poisson Blanc | 200.37 m | **200.40 m** | +3 cm | Rising (below 10 cm/day flag) |
| Cabonga | 359.66 m | **359.65 m** | −1 cm | Steady |
| Others (8) | — | — | −2 to +1 cm | Steady |

**Balance: 0 falling · 13 steady · 1 rising (Poisson Blanc +3 cm, below 10 cm/day flag).** Normal late-season holding posture.

**Milestone bookkeeping (W46 rollup Nov 15 anchor + corrected daily chain via DB):**

| Milestone | W46 close (Nov 15) | Nov 16 | Nov 17 | Nov 18 | Nov 19 | Nov 20 | **Nov 21** |
|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 197 | 198 | 199 | 200 | 201 | 202 | **203** |
| Bryson amont above band (104.67 m) | 171 | 172 | 173 | 174 | 175 | 176 | **177** |
| §15.3.5.1 trigger INACTIVE | 174 | 175 | 176 | 177 | 178 | 179 | **180** |
| Témiscaming sub-400 streak | *new D1 Nov 16 (366)* | D1: 366 | D2: 375 fin | D3: 381 fin | D4: 365 fin | D5: 358 fin (prov 386→fin 358) | **D6 prov: 317 (ORRPB) / 384 PSPC T00** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 21.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.28 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 180** (133 cm below trigger) |
| Carillon amont (1-2968) | **41.11 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 21.*

| Reservoir | Nov 20 (T00) | Nov 21 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.26 m | **219.25 m** | −1 cm | Steady |
| Témiscaming | 178.62 m | **178.60 m** | −2 cm | Steady |
| Dozois | 342.08 m | **342.08 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.52 m | **313.52 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (page fetched). Last Update: 2026-11-17 2:49 PM EST (2026-11-17T19:49:00Z UTC). Next Update: 2026-11-24 4:00 PM EST (2026-11-24T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` updated with mode=`weekly-notice`.*

**Unchanged from Nov 17 brief (no new ORRPB update expected until Nov 24):**

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Carillon dispatch step-DOWN −13.1%.** T19 879.49 vs yesterday T20 1011.99 m³/s = −132.5 (−13.1%; flag: >5%). Reverses yesterday's +18.9% step-up. Turbines handling all flow (0% spill). Routine HQ dispatch adjustment; no flood implication.
2. **Témiscaming PSPC/ORRPB discrepancy 67 m³/s (>50 threshold).** ORRPB daily provisional 317 m³/s vs PSPC T00 384 m³/s — gap 67 m³/s. Note: both series are PSPC-sourced (orrpb_river_flows temiscaming agency=PSPC); the gap reflects midnight snapshot (PSPC T00=384) vs partial-day running mean (ORRPB daily=317) rather than independent-source disagreement. Both are sub-400; sub-400 D6 provisional streak status appears secure. Flagged per >50 m³/s rule.
3. **Mattawa Nov 21 provisional −15 cm (likely artifact).** ORRPB daily Mattawa Nov 21 = 152.19 m vs Nov 20 finalized 152.34 m = −15 cm. This is a large single-day level drop in a stable season. Pembroke (downstream) rose +4 cm today, which is physically inconsistent with a 15 cm Mattawa crash. Pattern matches the Nov 13 −12 cm artifact (corrected Nov 14 to 152.36 m). Treat Nov 21 Mattawa as provisional — expect revision toward recent range (~152.25–152.35 m).
4. **RETRO — Nov 20 Témiscaming CONFIRMED.** PSPC prov 386 → finalized 358 m³/s (−28 m³/s; within 50 threshold). ORRPB prov 377 → finalized 358 m³/s (−19 m³/s; within 50 threshold). Sub-400 D5 confirmed at 358 m³/s.

No flood-risk implications. Lac Coulonge etat 0, 101 cm below pre-alert. §15.3.5.1 trigger inactive.

---

## Notes

- **Day 203** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (167 days stale). `freshet-forecast.json` regenerated without change. W46 HQ item 4 remains open.
- **Des Joachims ORRPB daily Nov 21: 0 m³/s** — placeholder zero per known artifact class. Treat as "not yet reported." Nov 20 finalized at 451 m³/s.
- **Témiscaming PSPC/ORRPB discrepancy note:** both values derive from PSPC (orrpb_river_flows.temiscaming agency=PSPC). The 67 m³/s gap is midnight T00 vs partial-day mean, not a cross-source discrepancy. Preferred value for "today": PSPC T00 = 384 m³/s.
- **Mattawa Nov 20 retro:** prov 152.30 m in yesterday's brief → finalized 152.34 m (+4 cm, within ±5 cm, CONFIRMED). Normal provisional revision.
