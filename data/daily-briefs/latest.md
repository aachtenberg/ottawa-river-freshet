# Daily brief — 2026-11-11

*Generated automatically at 23:09 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 112b). ORRPB forecast HTTP 200 ✓ (probed: HTTP 200 / 128625b) — last update Nov 10 2:19 PM EST; next update Nov 17 4:00 PM EST (weekly cadence). Vigilance 1195: proxy ingest fresh T21 UTC Nov 11 (106.011 m). V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged until `lac-coulonge-daily-1990-2026.csv` is extended).*

*Nov 10 retros: Témiscaming Nov 10 provisional (ORRPB daily 344 / PSPC T00 424 → DB finalized PSPC **383 m³/s**; D54 sub-400 **CONFIRMED** — the PSPC/ORRPB discrepancy flag correctly resolved as measurement-timing difference, not an anomaly; no corrections required). Mattawa Nov 10: headlined 152.33 m (ORRPB daily provisional) → DB finalized **152.34 m** (Δ = +1 cm, within ±5 cm tolerance; **CONFIRMED**).*

---

## In plain language

### Upstream — the upper basin

The basin is 193 days past the spring peak and continues a quiet late-autumn recession. The outflow from Lake Timiskaming — the large lake at the top of the Ottawa watershed — came in at 419 cubic metres per second today as a provisional daily figure, up from yesterday's finalized 383 cubic metres per second. That uptick nudges the running total above the 400 cubic-metre-per-second round number, though the final average for the full day has not been settled yet and could land on either side of 400 when it closes out at midnight. This is a moderate fluctuation on a river that has been running below 400 for most of the past two months, and no abrupt change.

Mid-valley gauges confirm the quiet picture. Water levels at Mattawa — roughly 200 kilometres upstream of the properties — held essentially flat at 152.33 metres, essentially unchanged from the finalized figure of 152.34 metres for the day before (a correction from the 152.33 m headlined in yesterday's brief). Pembroke, further downstream, edged down 4 centimetres to 111.07 metres. Among the basin's tracked reservoirs, one fell slightly (the Des Joachims pool, down 4 cm), twelve held steady, and one rose slightly (Poisson Blanc, up 4 cm). There is no active water-retention signal anywhere in the upper basin.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge stood at 106.011 metres at 9 PM UTC — up about 1 centimetre from the same hour yesterday. That is fully in normal conditions: 99 centimetres below the pre-alert threshold and 149 centimetres below the minor-flood mark. The ORRPB's weekly forecast, last updated Monday afternoon at 2:19 PM Eastern time, is unchanged: "Water levels and flows are expected to remain fairly stable over the coming week." The next scheduled update is a week from now, on November 17.

Downstream at the Bryson Generating Station — the facility reached via a long winding channel well below the southern end of Lac Coulonge, not visible from the Mansfield/Fort-Coulonge shoreline — the turbines remain offline for a third consecutive day, with the full flow continuing to pass through the spillway. Total flow through the dam is running at about 392 cubic metres per second — essentially the same volume as during the partial-spill period last week. The routing through the spillway rather than the turbines has no flood implications for the property; the amount of water reaching the river below is unchanged, and the lake is 99 centimetres below any flood threshold. At Carillon, the basin's terminal dam, today's late-afternoon reading was about 904 cubic metres per second — a 7 percent jump from yesterday, all through the turbines with no spillway involvement.

---

## TL;DR

*Nov 10 retros: Témiscaming D54 final **383 m³/s** (sub-400 CONFIRMED; provisional D54 open resolved). Mattawa Nov 10 final **152.34 m** (+1 cm vs brief; CONFIRMED).* **Today (Day 193):** Lac Coulonge T21 **106.011 m** (+1 cm vs T21 yesterday; etat 0, 99 cm below pre-alert). Bryson Day 3 100% spill: total **391.69 m³/s** (+0.6%), turbined **0**, spilled 391.69 m³/s, headpond **105.58 m** (+1 cm; Day 167 above band). §15.3.5.1 trigger INACTIVE **Day 170** (Hull 41.25 m). Carillon T19 **903.83 m³/s** (+57 m³/s / +6.7% vs yesterday, all turbined, 0% spill) ⚠ dispatch jump. Témiscaming D55 provisional **419 m³/s** (PSPC; above 400 — streak status open; floor at T23 ≈ 400 m³/s, finalization uncertain). Mattawa **152.33 m** (−1 cm vs Nov 10 finalized 152.34 m — flat). Pembroke **111.07 m** (−4 cm). Reservoir balance: **1 falling · 12 steady · 1 rising** (poisson_blanc +4 cm). ORRPB forecast unchanged.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 11 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 11 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 11) | **106.011 m** |
| ORRPB daily Nov 11 (provisional) | 106.01 m |
| ORRPB daily Nov 10 (finalized) | 106.00 m |
| 24h delta (Vigilance T21 Nov 11 vs T21 Nov 10) | **+1 cm** (106.011 vs 106.000 m) |
| ORRPB daily delta (Nov 10 final 106.00 → Nov 11 prov 106.01) | +1 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 99 cm below |
| Distance to minor flood (107.50 m) | 149 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Nov 11 (releases), T20 UTC Nov 11 (levels). Yesterday: T19 Nov 10 (releases), T21 Nov 10 (levels).*

