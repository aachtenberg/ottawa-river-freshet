# Daily brief — 2026-05-29

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data note: the cluster proxy now ingests through May 29T19:00 UTC — full day's data available at run time. ORRPB conditions page shows May 29 midnight values. Vigilance 1195 upstream INEDIT API still shows May 27T14:00 as last update, but the proxy `river_readings` table is sourcing from HQ telemetry directly and carries current data through May 29T19:00 UTC (106.60 m). This run supersedes the earlier stub filed at this date.*

---

## In plain language

### Upstream — the upper basin

The northern Ottawa basin continues its orderly retreat from the May 2 spring peak. The flow leaving Lake Temiscaming — the large upper reservoir that acts as the basin's outlet valve — was confirmed at 1,220 cubic metres per second for May 28 by the river authority's tally (roughly 44% of the peak flow of about 2,741 m³/s that arrived 28 days ago). A government cross-check source (Public Services and Procurement Canada) puts the same day's outflow at 1,322 m³/s — a 102-cubic-metre-per-second discrepancy that likely reflects the ORRPB's May 28 figure still being preliminary; previous days' readings resolved to the PSPC figure when ORRPB finalized them. The direction is unambiguous regardless: the upper basin is flowing at roughly half its peak rate and continuing to wind down.

The mid-valley picture is broadly calm. The gauge near Mattawa — where the Ottawa descends from the northern highlands — is essentially flat at 152.91 metres, unchanged from yesterday within measurement precision. Pembroke, roughly halfway between Lake Temiscaming and Lac Coulonge, dropped another 13 centimetres to 111.98 m and has now been falling for at least 12 consecutive days since its May 20 high of 112.75 m.

The most notable operational story in the basin today is at the Des Joachims reservoir (pronounced "Day-Zwahsham"), a mid-valley storage pool operated by Ontario Power Generation between Lake Temiscaming and the property. For the fifth consecutive day, OPG is aggressively storing water rather than passing it downstream: the reservoir level rose 34 centimetres in a single day to 151.63 metres — the largest single-day gain recorded there this season. This is normal post-freshet behaviour (operators rebuild summer storage), and it gently cushions the downstream lake from any residual pulse from the north. It is not a flood concern.

### At the property — Lac Coulonge / Mansfield

The river level at Fort-Coulonge has returned to 106.60 metres as of 7 p.m. Eastern time today — the Hydro-Québec sensor that feeds the provincial monitoring network has been transmitting normally all day, resolving the sensor-reporting gap noted in the past two days' briefs. (The gap was in the Vigilance government web interface, not in the underlying telemetry; HQ data flowed to the cluster database throughout.) The lake has now fallen 9 centimetres since midnight last night, landing at 106.59 m as of midnight, and is 41 centimetres below the pre-alert mark (107.00 m) and 91 centimetres below the minor-flood threshold (107.50 m). No monitoring flags are active.

At the dam at the foot of Lac Coulonge (Bryson Generating Station), today brought a striking reversal of the past week's pattern. The backed-up pond between the lake and the turbines — which had been sitting below its normal range (104.20–104.67 m) for eight days and only returned to the band two days ago — shot up 70 centimetres to 104.92 m. It is now 25 centimetres *above* the upper limit of its normal operating range. The operator cut total releases by about 9% and sharply reduced turbine generation (down 28%), while allowing more water to spill freely (up 19%). The combined effect was a rapid headpond refill. Whether the pond will be drawn back down toward the centre of its operating range in coming days depends on how the operator responds and how quickly the lake level stabilises.

The river authority's weekly bulletin (last updated May 26, next update June 2) remains unchanged: conditions are within seasonal values and expected to stay stable or decrease gradually. For the property owner: the water is going down steadily — about 9 centimetres per day over the past 24 hours — all warning flags are off, and the next milestone is the lake reaching a summer-normal level around 106 m, which appears imminent at current rates.

---

## TL;DR

