# Daily brief — 2026-10-18

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (78 b probe). ORRPB conditions + forecast HTTP 200 ✓ (128 KB; forecast unchanged since Oct 13 21:02 UTC — next update Oct 20). Vigilance 1195 ingest stale: latest proxy record T13 UTC Oct 13 (~129h before brief runtime; upstream unverifiable from sandbox — egress-blocked); ORRPB daily Oct 18 = 105.95 m used as primary. V3 posterior: timed out (exit 143, Day 45 consecutive); `freshet-forecast.json` restored from git HEAD unchanged (asof 2026-06-07).*

*Oct 17 retro-checks: Mid-valley exclusions ✓ — Des Joachims Oct 17 final = **336 m³/s** (provisional 275 excluded ✓; reasonable), Otto Holden Oct 17 final = **323 m³/s** (provisional 255 excluded ✓; reasonable). Témiscaming Oct 17 = **307 m³/s** — D30 confirmed ✓ (yesterday "D30 in progress"). Oct 16 OPG revisions: Des Joachims revised 409 → **479 m³/s** (+70); Otto Holden revised 334 → **381 m³/s** (+47) — Oct 17 brief floor check failure for Otto Holden (floor 339, posted "final" 334) now resolved; revised final 381 m³/s is above floor ✓. Témiscaming Oct 16 ORRPB revised 334 → **318 m³/s** (−16 m³/s; D29 unaffected, still sub-400).*

---

## In plain language

### Upstream — the upper basin

The upper basin continues its quiet late-season recession. Lake Timiskaming's daily outflow for October 17 finalized at 307 cubic metres per second — now Day 30 in the streak of sub-400 flow that began September 18. October 18 is still accumulating but the PSPC snapshot at midnight showed 300 m³/s, consistent with the ongoing trend. The Mattawa level gauge slipped another 3 centimetres to 152.26 metres, and Pembroke fell 4 centimetres to 111.00 metres — both continuing their slow decline from the slight mid-October uptick.

All 14 tracked reservoirs moved less than 2 centimetres day-over-day — a broadly stable snapshot. No active retention signal; normal late-season posture.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge dipped 1 centimetre to 105.95 metres — still fully normal and 105 centimetres below the 107.00-metre pre-alert level. Nothing of concern here.

At the Bryson Generating Station — the dam well downstream of Lac Coulonge, reached after the lake's south end narrows into a winding reach — releases continued to ease. Total flow dropped about 6 percent to 344 cubic metres per second, with most of the reduction coming from a slight cut in turbine output. The dam pond held essentially steady at 105.55 metres, unchanged from yesterday. At the basin's terminal dam, Carillon continued its gentle step-down to 1,134 cubic metres per second, and the Hull dock gauge (the regulatory trigger gauge at Gatineau) nudged up 7 centimetres to 41.30 metres — still 131 centimetres below the level at which Carillon's spring-flood operating ceiling would apply.

---

## TL;DR

Retro ✓: Oct 17 mid-valley finals Des Joachims 336/Otto Holden 323 (exclusions correct ✓); Oct 16 OPG revisions Des Joachims 409→479, Otto Holden 334→381 (floor check failure resolved ✓); Témiscaming Oct 17 D30 = 307 ✓; Oct 16 ORRPB revised 334→318 (D29 unaffected). **Today:** Lac Coulonge −1 cm to **105.95 m (etat 0; 105 cm below pre-alert)**. Bryson total −6.1% to 344 m³/s; turbined −8.8% to 128 m³/s (flags threshold; settling posture). Carillon −1.2% to 1,134 m³/s; Hull dock +7 cm to 41.30 m (trigger inactive D146). Témiscaming D30 = 307 confirmed; D31 in progress (PSPC T00 ≈ 300 m³/s). ORRPB forecast unchanged. Day **169** since May 2 peak. Mid-valley provisionals (Des Joachims 253, Otto Holden 220) excluded from headlines — sanity check not cleared; see Notes.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 18 daily (primary; Vigilance ingest stale at T13 UTC Oct 13 — ~129h before brief runtime; upstream unverifiable from sandbox).*

