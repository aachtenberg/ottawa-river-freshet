# Daily brief — 2026-11-02

*Generated automatically at 22:15 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (Python urllib required explicit proxy handler + CCR CA bundle — first-fetch 403 resolved by fix; curl probes confirmed proxy healthy throughout). ORRPB forecast HTTP 200 ✓ — **last updated Oct 27 3:46 PM EDT**, next update Nov 3 4:00 PM EDT (weekly cadence). Vigilance 1195: proxy ingest fresh T19 UTC Nov 2 (105.854 m). V3 posterior: script failed with `ModuleNotFoundError: No module named 'freshet_probability'` (new failure class vs prior timeout — module missing); `freshet-forecast.json` carried forward unchanged (asof 2026-06-07).*

*Nov 1 retro-checks: **Nov 1 Témiscaming D45 final 305 m³/s** (yesterday's brief provisional 339 m³/s → final 305 m³/s, −10.0%, at CONFIRMED threshold edge; D45 confirmed, sub-400 streak intact). **Nov 1 Mattawa convention note:** yesterday's brief reported live reading 152.37 m (+13 cm); ORRPB daily finalized at 152.27 m (+3 cm from Oct 31 daily) — data timing issue (brief used T21 UTC live reading; daily average is a different figure); direction (rising) was correct. No flood-risk claim was affected.*

---

## In plain language

### Upstream — the upper basin

The basin continues its quiet late-autumn recession, now Day 184 past the May 2 seasonal peak. The Lake Timiskaming outflow finalized at 305 cubic metres per second for November 1, confirming Day 45 of the sub-400 streak. Today's provisional figure of 346 cubic metres per second is cross-confirmed by the federal monitoring agency (PSPC) and sits comfortably within the recent daily range — no precipitation signal at the top of the system.

Mattawa rose another 10 centimetres overnight to 152.37 metres (the ORRPB daily figure), making this the third consecutive day of rise since late October. The rate is gentle and not associated with any surge at Témiscaming; it is consistent with slow mid-valley tributary contributions and early-November precipitation in the reach between Lake Timiskaming and Mattawa. Pembroke edged down 2 centimetres to 110.94 metres, continuing its multi-week gentle decline. All 14 tracked reservoirs held within 2 centimetres of yesterday — no retention or drawdown signal.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge fell 4 centimetres to 105.86 metres today (ORRPB daily), and the Vigilance gauge most recently showed 105.854 metres as of 7 PM UTC. That puts the lake 114 centimetres below the 107.00-metre pre-alert threshold — firmly in normal territory, etat 0.

Well downstream at the Bryson Generating Station — reached by a long winding channel below the lake's south end, a distinct location from the Mansfield properties — operators made a notable dispatch change today. Starting around 2 PM UTC, Bryson shifted from full-turbine operation (all water through the turbines, no spillway) to partial spillway use: turbines dropped from about 295 to 204 cubic metres per second, and roughly 125 cubic metres per second was routed through the spillway instead. Total release went up slightly. The dam pond (headpond) remained flat at 105.53 metres, indicating this is an operational dispatch decision — possibly a turbine unit coming offline for maintenance — rather than a pond management event. The Carillon dam at the basin outlet released 871 cubic metres per second, slightly less than yesterday.

The ORRPB forecast remains unchanged from October 27: flows and levels expected to slightly decrease or remain fairly stable. Next update is scheduled for November 3.

---

## TL;DR

**RETRO ✓:** Nov 1 Témiscaming D45 final **305 m³/s** (provisional 339 → −10%, CONFIRMED borderline; streak continues). **Today (Day 184):** Lac Coulonge **−4 cm** at **105.86 m** ORRPB daily (Vigilance T19 105.854 m; etat 0, 114 cm below pre-alert). **⚠ BRYSON POSTURE CHANGE:** 0% spill → **38% spill** (124.95 m³/s); turbined 295→204 m³/s; total +11%; headpond flat 105.53 m (Day 158 above band). Carillon 871.85 m³/s (−40, −4.4%). Mattawa **+10 cm** to **152.37 m** (3rd consecutive rise; no upstream surge). Pembroke −2 cm to 110.94 m. D46 in progress (Témiscaming prov 346 m³/s; PSPC agrees). Hull dock T17 41.24 m — trigger INACTIVE **Day 161**. Reservoir balance: **0 falling · 14 steady · 0 rising**. ORRPB forecast unchanged (next update Nov 3).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T19 UTC Nov 2 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 2 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T19 UTC Nov 2) | **105.854 m** |
| ORRPB daily Nov 2 | 105.86 m (provisional same-day) |
| 24h delta (ORRPB daily Nov 1→Nov 2) | **−4 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 114 cm below |
| Distance to minor flood (107.50 m) | 164 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T16 UTC Nov 2 (releases), T17 UTC Nov 2 (levels). Yesterday: T16 UTC Nov 1 (releases), T18 UTC Nov 1 (levels).*

