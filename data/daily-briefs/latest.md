# Daily brief — 2026-10-15

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (117 b probe). ORRPB conditions + forecast HTTP 200 ✓ (forecast unchanged since Oct 13 21:02 UTC — next update Oct 20). Vigilance 1195 ingest stale: latest proxy record T13 UTC Oct 13 (~57h before brief runtime; upstream unverifiable from sandbox — egress-blocked); ORRPB daily Oct 15 = 105.93 m used as primary level source. V3 posterior: timed out (exit 143, Day 42 consecutive); `freshet-forecast.json` updated with current fetch timestamp, posterior unchanged.*

*Oct 14 retro-checks: Lac Coulonge claim "105.93 m (+5 cm)" — ORRPB Oct 14 daily final = **105.93 m** ✓ CONFIRMED. Témiscaming D27 "prov 326 m³/s (PSPC T00)" — Oct 14 ORRPB final = **306 m³/s** (−20 m³/s; within 50 m³/s threshold) ✓ CONFIRMED. Carillon Oct 14 prov 1,015 (noted as partial-day) — Oct 14 final = **998 m³/s** (−17, −1.7%) ✓. Mid-valley Oct 14 exclusions validated: Des Joachims final 374 m³/s (prov 153, +2.4× — exclusion correct ✓); Otto Holden final 335 m³/s (prov 151, +2.2× — exclusion correct ✓).*

---

## In plain language

### Upstream — the upper basin

The upper basin is quietly receding. Lake Timiskaming's daily outflow for October 14 came in at 306 cubic metres per second — the 27th consecutive day below 400 m³/s — and October 15 is tracking in the same range. Mattawa, the mid-valley level gauge, fell eight centimetres today after two days of modest precipitation-driven increases, a sign the brief rain pulse has passed and the river is returning to its gentle downward trend. Pembroke is holding flat.

Reservoir storage is neutral: across 14 tracked reservoirs, two are falling slightly (the Des Joachims pool and the Lady Evelyn reservoir, each down 3–4 centimetres), one is inching upward (Kiamika, +3 centimetres), and the rest are flat. Normal quiet-autumn behaviour; no retention signal.

### At the property — Lac Coulonge / Mansfield

The lake at Fort-Coulonge held steady today at 105.93 metres — unchanged from yesterday according to the ORRPB daily record, and consistent with the 105.92-metre reading the ORRPB posted for mid-afternoon. The brief rise from precipitation earlier in the week has levelled off. At 107 centimetres below the 107-metre pre-alert level, the property is firmly in normal conditions.

At the Bryson Generating Station dam pond (well downstream of the lake, not adjacent to the Mansfield properties), the spill flow edged up slightly — about 5 percent — from yesterday's already-elevated level, continuing the pattern of passing excess autumn runoff through the spillway. The dam pond itself ticked down four centimetres, to 105.53 metres. Operations are routine. The ORRPB forecast (next update October 20) remains unchanged: levels expected to increase gradually or hold fairly stable, depending on location, over the coming week.

---

## TL;DR

Retro ✓: Oct 14 Lac Coulonge final 105.93 m ✓; Témiscaming D27 final 306 m³/s ✓; Carillon Oct 14 final 998 m³/s ✓; mid-valley Oct 14 exclusions validated (Des Joachims 374, Otto Holden 335 — both ~2× their provisionals). **Today:** Lac Coulonge **105.93 m (0 cm; etat 0; 107 cm below pre-alert)** — flat after Oct 14 precipitation rise. Bryson spill +5.5% (157.94→166.69 m³/s); total +2.5% (327.91→336.17 m³/s); turbined flat; headpond −4 cm to 105.53 m. Témiscaming D27 final = 306; D28 in progress (Oct 15 not yet posted). Carillon T19 = 904 m³/s. ORRPB forecast unchanged. Day **166** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: ORRPB `orrpb_river_levels?station=eq.lake-coulonge` Oct 15 daily (primary; Vigilance ingest stale at T13 UTC Oct 13 — real-time ORRPB conditions 105.92 m at 15:00 ET used as cross-check).*

