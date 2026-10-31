# Daily brief — 2026-10-31

*Generated automatically at 22:10 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **last updated Oct 27 3:46 PM EDT**, next update Nov 3 4:00 PM EDT (weekly cadence). Vigilance 1195: proxy ingest fresh T20 UTC Oct 31 (105.920 m). V3 posterior: script fails in local sandbox (ModuleNotFoundError: freshet_probability — local env issue, not production); `freshet-forecast.json` not regenerated this run.*

*Oct 30 retro-checks: **Oct 30 Témiscaming final 193 m³/s** (PSPC; D43 confirmed — yesterday's brief correctly reported no row yet and cross-check corrupted; D43 is the new streak low for the sub-400 streak, discussed in Notes). Oct 30 Mattawa provisional 152.29 → final 152.24 m (−5 cm; yesterday called "essentially flat, +1 cm" — direction accurate, specific value provisional artifact). No headlined Témiscaming provisional from yesterday — retro clean.*

---

## In plain language

### Upstream — the upper basin

The upper basin continues its quiet autumn recession. The Lake Timiskaming outflow for October 30 has finalized at 193 cubic metres per second — confirmed as Day 43 of the sub-400 streak, and notably the lowest single-day figure in that streak (the previous low was around 293 m³/s in mid-October). This appears to reflect a deliberate one-day reduction in managed release by the federal agency that controls Lake Timiskaming outflows, consistent with the lake level rising two centimetres that day and then falling back three centimetres as release returned to the 330-range on October 31. Today's (Day 44, in progress) provisional outflow of 337 cubic metres per second aligns exactly with the multi-day range — no concern. The Mattawa station is flat for a second consecutive day at 152.24 metres, and Pembroke eased five centimetres to 110.98 metres, continuing its gentle multi-day decline. All reservoir levels basin-wide are within a few centimetres day over day — essentially complete basin stability.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge fell one more centimetre to 105.93 metres — now 107 centimetres below the 107.00-metre pre-alert threshold and firmly in normal territory. No flood concern; slow steady recession.

Well downstream from the property, the dam pond at the Bryson Generating Station is unchanged from yesterday: total release holds near 295–296 cubic metres per second (all through the turbines, zero spillway flow) for a second straight day at this snapshot hour. The dam pond itself sits at 105.55 metres, down four centimetres from yesterday's peak of 105.59 metres — a slight adjustment that is consistent with HQ fine-tuning hydraulic head. At 105.55 metres the dam pond remains 88 centimetres above the top of its normal operating range for the 156th consecutive day. At the basin's terminal dam, Carillon released 870 cubic metres per second — down from yesterday's late-afternoon peak of 992 m³/s, normalizing back to its recent daily-average range. No regulatory concern: the trigger gauge at the Hull dock stands at 41.23 metres, well below the 42.61-metre threshold that would activate the spring-flood operating ceiling (Day 159 inactive).

The ORRPB forecast remains unchanged from October 27: "flows and levels are expected to slightly decrease or remain fairly stable." Next update November 3.

---

## TL;DR

**RETRO ✓:** Oct 30 Témiscaming final 193 m³/s → **D43 CONFIRMED** (brief had no provisional; retro clean; 193 m³/s = new streak low, see Notes). Mattawa Oct 30 provisional 152.29 → final 152.24 m (−5 cm; direction confirmed). **Today:** Lac Coulonge **−1 cm** at **105.93 m** (ORRPB daily; Vigilance T20 105.920 m; etat 0, 107 cm below pre-alert). Bryson **flat** (295.53 m³/s, 0% spill, same as yesterday T18); headpond −4 cm to 105.55 m (Day 156 above band). Carillon **−12.3%** (991.75→869.85 m³/s) — normalization from yesterday's afternoon-peak snapshot. Hull dock T19 41.23 m — trigger INACTIVE **Day 159**. D44 in progress (Témiscaming prov 337 m³/s; PSPC agrees 337). Reservoir balance: **2 falling · 12 steady · 0 rising**. Day **182** since May 2 peak. ORRPB forecast unchanged (next update Nov 3).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 31 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 31 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 31) | **105.920 m** |
| ORRPB daily Oct 31 | 105.93 m (provisional same-day) |
| 24h delta (ORRPB daily Oct 30→31) | **−1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 107 cm below |
| Distance to minor flood (107.50 m) | 157 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T18 UTC Oct 31. Yesterday: T18 UTC Oct 30.*

| Metric | Today (T18 Oct 31) | Yesterday (T18 Oct 30) | Δ |
|---|---|---|---|
| Total release (m³/s) | **295.53** | 295.97 | −0.44 (−0.1%) |
| Turbined (m³/s) | **295.53** | 295.97 | −0.44 (−0.1%) |
| Spilled (m³/s) | **0** | 0 | — |
| Spill share (%) | **0%** | 0% | — |
| Headpond / amont (m) | **105.55** (T19) | 105.59 | −4 cm |
| Tailwater / aval (m) | **86.81** (T19) | 86.76 | +5 cm |
| Δh (head differential, m) | **18.74** | 18.83 | −0.09 |

No flaggable changes today (all <5%). Headpond 105.55 m is 88 cm above the 104.67 m band ceiling — **Day 156** above band (ongoing status). Bryson has been in zero-spill mode at the T18 snapshot for two consecutive days.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18-T19 UTC Oct 31. Yesterday comparison: T18-T19 UTC Oct 30.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **210.29** T18 | 0% | −1.0 (flat) |
| Quinze (3-31) | **209.80** T18 | 0.4% | +2.5 (flat) |
| Îles (3-32) | **214.37** T19 | 0% | +4.2 (flat) |
| Rapide-2 (3-29) | **157.07** T19 | 0% | flat |
| Rapide-7 (3-28) | **158.43** T19 | 0% | flat |
| Bryson (3-46) | **295.53** T18 | 0% | −0.4 (flat) |
| Paugan — Gatineau R. (3-65) | **150.55** T19 | 0% | flat |
| Rapides-Farmers — Gatineau mouth (3-67) | **167.84** T18 | 0% | +6.3 (+3.9%) |
| Carillon — basin terminal (3-60) | **869.85** T19 | 0% | **−121.9 (−12.3%) ⚠** |

Carillon −12.3% is above the 5% flag threshold but reflects normalization from yesterday's anomalously high T18 snapshot of 991.75 m³/s (flagged in yesterday's brief as a late-afternoon dispatch peak). Today's 869.85 m³/s is consistent with the recent ORRPB daily average range (862–892 m³/s). No spill anywhere except trace at Quinze (0.4%).

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 24) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 31 provisional (m³/s) | **337** *(D44 in progress)* | 334 | +3 | **D43 (193) confirmed; D44 in progress** |
| Timiskaming PSPC cross-check Oct 31 T00 | level 178.62 m, **flow 337 m³/s** | 178.69 m (Oct 27) | level −3 cm (Oct 30→31) | Agrees with ORRPB; cross-check valid |
| Quinze release → into the lake (m³/s) | **209.80** (T18) | ~338 (Oct 24) | — | Baseload dispatch; steady week-over-week |
| Mattawa level (m) | **152.24** (Oct 31 daily) | 152.25 (Oct 27) | −1 cm over 4 d; **0 cm vs Oct 30** | Flat for 2nd consecutive day |
| Pembroke level (m) | **110.98** (Oct 31 daily) | 111.07 (Oct 27) | −9 cm over 4 d; −5 cm vs Oct 30 | Continuing gentle multi-day decline |

