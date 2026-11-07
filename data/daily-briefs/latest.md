# Daily brief — 2026-11-07

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 117b). ORRPB forecast HTTP 200 ✓ — last update Nov 3 2:09 PM EST; next update Nov 10 4:00 PM EST (weekly cadence, unchanged). Vigilance 1195: proxy ingest fresh T21 UTC Nov 7 (105.977 m). V3 posterior: ran successfully (exit 0) — `freshet-forecast.json` content unchanged (anchors on asof 2026-06-07; unchanged until `lac-coulonge-daily-1990-2026.csv` is extended). Detached HEAD at session start (recurrence; self-corrected via `git checkout main && git pull origin main` before commit).*

*Nov 6 retro-checks: **Nov 6 Témiscaming ORRPB provisional 367 → final 381 m³/s** (+14 m³/s, within 50 m³/s tolerance — **CONFIRMED sub-400**). **Nov 5 Témiscaming secondary DB revision: orrpb_river_flows now shows 413 m³/s for Nov 5** (up from 397 at yesterday's run time). Yesterday's "D49 confirmed sub-400 at 397" was correct against the DB at run time; the DB has since revised Nov 5 to 413 (above 400). Using today's DB as authoritative: the sub-400 streak ended at **D48 (Nov 4, 358 m³/s)**; Nov 5 = 413 (above), Nov 6 = 381 (sub-400, D1 of new run), Nov 7 = 417 provisional (above again). Yesterday's D50 label is accordingly voided. Nov 6 Mattawa ORRPB daily: claimed 152.43 m (provisional) → finalized **152.39 m** (−4 cm revision; Nov 6 was flat vs Nov 5 = 152.39, not a 4th consecutive rise). Today Nov 7 = 152.43 m (+4 cm, new rise D1). Nov 6 ORRPB Lac Coulonge: 105.94 m (unchanged — no revision).*

---

## In plain language

### Upstream — the upper basin

The basin is 189 days past the May 2 seasonal peak. The outflow from Lake Timiskaming today came in at 417 cubic metres per second as a preliminary daily figure — above the 400 m³/s mark that has served as a rough dividing line for recent weeks. That said, this is a correction-day: yesterday's brief reported a confirmed 50-day sub-400 streak through November 5, but the database has since revised the November 5 daily mean from 397 to 413 m³/s, moving it above 400. The streak's correct end date is November 4 (Day 48, at 358 m³/s). November 6 came in at 381 (sub-400, one day), and today's preliminary 417 is above 400 again. Flows are fluctuating in the 350–420 m³/s band — normal late-autumn recession, not a signal worth tracking as a streak for now.

The Mattawa gauge, an upstream indicator about 200 kilometres above Lac Coulonge, rose 4 centimetres overnight to 152.43 metres. Yesterday's claim of a "fourth consecutive rise" was based on a provisional November 6 reading that finalized flat (152.39 m = same as November 5); today's reading is a genuine rise and can be called Day 1 of a new upswing. Pembroke, further downstream, was essentially flat at 111.07 metres. Thirteen of the basin's tracked reservoirs were mostly quiet overnight: three rose slightly (Baskatong, Poisson Blanc, and Quinze, each up 3 centimetres), ten held steady, none fell meaningfully. No active storage event.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 105.977 metres at 9 PM UTC — up roughly 4 centimetres from the same hour yesterday (105.941 m). The ORRPB daily series puts it at 105.97 metres, up 3 centimetres from yesterday's finalized 105.94 metres. The lake is fully in normal conditions — 102 centimetres below the 107.00-metre pre-alert threshold. The gentle rise is consistent with the weekly forecast anticipating slight increases at some locations; nothing anomalous.

Well downstream, at the Bryson Generating Station (accessed via a long winding channel well below the southern tip of Lac Coulonge, not visible from the Mansfield properties), today is the sixth consecutive day of spillway release. Approximately 168 cubic metres per second is now running through the spillway — 45.2% of the total 371 m³/s release, up from 43.2% yesterday. The dam pond held at 105.61 metres, essentially flat. At Carillon, the basin's terminal dam, today's late-afternoon release measured around 952 m³/s — a step back up from yesterday's T19 reading of 752 m³/s, restoring the level seen on November 5. This is routine power-dispatch scheduling, with no spillway involvement and no flood-system implication.

---

## TL;DR

**CORRECTIONS (streak recount):** Nov 5 orrpb_river_flows DB-revised 397 → **413 m³/s** (above 400). Sub-400 streak ended D48 (Nov 4, 358 m³/s), not D50 as yesterday's brief tracked. Nov 6 Mattawa finalized at 152.39 m (flat vs Nov 5 — no 4th rise). **Today (Day 189):** Lac Coulonge T21 **105.977 m** (+4 cm vs T21 yesterday; etat 0, 102 cm below pre-alert). Bryson Day 6 spill: **45.2%** (167.63 m³/s, +12.93 / +8.4% ⚠ vs yesterday). Carillon T20 **951.79 m³/s** (step back up from yesterday T19 752; dispatch cycle). Témiscaming **provisional 417 m³/s** (ORRPB+PSPC agree — no discrepancy; +36/+9.4% vs Nov 6 final 381, below sanity-check thresholds). Mattawa ORRPB daily **152.43 m** (+4 cm from finalized Nov 6 152.39 — new rise D1). Pembroke **111.07 m** (−1 cm, flat). Hull dock T20 **41.28 m** — trigger INACTIVE **Day 166**. Reservoir balance: **0 falling · 10 steady · 3 rising** (baskatong +3 cm, quinze +3 cm, poisson_blanc +3 cm). ORRPB forecast unchanged (Nov 3; next Nov 10).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 7 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 7 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 7) | **105.977 m** |
| ORRPB daily Nov 7 | 105.97 m (provisional from T00) |
| 24h delta (Vigilance T21 Nov 7 vs T21 Nov 6) | **+4 cm** |
| ORRPB daily delta (Nov 6 finalized 105.94 → Nov 7 provisional 105.97) | +3 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 102 cm below |
| Distance to minor flood (107.50 m) | 152 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 UTC Nov 7. Yesterday: T20 UTC Nov 6.*

| Metric | Today (T20 Nov 7) | Yesterday (T20 Nov 6) | Δ |
|---|---|---|---|
| Total release (m³/s) | **371.05** | 358.22 | +12.83 (+3.6%) |
| Turbined (m³/s) | **203.41** | 203.52 | −0.11 (0.0%) |
| Spilled (m³/s) | **167.63** | 154.70 | **+12.93 (+8.4%)** ⚠ |
| Spill share (%) | **45.2%** | 43.2% | +2.0 pp |
| Headpond / amont (m) | **105.61** (T20) | 105.59 (T20 Nov 6) | +2 cm |
| Tailwater / aval (m) | **86.89** (T20) | 86.83 (T20 Nov 6) | +6 cm |
| Δh (head differential, m) | **18.72** | 18.76 | −4 cm |

Spilled m³/s up 8.4% (exceeds 5% flag). Day 6 of partial spill — share growing while headpond holds nearly flat at 105.61 m. Headpond 105.61 m = **94 cm above** the 104.67 m band ceiling — **Day 163** above band.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 7. Yesterday comparison: T19–T20 UTC Nov 6.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **220.82** T20 | 0% | −3.62 (−1.6%) |
| Quinze (3-31) | **211.32** T20 | 0.4% | −0.33 (flat) |
| Îles (3-32) | **216.32** T19 | 0% | −0.13 (flat) |
| Rapide-2 (3-29) | **240.05** T20 | 0% | −1.50 (flat) |
| Rapide-7 (3-28) | **157.10** T20 | 0% | −1.29 (flat) |
| Bryson (3-46) | **371.05** T20 | **45.2%** | +12.83 (+3.6%); spill Day 6, growing |
| Paugan — Gatineau R. (3-65) | **161.21** T19 | 0% | +0.40 (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **176.25** T20 | 0% | +2.68 (+1.5%) |
| Carillon — basin terminal (3-60) | **951.79** T20 | 0% | vs yesterday T19 752 (+200; step-back-up from dispatch step-down) † |

† Carillon T20 Nov 7 (952 m³/s) is consistent with Nov 5 T20 (~957); yesterday's T19 (752) was the lower end of a dispatch cycle. No spill in either direction; routine scheduling. Net day-over-day at same hour-of-day: essentially flat (~−5 m³/s vs Nov 5 T20).

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 31) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 7 provisional — ORRPB (m³/s) | **417** | 318 (Oct 31) | +99 | Above 400; see streak correction below |
| Témiscaming Nov 7 — PSPC T00 cross-check (m³/s) | **417** | — | No discrepancy (sources agree) | — |
| Quinze release → into lake (m³/s) | **211.32** (T20) | 317 (Oct 31 Carillon) | — | Baseload; stable |
| Mattawa level (m) | **152.43** (Nov 7 ORRPB daily) | — | +4 cm vs Nov 6 finalized 152.39 | **New rise D1** (Nov 6 finalized flat; "4th rise" claim voided) |
| Pembroke level (m) | **111.07** (Nov 7 ORRPB daily) | — | −1 cm vs Nov 6 finalized 111.08 | Flat; direction only |

**PSPC cross-check note — Témiscaming Nov 7:** orrpb_river_flows = 417 m³/s; PSPC T00 reservoir_readings = 417 m³/s. Sources agree exactly — no discrepancy flag.

**Provisional-flow sanity check (Témiscaming ORRPB Nov 7 = 417 m³/s):** Change vs Nov 6 final (381 m³/s) = +36 m³/s (+9.4%) — below both ≥25% and ≥150 m³/s thresholds. Formal sanity check NOT required.

**RETRO — Nov 6 Témiscaming ORRPB:** Yesterday's brief provisionally claimed 367 m³/s. Finalized: **381 m³/s** (+14 m³/s, within 50 m³/s tolerance — **CONFIRMED sub-400**).

**SECONDARY DB REVISION — Nov 5 Témiscaming:** orrpb_river_flows now shows **413 m³/s** for Nov 5 (was 397 at yesterday's 22:00 UTC run time). Yesterday's "D49 confirmed sub-400" retro was correct against the DB at run time. Post-run DB revision moves Nov 5 above 400. Using today's authoritative DB: the sub-400 streak ended at D48 (Nov 4, 358 m³/s). Nov 6 = 381 m³/s (sub-400, D1 new period). Today Nov 7 = 417 provisional (above 400). Streak label "D50" from yesterday's brief is voided.

**Reservoir balance (T00 Nov 6 → T00 Nov 7):**
0 falling · 10 steady · 3 rising (baskatong +3 cm, poisson_blanc +3 cm, quinze +3 cm). Normal late-season operations; no active retention signal (all well below 10 cm/day threshold). Yesterday's Lady Evelyn (−4 cm) has settled to 0 today.

**Milestone bookkeeping (W44 rollup anchor Nov 1 + daily extension):**

| Milestone | W44 close (Nov 1) | Nov 2 | Nov 3 | Nov 4 | Nov 5 | Nov 6 | **Nov 7** |
|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 183 | 184 | 185 | 186 | 187 | 188 | **189** |
| Bryson amont above band (104.67 m) | 157 | 158 | 159 | 160 | 161 | 162 | **163** |
| §15.3.5.1 trigger INACTIVE | 160 | 161 | 162 | 163 | 164 | 165 | **166** |
| Témiscaming | D45 (305) | D46 (353) | D47 (351) | D48 (358) **← streak ends** | 413 (above 400) | 381 (sub-400, new D1) | **417 prov (above 400)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 7.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.28 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 166** (133 cm below trigger; +1 cm from yesterday) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 7.*

| Reservoir | Nov 6 (T00) | Nov 7 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.17 m | **219.20 m** | +3 cm | Slight refill |
| Témiscaming | 178.68 m | **178.68 m** | 0 cm | Flat — consistent with outflow ≈ inflow |
| Dozois | 342.01 m | **342.03 m** | +2 cm | Steady |
| Bark Lake (OPG) | 313.57 m | **313.58 m** | +1 cm | Steady |

All 13 tracked reservoirs (timiskaming_haileybury excluded from balance — WSC level gauge only): 0 falling · 10 steady · 3 rising (baskatong +3, quinze +3, poisson_blanc +3). No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. Last Update: 2026-11-03 2:09 PM EST (2026-11-03T19:09:00Z UTC). Next Update: 2026-11-10 4:00 PM EST (2026-11-10T21:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief** (Nov 3 update):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to slightly increase or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **CORRECTION — Témiscaming Nov 5 D49 secondary DB revision:** orrpb_river_flows Nov 5 revised from 397 to **413 m³/s** after yesterday's run. Sub-400 streak ended at **D48 (Nov 4, 358 m³/s)**. Yesterday's "D49 confirmed sub-400" and "D50" labels voided by DB revision. Streak now: D48 ended Nov 4 → Nov 5 above 400 (413) → Nov 6 sub-400 (381, new D1) → Nov 7 above 400 (417 provisional).
2. **CORRECTION — Mattawa Nov 6 retro:** Provisional 152.43 m finalized at **152.39 m** (flat vs Nov 5). "4th consecutive daily rise" claim voided. Today Nov 7 = 152.43 m (+4 cm = new rise D1).
3. **Bryson spill Day 6 ≥5% flag:** Spilled +12.93 m³/s (+8.4%); spill share 45.2%; total release +3.6%. Headpond nearly flat at 105.61 m. Ongoing condition; no property-reach implication.
4. **Carillon dispatch step-up:** T20 Nov 7 = 952 m³/s vs yesterday T19 = 752 m³/s (+200 m³/s). Same-day reference: Nov 5 T20 ≈ 957 m³/s; today is essentially flat vs that. Routine dispatch cycle; no spill.

No flood-risk implications. Lac Coulonge etat 0, 102 cm below pre-alert.

---

## Notes

- **Sub-400 streak recount:** The original streak (Sep 18 – Nov 4, D48 days) is now closed. Daily flows have been fluctuating around 380–420 m³/s since, with no clean consecutive-sub-400 run worth tracking as a streak. The streak milestone will be dropped from the table until a new 5+ day unbroken run is established.
- **Secondary DB revision pattern:** This is the second time an ORRPB daily mean for a past day has been revised after the following day's brief ran (Oct 26 Otto Holden was a similar case per W44 claim ledger). Both involved revisions that moved a value across a threshold (above/below 400). The retro + PSPC T00 cross-check system caught the direction correctly but the PSPC T00 (midnight instantaneous) is not a reliable proxy for the ORRPB finalized daily mean when they straddle a threshold. Consider: the retro read should wait 48 h (reading T-2 days' orrpb_river_flows rather than T-1) to capture post-day-of revisions — flag for the weekly ops rollup review.
- **Mattawa correction note:** Nov 6 finalized at 152.39 m (flat vs Nov 5 152.39 m). The 4-day rise streak through Nov 5 (Nov 2: 152.35 → Nov 3: 152.35 → Nov 4: 152.36 → Nov 5: 152.39) ended with Nov 6 flat. Today Nov 7 = 152.43 (+4 cm) is day 1 of a new rise.
- **Detached HEAD:** Self-corrected via `git checkout main && git pull origin main` before writing today's brief. Recurrence continues (W44 rollup HQ item 2 unresolved).
- **V3 posterior:** Script ran (exit 0); `freshet-forecast.json` content unchanged from prior commit (asof 2026-06-07; all threshold probabilities = 1.0). Will update once `lac-coulonge-daily-1990-2026.csv` is extended past the freshet season.
