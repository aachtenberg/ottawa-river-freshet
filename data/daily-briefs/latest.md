# Daily brief — 2026-11-05

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 2495b). ORRPB forecast HTTP 200 ✓ (probed: HTTP 200 / 128722b) — last update Nov 3 2:09 PM EST; next update Nov 10 4:00 PM EST (weekly cadence, unchanged from prior brief). Vigilance 1195: proxy ingest fresh T21 UTC Nov 5 (105.919 m). V3 posterior: ran successfully (exit 0) — `freshet-forecast.json` content unchanged (anchors on asof 2026-06-07; unchanged until `lac-coulonge-daily-1990-2026.csv` is extended).*

*Nov 4 retro-checks: **Nov 4 Témiscaming PSPC provisional 398 → final 358 m³/s** (−40 m³/s, −10.1%, within 50 m³/s tolerance — **CONFIRMED sub-400 D48**). **Nov 4 Mattawa ORRPB daily: claimed 152.27 m in yesterday's brief → finalized 152.36 m (+9 cm revision).** Yesterday's "daily rise streak ends" claim was **INCORRECT** — Nov 4 revised value (152.36 m) exceeds Nov 3 (152.35 m), and the rise continued. **CORRECTION: the Mattawa rise streak did not end on Nov 4; it continued (Nov 3: 152.35 → Nov 4 revised: 152.36 → Nov 5: 152.42 m).** Direction in Nov 4 brief was correct (rising), level was 9 cm off due to data revision before finalization. No flood-state claim affected.*

---

## In plain language

### Upstream — the upper basin

The basin is 187 days past the May 2 seasonal peak and continues in late-autumn recession, with one development worth watching: the outflow from Lake Timiskaming — the large reservoir at the head of the main stem — was measured at 441 cubic metres per second for today (the latest preliminary reading, agreed between the federal monitoring agency and the river planning board). That is 83 cubic metres per second more than yesterday's finalized figure of 358, and it is above the 400 m³/s mark that the system has stayed under for the past 48 days. Because today's reading is based on a full day's data (we are near the end of the calendar day), this is very likely the final tally — the 48-day sub-400 streak almost certainly ends today. The uptick is consistent with the precipitation the ORRPB forecast mentioned; it is not alarming at this scale (normal autumn variability), but worth tracking day-to-day.

Meanwhile, the Mattawa level — an upstream indicator gauge roughly 200 kilometres above Lac Coulonge — edged up to 152.42 metres on today's daily reading, 6 centimetres above yesterday's finalized 152.36 metres. Pembroke, further downstream, dipped slightly to 110.99 metres (down 4 cm from yesterday). All 14 tracked reservoirs are essentially stable; three (Des Joachims, Quinze, and Lady Evelyn) each rose 3–5 centimetres overnight, a minor fluctuation consistent with normal operations.

### At the property — Lac Coulonge / Mansfield

The water at Fort-Coulonge stood at 105.919 metres at 9 PM UTC — up 5 centimetres from the same hour yesterday (105.869 m). The ORRPB daily series puts it at 105.90 metres, up 3 centimetres from yesterday's finalized daily of 105.87 metres. The lake is fully in normal conditions — 108 centimetres below the 107.00-metre pre-alert threshold — with no flood risk. The gentle rise matches the precipitation the weekly forecast anticipated, and nothing in the data suggests a sharp change is coming.

Well downstream, at the Bryson Generating Station (reached via a long, winding channel well below the southern tip of Lac Coulonge and not visible from the Mansfield properties), the spillway volume continued to grow for a fourth consecutive day. Today approximately 145 cubic metres per second is running through the spillway — 41.6% of the total 349 m³/s release — compared to 114 m³/s (35.8%) yesterday. The dam pond held essentially flat at 105.58 metres. Carillon, the basin's terminal dam near Hawkesbury, was releasing around 954 cubic metres per second by 7 PM UTC, having ramped steadily through the afternoon from a morning baseline of about 850 m³/s. This is routine power-dispatch scheduling, not a flood response. The ORRPB forecast (unchanged since November 3; next update November 10) calls for levels to "slightly increase or remain fairly stable depending on location" over the coming week.

---

## TL;DR