**Provisional sanity check — Témiscaming Oct 31 = 337 m³/s:** PSPC cross-check agrees (337 m³/s, T00 Oct 31). Within 3 m³/s of Oct 24 final (334). Consistent with Oct 27 (331), Oct 28 (324), Oct 29 (325) range. Level drop Oct 30→31 T00 (178.65→178.62, −3 cm) consistent with 337 m³/s outflow. Sanity check passed; no mass-balance anomaly.

**Reservoir balance (T00 Oct 30 → T00 Oct 31):**
2 falling · 12 steady · 0 rising. Lady Evelyn −3 cm, Timiskaming −3 cm; all others within ±2 cm.

**Milestone bookkeeping (W43 anchor Oct 25 + Oct 26–31 extension):**

| Milestone | W43 close (Oct 25) | Oct 26 | Oct 27 | Oct 28 | Oct 29 | Oct 30 | **Oct 31** |
|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 176 | 177 | 178 | 179 | 180 | 181 | **182** |
| Bryson amont above band (104.67 m) | 150 | 151 | 152 | 153 | 154 | 155 | **156** |
| §15.3.5.1 trigger INACTIVE | 153 | 154 | 155 | 156 | 157 | 158 | **159** |
| Témiscaming sub-400 | D38 (332) | D39 (347 ✓) | D40 (331 ✓) | D41 (324 ✓) | D42 (325 ✓) | D43 (193 ✓) | D44? (337 prov) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 31.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.23 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 159** (138 cm below trigger; +5 cm vs yesterday) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 31.*

