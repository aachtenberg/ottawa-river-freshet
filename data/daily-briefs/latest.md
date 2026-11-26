# Daily brief — 2026-11-26

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200/117b). ORRPB conditions forecast HTTP 200 ✓ (probed: HTTP 200/128640b; forecast UNCHANGED from Nov 24 3:17 PM update). Vigilance 1195: proxy ingest fresh T21 UTC Nov 26. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (172 days stale — unchanged, Human queue item 5 W47 unresolved). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 26.*

*Pipeline note: session again started on a detached HEAD (fifth consecutive episode). Today: fast-forwarded main to 611a534 to recover Nov 23 brief (642e844), W47 rollup (c759387), and Nov 25 brief (611a534) — all three were on an orphaned HEAD, not on origin/main. Public mirror has been missing these three files since they were committed (Nov 23 23:17 UTC). Root cause unresolved — see W47 rollup Human Queue item 1 (escalating: W44 1-day, W45 2-day, W46 1-day, W47 4-day, now again at session-start today).*

---

## In plain language

### Upstream — the upper basin

Day 208 of post-peak recession, and the upper basin remains in its settled autumn routine. Flow out of Lake Timiskaming finalized at 375 cubic metres per second for November 25 — confirming the tenth consecutive day below the 400 m³/s mark (the streak runs from November 16 through November 25). Today's preliminary snapshot sits at 384 m³/s, still below 400, but a final determination won't come until tomorrow.

The mid-valley gauges at Mattawa and Pembroke each eased a few centimetres today, continuing the gentle downward drift of recent weeks. All 14 tracked storage reservoirs remain nearly flat: eleven are essentially unchanged, two (Rapide-7 and Bark Lake) dropped three to four centimetres, and the Des Joachims pool ticked up three centimetres overnight. That minor uptick at Des Joachims is unremarkable — it reflects small day-to-day variation at a managed pool, not a change in operating posture. No reservoir is rising more than a few centimetres; operators are passing water through at roughly the rate it arrives.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge continued drifting gently downward tonight, landing at 105.96 metres — a little over a centimetre below yesterday's reading and sitting more than a metre below the first alert threshold. The lake is fully normal.

The only operational note at the downstream end of the cascade is that the Bryson Generating Station (located well downstream of Lac Coulonge, not at the property) stopped releasing water through its spillway today. Yesterday, about 23 cubic metres per second were going through the spillway alongside the turbines; today everything is routed through the turbines, and total output is slightly lower at 311 m³/s. This kind of adjustment is routine — when the dam pond level and load conditions allow it, operators prefer to run all flow through the turbines rather than the spillway. The dam pond level held essentially flat, confirming there is no unusual pressure on the system.

The ORRPB weekly forecast remains unchanged from Monday's update (November 24): flows and levels are expected to stay "close to seasonal values" with a "slight increase" possible over the coming week. Next forecast update: December 1.

---

## TL;DR

