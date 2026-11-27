# Daily brief — 2026-11-27

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200). ORRPB conditions forecast HTTP 200 ✓ (probed: HTTP 200; forecast UNCHANGED from Nov 24 3:17 PM update). Vigilance 1195: proxy ingest T21 UTC Nov 27 fresh. V3 posterior: ran successfully (exit 0; anchors on asof 2026-06-07 — 173 days stale, unchanged). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 27.*

*Pipeline note: session started on a detached HEAD (sixth consecutive episode). HEAD was at 25fd276 (merge commit of PR #70), which after `git fetch` matched origin/main. Resolved by `git checkout main` + `git pull --ff-only` before this commit. All previous briefs (Nov 23–26, backfills) successfully propagated to public mirror via PR #70 and PR #69 merges. No orphaned commits this run.*

---

## In plain language

### Upstream — the upper basin

Day 209 of post-peak recession. The upper basin's most notable item today is a provisional uptick at Témiscaming: the outflow for November 27 is showing 432 cubic metres per second, above the 400 m³/s mark for the first time since November 15. If this figure holds when finalized tomorrow, it would end the eleven-day streak (November 16–26) during which daily flows at Témiscaming stayed below 400. The jump from yesterday's finalized 394 is modest — less than 10 percent — and both the PSPC and ORRPB tracking systems agree on the number. But it remains a preliminary daily figure subject to revision, so the streak's fate will be confirmed in tomorrow's brief.

Mattawa and Pembroke are holding within a centimetre or two of yesterday's levels. The basin's fourteen tracked storage reservoirs remain nearly flat: twelve are within two centimetres of yesterday, Lady Evelyn is rising five centimetres, and Poisson Blanc is up three centimetres — both typical autumn refill at side-reservoirs, not a retention signal.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge edged up 1.7 centimetres today to 105.98 metres, a minor reversal of the small daily decline seen earlier this week. The lake is fully normal — more than a metre below the first alert threshold. There is no flood concern at any horizon visible in the current data or forecast.

The Bryson Generating Station (located well downstream of Lac Coulonge, not at the property) reintroduced spillway flow today after routing all water through the turbines yesterday. About 28 cubic metres per second — roughly 9 percent of the total release — now goes through the spillway. This back-and-forth between all-turbine and turbine-plus-spillway is routine and has no flood implications; operators adjust the split based on headpond levels and generating conditions. The dam pond level held essentially flat at 105.57 metres, 90 centimetres above the top of the normal operating band.

The ORRPB weekly forecast remains unchanged from Monday's update (November 24): flows and levels expected to stay close to seasonal values, with a possible slight increase at some locations. Next forecast update December 1.

---

## TL;DR

*RETRO Nov 26: Témiscaming D11 prov 384 → final **394 m³/s** (D11 sub-400 CONFIRMED ✓; streak D1–D11 Nov 16–26 all sub-400). Mattawa prov 152.31 → final **152.36 m** (Δ +5 cm — CONFIRMED at boundary ✓). Pembroke prov 111.04 → final **111.05 m** (Δ +1 cm — CONFIRMED ✓). Carillon prov 1,400 (expected min ~781, mean-through-T20 estimate 816) → final **903 m³/s** (high final reflects T21–T23 Nov 26 stayed at 1,340–1,375 m³/s; plausible ✓). Rapides-Farmers flag Nov 26 (104.22 m³/s, −35.4%) — RESOLVED: today 163.57 m³/s (full recovery).*

**Today (Day 209):** Lac Coulonge T21 **105.980 m** (+1.7 cm vs T21 Nov 26 105.963; etat 0, 102.0 cm below pre-alert). ORRPB daily Nov 27 **105.97 m** (matches ✓). Bryson T20: total **325.44 m³/s**, spill **8.62%** (28.06 m³/s — reintroduced; was 0% yesterday); turbined 297.38; headpond **105.57 m** (+1 cm; Day 183 above band). Hull dock T20 **41.39 m** (+14 cm vs T20 Nov 26 41.25; INACTIVE **Day 186**, 122 cm below trigger). Carillon: HQ T19 = **1,009 m³/s** (afternoon ramp); ORRPB prov **527 m³/s** = T13 snapshot artifact (no midday demand spike today, different dispatch pattern than Nov 24–26); mean-through-T19 = **759 m³/s**; expected final **~780–810 m³/s** (prov fails provisional sanity check — see Notes). Témiscaming D12 prov **432 m³/s** (above 400; PSPC T00 matches exactly ✓; feasibility floor 396; streak break highly likely — CONFIRMATION TOMORROW). Rapide-2 −34.7% (240→157 m³/s). Rapide-7 −33.9% (239→158 m³/s). Paugan (Gatineau) +99% (81→162). Rapides-Farmers +57% (104→164 — recovery). Reservoir balance: **2 falling · 10 steady · 2 rising** (Lady Evelyn +5, Poisson Blanc +3; Rapide-7 −3, Kipawa −2). Forecast UNCHANGED (last update Nov 24; next Dec 1).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 27 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 27 provisional (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 27) | **105.980 m** |
| ORRPB daily Nov 27 (provisional) | 105.97 m |
| ORRPB daily Nov 26 (finalized) | 105.96 m |
| 24h delta (Vigilance T21 Nov 27 vs T21 Nov 26 105.963) | **+1.7 cm** |
| ORRPB daily delta (Nov 26 fin 105.96 → Nov 27 prov 105.97) | +1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 102.0 cm below |
| Distance to minor flood (107.50 m) | 152.0 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 UTC Nov 27. Yesterday: T20 Nov 26 (from prior brief).*

| Metric | Today (T20 Nov 27) | Yesterday (T20 Nov 26) | Δ |
|---|---|---|---|
| Total release (m³/s) | **325.44** | 310.67 | +14.77 (+4.75% — flat) |
| Turbined (m³/s) | **297.38** | 310.67 | −13.29 (−4.3% — flat) |
| Spilled (m³/s) | **28.06** | 0 | **+28.06 (0%→8.62% — spill reintroduced, flag)** |
| Spill share (%) | **8.62%** | 0% | **+8.62 pp (flag)** |
| Headpond / amont (m) | **105.57** (T20) | 105.56 (T20 Nov 26) | +1 cm |
| Tailwater / aval (m) | **86.86** (T20) | 86.84 (T20 Nov 26) | +2 cm |
| Δh (head differential, m) | **18.71** | 18.72 | −1 cm |

Spill reintroduced (0 → 28.06 m³/s) after yesterday's spill elimination. Total release +4.75% (flat boundary). Headpond held essentially flat (105.56→105.57 m). Routine reversal of yesterday's posture optimization — operators running partial spillway today. No threshold implications. Headpond 105.57 m = **90 cm above** the 104.67 m band ceiling (Day 183 above band).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 27. Yesterday = T19–T20 Nov 26 (from prior brief).*

| Site | Total (m³/s) | Spill % | Δ vs yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **249.85** | 0% | −0.4% (flat) |
| Quinze (3-31) | **250.94** | 0.4% (1.04 m³/s) | +1.3% (flat) |
| Îles (3-32) | **256.75** | 0% | +4.7% (flat) |
| Rapide-2 (3-29) | **156.94** | 0% | **−34.7% (flag; 240.33→156.94)** |
| Rapide-7 (3-28) | **157.78** | 0% | **−33.9% (flag; 238.88→157.78)** |
| Bryson (3-46) | **325.44** | **8.62%** | +4.75% (flat); **spill reintroduced (see above)** |
| Paugan — Gatineau R. (3-65) | **162.04** | 0% | **+99% (flag; 81.41→162.04 — recovery from yesterday's suppression)** |
| Rapides-Farmers — Gatineau mouth (3-67) | **163.57** | 0% | **+57% (flag; 104.22→163.57 — full recovery, prior flag resolved)** |
| **Carillon — basin terminal (3-60)** | **1,009.42** T19 | 0% | HQ mean-through-T19 = **759 m³/s**; ORRPB prov 527 = T13 snapshot artifact (see Notes) |

### Carillon intraday pattern (HQ hourly, UTC Nov 27 — different from Nov 24–26 spike pattern)

| UTC hour | Carillon release (m³/s) |
|---|---|
| Nov 27 T00 | 923.59 |
| T01 | 891.83 |
| T02 | 945.91 |
| T03 | 943.43 |
| T04 | 946.85 |
| T05 | 943.67 |
| T06 | 916.55 |
| T07 | 842.97 |
| T08 | 587.30 |
| T09 | 528.64 |
| T10 | 527.47 |
| T11 | 527.42 |
| T12 | 528.78 |
| T13 | 528.73 |
| T14 | 530.24 |
| T15 | 682.71 |
| T16 | 789.55 |
| T17 | 795.41 |
| T18 | 793.39 |
| T19 | **1,009.42** |

Dispatch pattern today: high overnight (900–947 T00–T06), sharp midday trough (~528 T09–T14), afternoon ramp-up. No midday demand spike (contrast with Nov 24–26, when T11–T13 peaked at 1,394–1,399 m³/s). ORRPB prov 527 m³/s = T13 value (528.73) — same snapshot mechanism as prior days, different value. HQ mean-through-T19 (20 h) = **759 m³/s**. Expected final with remaining 4 h at ~900–1,000 m³/s: **~780–810 m³/s** (lower than recent finals of ~900, reflecting absent midday spike).

**Provisional sanity check (Carillon prov 527 vs Nov 26 final 903, −41.6%):** Applied per mandatory guardrail.
1. Feasibility: HQ T19 = 1,009 >> prov 527; mean-through-T19 = 759 (much higher than prov). The prov is a fixed-hour snapshot (T13), not a running mean. Expected final ~780–810 m³/s. No infeasibility.
2. Level consistency: Carillon amont T20 = 41.13 m (+5 cm from 41.08 — slight headpond rise consistent with midday low dispatch). No contradiction.
Result: Prov 527 is a snapshot artifact; actual daily mean will be ~780–810 m³/s. Reported in table only; not headlined.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 20) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 27 — ORRPB prov (m³/s) | **432** | 377 (Nov 20 fin) | +55 | **D12 prov above 400 — streak appears broken; floor 396; confirmation tomorrow** |
| Témiscaming PSPC T00 cross-check (m³/s) | **432** | — | — | Exact match ✓; both above 400 |
| Quinze release → into lake (m³/s) | **250.94** (T20) | — | flat | Upper cascade flat |
| Barrière 3-24 / Cabonga 3-62 (m³/s) | 0 / 6.4 | — | closed | Steady; no diversion state change |
| Mattawa level (m) | **152.34** (Nov 27 prov, WSC) | 152.33 (Nov 20 fin) | +1 cm | Prov — treat directionally; Nov 26 fin 152.36 (yesterday prov 152.31 → CONFIRMED at ±5 cm boundary ✓) |
| Pembroke level (m) | **111.06** (Nov 27 prov) | 111.07 (Nov 20 fin) | −1 cm | Direction only |

**Reservoir balance (Nov 26 T00 → Nov 27 T00):**

| Reservoir | Nov 26 (T00) | Nov 27 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.20 m | **219.21 m** | +1 cm | Steady |
| Dozois | 342.01 m | **342.00 m** | −1 cm | Steady |
| Rapide-7 | 308.91 m | **308.88 m** | −3 cm | Falling |
| Quinze | 262.91 m | **262.93 m** | +2 cm | Steady (boundary) |
| Kipawa | 268.86 m | **268.84 m** | −2 cm | Falling (boundary) |
| Témiscaming | 178.63 m | **178.65 m** | +2 cm | Steady (boundary) |
| Des Joachims | 152.14 m | **152.15 m** | +1 cm | Steady |
| Cabonga | 359.66 m | **359.65 m** | −1 cm | Steady |
| Mitchinamecus | 379.28 m | **379.28 m** | 0 cm | Steady |
| Kiamika | 266.52 m | **266.52 m** | 0 cm | Steady |
| Poisson Blanc | 200.54 m | **200.57 m** | +3 cm | Rising |
| Lady Evelyn | 288.93 m | **288.98 m** | +5 cm | Rising |
| Bark Lake (OPG) | 313.39 m | **313.38 m** | −1 cm | Steady |
| Timiskaming (WSC) | 178.55 m | **178.55 m** | 0 cm | Steady |

**Balance: 2 falling · 10 steady · 2 rising** (Rapide-7 −3 cm, Kipawa −2 cm; Lady Evelyn +5 cm, Poisson Blanc +3 cm). No reservoir rising >10 cm/day. Normal late-autumn holding posture.

**Milestone bookkeeping (W47 rollup Nov 22 anchor + DB-verified chain):**

| Milestone | W47 close (Nov 22) | Nov 23 | Nov 24 | Nov 25 | Nov 26 | **Nov 27** |
|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 204 | 205 | 206 | 207 | 208 | **209** |
| Bryson amont above band (104.67 m) | 178 | 179 | 180 | 181 | 182 | **183** |
| §15.3.5.1 trigger INACTIVE | 181 | 182 | 183 | 184 | 185 | **186** |
| Témiscaming sub-400 streak | D7 (349 fin) | D8 (373 fin ✓) | D9 (358 fin ✓) | D10 (375 fin ✓) | D11 (394 fin ✓) | **D12 prov: 432 (above 400; streak appears broken — CONFIRM TOMORROW)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 27.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.39 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 186** (122 cm below trigger; +14 cm vs T20 Nov 26 41.25 m — headpond rise due to Carillon midday trough) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull dock rise of +14 cm reflects headpond building during today's Carillon midday trough dispatch. No threshold implications.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 27.*

| Reservoir | Nov 26 (T00) | Nov 27 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.20 m | **219.21 m** | +1 cm | Steady |
| Témiscaming | 178.63 m | **178.65 m** | +2 cm | Steady |
| Dozois | 342.01 m | **342.00 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.39 m | **313.38 m** | −1 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs Nov 26 brief)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (probed: HTTP 200). Last Update: 2026-11-24 3:17 PM EST (2026-11-24T20:17:00Z UTC). Next Update: 2026-12-01 4:00 PM EST (2026-12-01T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` mode=`weekly-notice`.*

**UNCHANGED from Nov 24 update** (also unchanged from Nov 25 and Nov 26 briefs):

> *"Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly increase over the coming week, depending on locations. At some locations, water levels are below navigational chart datums."*

No flood-watch language. No change to Lac Coulonge / Britannia / Carillon-specific numeric forecasts (none given; seasonal-language-only mode).

---

## Anomaly flags

1. **Bryson spill reintroduced (0% → 8.62%, +28.06 m³/s).** Total release +4.75% (flat). Headpond held flat (105.56→105.57 m). Routine reversal of yesterday's spill elimination — operators returned to partial spillway. No flood implication.
2. **Rapide-2 (3-29) −34.7% (240.33→156.94 m³/s) and Rapide-7 (3-28) −33.9% (238.88→157.78 m³/s).** Exceeds 5% flag threshold. HQ dispatch reductions at both mid-reach sites; both holding flat (0% spill, no pool pressure). Rapide-7 reservoir pool −3 cm (slight fall, consistent with reduced headpond inflow). Routine dispatch adjustment.
3. **Paugan (Gatineau R., 3-65) +99% (81.41→162.04 m³/s).** Full recovery to expected Gatineau dispatch level after yesterday's suppression. The suppression that yielded yesterday's Rapides-Farmers −35.4% flag has fully reversed.
4. **Rapides-Farmers (Gatineau mouth, 3-67) +57% (104.22→163.57 m³/s) — Nov 26 flag RESOLVED.** Yesterday's flag (-35.4%) was a Gatineau tributary dispatch reduction; today full recovery.
5. **Témiscaming D12 prov 432 m³/s (above 400) — provisional sanity check applied.** Prov 432 vs Nov 26 final 394 = +38 m³/s (+9.6%) — under 25%/150 threshold, no mandatory multi-step check. PSPC T00 and ORRPB agree exactly (432). Feasibility floor: (22/24) × 432 = 396 m³/s (barely below 400 theoretically, but essentially impossible given river flow continuity). Sub-400 streak ending at D11 (Nov 16–26) is the working assumption — CONFIRMED TOMORROW.
6. **Carillon ORRPB prov Nov 27 = 527 m³/s (−41.6% vs Nov 26 final 903) — FAILS provisional sanity check.** Prov matches T13 HQ value (528.73 m³/s) — same T13-snapshot mechanism as Nov 24–26, different dispatch pattern today (no midday spike). Mean-through-T19 = 759 m³/s; expected final ~780–810 m³/s. Prov reported in cascade table only; not headlined. No flood implication.
7. **Hull dock +14 cm** (41.25→41.39 m, T20 snapshot comparison). Rise reflects headpond buildup during Carillon's midday low-dispatch trough (~528 m³/s T09–T14). Trigger INACTIVE Day 186; still 122 cm below 42.61 m.
8. **Pipeline: detached HEAD (sixth consecutive episode).** This run: HEAD was detached at 25fd276 (merge commit of PR #70); after `git fetch`, HEAD matched origin/main. Resolved via `git checkout main` + `git pull --ff-only`. No orphaned commits this run. Root cause unresolved (see W47 rollup Human Queue item 1).

No flood-risk implications at any point in the basin. Lac Coulonge etat 0, 102.0 cm below pre-alert. §15.3.5.1 trigger inactive Day 186.

---

## Notes

- **Day 209** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (173 days stale). `freshet-forecast.json` regenerated without change. Human queue item 5 (W47 rollup) remains unresolved.
- **Témiscaming streak:** D11 Nov 26 finalized 394 m³/s (sub-400, confirmed ✓). D12 Nov 27 prov = 432 m³/s — first prov reading above 400 since Nov 15 prov (401 m³/s, which finalized at 375 and was therefore a false signal). Today's 432 is a larger margin above 400 (vs Nov 15's 401). Floor calculation confirms the minimum possible final is 396 m³/s. Expect D12 final to come in around 420–440 m³/s, confirming streak break.
- **Carillon dispatch pattern change:** Today's Carillon lacked the characteristic midday demand-dispatch peak that appeared Nov 24–26 (1,394–1,399 m³/s at T11–T13). Instead, Carillon ran at ~940 overnight, dropped to ~528 at T08–T14, then began an afternoon ramp-up. The expected final (~780–810 m³/s) will be lower than recent finals (~900 m³/s). This may reflect a one-day demand pattern difference (American Thanksgiving — no effect on Canadian industrial/residential demand, but possibly on cross-border power export scheduling). Worth monitoring whether the Nov 24–26 morning spike pattern resumes.
- **Mattawa ORRPB daily artifact pattern:** Nov 27 prov = 152.34 m (WSC agency this time, not ORRPB daily); treat directionally. Nov 26 prov 152.31 → final 152.36 m (+5 cm, at ±5 cm confirmation boundary — CONFIRMED ✓).
- **ORRPB next update Dec 1.** On weekly schedule (Nov 17 → Nov 24 → Dec 1).
- **W47 Human Queue item 3 (Nov 17 Mattawa retro):** Still outstanding per W47 rollup. The Nov 24 backfill brief should have addressed it; not verified in this session. The W48 rollup (due Dec 7) will close it.