**CORRECTION (Mattawa Nov 4):** ORRPB daily Nov 4 revised 152.27 → **152.36 m**; rise streak did not end (Nov 3: 152.35 → Nov 4 revised: 152.36 → Nov 5: 152.42 m — 3rd consecutive rise). **Today (Day 187):** Lac Coulonge T21 **105.919 m** (+5 cm vs T21 yesterday; etat 0, 108 cm below pre-alert). Bryson Day 4 partial spill: **41.6%** (144.94 m³/s, +31.35 / +27.6% vs yesterday — ⚠ exceeds 5% flag). Carillon T19 **954 m³/s** (+173, intraday ramp; dispatch). Témiscaming **D49: ORRPB + PSPC both 441 m³/s** (above 400; floor at 22h ≈ 404 m³/s — sub-400 D48 streak almost certainly ends today; provisional, finalization expected). **RETRO ✓:** Nov 4 Témiscaming PSPC provisional 398 → final **358 m³/s** (−40, within 50 m³/s — CONFIRMED sub-400 D48). Mattawa ORRPB daily **152.42 m** (+6 cm from revised Nov 4 152.36 m). Pembroke **110.99 m** (−4 cm). Hull dock T20 41.24 m — trigger INACTIVE **Day 164**. Reservoir balance: **0 falling · 11 steady · 3 rising** (des_joachims +5 cm, quinze +4 cm, lady_evelyn +3 cm). ORRPB forecast unchanged (Nov 3; next Nov 10).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 5 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 5 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 5) | **105.919 m** |
| ORRPB daily Nov 5 | 105.90 m (provisional from T00) |
| 24h delta (Vigilance T21 Nov 5 vs T21 Nov 4) | **+5 cm** |
| ORRPB daily delta (Nov 4 finalized 105.87 → Nov 5 provisional 105.90) | +3 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 108 cm below |
| Distance to minor flood (107.50 m) | 158 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T20 UTC Nov 5. Yesterday: T20 UTC Nov 4.*

| Metric | Today (T20 Nov 5) | Yesterday (T20 Nov 4) | Δ |
|---|---|---|---|
| Total release (m³/s) | **348.64** | 317.36 | **+31.28 (+9.9%)** ⚠ |
| Turbined (m³/s) | **203.70** | 203.77 | −0.07 (0.0%) |
| Spilled (m³/s) | **144.94** | 113.59 | **+31.35 (+27.6%)** ⚠ |
| Spill share (%) | **41.6%** | 35.8% | **+5.8 pp** ⚠ |
| Headpond / amont (m) | **105.58** (T20) | 105.57 (T20 Nov 4) | +1 cm |
| Tailwater / aval (m) | **86.80** (T20) | 86.73 (T20 Nov 4) | +7 cm |
| Δh (head differential, m) | **18.78** | 18.84 | −6 cm |

Spill in m³/s and total release exceed the 5% flag threshold. Bryson Day 4 of partial spill — spill share growing while headpond holds flat. Headpond 105.58 m = **91 cm above** the 104.67 m band ceiling — **Day 161** above band.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 5. Yesterday comparison: Nov 4 brief T19–T20 snapshot values.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **235.71** T19 | 0% | +10.10 (+4.5%) |
| Quinze (3-31) | **212.02** T19 | 0.4% | +2.61 (flat) |
| Îles (3-32) | **218.41** T19 | 0% | +6.49 (+3.1%) |
| Rapide-2 (3-29) | **241.22** T19 | 0% | −1.49 (flat) |
| Rapide-7 (3-28) | **165.60** T19 | 0% | −47.87 (−22.4%) vs T19 yesterday † |
| Bryson (3-46) | **348.64** T20 | **41.6%** | +31.28 (+9.9%); spill Day 4, growing |
| Paugan — Gatineau R. (3-65) | **140.54** T20 | 0% | −0.48 (flat) |
| Rapides-Farmers — Gatineau mouth (3-67) | **154.93** T19 | 0% | −7.55 (−4.6%) |
| Carillon — basin terminal (3-60) | **953.99** T19 | 0% | +173.19 (+22.2%) vs T20 yesterday ‡ |

† Rapide-7 intraday: T12–T16 ~156 m³/s (steady), T17 147, T18 106 (dispatch dip), T19 165 m³/s. The T19-to-T19 comparison catches the dip from yesterday's ramped value (213 m³/s). Bryson headpond flat (105.58 m); no downstream effect.

‡ Carillon intraday ramp: T12 829 → T13 852 → T14–T17 ~852–856 → T18 904 → T19 954 m³/s. Building steadily throughout the day; this is routine power-dispatch scheduling. No spill.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 29) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 5 provisional — ORRPB (m³/s) | **441** | 324 (Oct 29) | +117 | *Likely ends sub-400 D48 streak — see note* |
| Témiscaming Nov 5 — PSPC T00 cross-check (m³/s) | **441** | 324 (Oct 29) | +117 | *Both sources agree — no discrepancy* |
| Quinze release → into lake (m³/s) | **212.02** (T19) | ~325 (Oct 29) | — | Baseload; slightly lower week-over-week |
| Mattawa level (m) | **152.42** (Nov 5 ORRPB daily) | 152.05 (Oct 29) | +37 cm | **3rd consecutive daily rise (Nov 3: 152.35 → Nov 4 rev: 152.36 → Nov 5: 152.42)** — see CORRECTION above |
| Pembroke level (m) | **110.99** (Nov 5 ORRPB daily) | 111.06 (Oct 29) | −7 cm | Slight dip; essentially flat |

