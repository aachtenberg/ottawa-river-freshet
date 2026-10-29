# Daily brief — 2026-10-29

*Generated automatically at 22:10 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **last updated Oct 27 3:46 PM EDT**, next update Nov 3 4:00 PM EDT (no update expected until Nov 3). Vigilance 1195: proxy ingest fresh T20 UTC Oct 29 (105.927 m). V3 posterior: exit 0, but CSV stale (asof 2026-06-07, **Day 57** consecutive stale CSV); `freshet-forecast.json` updated with stale-but-unchanged output.*

*Oct 28 retro-checks: **Oct 28 Témiscaming final 324 m³/s** (PSPC cross-check in yesterday's brief was 337 m³/s; revised −13 m³/s; direction sub-400 consistent — **D41 CONFIRMED**). Oct 28 Mattawa provisional 152.20 m → final 152.28 m (+8 cm; chronic underread confirmed; direction call "essentially flat" was conservative — actual +3 cm vs Oct 27 152.25 m, slightly rising).*

---

## In plain language

### Upstream — the upper basin

The upper basin remains in quiet late-autumn recession. October 28's daily outflow from Lake Timiskaming finalized at 324 cubic metres per second — the 41st consecutive day below 400 m³/s, extending a streak that began September 18. No current-day ORRPB provisional or PSPC cross-check is yet available for October 29; Day 42 is in progress. The Mattawa level provisionally reads 152.26 metres for October 29, barely changed from the October 28 final of 152.28 metres (subject to the chronic upward revision; actual finalized value typically runs 5–10 cm higher). Pembroke slipped three centimetres to 111.00 metres, continuing a gentle downward drift. The reservoir balance across the basin is 2 falling and 12 steady — Timiskaming and Des Joachims each shed three centimetres. Normal late-autumn drawdown; no storage-retention signal.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge slipped three centimetres to 105.94 metres — 106 centimetres below the 107.00-metre pre-alert threshold. No concern; normal recession.

Well downstream from the property, the dam pond at the Bryson Generating Station completed yet another large dispatch swing: spill volume dropped from 171 cubic metres per second yesterday (at 7 PM Eastern) to 55 cubic metres per second today (at 6 PM Eastern), while water through the turbines jumped from 211 to 302 cubic metres per second. Total release fell about 6 percent to 358 m³/s. Despite this shift, the dam pond level moved only 7 centimetres lower to 105.46 metres — consistent with HQ balancing inflows and outflows through dispatch. This is the fourth large day-over-day spill swing in a row (October 26 large surge, October 27 partial reversal, October 28 new surge, October 29 large reversal). The dam pond has been above the top of its normally permitted operating range for 154 consecutive days. This cycling has no upstream effect on the Mansfield properties, which are a long winding distance above the dam.

The ORRPB forecast, last updated October 27, continues to call for flows and levels to "slightly decrease or remain fairly stable" over the coming week. Next update due November 3. No flood watch; no precipitation event mentioned.

---

## TL;DR

**RETRO ✓:** Oct 28 Témiscaming final 324 m³/s (PSPC had been 337; −13 revision, sub-400 consistent) → **D41 CONFIRMED**. Mattawa Oct 28 provisional 152.20 → final 152.28 m (+8 cm; chronic underread; direction "flat" was conservative — actual +3 cm, slightly rising). **Today:** Lac Coulonge **−3 cm** to **105.94 m** (Vigilance T20: 105.927 m; etat 0, 106 cm below pre-alert). Bryson spill **−67.6%** (171.02→55.40 m³/s), turbines +43.1% (211.15→302.23), total −6.4% (382.16→357.63); spill share 44.8%→15.5%; headpond −7 cm to 105.46 m (Day 154 above band). Carillon −0.4% (840.32→836.64 m³/s). Hull dock T18 41.27 m — trigger INACTIVE **Day 157**. Reservoir balance: 2 falling (timiskaming/des_joachims −3 cm each) · 12 steady · 0 rising. D42 in progress (no ORRPB provisional yet; PSPC flow unavailable). Day **180** since May 2 peak. ORRPB forecast unchanged (next update Nov 3).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 29 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 29 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 29) | **105.927 m** |
| ORRPB daily Oct 29 | 105.94 m (provisional same-day) |
| 24h delta (ORRPB daily Oct 28→29) | **−3 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 106 cm below |
| Distance to minor flood (107.50 m) | 156 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T18 UTC Oct 29. Yesterday: T19 UTC Oct 28.*

