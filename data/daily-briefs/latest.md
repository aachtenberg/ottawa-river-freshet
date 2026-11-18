# Daily brief — 2026-11-18

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 2.5KB). ORRPB conditions pages HTTP 200 ✓ (all three pages, 119–129 KB — back online after Nov 17 outage). Vigilance 1195: proxy ingest fresh T21 UTC Nov 18. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 18.*

*Nov 17 retro: PSPC T00 provisional 414 m³/s (D3 of streak starting Nov 15, per yesterday's TL;DR) → finalized **375 m³/s** (sub-400). D3 confirmed. However — W46 rollup streak table also carried errors from provisional data: "Nov 14 D58=419" → Nov 14 finalized **389 m³/s** (sub-400); "Nov 15 D1=386" → Nov 15 finalized **401 m³/s** (above 400). The 57-day streak broke on **Nov 13 (412 m³/s)**, not Nov 14. The current sub-400 streak started **Nov 16 (D1=366)**, not Nov 15. Yesterday's TL;DR labelling of D3 is therefore off by one — Nov 17 (375) = D2, not D3. Corrected bookkeeping below.*

---

## In plain language

### Upstream — the upper basin

The upper basin is in a quiet late-season posture, 200 days past the May 2 freshet peak. The outflow from Lake Timiskaming — the first major pinch point below the northern headwaters — was at 341 cubic metres per second in the overnight preliminary reading, with the past three finalized days (November 16–17 plus the day before) all running below 400 m³/s. That sub-400 streak now reaches a third confirmed day, with today's provisional figure pointing to a fourth. All fourteen storage reservoirs are uniformly flat — thirteen within a centimetre of yesterday, one (Poisson Blanc) up by three centimetres — a typical November holding pattern with no active refill surge.

Upstream at Mattawa, the daily level ticked up five centimetres relative to yesterday's finalized value (152.37 m), continuing the oscillatory low-amplitude pattern that has characterized this gauge all November. Pembroke slipped two centimetres to 111.07 m. Neither move has flood significance; both reflect the routine variability of a river running well within seasonal norms.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge recorded 106.016 metres at 9 PM UTC on November 18, dropping about one half-centimetre from the same hour yesterday. The lake sits nearly a full metre below the first alert threshold and a metre and a half below the minor-flood mark — firmly in normal, non-event conditions.

The generating station at Bryson — reached by the long channel winding south from Lac Coulonge — maintained steady output overnight. Turbine output was essentially unchanged; the small decline in total flow came entirely from a reduced spillway share (now around 15% of total release, down from about 18% yesterday). The dam pond behind Bryson edged up two centimetres to 105.56 metres, now 89 centimetres above the normal operating ceiling — the 174th consecutive day above that band.

The ORRPB weekly forecast, last updated Monday November 17, calls for flows to "remain fairly stable or slightly decrease over the coming week" — a minor softening from the prior update's "remain fairly stable." Next update is expected November 24.

---

## TL;DR

**RETRO: W46 rollup streak boundaries corrected by finalized data — 57-day streak broke Nov 13 (412 m³/s, not Nov 14); current sub-400 streak D1=Nov 16 (366), D2=Nov 17 (375 finalized), D3=Nov 18 provisional (341 — below 380 uncertainty threshold, treated as reliable).** **Today (Day 200):** Lac Coulonge T21 **106.016 m** (−0.6 cm vs T21 yesterday; etat 0, 98 cm below pre-alert). Bryson T19: total **351.43 m³/s** (−2.5%), spill **53.78** (15.3%, −15.9% — flag), headpond **105.56 m** (+2 cm; Day 174 above band). §15.3.5.1 trigger INACTIVE **Day 177** (Hull 41.24 m). Carillon T20 **1018.9 m³/s** (−12.1% vs yesterday T20 1158.80 m³/s — routine dispatch step-down). Témiscaming sub-400 streak: D2 finalized (Nov 17=375), D3 provisional (Nov 18=341). Reservoir balance: **0 falling · 13 steady · 1 rising**. ORRPB weekly forecast updated Nov 17; next update Nov 24.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 18 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 18 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 18) | **106.016 m** |
| ORRPB daily Nov 18 (provisional) | 106.02 m |
| ORRPB daily Nov 17 (finalized) | 106.03 m |
| 24h delta (Vigilance T21 Nov 18 vs T21 Nov 17) | **−0.6 cm** (106.016 vs 106.022 m) |
| ORRPB daily delta (Nov 17 final 106.03 → Nov 18 prov 106.02) | −1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 98 cm below |
| Distance to minor flood (107.50 m) | 148 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 (releases) / T20 (levels) UTC Nov 18. Yesterday: T23 Nov 17 (releases) / T20 Nov 17 (levels).*