Lac Coulonge **106.60 m** real-time (proxy May 29T19:00 UTC; sensor-gap RESOLVED — proxy sourcing HQ directly while INEDIT frontend lags); ORRPB midnight May 29 = **106.59 m**, −9 cm from May 28. **Bryson headpond ABOVE upper operating band ← ANOMALY**: 104.92 m (+25 cm above ceiling 104.67 m; entered upper breach after 8-day lower breach resolved); turbined −27.7% ⚠⚠⚠ / spilled +18.6% ⚠ / total −9.4% ⚠ / spill share +12.2 pp. **Rapide-2 spill% +18 pp** (27.4%→45.4%) with flat total. Carillon +1.6% (2,930→2,975 m³/s); Carillon amont +32 cm (40.67→40.99 m). Hull dock 42.27 m → §15.3.5.1 INACTIVE Day 4. **Des Joachims Day 5 accumulation: +34 cm ← largest single-day gain of 2026 season** (now 151.63 m); only 1 reservoir >10 cm/day (flag threshold = 2+, not triggered). Temiscaming **1,220 m³/s** (ORRPB May 28 finalized) / **1,322 m³/s** (PSPC cross-check) → **102 m³/s discrepancy ⚠** (above 50 m³/s flag). **28 days past May 2 peak (~2,741); Day 9 sub-2,000; Day 7 sub-1,500; Day 4 sub-1,400; Day 2 sub-1,300.** Sub-1,000 ETA: ~May 31–June 1 at current pace. Mattawa 152.91 m (flat, +1 cm). Pembroke 111.98 m (−13 cm, 12th+ consecutive day of decline). Reservoir balance: 4 rising · 3 steady · 4 falling (Des Joachims dominant). ORRPB forecast unchanged (May 26 bulletin, weekly mode, next update June 2).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Sources: proxy `river_readings` station 1195 (sourcing HQ telemetry; live through May 29T19:00 UTC); ORRPB `lake-coulonge` station (midnight series, from conditions page); Vigilance metadata (thresholds). Vigilance upstream INEDIT API (`station_details_metadata_api`, `station_details_readings_api`) still reflects May 27T14:00 UTC as last update — INEDIT frontend lag only; proxy confirmed live (see guardrail below).*

| Metric | Value |
|---|---|
| Real-time level (proxy `river_readings`, May 29T19:00 UTC) | **106.5955 m ≈ 106.60 m** |
| 24h delta (ORRPB midnight May 28→29) | **−9 cm** |
| ORRPB midnight May 29 | 106.59 m |
| ORRPB midnight May 28 | 106.68 m |
| Flood state (Vigilance `etat_niv`) | **etat 0 — fully normal** (no threshold exceeded) |
| Distance to pre-alert (107.0 m) | −41 cm below |
| Distance to minor flood (107.5 m) | −91 cm below |
| Distance to moderate flood (108.0 m) | −141 cm below |

**Guardrail verification (sensor gap status):**
Proxy probe: HTTP 200, 286 bytes — live, contains May 29T19:00 UTC reading (106.5955 m).
Upstream Vigilance INEDIT probe: HTTP 200, 1,508 bytes — live, but buffer shows readings only through May 27T14:00 UTC = 106.785 m.
**Conclusion:** The upstream INEDIT web API is lagging, but the proxy is sourcing from HQ telemetry directly and has current data. The sensor itself is transmitting; the gap was in the INEDIT frontend. No outage language warranted.

**ORRPB midnight level series (recent):**

| Date | Level (m) | Midnight Δ | Notes |
|---|---|---|---|
| May 22 | 107.53 | −10 cm | |
| May 23 | 107.35 | −18 cm | |
| May 24 | 107.13 | −22 cm | |
| May 25 | 106.98 | −15 cm | |
| May 26 | 106.91 | −7 cm | |
| May 27 | 106.77 | −14 cm | |
| May 28 | 106.68 | −9 cm | |
| **May 29** | **106.59** | **−9 cm** | From ORRPB conditions page (May 29); proxy real-time 106.60 at 19:00 UTC consistent |

