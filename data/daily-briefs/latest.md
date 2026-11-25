# Daily brief — 2026-11-25

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200/113b). ORRPB conditions forecast HTTP 200 ✓ (probed: HTTP 200/128648b; forecast UPDATED Nov 24 3:17 PM — text changed). Vigilance 1195: proxy ingest fresh T21 UTC Nov 25. V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (170 days stale — unchanged). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 25.*

*Pipeline note: no brief was produced on Nov 24 (pipeline gap, Day 206). Two commits were also found on an orphaned detached HEAD (Nov 23 brief + W47 rollup); cherry-picked onto main prior to this commit — public mirror missed Nov 23 brief and W47 rollup until this push. This is the fourth detached-HEAD episode in five weeks (W44/W45/W47 prior episodes per rollup history). Root cause unresolved.*

*Nov 23 retro: Témiscaming D8 prov (335 ORRPB / 398 PSPC T00) → finalized **373 m³/s** (CONFIRMED sub-400 D8; both prov values were below 400 ✓). Des Joachims prov 500 m³/s ("minimum confirmed increase ≈ +22%") → finalized **404 m³/s** (+3.6% vs Nov 22 390 m³/s = essentially flat — **RETRACTION: the "min +22%" claim was false**; the prov was a point-measurement snapshot, not a 19-hour running mean, so the feasibility back-out produced an incorrect floor; sanity checks passed the wrong way). Mattawa prov 152.37 m → finalized **152.18 m** (Δ −19 cm — **ARTIFACT/REVISED**, week 7 of Mattawa ORRPB daily artifact pattern). Pembroke prov 111.06 m → finalized **111.13 m** (+7 cm, REVISED, outside ±5 cm).*

*CORRECTION (W47 rollup HQ item 3 — first opportunity after pipeline gap): Nov 17 Mattawa ORRPB daily prov 152.20 m → DB final **152.32 m** (+12 cm, REVISED) — no correction was issued in the Nov 18 brief. Closing this item now.*

---

## In plain language

### Upstream — the upper basin

The upper basin is on Day 207 past the May 2 freshet peak, and flow out of Lake Timiskaming edged back above the 400 cubic-metres-per-second level in tonight's snapshot — just barely, at 401 m³/s. That's one cubic metre per second above the round-number threshold that has defined the nine-day sub-400 streak since November 16. Because this is a midnight snapshot value rather than a finalized 24-hour average, the streak remains uncertain until tomorrow's data settles. The confirmed nine-day run (November 16 through 24) is solid; whether today extends it to ten or breaks it at nine won't be known until tomorrow.

The mid-valley gauges are holding largely steady. The water level at Mattawa edged up five centimetres today (a provisional figure that may revise), while the gauge at Pembroke slipped four centimetres — both moves are small and consistent with the flat-to-gently-declining pattern of recent weeks. Fourteen of the tracked upper-basin storage reservoirs were essentially flat overnight, with only three (Bark Lake, the Des Joachims pool, and Mitchinamecus) falling by as much as three centimetres. No reservoir is gaining level — the basin is not absorbing inflow in any significant way; operators are passing water through at roughly the rate it arrives.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge continued drifting sideways tonight, holding at essentially 105.975 metres — less than a centimetre below yesterday's reading, and sitting more than a metre below the first alert threshold. The lake is fully normal.

Hydro-Québec's operational pattern at Carillon — the large generating station at the mouth of the Ottawa River, far downstream of the property — repeated the same morning dispatch peak seen on November 23: a ramp-up to roughly 1,400 cubic metres per second between 11 AM and 1 PM Eastern time, then a step-back down through the afternoon. By 7 PM Eastern (the last telemetry in this run) it had settled near 693 m³/s, about half the morning peak. This is electricity-demand management for the winter heating season, and carries no flood implication anywhere in the basin.

The ORRPB weekly forecast, last updated Monday November 24, made a subtle but notable change to its outlook: the previous week's text said flows were expected to "remain fairly stable or slightly **decrease**" over the coming week; the new text substitutes "slightly **increase**." The magnitude of change is small, and the overall framing ("close to seasonal values") is unchanged. Next forecast update is expected December 1.

---

## TL;DR

