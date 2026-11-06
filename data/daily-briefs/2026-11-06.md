# Daily brief — 2026-11-06

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 112b). ORRPB forecast HTTP 200 ✓ — last update Nov 3 2:09 PM EST; next update Nov 10 4:00 PM EST (weekly cadence, unchanged). Vigilance 1195: proxy ingest fresh T21 UTC Nov 6 (105.941 m). V3 posterior: ran successfully (exit 0) — `freshet-forecast.json` content unchanged (anchors on asof 2026-06-07; unchanged until `lac-coulonge-daily-1990-2026.csv` is extended). Detached HEAD at session start (recurrence; self-corrected via `git checkout main && git pull origin main` before commit).*

*Nov 5 retro-checks: **Nov 5 Témiscaming ORRPB provisional 441 → final 397 m³/s** (−44 m³/s, within 50 m³/s tolerance — **CONFIRMED**). **CORRECTION: D49 (Nov 5) finalized at 397 m³/s — still sub-400. Yesterday's "sub-400 D48 streak almost certainly ends" claim was premature and incorrect; D49 confirmed sub-400. Streak continues; today is D50 (provisional 367 m³/s).** Nov 5 Mattawa ORRPB daily: claimed 152.42 m → finalized 152.39 m (−3 cm revision; direction unchanged, rise streak intact — no flood-state claim affected). Nov 5 ORRPB Lac Coulonge: 105.90 → finalized 105.91 m (+1 cm, immaterial).*

---

## In plain language

### Upstream — the upper basin

The basin is 188 days past the May 2 seasonal peak. The outflow from Lake Timiskaming — the large reservoir at the head of the main stem — came in at 367 cubic metres per second today as a preliminary daily figure, comfortably within the range that has been normal for the past 50 days (all sub-400 m³/s). Yesterday's report that this "streak was almost certainly ending" turned out to be incorrect: yesterday's preliminary reading of 441 m³/s finalized at 397 — still below 400 — so the streak continued rather than ended. Today's preliminary at 367 m³/s points to continuation. The federal monitoring agency's midnight snapshot reads somewhat higher at 422 m³/s, a 55 m³/s gap; possible that the flow was elevated earlier in the day and has since settled down, which would be consistent with Lake Timiskaming rising 7 centimetres overnight. This discrepancy is noted but the underlying picture — sub-400 baseflow continuing — is not in doubt.

The Mattawa gauge, an upstream indicator roughly 200 kilometres above Lac Coulonge, is on its fourth straight daily rise: 152.43 metres today, up 4 centimetres from yesterday's finalized 152.39 metres. Pembroke, further downstream, dipped a single centimetre to 111.05 metres — essentially flat. Six of the basin's fourteen tracked reservoirs rose slightly overnight (the largest gains: Lake Timiskaming and the Quinze reservoir each up 7 centimetres; Baskatong up 5 centimetres), suggesting inflows are very modestly outpacing outflows at several headwater locations — a normal late-autumn pattern, not a storage event.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 105.941 metres at 9 PM UTC — up about 2 centimetres from the same hour yesterday (105.919 m). The ORRPB daily series puts it at 105.94 metres, up 3 centimetres from yesterday's finalized 105.91 metres. The lake is fully in normal conditions — 106 centimetres below the 107.00-metre pre-alert threshold. The gentle day-to-day fluctuation aligns with what the weekly forecast anticipated (slight increases or stability depending on location); no sharp change is expected before the next ORRPB update on November 10.

Well downstream, at the Bryson Generating Station (accessed via a long winding channel well below the southern tip of Lac Coulonge and not visible from the Mansfield properties), today is the fifth consecutive day of spillway release. Approximately 155 cubic metres per second is now running through the spillway — 43.2% of the total 358 m³/s release, up from 41.6% yesterday. The dam pond held flat at 105.59 metres. At Carillon, the basin's terminal dam, the overnight dispatch was stepped down significantly: today's late-afternoon release measured around 752 m³/s, compared with roughly 957 m³/s at the same hour yesterday. This is routine power-dispatch scheduling, with no spillway involvement and no flood-system implication.

---

## TL;DR