*RETRO Nov 25: Témiscaming D10 prov (PSPC T00 401 m³/s) → final **375 m³/s** (D10 sub-400 CONFIRMED ✓, streak D1–D10 Nov 16–25 all confirmed). Mattawa prov 152.38 m → final **152.34 m** (Δ −4 cm, within ±5 cm → CONFIRMED ✓). Pembroke prov 111.04 m → final **111.07 m** (+3 cm → CONFIRMED ✓). Carillon ORRPB daily prov 1,378 m³/s → finalized **900 m³/s** (prov was T12 snapshot artifact as flagged in Nov 25 brief; expected final ≈ 861 m³/s — actual 900 within estimation range).*
*PIPELINE: detached HEAD (fifth episode) — Nov 23 brief, W47 rollup, Nov 25 brief all recovered via fast-forward onto main before this commit; public mirror has missed these files since ~Nov 23 23:17 UTC.*
**Today (Day 208):** Lac Coulonge T21 **105.963 m** (−1.2 cm vs T21 Nov 25 105.975 m; etat 0, 103.7 cm below pre-alert). ORRPB daily Nov 26 **105.96 m** (matches Vigilance ✓). Bryson T20: total **310.67 m³/s**, spill **0%** (spill eliminated — was 23.00 m³/s / 7.2% at T19 Nov 25 → Δ −100%); turbined +4.2%; headpond T20 **105.56 m** (Δ −1 cm; Day 182 above band). §15.3.5.1 trigger INACTIVE **Day 185** (Hull 41.25 m). Carillon T11–T13 peak ~1,395–1,399 m³/s (repeating Nov 25 intraday demand-dispatch pattern), T20 **535 m³/s**; mean-through-T20 = **816 m³/s**; ORRPB daily prov 1,400 = T13 snapshot artifact → fails prov sanity check; expected final ≈ **781 m³/s**. Rapides-Farmers (Gatineau mouth) **−35.4%** (161.28 → 104.22 m³/s — flag; Gatineau tributary dispatch). Témiscaming D11 prov **384 m³/s** (sub-400, uncertain). Reservoir balance: **2 falling · 11 steady · 1 rising** (Des Joachims +3 cm). Forecast UNCHANGED (last update Nov 24; next Dec 1).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 26 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 26 provisional (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 26) | **105.963 m** |
| ORRPB daily Nov 26 (provisional) | 105.96 m |
| ORRPB daily Nov 25 (finalized) | 105.97 m |
| 24h delta (Vigilance T21 Nov 26 vs T21 Nov 25) | **−1.2 cm** |
| ORRPB daily delta (Nov 25 fin 105.97 → Nov 26 prov 105.96) | −1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 103.7 cm below |
| Distance to minor flood (107.50 m) | 154.0 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 (releases + levels) UTC Nov 26. Yesterday: T19 Nov 25 (from prior brief).*

| Metric | Today (T20 Nov 26) | Yesterday (T19 Nov 25) | Δ |
|---|---|---|---|
| Total release (m³/s) | **310.67** | 321.08 | −10.41 (−3.2% — flat) |
| Turbined (m³/s) | **310.67** | 298.09 | +12.58 (+4.2% — flat) |
| Spilled (m³/s) | **0** | 23.00 | **−23.00 (−100% — spill eliminated, flag)** |
| Spill share (%) | **0%** | 7.2% | **−7.2 pp (flag)** |
| Headpond / amont (m) | **105.56** (T20) | 105.57 (T20 Nov 25) | −1 cm |
| Tailwater / aval (m) | **86.84** (T20) | 86.86 (T20 Nov 25) | −2 cm |
| Δh (head differential, m) | **18.72** | 18.69 | +3 cm |

Spill eliminated today (23.00 → 0 m³/s) with headpond essentially flat (105.56–105.57 m) — routine operator decision to route all flow through turbines when headpond level and load conditions allow it. No threshold implications. Total release within flat band. Headpond 105.56 m = **89 cm above** the 104.67 m band ceiling (Day 182 above band).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 26. Yesterday = T19 Nov 25 (from prior brief).*