**RETRO Nov 23: Témiscaming D8 prov (335/398) → final 373 m³/s (CONFIRMED sub-400 D8 ✓). Des Joachims prov 500 → final 404 m³/s (RETRACTED: prov was snapshot artifact, not running mean; feasibility back-out invalid; "min +22%" claim false — actual +3.6% = flat). Mattawa prov 152.37 → final 152.18 m (−19 cm, ARTIFACT, week 7). Pembroke prov 111.06 → final 111.13 m (+7 cm, REVISED).**
**CORRECTION (W47 rollup HQ item 3): Nov 17 Mattawa prov 152.20 → DB final 152.32 m (+12 cm, REVISED) — first opportunity to publish after pipeline gap.**
**Pipeline gap Nov 24: no brief produced. Orphaned Nov 23 brief + W47 rollup cherry-picked to main (fourth detached-HEAD episode).**
**Today (Day 207):** Lac Coulonge T21 **105.975 m** (−0.3 cm vs T21 Nov 23; etat 0, 102.5 cm below pre-alert; ORRPB daily prov 105.97 m — flat). Bryson T19: total **321.08 m³/s** (−0.0% vs T23 Nov 24 321.14; spill **7.2%** = 23.00 m³/s, flat). Headpond T20 **105.57 m** (+2 cm vs T23 Nov 24; Day 181 above band). §15.3.5.1 trigger INACTIVE **Day 184** (Hull 41.25 m). Carillon: morning peak T11–T13 UTC at **1,376–1,404 m³/s** (HQ demand dispatch, same Nov 23 pattern), stepping down to T19 **692.84 m³/s**; mean-through-T19 = **860 m³/s**, min final ≈ **861 m³/s**. **ORRPB Carillon daily prov 1,378 = snapshot of T12 peak value — fails provisional sanity check; report in table only.** Mid-cascade: Rapide-2 **+53.1%** (240.39 m³/s vs Nov 24 T23 156.98), Rapide-7 **+51.7%** (238.5 vs 157.17) — real HQ telemetry; dispatch rebalancing. Paugan (Gatineau) **−16.2%** (78.46 vs 93.68). **Témiscaming D10 prov: PSPC T00 401 m³/s (1 m³/s above 400 — UNCERTAIN; D1–D9 Nov 16–24 all sub-400 confirmed).** Mattawa prov 152.38 m (+5 cm vs Nov 24 fin 152.33 m — provisional). Pembroke −4 cm (111.04 prov). Reservoir balance: **3 falling · 11 steady · 0 rising**. **ORRPB forecast updated Nov 24 3:17 PM: "slightly increase" (changed from "slightly decrease"); next update Dec 1 4:00 PM.**

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 25 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 25 provisional (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 25) | **105.975 m** |
| ORRPB daily Nov 25 (provisional) | 105.97 m |
| ORRPB daily Nov 24 (finalized) | 105.97 m |
| 24h delta (Vigilance T21 Nov 25 vs T21 Nov 23) | **−0.3 cm** (note: Nov 24 T21 not independently available; two-day span across pipeline gap) |
| ORRPB daily delta (Nov 24 fin 105.97 → Nov 25 prov 105.97) | 0 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 102.5 cm below |
| Distance to minor flood (107.50 m) | 152.5 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 (releases) / T20 (levels) UTC Nov 25. Yesterday: T23 Nov 24.*

| Metric | Today (T19/T20 Nov 25) | Yesterday (T23 Nov 24) | Δ |
|---|---|---|---|
| Total release (m³/s) | **321.08** | 321.14 | −0.06 (−0.0% — flat) |
| Turbined (m³/s) | **298.09** | 298.17 | −0.08 (flat) |
| Spilled (m³/s) | **23.00** | 22.96 | +0.04 (flat) |
| Spill share (%) | **7.2%** | 7.1% | +0.1 pp (flat) |
| Headpond / amont (m) | **105.57** (T20) | 105.55 (T23 Nov 24) | +2 cm |
| Tailwater / aval (m) | **86.86** (T20) | 86.86 (T23 Nov 24) | 0 cm |
| Δh (head differential, m) | **18.71** | 18.69 | +2 cm |

