# Daily brief — 2026-11-10

*Generated automatically at 23:02 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 105b). ORRPB forecast HTTP 200 ✓ — last update Nov 10 2:19 PM EST (**UPDATED** from Nov 3); next update Nov 17 4:00 PM EST (weekly cadence). Vigilance 1195: proxy ingest fresh T21 UTC Nov 10 (106.000 m). V3 posterior: ran successfully (exit 0) — `freshet-forecast.json` content unchanged (anchors on asof 2026-06-07; unchanged until `lac-coulonge-daily-1990-2026.csv` is extended). **PIPELINE GAP: Nov 9 brief never committed** — no Nov 9 brief in repo; last brief was Nov 8. Milestone table extended from W45 rollup anchor by 2 days (Nov 9 unbroken via DB, Nov 10 today).*

*Nov 8 retro (W45 rollup assigned correction): **CORRECTION — Nov 8 Témiscaming provisional 418 m³/s → final 376 m³/s (sub-400, D52 confirmed; "if 418 finalizes above 400, streak ends D51" claim VOIDED — streak extended to D52+)**. Nov 8 Mattawa retro: TL;DR headlined 152.27 m; DB final = **152.11 m** (−16 cm revision, outside ±5 cm tolerance — corrected). Nov 8 Pembroke: headlined 111.07 m; DB = 111.15 m (+8 cm, within tolerance — no correction). Nov 9 (no brief): Témiscaming DB = **382 m³/s** (revised from 363 m³/s seen at W45 rollup time; D53 sub-400 confirmed either way).*

---

## In plain language

### Upstream — the upper basin

The basin is 192 days past the May 2 seasonal peak and continues its quiet late-autumn recession. The outflow from Lake Timiskaming — the large lake separating Ontario and Quebec at the top of the Ottawa River watershed — is coming in at a preliminary 344 cubic metres per second for today, based on the ORRPB running daily average, while a midnight snapshot from the same gauge read 424 m³/s (a discrepancy of 80 m³/s above the reporting threshold; both are well below the sub-400 range the river has maintained since mid-September). The sub-400 streak is at 54 days and counting — Day 54 today is provisionally sub-400 on the ORRPB running mean.

Water levels at Mattawa — a gauge roughly 200 kilometres upstream of the properties — rose 27 centimetres today to 152.33 metres after two days of moderate decline. This uptick is consistent with a precipitation response; it does not change the broader recession trend. Pembroke, further downstream, edged down 9 centimetres to 111.07 metres. Among the basin's tracked reservoirs, one rose slightly (Dozois, up 3 cm), ten held steady, and three fell a few centimetres (Des Joachims pool, Kipawa, Timiskaming). Normal late-season posture — no active retention signal anywhere in the upper basin.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 106.000 metres at 9 PM UTC, down about 1.5 centimetres from the same hour yesterday (106.015 m). The lake is fully in normal conditions — 100 centimetres below the 107.00-metre pre-alert threshold, and 151 centimetres below the minor-flood mark. The ORRPB's weekly forecast, which was updated this afternoon at 2:19 PM Eastern time, now says that "water levels and flows are expected to remain fairly stable over the coming week" — the previous forecast had allowed for slight increases driven by precipitation, but that language has been dropped. No concern at the property.

Downstream, at the Bryson Generating Station — a facility reached via a long, winding channel well below the southern end of Lac Coulonge, not visible from the Mansfield/Fort-Coulonge shoreline — there is an operational development worth noting. All of the dam's turbine units appear to have been taken offline beginning around noon Eastern time yesterday (November 9), with the full flow now being routed through the spillway rather than the turbines. The total release remains similar at about 389 cubic metres per second, but every drop of that is now going over the spillway. This is the second consecutive day of this configuration, following a week of partial-spill operations (November 2–8, Day 1–7 at 38–48% spill). The operating switch to 100% spillway flow has no flood implications for the property reach — the total volume passing through Bryson is unchanged, and Lac Coulonge is 100+ centimetres below any flood threshold. At Carillon, the basin's terminal dam, today's late-afternoon reading was around 847 cubic metres per second, all turbined, no spillway involvement.

---

## TL;DR