| Metric | Today (T19 Nov 11) | Yesterday (T19 Nov 10) | Δ |
|---|---|---|---|
| Total release (m³/s) | **391.69** | 389.43 | +2.26 (+0.6%) |
| Turbined (m³/s) | **0** | 0 | 0 (Day 3 offline) |
| Spilled (m³/s) | **391.69** | 389.43 | +2.26 (+0.6%) |
| Spill share (%) | **100%** | 100% | 0 pp |
| Headpond / amont (m) | **105.58** (T20) | 105.57 (T21 Nov 10) | +1 cm |
| Tailwater / aval (m) | **87.06** (T20) | 87.07 (T21 Nov 10) | −1 cm |
| Δh (head differential, m) | **18.52** | 18.50 | +2 cm |

Day 3 of 100% spillway routing — no change in posture. Headpond 105.58 m = **91 cm above** the 104.67 m band ceiling (Day 167 above band). No values changed >5%. All normal.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 11.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **255.28** T20 | 0% |
| Quinze (3-31) | **251.62** T19 | 0.3% |
| Îles (3-32) | **250.38** T19 | 0% |
| Rapide-2 (3-29) | **157.18** T20 | 0% |
| Rapide-7 (3-28) | **154.54** T20 | 0% |
| Bryson (3-46) | **391.69** T19 | **100%** (Day 3 turbines offline) |
| Paugan — Gatineau R. (3-65) | **165.01** T20 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **175.92** T20 | 0% |
| Carillon — basin terminal (3-60) | **903.83** T19 | 0% ⚠ (+57 / +6.7% vs yesterday) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 4) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 11 provisional — PSPC (m³/s) | **419** | 356 (Nov 4) | +63 | D55 provisional above 400 — streak open (D54 final 383 = sub-400 confirmed); see note |
| Témiscaming Nov 11 — PSPC reservoir cross-check (m³/s) | **419** | — | — | Level 178.64 m (flat vs yesterday 178.64 m); PSPC outflow = PSPC reservoir flow, consistent |
| Quinze release → into lake (m³/s) | **251.62** (T19) | — | — | Steady baseload |
| Mattawa level (m) | **152.33** (Nov 11 prov) | 152.16 (Nov 4) | +17 cm | Flat vs Nov 10 finalized 152.34 m (−1 cm) — essentially steady |
| Pembroke level (m) | **111.07** (Nov 11 prov) | 111.07 (Nov 4) | 0 cm | Direction: declining (−4 cm vs Nov 10 finalized 111.11 m); direction only |

**Témiscaming D55 provisional note:** PSPC daily average for Nov 11 = 419 m³/s (above 400). Change vs D54 finalized (383 m³/s): +36 m³/s = +9.4% — below the 25%/150 m³/s mandatory-guardrail thresholds; no enhanced sanity check required. Floor at T23 (23/24 × 419 ≈ 401 m³/s) — the minimum possible final even if flows ceased for the remaining hour. This is essentially AT the 400 m³/s threshold; the finalization could realistically go either side of 400. Streak status open until PSPC finalizes Nov 11.

**Retro — Témiscaming Nov 10:** Yesterday's TL;DR headlined "D54 provisional open — ORRPB daily 344 / PSPC T00 424." Today's DB shows Nov 10 finalized PSPC = **383 m³/s** (sub-400). D54 CONFIRMED. The PSPC/ORRPB discrepancy was correctly identified as a measurement-timing difference, not a supply anomaly. No corrections required.

**Reservoir balance (T00 Nov 11 vs T00 Nov 10):**