No change exceeds 5% in any series. Headpond 105.57 m = **90 cm above** the 104.67 m band ceiling (Day 181 above band). No threshold changes.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19 UTC Nov 25 (all sites). Yesterday = T23 Nov 24 from `dam_releases` time-filter query.*

| Site | Total (m³/s) | Spill % | Δ vs yesterday (T23 Nov 24) |
|---|---|---|---|
| Première-Chute (3-33) | **253.5** | 0% | −3.3% (flat) |
| Quinze (3-31) | **247.84** | 0.4% (1.0 m³/s) | −4.9% (flat) |
| Îles (3-32) | **247.97** | 0% | −5.0% (at flag boundary) |
| Rapide-2 (3-29) | **240.39** | 0% | **+53.1% (flag; real HQ telemetry)** |
| Rapide-7 (3-28) | **238.5** | 0% | **+51.7% (flag; real HQ telemetry)** |
| Bryson (3-46) | **321.08** | **7.2%** (23.0 m³/s) | −0.0% (flat) |
| Paugan — Gatineau R. (3-65) | **78.46** | 0% | **−16.2% (flag)** |
| Rapides-Farmers — Gatineau mouth (3-67) | **161.28** | 0% | N/A (Nov 24 T23 not retrieved) |
| **Carillon — basin terminal (3-60)** | **692.84** T19 | 0% | HQ mean-through-T19 = **860 m³/s**; ORRPB daily prov 1,378 = snapshot artifact (see below) |

### Carillon intraday pattern (HQ hourly telemetry — repeats Nov 23 morning-peak pattern)

| UTC hour | Carillon release (m³/s) |
|---|---|
| Nov 25 T00 | 930.6 |
| T01–T05 | 790–874 |
| T06–T09 | ~790 |
| T10 | 533.5 (brief dip) |
| T11 | 1,376.2 |
| T12 | **1,378.2** ← matches ORRPB prov exactly |
| T13 | 1,404.2 (peak) |
| T14 | 879.5 (sharp step-down) |
| T15–T16 | 685–686 |
| T17–T19 | 714–718 (partial recovery) |
| T19 current | **692.8** |

ORRPB daily prov 1,378 m³/s = HQ T12 value (1,378.2 m³/s). This is a snapshot artifact, not a running 24-hour mean. HQ hourly mean through T19 (20 h) = **860 m³/s**. Expected final ≈ **861 m³/s** (minimum possible, if remaining 5h = current 693 m³/s). The +71% claim in the ORRPB daily prov (vs Nov 24 finalized 806 m³/s) fails the provisional-flow sanity check and is not reported as a surge.

**Cascade context:** Rapide-2 and Rapide-7 doubled their release today (from ~157 m³/s to ~240 m³/s), while Première-Chute, Quinze, and Îles eased ~3–5% lower. This is a mid-cascade dispatch shift: HQ increased flow through the mid-reach dams while slightly reducing the upper cascade. Paugan (Gatineau River) stepped down 16% (93.7 → 78.5 m³/s). Bryson, the mid-reach pivot into the property reach, was unaffected and held flat. All flow is turbined throughout the cascade (0% spill at all sites except Bryson at 7.2% and trace spill at Quinze). Normal HQ seasonal dispatch operations.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 18) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 25 — PSPC T00 (m³/s) | **401** | 361 (Nov 18 fin) | +40 | D10 prov: 1 m³/s above 400 — **UNCERTAIN** (streak D1=Nov 16 through D9=Nov 24 all sub-400 confirmed) |
| Témiscaming PSPC cross-check T00 (timiskaming reservoir flow) | **401** | — | — | Matches orrpb_river_flows exactly (consistent; still 1 m³/s above 400) |
| Quinze release → into lake (m³/s) | **247.84** (T19) | — | −4.9% vs Nov 24 T23 | Flat; upper cascade stepped down from Nov 23 dispatch peak |
| Mattawa level (m) | **152.38** (Nov 25 prov) | — | +5 cm vs Nov 24 fin 152.33 m | Provisional; treat directionally only (Mattawa ORRPB daily artifact pattern active) |
| Pembroke level (m) | **111.04** (Nov 25 prov) | 111.08 (Nov 18 fin) | −4 cm | −4 cm vs Nov 24 fin 111.08 m; easing |

