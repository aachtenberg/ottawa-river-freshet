# Daily brief — 2026-10-30

*Generated automatically at 22:10 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (206 KB). ORRPB forecast HTTP 200 ✓ (129 KB) — **last updated Oct 27 3:46 PM EDT**, next update Nov 3 4:00 PM EDT (weekly cadence; no update expected until Nov 3). Vigilance 1195: proxy ingest fresh T20 UTC Oct 30 (105.936 m). V3 posterior: exit 0 today (Day **58** stale CSV; asof 2026-06-07; underlying daily CSV not updated — W43 HQ item 1 unresolved); `freshet-forecast.json` written with same stale content.*

*Oct 29 retro-checks: **Oct 29 Témiscaming final 325 m³/s** (ORRPB PSPC; D42 confirmed — yesterday's brief had no provisional, correctly said "D42 in progress"). Oct 29 Mattawa provisional 152.26 m → final 152.28 m (+2 cm chronic underread; direction "essentially flat" confirmed accurate). No provisionals were headlined yesterday — retro clean.*

---

## In plain language

### Upstream — the upper basin

The upper basin continues its undisturbed late-autumn recession. October 29's outflow from Lake Timiskaming has now finalized at 325 cubic metres per second — the 42nd consecutive day below 400 m³/s, with today (Day 43) in progress. The Témiscaming PSPC cross-check for this morning's reading carried a corrupted negative-flow value and cannot be used today; the level at 178.64 metres is consistent with continued sub-400 outflow and the ongoing gentle recession. The Mattawa station rose just one centimetre to 152.29 metres — essentially flat for a third straight day — while Pembroke held at 111.02 metres, flat for a second day. Neither of these small moves is meaningful; the mid-valley reach is in quiet, stable late-autumn mode. All fourteen tracked reservoirs are steady within two centimetres day over day — no storage-loading or retention signal anywhere in the upper basin.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge is unchanged from yesterday at 105.94 metres — 106 centimetres below the 107.00-metre pre-alert threshold, well within the normal range. No concern; flat recession.

Well downstream from the property, the dam pond at the Bryson Generating Station continues a pattern of large day-over-day dispatch swings for a fifth consecutive day: today all spillway flow was cut off entirely (from 55 cubic metres per second yesterday to zero today) while water through the turbines edged slightly down, dropping total release by about 17 percent. The dam pond actually rose 13 centimetres to 105.59 metres — consistent with HQ holding back a little more water for hydraulic head — and remains 92 centimetres above the top of its normal operating range for the 155th consecutive day. This cycling is HQ dispatch optimization, not an inflow event, and has no upstream effect on the Mansfield properties.

The ORRPB forecast, last updated October 27, continues to call for flows and levels to "slightly decrease or remain fairly stable" over the coming week. Next update due November 3. No flood watch.

---

## TL;DR

**RETRO ✓:** Oct 29 Témiscaming final 325 m³/s → **D42 CONFIRMED** (brief had no provisional; retro clean). Mattawa Oct 29 provisional 152.26 → final 152.28 m (+2 cm; direction confirmed). **Today:** Lac Coulonge **flat, 0 cm** at **105.94 m** (Vigilance T20: 105.936 m; etat 0, 106 cm below pre-alert). Bryson spill **−100%** (55.40→0 m³/s), total **−17.2%** (357.63→295.97 m³/s); spill share 15.5%→0%; headpond +13 cm to 105.59 m (Day 155 above band). Carillon +18.6% (836.64→991.75 m³/s, T18 HQ telemetry). Hull dock T19 41.18 m — trigger INACTIVE **Day 158**. Reservoir balance: **0 falling · 14 steady · 0 rising**. D43 in progress (no Témiscaming row yet). Day **181** since May 2 peak. ORRPB forecast unchanged (next update Nov 3).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 30 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 30 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 30) | **105.936 m** |
| ORRPB daily Oct 30 | 105.94 m (provisional same-day) |
| 24h delta (ORRPB daily Oct 29→30) | **0 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 106 cm below |
| Distance to minor flood (107.50 m) | 156 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T18 UTC Oct 30. Yesterday: T18 UTC Oct 29.*

