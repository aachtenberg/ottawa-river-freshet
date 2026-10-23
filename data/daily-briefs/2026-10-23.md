# Daily brief — 2026-10-23

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **last updated Oct 20 3:46 PM EDT**, next update Oct 27. Vigilance 1195: proxy ingest fresh T20 UTC Oct 23 (105.980 m). V3 posterior: exit 143, Day 50 consecutive timeout; `freshet-forecast.json` updated with current run timestamp, forecast content unchanged.*

*Oct 22 retro-checks: **Oct 22 Des Joachims provisional 842 m³/s → final 404 m³/s** — exclusion confirmed correct ✓. **Oct 22 Chenaux provisional 725 m³/s → final 467 m³/s** — exclusion confirmed correct ✓. Both exclusions right call; finals in normal range.*

---

## In plain language

### Upstream — the upper basin

The basin is 174 days past the May 2 seasonal peak. Most of the reach continues a quiet late-autumn recession, but there is one notable development: the Lake Timiskaming control structure (operated by Public Services and Procurement Canada) posted a provisional daily release of 477 cubic metres per second for today — up from yesterday's finalized 378, a jump of 26%. This is a PSPC-managed outflow, not a natural river flood wave, and the mass balance is physically plausible if PSPC chose to ramp up releases. All four standard sanity checks pass or are inconclusive (no check fails), so the provisional figure is reported in the data tables below; it will confirm or revise overnight. If it finalizes above 400 m³/s, the 35-day sub-400 release streak that has held since September 18 would be broken. That would be an operational decision, not a basin anomaly.

Mattawa ticked up 3 centimetres to 152.32 metres — consistent with the rising Temiscaming outflows of the past week arriving at the mid-valley gauge. Pembroke eased 1 centimetre to 111.05 metres, remaining solidly in normal seasonal range. All fourteen tracked reservoirs are essentially flat today, with every one landing within 2 centimetres of yesterday — an unusually quiet day across the entire storage network.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge rose 1 centimetre to 105.98 metres — the same incremental uptick seen the past two days, and still 102 centimetres below the 107.00-metre pre-alert threshold. Nothing is happening at the property.

The dam pond at the Bryson Generating Station — located well downstream from the property reach, at the end of Lac Coulonge's long, winding southern outlet — was essentially unchanged. Release, turbined flow, spill, and headpond level were all flat within measurement noise. The ORRPB forecast remains unchanged from Tuesday's update: stable or slightly decreasing flows through the coming week. Next update October 27.

---

## TL;DR

**RETRO ✓:** Oct 22 DJ=842 provisional → final 404; Chenaux=725 → 467. Both exclusions correct. **Today:** Lac Coulonge **+1 cm** to **105.98 m (etat 0; 102 cm below pre-alert)**. Bryson flat: total −0.2% (323→322 m³/s), headpond **−1 cm** to **105.56 m (Day 148 above band)**. Hull dock T19 41.28 m — trigger INACTIVE **Day 151**. Carillon ORRPB provisional 941 m³/s. Oct 23 DJ=837 provisional EXCLUDED (fails checks 3, 4); Chenaux=721 EXCLUDED (fails check 4). Témiscaming Oct 23 provisional **477 m³/s (+26%)** — all sanity checks pass/inconclusive; if finalizes >400, ends **sub-400 streak at D35**. Day **174** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 23 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 23 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 23) | **105.980 m** |
| ORRPB daily Oct 23 | 105.98 m |
| 24h delta (ORRPB daily Oct 22→23) | **+1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 102 cm below |
| Distance to minor flood (107.50 m) | 152 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 23. Yesterday: T19 UTC Oct 22.*

| Metric | Today (T19 Oct 23) | Yesterday (T19 Oct 22) | Δ |
|---|---|---|---|
| Total release (m³/s) | **322.33** | 322.99 | −0.66 (−0.2%) |
| Turbined (m³/s) | **297.50** | 298.14 | −0.64 (−0.2%) |
| Spilled (m³/s) | **24.83** | 24.85 | −0.02 (−0.1%) |
| Spill share (%) | **7.7%** | 7.7% | 0 pp |
| Headpond / amont (m) | **105.56** | 105.57 | −1 cm |
| Tailwater / aval (m) | **86.86** | 86.85 | +1 cm |
| Δh (head differential, m) | **18.70** | 18.72 | −2 cm |

