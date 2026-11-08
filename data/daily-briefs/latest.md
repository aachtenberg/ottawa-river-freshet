# Daily brief — 2026-11-08

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 223631b). ORRPB forecast HTTP 200 ✓ — last update Nov 3 2:09 PM EST; next update Nov 10 4:00 PM EST (weekly cadence, unchanged). Vigilance 1195: proxy ingest fresh T21 UTC Nov 8 (105.995 m). V3 posterior: ran successfully (exit 0) — `freshet-forecast.json` content unchanged (anchors on asof 2026-06-07; unchanged until `lac-coulonge-daily-1990-2026.csv` is extended). Detached HEAD at session start (recurrence; self-corrected via `git checkout main && git pull origin main` before commit).*

*Nov 7 retro-checks: **Nov 7 Témiscaming ORRPB provisional 417 → final 390 m³/s** (−27 m³/s, within 50 m³/s tolerance — **CONFIRMED sub-400 D51**). **CORRECTION — Nov 5 Témiscaming tertiary DB revision:** `orrpb_river_flows` now shows **397 m³/s** for Nov 5 (yesterday's brief saw 413 m³/s, declaring the sub-400 streak ended at D48; today's DB restores the original 397 value, restoring the streak through D51). Yesterday's voiding of D49–D51 is reversed — see streak table below. **Nov 7 Mattawa ORRPB daily: claimed 152.43 m (Rise D1) → finalized 152.37 m** (−2 cm from Nov 6 finalized 152.39 m; "Rise D1" claim voided — Nov 7 was a slight decline). Nov 7 ORRPB Lac Coulonge: 105.97 m (unchanged — no revision). Nov 7 Pembroke: DB now shows 111.11 m (yesterday's brief reported 111.07 m; +4 cm small revision, below ±5 cm confirmation threshold).*

---

## In plain language

### Upstream — the upper basin

The basin is 190 days past the May 2 seasonal peak. Today's preliminary outflow from Lake Timiskaming came in at 418 cubic metres per second, which is above the 400 m³/s mark. However, today's brief carries an important correction to yesterday's: the database had briefly shown the November 5 flow as 413 m³/s when yesterday's routine ran, which led yesterday to prematurely declare the sub-400 streak broken at Day 48. Today's database restores November 5 to 397 m³/s (sub-400), extending the confirmed streak to Day 51 (November 7, finalized at 390 m³/s). If today's provisional 418 m³/s holds through finalization, it would be the first above-400 day since September 17 — ending a 51-day unbroken run.

Mattawa, an upstream gauge roughly 200 kilometres above the properties, fell 10 centimetres overnight to 152.27 metres. Yesterday's report of a "Day 1 rise" at Mattawa was based on a preliminary reading that finalized lower than reported: November 7 finalized at 152.37 metres, itself down 2 centimetres from November 6; the upstream reach continues to slowly decline. Pembroke, further downstream, also edged down 4 centimetres to 111.07 metres. Among the basin's tracked reservoirs, two rose slightly overnight (Lady Evelyn and Poisson Blanc, each up 3–4 centimetres), twelve held steady, and none fell. Normal late-season posture.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 105.995 metres at 9 PM UTC — up roughly 2 centimetres from the same hour yesterday (105.977 m). The ORRPB daily series puts it at 105.99 metres for today, also up 2 centimetres from yesterday's finalized 105.97 metres. The lake is fully in normal conditions — 101 centimetres below the 107.00-metre pre-alert threshold. The gentle continuing rise is consistent with the weekly forecast's expectation of slight increases at some locations; nothing anomalous.

Well downstream, at the Bryson Generating Station — a facility reached via a long winding channel well below the southern tip of Lac Coulonge, not visible from the Mansfield/Fort-Coulonge properties — today is the seventh consecutive day of partial spillway release. Approximately 190 cubic metres per second is now running through the spillway, 48.3% of the total 393 m³/s release, up from 45.2% yesterday. Both the total release and the spilled fraction increased by more than the reporting threshold (5%) from yesterday, while the turbine output held essentially flat. The dam pond at Bryson dropped 4 centimetres to 105.57 metres. At Carillon, the basin's terminal dam, today's late-afternoon reading was around 883 m³/s — a step down from yesterday's 952 m³/s reading, consistent with the normal range of power-dispatch scheduling. No spillway involvement at any location downstream of Bryson.

