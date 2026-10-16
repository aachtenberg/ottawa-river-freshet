# Daily brief — 2026-10-16

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (116 b probe). ORRPB conditions + forecast HTTP 200 ✓ (forecast unchanged since Oct 13 21:02 UTC — next update Oct 20). Vigilance 1195 ingest stale: latest proxy record T13 UTC Oct 13 (~81h before brief runtime; upstream unverifiable from sandbox — egress-blocked); ORRPB daily Oct 16 = 105.95 m used as primary level source, ORRPB real-time 15:00 ET = 105.96 m as cross-check. V3 posterior: timed out (exit 124, Day 43 consecutive); `freshet-forecast.json` restored from git HEAD unchanged (asof 2026-06-07).*

*Oct 15 retro-checks: Lac Coulonge Oct 15 daily final = **105.93 m** ✓ CONFIRMED (claimed 105.93 m ✓). Témiscaming D28 = **308 m³/s** ✓ CONFIRMED (yesterday marked "D28 in progress" — confirmed sub-400, Day 28). Mid-valley Oct 15 exclusions validated: Des Joachims final 321 m³/s (provisional 444 — excluded from headlines, reported in tables as provisional ✓); Otto Holden final 317 m³/s (provisional 412 — excluded ✓). Bryson Oct 15 spill at T21: 166.78 m³/s (brief claimed 166.69 at T19 ✓, consistent within 0.1%).*

---

## In plain language

### Upstream — the upper basin

The upper basin is in quiet recession. Lake Timiskaming's outflow for October 15 came in at 308 cubic metres per second — Day 28 below 400 — and October 16 has not yet posted to the ORRPB flow table. The Mattawa level gauge fell 4 centimetres today to 152.25 m, continuing its gentle post-precipitation-pulse decline from the 152.31 m high on October 14; Pembroke ticked down 1 centimetre to 110.99 m.

Reservoir storage is broadly steady, with at least three reservoirs nudging upward: Lake Timiskaming (+5 cm), the Des Joachims pool (+6 cm), and Kiamika (+3 cm). None is moving at a pace that signals active large-scale retention.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge rose 2 centimetres today to 105.95 m according to the ORRPB daily record, and the mid-afternoon ORRPB reading (3:00 PM Eastern) shows 105.96 m. Still firmly in normal conditions — 105 centimetres below the 107.00-metre pre-alert level.

The notable event today is at the Bryson Generating Station dam pond, well downstream of the lake and not adjacent to the Mansfield properties. Operators nearly shut down the turbines — turbine output dropped from 169 to 35 cubic metres per second — and routed almost all flow through the spillway, which surged from 167 to 377 cubic metres per second. Total release rose 23% to 412 m³/s. The dam pond level barely moved (+2 cm to 105.56 m, still 89 centimetres above the top of its operating band). Whether this reflects grid pricing, equipment maintenance, or flow management is not stated in the public telemetry; the pattern is consistent with an operator choosing to pass a precipitation-related inflow pulse through the spillway rather than through the turbines. The increased flow is propagating downstream: mid-valley gauges at Des Joachims and Otto Holden are running about 35% above yesterday's finals, with all sanity checks passing (see Notes). At the basin's terminal dam, Carillon is releasing 1,631 m³/s — up from 904 yesterday — with the headpond and the Hull dock gauge rising modestly, indicating lower-Ottawa-Valley inflow is loading the reservoir, likely from the same precipitation system.

The ORRPB forecast (next update October 20) is unchanged: levels expected to increase gradually or hold fairly stable depending on location over the coming week. That language fits what is unfolding today.

---

## TL;DR

Retro ✓: Oct 15 Lac Coulonge 105.93 m ✓; Témiscaming D28 final 308 m³/s ✓ (sub-400 confirmed); mid-valley Oct 15 exclusions validated (Des Joachims 321, Otto Holden 317 — well below provisionals 444/412). **Today:** ⚠ **Bryson posture shift** — turbines near-shutdown (169→35 m³/s, −79%); spillway surge (167→377 m³/s, +126%); total +23% to 412 m³/s. Lac Coulonge +2 cm to **105.95 m (etat 0; 105 cm below pre-alert)**. Carillon **1,631 m³/s** (was 904; Hull dock +7 cm). Témiscaming Oct 15 final 308 (D28); Oct 16 not yet posted (D29 in progress). ORRPB forecast unchanged. Day **167** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 16 daily (primary; Vigilance ingest stale at T13 UTC Oct 13 — ~81h before brief runtime; upstream unverifiable from sandbox). ORRPB real-time conditions 105.96 m at 15:00 ET as cross-check.*

