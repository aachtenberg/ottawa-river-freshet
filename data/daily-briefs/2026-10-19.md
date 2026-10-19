# Daily brief — 2026-10-19

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (112 b probe; curl used — Python urllib returns 403 for table queries, likely Accept-header mismatch; curl with `-H 'Accept: application/json'` returns 200 ✓). ORRPB conditions + forecast HTTP 200 ✓ (128 KB; forecast unchanged since Oct 13 21:02 UTC — next update Oct 20). Vigilance 1195: INGEST RESTORED — latest proxy record T20 UTC Oct 19 (fresh; was stale at T13 Oct 13 ~129h in Oct 18 brief). V3 posterior: timed out (exit 124, Day 46 consecutive); `freshet-forecast.json` restored from git HEAD unchanged (asof 2026-06-07).*

*Oct 18 retro-checks: Mid-valley exclusions confirmed ✓ — Des Joachims Oct 18 final = **374 m³/s** (provisional 253 excluded ✓); Otto Holden Oct 18 final = **328 m³/s** (provisional 220 excluded ✓). Oct 16 OPG data today reads Des Joachims = **409**, Otto Holden = **334** — back to pre-revision values (yesterday's brief noted revisions to 479/381; appear rolled back; weekly rollup to reconcile). Témiscaming Oct 18 = **295 m³/s** — D31 sub-400 confirmed ✓.*

---

## In plain language

### Upstream — the upper basin

The upper basin is quiet. Lake Timiskaming's outflow finalized at 295 cubic metres per second for October 18 — the thirty-first consecutive day below 400 m³/s, a streak that started September 18. The midnight reading for October 19 came in at 270 m³/s, pointing toward a thirty-second day. That is 170 days past the May 2 freshet peak, and the river is simply running at its normal late-autumn low.

Mattawa fell 6 centimetres to 152.26 metres and Pembroke edged up 1 centimetre to 111.02 metres — both fluctuating within the small range they have held since mid-October. Fourteen tracked reservoirs moved less than 3 centimetres overnight; most are steady, consistent with routine autumn dispatch.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge held flat at 105.95 metres — unchanged from yesterday, 105 centimetres below the 107.00-metre pre-alert level, and fully normal for the season.

One operational note: the Vigilance water-level gauge on the lake (the data feed our cluster reads to stay current) came back online after roughly six days of silence — readings are fresh again as of this afternoon. The data value is the same as what ORRPB has been reporting through the gap.

At the Bryson Generating Station — downstream of Lac Coulonge at the end of the lake's winding southern reach — total releases edged up 2.6 percent to 353 cubic metres per second, a small day-to-day adjustment well within normal variation. The dam pond (headpond) was essentially unchanged at 105.56 metres. Carillon, the basin's terminal dam near Hawkesbury, ran at 1,159 cubic metres per second at the latest hourly read — up slightly, all through turbines with no spillway use.

The ORRPB forecast remains unchanged from its October 13 update and calls for gradual or stable levels given forecast precipitation. The next scheduled update is tomorrow.

---

## TL;DR

Retro ✓: Oct 18 mid-valley finals Des Joachims 374/Otto Holden 328 (exclusions correct ✓); Oct 16 OPG revisions (noted yesterday as DJ 479/OH 381) appear rolled back to 409/334 — weekly rollup to reconcile. Témiscaming Oct 18 D31 = 295 ✓. **Today:** Lac Coulonge **0 cm** to **105.95 m (etat 0; 105 cm below pre-alert)** — flat. Bryson +2.6% to 353 m³/s; headpond +1 cm to 105.56 m (Day 144 above band). Carillon +2.2% to 1,159 m³/s (T19); Hull dock −4 cm to 41.26 m (trigger inactive Day 147). Témiscaming D31 = 295 confirmed; D32 in progress (PSPC T00 = 270). Vigilance ingest restored (T20 Oct 19). Day **170** since May 2 peak. Mid-valley Oct 19 provisionals (Des Joachims 578, Otto Holden 490) excluded — downstream check failed; data tables only.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: Vigilance 1195 via proxy `river_readings` T20 UTC Oct 19 (PRIMARY — ingest restored); ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 19 daily (cross-check; agree).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 19) | **105.95 m** |
| ORRPB daily Oct 18 | 105.95 m |
| 24h delta (Oct 18 → Oct 19 ORRPB daily) | **0 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 105 cm below |
| Distance to minor flood (107.50 m) | 155 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 19. Yesterday: T19 UTC Oct 18.*