| Site | Total (m³/s) | Spill % | Δ vs yesterday (T19 Nov 25) |
|---|---|---|---|
| Première-Chute (3-33) | **250.91** | 0% | −1.0% (flat) |
| Quinze (3-31) | **247.67** | 0.4% (1.0 m³/s) | −0.1% (flat) |
| Îles (3-32) | **245.17** | 0% | −1.1% (flat) |
| Rapide-2 (3-29) | **240.33** | 0% | −0.0% (flat) |
| Rapide-7 (3-28) | **238.88** | 0% | +0.2% (flat) |
| Bryson (3-46) | **310.67** | **0%** | −3.2% (flat); **spill eliminated (see above)** |
| Paugan — Gatineau R. (3-65) | **81.41** | 0% | +3.8% (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **104.22** | 0% | **−35.4% (flag; 161.28 → 104.22; Gatineau tributary dispatch)** |
| **Carillon — basin terminal (3-60)** | **535.09** T20 | 0% | HQ mean-through-T20 = **816 m³/s**; ORRPB daily prov 1,400 = T13 snapshot artifact (see below) |

### Carillon intraday pattern (HQ hourly, UTC Nov 26 — same demand-dispatch shape as Nov 25)

| UTC hour | Carillon release (m³/s) |
|---|---|
| Nov 26 T00 | 732.95 |
| T01 | 719.9 |
| T02–T04 | 891 range |
| T05 | 870.74 |
| T06 | 756.56 |
| T07–T08 | ~706 |
| T09 | 577.56 |
| T10 | 545.88 |
| T11 | 1,394.48 |
| T12 | 1,397.28 |
| T13 | **1,398.8** (peak) |
| T14 | 881.27 |
| T15–T16 | ~716 |
| T17 | 715.54 |
| T18 | 550.02 |
| T19–T20 | 534–535 |

ORRPB daily prov Nov 26 = 1,400 m³/s ≈ T13 value (1,398.8 m³/s) — same snapshot-of-morning-peak artifact as Nov 25. HQ hourly mean through T20 (21 h) = **816 m³/s**. Expected final ≈ **781 m³/s** (minimum, if remaining 3 h hold at ~535 m³/s). The +55.6% claim in the ORRPB daily prov (vs Nov 25 finalized 900 m³/s) fails the provisional-flow sanity check and is not reported as an event. Same daily dispatch shape as Nov 24 and Nov 25.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 19) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 26 — ORRPB daily prov (m³/s) | **384** | 369 (Nov 19 fin) | +15 | D11 prov: sub-400, uncertain (D1–D10 Nov 16–25 all sub-400 confirmed; D10 fin 375 ✓) |
| Témiscaming PSPC T00 cross-check (m³/s) | **384** | — | — | Exact match with ORRPB ✓; both sub-400 |
| Quinze release → into lake (m³/s) | **247.67** (T19) | — | flat | Upper cascade flat |
| Mattawa level (m) | **152.31** (Nov 26 prov) | 152.19 (Nov 19 — may be prov artifact) | +12 cm (treat as directional; Mattawa prov artifact pattern ongoing) | Provisional — treat directionally only |
| Pembroke level (m) | **111.04** (Nov 26 prov) | 111.12 (Nov 19 fin) | −8 cm | Gradual easing trend; direction only |

**Reservoir balance (T00 Nov 25 → T00 Nov 26):**

| Reservoir | Nov 25 (T00) | Nov 26 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.21 m | **219.20 m** | −1 cm | Steady |
| Dozois | 342.03 m | **342.02 m** | −1 cm | Steady |
| Quinze | 262.90 m | **262.92 m** | +2 cm | Steady |
| Témiscaming | 178.62 m | **178.63 m** | +1 cm | Steady |
| Poisson Blanc | 200.51 m | **200.53 m** | +2 cm | Steady |
| Cabonga | 359.66 m | **359.66 m** | 0 cm | Steady |
| Des Joachims | 152.14 m | **152.17 m** | +3 cm | Rising |
| Bark Lake (OPG) | 313.42 m | **313.39 m** | −3 cm | Falling |
| Rapide-7 | 308.95 m | **308.91 m** | −4 cm | Falling |
| Mitchinamecus | 379.30 m | **379.29 m** | −1 cm | Steady |
| Kipawa | 268.86 m | **268.86 m** | 0 cm | Steady |
| Kiamika | 266.54 m | **266.52 m** | −2 cm | Steady |
| Lady Evelyn | 288.91 m | **288.91 m** | 0 cm | Steady |
| Timiskaming (Haileybury) | 178.56 m | **178.56 m** | 0 cm | Steady |

**Balance: 2 falling · 11 steady · 1 rising** (Rapide-7 −4 cm, Bark Lake −3 cm falling; Des Joachims +3 cm rising). No active retention signal; no reservoir rising >10 cm/day. Normal late-autumn holding posture.

**Milestone bookkeeping (W47 rollup Nov 22 anchor + DB-verified chain):**

| Milestone | W47 close (Nov 22) | Nov 23 | Nov 24 | Nov 25 | **Nov 26** |
|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 204 | 205 | 206 | 207 | **208** |
| Bryson amont above band (104.67 m) | 178 | 179 | 180 | 181 | **182** |
| §15.3.5.1 trigger INACTIVE | 181 | 182 | 183 | 184 | **185** |
| Témiscaming sub-400 streak | D7 (349 fin) | D8 (373 fin ✓) | D9 (358 fin ✓) | D10 (375 fin ✓) | **D11 prov: 384 (sub-400, uncertain)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 26.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.25 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 185** (136 cm below trigger) |
| Carillon amont (1-2968) | **41.08 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Carillon morning dispatch peak (1,399 m³/s) is within normal turbine operations; no regulatory exceedance.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 26.*