| Metric | Today (T19/T20 Nov 18) | Yesterday (T23/T20 Nov 17) | Δ |
|---|---|---|---|
| Total release (m³/s) | **351.43** | 360.59 | −9.16 (−2.5%) |
| Turbined (m³/s) | **297.66** | 296.61 | +1.05 (+0.4%) |
| Spilled (m³/s) | **53.78** | 63.98 | −10.20 (**−15.9%** — flag) |
| Spill share (%) | **15.3%** | 17.7% | −2.4 pp |
| Headpond / amont (m) | **105.56** (T20) | 105.54 (T20 Nov 17) | +2 cm |
| Tailwater / aval (m) | **86.94** (T20) | 86.99 (T20 Nov 17) | −5 cm |
| Δh (head differential, m) | **18.62** | 18.55 | +7 cm |

Spill decreased 15.9% (flag: >5%). Total release −2.5% (below 5% threshold — not independently flagged). Turbine output flat. Headpond 105.56 m = **89 cm above** the 104.67 m band ceiling (Day 174 above band). Normal run-of-river dispatch.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 18.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **212.5** T20 | 0% |
| Quinze (3-31) | **222.6** T20 | 0.4% (1.0 m³/s) |
| Îles (3-32) | **224.37** T19 | 0% |
| Rapide-2 (3-29) | **158.0** T20 | 0% |
| Rapide-7 (3-28) | **157.63** T19 | 0% |
| Bryson (3-46) | **351.43** T19 | **15.3%** (53.78 m³/s) |
| Paugan — Gatineau R. (3-65) | **159.09** T19 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **259.19** T20 | 0% |
| Carillon — basin terminal (3-60) | **1018.9** T20 | 0% (−12.1% vs yesterday T20 1158.80 m³/s — routine dispatch step-down) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 11) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 18 — ORRPB/PSPC provisional (m³/s) | **341** | 381 (Nov 11) | −40 | D3 prov sub-400 (below 380 uncertainty threshold — treated reliable); D1=Nov 16 (366), D2=Nov 17 (375 fin) |
| Témiscaming PSPC cross-check (m³/s) | **341** T00 Nov 18 | — | — | Consistent with ORRPB (no discrepancy) |
| Quinze release → into lake (m³/s) | **222.6** (T20) | — | — | Steady baseload; trace spill 1.0 m³/s |
| Mattawa level (m) | **152.37** (Nov 18) | 152.07 (Nov 11) | +30 cm | Oscillatory; +5 cm vs Nov 17 finalized (152.32); direction: low-amplitude variation |
| Pembroke level (m) | **111.07** (Nov 18) | — (not in 10-row window) | — | −2 cm vs Nov 17 (111.09); direction: slowly declining |

**W46 streak table corrections (from finalized data):**

| Date | Finalized flow | Status | W46 rollup claim | Correction |
|---|---|---|---|---|
| Nov 12 | 380 m³/s | sub-400 ✓ | — | — |
| Nov 13 | 412 m³/s | ABOVE 400 ✗ | "D57 of 57-day streak" | **Streak broke Nov 13 (not Nov 14)** |
| Nov 14 | 389 m³/s | sub-400 ✓ | "D58=419, streak broke" | 419 was provisional; 389 finalized = sub-400 |
| Nov 15 | 401 m³/s | ABOVE 400 ✗ | "D1=386 new streak" | 386 was provisional; 401 finalized = above 400 |
| Nov 16 | 366 m³/s | sub-400 ✓ | — | **D1 of current streak** |
| Nov 17 | 375 m³/s | sub-400 ✓ | D3 (of incorrect Nov 15 D1) | **D2 of current streak** |
| Nov 18 | 341 prov. | sub-400 (prov) | — | **D3 provisional** |