| Metric | Today (T19 Oct 19) | Yesterday (T19 Oct 18) | Δ |
|---|---|---|---|
| Total release (m³/s) | **352.80** | 343.77 | +9.03 (+2.6%) |
| Turbined (m³/s) | **127.97** | 128.14 | −0.17 (−0.1%) |
| Spilled (m³/s) | **224.82** | 215.63 | +9.19 (+4.3%) |
| Spill share (%) | **63.7%** | 62.7% | +1.0 pp |
| Headpond / amont (m) | **105.56** | 105.55 | +1 cm |
| Tailwater / aval (m) | **86.94** | 86.94 | 0 |
| Δh (head differential, m) | **18.62** | 18.61 | +1 cm |

No parameter exceeds the >5% flag threshold. **Headpond band status:** 105.56 m is 89 cm above the 104.67 m band ceiling — **Day 144** above band.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T19 UTC Oct 19.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 204.06 | 0% |
| Quinze (3-31) | 200.02 | 0.5% |
| Îles (3-32) | 209.55 | 0% |
| Rapide-2 (3-29) | 156.86 | 0% |
| Rapide-7 (3-28) | 156.60 | 0% |
| Bryson (3-46) | **352.80** | **63.7%** |
| Paugan — Gatineau R. (3-65) | 162.57 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 171.03 | 0% |
| Carillon — basin terminal (3-60) | **1,159.07** | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 12) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 18 ORRPB final (m³/s) | **295** | 304 (Oct 12) | −9 | **D31 sub-400 confirmed** |
| Témiscaming Oct 19 PSPC T00 (m³/s) | **270** | — | — | D32 in progress |
| PSPC cross-check vs ORRPB | Oct 18: 295 PSPC / 295 ORRPB | — | — | Agree ✓ |
| Quinze release → into the lake (m³/s) | **200.02** (T19) | ~204 (Oct 12) | — | Autumn dispatch; steady |
| Mattawa level (m) | **152.26** (Oct 19 daily) | 152.12 (Oct 12) | +14 cm since Oct 12 | −6 cm from Oct 18 (152.32); direction slightly down |
| Pembroke level (m) | **111.02** (Oct 19 daily) | 110.99 (Oct 12) | +3 cm since Oct 12 | +1 cm from Oct 18 (111.01); direction flat |

**Reservoir balance (T00 Oct 18 → T00 Oct 19):**
Dozois −3 cm · Des Joachims −3 cm · Mitchinamecus −2 cm = 3 **falling** · Rapide-7 +1 · Quinze +1 · Bark Lake +1 · Lady Evelyn −1 · Kipawa −1 · Timiskaming-Haileybury +1 · Cabonga 0 · Baskatong −1 · Kiamika −1 = 9 **steady** · Timiskaming +2 cm · Poisson Blanc +2 cm = 2 **rising**. **3 falling · 9 steady · 2 rising.** Normal low-volatility autumn pattern.

**Milestone bookkeeping (W41 anchor Oct 11 + Oct 12–19 extension):**

| Milestone | W41 close (Oct 11) | Oct 12 | Oct 13 | Oct 14 | Oct 15 | Oct 16 | Oct 17 | Oct 18 | **Oct 19** |
|---|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 162 | 163 | 164 | 165 | 166 | 167 | 168 | 169 | **170** |
| Bryson amont above band (104.67 m) | 136 | 137 | 138 | 139 | 140 | 141 | 142 | 143 | **144** |
| §15.3.5.1 trigger INACTIVE | 139 | 140 | 141 | 142 | 143 | 144 | 145 | 146 | **147** |
| Temiscaming sub-400 | D24 (308) | D25 (304) | D26 (309) | D27 (306) | D28 (302 rev.) | D29 (318 rev.) | D30 (307) | **D31 (295)** | D32 in progress |