| Metric | Today (T18 Oct 29) | Yesterday (T19 Oct 28) | Δ |
|---|---|---|---|
| Total release (m³/s) | **357.63** | 382.16 | **−24.53 (−6.4%) ⚠** |
| Turbined (m³/s) | **302.23** | 211.15 | **+91.08 (+43.1%) ⚠** |
| Spilled (m³/s) | **55.40** | 171.02 | **−115.62 (−67.6%) ⚠** |
| Spill share (%) | **15.5%** | 44.8% | **−29.3 pp ⚠** |
| Headpond / amont (m) | **105.46** | 105.53 | −7 cm |
| Tailwater / aval (m) | **86.88** | 86.95 | −7 cm |
| Δh (head differential, m) | **18.58** | 18.58 | 0 |

All three change thresholds exceeded (total −6.4%, turbined +43.1%, spill −67.6%). Headpond 105.46 m is 79 cm above the 104.67 m band ceiling — **Day 154** above band (ongoing status). Head differential unchanged; dam pond dropped 7 cm, consistent with the dispatch swing rather than an uncontrolled inflow event. Fourth large Bryson dispatch oscillation in four days.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18 UTC Oct 29. Yesterday comparison: T19 UTC Oct 28.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **211.89** T18 | 0% | +2.1 (+1.0%) |
| Quinze (3-31) | **208.70** T18 | 0.4% | +0.1 (flat) |
| Îles (3-32) | **210.88** T18 | 0% | −3.1 (−1.5%) |
| Rapide-2 (3-29) | **157.23** T18 | 0% | +0.0 (flat) |
| Rapide-7 (3-28) | **158.12** T18 | 0% | +0.5 (flat) |
| Bryson (3-46) | **357.63** T18 | 15.5% | **−24.5 (−6.4%) ⚠** |
| Paugan — Gatineau R. (3-65) | **150.91** T18 | 0% | −0.7 (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **147.47** T18 | 0% | **−8.6 (−5.5%) ⚠** |
| Carillon — basin terminal (3-60) | **836.64** T18 | 0% | −3.7 (−0.4%) |

Bryson −6.4% exceeds the 5% flag threshold; spill share back to 15.5% after yesterday's 44.8% peak. Rapides-Farmers −5.5% also exceeds threshold; Paugan (upstream on Gatineau) was flat — divergence could reflect routing lag or measurement noise, not a structural event.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 22) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 28 final (m³/s) | **324** *(Oct 29 not yet posted)* | 376 (Oct 22) | −52 | **D41 confirmed; D42 in progress** |
| Timiskaming PSPC cross-check Oct 29 T00 | level 178.61 m, **flow unavailable** | — | level −3 cm vs Oct 28 T00 | No cross-check today; sub-400 trend consistent |
| Quinze release → into the lake (m³/s) | **208.70** (T18) | ~376 (Oct 22) | — | Baseload dispatch |
| Mattawa level (m) | **152.26** *(provisional — chronic underread caution)* | n/a | −2 cm vs Oct 28 final (152.28) | Near-flat; likely slightly rising on finalization |
| Pembroke level (m) | **111.00** (Oct 29 daily) | n/a | −3 cm vs Oct 28 (111.03) | Gently declining |

PSPC flow unavailable for Oct 29 T00; no cross-check possible today.

**Reservoir balance (T00 Oct 28 → T00 Oct 29):**
2 falling · 12 steady · 0 rising. timiskaming −3 cm; des_joachims −3 cm (minor late-autumn drawdown, no retention signal).

**Milestone bookkeeping (W43 anchor Oct 25 + Oct 26–29 extension):**

| Milestone | W43 close (Oct 25) | Oct 26 | Oct 27 | Oct 28 | **Oct 29** |
|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 176 | 177 | 178 | 179 | **180** |
| Bryson amont above band (104.67 m) | 150 | 151 | 152 | 153 | **154** |
| §15.3.5.1 trigger INACTIVE | 153 | 154 | 155 | 156 | **157** |
| Témiscaming sub-400 | D38 (333) | D39 (347 ✓) | D40 (331 ✓) | D41 (324 ✓) | D42? (no provisional) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T18 UTC Oct 29.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 157** (134 cm below trigger; −3 cm vs yesterday) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 29.*

| Reservoir | Oct 28 (T00) | Oct 29 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.28 m | **219.26 m** | −2 cm | Steady |
| Témiscaming | 178.64 m | **178.61 m** | −3 cm | Falling |
| Dozois | 342.17 m | **342.15 m** | −2 cm | Steady |
| Bark Lake (OPG) | 313.67 m | **313.65 m** | −2 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-27 3:46 PM EDT** (2026-10-27T19:46:00Z UTC). **Next Update: 2026-11-03 4:00 PM EDT** (2026-11-03T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Oct 28 brief** — no new ORRPB update today (next update Nov 3). Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to slightly decrease or remain fairly stable over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false.

---

## Anomaly flags

1. **Bryson dispatch oscillation — Day 4.** Spill −67.6% (171.02→55.40 m³/s), turbines +43.1% (211.15→302.23 m³/s), total −6.4% (382.16→357.63 m³/s). Spill share 44.8%→15.5%. Headpond dropped 7 cm to 105.46 m. Pattern: Oct 26 large spill surge, Oct 27 partial reversal, Oct 28 large surge, Oct 29 large reversal. Headpond has ranged 105.46–105.54 m across all four days — stable despite the amplitude; no structural head rise. Ongoing Day 154 above band is status, not a new event.

2. **Rapides-Farmers −5.5%** (156.10→147.47 m³/s, T19 Oct 28 → T18 Oct 29). Paugan (upstream Gatineau) was flat (−0.7 m³/s). Divergence noted; likely routing lag or short-term inflow variation. No spill change anywhere (0% throughout).

None of the above affects property flood risk. Lac Coulonge etat 0, 106 cm below pre-alert.

---

## Notes

- **Oct 28 retro summary:** Témiscaming 324 m³/s (D41 confirmed; PSPC cross-check had been 337, revision −13 within normal range). Mattawa Oct 28 provisional 152.20 → final 152.28 m (+8 cm; chronic underread confirmed; direction "essentially flat" was accurate at ±3 cm).
- **Bryson spill cycling:** Four-day pattern (Oct 26–29): +90.9%, −26.5%, +231.7%, −67.6%. Headpond held 105.46–105.54 m throughout — the amplitude of these spill swings is large but the dam pond is stable, confirming HQ dispatch optimization. Not an inflow event.
- **D42 status:** No ORRPB provisional available for Oct 29 at brief time. PSPC flow unavailable (T00 row exists but flow=None). Témiscaming level at T00 Oct 29 was 178.61 m (−3 cm from Oct 28 T00 178.64 m) — consistent with continued sub-400 outflow and ongoing recession. D42 provisional confirmation will appear in tomorrow's retro.
- **V3 posterior:** Day 57 stale CSV (asof 2026-06-07, exit 0 today — script ran normally, underlying daily CSV not updated). `freshet-forecast.json` written but reflects June 7 state (last-valid data). Committed alongside this brief for dashboard continuity.