**CORRECTIONS (Nov 8 retros):** Nov 8 Témiscaming → **final 376 m³/s (D52 sub-400; "streak ends D51" voided — streak continues)**. Nov 8 Mattawa → **final 152.11 m** (brief claimed 152.27 m, −16 cm revision). **PIPELINE GAP: Nov 9 brief was never committed.** Nov 9 Témiscaming DB (revised after W45 rollup): **382 m³/s (D53 sub-400)**. **Today (Day 192):** Lac Coulonge T21 **106.000 m** (−2 cm vs T21 yesterday; etat 0, 100 cm below pre-alert). ⚠ **Bryson Day 2 of 100% spill** (turbines offline since ~Nov 9 T12-T17 UTC): total 389.43 m³/s (−1.0%), **turbined 0 m³/s (−100%)**, spilled 389.43 m³/s (+105%), spill share 48.3%→**100%**. Headpond 105.57 m (flat; min today 105.47 m = 80 cm above 104.67 m ceiling, Day 166 above band). §15.3.5.1 trigger INACTIVE **Day 169** (Hull 41.25 m). Carillon T19 **846.89 m³/s** (0% spill). Témiscaming **provisional 344 m³/s** (ORRPB daily); **PSPC T00 424 m³/s** (**⚠ discrepancy +80 m³/s >50 threshold** — measurement-timing difference; preferred PSPC T00 above 400, ORRPB daily sub-400; D54 provisional open). Sanity check: ORRPB vs D53 final (382) = −38/−10% — below threshold. Mattawa **152.33 m** (+27 cm vs Nov 9 finalized 152.06 m — uptick, likely precipitation response). Pembroke **111.07 m** (−9 cm). Reservoir balance: **3 falling · 10 steady · 1 rising** (dozois +3 cm). **ORRPB forecast UPDATED** Nov 10 2:19 PM ET: changed from "slightly increase or remain fairly stable" → **"remain fairly stable"** (precipitation reference dropped; stable outlook for coming week; next Nov 17).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 10 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 10 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 10) | **106.000 m** |
| ORRPB daily Nov 10 | 105.99 m (provisional) |
| ORRPB daily Nov 9 (finalized) | 106.01 m |
| 24h delta (Vigilance T21 Nov 10 vs T21 Nov 9) | **−2 cm** (106.000 vs 106.015 m) |
| ORRPB daily delta (Nov 9 106.01 → Nov 10 105.99 provisional) | −2 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 100 cm below |
| Distance to minor flood (107.50 m) | 150 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Nov 10 (releases), T20 UTC Nov 10 (levels). Comparison: last brief T19 Nov 8 (releases), T20 Nov 8 (levels). Nov 9 brief was not committed — no Nov 9 comparison row available.*

| Metric | Today (T19 Nov 10) | Last brief (T19 Nov 8) | Δ |
|---|---|---|---|
| Total release (m³/s) | **389.43** | 393.27 | −3.84 (−1.0%) |
| Turbined (m³/s) | **0** | 203.29 | **−203.29 (−100%)** ⚠⚠ |
| Spilled (m³/s) | **389.43** | 189.99 | **+199.44 (+105%)** ⚠⚠ |
| Spill share (%) | **100%** | 48.3% | **+51.7 pp** ⚠⚠ |
| Headpond / amont (m) | **105.57** (T20) | 105.57 (T20 Nov 8) | 0 cm |
| Tailwater / aval (m) | **87.07** (T20) | 86.98 (T20 Nov 8) | +9 cm |
| Δh (head differential, m) | **18.50** | 18.59 | −9 cm |

⚠⚠ **Day 2 of 100% spillway routing.** Turbines went offline progressively Nov 9 from T12–T17 UTC (7 AM–12 noon ET). No turbine output for 30+ hours. Total release is similar to the Nov 2–8 partial-spill period (~393 m³/s avg); the change is in routing, not volume. Headpond held flat at 105.57 m (Nov 10 daily min 105.47 m = **80 cm above** the 104.67 m band ceiling — **Day 166** above band; lowest single-hour clearance since W44 Nov 2 at 81 cm).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 10.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **255.28** T19 | 0% |
| Quinze (3-31) | **252.50** T19 | 0.4% |
| Îles (3-32) | **250.04** T19 | 0% |
| Rapide-2 (3-29) | **157.36** T19 | 0% |
| Rapide-7 (3-28) | **159.45** T19 | 0% |
| Bryson (3-46) | **389.43** T19 | **100%** (Day 2 turbines offline) ⚠⚠ |
| Paugan — Gatineau R. (3-65) | **161.53** T20 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **176.51** T20 | 0% |
| Carillon — basin terminal (3-60) | **846.89** T19 | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 3) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 10 provisional — ORRPB (m³/s) | **344** | 350 (Nov 3) | −6 | D54 provisional sub-400 (ORRPB running daily mean) |
| Témiscaming Nov 10 — PSPC T00 cross-check (m³/s) | **424** | — | **⚠ +80 m³/s vs ORRPB (>50 threshold; measurement-timing difference: PSPC=midnight snapshot, ORRPB=running 22h daily mean; not a supply anomaly)** | PSPC T00 above 400; ORRPB daily sub-400; D54 open |
| Quinze release → into lake (m³/s) | **252.50** (T19) | — | — | Increased ~20% vs Nov 8 (210.90); stable baseload |
| Mattawa level (m) | **152.33** (Nov 10 ORRPB daily) | — | +27 cm vs Nov 9 finalized 152.06 | Uptick after 2-day decline — likely precipitation response; Nov 10 PROVISIONAL |
| Pembroke level (m) | **111.07** (Nov 10 ORRPB daily) | — | −9 cm vs Nov 9 finalized 111.16 | Direction only |