| Metric | Value |
|---|---|
| Current level (ORRPB daily Oct 15) | **105.93 m** |
| ORRPB real-time (Oct 15, 15:00 ET) | 105.92 m |
| ORRPB daily Oct 14 | 105.93 m |
| 24h delta (ORRPB daily Oct 14→15) | **0 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 107 cm below |
| Distance to minor flood (107.50 m) | 157 cm below |

---

## Bryson operating posture (cluster proxy)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)` — T19 UTC Oct 15 vs T19 UTC Oct 14.*

| Metric | Today (T19 Oct 15) | Yesterday (T19 Oct 14) | Δ |
|---|---|---|---|
| Total release (m³/s) | **336.17** | 327.91 | +8.3 (+2.5%) |
| Turbined (m³/s) | **169.49** | 169.97 | −0.5 (flat) |
| Spilled (m³/s) | **166.69** | 157.94 | **+8.8 (+5.5%)** |
| Spill share (%) | **49.6%** | 48.2% | +1.4 pp |
| Headpond / amont (m) | **105.53** | 105.57 | −4 cm |
| Tailwater / aval (m) | **86.89** | 86.84 | +5 cm |
| Δh (head differential, m) | **18.64** | 18.73 | −9 cm |

**Headpond band status:** 105.53 m is 86 cm above the 104.67 m band ceiling — **Day 140** above band. Spill +5.5% exceeds the >5% flag threshold (flagged below). Turbined flat; headpond fell 4 cm; interpretation: precipitation runoff passthrough continuing from Oct 14.

---

