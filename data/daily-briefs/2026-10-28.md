# Daily brief — 2026-10-28

*Generated automatically at 22:10 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **last updated Oct 27 3:46 PM EDT**, next update Nov 3 4:00 PM EDT (no update expected today). Vigilance 1195: proxy ingest fresh T20 UTC Oct 28 (105.966 m). V3 posterior: exit 143 (Day 56 consecutive timeout); `freshet-forecast.json` not updated — keeping last-valid output.*

*Oct 27 retro-checks: **Oct 27 Témiscaming final 331 m³/s** (PSPC cross-check in yesterday's brief was 367 m³/s; revised −36 m³/s; direction sub-400 consistent — **D40 CONFIRMED**). Oct 27 Mattawa provisional 152.40 m → final 152.25 m (−15 cm; chronic underread confirmed; direction rising was correct).*

---

## In plain language

### Upstream — the upper basin

The upper basin continues its late-autumn recession without interruption. October 27's daily outflow from Lake Timiskaming finalized at 331 cubic metres per second — the 40th consecutive day below 400 m³/s, extending a streak that began September 18. The preliminary midnight reading for October 28 is 337 m³/s, keeping Day 41 on track. The Mattawa level posted 152.20 metres as a provisional value for October 28, essentially flat versus the finalized 152.25 metres for October 27 (subject to the usual chronic downward revision). Pembroke edged down five centimetres to 111.02 metres, consistent with a gentle mid-valley outflow trend. The reservoir balance across the basin is 4 falling and 10 steady — Baskatong, Des Joachims, Mitchinamecus, and Timiskaming all shed one to five centimetres. Normal late-autumn drawdown; no storage-retention signal.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge edged down two centimetres to 105.98 metres, remaining solidly in the normal range — about 102 centimetres below the 107.00-metre pre-alert threshold. No concern.

Well downstream from the property, the dam pond at the Bryson Generating Station saw a large operational shift today: spill volume jumped from about 52 cubic metres per second yesterday to 171 cubic metres per second today (measured at 7 PM Eastern), while water through the turbines fell from about 296 to 211 cubic metres per second. Total water released from the dam rose roughly 10 percent to 382 m³/s. Despite this swing, the dam pond level itself stayed flat at 105.53 metres — unchanged from yesterday — so HQ appears to have increased both inflow handling and spill share simultaneously, a normal form of dispatch optimization. This operational change has no upstream effect on Lac Coulonge or the Mansfield properties, which are a winding distance upstream of the dam. The dam pond has now been above the top of its normally permitted operating range for 153 consecutive days.

The ORRPB forecast, last updated October 27, calls for flows and levels to "slightly decrease or remain fairly stable" over the coming week. No new update is expected until November 3. No precipitation event or flood watch is mentioned.

---

## TL;DR

**RETRO ✓:** Oct 27 Témiscaming final 331 m³/s (cross-check had been 367; −36 revision, sub-400 consistent) → **D40 CONFIRMED**. Mattawa Oct 27 provisional 152.40 → final 152.25 (−15 cm; chronic underread; direction correct). **Today:** Lac Coulonge **−2 cm** to **105.98 m** (Vigilance T20: 105.966 m; etat 0, 102 cm below pre-alert). Bryson spill **+231.7%** (51.56→171.02 m³/s), turbines −28.7% (296.04→211.15), total +9.9% (347.60→382.16); spill share 14.8%→44.8%; headpond flat at 105.53 m (Day 153 above band). Carillon −10.9% (943.33→840.32 m³/s). Hull dock T19 41.30 m — trigger INACTIVE **Day 156**. Reservoir balance: 4 falling (timiskaming −5 cm, baskatong/des_joachims/mitchinamecus −2 cm) · 10 steady · 0 rising. D41 in progress (PSPC Oct 28 T00: 337 m³/s). Day **179** since May 2 peak. ORRPB forecast unchanged (next update Nov 3).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 28 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 28 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 28) | **105.966 m** |
| ORRPB daily Oct 28 | 105.98 m (provisional same-day) |
| 24h delta (ORRPB daily Oct 27→28) | **−2 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 102 cm below |
| Distance to minor flood (107.50 m) | 152 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 28. Yesterday: T19 UTC Oct 27 (from Oct 27 brief).*