No threshold breaches. All changes well below the 5% flag threshold. **Headpond band status:** 105.56 m is 89 cm above the 104.67 m band ceiling — **Day 148** above band (ongoing status).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T18–T19 UTC Oct 23. Yesterday comparison: T18–T19 UTC Oct 22.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **209.54** T18 | 0% | −122 (−37%) |
| Quinze (3-31) | **209.03** T19 | 0.5% | −23 (−10%) |
| Îles (3-32) | **210.67** T19 | 0% | −85 (−29%) |
| Rapide-2 (3-29) | **157.62** T18 | 0% | −0.2 (flat) |
| Rapide-7 (3-28) | **156.83** T19 | 0% | +0.3 (flat) |
| Bryson (3-46) | **322.33** T19 | 7.7% | −1 (flat) |
| Paugan — Gatineau R. (3-65) | **161.71** T19 | 0% | flat |
| Rapides-Farmers — Gatineau mouth (3-67) | **181.34** T19 | 0% | +3 (+1.5%) |
| Carillon — basin terminal (3-60) | **817.34** T19 | 0% | −201 (−20%) |

Première-Chute, Quinze, and Îles returning to baseload (~210 m³/s each) after yesterday's afternoon dispatch ramp — expected cascade transit. Carillon T19=817 vs yesterday T19=1018: intraday dispatch variation (ORRPB Oct 23 partial-day running mean = 941 m³/s, down from Oct 22 final 999); not a river-level event.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 16) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 23 PSPC provisional (m³/s) | **477** *(provisional — sanity checks pass/inconclusive; see Notes)* | 334 (Oct 16) | +143 | **D35 confirmed (Oct 22=378 sub-400); D36 in progress — provisional 477 > 400, streak continuation at risk** |
| Timiskaming PSPC cross-check Oct 23 T00 (m³/s) | 178.77 m / no flow yet | — | level −2 cm | Oct 22 reservoir_readings flow=378 ✓ (matches ORRPB); Oct 23 T00 no PSPC flow yet |
| Quinze release → into the lake (m³/s) | **209.03** (T19) | ~334 (Oct 16) | — | Declining from Oct 16 peak dispatch |
| Mattawa level (m) | **152.32** (Oct 23 daily) | 152.14 (Oct 16) | +18 cm | +3 cm from Oct 22 (152.29); rising trend Oct 18–23 (152.17→152.32) |
| Pembroke level (m) | **111.05** (Oct 23 daily) | 111.11 (Oct 16) | −6 cm | Direction: −1 cm from Oct 22 (111.06); gradual drift |

**Reservoir balance (T00 Oct 22 → T00 Oct 23):**
All 14 tracked reservoirs within ±2 cm today. baskatong 0 · kipawa 0 · rapide_7 0 = **3 steady** · bark_lake −1 · cabonga −1 · dozois −1 · lady_evelyn −1 · quinze −1 = **5 steady** · des_joachims −2 · kiamika −2 · mitchinamecus −2 · timiskaming −2 · timiskaming_haileybury −2 = **5 steady** · poisson_blanc +2 = **1 steady**. **0 falling · 14 steady · 0 rising.** An unusually flat day across the entire storage network; consistent with late-autumn equilibrium.

**Milestone bookkeeping (W42 anchor Oct 18 + Oct 19–23 extension):**

| Milestone | W42 close (Oct 18) | Oct 19 | Oct 20 | Oct 21 | Oct 22 | **Oct 23** |
|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 169 | 170 | 171 | 172 | 173 | **174** |
| Bryson amont above band (104.67 m) | 143 | 144 | 145 | 146 | 147 | **148** |
| §15.3.5.1 trigger INACTIVE | 146 | 147 | 148 | 149 | 150 | **151** |
| Témiscaming sub-400 | D31 (295) | D32 (307) | D33 (312) | D34 (335) | D35 (378 ✓) | D36? (477 prov.) |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 23.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.28 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 151** (133 cm below trigger; +1 cm from Oct 22) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. Hull dock and Carillon amont both flat.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 23.*