| Metric | Today (T18 Oct 30) | Yesterday (T18 Oct 29) | Δ |
|---|---|---|---|
| Total release (m³/s) | **295.97** | 357.63 | **−61.66 (−17.2%) ⚠** |
| Turbined (m³/s) | **295.97** | 302.23 | −6.26 (−2.1%) |
| Spilled (m³/s) | **0** | 55.40 | **−55.40 (−100%) ⚠** |
| Spill share (%) | **0%** | 15.5% | **−15.5 pp ⚠** |
| Headpond / amont (m) | **105.59** (T18) | 105.46 | +13 cm |
| Tailwater / aval (m) | **86.76** (T19) | 86.88 | ~−12 cm |
| Δh (head differential, m) | **18.83** | 18.58 | +0.25 |

Spill cutoff to 0% (−100%) and total −17.2% both exceed flag threshold. Headpond 105.59 m is 92 cm above the 104.67 m band ceiling — **Day 155** above band (ongoing status). Headpond rose +13 cm while release fell, consistent with HQ constraining outflow for dispatch optimization. Fifth consecutive day of large Bryson oscillations (Oct 26: surge, Oct 27: partial reversal, Oct 28: surge, Oct 29: partial reversal, Oct 30: full spill cutoff).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18 UTC Oct 30 (3-65 Paugan and 3-3 T19). Yesterday comparison: T18 UTC Oct 29.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **211.30** T18 | 0% | −0.6 (flat) |
| Quinze (3-31) | **207.33** T18 | 0.4% | −1.4 (flat) |
| Îles (3-32) | **210.14** T18 | 0% | −0.7 (flat) |
| Rapide-2 (3-29) | **157.26** T18 | 0% | flat |
| Rapide-7 (3-28) | **158.44** T18 | 0% | flat |
| Bryson (3-46) | **295.97** T18 | 0% | **−61.7 (−17.2%) ⚠** |
| Paugan — Gatineau R. (3-65) | **150.57** T19 | 0% | flat |
| Rapides-Farmers — Gatineau mouth (3-67) | **161.55** T18 | 0% | +14.1 (+9.5%) |
| Carillon — basin terminal (3-60) | **991.75** T18 | 0% | **+155.1 (+18.6%) ⚠** |

Bryson −17.2% and Carillon +18.6% both exceed 5% flag threshold. Rapides-Farmers +9.5% recovers from yesterday's −5.5% anomaly flag — the divergence has normalized. No spill anywhere except trace at Quinze (0.4%).

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 23) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 29 final (m³/s) | **325** *(Oct 30 not yet posted)* | 347 (Oct 23 PSPC) | −22 | **D42 confirmed; D43 in progress** |
| Timiskaming PSPC cross-check Oct 30 T00 | level 178.64 m, **flow −18 m³/s (corrupted artifact)** | — | level +1 cm vs Oct 29 T00 178.63 m | Cross-check unavailable today — negative flow is a corrupted placeholder |
| Quinze release → into the lake (m³/s) | **207.33** (T18) | ~347 (Oct 23) | — | Baseload dispatch |
| Mattawa level (m) | **152.29** (Oct 30 daily) | 152.23 (Oct 23) | +6 cm over 7 d; +1 cm vs Oct 29 | Near-flat; slight recovery from Oct 25 low (152.15 m) |
| Pembroke level (m) | **111.02** (Oct 30 daily) | 111.09 (Oct 23) | −7 cm over 7 d; flat vs Oct 29 | Gentle multi-day decline; flat last 2 days |

PSPC flow for Oct 30 T00 is corrupted (−18 m³/s, impossible value); level 178.64 m (+1 cm from Oct 29 T00 178.63 m) is consistent with continued sub-400 outflow. No cross-check possible today.

**Reservoir balance (T00 Oct 29 → T00 Oct 30):**
0 falling · 14 steady · 0 rising. All reservoirs within ±2 cm day over day — complete basin-wide stability.

**Milestone bookkeeping (W43 anchor Oct 25 + Oct 26–30 extension):**

| Milestone | W43 close (Oct 25) | Oct 26 | Oct 27 | Oct 28 | Oct 29 | **Oct 30** |
|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 176 | 177 | 178 | 179 | 180 | **181** |
| Bryson amont above band (104.67 m) | 150 | 151 | 152 | 153 | 154 | **155** |
| §15.3.5.1 trigger INACTIVE | 153 | 154 | 155 | 156 | 157 | **158** |
| Témiscaming sub-400 | D38 (332) | D39 (347 ✓) | D40 (331 ✓) | D41 (317 ✓) | D42 (325 ✓) | D43? (no row yet) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 30.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.18 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 158** (143 cm below trigger; −9 cm vs yesterday) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 30.*

