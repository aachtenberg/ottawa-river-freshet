# Daily brief — 2026-10-11

*Generated automatically at 22:15 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) **RESTORED** — HTTP 200 ✓ (was HTTP 530 yesterday). All tables available. ORRPB conditions + forecast HTTP 200 ✓. Vigilance ingest fresh (station 1195 T21:00 UTC). V3 posterior: CSV still stale (asof 2026-06-07); `freshet_posterior.py` timed out (exit 143, Day 38); `freshet-forecast.json` carried forward unchanged.*

*Oct 10 retro-checks: Proxy now has Oct 10 T19 UTC data. Bryson T19 Oct 10 proxy = 328.39 m³/s total / 205.2 turbined / 123.19 spilled — matches HQ fallback exactly ✓. Lac Coulonge Oct 10 DB = 105.86 m — matches brief ✓. Temiscaming Oct 10 final (DB `orrpb_river_flows`) = **286 m³/s** (D23 confirmed; brief had 290 prov, diff −4 m³/s ✓ CONFIRMED). Des Joachims Oct 10 final = **311 m³/s** (brief correctly excluded prov 533 ✓ CONFIRMED EXCLUSION). Chats Falls Oct 10 final = 411 m³/s (brief excluded prov 538 ✓). Mattawa Oct 10 final = 152.27 m (brief had 152.22, diff +5 cm — borderline CONFIRMED, consistent with chronic low-read artifact noted in W40).*

---

## In plain language

### Upstream — the upper basin

The basin continues its autumn recession. Outflow from Lake Timiskaming finalized at 286 cubic metres per second for October 10 — the 23rd straight day below 400 m³/s — and today's running figure is around 278 m³/s, on pace for a 24th. The mid-valley reach is quiet: levels at Mattawa (152.17 m provisional) and Pembroke (110.95 m) continue their slow drift downward, consistent with the gentle recession of the past month.

All but one of the fourteen tracked reservoirs are either stable or slowly falling, with only one minor riser (Lady Evelyn, +3 cm). This is normal autumn drawdown — no active basin-wide retention underway.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge is sitting at 105.85 metres — down 1 centimetre from yesterday, fully in normal status, 115 centimetres below the 107-metre pre-alert level. At the Bryson Generating Station dam pond downstream, operators released slightly less water today (317 cubic metres per second total vs. 328 yesterday), with the spillway share dipping from 38% to 35%. The headpond ticked up 1 centimetre. No threshold concerns anywhere in the reach.

The ORRPB forecast (last published October 6, next update October 13) remains unchanged: water levels and flows are expected to stay fairly stable through next week.

---

## TL;DR