**Reservoir balance (T00 Nov 24 → T00 Nov 25):**

| Reservoir | Nov 24 (T00) | Nov 25 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.22 m | **219.22 m** | 0 cm | Steady |
| Dozois | 342.04 m | **342.04 m** | 0 cm | Steady |
| Quinze | 262.90 m | **262.90 m** | 0 cm | Steady |
| Témiscaming | 178.63 m | **178.62 m** | −1 cm | Steady |
| Poisson Blanc | 200.49 m | **200.51 m** | +2 cm | Steady (within ±2 cm band) |
| Cabonga | 359.66 m | **359.66 m** | 0 cm | Steady |
| Des Joachims | 152.14 m | **152.11 m** | −3 cm | Falling |
| Bark Lake (OPG) | 313.46 m | **313.43 m** | −3 cm | Falling |
| Rapide-7 | 308.97 m | **308.96 m** | −1 cm | Steady |
| Mitchinamecus | 379.32 m | **379.29 m** | −3 cm | Falling |
| Kipawa | 268.87 m | **268.86 m** | −1 cm | Steady |
| Kiamika | 266.55 m | **266.54 m** | −1 cm | Steady |
| Lady Evelyn | 288.94 m | **288.92 m** | −2 cm | Steady |
| Timiskaming (Haileybury) | 178.56 m | **178.56 m** | 0 cm | Steady |

**Balance: 3 falling · 11 steady · 0 rising** (Des Joachims −3 cm, Bark Lake −3 cm, Mitchinamecus −3 cm falling; nothing above +2 cm). No active retention signal. Normal late-autumn holding posture.

**Milestone bookkeeping (W47 rollup Nov 22 anchor + DB-verified chain):**

| Milestone | W47 close (Nov 22) | Nov 23 | Nov 24 | **Nov 25** |
|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 204 | 205 | 206 | **207** |
| Bryson amont above band (104.67 m) | 178 | 179 | 180 | **181** |
| §15.3.5.1 trigger INACTIVE | 181 | 182 | 183 | **184** |
| Témiscaming sub-400 streak | D7 (349 fin) | D8 (373 fin ✓) | D9 (358 fin ✓) | **D10 prov: PSPC T00 401 (1 m³/s above 400 — UNCERTAIN)** |

*Nov 24 continuity (pipeline gap): Bryson headpond T23 Nov 24 = 105.55 m (above 104.67 m → D180 ✓); Hull dock T20 Nov 25 and hourly series confirm Hull well below 42.61 m throughout Nov 24 → trigger INACTIVE D183 ✓. Nov 24 Témiscaming (358 m³/s) sub-400 → D9 ✓.*

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 25.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.25 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 184** (136 cm below trigger) |
| Carillon amont (1-2968) | **41.11 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. The morning Carillon dispatch peak (1,404 m³/s max) is entirely within normal turbine operations; no regulatory exceedance.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 25.*

| Reservoir | Nov 24 (T00) | Nov 25 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.22 m | **219.22 m** | 0 cm | Steady |
| Témiscaming | 178.63 m | **178.62 m** | −1 cm | Steady |
| Dozois | 342.04 m | **342.04 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.46 m | **313.43 m** | −3 cm | Falling |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs Nov 23 brief)

*Source: `ottawariver.ca/conditions/?display=forecast` — HTTP 200 ✓ (probed: HTTP 200/128648b). Last Update: 2026-11-24 3:17 PM EST (2026-11-24T20:17:00Z UTC). Next Update: 2026-12-01 4:00 PM EST (2026-12-01T21:00:00Z UTC). Cadence: weekly. `forecast/latest.json` updated with mode=`weekly-notice`, fetched_at updated to 2026-11-25T22:00:00Z.*

**CHANGED from Nov 17 text (missed on Nov 24 due to pipeline gap, captured now):**

Previous forecast text (Nov 17 through Nov 23 brief):
> *"...Flows and levels are expected to remain fairly stable or slightly **decrease** over the coming week..."*

**Current forecast text (Nov 24 3:17 PM):**
> *"Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly **increase** over the coming week, depending on locations. At some locations, water levels are below navigational chart datums."*