**Reservoir balance (T00 Nov 17 → T00 Nov 18):**

| Reservoir | Nov 17 (T00) | Nov 18 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.27 m | **219.27 m** | 0 cm | Steady |
| Dozois | 342.10 m | **342.10 m** | 0 cm | Steady |
| Témiscaming | 178.64 m | **178.63 m** | −1 cm | Steady |
| Bark Lake | 313.54 m | **313.54 m** | 0 cm | Steady |
| Des Joachims | 152.13 m | **152.08 m** | −5 cm | Steady (−2 cm within band; note: 5 cm gap may reflect T00 rounding) |
| Poisson Blanc | 200.27 m | **200.31 m** | +4 cm | Steady (below 10 cm/day flag threshold) |
| Rapide-7 | 309.00 m | **309.00 m** | 0 cm | Steady |
| Others (7) | — | — | 0 to −1 cm | Steady |

**Balance: 0 falling · 13 steady · 1 rising (Poisson Blanc +4 cm, below 10 cm/day flag).** Normal late-season holding posture.

**Milestone bookkeeping (W46 rollup anchor Nov 15 + 3 days via DB, corrected for finalized data):**

| Milestone | W46 close (Nov 15) | Nov 16 | Nov 17 | **Nov 18** |
|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 197 | 198 | 199 | **200** |
| Bryson amont above band (104.67 m) | 171 | 172 | 173 | **174** |
| §15.3.5.1 trigger INACTIVE | 174 | 175 | 176 | **177** |
| Témiscaming sub-400 streak (corrected) | *prior streak broke Nov 13 (412)* | D1: 366 | D2: 375 fin (W46 prov 414 → 375) | **D3 prov: 341** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 18.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.24 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 177** (137 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 18.*

| Reservoir | Nov 17 (T00) | Nov 18 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.27 m | **219.27 m** | 0 cm | Steady |
| Témiscaming | 178.64 m | **178.63 m** | −1 cm | Steady |
| Dozois | 342.10 m | **342.10 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.54 m | **313.54 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (128 KB; back online after Nov 17 outage). Last Update: 2026-11-17 2:49 PM EST (2026-11-17T19:49:00Z UTC). Next Update: 2026-11-24 4:00 PM EST (2026-11-24T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` updated with mode=`weekly-notice`.*

**Nov 17 weekly update (first retrieved today — was unreachable during the Nov 17 routine run):**

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums.*

**Change vs Nov 10 forecast:** "remain fairly stable over the coming week" → "remain fairly stable **or slightly decrease** over the coming week, **depending on locations**." Minor softening; no flood implication.

---

## Anomaly flags

1. **Bryson spill −15.9%** (53.78 vs 63.98 m³/s yesterday, −10.20 m³/s). Total release −2.5%. Turbines flat. Run-of-river dispatch adjustment; no headpond consequence (amont +2 cm, within normal variation). Day 174 of headpond above 104.67 m continues.
2. **W46 rollup streak table corrected:** finalized data moves the 57-day streak break to Nov 13 (412 m³/s) and current streak D1 to Nov 16. Yesterday's brief correctly held D3 as UNCERTAIN; now D2 (Nov 17=375) finalized and D3 (Nov 18=341 provisional) is below the 380 uncertainty threshold.

No flood-risk implications. Lac Coulonge etat 0, 98 cm below pre-alert. §15.3.5.1 trigger inactive.

---

## Notes

- **Day 200** since the May 2 freshet peak (2,741 m³/s).
- **ORRPB back online:** the Nov 17 weekly update was published at 2:49 PM EST but could not be retrieved during yesterday's run (HTTP 000 outage). Retrieved today; forecast/latest.json updated. Next update Nov 24.
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (165 days stale). `freshet-forecast.json` regenerated without change. W46 HQ item 4 remains open.
- **Des Joachims reservoir:** T00 Nov 18 reads 152.08 m vs Nov 17 152.13 m (−5 cm gap). The day-to-day jump is larger than typical rounding but within normal OPG operational variation; latest_reservoir_readings shows T00 Nov 18 = 152.08 and T00 flow 831 m³/s. Not flagged.
- **Témiscaming PSPC/ORRPB agreement:** both report 341 m³/s for Nov 18 — no cross-check discrepancy.