---

## Bryson operating posture (HQ open-data via cluster proxy)

*Source: proxy `dam_releases` (site 3-46, May 29T19:00 UTC) and `dam_levels` (stations 1-2964 amont, 1-2965 aval, May 29T19:00 UTC). "Yesterday" = May 28T18:00 UTC (from prior brief).*

| Metric | Today (May 29T19:00) | Yesterday (May 28T18:00) | Δ |
|---|---|---|---|
| Total release (m³/s) | 592.59 | 654.40 | **−61.81 (−9.4% ⚠)** |
| Turbined (m³/s) | 286.90 | 396.67 | **−109.77 (−27.7% ⚠⚠⚠)** |
| Spilled (m³/s) | 305.68 | 257.73 | **+47.95 (+18.6% ⚠)** |
| Spill share (%) | 51.6% | 39.4% | **+12.2 pp ⚠** |
| Headpond / amont (m) | **104.92** | 104.22 | **+70 cm ← ABOVE UPPER BAND LIMIT** |
| Tailwater / aval (m) | 87.84 | 88.08 | −24 cm |
| Δh (head differential, m) | **17.08** | 16.14 | +0.94 m |

**Headpond operating band (104.20–104.67 m):** At 104.92 m, the headpond is **25 cm above the upper bound** — a new breach on the high side. Context: the headpond had been below the lower bound (104.20 m) for 8 consecutive days (May 21–28), bottoming at 103.90 m on May 27 evening. It re-entered the band on May 28 (+2 cm above floor at 104.22 m). Today the aggressive reduction in total release (−61 m³/s) and turbining (−110 m³/s) caused rapid forebay refill, overshooting the upper limit.

**All four flag thresholds exceeded**: total −9.4% ⚠, turbined −27.7% ⚠⚠⚠, spilled +18.6% ⚠, spill share +12.2 pp ⚠.

**Updated headpond series:**

| Date | Headpond (m) | vs. band (104.20–104.67 m) |
|---|---|---|
| May 21 | 104.16 | −4 cm below floor (breach begins) |
| May 25 | 103.94 | −26 cm below floor (deepest) |
| May 27 23:00 UTC | 103.90 | −30 cm below floor (worst point) |
| May 28 19:00 UTC | 104.22 | +2 cm — breach ends, re-enters band |
| **May 29 19:00 UTC** | **104.92** | **+25 cm above ceiling — new upper breach** |

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: proxy `dam_releases`, May 29T18:00–19:00 UTC. "Yesterday" = May 28T18:00–19:00 UTC (prior brief). Spill % = spilled / total.*

| Site | Total (m³/s) | Spill % | Vs yesterday Δ% | Note |
|---|---|---|---|---|
| Première-Chute (3-33) | 760.1 | 45.8% | −3.0% | |
| Quinze (3-31) | 718.6 | 37.3% | **−6.0% ⚠** | |
| Îles (3-32) | 802.0 | 53.5% | −5.0% | |
| Rapide-2 (3-29) | 455.0 | 45.4% | ~0.0% total | **Spill% +18 pp ⚠ (was 27.4%)** |
| Rapide-7 (3-28) | 438.8 | 23.2% | flat | |
| Bryson (3-46) | 592.6 | 51.6% | **−9.4% ⚠** | See Bryson table above |
| Paugan — Gatineau R. (3-65) | 621.7 | 17.3% | **−8.9% ⚠** | |
| Rapides-Farmers — Gatineau mouth (3-67) | 619.8 | 23.9% | **−8.6% ⚠** | |
| Carillon — basin terminal (3-60) | 2,975.1 | 15.1% | +1.6% | Headpond rising (+32 cm); Hull dock declining |

**Cascade notes:**