| Reservoir | Oct 22 (T00) | Oct 23 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.43 m | **219.43 m** | 0 cm | Steady |
| Témiscaming | 178.79 m | **178.77 m** | −2 cm | Slight decline; consistent with Oct 22 PSPC outflow=378 vs inflow ~270 |
| Dozois | 342.31 m | **342.30 m** | −1 cm | Steady decline |
| Bark Lake (OPG) | 313.78 m | **313.77 m** | −1 cm | Steady decline |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-20 3:46 PM EDT** (2026-10-20T19:46:00Z UTC). **Next Update: 2026-10-27 4:00 PM EDT** (2026-10-27T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false. Mode: `weekly-notice`.

---

## Anomaly flags

1. **Oct 22 provisional exclusions confirmed correct (retro):** Des Joachims 842 → final 404 (normal range, +0.5% from Oct 21 final 406). Chenaux 725 → final 467 (flat vs Oct 21 final 468). Both exclusions validated.

2. **Oct 23 Des Joachims provisional 837 m³/s EXCLUDED (mandatory sanity check).** Oct 22 final = 404 m³/s → +107% change ≥ 25%, triggers full check. Check 1: floor = (22/24)×837 = 766 m³/s; recent finals 361–406 — floor nearly double any recent final. Check 3 FAIL: Des Joachims pool T00 Oct 23 = 152.10 m (only −2 cm); net outflow of 837−~410 = 427 m³/s over 24h would require 427×86,400/(40×10⁶)×100 ≈ 924 cm pool drop — physically impossible vs −2 cm measured. Check 4 FAIL: Chats Falls Oct 23 = 575 m³/s (flat vs Oct 22 = 575); a real 837 m³/s through Des Joachims would move Chats Falls within hours. Raw value reported in data table only.

3. **Oct 23 Chenaux provisional 721 m³/s EXCLUDED (mandatory sanity check).** Oct 22 final = 467 → +54% ≥ 25%. Check 4 FAIL: Chats Falls Oct 23 = 575 (flat vs Oct 22 = 575); Chenaux-to-Chats-Falls transit is hours. Raw value excluded from headlines.

4. **Témiscaming Oct 23 provisional 477 m³/s (+26% from Oct 22 final 378).** Check 1: floor = (22/24)×477 = 437 m³/s — plausible for PSPC-controlled dam. Check 2: INCONCLUSIVE — Quinze ~209 m³/s + tributaries ~80 m³/s = ~290 inflow; net outflow ~187 m³/s implying ~6 cm lake-level drop not yet observable (T00 comparison measures yesterday's balance). Check 3 PASS — Oct 22 balance self-consistent (−2 cm at lake, net outflow ~90 m³/s with 378 PSPC, inflow ~270). Check 4 INCONCLUSIVE — Mattawa +3 cm consistent with multi-day rising trend, not specifically diagnostic of today's value. No check fails. Reported in data tables provisionally. If Oct 23 finalizes >400, sub-400 streak ends at D35.

None flagged beyond above.

---

## Notes

- **Oct 23 mid-valley sanity checks:** Des Joachims 837 and Chenaux 721 provisional values excluded per mandatory checks. Same artifact mechanism as prior days (partial-day running means). Otto Holden Oct 23 provisional = 412 (+7% from Oct 22 final 385) — below 25% threshold, reported without exclusion.
- **Carillon dispatch Oct 23:** T19 = 817 m³/s (−20% vs yesterday T19 = 1018). ORRPB Oct 23 partial-day running mean = 941. Intraday operational variation; not a river-level event.
- **V3 posterior:** Day 50 consecutive timeout (exit 143). `freshet-forecast.json` updated with Oct 23 run timestamp; forecast content unchanged.
- **Detached HEAD status:** Repo on branch main, up to date — no detached HEAD this session.
