# Daily brief — 2026-11-04

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 117 b). ORRPB forecast HTTP 200 ✓ — last update Nov 3 2:09 PM EST; next update Nov 10 4:00 PM EST (weekly cadence, unchanged from prior brief). Vigilance 1195: proxy ingest fresh T21 UTC Nov 4 (105.869 m). V3 posterior: ran successfully (exit 0) — `freshet-forecast.json` content unchanged (anchors on asof 2026-06-07; unchanged until `lac-coulonge-daily-1990-2026.csv` is extended).*

*Nov 3 retro-checks: **Nov 3 Témiscaming D47 final 352 m³/s** — wait, `orrpb_river_flows` row for Nov 3 now shows **351 m³/s** (yesterday's provisional 358 m³/s → −2.0%, well within 50 m³/s, **CONFIRMED**). D47 sub-400 confirmed. **Nov 3 Mattawa daily:** yesterday's TL;DR reported live T17 reading of 152.49 m (+18 cm); ORRPB daily Nov 3 finalized at **152.35 m** (+11 cm from Nov 2 daily 152.24 m) — direction (rising) correct, level differs by 14 cm (recurring live-vs-daily convention). No flood-state claim affected. **Nov 3 Lac Coulonge ORRPB daily** finalized at **105.85 m** (yesterday provisional 105.86 m, −1 cm, negligible).*

---

## In plain language

### Upstream — the upper basin

The basin is in quiet late-autumn recession, now 186 days past the May 2 seasonal peak. The outflow from Lake Timiskaming — the large reservoir at the head of the main stem — was measured by federal monitors at 398 cubic metres per second at midnight going into today. That is a modest uptick from the 351 cubic metres per second finalized for November 3, and the 48th straight day the outflow has stayed below 400 cubic metres per second. Note that the Ottawa River Regulation Planning Board's own provisional figure for today reads an unusually low 202 cubic metres per second — far from the federal figure and inconsistent with any physically plausible single-day change — this appears to be a corrupted provisional value, not a real reading. The federal measurement is the reliable one.

The Mattawa level, an upstream indicator at a town roughly 200 kilometres above Lac Coulonge, edged down to 152.27 metres on today's early-morning snapshot — 8 centimetres lower than yesterday's daily reading — ending the brief three-day rise that the late-October rainfall produced. The slide is gentle and there is no new precipitation loading visible at the head of the system. Pembroke, further downstream, held essentially flat at 111.00 metres. All 14 tracked reservoirs are essentially stable; two (at the Rapide-7 pond and the Des Joachims pool) each rose 3–4 centimetres overnight, a minor fluctuation consistent with normal operations.

### At the property — Lac Coulonge / Mansfield

The water at Fort-Coulonge stood at 105.869 metres at 9 PM UTC — slightly higher than the 105.851 it showed at the same hour yesterday — essentially flat, up about 2 centimetres. The ORRPB daily series for today, based on the midnight reading, shows 105.86 metres, 1 centimetre above yesterday's finalized daily of 105.85 metres. The lake is fully in normal conditions — 115 centimetres below the 107.00-metre pre-alert threshold — with no flood risk.

Well downstream, at the Bryson Generating Station (reached by a long winding channel well below Lac Coulonge's south end, not visible from the Mansfield properties), partial spillway operation entered its third consecutive day unchanged: about 114 cubic metres per second continued through the spillway alongside 204 cubic metres per second through the turbines, for a total of 317 cubic metres per second — practically identical to the past two days. The dam pond held at 105.57 metres. Carillon, the basin's terminal dam near Hawkesbury, was releasing around 781 cubic metres per second at 8 PM UTC, down from about 970 cubic metres per second earlier in the afternoon — an intraday dispatch reduction rather than a day-over-day trend change. The ORRPB forecast from November 3 (unchanged; next update November 10) calls for levels to "slightly increase or remain fairly stable depending on location" in the coming week, citing forecast precipitation, but does not name Lac Coulonge specifically.

---

## TL;DR

**RETRO ✓:** Nov 3 D47 final **351 m³/s** (prov 358 → −2.0%, CONFIRMED). **Today (Day 186):** Lac Coulonge T21 **105.869 m** (+2 cm vs T20 yesterday; etat 0, 115 cm below pre-alert). Bryson Day 3 partial spill: **35.8%** (113.6 m³/s, flat). Carillon T20 **781 m³/s** (intraday: 970 → 781, −19.5% from T16–T20; dispatch drawdown). R7 intraday ramp T17→T19: 158 → 213 m³/s. Témiscaming D48: PSPC T00 **398 m³/s** (barely sub-400; ORRPB provisional **202 corrupted** — PSPC/ORRPB discrepancy 196 m³/s). Mattawa ORRPB daily **152.27 m** (−8 cm from Nov 3 finalized 152.35 m; daily rise streak ends). Pembroke 111.00 m (flat). Hull dock T20 41.24 m — trigger INACTIVE **Day 163**. Reservoir balance: **0 falling · 12 steady · 2 rising** (rapide_7 +3 cm, des_joachims +4 cm). ORRPB forecast unchanged (Nov 3; next Nov 10).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 4 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 4 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 4) | **105.869 m** |
| ORRPB daily Nov 4 | 105.86 m (provisional from T00) |
| 24h delta (Vigilance T21 Nov 4 vs T20 Nov 3) | **+2 cm** |
| ORRPB daily delta (Nov 3 finalized 105.85 → Nov 4 provisional 105.86) | +1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 115 cm below |
| Distance to minor flood (107.50 m) | 165 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 UTC Nov 4 (releases + levels). Yesterday: T16 UTC Nov 3 (releases, from yesterday's brief); T17 UTC Nov 3 (levels, from yesterday's brief).*

| Metric | Today (T20 Nov 4) | Yesterday (T16/T17 Nov 3) | Δ |
|---|---|---|---|
| Total release (m³/s) | **317.36** | 317.54 | −0.18 (−0.1%) |
| Turbined (m³/s) | **203.77** | 204.09 | −0.32 (−0.2%) |
| Spilled (m³/s) | **113.59** | 113.44 | +0.15 (+0.1%) |
| Spill share (%) | **35.8%** | 35.7% | +0.1 pp |
| Headpond / amont (m) | **105.57** (T20) | 105.56 (T17 Nov 3) | +1 cm |
| Tailwater / aval (m) | **86.73** (T20) | 86.70 (T17 Nov 3) | +3 cm |
| Δh (head differential, m) | **18.84** | 18.86 | −0.02 |

No change exceeds the 5% flag threshold. Bryson Day 3 of partial spill — essentially flat across all metrics. Headpond 105.57 m = **90 cm above** the 104.67 m band ceiling — **Day 160** above band.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 4. Yesterday comparison: Nov 3 brief T16–T17 snapshot values.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **225.61** T20 | 0% | +7.00 (+3.2%) |
| Quinze (3-31) | **209.41** T20 | 0.4% | +0.76 (flat) |
| Îles (3-32) | **211.92** T20 | 0% | −3.68 (−1.7%) |
| Rapide-2 (3-29) | **242.71** T20 | 0% | **+85.37 vs yesterday snapshot (+54.3%)** † |
| Rapide-7 (3-28) | **213.47** T19 | 0% | **+54.84 vs yesterday snapshot (+34.6%)** ‡ |
| Bryson (3-46) | **317.36** T20 | **35.8%** | −0.18 (flat); spill Day 3 unchanged |
| Paugan — Gatineau R. (3-65) | **141.02** T19 | 0% | −9.66 (−6.4%) |
| Rapides-Farmers — Gatineau mouth (3-67) | **162.48** T19 | 0% | +0.46 (flat) |
| Carillon — basin terminal (3-60) | **780.80** T20 | 0% | −126.03 (−13.9%) vs yesterday T17 ‡‡ |

† Rapide-2 (3-29) has been running 241–252 m³/s throughout today (all hourly records T15–T20); the transition from yesterday's ~157 m³/s occurred sometime between T16 Nov 3 and T15 Nov 4. These are HQ real-time telemetry values (not provisional daily means); no sanity check required, but the shift is noted as a dispatch change of unknown timing.

‡ Rapide-7 (3-28) ran ~158 m³/s through T17 today, then ramped: T18 182, T19 213 m³/s. Intraday dispatch increase. Bryson headpond flat (105.57 m); no downstream propagation yet.

‡‡ Carillon was at ~960–970 m³/s at T16–T17 today before an active intraday drawdown: T18 956, T19 871, T20 781 m³/s (−189 m³/s over 4 hours). The snapshot-to-snapshot comparison to yesterday's T17 (907) overstates the decline; Carillon was actually *higher* than yesterday's snapshot level earlier today. This is routine dispatch variability for Carillon.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 28) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 4 provisional — ORRPB (m³/s) | **202** *(corrupted — do not headline; see PSPC)* | 322 (Oct 28) | — | *See PSPC cross-check below* |
| Témiscaming Nov 4 — PSPC T00 (m³/s) | **398** *(preferred; D48 in progress, barely sub-400)* | 322 (Oct 28) | +76 | **D48 provisional — 48th straight day sub-400 (barely)** |
| Quinze release → into lake (m³/s) | **209.41** (T20) | ~322 (Oct 28) | — | Baseload; slightly lower week-over-week |
| Mattawa level (m) | **152.27** (Nov 4 ORRPB daily, T00) | ~152.08 (Nov 1) | — | **Daily rise streak ends (3 days Nov 1→3); −8 cm from Nov 3 daily** |
| Pembroke level (m) | **111.00** (Nov 4 ORRPB daily) | ~110.99 (Nov 3) | +1 cm | Essentially flat |