- **Upper Ottawa (Première-Chute through Rapide-7):** Generally declining 3–6%, within the broad recession signal. **Rapide-2 exception**: total release is essentially unchanged (455.0 vs 455.4 m³/s), but spill share jumped 18 percentage points (27.4%→45.4%), implying a turbine → spillway rebalancing with near-constant total throughput. This is a significant intra-site operational shift.
- **Bryson −9.4% ⚠ / turbined −27.7% ⚠⚠⚠ / spilled +18.6% ⚠ / spill share +12.2 pp ⚠:** The operator dramatically shifted the composition away from turbines toward spilling. The headpond's 70 cm rise (+25 cm into upper breach) is the direct result of the reduced total outflow.
- **Gatineau (Paugan / Rapides-Farmers):** Both declining ~8–9% ⚠. Continued post-peak Gatineau recession.
- **Carillon +1.6%:** Near-flat after yesterday's massive −21.9% cut. Carillon headpond continued rising (+32 cm to 40.99 m/41.00 m) because upstream inflow still exceeds the release set point post-cut. Hull dock continuing slow decline (−2 cm to 42.27 m).

**ORRPB average daily flows (May 29 preliminary from conditions page vs May 28 finalized):**

| Station | May 28 (m³/s) | May 29 (m³/s) | Δ |
|---|---|---|---|
| Otto Holden | 968 | **1,237** | **+269 (+27.8% ⚠)** — reversal of yesterday's −29.4% cut |
| Des Joachims | 1,433 | 1,217 | −216 (−15.1%) |
| Chenaux | 1,935 | 1,859 | −76 |
| Chats Falls | 2,213 | 2,078 | −135 |
| Britannia | 2,280 | 2,190 | −90 |
| Carillon | 2,916 | 2,947 | +31 |

Temiscaming flow not yet in the May 29 ORRPB daily table at run time.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: proxy `orrpb_river_flows` (Temiscaming May 28 finalized = 1,220 m³/s; May 22 = 1,574 m³/s); proxy `reservoir_readings` (timiskaming PSPC, May 28 flow = 1,322 m³/s); ORRPB conditions page river table (May 29 midnight values for Mattawa, Pembroke, Lake Coulonge); proxy `orrpb_river_levels` (for May 28 comparison). "7 d ago" anchored to May 22 (7 days before May 29).*

| Metric | Today (May 28 confirmed / May 29 preliminary) | 7 d ago (May 22) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming outflow — ORRPB (m³/s) | **1,220** (May 28 finalized; May 29 daily n/a yet) | 1,574 | −354 (−22%) | **28 days past May 2 peak (~2,741); Day 9 sub-2,000; Day 7 sub-1,500; Day 4 sub-1,400; Day 2 sub-1,300. 55% below peak. Sub-1,000 ETA: ~May 31–June 1 at ~107 m³/s/day decline.** |
| Témiscaming outflow — PSPC cross-check (m³/s) | **1,322** (May 28, `reservoir_readings` PSPC) | — | — | **⚠ 102 m³/s discrepancy vs ORRPB May 28 (above 50 m³/s flag). May 27 both agreed at 1,327. Likely ORRPB May 28 will revise upward. Prefer PSPC 1,322 for "today."** |
| Quinze release → into the lake (m³/s) | 718.6 (May 29T18:00, proxy) | ~770 | −51 | Modest decline; upper-basin HQ cascade continuing recession |
| Mattawa level (m) | 152.91 (ORRPB midnight May 29) | 153.04 | −13 cm | Essentially flat (+1 cm from May 28 midnight 152.90 m). Broadly declining from 153.74 m May 20 high; Des Joachims storage moderating signal. |
| Pembroke level (m) | 111.98 (ORRPB midnight May 29) | 112.51 | −53 cm | **−13 cm day-over-day; 12th+ consecutive day of decline from 112.75 m May 20 high.** Direction only — no flood threshold in this table. |

**ORRPB flows (May 29 preliminary, partial — Temiscaming not yet published):**