**PSPC/ORRPB note — Témiscaming Nov 10:** ORRPB running daily mean = 344 m³/s; PSPC midnight snapshot (T00 Nov 10 = 7 PM ET Nov 9) = 424 m³/s. These are different measurement types (daily average vs instantaneous). Discrepancy = 80 m³/s (>50 m³/s flag). Physical interpretation: flows were higher at midnight (424 m³/s) and have averaged 344 m³/s across the full day. Consistent with diurnal or overnight flow dynamics; not a supply anomaly. No sanity check required (ORRPB change vs D53 final = −38/−10%, below 25%/150 m³/s thresholds).

**RETRO — Nov 8 Témiscaming (W45 assigned correction):** Provisional 418 m³/s → **final 376 m³/s** (sub-400, D52 confirmed). "Streak ends D51" claim VOIDED. The streak ran through D52 (Nov 8 = 376) and has continued.

**Nov 9 Témiscaming (no brief — gap):** W45 rollup at 00:14 UTC Nov 10 showed 363 m³/s. DB today shows **382 m³/s** (secondary revision since rollup). D53 sub-400 confirmed either way.

**RETRO — Nov 8 Mattawa:** TL;DR headlined 152.27 m (−10 cm from Nov 7). DB finalized: **152.11 m** (−26 cm from Nov 7 finalized 152.37 m). The decline was sharper than headlined; direction was correct, magnitude was not. Nov 9 finalized at 152.06 m (continuing decline). Today (Nov 10 provisional): 152.33 m (+27 cm — uptick).

**Reservoir balance (T00 Nov 9 → T00 Nov 10):**
3 falling · 10 steady · 1 rising (dozois +3 cm). Normal late-season operations; no active retention signal (all well below 10 cm/day threshold).

**Milestone bookkeeping (W45 rollup anchor Nov 8 + 2 days via DB):**

| Milestone | W45 close (Nov 8) | Nov 9 (gap — DB) | **Nov 10** |
|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 190 | 191 | **192** |
| Bryson amont above band (104.67 m) | 164 | 165 | **166** (min today 105.47 m = 80 cm clearance) |
| §15.3.5.1 trigger INACTIVE | 167 | 168 | **169** |
| Témiscaming | D52 (376 final — corrected from prov 418) | D53 (382 — revised from 363 at rollup) | **D54 (344 prov / PSPC T00 424 — open)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 10.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.25 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 169** (136 cm below trigger) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull dock range today: 41.21–41.26 m (unchanged from Nov 8 range 41.22–41.28 m).

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 10.*

| Reservoir | Nov 9 (T00) | Nov 10 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.24 m | **219.25 m** | +1 cm | Steady |
| Témiscaming | 178.65 m | **178.61 m** | −4 cm | Falling (small; consistent with outflow > inflow) |
| Dozois | 342.04 m | **342.07 m** | +3 cm | Rising |
| Bark Lake (OPG) | 313.58 m | **313.57 m** | −1 cm | Steady |

All 14 tracked reservoirs (including timiskaming_haileybury as WSC level gauge): **3 falling · 10 steady · 1 rising** (dozois +3 cm). No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓ (probed: HTTP 200 / 128633b). Last Update: **2026-11-10 2:19 PM EST** (2026-11-10T19:19:00Z UTC). Next Update: 2026-11-17 4:00 PM EST (2026-11-17T21:00:00Z UTC). Cadence: weekly.*

**CHANGED from Nov 3 brief** — forecast updated today at 2:19 PM ET:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Water levels and flows are expected to remain fairly stable over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

**Key change from Nov 3 text:** Removed "With precipitation forecast over the coming days, water levels and flows are expected to slightly increase or remain fairly stable depending on location." Replaced with just "Water levels and flows are expected to remain fairly stable." The "slightly increase" option has been dropped; the outlook is now uniformly stable. Precipitation reference removed.

---

## Anomaly flags