**Provisional sanity check — Témiscaming ORRPB Nov 4 = 202 m³/s:** This triggers the sanity check (−149 m³/s vs Nov 3 final 351 = −42.5%). PSPC T00 cross-check = 398 m³/s. Discrepancy 196 m³/s (well above 50 m³/s threshold). The PSPC T00 reading is the physically consistent value (398 vs 351 = +47, +13.4% — moderate, within range). Floor feasibility at ~22 h into day: (22/24)×202 = 185 m³/s minimum final — inconsistent with the PSPC T00 reading of 398. Conclusion: ORRPB provisional 202 is a data artifact (possibly a corrupted or stale entry). Sanity check FAILED for the ORRPB provisional. Preferred value: **PSPC T00 398 m³/s**. This provisional figure is excluded from TL;DR, plain-language sections, and anomaly flags; reported only in this table.

**Reservoir balance (T00 Nov 3 → T00 Nov 4):**
0 falling · 12 steady · 2 rising (rapide_7 +3 cm, des_joachims +4 cm). Baskatong −2 cm is at the ±2 cm boundary; counted steady. No active retention signal.

**Milestone bookkeeping (W44 rollup anchor Nov 1 + daily extension):**

| Milestone | W44 close (Nov 1) | Nov 2 | Nov 3 | **Nov 4** |
|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 183 | 184 | 185 | **186** |
| Bryson amont above band (104.67 m) | 157 | 158 | 159 | **160** |
| §15.3.5.1 trigger INACTIVE | 160 | 161 | 162 | **163** |
| Témiscaming sub-400 | D45 | D46 ✓ (352) | D47 ✓ (351) | D48? (PSPC 398) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 4.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.24 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 163** (137 cm below trigger; −4 cm vs yesterday T17) |
| Carillon amont (1-2968) | **41.11 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 4.*