| Metric | Today (T19 Oct 28) | Yesterday (T19 Oct 27) | Δ |
|---|---|---|---|
| Total release (m³/s) | **382.16** | 347.60 | **+34.56 (+9.9%) ⚠** |
| Turbined (m³/s) | **211.15** | 296.04 | **−84.89 (−28.7%) ⚠** |
| Spilled (m³/s) | **171.02** | 51.56 | **+119.46 (+231.7%) ⚠** |
| Spill share (%) | **44.8%** | 14.8% | **+30 pp ⚠** |
| Headpond / amont (m) | **105.53** | 105.54 | −1 cm (flat) |
| Tailwater / aval (m) | **86.95** | 86.94 | +1 cm (flat) |
| Δh (head differential, m) | **18.58** | 18.59 | −1 cm |

All three change thresholds exceeded (total +9.9%, turbined −28.7%, spill +231.7%). Headpond 105.53 m is 86 cm above the 104.67 m band ceiling — **Day 153** above band (ongoing status). No breach of the lower band limit (104.20 m). Spill share shift (+30 pp) is large; dam pond flat throughout, consistent with dispatch optimization rather than uncontrolled head rise.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T19 UTC Oct 28 (T18 for sites with T18 as latest). Yesterday comparison: T19 UTC Oct 27.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **209.80** T19 | 0% | +0.5 (+0.2%) |
| Quinze (3-31) | **208.58** T19 | 0.4% | −0.9 (flat) |
| Îles (3-32) | **214.41** T18 | 0% | **+13.9 (+6.9%) ⚠** |
| Rapide-2 (3-29) | **157.23** T18 | 0% | −0.3 (flat) |
| Rapide-7 (3-28) | **157.87** T18 | 0% | +0.0 (flat) |
| Bryson (3-46) | **382.16** T19 | 44.8% | **+34.6 (+9.9%) ⚠** |
| Paugan — Gatineau R. (3-65) | **155.05** T18 | 0% | +6.7 (+4.5%) |
| Rapides-Farmers — Gatineau mouth (3-67) | **156.27** T18 | 0% | +0.6 (flat) |
| Carillon — basin terminal (3-60) | **840.32** T19 | 0% | **−103.0 (−10.9%) ⚠** |

Bryson spill share at 44.8% is anomalous (was near-zero before Oct 26 and has been cycling large). Îles +6.9% and Carillon −10.9% both exceed the 5% flag threshold. No zero-to-high spill transitions elsewhere. Carillon's −10.9% drop (103 m³/s) is the largest single-day change in the cascade today.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 21) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 27 final (m³/s) | **331** *(Oct 28 not yet posted)* | 336 (Oct 21) | −5 | **D40 confirmed; D41 in progress** |
| Timiskaming PSPC cross-check Oct 28 T00 | **337 m³/s**, level 178.64 m | — | +6 vs Oct 27 final | sub-400 ✓; level −5 cm vs Oct 27 T00 |
| Quinze release → into the lake (m³/s) | **208.58** (T19) | ~336 (Oct 21) | — | Baseload dispatch |
| Mattawa level (m) | **152.20** *(provisional — chronic underread caution)* | n/a | −5 cm vs Oct 27 final (152.25) | Slightly down; magnitude unreliable |
| Pembroke level (m) | **111.02** (Oct 28 daily) | n/a | −5 cm vs Oct 27 (111.07) | Gently declining |

PSPC Oct 28 T00 (337 m³/s) vs ORRPB Oct 27 final (331 m³/s): +6 m³/s difference — within 50 m³/s → no flag.

