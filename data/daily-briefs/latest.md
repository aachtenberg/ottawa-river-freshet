# Daily brief — 2026-11-22

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200/94b). ORRPB conditions forecast HTTP 200 ✓ (probed: HTTP 200/128655b; forecast unchanged — last update Nov 17). Vigilance 1195: proxy ingest fresh T21 UTC Nov 22. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged — 168 days stale). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 22. **Git note: main was at Nov 17 brief on startup (Nov 18–21 commits were on orphaned detached HEAD); fast-forwarded main to b71954c before writing this brief — public mirror was 4 days behind.**.*

*Nov 21 retro: Témiscaming ORRPB daily prov 317 → finalized **367 m³/s** (+50 m³/s, right at threshold boundary — CONFIRMED sub-400 D6); PSPC T00 revised from 384 → 367 m³/s (both sources now 367 m³/s, converging). Pembroke prov 111.13 → finalized **111.08 m** (−5 cm, within ±5 cm — CONFIRMED). Mattawa prov 152.19 → finalized **152.34 m** (+15 cm — ARTIFACT CONFIRMED, correctly flagged yesterday).*

---

## In plain language

### Upstream — the upper basin

The upper basin remains in a quiet late-autumn posture, 204 days past the May 2 freshet peak of 2,741 cubic metres per second. Outflow from Lake Timiskaming edged down to 325 cubic metres per second in the ORRPB provisional reading for today, while the PSPC midnight snapshot sits at 363 m³/s — both firmly below 400 m³/s, extending the sub-400 streak to a provisional seventh day. Yesterday's provisional of 317 m³/s finalized at 367 m³/s, confirming the sixth day. The gap between the two sources today is 38 m³/s — well within the 50 m³/s alert threshold — so both numbers are telling the same story.

The notable operational event today is an HQ dispatch step-up at multiple upper-cascade generating stations: the Quinze dam on Lake Quinze jumped from about 221 to 313 cubic metres per second, and similar increases appeared at Première-Chute and Îles — all roughly 25–40% above yesterday. This kind of coordinated ramp-up is typical at the start of heating season when power demand rises. The water moving through those turbines will take hours to reach the Rapide-2 and Rapide-7 stations further downstream, which are still showing yesterday's pace. No flood implication. The gauge at Pembroke, mid-valley, edged down three centimetres to 111.05 metres — a gentle, unremarkable decline. The Mattawa reading shows another large 15-centimetre drop (to 152.19 m), but this is exactly the same suspicious pattern as yesterday's provisional, which corrected upward 15 centimetres when finalized. Treat today's Mattawa reading as preliminary.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge recorded 105.970 metres at 9 PM UTC on November 22, down about 1.7 centimetres from yesterday. The lake sits just over a metre below the first alert threshold — firmly normal. The ORRPB daily figure for today (105.98 m) confirms the same mild downward drift.

The generating station at Bryson — reached by the long channel winding south from Lac Coulonge — held essentially flat: total release 349 cubic metres per second, turbines producing 296 m³/s, with 54 m³/s through the spillway (15% of the total, unchanged). The dam pond behind Bryson eased two centimetres to 105.49 metres, still 82 centimetres above the normal operating ceiling. This is Day 178 of the headpond sitting above that band; it is an ongoing baseline condition with no operational significance today.

The ORRPB weekly forecast, last updated Monday November 17, calls for flows to "remain fairly stable or slightly decrease over the coming week, depending on locations." Next update is expected November 24 (tomorrow).

---

## TL;DR

**RETRO: Nov 21 Témiscaming ORRPB prov 317 → final 367 m³/s (+50 m³/s, boundary — CONFIRMED sub-400 D6); PSPC T00 revised 384 → 367 (both converge 367). Pembroke prov 111.13 → 111.08 m (CONFIRMED ±5 cm). Mattawa prov 152.19 → 152.34 m (ARTIFACT CONFIRMED, +15 cm, as flagged).** **Today (Day 204):** Lac Coulonge T21 **105.970 m** (−1.7 cm vs T21 Nov 21; etat 0, 103 cm below pre-alert; ORRPB daily prov 105.98 m). Bryson T20: total **349.36 m³/s** (−0.28%), spill **53.52** (15.3%), headpond **105.49 m** (−2 cm; Day 178 above band). §15.3.5.1 trigger INACTIVE **Day 181** (Hull 41.29 m). Carillon T19 **842.1 m³/s** (−4.3% vs Nov 21 T19 879.49 — below 5% threshold). Témiscaming D7 prov: ORRPB daily **325 m³/s**, PSPC T00 **363 m³/s** (gap 38 m³/s — within 50 threshold; both sub-400). Mattawa prov 152.19 m (−15 cm vs Nov 21 final 152.34 m — same artifact pattern as yesterday; expect revision; Pembroke −3 cm mildly inconsistent). Reservoir balance: **1 falling · 12 steady · 1 rising** (des_joachims −4 cm; Poisson Blanc +3 cm). **HQ cascade dispatch step-up: Quinze +41.6%, Îles +39.0%, Première-Chute +24.5% (all flag; HQ demand-response; no flood implication).** ORRPB weekly forecast unchanged from Nov 17; next update Nov 24. Git: fast-forwarded main from Nov 17 to Nov 21 on startup; Nov 18–21 briefs were on orphaned detached HEAD.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 22 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 22 provisional (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 22) | **105.970 m** |
| ORRPB daily Nov 22 (provisional) | 105.98 m |
| ORRPB daily Nov 21 (finalized) | 105.99 m |
| 24h delta (Vigilance T21 Nov 22 vs T21 Nov 21) | **−1.7 cm** (105.970 vs 105.987 m) |
| ORRPB daily delta (Nov 21 finalized 105.99 → Nov 22 prov 105.98) | −1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 103 cm below |
| Distance to minor flood (107.50 m) | 153 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 (releases and levels) UTC Nov 22. Yesterday: T20 Nov 21 (from prior brief).*