Retro ✓: Oct 10 all CONFIRMED — Temiscaming D23 final 286 m³/s ✓; Des Joachims prov 533 exclusion ✓; Chats Falls prov 538 exclusion ✓. Today: Lac Coulonge **105.85 m** (−1 cm; etat 0; 115 cm below pre-alert). Temiscaming D24 in progress (278 prov). Cluster proxy **RESTORED** (HTTP 200). Mid-valley Oct 11 provisionals (Des Joachims 145, Otto Holden 130, Chenaux 539, Chats 558) all failed sanity checks — excluded from headlines. Day **162** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: cluster proxy `river_readings?station_id=eq.1195` (HTTP 200 ✓) — T21:00 UTC Oct 11. DB `orrpb_river_levels?station=eq.lake-coulonge` Oct 11 = 105.85 m (HQ, same result).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21:00 UTC Oct 11) | **105.853 m** |
| ORRPB daily level Oct 11 | 105.85 m |
| ORRPB daily level Oct 10 | 105.86 m |
| 24h delta | **−1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 115 cm below |
| Distance to minor flood (107.50 m) | 165 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)` — HTTP 200 ✓, T19:00 UTC Oct 11. "Yesterday" = T19:00 UTC Oct 10 (from proxy, verified today).*

| Metric | Today (T19 Oct 11) | Yesterday (T19 Oct 10) | Δ |
|---|---|---|---|
| Total release (m³/s) | **316.77** | 328.39 | −11.62 (−3.5%) |
| Turbined (m³/s) | **205.07** | 205.20 | −0.13 (flat) |
| Spilled (m³/s) | **111.70** | 123.19 | **−11.49 (−9.3%) ⚑** |
| Spill share (%) | **35.2%** | 37.5% | −2.3 pp |
| Headpond / amont (m) | **105.55** | 105.54 | +1 cm |
| Tailwater / aval (m) | **86.66** | 86.70 | −4 cm |
| Δh (head differential, m) | **18.89** | 18.84 | +5 cm |

**Headpond band status:** 105.55 m is 88 cm above the 104.67 m band ceiling — **Day 136** above band (47-cm band: 104.20–104.67 m). Spill change (−9.3%) exceeds 5% flag threshold. Partial reversal of yesterday's +12.4% spill increase; total release returning toward the 315–320 m³/s range of recent weeks. No headpond band breach.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — HTTP 200 ✓, T19:00 UTC Oct 11 (Carillon, Quinze at T18:00).*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 208.33 | 0% |
| Quinze (3-31) | 203.62 | 0.6% |
| Îles (3-32) | 205.73 | 0% |
| Rapide-2 (3-29) | 157.39 | 0% |
| Rapide-7 (3-28) | 155.71 | 0% |
| Bryson (3-46) | **316.77** | **35.2%** |
| Paugan — Gatineau R. (3-65) | 155.50 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 152.26 | 0% |
| Carillon — basin terminal (3-60) | **640.42** (T18) | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming` (HTTP 200 ✓); `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke, lake-coulonge). All via cluster proxy.*

| Metric | Today / Latest | 7 d ago (Oct 4) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 10 final (m³/s) | **286** | 316 (Oct 4 final) | −30 (−9.5%) | D23 confirmed ✓; **D24 in progress** (278 prov Oct 11) |
| Témiscaming Oct 11 prov (m³/s) | **278** (PSPC cross-check, T00 UTC) | — | — | Sub-400 D24 in progress; provisional, directional only |
| PSPC cross-check (m³/s) | **278** (timiskaming reservoir flow) | — | — | Agrees with ORRPB provisional; no discrepancy >50 m³/s |
| Quinze release → into the lake (m³/s) | **203.62** (T18 HQ) | ~202 (W40 est.) | ~flat | Normal autumn dispatch |
| Mattawa level (m) | **152.17** (Oct 11 prov — artifact caution: typically finalizes 5–12 cm higher; Oct 10 final = 152.27 m) | 152.26 (Oct 4 final, W40) | ~−9 cm | Direction DOWN; provisional |
| Pembroke level (m) | **110.95** (Oct 11) | ~110.97 (Oct 4 est.) | ~−2 cm | Direction DOWN (slight); no threshold data |

**Reservoir balance (Oct 10 → Oct 11, all 14 reservoirs in DB):** 5 falling · 8 steady · 1 rising (Lady Evelyn +3 cm). No reservoir rising >10 cm/day. Normal autumn drawdown; no active basin-wide retention.

**Milestone bookkeeping (W40 anchor Oct 4 + Oct 5–11 extension):**

| Milestone | W40 close (Oct 4) | Oct 5 | Oct 6 | Oct 7 | Oct 8 | Oct 9 | Oct 10 | **Oct 11** |
|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 155 | 156 | 157 | 158 | 159 | 160 | 161 | **162** |
| Bryson amont above band (104.67 m) | 129 | 130 | 131 | 132 | 133 | 134 | 135 | **136** |
| §15.3.5.1 trigger INACTIVE | 132 | 133 | 134 | 135 | 136 | 137 | 138 | **139** (Hull 41.24 m) |
| Temiscaming sub-400 | D17 (316) | D18 (315) | D19 (306) | D20 (315) | D21 (296) | D22 (311) | D23 (286) | **D24** (278 prov) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19:00 UTC Oct 11.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.24 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 139** (137 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull at 41.24 m, flat vs. Oct 10 T19 (41.24 m).

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00:00 UTC Oct 11.*

| Reservoir | Oct 10 | Oct 11 | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.68 m | **219.65 m** | −3 cm | Normal autumn drainage |
| Témiscaming (PSPC) | 178.74 m | **178.71 m** | −3 cm | Consistent with ~278–286 m³/s outflow |
| Dozois | 342.67 m | **342.63 m** | −4 cm | Normal drawdown |
| Bark Lake (OPG) | 313.71 m | **313.71 m** | 0 cm | Steady |

Full balance: 5 falling · 8 steady · 1 rising across 14 tracked reservoirs. No 2+ reservoirs rising >10 cm/day.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 128,826b ✓. **Last Update: 2026-10-06 2:57 PM EDT** (2026-10-06T18:57:00Z UTC). **Next Update: 2026-10-13 4:00 PM EDT** (2026-10-13T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from Oct 6 publication.** Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year resulting from below-normal precipitation across the watershed over recent weeks. Water levels and flows are expected to remain fairly stable in most locations over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false. Mode: `weekly-notice`. Next update Oct 13.

---

## Anomaly flags

1. **Bryson spill −9.3% vs Oct 10** (123.19 → 111.70 m³/s). Total release −3.5%; turbined flat. Spill share fell from 37.5% to 35.2%. Partial reversal of yesterday's +12.4% flag. No headpond band breach. Flagged per rule (>5% in any series); within routine autumn dispatch variation.

2. **Mid-valley Oct 11 provisionals all failed sanity checks — excluded from headlines.**
   - Des Joachims: 145 m³/s prov vs Oct 10 final 311 (−53.4%). Run time ~22:15 UTC (~18.2h of day).
     - Feasibility: floor = (18.2/24)×145 = 110 m³/s — physically possible but inconsistent with upstream.
     - Mass balance: Bryson upstream at 317 m³/s; Des Joachims (downstream of Bryson) cannot be 145 m³/s. Direct upstream contradiction. **FAILS.**
     - Downstream response: Chenaux immediately downstream = 539 m³/s vs Des Joachims 145. Direct contradiction. **FAILS.**
   - Otto Holden: 130 m³/s prov vs Oct 10 final 299 (−56.5%). Same upstream contradiction. **FAILS.**
   - Chenaux: 539 m³/s prov vs Oct 10 final 411 (+31.1%).
     - Feasibility: floor = (18.2/24)×539 = 409 m³/s — borderline.
     - Mass balance: Bryson 317 + Petawawa 9.7 (WSC proxy T20:35) + other tributaries ~15 ≈ 342 expected. 539 implies ~197 m³/s unexplained. **FAILS.**
     - Pool consistency: Des Joachims reservoir Oct 11 = 152.11 m (essentially flat vs Oct 10 152.10). No pool signal for a real dispatch change. **FAILS.**
     - Downstream: Carillon 640 < Chats Falls 558 + Gatineau mouth 152 = 710. 70 m³/s gap. **FAILS.**
   - Chats Falls: 558 m³/s prov vs Oct 10 final 411 (+35.8%). Downstream contradiction vs Carillon. **FAILS.**
   - Petawawa (WSC 02KB001): 9.68–9.74 m³/s at T20:30–20:35 UTC. Mass balance check result confirmed.
   - All four in data tables only, marked provisional/failed sanity check.

3. **Cluster proxy RESTORED** (HTTP 200 after yesterday's HTTP 530 Cloudflare error). All proxy tables available. No data gap in finalized records — HQ upstream fallback data from yesterday's brief matched proxy values exactly (Bryson T19 Oct 10: proxy 328.39 vs HQ fallback 328.4 ✓).

---

## Notes

- **ORRPB flows table (Oct 1–11):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=306, Oct 7=315, Oct 8=296, Oct 9=311, Oct 10=286 (final). Oct 11 not yet in orrpb_river_flows table; PSPC cross-check from `reservoir_readings` shows 278 m³/s (provisional).
- **Mattawa chronic artifact:** Oct 10 brief reported 152.22 m; final = 152.27 m, diff +5 cm (borderline CONFIRMED). Pattern ongoing (W40 Human queue item 5). Today's provisional 152.17 m likely understates the final mean.
- **V3 posterior:** Day 38 consecutive timeout (exit 143, limit 35s). `freshet-forecast.json` unchanged (asof 2026-06-07). Probabilities = 1.0 for all season-resolved thresholds.
- **ORRPB river page:** Oct 11 Carillon shows 692 m³/s at page-fetch time (~T21 UTC page cache); DB `orrpb_river_flows` shows 640 m³/s for Oct 11 prov. Timing difference (page may have been cached at mid-afternoon T15 EDT); DB value used throughout.