**Sub-400 streak note — Témiscaming Nov 5 = 441 m³/s:** Both ORRPB `orrpb_river_flows` and PSPC `reservoir_readings` T00 agree at 441 m³/s. Change vs Nov 4 final (358 m³/s): +83 m³/s = +23.2%. Below the ≥25% formal sanity-check trigger, but: at ~22h into the calendar day, the feasibility floor = (22/24)×441 = 404 m³/s — still above 400 even under the most pessimistic assumption. The two-source agreement and the level-consistent rise at Lake Timiskaming (178.60 → 178.62 m, +2 cm T00 Nov 4→5, consistent with inflows slightly exceeding outflows at ~440 m³/s) confirm this is a genuine reading. The D48 sub-400 streak very likely ends today; provisional until ORRPB finalizes.

**RETRO — Nov 4 Témiscaming PSPC:** Yesterday's brief reported PSPC T00 = 398 m³/s. Final (now in DB for Nov 4): **358 m³/s** (−40 m³/s, within 50 m³/s tolerance — **CONFIRMED**). D48 sub-400 confirmed at 358 m³/s.

**Reservoir balance (T00 Nov 4 → T00 Nov 5):**
0 falling · 11 steady · 3 rising (des_joachims +5 cm, quinze +4 cm, lady_evelyn +3 cm). No active retention signal (all well below 10 cm/day threshold). Normal late-season operations.

**Milestone bookkeeping (W44 rollup anchor Nov 1 + daily extension):**

| Milestone | W44 close (Nov 1) | Nov 2 | Nov 3 | Nov 4 | **Nov 5** |
|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 183 | 184 | 185 | 186 | **187** |
| Bryson amont above band (104.67 m) | 157 | 158 | 159 | 160 | **161** |
| §15.3.5.1 trigger INACTIVE | 160 | 161 | 162 | 163 | **164** |
| Témiscaming sub-400 | D45 | D46 ✓ (352) | D47 ✓ (351) | D48 ✓ (358, rev from PSPC prov 398) | D49 provisional 441 m³/s — **above 400; streak likely ends at D48** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 5.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.24 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 164** (137 cm below trigger; unchanged) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Nov 5.*

| Reservoir | Nov 4 (T00) | Nov 5 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.12 m | **219.12 m** | 0 cm | Steady |
| Témiscaming | 178.60 m | **178.62 m** | +2 cm | Steady (at ±2 cm boundary); level-consistent with 441 m³/s outflow |
| Dozois | 342.01 m | **342.01 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.57 m | **313.57 m** | 0 cm | Steady |

All 14 tracked reservoirs: 0 falling · 11 steady · 3 rising (des_joachims +5 cm, quinze +4 cm, lady_evelyn +3 cm). No active retention signal.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. Last Update: 2026-11-03 2:09 PM EST (2026-11-03T19:09:00Z UTC). Next Update: 2026-11-10 4:00 PM EST (2026-11-10T21:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief** (Nov 3 update):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. With precipitation forecast over the coming days, water levels and flows are expected to slightly increase or remain fairly stable depending on location over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Bryson spill increase ≥5% threshold:** Spilled m³/s: 113.59 → 144.94 (+31.35, +27.6%); spill share 35.8% → 41.6% (+5.8 pp); total release +9.9%. Day 4 of partial spill with spill share growing. Headpond flat at 105.58 m. No property-reach implication.
2. **Témiscaming Nov 5 provisional = 441 m³/s — sub-400 streak likely ends at D48:** Both ORRPB and PSPC agree at 441; two-source agreement and level consistency confirm genuine reading. Floor at 22h ≈ 404 m³/s. D48 sub-400 streak almost certainly ends today (see upper basin section for full check). Provisional.
3. **Mattawa data-revision correction from yesterday's brief:** Nov 4 ORRPB daily revised from 152.27 → 152.36 m (+9 cm). Yesterday's "daily rise streak ends" claim was incorrect — streak continued through Nov 4 and Nov 5 (3 consecutive rises). No flood-state implication; noted for record accuracy.

No flood-risk implications. Lac Coulonge etat 0, 108 cm below pre-alert.

---

## Notes

- **Nov 4 Témiscaming retro: final 358 m³/s.** Yesterday's PSPC provisional was 398 m³/s (revision −40 m³/s, within 50 m³/s tolerance, CONFIRMED). D48 sub-400 confirmed.
- **Mattawa ORRPB daily convention note:** The Nov 4 value used in yesterday's brief was 152.27 m (from T00 provisional at run time). It finalized at 152.36 m — a +9 cm revision that changed the streak conclusion. This is a recurring source of same-day discrepancy; the ORRPB provisional T00 value used at run time can be revised by the following afternoon's data refresh.
- **Rapide-7 intraday dispatch (3-28):** T18 dipped to 106 m³/s (dispatch reduction), T19 recovered to 165 m³/s, while Carillon simultaneously ramped T18-T19. This appears to be coordinated inter-dam dispatch scheduling. No effect on property reach.
- **V3 posterior:** Script ran successfully (exit 0). `freshet-forecast.json` content unchanged from prior commit (asof 2026-06-07). Will update once `lac-coulonge-daily-1990-2026.csv` is extended past the freshet season.
- **Des Joachims reservoir +5 cm overnight** (152.14 → 152.19 m). Largest single-reservoir rise today; still modest, well below the 10 cm/day active-retention threshold.