## Main-stem cascade (cluster proxy, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 15.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | 203.31 | 0% |
| Quinze (3-31) | 202.31 | 0.5% |
| Îles (3-32) | 207.30 | 0% |
| Rapide-2 (3-29) | 157.32 | 0% |
| Rapide-7 (3-28) | 155.40 | 0% |
| Bryson (3-46) | **336.17** | **49.6%** |
| Paugan — Gatineau R. (3-65) | 160.85 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | 180.70 | 0% |
| Carillon — basin terminal (3-60) | 904.29 | 0% |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows?station=eq.temiscaming`; `reservoir_readings?reservoir_id=eq.timiskaming` (PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 8) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 14 final (m³/s) | **306** | 296 (Oct 8 final) | +10 | D27 confirmed ✓ |
| Témiscaming Oct 15 ORRPB prov (m³/s) | not posted yet | — | — | D28 in progress |
| PSPC cross-check Oct 15 T00 (m³/s) | null (WSC row only; PSPC not yet posted) | — | — | — |
| Quinze release → into the lake (m³/s) | **202.31** (T18 HQ) | ~296 (Oct 8) | — | Autumn low dispatch; normal |
| Mattawa level (m) | **152.23** (Oct 15 ORRPB daily) | 152.27 (Oct 8) | −4 cm (vs 7d) | Direction DOWN (post-precip decline; was 152.31 Oct 14) |
| Pembroke level (m) | **111.01** (Oct 15) | 111.00 (Oct 8 est.) | +1 cm (flat) | Direction flat; no threshold data |

**Reservoir balance (Oct 14 T00 → Oct 15 T00, 14 reservoirs):** 2 falling (Des Joachims −4 cm, Lady Evelyn −3 cm) · 11 steady · 1 rising (Kiamika +3 cm). Neutral posture — no reservoir rising >10 cm/day.

**Milestone bookkeeping (W41 anchor Oct 11 + Oct 12–15 extension):**

| Milestone | W41 close (Oct 11) | Oct 12 | Oct 13 | Oct 14 | **Oct 15** |
|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 162 | 163 | 164 | 165 | **166** |
| Bryson amont above band (104.67 m) | 136 | 137 | 138 | 139 | **140** |
| §15.3.5.1 trigger INACTIVE | 139 | 140 | 141 | 142 | **143** |
| Temiscaming sub-400 | D24 (308) | D25 (304) | D26 (309) | D27 (306 final) | **D28 (not yet posted)** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 15.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.26 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 143** (135 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull at 41.26 m, 135 cm below trigger threshold.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 15.*

| Reservoir | Oct 14 (T00) | Oct 15 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.59 m | **219.57 m** | −2 cm | Normal autumn drainage |
| Témiscaming | 178.78 m | **178.78 m** | 0 cm | Flat; PSPC flow Oct 14 final 306 m³/s |
| Dozois | 342.51 m | **342.49 m** | −2 cm | Normal drawdown |
| Bark Lake (OPG) | 313.75 m | **313.75 m** | 0 cm | Steady |

Full balance: 2 falling · 11 steady · 1 rising (Kiamika +3 cm) across 14 tracked reservoirs. No active basin-wide retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-13 5:02 PM EDT** (2026-10-13T21:02:00Z UTC). **Next Update: 2026-10-20 4:00 PM EDT** (2026-10-20T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Forecast text (verbatim):

> *Water levels and flows along the main stem of the Ottawa River are below average at most locations for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to increase gradually or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: true (precipitation language still valid). Mode: `weekly-notice`.

---

## Anomaly flags

1. **Bryson spill +5.5% (157.94→166.69 m³/s).** Exceeds the >5% flag threshold. Total release +2.5%; turbined flat; headpond −4 cm. Continuation of precipitation-runoff passthrough from Oct 14. Headpond declining slightly indicates normal pass-through, not accumulation.

2. **Mid-valley Oct 15 provisionals (below sanity-check trigger thresholds):** Des Joachims 444 m³/s prov (+70 m³/s vs Oct 14 final 374; +18.7%); Otto Holden 412 m³/s prov (+77 m³/s vs Oct 14 final 335; +23%). Both below the ≥25% / ≥150 m³/s mandatory-check threshold — reported in tables as provisional, no sanity protocol required. Changes are plausible: Bryson dispatching 336 m³/s with Petawawa and other mid-valley tributaries adding ~100 m³/s is consistent with Des Joachims at 444 m³/s. Des Joachims pool falling 4 cm (152.16→152.12 m) is consistent with outflow exceeding inflow.

---

## Notes

- **Vigilance ingest staleness:** Latest proxy record for station 1195 is T13 UTC Oct 13 (~57h before brief runtime). ORRPB daily (105.93 m) and ORRPB real-time conditions (105.92 m at 15:00 ET) used as primary and cross-check respectively. Upstream Vigilance reachability unverifiable from this sandbox (egress-blocked domain). Not an upstream outage claim — ingest lag only.
- **Oct 14 mid-valley exclusion validated.** Des Joachims Oct 14 final = 374 m³/s (provisonal was 153; ratio 2.44×); Otto Holden Oct 14 final = 335 m³/s (provisional was 151; ratio 2.22×). Structural partial-day running-mean artifact confirmed. Today's Oct 15 provisionals (444, 412) are more plausible in context of Bryson's 336 m³/s dispatch.
- **V3 posterior:** Day 42 consecutive timeout (exit 143, 35-second limit). `freshet-forecast.json` updated with refreshed `fetched_at_iso`; all other fields unchanged from Oct 13.
- **Detached HEAD at session start (recurrence).** Fixed before commit: `git checkout main` + `git pull origin main`. This is the W41 human-queue item 3 recurring failure. State was clean (previous brief already in origin/main; no local commits lost).
- **ORRPB flows Oct 1–15 (Témiscaming finals):** Oct 1=314, Oct 2=336, Oct 3=325, Oct 4=316, Oct 5=315, Oct 6=307, Oct 7=313, Oct 8=296, Oct 9=309, Oct 10=286, Oct 11=308, Oct 12=304, Oct 13=309, Oct 14=306. Oct 15 not yet posted.