| Metric | Today (T20 Nov 22) | Yesterday (T20 Nov 21) | Δ |
|---|---|---|---|
| Total release (m³/s) | **349.36** | 350.34 | −0.98 (−0.28%) |
| Turbined (m³/s) | **295.84** | 296.74 | −0.90 (−0.30%) |
| Spilled (m³/s) | **53.52** | 53.60 | −0.08 (−0.15%) |
| Spill share (%) | **15.3%** | 15.3% | 0 pp |
| Headpond / amont (m) | **105.49** (T20) | 105.51 (T20 Nov 21) | −2 cm |
| Tailwater / aval (m) | **86.93** (T20) | 86.98 (T20 Nov 21) | −5 cm |
| Δh (head differential, m) | **18.56** | 18.53 | +3 cm |

No change exceeds 5% threshold. Headpond 105.49 m = **82 cm above** the 104.67 m band ceiling (Day 178 above band). Stable run-of-river dispatch.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 22.*

| Site | Total (m³/s) | Spill % | Δ vs yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **273.3** T19 | 1.7% (4.56 m³/s) | **+24.5% (flag; HQ dispatch step-up)** |
| Quinze (3-31) | **312.78** T19 | 0.3% (0.97 m³/s) | **+41.6% (flag; HQ dispatch step-up)** |
| Îles (3-32) | **313.27** T20 | 0% | **+39.0% (flag; HQ dispatch step-up)** |
| Rapide-2 (3-29) | **157.44** T19 | 0% | −0.1% (flat; routing delay expected) |
| Rapide-7 (3-28) | **157.71** T19 | 0% | −0.1% (flat; routing delay expected) |
| Bryson (3-46) | **349.36** T20 | **15.3%** (53.52 m³/s) | −0.28% |
| Paugan — Gatineau R. (3-65) | **159.00** T19 | 0% | −0.2% |
| Rapides-Farmers — Gatineau mouth (3-67) | **170.34** T20 | 0% | −0.4% |
| Carillon — basin terminal (3-60) | **842.1** T19 | 0% | −4.3% (below 5% flag; continuing step-down from yesterday) |

Upper-cascade step-up (Première-Chute, Quinze, Îles) is a coordinated HQ dispatch increase, consistent with heating-season demand response. Routing delay means downstream stations (Rapide-2, 7) have not yet absorbed the increased flow. Première-Chute added trace spill (1.7%) where it was 0% yesterday — triggered by the increased generation, minor.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 15) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 22 — ORRPB daily provisional (m³/s) | **325** | 401 (Nov 15 fin — above 400) | −76 | D7 provisional sub-400; D1=Nov 16 (366 fin), D2=Nov 17 (375 fin), D3=Nov 18 (381 fin), D4=Nov 19 (365 fin), D5=Nov 20 (358 fin), D6=Nov 21 (367 fin) |
| Témiscaming PSPC cross-check (m³/s) | **363** T00 Nov 22 | — | — | 38 m³/s gap vs ORRPB daily (within 50 threshold — no flag; both sub-400) |
| Quinze release → into lake (m³/s) | **312.78** (T19) | — | +41.6% vs yesterday | HQ dispatch step-up; Quinze reservoir +2 cm (262.93→262.95 m) |
| Mattawa level (m) | **152.19** (Nov 22 prov) | 152.38 (Nov 15 fin) | — | −15 cm vs Nov 21 finalized (152.34 m); **likely artifact** — identical to Nov 21 prov (152.19 m, corrected +15 cm to 152.34 m); Pembroke −3 cm mildly inconsistent with large Mattawa crash |
| Pembroke level (m) | **111.05** (Nov 22) | 111.13 (Nov 15 fin) | −8 cm over 7d | −3 cm vs Nov 21 finalized (111.08 m); mild continuing decline |

**Reservoir balance (T00 Nov 21 → T00 Nov 22):**