*Oct 16 Témiscaming ORRPB shows 334 today (yesterday's brief noted 318 revised; current DB shows 334 — weekly rollup to reconcile). All values remain sub-400.*

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 19.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.26 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 147** (135 cm below trigger; −4 cm from Oct 18) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull dock fell 4 cm from Oct 18 T19.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 19.*

| Reservoir | Oct 18 (T00) | Oct 19 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.49 m | **219.48 m** | −1 cm | Steady |
| Témiscaming | 178.73 m | **178.75 m** | +2 cm | Steady; Oct 18 outflow confirmed 295 m³/s |
| Dozois | 342.43 m | **342.40 m** | −3 cm | Falling (within normal range) |
| Bark Lake (OPG) | 313.80 m | **313.81 m** | +1 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓, 128 KB. **Last Update: 2026-10-13 5:02 PM EDT** (2026-10-13T21:02:00Z UTC). **Next Update: 2026-10-20 4:00 PM EDT** (2026-10-20T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: true (precipitation language present). Mode: `weekly-notice`.

---

## Anomaly flags

1. **Mid-valley Oct 19 provisionals excluded (data quality).** Des Joachims Oct 19 partial-day provisional mean = 578 m³/s (+54% vs Oct 18 final 374); Otto Holden = 490 m³/s (+49% vs Oct 18 final 328). Both exceed 25%/150 m³/s thresholds. Sanity checks: (1) feasibility floor at ~22h = (22/24)×578 = 530 m³/s — above Oct 18 final by 156; (2) upstream Témiscaming Oct 18 = 295, Quinze = 200 — no obvious contributing surge; (3) Des Joachims pool T00 = 152.13 vs 152.16 yesterday (−3 cm), inconsistent with a sustained 204 m³/s outflow increase; (4) downstream Chenaux = 523 (+26 vs Oct 18), Chats Falls = 562 (+6 vs Oct 18) — much smaller changes than a 204 m³/s upstream surge would produce. **Check 4 fails.** Excluded from TL;DR, plain language, and anomaly flags. Reported in data tables only as "provisional — failed sanity check, see Notes."

2. **Vigilance ingest restored.** Station 1195 proxy records now show T19 and T20 UTC Oct 19 (value = 105.951 m). Was stale at T13 UTC Oct 13 (~129h before Oct 18 brief). Not an upstream outage claim; ingest pipeline issue resolved.

None further.

---

## Notes

- **Mid-valley provisional check (Oct 19):** Des Joachims provisional 578 m³/s, Otto Holden 490 m³/s — similar failure pattern to the Aug 5 event documented in the routine guardrail. Finals expected Oct 20. ORRPB daily row for Oct 19 also shows these provisional values (Des Joachims 578, Otto Holden 490) alongside Chenaux 523 and Chats Falls 562. The downstream stations' much smaller increases are the decisive check failure.
- **Oct 18 retro confirmation:** Oct 18 finals (DJ 374, OH 328) confirmed the Oct 18 provisional exclusion (253/220) was correct. No correction required.
- **Oct 16 OPG data inconsistency:** Current DB shows Oct 16 Des Joachims = 409, Otto Holden = 334. Yesterday's brief (written T22 Oct 18) noted these as revised to 479/381. The revisions appear rolled back as of today. Weekly rollup (Monday Oct 20) will reconcile.
- **Oct 16 Témiscaming flow:** Current DB shows 334 m³/s; yesterday's brief noted ORRPB revised Oct 16 = 318 m³/s. Today DB shows 334. Same reconciliation needed at rollup. Sub-400 status unaffected in either case.
- **V3 posterior:** Day 46 consecutive timeout (exit 124, 60-second limit). `freshet-forecast.json` restored from git HEAD (asof 2026-06-07, season_resolved=false, unchanged). Dashboard continues to serve the Jun 7 posterior.
- **Carillon afternoon ramp:** Hourly Carillon releases: T17=1,044 → T18=1,099 → T19=1,159 m³/s — a 115 m³/s ramp over the late afternoon. Within normal HQ dispatch variation; all turbined, 0% spill.
- **Vigilance ingest:** Confirmed fresh. Value 105.951 m matches ORRPB daily 105.95 m for Oct 19.
- **ORRPB flows Oct 1–19 (Témiscaming):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=306, Oct 7=315, Oct 8=296, Oct 9=311, Oct 10=286, Oct 11=308, Oct 12=304, Oct 13=309, Oct 14=306, Oct 15=308, Oct 16=334 (DB; revision status unclear), Oct 17=307, Oct 18=295. Oct 19 not yet finalized (PSPC T00 = 270).
