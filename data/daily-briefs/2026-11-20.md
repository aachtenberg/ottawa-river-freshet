# Daily brief — 2026-11-20

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 116b). ORRPB conditions forecast HTTP 200 ✓ (page fetched; forecast unchanged — last update Nov 17). Vigilance 1195: proxy ingest fresh T21 UTC Nov 20. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 20.*

*Nov 19 retro: Témiscaming provisional 334 m³/s → finalized **365 m³/s** (+31 m³/s, within 50 m³/s threshold — CONFIRMED sub-400; D4 confirmed). Nov 19 Mattawa ORRPB daily revised 152.26 → **152.32 m** (+6 cm, outside ±5 cm threshold — REVISED; direction essentially flat, no flood significance).*

---

## In plain language

### Upstream — the upper basin

The upper basin remains in a quiet late-autumn posture, 202 days past the May 2 freshet peak of 2,741 cubic metres per second. Outflow from Lake Timiskaming — the first major pinch point below the northern headwaters — came in today at 386 cubic metres per second in the PSPC operator measurement, with the ORRPB independently reporting 377 m³/s (a 9 m³/s gap, well within normal agreement). That is Day 5 of the current sub-400 m³/s streak that began November 16. Yesterday's provisional reading of 334 m³/s revised upward to 365 m³/s once finalized — still sub-400, streak continues.

All fourteen storage reservoirs continue their quiet late-season holding posture: thirteen are within two centimetres of yesterday, with only Poisson Blanc edging up three centimetres again. Mattawa slipped two centimetres to 152.30 metres today (note: yesterday's provisional of 152.26 m revised upward to 152.32 m once finalized — essentially flat, not declining as the provisional suggested). Pembroke eased one centimetre to 111.06 metres. Neither move has flood significance.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge recorded 106.000 metres at 9 PM UTC on November 20, about one centimetre below yesterday's reading. The lake sits a full metre below the first alert threshold — firmly in normal, non-event conditions.

The generating station at Bryson — reached by the long channel winding south from Lac Coulonge — held essentially unchanged overnight: total release 351 m³/s, turbines producing 297 m³/s, with the remaining 54 m³/s passing through the spillway (about 15% of the total). The dam pond behind Bryson edged up one centimetre to 105.55 metres, now 88 centimetres above the normal operating ceiling. This is Day 176 of the headpond sitting above that band; it is an ongoing baseline condition, not a new development.

The ORRPB weekly forecast, last updated Monday November 17, calls for flows to "remain fairly stable or slightly decrease over the coming week, depending on locations." Next update is expected November 24. No change from yesterday.

---

## TL;DR

**RETRO: Nov 19 Témiscaming prov 334 → final 365 m³/s (CONFIRMED sub-400, D4); Nov 19 Mattawa prov 152.26 → final 152.32 m (REVISED +6 cm, outside ±5 cm threshold; direction essentially flat, no flood significance).** **Today (Day 202):** Lac Coulonge T21 **106.000 m** (−0.9 cm vs T21 yesterday; etat 0, 100 cm below pre-alert). Bryson T19: total **351.15 m³/s** (+0.03%), spill **53.73** (15.3%, unchanged), headpond **105.55 m** (+1 cm; Day 176 above band). §15.3.5.1 trigger INACTIVE **Day 179** (Hull 41.25 m). Carillon T20 **1011.99 m³/s** (+18.9% vs yesterday T19 851.31 — step-up reversing recent step-down; flag). Témiscaming sub-400 streak: D4 finalized (Nov 19=365), D5 provisional (Nov 20=386 PSPC / 377 ORRPB; gap 9 m³/s, within 50). Reservoir balance: **0 falling · 13 steady · 1 rising**. ORRPB weekly forecast unchanged from Nov 17; next update Nov 24.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 20 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 20 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 20) | **106.000 m** |
| ORRPB daily Nov 20 (provisional) | 106.00 m |
| ORRPB daily Nov 19 (finalized) | 106.01 m |
| 24h delta (Vigilance T21 Nov 20 vs T21 Nov 19) | **−0.9 cm** (106.000 vs 106.009 m) |
| ORRPB daily delta (Nov 19 final 106.01 → Nov 20 prov 106.00) | −1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 100 cm below |
| Distance to minor flood (107.50 m) | 150 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 (releases) / T20 (levels) UTC Nov 20. Yesterday: T20/T20 Nov 19 (from prior brief).*

| Metric | Today (T19/T20 Nov 20) | Yesterday (T20/T20 Nov 19) | Δ |
|---|---|---|---|
| Total release (m³/s) | **351.15** | 351.03 | +0.12 (+0.03%) |
| Turbined (m³/s) | **297.41** | 297.33 | +0.08 (+0.03%) |
| Spilled (m³/s) | **53.73** | 53.71 | +0.02 (+0.04%) |
| Spill share (%) | **15.3%** | 15.3% | 0 pp |
| Headpond / amont (m) | **105.55** (T20) | 105.54 (T20 Nov 19) | +1 cm |
| Tailwater / aval (m) | **86.94** (T20) | 86.94 (T20 Nov 19) | 0 cm |
| Δh (head differential, m) | **18.61** | 18.60 | +1 cm |