All stations continuing to decline except Carillon (+1%) and Otto Holden (+28% — OPG operational rebalancing, see above table).

**Reservoir balance (May 28→29, using ORRPB conditions page for May 29 / proxy for May 28):**

| Reservoir | May 28 (m) | May 29 (m) | Δ | Direction |
|---|---|---|---|---|
| Des Joachims | 151.29 | **151.63** | **+34 cm** | **Rising ⚠ — Day 5 accumulation; largest single-day gain this season** |
| Mitchinamecus | 381.01 | 381.07 | +6 cm | Rising |
| Timiskaming Haileybury (WSC) | 179.07 | ~179.10 | +3 cm | Rising |
| Cabonga | 360.42 | 360.45 | +3 cm | Rising |
| Bark Lake | 313.71 | 313.72 | +1 cm | Steady |
| Lady Evelyn | 289.18 | 289.17 | −1 cm | Steady |
| Kipawa | 269.50 | 269.49 | −1 cm | Steady |
| Dozois | 345.51 | 345.48 | −3 cm | Falling |
| Rapide-7 | 309.01 | 308.98 | −3 cm | Falling |
| Quinze | 263.09 | 263.05 | −4 cm | Falling |
| Baskatong | 221.81 | 221.76 | −5 cm | Falling |

**Balance (±2 cm = steady, 11 reservoirs with May 29 data): 4 rising · 3 steady · 4 falling.** Shift toward more falling/rising vs yesterday's 3/10/1. Active basin-wide retention flag (2+ reservoirs >10 cm/day): **not triggered** — only Des Joachims (+34 cm) exceeds the threshold; all others below 10 cm/day.

**Milestone bookkeeping:**

| Milestone | Date first crossed | Day count today (May 29) |
|---|---|---|
| Freshet peak (~2,741 m³/s) | ~May 2 | 28 days ago |
| Sub-2,000 | May 21 | Day 9 |
| Sub-1,500 | May 23 | Day 7 |
| Sub-1,400 | May 26 (1,352 m³/s finalized) | Day 4 |
| Sub-1,300 | May 28 (1,220 m³/s ORRPB / 1,322 PSPC) | Day 2 |
| Sub-1,000 (forecast) | ~May 31–June 1 | — |

*Note: sub-1,300 Day 1 is May 28 per ORRPB (1,220 m³/s). PSPC cross-check (1,322) does not yet confirm sub-1,300. If ORRPB May 28 revises upward toward 1,322, sub-1,300 Day 1 would shift to May 29 (once the May 29 ORRPB daily is published and expected near ~1,100–1,200 m³/s).*

---

## Carillon §15.3.5.1 directive check

*Source: proxy `dam_levels` (station 1-2968 Carillon amont, station 1-3675 Hull dock, May 29T19:00 UTC). ORRPB conditions table cross-check (midnight May 29).*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (1-3675, May 29T19:00 UTC) | **42.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 4** (34 cm below threshold) |
| Hull dock (ORRPB midnight May 29) | 42.26 m | — | Cross-confirms; −5 cm from May 28 (42.31 m) |
| Hull dock delta vs yesterday | −2 cm (42.29→42.27 m) | — | Continued slow decline |
| Carillon amont (1-2968, May 29T19:00 UTC) | **40.99 m** | 40.08 m spring-flood ceiling (active when Hull > 42.61) | **Ceiling NOT in effect — trigger inactive** |
| Carillon amont (ORRPB midnight May 29) | 41.00 m | — | Cross-confirms |
| Carillon amont delta vs yesterday | **+32 cm** (40.67→40.99) | — | Headpond continuing to fill post-cut |

The §15.3.5.1 monitoring period closed on May 26 (Day 22 of trigger activation). The Hull dock has been below 42.61 m for four consecutive days. The spring-flood ceiling at Carillon (40.08 m) is not in effect. For the record: Carillon amont is now 40.99–41.00 m — 91 cm above the now-inactive ceiling.