| Metric | Value |
|---|---|
| Current level (ORRPB daily Oct 18) | **105.95 m** |
| ORRPB daily Oct 17 | 105.96 m |
| 24h delta (ORRPB daily Oct 17→18) | **−1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 105 cm below |
| Distance to minor flood (107.50 m) | 155 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 18. Yesterday: T19 UTC Oct 17. ⚠ Total −6.1%, turbined −8.8% (both exceed >5% flag threshold).*

| Metric | Today (T19 Oct 18) | Yesterday (T19 Oct 17) | Δ |
|---|---|---|---|
| Total release (m³/s) | **343.77** | 366.31 | **−22.54 (−6.1%) ⚠** |
| Turbined (m³/s) | **128.14** | 140.46 | **−12.32 (−8.8%) ⚠** |
| Spilled (m³/s) | **215.63** | 225.85 | −10.22 (−4.5%) |
| Spill share (%) | **62.7%** | 61.6% | +1.1 pp |
| Headpond / amont (m) | **105.55** | 105.54 | +1 cm |
| Tailwater / aval (m) | **86.94** | 87.01 | −7 cm |
| Δh (head differential, m) | **18.61** | 18.53 | +8 cm |

**Headpond band status:** 105.55 m is 88 cm above the 104.67 m band ceiling — **Day 143** above band.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 18.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 226.28 | 0% |
| Quinze (3-31) | 203.35 | 0.5% |
| Îles (3-32) | 212.11 | 0% |
| Rapide-2 (3-29) | 156.79 | 0% |
| Rapide-7 (3-28) | 155.69 | 0% |
| Bryson (3-46) | **343.77** | **62.7%** |
| Paugan — Gatineau R. (3-65) | 162.61 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 183.82 | 0% |
| Carillon — basin terminal (3-60) | **1,134.43** | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 11) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 17 ORRPB final (m³/s) | **307** | 308 (Oct 11 ORRPB) | −1 | **D30 sub-400 confirmed** |
| Témiscaming Oct 18 PSPC T00 (m³/s) | **300** | — | — | D31 in progress |
| PSPC cross-check vs ORRPB | Oct 17: 307 PSPC / 307 ORRPB | — | — | Agree ✓ |
| Quinze release → into the lake (m³/s) | **203.35** (T19) | ~202 | — | Autumn dispatch; steady |
| Mattawa level (m) | **152.26** (Oct 18 daily) | 152.21 (Oct 11) | +5 cm since Oct 11 | −3 cm from Oct 17 (152.29); direction slightly down |
| Pembroke level (m) | **111.00** (Oct 18 daily) | 110.98 (Oct 11) | +2 cm since Oct 11 | −4 cm from Oct 17 (111.04); direction slightly down |

**Reservoir balance (T00 Oct 17 → T00 Oct 18):** All 14 tracked reservoirs within ±2 cm: Baskatong −2 cm · Mitchinamecus −2 cm · Timiskaming −2 cm · Cabonga −1 cm · Kiamika −1 cm · Des Joachims 0 · Dozois 0 · Bark Lake 0 · Kipawa 0 · Lady Evelyn 0 · Quinze +1 cm · Timiskaming-Haileybury +1 cm · Poisson Blanc +2 cm · Rapide-7 +2 cm. **0 falling · 14 steady · 0 rising.** Flattest reservoir day of the post-freshet record; normal low-volatility autumn pattern.

**Milestone bookkeeping (W41 anchor Oct 11 + Oct 12–18 extension):**

| Milestone | W41 close (Oct 11) | Oct 12 | Oct 13 | Oct 14 | Oct 15 | Oct 16 | Oct 17 | **Oct 18** |
|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 162 | 163 | 164 | 165 | 166 | 167 | 168 | **169** |
| Bryson amont above band (104.67 m) | 136 | 137 | 138 | 139 | 140 | 141 | 142 | **143** |
| §15.3.5.1 trigger INACTIVE | 139 | 140 | 141 | 142 | 143 | 144 | 145 | **146** |
| Temiscaming sub-400 | D24 (308) | D25 (304) | D26 (309) | D27 (306) | D28 (302 rev.) | D29 (318 rev.) | **D30 (307)** | D31 in progress |