No change exceeds 5% threshold. Headpond 105.55 m = **88 cm above** the 104.67 m band ceiling (Day 176 above band). Stable run-of-river dispatch.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 20.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **219.46** T19 | 0% |
| Quinze (3-31) | **221.31** T20 | 0.5% (1.06 m³/s) |
| Îles (3-32) | **228.51** T20 | 0% |
| Rapide-2 (3-29) | **157.62** T20 | 0% |
| Rapide-7 (3-28) | **157.79** T20 | 0% |
| Bryson (3-46) | **351.15** T19 | **15.3%** (53.73 m³/s) |
| Paugan — Gatineau R. (3-65) | **159.04** T20 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **171.79** T20 | 0% |
| Carillon — basin terminal (3-60) | **1011.99** T20 | 0% (**+18.9%** vs yesterday T19 851.31 m³/s — step-up reversing recent step-down; flag) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 13) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 20 — ORRPB daily provisional (m³/s) | **377** | 412 (Nov 13) | −35 | D5 provisional sub-400; D1=Nov 16 (366), D2=Nov 17 (375), D3=Nov 18 (381 fin), D4=Nov 19 (365 fin) |
| Témiscaming PSPC cross-check (m³/s) | **386** T00 Nov 20 | — | — | 9 m³/s gap vs ORRPB (consistent; <50 m³/s threshold); PSPC preferred for today |
| Quinze release → into lake (m³/s) | **221.31** (T20) | — | — | Steady baseload; trace spill 1.1 m³/s |
| Mattawa level (m) | **152.30** (Nov 20 prov) | 152.32 (Nov 13 est) | — | −2 cm vs Nov 19 finalized (152.32); note Nov 19 prov 152.26 REVISED to 152.32 |
| Pembroke level (m) | **111.06** (Nov 20) | 111.09 (Nov 13 est) | −3 cm | −3 cm vs Nov 19 finalized (111.09); slowly declining |

**Reservoir balance (T00 Nov 19 → T00 Nov 20):**

| Reservoir | Nov 19 (T00) | Nov 20 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.26 m | **219.25 m** | −1 cm | Steady |
| Dozois | 342.09 m | **342.08 m** | −1 cm | Steady |
| Témiscaming | 178.61 m | **178.63 m** | +2 cm | Steady |
| Bark Lake | 313.52 m | **313.52 m** | 0 cm | Steady |
| Des Joachims | 152.09 m | **152.11 m** | +2 cm | Steady |
| Poisson Blanc | 200.34 m | **200.37 m** | +3 cm | Rising (below 10 cm/day flag) |
| Rapide-7 | 309.00 m | **308.99 m** | −1 cm | Steady |
| Others (7) | — | — | −2 to +1 cm | Steady |

**Balance: 0 falling · 13 steady · 1 rising (Poisson Blanc +3 cm, below 10 cm/day flag).** Normal late-season holding posture.

**Milestone bookkeeping (W46 rollup Nov 15 anchor + corrected daily chain via DB):**

| Milestone | W46 close (Nov 15) | Nov 16 | Nov 17 | Nov 18 | Nov 19 | **Nov 20** |
|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 197 | 198 | 199 | 200 | 201 | **202** |
| Bryson amont above band (104.67 m) | 171 | 172 | 173 | 174 | 175 | **176** |
| §15.3.5.1 trigger INACTIVE | 174 | 175 | 176 | 177 | 178 | **179** |
| Témiscaming sub-400 streak | *new D1 Nov 16 (366)* | D1: 366 | D2: 375 fin | D3: 381 fin | D4: 365 fin (prov 334→fin 365) | **D5 prov: 386 PSPC** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 20.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.25 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 179** (136 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 20.*

| Reservoir | Nov 19 (T00) | Nov 20 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.26 m | **219.25 m** | −1 cm | Steady |
| Témiscaming | 178.61 m | **178.63 m** | +2 cm | Steady |
| Dozois | 342.09 m | **342.08 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.52 m | **313.52 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (page fetched). Last Update: 2026-11-17 2:49 PM EST (2026-11-17T19:49:00Z UTC). Next Update: 2026-11-24 4:00 PM EST (2026-11-24T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` updated with mode=`weekly-notice`.*

**Unchanged from Nov 17 brief (no new ORRPB update expected until Nov 24):**

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Carillon dispatch step-UP +18.9%.** T20 1011.99 vs yesterday T19 851.31 m³/s = +160.68 (+18.9%; flag: >5%). Reverses the third consecutive step-down flagged in prior briefs (−12.1% Nov 18, −16.4% Nov 19). Turbines handling all flow (0% spill). Routine HQ dispatch adjustment; no flood implication, no headpond or regulatory consequence.
2. **RETRO — Nov 19 Mattawa REVISED.** ORRPB daily Nov 19 reported 152.26 m in yesterday's brief; finalized 152.32 m (+6 cm revision, outside ±5 cm threshold). Direction: essentially flat (Nov 18 final 152.31 → Nov 19 final 152.32 m; +1 cm), no flood significance.
3. **RETRO — Nov 19 Témiscaming CONFIRMED.** Provisional 334 → finalized 365 m³/s (+31 m³/s; within 50 m³/s threshold). Sub-400 streak D4 confirmed at 365 m³/s.
4. **Paugan (3-65) total_cms now populated.** Yesterday's brief noted `total_cms null`; today shows 159.04 m³/s (matches turbined). Apparent one-day data gap in that field, now resolved.

No flood-risk implications. Lac Coulonge etat 0, 100 cm below pre-alert. §15.3.5.1 trigger inactive.

---

## Notes

- **Day 202** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (166 days stale). `freshet-forecast.json` regenerated without change. W46 HQ item 4 remains open.
- **Témiscaming PSPC/ORRPB agreement:** 386 vs 377 m³/s for Nov 20 (9 m³/s gap; within 50 threshold — consistent).
- **Mattawa Nov 19 revision detail:** provisional 152.26 m in yesterday's brief; DB finalized 152.32 m (+6 cm). This is within the range of normal ORRPB provisional-to-final revisions at Mattawa seen in W45–W46; no structural concern.