**Reservoir balance (T00 Oct 27 → T00 Oct 28):**
4 falling · 10 steady · 0 rising. timiskaming −5 cm; baskatong −2 cm; des_joachims −2 cm; mitchinamecus −2 cm (minor late-autumn drawdown, no retention signal).

**Milestone bookkeeping (W43 anchor Oct 25 + Oct 26–28 extension):**

| Milestone | W43 close (Oct 25) | Oct 26 | Oct 27 | **Oct 28** |
|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 176 | 177 | 178 | **179** |
| Bryson amont above band (104.67 m) | 150 | 151 | 152 | **153** |
| §15.3.5.1 trigger INACTIVE | 153 | 154 | 155 | **156** |
| Témiscaming sub-400 | D38 (333) | D39 (347 ✓) | D40 (331 ✓) | D41? (PSPC 337 sub-400) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 28.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.30 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 156** (131 cm below trigger; +4 cm vs yesterday) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 28.*

| Reservoir | Oct 27 (T00) | Oct 28 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.31 m | **219.29 m** | −2 cm | Falling |
| Témiscaming | 178.69 m | **178.64 m** | −5 cm | Falling |
| Dozois | 342.19 m | **342.18 m** | −1 cm | Steady |
| Bark Lake (OPG) | 313.68 m | **313.67 m** | −1 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-27 3:46 PM EDT** (2026-10-27T19:46:00Z UTC). **Next Update: 2026-11-03 4:00 PM EDT** (2026-11-03T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Oct 27 brief** — no new ORRPB update today (next update Nov 3). Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to slightly decrease or remain fairly stable over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false.

---

## Anomaly flags

1. **Bryson spill +231.7%** (51.56→171.02 m³/s, T19 Oct 28 vs T19 Oct 27). Turbines −28.7% (296.04→211.15 m³/s). Total +9.9% (347.60→382.16). Spill share 14.8%→44.8%. Headpond flat at 105.53 m — dam pond level stable despite surge, consistent with dispatch optimization. HQ real-time telemetry, not a provisional artifact. Second large Bryson spill event in three days (Oct 26 +90.9%, Oct 27 −26.5%, Oct 28 +231.7%).

2. **Carillon −10.9%** (943.33→840.32 m³/s, T19 Oct 28 vs T19 Oct 27). Largest cascade movement today (103 m³/s). No concurrent spill change (0% throughout). Terminal dam operational adjustment; travel time from Bryson to Carillon is days, so these moves are not directly linked.

3. **Îles (3-32) +6.9%** (200.50→214.41 m³/s). Dispatch cycling in upper cascade. No spill change (0% throughout).

None of the above affects property flood risk. Lac Coulonge etat 0, 102 cm below pre-alert.

---

## Notes

- **Oct 27 retro summary:** Témiscaming 331 m³/s (D40 confirmed; PSPC cross-check had been 367, revision −36 within normal range). Mattawa Oct 27 provisional 152.40 → final 152.25 m (−15 cm; chronic underread confirmed; direction correctly identified).
- **Bryson spill cycling:** Three-day pattern: Oct 26 +90.9% surge, Oct 27 −26.5% partial reversal, Oct 28 +231.7% new surge. Headpond held 105.53–105.54 m throughout — the amplitude of these spill swings is large but the dam pond is stable, indicating HQ dispatch optimization rather than a structural inflow event. Note for context: Oct 23–25 Bryson was running ~11% spill; this cycling appears to have started Oct 26.
- **Carillon 840 m³/s:** Lowest Carillon release since records in this window. Compare: Oct 27 was 943, Oct 26 was 901 (from Oct 26 brief). Today's 840 m³/s is a further step down. Basin-outflow context: Carillon averaging sub-900 is consistent with the Témiscaming sub-400 upstream and overall late-autumn recession.
- **V3 posterior:** Day 56 consecutive timeout (exit 143). `freshet-forecast.json` unchanged — last-valid output retained (asof 2026-06-07).