---

## TL;DR

**CORRECTIONS (streak restoration + retros):** Nov 5 Témiscaming DB restored 413 → **397 m³/s** (sub-400); sub-400 streak D49–D51 reinstated (D49 Nov 5 = 397, D50 Nov 6 = 381, D51 Nov 7 = 390 final). Yesterday's "streak ended D48" voided. Nov 7 Témiscaming retro: provisional 417 → **final 390 m³/s** (within 50 m³/s — CONFIRMED sub-400 D51). Nov 7 Mattawa retro: provisional 152.43 → **final 152.37 m** (down 2 cm from Nov 6; Rise D1 voided). **Today (Day 190):** Lac Coulonge T21 **105.995 m** (+2 cm vs T21 yesterday; etat 0, 101 cm below pre-alert). Bryson Day 7 spill: **48.3%** (189.99 m³/s, +22.36/+13.3% ⚠; total +6.0% ⚠). Carillon T19 **882.74 m³/s** (vs yesterday T20 952 = −69 m³/s / −7.2% ⚠; dispatch step-down). Témiscaming **provisional 418 m³/s** (PSPC agrees — no discrepancy; +28/+7.2% vs Nov 7 final 390, below sanity-check thresholds). **If 418 finalizes above 400, streak ends at D51 (Sep 18 – Nov 7).** Mattawa ORRPB daily **152.27 m** (−10 cm from finalized Nov 7 152.37 — continuing decline). Pembroke **111.07 m** (−4 cm). Hull dock T20 **41.22 m** — trigger INACTIVE **Day 167**. Reservoir balance: **0 falling · 12 steady · 2 rising** (lady_evelyn +3 cm, poisson_blanc +4 cm). ORRPB forecast unchanged (Nov 3; next Nov 10).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 8 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 8 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 8) | **105.995 m** |
| ORRPB daily Nov 8 | 105.99 m (provisional from T00) |
| 24h delta (Vigilance T21 Nov 8 vs T21 Nov 7) | **+2 cm** |
| ORRPB daily delta (Nov 7 finalized 105.97 → Nov 8 provisional 105.99) | +2 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 101 cm below |
| Distance to minor flood (107.50 m) | 151 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Nov 8 (releases), T20 UTC Nov 8 (levels). Yesterday: T20 UTC Nov 7.*

| Metric | Today (T19 Nov 8) | Yesterday (T20 Nov 7) | Δ |
|---|---|---|---|
| Total release (m³/s) | **393.27** | 371.05 | **+22.22 (+6.0%)** ⚠ |
| Turbined (m³/s) | **203.29** | 203.41 | −0.12 (0.0%) |
| Spilled (m³/s) | **189.99** | 167.63 | **+22.36 (+13.3%)** ⚠ |
| Spill share (%) | **48.3%** | 45.2% | +3.1 pp |
| Headpond / amont (m) | **105.57** (T20) | 105.61 (T20 Nov 7) | −4 cm |
| Tailwater / aval (m) | **86.98** (T20) | 86.89 (T20 Nov 7) | +9 cm |
| Δh (head differential, m) | **18.59** | 18.72 | −13 cm |