**Main-stem level snapshot (ORRPB conditions page, May 28→29 midnight):**

| Station | May 28 (m) | May 29 (m) | Δ |
|---|---|---|---|
| Otto Holden GS | 177.09 | 177.24 | **+15 cm** (OPG storing) |
| Mattawa | 152.90 | 152.91 | +1 cm (flat) |
| Des Joachims GS | 151.31 | 151.63 | **+32 cm** (OPG Day 5 storage) |
| Pembroke | 112.11 | 111.98 | −13 cm |
| Lake Coulonge | 106.68 | 106.59 | −9 cm |
| Chenaux GS | 86.23 | 86.01 | −22 cm |
| Chats Falls | 74.27 | 74.16 | −11 cm |
| Britannia | 59.00 | 58.93 | −7 cm |
| Hull/Gatineau | 42.31 | 42.26 | −5 cm |
| Thurso | 41.43 | 41.55 | +12 cm (Carillon backwater) |
| Grenville | 41.16 | 41.35 | +19 cm (Carillon backwater) |
| Carillon GS | 40.61 | 41.00 | **+39 cm** (headpond filling) |

---

## Reservoir storage (latest_reservoir_readings)

*Source: proxy `latest_reservoir_readings` (rows dated 2026-05-28T00:00 UTC — within 48 h of run time, not stale). Day-over-day delta computed using ORRPB conditions reservoir page (May 29) for May 29 levels vs proxy May 28 values.*

| Reservoir | May 28 (m) | May 29 (m, ORRPB) | Δ | Agency | Notes |
|---|---|---|---|---|---|
| Baskatong | 221.81 | 221.76 | −5 cm | HQ | Modest drawdown; outflow ~469 m³/s (ORRPB page) |
| Timiskaming (PSPC) | 179.04 | ~179.06 | ~+2 cm | PSPC | Slight rise; outflow 1,322 m³/s (PSPC cross-check) |
| Dozois | 345.51 | 345.48 | −3 cm | HQ | Slight drawdown; outflow 357 m³/s |
| Bark Lake | 313.71 | 313.72 | +1 cm | OPG | Stable; outflow 39 m³/s |

Active basin-wide retention flag (2+ reservoirs rising >10 cm/day): **not triggered.** Baskatong is falling slightly; Timiskaming is nearly flat. Des Joachims (not in this top-4 list) is the dominant storage event at +34 cm/day.

---

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. **Last Update: 2026-05-26 3:35 PM EDT** (19:35 UTC). **Next Update: 2026-06-02 4:00 PM EDT** (20:00 UTC Jun 2). Fetched at 22:00 UTC May 29. Cadence: weekly (7-day gap). Mode: weekly-notice.*

**Unchanged from prior brief** (May 26 bulletin; next scheduled update June 2, 2026):

> *Flows and water levels along the main stem of the Ottawa River are within seasonal values for this time of year, and are expected to remain stable or decrease gradually over the coming week depending on location.*

No further increases flagged. No precipitation or flood-watch language. No new climate or window-record claim to test.

---

## Anomaly flags

1. **Bryson headpond breaches UPPER operating band (104.67 m ceiling) ← ANOMALY:** 104.92 m at May 29T19:00 UTC, +25 cm above the upper bound. This follows an 8-day lower-bound breach (May 21–28). The headpond swung 70 cm in one day (104.22→104.92 m) driven by a large turbine reduction (−27.7% ⚠⚠⚠, −110 m³/s) and total release cut (−9.4% ⚠). Spilled increased +18.6% ⚠ and spill share rose +12.2 pp ⚠. All four metrics exceed the 5% flag threshold.

2. **Rapide-2 spill share +18 pp ⚠ (27.4%→45.4%) at flat total:** Upper-Ottawa site redirected flow from turbines to spillway while holding total release essentially constant (~455 m³/s). Not a 0%→high spill event, but an 18 pp intraday operational shift is significant.