| Reservoir | Oct 29 (T00) | Oct 30 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.25 m | **219.23 m** | −2 cm | Steady |
| Témiscaming | 178.63 m | **178.64 m** | +1 cm | Steady |
| Dozois | 342.13 m | **342.11 m** | −2 cm | Steady |
| Bark Lake (OPG) | 313.65 m | **313.65 m** | 0 cm | Steady |

All 14 tracked reservoirs within ±2 cm day over day.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-27 3:46 PM EDT** (2026-10-27T19:46:00Z UTC). **Next Update: 2026-11-03 4:00 PM EDT** (2026-11-03T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Oct 29 brief** — no new ORRPB update (next update Nov 3). Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to slightly decrease or remain fairly stable over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false.

---

## Anomaly flags

1. **Bryson dispatch oscillation — Day 5.** Spill cutoff to 0 (from 55.40 m³/s yesterday), total −17.2% (357.63→295.97 m³/s). Headpond rose +13 cm to 105.59 m. Pattern: Oct 26 large spill surge, Oct 27 partial reversal, Oct 28 large surge, Oct 29 large reversal, Oct 30 spill cutoff. Headpond has ranged 105.46–105.59 m across the five days — dam pond is being held up, not rising uncontrolled. Day 155 above band is ongoing status, not a new event.

2. **Carillon +18.6% to 991.75 m³/s** (T18 HQ telemetry). HQ real-time (not ORRPB provisional) — this is an actual dispatch figure. ORRPB Oct 30 provisional running mean is 862 m³/s; HQ telemetry at T18 (6 PM local time) shows 991.75 m³/s, suggesting an afternoon ramp-up. This is the highest Carillon single-hour figure in recent briefs. The daily average (ORRPB provisional 862 m³/s) remains below 1,000; the T18 snapshot crosses it. No regulatory concern (Hull trigger inactive, §15.3.5.1 ceiling not in effect). Worth monitoring tomorrow.

3. **PSPC cross-check corrupted.** Oct 30 T00 Timiskaming `reservoir_readings` reports flow = −18 m³/s (impossible). Not treated as real data; cross-check unavailable today.

4. **Otto Holden Oct 30 ORRPB provisional = 0 m³/s.** Documented placeholder-zero artifact per guardrail. Excluded from all calculations and narratives.

None of the above affects property flood risk. Lac Coulonge etat 0, 106 cm below pre-alert.

---

## Notes

- **Oct 29 retro summary:** Témiscaming 325 m³/s (D42 confirmed; brief had no provisional). Mattawa Oct 29 provisional 152.26 → final 152.28 m (+2 cm; chronic underread confirmed; direction "essentially flat" accurate — actual 0 cm change Oct 28→29).
- **Bryson oscillation pattern (Oct 26–30):** Spill % by day: 0% → 44.8% → 15.5% (partial reversal) → 44.8% → 15.5% (yesterday) → 0% (today). Each large spill day is followed by a cutback. Headpond has held 105.46–105.59 m throughout. This is HQ peak-demand dispatch balancing, not inflow-driven.
- **Carillon 991.75 m³/s at T18:** ORRPB Oct 29 daily final was 892 m³/s; Oct 30 provisional running mean (through T18) is 862 m³/s. The T18 telemetry value exceeds both — consistent with an afternoon peak-demand dispatch ramp. Downstream of the basin, Carillon manages the Ottawa River outflow into Lac des Deux-Montagnes. No flood implications.
- **Mattawa micro-recovery:** After hitting 152.15 m on Oct 25, Mattawa has recovered to 152.29 m over five days (+14 cm). This is a low-amplitude recovery, likely reflecting intermittent rainfall or minor tributary contributions to the upper valley. No significant trend reversal; still well within recession range.
- **D43 status:** No ORRPB Témiscaming row yet for Oct 30 (PSPC cross-check corrupted). Level at T00 Oct 30 = 178.64 m (+1 cm) consistent with sub-400 trend. D43 provisional confirmation will appear in tomorrow's retro.
- **V3 posterior:** Day 58 stale CSV (asof 2026-06-07, exit 0 today — script ran normally, underlying daily CSV not updated; W43 HQ item 1 unresolved). `freshet-forecast.json` written with same stale content (unchanged from HEAD).
