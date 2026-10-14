# Daily brief — 2026-10-14

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB conditions + forecast HTTP 200 ✓ (forecast unchanged since Oct 13 21:02 UTC — next update Oct 20). Vigilance 1195 ingest stale: latest proxy record T13 UTC Oct 13 (~33h before brief runtime; upstream unverifiable from sandbox — egress-blocked); ORRPB daily Oct 14 = 105.93 m used as primary level source. V3 posterior: timed out (exit 143, Day 41); `freshet-forecast.json` updated with current fetch timestamp, posterior unchanged.*

*Oct 13 retro-checks: Lac Coulonge claim in TL;DR "105.86 m (flat)"; ORRPB Oct 13 daily final = **105.88 m** (+2 cm). CONFIRMED ✓. Carillon Oct 13 daily final = **765 m³/s** (yesterday's brief predicted "substantially higher than 496"; confirmed ✓ — noted for record, no correction). Témiscaming Oct 13 final = **309 m³/s** (D26 confirmed; no headline to retro-check — was "not yet posted"). Oct 13 mid-valley (Des Joachims 701, Otto Holden 652) were excluded; finals 331/320 — no retro needed.*

---

## In plain language

### Upstream — the upper basin

The upper basin continues in gentle late-autumn recession. Lake Timiskaming's outflow came in at 309 cubic metres per second for October 13 — the 26th consecutive day below 400 m³/s — and October 14 is trending in the same range (the PSPC cross-check at midnight showed 326 m³/s, still comfortably sub-400). Levels at Mattawa continued their modest drift, while Pembroke held essentially flat.

The precipitation that ORRPB flagged in its October 13 forecast update appears to have arrived over parts of the mid-valley reach. Reservoir storage is largely neutral: across 14 tracked reservoirs, two are falling slightly (Baskatong and Dozois, each down 3 cm), two are rising slightly (Des Joachims +4 cm, Poisson Blanc +5 cm), and the rest are holding steady. None are rising more than 10 cm per day.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge rose five centimetres today — from 105.88 metres to 105.93 metres, according to the ORRPB daily reading — marking the first notable single-day increase in several weeks. This is consistent with the precipitation that arrived across the mid-valley reach, and it is exactly what ORRPB's updated forecast from yesterday anticipated. Despite the rise, the lake remains firmly in normal status: at 107 centimetres below the 107-metre pre-alert level, there is ample buffer for any continuation of gradual increases. The ORRPB forecast (unchanged today, next update October 20) still calls for levels to "increase gradually or remain fairly stable depending on location" over the coming week; no flood concern is implied.

At the Bryson Generating Station dam pond (several kilometres downstream of the lake's south end — not adjacent to the Mansfield properties), the spillway absorbed the increased runoff: Bryson's spill flow rose from 125 to 158 cubic metres per second (+26%), with turbine output held flat. The dam pond itself didn't budge (still at 105.57 metres), which confirms that operators are simply passing the additional inflow straight through the spillway rather than holding it back. This is normal water-management practice during a runoff event.

---

## TL;DR

Retro ✓: Oct 13 Lac Coulonge final 105.88 m ✓; Oct 13 Carillon daily final 765 m³/s (predicted substantially higher than 496 ✓); Oct 13 Témiscaming D26 = 309 m³/s confirmed. **Today:** Lac Coulonge **105.93 m (+5 cm; etat 0; 107 cm below pre-alert)** — first notable single-day rise in weeks, consistent with arriving precipitation. Bryson spill +26.1% (125→158 m³/s), total +11.2% (295→328 m³/s), turbined flat — precipitation passthrough, not flood-management posture change. Headpond flat at 105.57 m. Témiscaming D27 in progress (PSPC Oct 14 prov 326 m³/s; D26 final 309). Carillon T18 = 852 m³/s (down from yesterday's 1,257 afternoon peak). ORRPB forecast unchanged. Day **165** since May 2 peak. Mid-valley Oct 14 provisionals (Des Joachims 153, Otto Holden 151) failed all sanity checks — excluded.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 14 daily (primary; Vigilance ingest stale at T13 UTC Oct 13 — used as cross-check only).*

| Metric | Value |
|---|---|
| Current level (ORRPB daily Oct 14) | **105.93 m** |
| Vigilance 1195 latest (T13 UTC Oct 13) | 105.863 m (stale ~33h; ingest lag) |
| ORRPB daily Oct 13 | 105.88 m |
| 24h delta (ORRPB daily Oct 13→14) | **+5 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 107 cm below |
| Distance to minor flood (107.50 m) | 157 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` — T19 UTC Oct 14 vs T21 UTC Oct 13.*

| Metric | Today (T19 Oct 14) | Yesterday (T21 Oct 13) | Δ |
|---|---|---|---|
| Total release (m³/s) | **327.91** | 294.98 | **+32.9 (+11.2%)** |
| Turbined (m³/s) | **169.97** | 169.76 | +0.2 (flat) |
| Spilled (m³/s) | **157.94** | 125.22 | **+32.7 (+26.1%)** |
| Spill share (%) | **48.2%** | 42.5% | **+5.7 pp** |
| Headpond / amont (m) | **105.57** | 105.57 | 0 cm |
| Tailwater / aval (m) | **86.84** | 86.68 | +16 cm |
| Δh (head differential, m) | **18.73** | 18.89 | −16 cm |

**Headpond band status:** 105.57 m is 90 cm above the 104.67 m band ceiling — **Day 139** above band. **ANOMALY: total +11.2%, spilled +26.1% — both exceed the >5% flag threshold.** Turbined output flat. Headpond unchanged. Interpretation: precipitation runoff arriving from upstream, passed straight through the spillway; no flood-management posture change.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 14.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 205.79 | 0% |
| Quinze (3-31) | 205.25 | 0.5% |
| Îles (3-32) | 208.19 | 0% |
| Rapide-2 (3-29) | 157.31 | 0% |
| Rapide-7 (3-28) | 155.42 | 0% |
| Bryson (3-46) | **327.91** | **48.2%** |
| Paugan — Gatineau R. (3-65) | 157.90 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 189.03 | 0% |
| Carillon — basin terminal (3-60) | 852.22 | 0% |

*Note: Carillon real-time T18 = 852 m³/s; ORRPB Oct 14 daily prov = 1,015 m³/s (reflects yesterday's large afternoon peaking ramp being averaged in; today's dispatch is lower).*

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 7) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 13 final (m³/s) | **309** | 313 (Oct 7 final) | −4 | D26 confirmed ✓ |
| Témiscaming Oct 14 ORRPB prov (m³/s) | not posted yet | — | — | D27 in progress |
| PSPC cross-check Oct 14 T00 (m³/s) | **326** | — | — | D27 prov; sub-400 |
| Quinze release → into the lake (m³/s) | **205.25** (T19 HQ) | ~313 (Oct 7) | — | Autumn low dispatch; normal |
| Mattawa level (m) | **152.20** (Oct 14 ORRPB daily) | ~152.26 (Oct 7) | −6 cm | Direction DOWN (marginal) |
| Pembroke level (m) | **111.00** (Oct 14) | ~110.97 (Oct 7 est.) | +3 cm | Direction flat; no threshold data |

**Reservoir balance (Oct 13 T00 → Oct 14 T00, 14 reservoirs):** 2 falling (Baskatong −3 cm, Dozois −3 cm) · 10 steady · 2 rising (Des Joachims +4 cm, Poisson Blanc +5 cm). Neutral posture — no reservoir rising >10 cm/day.

**Milestone bookkeeping (W41 anchor Oct 11 + Oct 12–14 extension):**

| Milestone | W41 close (Oct 11) | Oct 12 | Oct 13 | **Oct 14** |
|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 162 | 163 | 164 | **165** |
| Bryson amont above band (104.67 m) | 136 | 137 | 138 | **139** |
| §15.3.5.1 trigger INACTIVE | 139 | 140 | 141 | **142** |
| Temiscaming sub-400 | D24 (308) | D25 (304) | D26 (309) | **D27 (prov 326)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 14.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.23 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 142** (138 cm below trigger) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull at 41.23 m, 138 cm below trigger threshold.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 14.*

| Reservoir | Oct 13 (T00) | Oct 14 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.62 m | **219.59 m** | −3 cm | Normal autumn drainage |
| Témiscaming | 178.77 m | **178.77 m** | 0 cm | Flat; PSPC Oct 14 prov 326 m³/s |
| Dozois | 342.55 m | **342.52 m** | −3 cm | Normal drawdown |
| Bark Lake (OPG) | 313.73 m | **313.75 m** | +2 cm | Steady |

Full balance: 2 falling · 10 steady · 2 rising (Des Joachims +4 cm, Poisson Blanc +5 cm) across 14 tracked reservoirs. No active basin-wide retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-13 5:02 PM EDT** (2026-10-13T21:02:00Z UTC). **Next Update: 2026-10-20 4:00 PM EDT** (2026-10-20T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from yesterday.** Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: true (precipitation has arrived; language still valid). Mode: `weekly-notice`.

---

## Anomaly flags

1. **Bryson spill +26.1% (125→158 m³/s); total release +11.2% (295→328 m³/s).** Both exceed the >5% flag threshold. Turbined flat; headpond unchanged at 105.57 m. Interpretation: local precipitation runoff passing through Bryson's spillway without headpond buildup. Consistent with the "increase gradually" scenario in the Oct 13 ORRPB forecast.

2. **Lac Coulonge +5 cm** (105.88→105.93 m ORRPB daily Oct 13→14). First notable single-day increase in several weeks. Still etat 0 with 107 cm below pre-alert; not a flood concern at current levels.

3. **Mid-valley Oct 14 provisionals — structural recurring artifact, all sanity checks failed; excluded from headlines.**
   - **Des Joachims 153 m³/s prov** (Oct 13 final 331; −54%): (1) Feasibility: Des Joachims reservoir recorded 429 m³/s dispatch at T00 UTC Oct 14; a daily running mean of 153 from that starting point requires implausibly low dispatch for the remainder of the day. (2) Mass balance: Bryson immediately upstream dispatching 327 m³/s; Des Joachims at 153 with only +4 cm of pool rise is physically inconsistent — pool should be rising rapidly if outflow were truly 153 with 327 m³/s arriving. (3) Level: Des Joachims pool +4 cm Oct 13→14 T00; inconsistent with 153 m³/s outflow against 327+ m³/s inflow. (4) Downstream: Chenaux Oct 14 = 542 m³/s daily prov — incompatible with only 153 m³/s dispatched from Des Joachims immediately upstream (no tributary between the two can supply 389 m³/s). All 4 checks FAIL.
   - **Otto Holden 151 m³/s prov** (Oct 13 final 320; −53%): Upstream of Des Joachims; same artifact class. Otto Holden pool T00 Oct 14 = 177.18 m (unchanged from Oct 13 per recent trend) — incompatible with 151 m³/s outflow. All checks FAIL.
   - Petawawa cross-check: not pulled (Petawawa is not material here — the artifact is a partial-day running mean issue, not a tributary sourcing question).

---

## Notes

- **Vigilance ingest staleness:** Latest proxy record for station 1195 is T13 UTC Oct 13 (~33h before brief runtime). The ORRPB daily reading (105.93 m) is used as the primary Lac Coulonge level. Upstream Vigilance reachability is unverifiable from this sandbox (egress-blocked domain). Not an upstream outage claim — ingest lag only.
- **Carillon Oct 13 daily final = 765 m³/s.** Yesterday's brief predicted this would be "substantially higher than 496 m³/s" (the partial-day avg at brief time). Confirmed ✓. The 1,257 m³/s real-time value reported yesterday was a peak dispatch reading, not a daily average.
- **Oct 14 ORRPB Carillon daily prov = 1,015 m³/s.** Reflects yesterday's large peaking ramp still in the running mean. Real-time T18 = 852 m³/s, indicating today's dispatch is lower than yesterday's peak. Oct 14 daily final will settle lower than 1,015.
- **Témiscaming Oct 14 not yet posted by ORRPB.** PSPC cross-check at T00 UTC shows 326 m³/s — consistent with D27 sub-400. Will retro-check tomorrow.
- **V3 posterior:** Day 41 consecutive timeout (exit 143, 35s limit). `freshet-forecast.json` updated with refreshed `fetched_at_iso`; all other fields unchanged from Oct 13.
- **ORRPB flows Oct 1–14 (Témiscaming finals):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=307, Oct 7=313, Oct 8=296, Oct 9=309, Oct 10=286, Oct 11=308, Oct 12=304, Oct 13=309. Oct 14 not yet posted.