Total release up 6.0% and spilled up 13.3% (both exceed 5% flag). Day 7 of partial spill — spill share growing while headpond edges down 4 cm to 105.57 m. Headpond 105.57 m = **90 cm above** the 104.67 m band ceiling — **Day 164** above band.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 8.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **220.18** T20 | 0% |
| Quinze (3-31) | **210.90** T20 | 0.4% |
| Îles (3-32) | **218.17** T19 | 0% |
| Rapide-2 (3-29) | **158.10** T20 | 0% |
| Rapide-7 (3-28) | **156.42** T19 | 0% |
| Bryson (3-46) | **393.27** T19 | **48.3%** (Day 7 spill, growing) |
| Paugan — Gatineau R. (3-65) | **161.47** T19 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **173.87** T19 | 0% |
| Carillon — basin terminal (3-60) | **882.74** T19 | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 1) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 8 provisional — ORRPB (m³/s) | **418** | 306 (Nov 1) | +112 | Provisional above 400; if confirmed, **streak ends at D51 (Sep 18 – Nov 7)** |
| Témiscaming Nov 8 — PSPC T00 cross-check (m³/s) | **418** | — | No discrepancy (sources agree) | — |
| Quinze release → into lake (m³/s) | **210.90** (T20) | — | — | Baseload; stable |
| Mattawa level (m) | **152.27** (Nov 8 ORRPB daily) | — | −10 cm vs finalized Nov 7 152.37 | Continuing decline; Nov 7 "Rise D1" voided by retro (see below) |
| Pembroke level (m) | **111.07** (Nov 8 ORRPB daily) | — | −4 cm vs finalized Nov 7 111.11 | Direction only |

**PSPC cross-check note — Témiscaming Nov 8:** orrpb_river_flows = 418 m³/s; PSPC T00 reservoir_readings = 418 m³/s. Sources agree exactly — no discrepancy flag.

**Provisional-flow sanity check (Témiscaming ORRPB Nov 8 = 418 m³/s):** Change vs Nov 7 final (390 m³/s) = +28 m³/s (+7.2%) — below both ≥25% and ≥150 m³/s thresholds. Formal sanity check NOT required.

**RETRO — Nov 7 Témiscaming ORRPB:** Yesterday's brief provisionally claimed 417 m³/s. Finalized: **390 m³/s** (−27 m³/s, within 50 m³/s tolerance — **CONFIRMED sub-400 D51**).

**TERTIARY DB REVISION — Nov 5 Témiscaming:** `orrpb_river_flows` now shows **397 m³/s** for Nov 5 (yesterday's brief saw 413 m³/s and voided the streak at D48; today's DB restores the original pre-revision value). Authoritative DB today: D45 (Nov 1, 306) → D46 (Nov 2, 353) → D47 (Nov 3, 351) → D48 (Nov 4, 358) → D49 (Nov 5, 397) → D50 (Nov 6, 381) → D51 (Nov 7, 390). Yesterday's "streak ended D48" label is voided.

**RETRO — Nov 7 Mattawa:** Yesterday's brief reported 152.43 m (+4 cm, Rise D1). Finalized: **152.37 m** (−2 cm from Nov 6 finalized 152.39 m). The "Rise D1" claim is voided — Nov 7 was a slight decline. Today Nov 8 = 152.27 m (−10 cm), continuing the declining trend.

**Reservoir balance (T00 Nov 7 → T00 Nov 8):**
0 falling · 12 steady · 2 rising (lady_evelyn +3 cm, poisson_blanc +4 cm). Normal late-season operations; no active retention signal (all well below 10 cm/day threshold).

**Milestone bookkeeping (W44 rollup anchor Nov 1 + daily extension):**

| Milestone | W44 close (Nov 1) | Nov 2 | Nov 3 | Nov 4 | Nov 5 | Nov 6 | Nov 7 | **Nov 8** |
|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 183 | 184 | 185 | 186 | 187 | 188 | 189 | **190** |
| Bryson amont above band (104.67 m) | 157 | 158 | 159 | 160 | 161 | 162 | 163 | **164** |
| §15.3.5.1 trigger INACTIVE | 160 | 161 | 162 | 163 | 164 | 165 | 166 | **167** |
| Témiscaming | D45 (306) | D46 (353) | D47 (351) | D48 (358) | D49 (397) **← restored** | D50 (381) | D51 (390) **← RETRO confirmed** | **418 prov (above 400; streak D51 pending finalization)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 8.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.22 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 167** (139 cm below trigger; −6 cm from yesterday) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 8.*

| Reservoir | Nov 7 (T00) | Nov 8 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.20 m | **219.21 m** | +1 cm | Steady |
| Témiscaming | 178.67 m | **178.65 m** | −2 cm | Steady (within ±2 cm; consistent with outflow ≈ inflow) |
| Dozois | 342.03 m | **342.04 m** | +1 cm | Steady |
| Bark Lake (OPG) | 313.58 m | **313.58 m** | 0 cm | Steady |

