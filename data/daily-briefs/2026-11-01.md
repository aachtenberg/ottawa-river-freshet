# Daily brief — 2026-11-01

*Generated automatically at 22:03 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **last updated Oct 27 3:46 PM EDT**, next update Nov 3 4:00 PM EDT (weekly cadence). Vigilance 1195: proxy ingest fresh T20 UTC Nov 1 (105.893 m). V3 posterior: script completed (exit code 0); output identical to prior run (asof 2026-06-07 — input CSV not yet updated); `freshet-forecast.json` regenerated (same content).*

*Nov 1 retro-checks: **Oct 31 Témiscaming D44 final 317 m³/s** (yesterday's brief provisional 337 m³/s → final 317 m³/s, −6%, within CONFIRMED threshold; D44 confirmed). Oct 31 Mattawa 152.24 m — provisional matched final exactly. No headlined property or Bryson figures requiring retro — clean.*

---

## In plain language

### Upstream — the upper basin

The basin continues in steady late-autumn recession. The Lake Timiskaming outflow finalized at 317 cubic metres per second for October 31, confirming Day 44 of the sub-400 streak. Today's provisional reading of 339 cubic metres per second is confirmed by the federal agency's (PSPC) own cross-check gauge, and aligns with the recent daily range (193–347 m³/s) — no precipitation signal visible at the top of the system.

The Mattawa gauge, about 100 kilometres downstream of Lake Timiskaming, rose 13 centimetres today to 152.37 metres — the first notable rise after four days of essentially flat readings. Since Témiscaming outflow isn't surging, this is likely a small tributary or runoff contribution from early-November precipitation somewhere between Timiskaming and Mattawa. Normal for the season. Pembroke continued its gentle multi-week decline (down 6 cm to 110.93 m). All basin reservoirs held within a few centimetres of yesterday — 2 falling slightly, 12 steady, none rising.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge fell 2 centimetres to 105.90 metres — now 110 centimetres below the 107.00-metre pre-alert threshold. Etat 0; no flood concern, slow steady recession continues.

Well downstream of the property, the dam pond at the Bryson Generating Station (reached by a long winding channel below the lake's south end — a distinct gauge from the property) held essentially flat at 105.51 metres, 3 centimetres below yesterday's reading and 84 centimetres above the top of its normal operating range for the 157th consecutive day. All 296 cubic metres per second passing through the turbines; spillway remains at zero. Carillon at the basin outlet released 911 cubic metres per second, a 41 m³/s uptick from yesterday's snapshot — intraday dispatch variation, just under the 5% reporting threshold. The Hull dock gauge at 41.25 metres is 136 centimetres below the threshold that activates the spring-flood operating ceiling (Day 160 inactive).

The ORRPB forecast remains unchanged from October 27: flows and levels expected to slightly decrease or remain fairly stable. Next update November 3.

---

## TL;DR

**RETRO ✓:** Oct 31 Témiscaming D44 final **317 m³/s** (provisional 337 → −6%, CONFIRMED; streak continues). **Today (Day 183):** Lac Coulonge **−2 cm** at **105.90 m** (Vigilance T20 105.893 m; etat 0, 110 cm below pre-alert). Bryson flat (295.6 m³/s, 0% spill); headpond **−3 cm** to **105.51 m** (Day 157 above band). Mattawa **+13 cm** to **152.37 m** — first rise after 4 flat days; no upstream surge, likely tributary runoff. Hull dock T17 41.25 m — trigger INACTIVE **Day 160**. D45 in progress (Témiscaming prov 339 m³/s; PSPC agrees 339). Reservoir balance: **2 falling · 12 steady · 0 rising**. ORRPB forecast unchanged (next update Nov 3).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Nov 1 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 1 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Nov 1) | **105.893 m** |
| ORRPB daily Nov 1 | 105.90 m (provisional same-day) |
| 24h delta (ORRPB daily Oct 31→Nov 1) | **−2 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 110 cm below |
| Distance to minor flood (107.50 m) | 160 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T17 UTC Nov 1. Yesterday: T17 UTC Oct 31.*

| Metric | Today (T17 Nov 1) | Yesterday (T17 Oct 31) | Δ |
|---|---|---|---|
| Total release (m³/s) | **295.60** | 295.98 | −0.38 (−0.1%) |
| Turbined (m³/s) | **295.60** | 295.98 | −0.38 (−0.1%) |
| Spilled (m³/s) | **0** | 0 | — |
| Spill share (%) | **0%** | 0% | — |
| Headpond / amont (m) | **105.51** (T17) | 105.54 | −3 cm |
| Tailwater / aval (m) | **86.82** (T17) | 86.80 | +2 cm |
| Δh (head differential, m) | **18.69** | 18.74 | −0.05 |

No flaggable changes (all <5%). Headpond 105.51 m is 84 cm above the 104.67 m band ceiling — **Day 157** above band. Zero spill for 3rd consecutive day at this snapshot hour.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T16–T17 UTC Nov 1. Yesterday comparison: T18–T19 UTC Oct 31.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **208.73** T17 | 0% | −1.6 (flat) |
| Quinze (3-31) | **206.34** T16 | 0.4% | −3.5 (flat) |
| Îles (3-32) | **211.19** T16 | 0% | −3.2 (flat) |
| Rapide-2 (3-29) | **157.18** T16 | 0% | +0.1 (flat) |
| Rapide-7 (3-28) | **158.33** T17 | 0% | −0.1 (flat) |
| Bryson (3-46) | **295.60** T17 | 0% | +0.1 (flat) |
| Paugan — Gatineau R. (3-65) | **150.60** T16 | 0% | +0.1 (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **165.95** T16 | 0% | −1.9 (flat) |
| Carillon — basin terminal (3-60) | **911.02** T16 | 0% | **+41.2 (+4.7%)** |

Carillon +4.7% — just below the 5% flag threshold. Different snapshot hours (T16 vs T19 yesterday) and normal intraday dispatch variation; consistent with ORRPB recent daily-average range. No spill anywhere except trace at Quinze (0.4%).

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 25) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 1 provisional (m³/s) | **339** *(D45 in progress)* | 333 | +6 | **D44 (317) confirmed; D45 in progress** |
| Timiskaming PSPC cross-check Nov 1 T00 | level 178.60 m, **flow 339 m³/s** | 178.69 m (Oct 27) | level −1 cm (Oct 31→Nov 1) | Agrees with ORRPB exactly; cross-check valid |
| Quinze release → into the lake (m³/s) | **206.34** (T16) | ~338 (Oct 25) | — | Baseload dispatch; flat week-over-week |
| Mattawa level (m) | **152.37** (Nov 1 daily) | 152.15 (Oct 25) | +22 cm over 7 d; **+13 cm vs Oct 31** | First notable rise after 4 flat days |
| Pembroke level (m) | **110.93** (Nov 1 daily) | 111.10 (Oct 25) | −17 cm over 7 d; −6 cm vs Oct 31 | Continuing gentle multi-week decline |

**Provisional sanity check — Témiscaming Nov 1 = 339 m³/s:** PSPC cross-check agrees exactly (339 m³/s, T00 Nov 1). Level drop Oct 31→Nov 1 T00 (178.61→178.60, −1 cm) consistent with ~340 m³/s outflow. Within recent range (317–347 m³/s, Oct 27–Nov 1). No mass-balance anomaly. Sanity check passed.

**Reservoir balance (T00 Oct 31 → T00 Nov 1):**
2 falling · 12 steady · 0 rising. Baskatong −3 cm, Dozois −3 cm; all others within ±2 cm (Témiscaming −1 cm, Bark Lake −1 cm, others flat).

**Milestone bookkeeping (W43 anchor Oct 25 + Oct 26 – Nov 1 extension):**

| Milestone | W43 close (Oct 25) | Oct 26 | Oct 27 | Oct 28 | Oct 29 | Oct 30 | Oct 31 | **Nov 1** |
|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 176 | 177 | 178 | 179 | 180 | 181 | 182 | **183** |
| Bryson amont above band (104.67 m) | 150 | 151 | 152 | 153 | 154 | 155 | 156 | **157** |
| §15.3.5.1 trigger INACTIVE | 153 | 154 | 155 | 156 | 157 | 158 | 159 | **160** |
| Témiscaming sub-400 | D38 (332) | D39 (347 ✓) | D40 (331 ✓) | D41 (324 ✓) | D42 (325 ✓) | D43 (193 ✓) | D44 (317 ✓) | D45? (339 prov) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T17 UTC Nov 1.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.25 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 160** (136 cm below trigger; +2 cm vs yesterday T19) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 1.*

| Reservoir | Oct 31 (T00) | Nov 1 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.20 m | **219.17 m** | −3 cm | Falling |
| Témiscaming | 178.61 m | **178.60 m** | −1 cm | Steady |
| Dozois | 342.08 m | **342.05 m** | −3 cm | Falling |
| Bark Lake (OPG) | 313.62 m | **313.61 m** | −1 cm | Steady |

All 14 tracked reservoirs: 2 falling (−3 cm each) · 12 steady · 0 rising. No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-27 3:46 PM EDT** (2026-10-27T19:46:00Z UTC). **Next Update: 2026-11-03 4:00 PM EDT** (2026-11-03T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Oct 31 brief** — no new ORRPB update (next update Nov 3). Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to slightly decrease or remain fairly stable over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false.

---

## Anomaly flags

1. **Mattawa +13 cm (152.24→152.37 m) — first rise after 4 flat days.** No upstream surge visible (Témiscaming 317 m³/s Oct 31 final; 339 m³/s Nov 1 provisional — within normal range). Consistent with small tributary or early-November precipitation contribution in the Mattawa reach. Normal early-autumn seasonal fluctuation; no property implications.

None of the above affects property flood risk. Lac Coulonge etat 0, 110 cm below pre-alert.

---

## Notes

- **Oct 31 D44 Témiscaming retro: final 317 m³/s.** Yesterday's brief provisional was 337 m³/s (−6% revision, CONFIRMED threshold). D44 confirmed; sub-400 streak intact. D45 in progress at 339 m³/s.
- **Detached HEAD at session start (7th recurrence).** Self-corrected via `git checkout main && git pull origin main` (fast-forward to include Oct 31 brief that had been committed in detached HEAD). No data loss. W43 HQ item 2 (recurring git session state issue) continues unresolved; frequency holding at ~1/week.
- **V3 posterior (freshet_posterior.py):** Script completed (exit code 0) this run — no timeout. Output asof "2026-06-07" unchanged (input CSV `lac-coulonge-daily-1990-2026.csv` not updated since Jun 7; all posteriors = 1.0; W43 HQ item 1 unresolved). `freshet-forecast.json` content unchanged but regenerated and committed.