| Reservoir | Nov 25 (T00) | Nov 26 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.21 m | **219.20 m** | −1 cm | Steady |
| Témiscaming | 178.62 m | **178.63 m** | +1 cm | Steady |
| Dozois | 342.03 m | **342.02 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.42 m | **313.39 m** | −3 cm | Falling |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs Nov 25 brief)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (probed: HTTP 200/128640b). Last Update: 2026-11-24 3:17 PM EST (2026-11-24T20:17:00Z UTC). Next Update: 2026-12-01 4:00 PM EST (2026-12-01T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` mode=`weekly-notice`.*

**UNCHANGED from Nov 24 update** (also unchanged from Nov 25 brief):

> *"Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly increase over the coming week, depending on locations. At some locations, water levels are below navigational chart datums."*

No flood-watch language. No change to Lac Coulonge / Britannia / Carillon-specific numeric forecasts (none given in current forecast; seasonal-language-only mode).

---

## Anomaly flags

1. **Bryson spill eliminated (23.00 → 0 m³/s, −100%).** Total release −3.2% (flat). Turbined +4.2% (flat). Headpond held flat (105.56–105.57 m). Routine operator posture optimization — spill converted to turbine output when headpond allows. No flood implication.
2. **Rapides-Farmers (Gatineau mouth, 3-67) −35.4% (161.28 → 104.22 m³/s).** Exceeds 5% flag threshold. Gatineau River tributary dispatch reduction; Paugan (Gatineau R. mainline, 3-65) up +3.8% — offsetting. Routine HQ Gatineau system dispatch.
3. **Carillon ORRPB daily prov Nov 26 = 1,400 m³/s (+55.6% vs Nov 25 finalized 900 m³/s) — FAILS provisional sanity check.** Prov matches HQ T13 hourly (1,398.8 m³/s). Snapshot artifact, not a running daily mean. HQ mean-through-T20 = 816 m³/s; expected final ≈ 781 m³/s. Reported in cascade table only; not headlined. Same pattern as Nov 24 and Nov 25.
4. **Témiscaming D11 prov = 384 m³/s.** Below 400; streak D1–D10 (Nov 16–25) all confirmed sub-400. D11 resolution tomorrow.
5. **Pipeline: detached HEAD (fifth episode).** Orphaned Nov 23 brief, W47 rollup, and Nov 25 brief fast-forwarded onto main before this commit. Public mirror missed these files since ~Nov 23 23:17 UTC (approximately 70 hours). Root cause unresolved (W47 rollup Human Queue item 1 — escalating pattern).

No flood-risk implications at any point in the basin. Lac Coulonge etat 0, 103.7 cm below pre-alert. §15.3.5.1 trigger inactive Day 185.

---

## Notes

- **Day 208** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (172 days stale). `freshet-forecast.json` regenerated without change. Human queue item 5 (W47 rollup) remains unresolved.
- **Témiscaming streak:** D10 Nov 25 finalized at 375 m³/s (sub-400, confirmed). D11 Nov 26 prov = 384 m³/s — well below 400, no near-miss ambiguity this time (vs D10 prov 401 which was 1 m³/s above). Expect D11 confirmation tomorrow.
- **Mattawa ORRPB daily artifact pattern** ongoing. Nov 26 prov 152.31 m; treat as directional only.
- **ORRPB next update Dec 1.** On weekly schedule (Nov 17 → Nov 24 → Dec 1).
- **Carillon ORRPB prov snapshot pattern:** This is now the third consecutive day (Nov 24, Nov 25, Nov 26) where the ORRPB Carillon daily provisional matches the morning HQ dispatch peak value rather than a running daily mean. The pattern is consistent with ORRPB pulling a fixed-hour snapshot of the HQ telemetry. As long as Carillon has a morning demand-dispatch peak, this will recur daily.