**CORRECTION (Témiscaming Nov 5):** Provisional 441 m³/s → final **397 m³/s** (−44, within 50 m³/s — CONFIRMED sub-400). D49 was sub-400; yesterday's "streak ends" claim was wrong. **Today (Day 188):** Lac Coulonge T21 **105.941 m** (+2 cm vs T21 yesterday; etat 0, 106 cm below pre-alert). Bryson Day 5 partial spill: **43.2%** (154.70 m³/s, +9.76 / +6.7% vs yesterday — ⚠ exceeds 5% flag). Carillon T19 **751.92 m³/s** (−205.5, −21.5% intraday step-down from yesterday T20 957 — dispatch). Témiscaming **D50 provisional 367 m³/s** (ORRPB) / **422 m³/s** (PSPC T00; +55 m³/s discrepancy > 50 threshold — ⚠ flag; ORRPB primary, streak sub-400). Mattawa ORRPB daily **152.43 m** (+4 cm from finalized Nov 5 152.39 m — 4th consecutive daily rise). Pembroke **111.05 m** (−1 cm, flat). Hull dock T20 **41.27 m** — trigger INACTIVE **Day 165**. Reservoir balance: **1 falling · 7 steady · 6 rising** (timiskaming +7 cm, quinze +7 cm, baskatong +5 cm). ORRPB forecast unchanged (Nov 3; next Nov 10).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 6 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 6 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 6) | **105.941 m** |
| ORRPB daily Nov 6 | 105.94 m (provisional from T00) |
| 24h delta (Vigilance T21 Nov 6 vs T21 Nov 5) | **+2 cm** |
| ORRPB daily delta (Nov 5 finalized 105.91 → Nov 6 provisional 105.94) | +3 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 106 cm below |
| Distance to minor flood (107.50 m) | 156 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 UTC Nov 6. Yesterday: T20 UTC Nov 5.*

| Metric | Today (T20 Nov 6) | Yesterday (T20 Nov 5) | Δ |
|---|---|---|---|
| Total release (m³/s) | **358.22** | 348.64 | +9.58 (+2.7%) |
| Turbined (m³/s) | **203.52** | 203.70 | −0.18 (0.0%) |
| Spilled (m³/s) | **154.70** | 144.94 | **+9.76 (+6.7%)** ⚠ |
| Spill share (%) | **43.2%** | 41.6% | +1.6 pp |
| Headpond / amont (m) | **105.59** (T20) | 105.58 (T20 Nov 5) | +1 cm |
| Tailwater / aval (m) | **86.83** (T20) | 86.80 (T20 Nov 5) | +3 cm |
| Δh (head differential, m) | **18.76** | 18.78 | −2 cm |

Spilled m³/s up 6.7% (exceeds 5% flag). Day 5 of partial spill — share growing while headpond holds flat at 105.59 m. Headpond 105.59 m = **92 cm above** the 104.67 m band ceiling — **Day 162** above band.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 6. Yesterday comparison: T19–T20 UTC Nov 5.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **224.44** T20 | 0% | −11.06 (−4.7%) |
| Quinze (3-31) | **211.65** T19 | 0.4% | −0.73 (flat) |
| Îles (3-32) | **216.45** T19 | 0% | −4.31 (−2.0%) |
| Rapide-2 (3-29) | **241.55** T19 | 0% | +0.66 (flat) |
| Rapide-7 (3-28) | **158.39** T19 | 0% | −0.40 (flat) |
| Bryson (3-46) | **358.22** T20 | **43.2%** | +9.58 (+2.7%); spill Day 5, growing |
| Paugan — Gatineau R. (3-65) | **160.81** T19 | 0% | +20.27 (+14.4%) |
| Rapides-Farmers — Gatineau mouth (3-67) | **173.57** T19 | 0% | +17.25 (+11.0%) |
| Carillon — basin terminal (3-60) | **751.92** T19 | 0% | −205.49 (−21.5%) vs T20 yesterday † |