Direction shifted from "slightly decrease" to "slightly increase." The overall framing ("close to seasonal values") is unchanged. No flood-watch language added.

---

## Anomaly flags

1. **ORRPB forecast direction change: "slightly decrease" → "slightly increase"** (updated Nov 24 3:17 PM; next update Dec 1). The shift is directionally notable for the property reach, but the forecast remains entirely within normal seasonal language. No flood-watch language. Noted for record.
2. **Rapide-2 +53.1% (240.39 vs 156.98 m³/s) and Rapide-7 +51.7% (238.5 vs 157.17 m³/s).** Real HQ telemetry; exceeds 5% flag threshold. Mid-cascade dispatch rebalancing today: HQ increased mid-reach output while slightly reducing upper cascade. Bryson and Carillon unchanged / stepping down. No flood implication.
3. **Paugan (Gatineau) −16.2% (78.46 vs 93.68 m³/s).** Exceeds 5% flag threshold. Gatineau dispatch reduction. Normal HQ scheduling.
4. **Carillon ORRPB daily prov 1,378 m³/s (+70.7% vs Nov 24 finalized 806 m³/s) — FAILS provisional sanity check.** Prov matches HQ T12 hourly value exactly (1,378.2 m³/s). This is a snapshot of the morning peak, not a running daily mean. HQ mean-through-T19 = 860 m³/s; expected final ≈ 861 m³/s. Reported in cascade table only; not headlined.
5. **Témiscaming D10 PSPC T00 prov = 401 m³/s (1 m³/s above 400).** Streak D1–D9 (Nov 16–24) all sub-400 confirmed. D10 status uncertain. Expect resolution tomorrow.
6. **Pipeline gap Nov 24** — no brief produced. Property data (etat 0, flat) not materially affected, but the ORRPB forecast update was missed by one day.
7. **Detached HEAD (fourth episode) — Nov 23 brief and W47 rollup were orphaned on detached HEAD; cherry-picked to main before this commit.** Public mirror was approximately 36 hours behind (Nov 23 brief from Nov 23 23:17 UTC through this push on Nov 25 ~22:00 UTC). Root cause unresolved (see W47 rollup Human Queue item 1).

No flood-risk implications at any point in the basin. Lac Coulonge etat 0, 102.5 cm below pre-alert. §15.3.5.1 trigger inactive Day 184.

---

## Notes

- **Day 207** since the May 2 freshet peak (2,741 m³/s).
- **V3 posterior CSV stale:** anchors on asof 2026-06-07 (170 days stale). `freshet-forecast.json` regenerated without change. Human queue item 5 (W47 rollup) remains unresolved.
- **Témiscaming streak caution.** PSPC T00 Nov 25 = 401 m³/s — exactly 1 m³/s above the 400 m³/s threshold. The same near-miss pattern occurred on Nov 23 (PSPC T00 398, 2 below) and was confirmed sub-400. The T00 is a midnight snapshot; the finalized 24h average often differs. If Nov 25 finalizes at ≥400, the streak runs D1–D9 (9 days). If it finalizes sub-400, D10 extends the streak to 10 days.
- **Des Joachims retro learning note.** The feasibility back-out check for the Nov 23 Des Joachims prov 500 assumed the prov was a 19-hour running mean (computed at brief-run time 22:00 UTC). The actual final of 404 m³/s fell below the computed floor of 477 m³/s, which is physically impossible for a running hourly mean. This confirms the ORRPB daily prov is NOT always a running mean — it can be a snapshot of a recent dispatch rate (possibly updated at a fixed hour during the day). The feasibility back-out in the guardrail is only valid when you can confirm the prov is a running mean. When the prov value matches a known recent hourly measurement (as in the Carillon case today, where prov 1,378 = T12 value 1,378.2), the snapshot origin is confirmed and the feasibility back-out does not apply. Flag all such cases.
- **ORRPB next update Dec 1.** Transition from "weekly" Nov cadence: last three updates were Nov 17 → Nov 24 → Dec 1 (7-day gaps). Cadence held.
- **Mattawa ORRPB daily artifact pattern** ongoing (week 7). Prov 152.38 m today; expect finalization to differ, treat as directional only.