*Oct 16 Témiscaming ORRPB revised 334 → 318 since Oct 17 brief (D29 sub-400 unaffected). Oct 15 revised 308 → 302 (W41 note). Both sub-400.*

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 18.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.30 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 146** (131 cm below trigger; +7 cm from Oct 17) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull dock +7 cm today; still far below servitude threshold.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 18.*

| Reservoir | Oct 17 (T00) | Oct 18 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.52 m | **219.50 m** | −2 cm | Steady (within ±2 cm band) |
| Témiscaming | 178.77 m | **178.75 m** | −2 cm | Steady; Oct 17 outflow confirmed 307 m³/s |
| Dozois | 342.44 m | **342.44 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.79 m | **313.79 m** | 0 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓, 128 KB. **Last Update: 2026-10-13 5:02 PM EDT** (2026-10-13T21:02:00Z UTC). **Next Update: 2026-10-20 4:00 PM EDT** (2026-10-20T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: true (precipitation language present). Mode: `weekly-notice`.

---

## Anomaly flags

1. **⚠ Bryson total −6.1%, turbined −8.8%.** Total 366→344 m³/s, turbined 140→128 m³/s — both exceed >5% flag threshold. Post-reversal settling (Day 2 after yesterday's turbine-recovery posture change). Spill share nearly unchanged (61.6→62.7%). Headpond stable at 105.55 m.

2. **Mid-valley provisionals excluded (data quality).** Oct 18 partial-day provisional daily means: Des Joachims 253 m³/s (−24.7% vs Oct 17 final 336), Otto Holden 220 m³/s (−31.9% vs Oct 17 final 323). Otto Holden exceeds 25% threshold. Per sanity check guardrail: check 4 (downstream response) inconclusive — Chenaux Oct 18 = 443 (vs Oct 17 final 506, −12.4%; less decline than upstream provisional implies). Excluded from headlines. Finals expected Oct 19. See Notes.

None further.

---

## Notes

- **Vigilance ingest staleness:** Latest proxy record for station 1195 is T13 UTC Oct 13 (~129h before brief runtime). ORRPB daily Oct 18 (105.95 m) used as primary. Upstream reachability unverifiable (egress-blocked sandbox). Not an upstream outage claim.
- **Mid-valley provisional check:** Des Joachims Oct 18 partial-day mean 253 m³/s (19:00 UTC, ~15h into day); feasibility floor (15/24)×253 = 158 m³/s. Not infeasible on its own. Otto Holden 220 m³/s. Downstream Chenaux 443 m³/s (−12% from Oct 17 final 506), Chats Falls 539 m³/s (−4% from 560). The 12% Chenaux decline is inconsistent with a 25-32% mid-valley decline (check 4 does not clearly pass). Keeping out of headlines; finals Oct 19.
- **Oct 16 OPG revisions:** Des Joachims Oct 16 revised 409 → 479 m³/s (+70), Otto Holden revised 334 → 381 m³/s (+47). This is part of the documented OPG 2–3 day revision cycle. Oct 17 brief's floor check failure for Otto Holden (floor 339 > posted "final" 334) is now resolved: revised final 381 > floor 339 ✓.
- **Témiscaming Oct 16 revision:** ORRPB flows revised 334 → 318 m³/s (−16 m³/s). D29 sub-400 status unaffected. Milestone table updated.
- **V3 posterior:** Day 45 consecutive timeout (exit 143). `freshet-forecast.json` restored from git HEAD (asof 2026-06-07, season_resolved=false, unchanged). Dashboard continues to serve the Jun 7 posterior.
- **ORRPB flows Oct 1–18 (Témiscaming):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=306, Oct 7=315, Oct 8=296, Oct 9=311, Oct 10=286, Oct 11=308, Oct 12=304, Oct 13=309, Oct 14=306, Oct 15=302 (revised), Oct 16=318 (revised), Oct 17=307. Oct 18 not yet posted (PSPC T00 ≈300).