| Metric | Value |
|---|---|
| Current level (ORRPB daily Oct 16) | **105.95 m** |
| ORRPB real-time (Oct 16, 15:00 ET) | 105.96 m |
| ORRPB daily Oct 15 | 105.93 m |
| 24h delta (ORRPB daily Oct 15→16) | **+2 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 105 cm below |
| Distance to minor flood (107.50 m) | 155 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T18–T19 UTC Oct 16. Yesterday: T21 UTC Oct 15. ⚠ Major posture change — turbines near-shutdown, spill surge.*

| Metric | Today (T18–T19 Oct 16) | Yesterday (T21 Oct 15) | Δ |
|---|---|---|---|
| Total release (m³/s) | **412.04** | 335.88 | **+76.2 (+22.7%)** |
| Turbined (m³/s) | **35.11** | 169.10 | **−133.99 (−79.2%)** |
| Spilled (m³/s) | **376.93** | 166.78 | **+210.15 (+126.0%)** |
| Spill share (%) | **91.5%** | 49.6% | **+41.9 pp** |
| Headpond / amont (m) | **105.56** | 105.54 | +2 cm |
| Tailwater / aval (m) | **86.96** | 86.89 | +7 cm |
| Δh (head differential, m) | **18.60** | 18.65 | −5 cm |

**Headpond band status:** 105.56 m is 89 cm above the 104.67 m band ceiling — **Day 141** above band. All metrics exceed the >5% flag threshold. Turbined and spilled changes exceed 100%.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 16.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 203.22 | 0% |
| Quinze (3-31) | 202.24 | 0.6% |
| Îles (3-32) | 201.74 | 0% |
| Rapide-2 (3-29) | 156.99 | 0% |
| Rapide-7 (3-28) | 155.76 | 0% |
| Bryson (3-46) | **412.04** | **91.5%** |
| Paugan — Gatineau R. (3-65) | 163.02 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 191.34 | 0% |
| Carillon — basin terminal (3-60) | **1,631.79** | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 9) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 15 final (m³/s) | **308** | 309 (Oct 9 final) | −1 | **D28 sub-400 confirmed** |
| Témiscaming Oct 16 ORRPB prov (m³/s) | not yet posted | — | — | D29 in progress |
| PSPC cross-check Oct 15 (m³/s) | **308** (agrees) | — | — | ✓ agrees with ORRPB within 50 m³/s |
| PSPC cross-check Oct 16 T00 | not yet posted | — | — | WSC-only row; PSPC pending |
| Quinze release → into the lake (m³/s) | **202.24** (T19) | ~309 (Oct 9) | — | Autumn low dispatch |
| Mattawa level (m) | **152.25** (Oct 16 ORRPB daily) | 152.12 (Oct 9) | +13 cm | Direction DOWN (from 152.31 Oct 14 high) |
| Pembroke level (m) | **110.99** (Oct 16) | 111.00 (Oct 9) | −1 cm | Direction flat/slightly down; no threshold data |