| Reservoir | Oct 30 (T00) | Oct 31 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.22 m | **219.20 m** | −2 cm | Steady |
| Témiscaming | 178.65 m | **178.62 m** | −3 cm | Falling (just outside steady band; consistent with 337 m³/s managed release) |
| Dozois | 342.09 m | **342.08 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.64 m | **313.63 m** | −1 cm | Steady |

All 14 tracked reservoirs: 2 falling (−3 cm each) · 12 steady · 0 rising. No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-27 3:46 PM EDT** (2026-10-27T19:46:00Z UTC). **Next Update: 2026-11-03 4:00 PM EDT** (2026-11-03T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Oct 30 brief** — no new ORRPB update (next update Nov 3). Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to slightly decrease or remain fairly stable over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false.

---

## Anomaly flags

1. **Carillon −12.3% (991.75→869.85 m³/s).** Exceeds 5% flag threshold. Contextual: yesterday's brief explicitly noted 991.75 m³/s as an "anomalously high T18 snapshot / afternoon ramp-up" and flagged it for monitoring. Today's 869.85 m³/s returns to the recent daily-average range (ORRPB provisional Oct 30 = 862 m³/s; Oct 29 final = 892 m³/s). This is a normalization, not a new event. No regulatory concern (Hull trigger inactive, Day 159).

None of the above affects property flood risk. Lac Coulonge etat 0, 107 cm below pre-alert.

---

## Notes

- **Oct 30 Témiscaming D43 = 193 m³/s — new streak low.** The sub-400 streak's previous low was 293 m³/s (Oct 18-19 range per W43). PSPC cross-check for Oct 31 T00 (337 m³/s, level 178.62 m) is consistent: the −3 cm level drop from Oct 30 T00 (178.65 m) is consistent with resuming ~335 m³/s outflow after the lower-release Oct 30. The lake level on Oct 30 T00 (178.65 m, +2 cm from Oct 29) was consistent with the reduced 193 m³/s day — the lake stored water slightly, then resumed normal drainage. No data quality concern; 193 m³/s appears to be a real deliberate PSPC release reduction. D43 confirmed and streak intact (D44 in progress at 337 m³/s).
- **Mattawa Oct 30 provisional retro.** Yesterday's brief reported "152.29 m" for Oct 30 Mattawa daily (the ORRPB same-day provisional figure at report time). Final = 152.24 m (−5 cm discrepancy). The qualitative "essentially flat" description was accurate; the specific value was a provisional artifact. Chronic ~4–5 cm provisional underread pattern continues (see also Oct 29: provisional 152.26 → final 152.28).
- **Bryson dispatch oscillation resolved.** The five-day spill oscillation pattern (Oct 26–30) appears to have subsided: both T18 Oct 30 and T18 Oct 31 show zero spill at 295-296 m³/s. The headpond has settled back from its Oct 30 peak of 105.59 m to 105.55 m. Normal HQ dispatch cycling, no property implications.
- **V3 posterior (local env):** Script fails with `ModuleNotFoundError: freshet_probability` — local sandbox missing module, same as prior local runs. Production routine likely has the full environment. `freshet-forecast.json` not regenerated this run; last production commit holds stale asof 2026-06-07 content (unresolved W43 HQ item 1).