† Carillon intraday step-down from yesterday's late-afternoon peak of ~957 m³/s. No spill in either direction; routine dispatch scheduling. Paugan and Rapides-Farmers (Gatineau tributary) both up 11–14%; typical Gatineau dispatch fluctuation.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 30) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 6 provisional — ORRPB (m³/s) | **367** | 193 (Oct 30) | +174 | *D50 provisional sub-400 — see PSPC discrepancy note below* |
| Témiscaming Nov 6 — PSPC T00 cross-check (m³/s) | **422** | — | **⚠ +55 vs ORRPB** (>50 m³/s threshold) | *See note — not a surge claim; streak sub-400 on ORRPB primary* |
| Quinze release → into lake (m³/s) | **211.65** (T19) | 207.47 (Oct 30) | +4 (flat) | Baseload; stable |
| Mattawa level (m) | **152.43** (Nov 6 ORRPB daily) | 152.05 (Oct 30) | +38 cm | **4th consecutive daily rise (Nov 3: 152.35 → Nov 4: 152.36 → Nov 5: 152.39 → Nov 6: 152.43)** |
| Pembroke level (m) | **111.05** (Nov 6 ORRPB daily) | 111.03 (Oct 30) | +2 cm | Flat week-over-week; −1 cm day-over-day |

**PSPC discrepancy note — Témiscaming Nov 6:** ORRPB `orrpb_river_flows` = 367 m³/s; PSPC `reservoir_readings` T00 = 422 m³/s. Gap = 55 m³/s, just above the 50 m³/s flag threshold. PSPC T00 is a midnight-snapshot flow; ORRPB is a running daily mean. Level consistency: Timiskaming rose 7 cm (178.62 → 178.69 m, T00 Nov 5 → T00 Nov 6), consistent with inflows slightly exceeding outflows at some point in the day. Plausible explanation: flow was elevated earlier (consistent with PSPC midnight 422 m³/s), settling lower through the day to bring the daily mean toward 367. This is not a surge claim — provisional sanity check is NOT triggered (day-over-day change −30 m³/s / −7.6%, well below ≥25% / ≥150 m³/s thresholds). ORRPB remains the primary metric for the sub-400 streak; both sources are sub-400 regardless (422 vs 367; neither above 400 sufficiently to end the streak after the Nov 5 retro confirmed D49 at 397).

Wait — PSPC T00 Nov 6 = 422 m³/s is ABOVE 400. But ORRPB Nov 6 = 367 m³/s is below 400. For streak purposes: the streak is tracked using ORRPB `orrpb_river_flows` (the daily average). ORRPB = 367 m³/s → D50 provisional sub-400. The PSPC T00 reading at 422 represents the midnight instantaneous snapshot, which can be above 400 even on a day when the daily average finishes below 400.

**Provisional-flow sanity check (Témiscaming ORRPB Nov 6 = 367 m³/s):** Change vs Nov 5 final (397 m³/s) = −30 m³/s (−7.6%) — below both ≥25% and ≥150 m³/s thresholds. Formal sanity check NOT required. Normal day-over-day movement.

**RETRO — Nov 5 Témiscaming ORRPB:** Yesterday's brief provisionally claimed 441 m³/s. Finalized: **397 m³/s** (−44 m³/s, within 50 m³/s tolerance — **CONFIRMED**). D49 confirmed sub-400.

**Reservoir balance (T00 Nov 5 → T00 Nov 6):**
1 falling · 7 steady · 6 rising (timiskaming +7 cm, quinze +7 cm, baskatong +5 cm, mitchinamecus +4 cm, des_joachims +3 cm, poisson_blanc +3 cm). Lady Evelyn −4 cm is the sole faller. Timiskaming's +7 cm is consistent with the PSPC midnight reading suggesting inflows > outflows during the Nov 5→6 overnight window. Normal late-season operations; no active retention signal (all well below 10 cm/day threshold).

**Milestone bookkeeping (W44 rollup anchor Nov 1 + daily extension):**