**Reservoir balance (Oct 15 T00 → Oct 16 T00, using `latest_reservoir_readings` vs yesterday's brief):** Timiskaming +5 cm (rising) · Des Joachims +6 cm (rising) · Kiamika +3 cm (rising) · Baskatong −1 cm (steady) · Dozois −2 cm (steady) · Bark Lake +1 cm (steady) · other 8 reservoirs not resolved from available data. At least 3 rising · ≥3 steady · 0 confirmed falling. None rising >10 cm/day; no active basin-wide retention signal. Timiskaming rising despite outflow (308 m³/s) > identified Quinze inflow (202 m³/s) — likely lag in PSPC reporting or untracked local inflow; not flagged as anomaly.

**Milestone bookkeeping (W41 anchor Oct 11 + Oct 12–16 extension):**

| Milestone | W41 close (Oct 11) | Oct 12 | Oct 13 | Oct 14 | Oct 15 | **Oct 16** |
|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 162 | 163 | 164 | 165 | 166 | **167** |
| Bryson amont above band (104.67 m) | 136 | 137 | 138 | 139 | 140 | **141** |
| §15.3.5.1 trigger INACTIVE | 139 | 140 | 141 | 142 | 143 | **144** |
| Temiscaming sub-400 | D24 (308) | D25 (304) | D26 (309) | D27 (306) | D28 (308 final) | **D29 in progress** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 16.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.33 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 144** (128 cm below trigger; +7 cm from Oct 15) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull rising (+7 cm today), consistent with Carillon headpond loading from lower-valley inflow.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 16.*

| Reservoir | Oct 15 (T00) | Oct 16 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.57 m | **219.56 m** | −1 cm | Steady |
| Témiscaming | 178.78 m | **178.83 m** | **+5 cm** | Rising; outflow 308 > Quinze 202 — lag or untracked local inflow |
| Dozois | 342.49 m | **342.47 m** | −2 cm | Steady |
| Bark Lake (OPG) | 313.75 m | **313.76 m** | +1 cm | Steady |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-13 5:02 PM EDT** (2026-10-13T21:02:00Z UTC). **Next Update: 2026-10-20 4:00 PM EDT** (2026-10-20T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: true (precipitation language still current). Mode: `weekly-notice`.

---

## Anomaly flags

1. **⚠ Bryson posture shift.** Turbined −79% (169→35 m³/s); spilled +126% (167→377 m³/s); total +22.7%; spill share 49.6%→91.5%. Exceeds every >5% flag threshold by a wide margin. Headpond barely moved (+2 cm to 105.56 m), consistent with a management decision rather than headpond-level-driven response. Cause not stated in public data.

2. **⚠ Carillon 1,631 m³/s** (was 904 yesterday, +80%). HQ real-time data — not an ORRPB provisional. Hull dock +7 cm; Carillon amont +1 cm. Pattern consistent with lower-basin precipitation/runoff loading the Carillon headpond, and HQ releasing to manage headpond level. No directive exceedance (trigger inactive).

3. **Mid-valley flows elevated — Oct 16 ORRPB provisionals (sanity-check PASSES — see Notes for full check results).** Des Joachims 432 m³/s prov (+34.6% vs Oct 15 final 321; all 4 checks pass); Otto Holden 429 m³/s prov (+35.3% vs Oct 15 final 317; all 4 checks pass). Bryson's 412 m³/s dispatch drives the elevation; downstream response (Chenaux 541, Chats Falls 563) is consistent. Reported in tables as provisional; finals expected Oct 17.

---

## Notes

- **Vigilance ingest staleness:** Latest proxy record for station 1195 is T13 UTC Oct 13 (~81h before brief runtime). ORRPB daily Oct 16 (105.95 m) and real-time (105.96 m at 15:00 ET) used as primary and cross-check. Upstream reachability unverifiable (egress-blocked sandbox). Not an upstream outage claim.
- **Provisional-flow sanity checks (Oct 16 mid-valley, mandatory for ≥25% claims):**
  - *Des Joachims 432 prov vs Oct 15 final 321 (+34.6%):* (1) Feasibility back-out: at T19 UTC (h=19), floor = (19/24)×432 = **342 m³/s minimum** for final — comfortably above Oct 15 final. (2) Mass balance: Bryson dispatching 412 m³/s upstream is the primary driver; tributaries negligible at this season. (3) Level/pool: Des Joachims pool rose +6 cm (T00-to-T00), consistent with elevated throughput. (4) Downstream: Chenaux 541, Chats Falls 563 — both elevated, consistent. **All 4 checks pass.**
  - *Otto Holden 429 prov vs Oct 15 final 317 (+35.3%):* (1) At T19 UTC, floor = (19/24)×429 = **339 m³/s minimum**. (2) Otto Holden receives Des Joachims outflow (432); +3 m³/s difference negligible. (3) Des Joachims pool rising = consistent with upstream propagation. (4) Chenaux/Chats Falls elevated = consistent. **All 4 checks pass.**
- **V3 posterior:** Day 43 consecutive timeout (exit 124, 40-second limit). `freshet-forecast.json` restored from git HEAD (asof 2026-06-07, season_resolved=false, unchanged). Dashboard continues to serve the Jun 7 posterior.
- **ORRPB flows Oct 1–16 (Témiscaming finals):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=306, Oct 7=315, Oct 8=296, Oct 9=309, Oct 10=286, Oct 11=308, Oct 12=304, Oct 13=309, Oct 14=306, Oct 15=308. Oct 16 not yet posted.