| Reservoir | Nov 3 (T00) | Nov 4 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.14 m | **219.12 m** | −2 cm | Steady (at ±2 cm boundary) |
| Témiscaming | 178.59 m | **178.59 m** | 0 cm | Steady |
| Dozois | 342.01 m | **342.01 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.58 m | **313.58 m** | 0 cm | Steady |

All 14 tracked reservoirs: 0 falling · 12 steady · 2 rising (rapide_7 +3 cm, des_joachims +4 cm). No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. Last Update: 2026-11-03 2:09 PM EST (2026-11-03T19:09:00Z UTC). Next Update: 2026-11-10 4:00 PM EST (2026-11-10T21:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief** (Nov 3 update):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to slightly increase or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Témiscaming ORRPB provisional data artifact (Nov 4):** ORRPB `orrpb_river_flows` shows 202 m³/s for Nov 4; PSPC T00 `reservoir_readings` shows 398 m³/s — discrepancy 196 m³/s. Provisional sanity check failed (202 is inconsistent with PSPC T00 and physically implausible as a 22-hour running mean). PSPC preferred at 398. D48 barely sub-400.
2. **Mid-cascade HQ dispatch activity:** Rapide-2 (3-29) running ~242 m³/s all day today (up from ~157 at yesterday's T16 snapshot — shift timing unknown). Rapide-7 (3-28) intraday ramp: 158 → 213 m³/s over T17–T19 today. Neither affects property reach; Bryson headpond flat. Noted for dispatch-pattern record.
3. **Carillon intraday drawdown:** 970 m³/s at T16 → 781 m³/s at T20 (−189 m³/s, −19.5% over 4 hours). Routine dispatch variability; within normal Carillon operating range.

No flood-risk implications. Lac Coulonge etat 0, 115 cm below pre-alert.

---

## Notes

- **Nov 3 D47 Témiscaming retro: final 351 m³/s.** Yesterday's provisional was 358 m³/s (revision −2.0%, well within 50 m³/s tolerance, CONFIRMED). Sub-400 streak extends to D47; D48 provisional via PSPC T00 = 398 m³/s.
- **Mattawa convention note (recurring):** Yesterday's TL;DR reported live T17 reading of 152.49 m (+18 cm), framed as "4th consecutive rise." ORRPB daily Nov 3 finalized at 152.35 m (+11 cm from Nov 2 daily 152.24 m). Direction was correct; the 14 cm discrepancy reflects live-reading vs daily-average convention. Today's ORRPB daily (152.27 m) is based on the T00 midnight snapshot. The brief now consistently uses ORRPB daily series values to avoid this.
- **V3 posterior:** Script ran successfully (exit 0). `freshet-forecast.json` content unchanged from prior commit (asof 2026-06-07). Will update once `lac-coulonge-daily-1990-2026.csv` is extended past the freshet season.
- **Des Joachims reservoir +4 cm overnight** (152.14 → 152.18 m). OPG run-of-river facility, outflow likely underreported (placeholder 205 m³/s vs yesterday 407 m³/s — large OPG flow discrepancy). No anomaly at the river level.