All 14 tracked reservoirs (including timiskaming_haileybury as WSC level gauge): 0 falling · 12 steady · 2 rising (lady_evelyn +3 cm, poisson_blanc +4 cm). No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. Last Update: 2026-11-03 2:09 PM EST (2026-11-03T19:09:00Z UTC). Next Update: 2026-11-10 4:00 PM EST (2026-11-10T21:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief** (Nov 3 update):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to slightly increase or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **CORRECTION — Nov 5 Témiscaming tertiary DB revision:** `orrpb_river_flows` now shows **397 m³/s** for Nov 5 (down from the transient 413 m³/s seen at yesterday's run time). Sub-400 streak restored: D49 (Nov 5 = 397), D50 (Nov 6 = 381), D51 (Nov 7 = 390 final). Yesterday's "streak ended D48" voided.
2. **CORRECTION — Témiscaming Nov 7 retro:** Provisional 417 → **final 390 m³/s** (within 50 m³/s — CONFIRMED sub-400 D51).
3. **CORRECTION — Mattawa Nov 7 retro:** Provisional 152.43 m → **final 152.37 m** (down 2 cm from Nov 6; Rise D1 claim voided). Today 152.27 m — continuing decline.
4. **Potential sub-400 streak end:** Témiscaming Nov 8 provisional = 418 m³/s (above 400). If confirmed, streak ends at D51 (Sep 18 – Nov 7). Provisional-flow sanity check: +7.2% / +28 m³/s — below thresholds; number is plausible. PSPC T00 agrees exactly. Watch for finalization in tomorrow's retro.
5. **Bryson spill Day 7 ≥5% flags:** Total +6.0% and spilled +13.3% (both exceed 5% flag). Spill share 48.3%; headpond −4 cm to 105.57 m. Ongoing condition; no property-reach implication.
6. **Carillon dispatch step-down:** T19 Nov 8 = 882.74 m³/s vs yesterday T20 = 951.79 m³/s (−69 m³/s / −7.2%). Exceeds 5% threshold. Same pattern as the reverse step-up flagged yesterday; routine power-dispatch scheduling, no spill.

No flood-risk implications. Lac Coulonge etat 0, 101 cm below pre-alert.

---

## Notes

- **Sub-400 streak tertiary revision pattern:** This is the third distinct value seen for the Nov 5 Témiscaming daily mean across successive brief runs: 397 (original, Nov 6 brief) → 397 (Nov 6) → 413 (at Nov 7 run time, led to streak voiding) → 397 (today). The 413 appears to have been a transient DB state that ORRPB corrected. This is the second secondary/tertiary revision in two weeks (Oct 26 Otto Holden was the other). Consider: the retro should wait 48 h (reading T-2 days) to capture stabilized finals — the two-revision pattern suggests T-1 finalization is not always stable.
- **Mattawa correction note:** Nov 7 finalized 152.37 m (−2 cm from Nov 6 152.39 m). The brief correctly provisioned 152.43 m (+4 cm) but the final landed below the prior day. At T-1 hour from the ORRPB midnight update, the daily mean is not yet settled; the same applies to any ORRPB river-levels station.
- **Pembroke small revision:** DB now shows Nov 7 = 111.11 m (yesterday's brief reported 111.07 m; +4 cm small revision, within normal rounding). Today 111.07 m (−4 cm from finalized Nov 7).
- **Detached HEAD:** Self-corrected via `git checkout main && git pull origin main` before writing today's brief. Fast-forward merge with 19 commits ahead (the agent-review-permissions PR merged since yesterday's branch diverged). Recurrence continues (W44 HQ item 2 unresolved).
- **V3 posterior:** Script ran (exit 0); `freshet-forecast.json` regenerated (content unchanged from prior commit — asof 2026-06-07; all threshold probabilities = 1.0). Will update once `lac-coulonge-daily-1990-2026.csv` is extended past the freshet season.