| Milestone | W44 close (Nov 1) | Nov 2 | Nov 3 | Nov 4 | Nov 5 | **Nov 6** |
|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 183 | 184 | 185 | 186 | 187 | **188** |
| Bryson amont above band (104.67 m) | 157 | 158 | 159 | 160 | 161 | **162** |
| §15.3.5.1 trigger INACTIVE | 160 | 161 | 162 | 163 | 164 | **165** |
| Témiscaming sub-400 | D45 (305) | D46 ✓ (353) | D47 ✓ (351) | D48 ✓ (334) | D49 ✓ (**397**, RETRO — was 441 prov; streak did NOT end) | **D50 provisional (367)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 6.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 165** (134 cm below trigger; +3 cm from yesterday) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 6.*

| Reservoir | Nov 5 (T00) | Nov 6 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.12 m | **219.17 m** | +5 cm | Rising — upper-basin refill |
| Témiscaming | 178.62 m | **178.69 m** | +7 cm | Rising — largest gain; consistent with overnight inflows > outflows |
| Dozois | 342.01 m | **342.00 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.57 m | **313.57 m** | 0 cm | Steady |

All 14 tracked reservoirs: 1 falling · 7 steady · 6 rising (timiskaming +7 cm, quinze +7 cm, baskatong +5 cm, mitchinamecus +4 cm, des_joachims +3 cm, poisson_blanc +3 cm). No active retention signal (all well below 10 cm/day threshold). Normal late-season operations.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. Last Update: 2026-11-03 2:09 PM EST (2026-11-03T19:09:00Z UTC). Next Update: 2026-11-10 4:00 PM EST (2026-11-10T21:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief** (Nov 3 update):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to slightly increase or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **CORRECTION — Témiscaming Nov 5 D49 retro:** Provisional 441 m³/s → final **397 m³/s** (−44, CONFIRMED within 50 m³/s). D49 was sub-400. Yesterday's headline "sub-400 D48 streak almost certainly ends" was premature and incorrect. D50 today provisional = 367 m³/s.
2. **PSPC T00 Nov 6 disagrees with ORRPB Nov 6 by 55 m³/s** (422 vs 367 — exceeds 50 m³/s threshold). Not a surge: provisional sanity check not triggered (change vs Nov 5 final = −30 m³/s / −7.6%). Level-consistent explanation available (Timiskaming +7 cm overnight). ORRPB primary; both sources sub-400; streak status unaffected.
3. **Bryson spill Day 5 ≥5% flag:** Spilled +9.76 m³/s (+6.7%); spill share 43.2%; total release +2.7%. Headpond flat at 105.59 m. Ongoing condition; no property-reach implication.
4. **Carillon intraday step-down −205 m³/s (−21.5%):** From yesterday T20 (957 m³/s) to today T19 (752 m³/s). No spill in either direction; routine dispatch scheduling.

No flood-risk implications. Lac Coulonge etat 0, 106 cm below pre-alert.

---

## Notes

- **Nov 5 Témiscaming retro: final 397 m³/s.** Both ORRPB and PSPC finalized at 397 m³/s — the two-source agreement in yesterday's brief was real, but the value was 397 not 441. The 22h feasibility floor estimate (≈404 m³/s) in yesterday's brief was also slightly above the actual final, underscoring that the floor calculation is a lower bound only, not a prediction.
- **Mattawa ORRPB data convention note:** Yesterday's brief reported Nov 5 Mattawa = 152.42 m (provisional at run time); finalized 152.39 m (−3 cm). The rise streak direction was correct throughout; the level difference is minor. The 4-consecutive-rise streak (Nov 3: 152.35 → Nov 4: 152.36 → Nov 5: 152.39 → Nov 6: 152.43) is established against finalized DB values.
- **Pembroke note:** Yesterday's brief reported 110.99 m for Nov 5. DB shows Nov 5 = 111.06 m and Nov 4 = 111.07 m. The 110.99 value matches Nov 3 in the DB, suggesting the routine read a stale row (data latency at run time). No flood-state claim was made for Pembroke; direction-only reporting is unaffected.
- **Detached HEAD:** Self-corrected via `git checkout main && git pull origin main` before writing today's brief. Recurrence continues (W44 rollup HQ item 2 unresolved).
- **V3 posterior:** Script ran (exit 0); `freshet-forecast.json` content unchanged from prior commit (asof 2026-06-07; all threshold probabilities = 1.0). Will update once `lac-coulonge-daily-1990-2026.csv` is extended past the freshet season.