3. **Des Joachims Day 5 accumulation — largest single-day rise this season:** +34 cm (151.29→151.63 m). Exceeds the 10 cm/day individual threshold, but no second reservoir is also >10 cm (flag requires 2+; not triggered). OPG operational storage; not a flood concern.

4. **PSPC / ORRPB Temiscaming discrepancy for May 28:** PSPC outflow (`reservoir_readings`) = 1,322 m³/s; ORRPB Temiscaming daily (`orrpb_river_flows`) = 1,220 m³/s. Discrepancy = **102 m³/s ⚠** (above 50 m³/s flag). May 27 both agreed at 1,327. Consistent with ORRPB May 28 still being preliminary; expect revision toward PSPC when ORRPB finalizes. Prefer PSPC (1,322 m³/s) as the "today" Temiscaming value.

5. **Otto Holden +27.8% ⚠** (968→1,237 m³/s, ORRPB May 29 daily): Reversal of yesterday's −29.4% cut. OPG continuing short-cycle storage/release management.

6. **Vigilance 1195 upstream INEDIT API lag (not a sensor outage):** INEDIT `station_details_metadata_api` still shows May 27T14:00 as last update. However, guardrail probe confirms both proxy (200/286b, contains May 29T19:00 UTC data) and upstream INEDIT (200/1,508b) are live. Proxy is sourcing from HQ telemetry directly. Sensor is transmitting; INEDIT frontend is lagging. No outage language warranted.

7. **Carillon §15.3.5.1 trigger INACTIVE Day 4.** Hull dock 42.27 m (34 cm below 42.61 m trigger). Ceiling not in effect. Carillon amont 40.99 m — 91 cm above the now-inactive ceiling, and continuing to rise (+32 cm today).

---

## Notes

- **Bryson headpond whipsaw:** The headpond has swung from −30 cm below the lower bound (May 27 night) to +25 cm above the upper bound (May 29 evening) in just 48 hours — a 55 cm total swing through the 47 cm band. This rapid oscillation is unusual and may indicate the operator is struggling to find the right release equilibrium as Lac Coulonge settles toward summer-normal inflow. The case file's operating posture analysis may find this period noteworthy: both the 8-day lower breach and the rapid upper overshoot happened within a 10-day window. Watch whether the headpond is drawn back toward the band centre in coming days, or continues oscillating.

- **Pembroke 12th consecutive decline day:** From 112.75 m on May 20 to 111.98 m today = −77 cm over 9 days. Direction only (no threshold data for Pembroke in the ORRPB levels table), but the trend clearly confirms the recession propagating through the mid-valley.

- **Chenaux −22 cm:** A larger-than-typical single-day drop at Chenaux GS (86.23→86.01 m). This is downstream of Des Joachims and Rapide-2, and may reflect OPG's routing decisions as well as Chats Falls management. Worth monitoring.

- **Carillon headpond rising toward notable levels:** At 41.00 m (midnight May 29) and climbing (+32-39 cm per day), the Carillon headpond is approaching territory where, if the Hull dock were also to rise above 42.61 m, the §15.3.5.1 ceiling (40.08 m) would become binding. The Hull dock is currently declining (42.26–42.27 m, −5 cm/day) and 34 cm below the trigger, so this is not an immediate concern. But the rapid headpond rise is worth tracking.

- **Sub-1,000 Temiscaming timing:** The May 27→28 decline was 107 m³/s/day (1,327→1,220). At that pace from 1,220 m³/s, sub-1,000 arrives in ~2 days (May 30–31). The PSPC cross-check (1,322) implies a possibly higher starting point, pushing the ETA to ~June 1. Both estimates are consistent with the prior brief's "~June 1" call.

- **Proxy data lag resolved:** The prior brief noted the proxy was ~27 hours behind run time (topping out at May 28T19:00 UTC for a 22:00 UTC May 29 run). Today the proxy has data through May 29T19:00 UTC — only 3 hours behind run time. The ingester has caught up; no health check needed.