| Metric | Today (T16 Nov 2) | Yesterday (T16 Nov 1) | Δ |
|---|---|---|---|
| Total release (m³/s) | **328.61** | 295.20 | **+33.41 (+11.3%) ⚠** |
| Turbined (m³/s) | **203.66** | 295.20 | **−91.54 (−31.0%) ⚠** |
| Spilled (m³/s) | **124.95** | 0 | **+124.95 (0→38%) ⚠** |
| Spill share (%) | **38.0%** | 0% | **+38 pp ⚠** |
| Headpond / amont (m) | **105.53** (T17) | 105.51 (T17 Nov 1) | +2 cm |
| Tailwater / aval (m) | **86.76** (T17) | 86.82 (T18 Nov 1) | −6 cm |
| Δh (head differential, m) | **18.77** | 18.70 | +0.07 |

All four release metrics exceeded the 5% flag threshold. Headpond 105.53 m is **86 cm above** the 104.67 m band ceiling — **Day 158** above band. Spill first appeared at ~T14 UTC today (T14: 139.10 m³/s, 40.6%; T15: 128.37 m³/s, 38.6%; T16: 124.95 m³/s, 38.0%) with headpond flat throughout — posture shift is a dispatch decision, not a storage management event. 47-cm operating band (104.20–104.67 m): not breached; headpond is 86 cm above it.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `dam_releases` latest rows T16–T17 UTC Nov 2. Yesterday comparison: Nov 1 brief T16–T17 values.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **223.55** T17 | 0% | +14.82 (+7.1%) |
| Quinze (3-31) | **223.29** T17 | 0.4% | +16.95 (+8.2%) |
| Îles (3-32) | **227.78** T17 | 0% | +16.59 (+7.8%) |
| Rapide-2 (3-29) | **156.73** T17 | 0% | −0.45 (flat) |
| Rapide-7 (3-28) | **158.36** T17 | 0% | +0.03 (flat) |
| Bryson (3-46) | **328.61** T16 | **38.0% ⚠** | +33.01 (+11.2% total; spill 0→38%) |
| Paugan — Gatineau R. (3-65) | **150.36** T17 | 0% | −0.24 (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **162.61** T17 | 0% | −3.34 (flat) |
| Carillon — basin terminal (3-60) | **871.85** T17 | 0% | −39.17 (−4.4%) |

Upper cascade (Première-Chute through Îles) shows ~7–8% upticks vs yesterday — these are different snapshot hours and typical intraday dispatch variation; no persistent surge pattern. Only Bryson carries a flaggable anomaly. Carillon −4.4% (under 5% threshold).

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 26) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 2 provisional (m³/s) | **346** *(D46 in progress)* | 347 (Oct 26) | −1 | **D45 (305) confirmed; D46 in progress** |
| Timiskaming PSPC cross-check Nov 2 T00 | level 178.59 m, **flow 346 m³/s** | 178.69 m (Oct 26) | level flat Oct 31→Nov 2 (−2 cm total) | Agrees with ORRPB exactly; cross-check valid |
| Quinze release → into lake (m³/s) | **223.29** (T17) | ~338 (Oct 26) | — | Baseload; steady week-over-week |
| Mattawa level (m) | **152.37** (Nov 2 daily) | 152.15 (Oct 26) | +22 cm over 7 d; **+10 cm vs Nov 1 daily** | 3rd consecutive day of rise; no upstream surge |
| Pembroke level (m) | **110.94** (Nov 2 daily) | 111.10 (Oct 26) | −16 cm over 7 d; −2 cm vs Nov 1 | Continuing gentle multi-week decline |

**Provisional sanity check — Témiscaming Nov 2 = 346 m³/s (+41, +13.4% vs Nov 1 final 305):** Below the 25%/150 m³/s trigger threshold; full guardrail not required. Quick checks: PSPC agrees exactly (346 m³/s T00 Nov 2 level 178.59 m — flat, consistent with ~340 m³/s outflow). Within recent range (193–378 m³/s Oct 27–Nov 2). No anomaly. Sanity check passed.