1. ⚠⚠ **Bryson turbines offline — Day 2 (100% spillway routing).** All turbine output ceased progressively on Nov 9 starting ~T12 UTC (7 AM ET). By T17 UTC (noon ET) turbines were fully offline. Total release held steady (~389–430 m³/s range Nov 9–10). Spill share went from 48.3% (Nov 8) to 100% (Nov 9 T17 onwards). No flood implications; the total discharge reaching the river is essentially the same as during the partial-spill period. Likely a scheduled maintenance or dispatch outage. Ongoing — watch for turbine restoration.
2. **CORRECTION — Nov 8 Témiscaming:** provisional 418 m³/s → **final 376 m³/s (D52 sub-400)**. "If 418 finalizes above 400, streak ends D51" (Nov 8 anomaly flag 4) voided. Streak continues: D52 (Nov 8=376), D53 (Nov 9=382), D54 (today provisional).
3. **CORRECTION — Nov 8 Mattawa:** headlined 152.27 m; DB final **152.11 m** (−16 cm revision, outside ±5 cm tolerance).
4. **PIPELINE GAP — Nov 9 brief never committed.** No Nov 9 brief exists in the repo. W45 rollup ran at 00:14 UTC Nov 10 (before the brief run time), so the gap was not caught there. This is the first missed brief. Cause unknown — may be a session failure, Detached HEAD failure, or network issue. Human queue.
5. **PSPC/ORRPB discrepancy — Témiscaming Nov 10:** 424 vs 344 m³/s (+80 m³/s, >50 threshold). Measurement-timing difference (PSPC T00 midnight vs ORRPB running 22h daily mean). D54 sub-400 streak status open — ORRPB daily says sub-400, PSPC midnight says above. Watch for ORRPB finalization.
6. **ORRPB forecast CHANGED:** Nov 10 2:19 PM ET update dropped "slightly increase" language. Outlook now uniformly "remain fairly stable." Note: Mattawa rose 27 cm today despite the stable forecast — consistent with a precipitation event that the weekly forecast window may not fully resolve; not a forecast discrepancy at this scale.

No flood-risk implications. Lac Coulonge etat 0, 100 cm below pre-alert.

---

## Notes

- **Nov 9 brief gap:** This is the first daily brief gap in the monitoring period. The W45 rollup at 00:14 UTC Nov 10 did not cover a Nov 9 brief because the brief hadn't run yet (routine time is 22:00 UTC = 5 PM ET). The gap means: (a) the Nov 9 retro for the Nov 8 TL;DR was not performed (done here instead); (b) the ORRPB forecast change (Nov 10) would have been visible from yesterday but wasn't captured. Human queue — investigate root cause.
- **Bryson turbine outage mechanics:** The step-down was gradual over Nov 9 T12–T17 UTC (turbined fell 203→91→35→0 m³/s in four steps). This is not a sudden trip but an operator-driven curtailment. The headpond responded by rising from 105.58 to 105.65 m before stabilizing back to 105.57 m. The outage has lasted 30+ hours with no sign of restoration as of this run. If turbines remain offline through tomorrow, it will be Day 3.
- **Mattawa Nov 10 provisional:** The +27 cm figure is the ORRPB daily running mean for Nov 10, provisional. Given the pattern of Mattawa daily means revising ±10–20 cm day-over-day (see Nov 8 retro above), tomorrow's retro should check whether this settles. Direction (rise) is consistent with precipitation.
- **Lac Coulonge stable:** The lake has held within a 15 cm band (105.85–106.02 m) for the entire month of November. No ORRPB forecast change affects property flood risk.
- **V3 posterior CSV stale (W44/W45 HQ item 3 unresolved):** Script runs (exit 0) but anchors on 2026-06-07. `freshet-forecast.json` regenerated without change.
- **Detached HEAD:** Checked `git status` before writing brief. Local state: clean, `main` branch current. No detached-HEAD condition this run.

---

## HQ capture table addendum (Nov 9–10)

*Extends W45 rollup table (archived through Nov 8). Per-day daily min/max from `dam_levels` for the three case-file level series. Queried 2026-11-10T23:02 UTC.*

| Date | Bryson amont 1-2964 min–max (m) | Carillon amont 1-2968 min–max (m) | Hull dock 1-3675 min–max (m) |
|---|---|---|---|
| 2026-11-09 | 105.56–105.65 | 41.10–41.13 | 41.20–41.26 |
| 2026-11-10 | **105.47–105.57** | 41.10–41.13 | 41.21–41.26 |

Nov 10 Bryson amont new low (105.47 m, 80 cm above 104.67 m ceiling) — still far above threshold, streak intact. Hull daily max ≤41.26 m both days (trigger 42.61 m; minimum 135 cm clearance). No threshold breach.