| Reservoir | Nov 10 | Nov 11 | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.25 m | 219.26 m | +1 cm | Steady |
| Dozois | 342.06 m | 342.07 m | +1 cm | Steady |
| Témiscaming | 178.64 m | 178.64 m | 0 cm | Steady |
| Bark Lake | 313.57 m | 313.57 m | 0 cm | Steady |
| Des Joachims | 152.12 m | 152.08 m | −4 cm | Falling |
| Poisson Blanc | 199.98 m | 200.02 m | +4 cm | Rising |
| Others (8) | — | — | 0 to +2 cm | Steady |

**Balance: 1 falling · 12 steady · 1 rising** (poisson_blanc +4 cm). Normal late-season posture; no active retention signal (all well below 10 cm/day threshold).

**Milestone bookkeeping (W45 rollup anchor Nov 8 + 3 days via DB):**

| Milestone | W45 close (Nov 8) | Nov 9 | Nov 10 | **Nov 11** |
|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 190 | 191 | 192 | **193** |
| Bryson amont above band (104.67 m) | 164 | 165 | 166 | **167** |
| §15.3.5.1 trigger INACTIVE | 167 | 168 | 169 | **170** |
| Témiscaming sub-400 streak | D52 (376) | D53 (382) | D54 (383 — confirmed) | **D55 prov 419 — open** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 11.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.25 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 170** (136 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 11.*

| Reservoir | Nov 10 (T00) | Nov 11 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.25 m | **219.26 m** | +1 cm | Steady |
| Témiscaming | 178.64 m | **178.64 m** | 0 cm | Steady (consistent with PSPC outflow 419 from large lake) |
| Dozois | 342.06 m | **342.07 m** | +1 cm | Steady |
| Bark Lake (OPG) | 313.57 m | **313.57 m** | 0 cm | Steady |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓ (probed: HTTP 200 / 128625b). Last Update: **2026-11-10 2:19 PM EST** (2026-11-10T19:19:00Z UTC). Next Update: 2026-11-17 4:00 PM EST (2026-11-17T21:00:00Z UTC). Cadence: weekly.*

**Unchanged from yesterday's brief** (last update remains Nov 10 2:19 PM ET):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Water levels and flows are expected to remain fairly stable over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Bryson Day 3 of 100% spillway routing (ongoing status).** Turbines have been offline since Nov 9 T12–T17 UTC. Total release unchanged (~390–392 m³/s). No flood implications. Watch for turbine restoration.
2. ⚠ **Carillon T19: +56.94 m³/s / +6.73%** (903.83 vs 846.89 m³/s yesterday). Above the 5% change threshold. All turbined, 0% spill — a generation dispatch adjustment. No flood implications. Single-hour snapshot; check tomorrow for persistence.
3. **Témiscaming D55 provisional 419 m³/s (above 400 — streak open).** Change vs D54 final (+36 m³/s = +9.4%) is below mandatory-guardrail thresholds. Floor at T23 ≈ 401 m³/s. Streak status will be resolved on finalization; watch tomorrow's DB.

None of the above have flood-risk implications. Lac Coulonge etat 0, 99 cm below pre-alert.

---

## Notes

- **Carillon dispatch:** The 7% uptick in Carillon generation today (847→904 m³/s) is consistent with normal daily dispatch management at the terminal dam. Carillon routinely modulates output for grid demand; this is not a supply-driven event (inflows have not changed materially). No cascade-wide spill change.
- **Témiscaming D55:** The floor calculation at T23 (23/24 × 419 ≈ 401 m³/s) is essentially at the threshold — the final can realistically land just below or just above 400 m³/s. Tomorrow's retro will resolve the streak count. If D55 finalizes above 400 m³/s, the sub-400 streak ends at D54 (Nov 10, 383 m³/s).
- **Mattawa Nov 11 provisional:** Today's figure (152.33 m) is marginally below Nov 10 finalized (152.34 m). The Nov 10 brief noted a +27 cm uptick (from 152.06 to 152.34) attributed to a precipitation response. The plateau/slight decline today is consistent with that pulse passing through.
- **V3 posterior CSV stale:** Script runs (exit 0) but anchors on asof 2026-06-07. `freshet-forecast.json` regenerated without change.

---

## HQ capture table addendum (Nov 11)

*Extends W45 rollup table. Per-day single-hour max/min from `dam_levels` for the case-file level series. T20 UTC Nov 11.*

| Date | Bryson amont 1-2964 (m) | Carillon amont 1-2968 (m) | Hull dock 1-3675 (m) |
|---|---|---|---|
| 2026-11-11 | 105.58 (T20) | 41.12 (T20) | 41.25 (T20) |

Bryson amont 105.58 m = 91 cm above 104.67 m ceiling. Hull max ≤41.25 m (trigger 42.61 m; 136 cm clearance). No threshold breach.