| Reservoir | Nov 21 (T00) | Nov 22 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.25 m | **219.24 m** | −1 cm | Steady |
| Dozois | 342.08 m | **342.08 m** | 0 cm | Steady |
| Témiscaming | 178.58 m | **178.58 m** | 0 cm | Steady |
| Bark Lake | 313.51 m | **313.51 m** | 0 cm | Steady |
| Des Joachims | 152.10 m | **152.06 m** | −4 cm | Falling |
| Poisson Blanc | 200.40 m | **200.43 m** | +3 cm | Rising (below 10 cm/day flag) |
| Cabonga | 359.66 m | **359.65 m** | −1 cm | Steady |
| Quinze | 262.93 m | **262.95 m** | +2 cm | Steady |
| Others (6) | — | — | −2 to 0 cm | Steady |

**Balance: 1 falling · 12 steady · 1 rising (des_joachims −4 cm; Poisson Blanc +3 cm, below 10 cm/day flag).** Normal late-season holding posture; no active retention signal.

**Milestone bookkeeping (W46 rollup Nov 15 anchor + corrected daily chain via DB):**

| Milestone | W46 close (Nov 15) | Nov 16 | Nov 17 | Nov 18 | Nov 19 | Nov 20 | Nov 21 | **Nov 22** |
|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 197 | 198 | 199 | 200 | 201 | 202 | 203 | **204** |
| Bryson amont above band (104.67 m) | 171 | 172 | 173 | 174 | 175 | 176 | 177 | **178** |
| §15.3.5.1 trigger INACTIVE | 174 | 175 | 176 | 177 | 178 | 179 | 180 | **181** |
| Témiscaming sub-400 streak | *new D1 Nov 16 (366)* | D1: 366 | D2: 375 fin | D3: 381 fin | D4: 365 fin | D5: 358 fin | D6: 367 fin (prov 317→fin 367) | **D7 prov: 325 (ORRPB) / 363 PSPC T00** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 22.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.29 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 181** (132 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 22.*

| Reservoir | Nov 21 (T00) | Nov 22 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.25 m | **219.24 m** | −1 cm | Steady |
| Témiscaming | 178.58 m | **178.58 m** | 0 cm | Steady |
| Dozois | 342.08 m | **342.08 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.51 m | **313.51 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (probed: HTTP 200/128655b). Last Update: 2026-11-17 2:49 PM EST (2026-11-17T19:49:00Z UTC). Next Update: 2026-11-24 4:00 PM EST (2026-11-24T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` updated with mode=`weekly-notice`, fetched_at updated to 2026-11-22T22:00:00Z.*

**Unchanged from Nov 17 brief (no new ORRPB update expected until Nov 24):**

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **HQ upper-cascade dispatch step-up: Quinze +41.6%, Îles +39.0%, Première-Chute +24.5%.** T19 Nov 22 vs T20 Nov 21: Quinze 220.89→312.78 m³/s, Îles 225.41→313.27 m³/s, Première-Chute 219.52→273.3 m³/s. All three exceed the >5% cascade flag threshold. Rapide-2 and Rapide-7 (downstream) are essentially flat — routing delay expected. The Première-Chute trace spill (0%→1.7%, 4.56 m³/s) is a byproduct of the increased generation. Consistent with normal HQ heating-season demand-response ramping. No flood implication; informational flag only.
2. **Mattawa Nov 22 provisional 152.19 m (likely artifact, same as Nov 21).** ORRPB daily Mattawa Nov 22 = 152.19 m vs Nov 21 finalized 152.34 m = −15 cm. This is the same value and same drop magnitude as Nov 21's provisional (152.19 m), which corrected to 152.34 m (+15 cm). Pembroke dropped only 3 cm (111.08→111.05 m) — mildly inconsistent with a 15 cm Mattawa crash, though not as strongly contradictory as yesterday's +4 cm Pembroke. Treat Nov 22 Mattawa as provisional; expect revision toward 152.20–152.34 m range.
3. **Git: main was 4 days behind (Nov 18–21 briefs on orphaned detached HEAD).** On startup, main pointed to the Nov 17 brief; Nov 18–21 commits were on a detached HEAD (b71954c). Fast-forwarded main to b71954c before writing today's brief. Origin/main also lagged — today's push will propagate all five missing days to the public mirror at once. W47 HQ item: investigate why recent sessions are leaving commits on a detached HEAD rather than committing to main.

No flood-risk implications. Lac Coulonge etat 0, 103 cm below pre-alert. §15.3.5.1 trigger inactive.

---

## Notes

- **Day 204** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (168 days stale). `freshet-forecast.json` regenerated without change. W46 HQ item 4 remains open.
- **Des Joachims reservoir −4 cm (152.10→152.06 m).** Des Joachims pool down 4 cm at T00. This is "falling" per the ±2 cm threshold. Latest_reservoir_readings flow for des_joachims = 709 m³/s — consistent with elevated releases. No anomaly implication; informational.
- **Témiscaming PSPC T00 Nov 21 revised.** The PSPC T00 value for Nov 21 updated from 384 m³/s (at yesterday's run time) to 367 m³/s (now), converging with the ORRPB daily final (also 367 m³/s). This confirms D6 sub-400 at 367 m³/s. The 384→367 T00 revision is an unusual downstream update but within normal PSPC provisional-data behavior.
- **ORRPB next update Nov 24.** Tomorrow's brief should catch the first weekly forecast update since Nov 17.