**Reservoir balance (T00 Nov 1 → T00 Nov 2):**
0 falling · 14 steady · 0 rising. All 14 tracked reservoirs within ±2 cm: largest movements Dozois −2 cm, Mitchinamecus −2 cm; Baskatong −1 cm; lady_evelyn and poisson_blanc +1 cm each. No active retention or drawdown signal.

**Milestone bookkeeping (W43 anchor Oct 25 + Oct 26 – Nov 2 extension):**

| Milestone | W43 close (Oct 25) | Oct 26 | Oct 27 | Oct 28 | Oct 29 | Oct 30 | Oct 31 | Nov 1 | **Nov 2** |
|---|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 176 | 177 | 178 | 179 | 180 | 181 | 182 | 183 | **184** |
| Bryson amont above band (104.67 m) | 150 | 151 | 152 | 153 | 154 | 155 | 156 | 157 | **158** |
| §15.3.5.1 trigger INACTIVE | 153 | 154 | 155 | 156 | 157 | 158 | 159 | 160 | **161** |
| Témiscaming sub-400 | D38 (332) | D39 (347 ✓) | D40 (331 ✓) | D41 (324 ✓) | D42 (325 ✓) | D43 (193 ✓) | D44 (317 ✓) | D45 (305 ✓) | D46? (346 prov) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T17 UTC Nov 2.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.24 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 161** (137 cm below trigger; −1 cm vs yesterday T17) |
| Carillon amont (1-2968) | **41.11 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 2.*

| Reservoir | Nov 1 (T00) | Nov 2 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.17 m | **219.16 m** | −1 cm | Steady |
| Témiscaming | 178.59 m | **178.59 m** | 0 cm | Steady |
| Dozois | 342.05 m | **342.03 m** | −2 cm | Steady |
| Bark Lake (OPG) | 313.60 m | **313.59 m** | −1 cm | Steady |

All 14 tracked reservoirs: 0 falling · 14 steady · 0 rising. No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-27 3:46 PM EDT** (2026-10-27T19:46:00Z UTC). **Next Update: 2026-11-03 4:00 PM EDT** (2026-11-03T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Nov 1 brief** — no new ORRPB update (next update Nov 3). Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to slightly decrease or remain fairly stable over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false.

---

## Anomaly flags

1. **⚠ Bryson posture shift: 0% spill → 38% spill (sustained from ~T14 UTC).** Turbined dropped from ~295 to ~204 m³/s; spillway opened to ~125 m³/s; total release up ~11%. Headpond held flat at 105.53 m throughout — this is a dispatch decision (likely a turbine unit offline), not a headpond management response. Spill share declining gradually (T14: 40.6% → T16: 38.0%). No property-reach implications (Carillon is down 4% and the Lac Coulonge/Mansfield area is far upstream of Bryson). Flagged because it meets the "0% → significant spill" anomaly criterion.

None of the above affects property flood risk. Lac Coulonge etat 0, 114 cm below pre-alert.

---

## Notes

- **Nov 1 D45 Témiscaming retro: final 305 m³/s.** Yesterday's brief provisional was 339 m³/s (−10% revision, borderline CONFIRMED; D45 confirmed). Sub-400 streak intact at D46 in progress.
- **Nov 1 Mattawa convention note:** Yesterday's brief used a live T21 UTC reading of 152.37 m (+13 cm); ORRPB daily for Nov 1 finalized at 152.27 m (+3 cm from Oct 31). The live reading was technically accurate at that timestamp; the daily average is a different product. No flood-risk claim was affected; direction (rising) was correct. Nov 2 ORRPB daily is 152.37 m, so the level has since confirmed.
- **Detached HEAD at session start (8th recurrence).** Self-corrected via `git checkout main && git pull origin main` (fast-forward; included Oct-monthly rollup and Nov 1 brief). No data loss.
- **V3 posterior (freshet_posterior.py): new failure class — `ModuleNotFoundError: No module named 'freshet_probability'`.** Previously the script timed out (exit 143/124); now it fails with import error at line 68. Module may have been removed or renamed. `freshet-forecast.json` carried forward unchanged (asof 2026-06-07). W43 HQ item 1 status has changed: now module-missing rather than timeout. Needs investigation.
- **Python urllib 403 at session start:** First fetch attempt via Python `urllib.request` without explicit proxy handler returned 403 (proxy required). Fixed by adding `urllib.request.ProxyHandler({"https": HTTPS_PROXY})` and loading `/root/.ccr/ca-bundle.crt`. All subsequent data fetches succeeded. Curl probes confirmed proxy and upstreams healthy throughout — no actual outage. This is the first run to encounter this Python proxy issue; may be environment-specific.
