# Daily brief — 2026-05-16

*Generated automatically at 22:06 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

## In plain language

The lake at Fort-Coulonge and Mansfield dropped about 2 centimetres today — from 107.72 metres to 107.70 metres — still in minor flood, but the pace of recession has doubled compared to yesterday's near-standstill of 1 centimetre per day. Water is now sitting 20 centimetres above the level where it's officially considered a minor flood, compared to 22 centimetres yesterday. More encouragingly, the gauge at Mattawa — the main northern feed point into the Ottawa River — dropped 11 centimetres overnight, its sharpest single-day decline in the current monitoring period. When water recedes that fast at Mattawa, it typically works its way past the property gauge in about 3–5 days and adds further momentum to the recession already underway.

The dam at the foot of Lac Coulonge (Bryson, operated by Hydro-Québec) made a modest but noticeable adjustment today: operators pulled back their total release by about 15 cubic metres per second (roughly 1.4%), while the dam's own pond rose 11 centimetres — from barely inside its normal operating range yesterday to comfortably within it today at 104.32 metres. That headpond recovery is a small but positive sign for storage management. The share of water going through the spillway rather than the turbines held essentially steady at about 78%.

The river management board's forecast has not been updated since Thursday afternoon, May 15, and the next bulletin is not expected until Tuesday, May 19 — the board signalled last update that it considers the acute phase of the freshet behind us. The standing forecast projects "fairly stable" conditions for the next few days, with a gradual decline expected later next week. No further rises or rain events are flagged.

For property owners: the trend has turned slightly more positive today — recession has picked up to roughly 2 centimetres per day, and the northern basin is clearing faster than it has at any point in this event. If that pace holds and no new rain arrives, the property could exit minor flood (107.50 metres) in roughly 10 days from now. The basin's terminal dam (Carillon, near Grenville, Quebec) remains in a regulatory zone it is not supposed to occupy during spring floods — now for 12 consecutive days — but its headpond is slowly working lower alongside the declining river.

## TL;DR

Recession accelerating: Lac Coulonge −2 cm/day (up from −1 cm yesterday); Mattawa −11 cm is the sharpest single-day drop in the series — positive upstream signal. Bryson reduced releases by 1.4% while headpond recovered 11 cm to 104.32 m (back into the comfortable middle of the operating band). Carillon §15.3.5.1 overshoot Day 12 continues at 42 cm (40.50 m vs 40.08 m ceiling); Hull dock 42.91 m = 30 cm above trigger, down 4 cm. ORRPB forecast unchanged — next update May 19. No site in cascade exceeds 5% change flag.

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: cluster proxy `river_readings` station 1195. Latest: 2026-05-16T20:00 UTC. 24h comparison: 2026-05-15T19:00 UTC. ORRPB live reading from conditions/?display=river page (15:00 UTC May 16).*

| Metric | Value |
|---|---|
| Current level (proxy, 20:00 UTC) | 107.703 m |
| ORRPB live reading (15:00 UTC May 16) | 107.70 m |
| Yesterday (proxy, 19:00 UTC May 15) | 107.722 m |
| 24h delta (proxy) | −2.0 cm |
| Flood state | etat 4 — minor flood |
| Distance above minor threshold (107.500 m) | +20 cm |
| Distance below moderate threshold (108.000 m) | −30 cm |
| Distance below major threshold (108.500 m) | −80 cm |

**Recession trend (ORRPB midnight and live series):**

| Date | Level (m) | Midnight / live Δ | Notes |
|---|---|---|---|
| May 8 | 108.01 | −9 cm | peak recession rate |
| May 9 | 107.92 | −9 cm | peak recession rate |
| May 10 | 107.86 | −6 cm | slowdown begins |
| May 11 | 107.81 | −5 cm | |
| May 12 | 107.77 | −4 cm | |
| May 13 | 107.74 | −3 cm | rain arrives |
| May 14 | 107.73 | −1 cm | stall |
| May 15 | 107.72 | −1 cm | stall; ORRPB drops secondary-rise warning |
| **May 16** | **107.70** | **−2 cm (proxy)** | **recession picking back up** |

Recession rate recovering from the 1 cm/day stall. Proxy and ORRPB live are consistent. Mattawa (154.03 m today, down from 154.14 m at May 15 midnight) signals the northern basin is clearing rapidly — the strongest single-day northern-basin decline in the current event.

## Bryson operating posture (HQ open-data via cluster proxy)

*Source: proxy `dam_releases` (site 3-46) and `dam_levels` (stations 1-2964 amont, 1-2965 aval). Today = 2026-05-16T19:00 UTC. Yesterday = 2026-05-15T19:00 UTC (confirmed from proxy; consistent with May 15 brief).*

| Metric | Today | Yesterday | Δ |
|---|---|---|---|
| Total release (m³/s) | 1,075.6 | 1,090.82 | −15.2 (−1.4%) |
| Turbined (m³/s) | 238.71 | 237.72 | +1.0 (+0.4%) |
| Spilled (m³/s) | 836.89 | ~853.10 | −16.2 (−1.9%) |
| Spill share (%) | 77.8% | 78.2% | −0.4 pp |
| Headpond / amont (m) | 104.32 | 104.21 | **+11 cm** |
| Tailwater / aval (m) | 89.01 | 89.05 | −4 cm |
| Δh (head differential, m) | 15.31 | 15.16 | +0.15 m |

**Headpond operating band (104.20–104.67 m):** Headpond at 104.32 m is 12 cm above the lower bound — recovered from the bottom-edge position of 1 cm above floor that persisted for three days. No band breach; the rise of 11 cm moves the headpond comfortably into the middle of the 47-cm band. No individual flow series exceeds the 5% change flag threshold. The combination of reduced release (−1.4%) and headpond rise (+11 cm) indicates operators modestly curtailed output while inflows held steady or fractionally increased, allowing the headpond to recover.

*Note on spilled for yesterday: `spilled_cms` was null at 19:00 UTC May 15 in the proxy; computed as total − turbined = 1090.82 − 237.72 = 853.10 m³/s, consistent with the 18:00 UTC spilled value of 852.72.*

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: proxy `dam_releases`. Today = latest per site (19:00 UTC May 16, except Rapides-Farmers which is 18:00 UTC). Yesterday = 19:00 UTC May 15 (from May 15 brief). Rapide-7 spill % computed from 18:00 UTC (spilled_cms null at 19:00).*

| Site | Total today | Total yest. | Δ% | Spill % today | Spill % yest. |
|---|---|---|---|---|---|
| Première-Chute (3-33) | 1,028.25 | 1,031.91 | −0.4% | 56.9% | 57.3% |
| Quinze (3-31) | 971.54 | 975.78 | −0.4% | 58.1% | 58.3% |
| Îles (3-32) | 1,082.96 | 1,086.93 | −0.4% | 54.2% | 54.0% |
| Rapide-2 (3-29) | 416.44 | 418.00 | −0.4% | 20.8% | 20.9% |
| Rapide-7 (3-28) | 382.67 | 381.98 | +0.2% | ~11.5%* | 11.4% |
| Bryson (3-46) | 1,075.6 | 1,090.82 | −1.4% | 77.8% | 78.2% |
| Paugan — Gatineau R. (3-65) | 534.34 | 547.45 | **−2.4%** | 0.0% | 0.0% |
| Rapides-Farmers — Gatineau (3-67) | 543.49 | 547.44 | −0.7% | 13.0% | 13.6% |
| Carillon — basin terminal (3-60) | 4,545.8 | 4,569.11 | −0.5% | 35.1% | 35.4% |

*\* Rapide-7 spilled_cms null at 19:00 UTC; spill % from 18:00 reading (43.78/381.98).*

**Cascade notes:**

- **No site exceeds the 5% change flag threshold.** Basin-wide output is uniformly down 0.4–1.4%, reflecting a broad, steady recession rather than any deliberate operational shift.
- **Paugan (3-65) −2.4%:** The largest relative drop today, though still below the 5% flag. Paugan remains at 0% spill (all turbined); the drop reflects declining Gatineau River inflows.
- **Upper cascade uniform −0.4%:** Première-Chute, Quinze, Îles, and Rapide-2 all declined exactly 0.4% — a tight cluster suggesting the upper-basin forcing is uniform and natural (snowmelt recession).
- **Carillon (3-60) −0.5%:** Basin-terminal release continuing gradual decline. Spill share 35.1% (−0.3 pp).

## Carillon §15.3.5.1 directive check

*Source: proxy `dam_levels` (station 1-2968 Carillon amont, station 1-3675 Hull dock). Today = 2026-05-16T19:00 UTC. Yesterday = 2026-05-15T19:00 UTC. ORRPB live reads: Carillon 40.5 m at 15:00 UTC, Hull (Gatineau) 42.91 m at 15:00 UTC — consistent with proxy.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (1-3675, proxy 19:00 UTC May 16) | 42.91 m | 42.61 m servitude | **ABOVE — trigger active** (+30 cm) |
| Hull dock delta vs yesterday (proxy) | −4 cm (42.95 → 42.91 m) | — | Modest improvement |
| Carillon amont (1-2968, proxy 19:00 UTC May 16) | 40.50 m | 40.08 m spring-flood ceiling | **OVERSHOOT — 42 cm above ceiling ⚠** |
| Carillon amont delta vs yesterday (proxy) | +1 cm (40.49 → 40.50 m) | — | Essentially flat |

The IWMP §15.3.5.1 spring-flood operating ceiling of 40.08 m remains formally in effect at Carillon (Hull dock 30 cm above the 42.61 m servitude trigger). **Day 12** of directive exceedance.

The overshoot is effectively unchanged from yesterday (41 cm yesterday proxy → 42 cm today proxy). The +1 cm is within instrument noise. Hull dock is declining (−4 cm today) which is a positive signal; when Hull falls to 42.61 m the spring-flood ceiling no longer formally applies.

**Updated Carillon overshoot series (proxy live readings at 19:00 UTC):**

| Date | Level (proxy) | Overshoot vs 40.08 m |
|---|---|---|
| May 6 | 40.50 | 42 cm |
| May 7 | 40.51 | 43 cm |
| May 8 | 40.51 | 43 cm |
| May 9 | 40.51 | 43 cm |
| May 10 | 40.52 | **44 cm — peak** |
| May 11 | 40.51 | 43 cm |
| May 12 | 40.50 | 42 cm |
| May 13 | 40.43 | 35 cm — rapid improvement |
| May 14 | 40.51 | 43 cm — rain-driven reversal |
| May 15 | 40.49 | 41 cm |
| **May 16** | **40.50** | **42 cm — plateau** |

Headpond remains locked in the 41–43 cm range. Resolution depends on upstream inflows declining further; Mattawa's sharp −11 cm drop today is a positive upstream signal.

*See `docs/analysis/Freshet_2026_Complete_Summary.md` § "The Carillon directive enforcement gap" for regulatory context.*

## Reservoir storage (ORRPB conditions/?display=reservoir, May 16)

*Source: ORRPB reservoir page (fetched 22:06 UTC May 16); readings shown at 15:00 UTC May 16 except Bark Lake (00:00 UTC May 16). Day-over-day delta vs ORRPB May 15 values from prior brief. Proxy `latest_reservoir_readings` is stale (timestamps all 2026-05-15T00:00 UTC, ~46 h old); ORRPB reservoir page used as primary for today's values.*

| Reservoir | Level (May 16, ORRPB) | Level (May 15, prior brief) | Δ | Agency |
|---|---|---|---|---|
| Baskatong | 221.54 m | 221.48 m | +6 cm | HQ |
| Dozois | 345.26 m | 345.19 m | +7 cm | HQ |
| Cabonga | 360.26 m | 360.24 m | +2 cm | HQ |
| Bark Lake | 313.80 m | 313.78 m | +2 cm | OPG |

All four continue slow refill. None approach the 10 cm/day flag threshold; active-retention flag not triggered. Baskatong (+6 cm) and Dozois (+7 cm) are the fastest-filling reservoirs, consistent with ongoing but moderating inflows from snowmelt. The basin is absorbing rather than fully passing inflow — a normal post-peak refill posture.

*Note: proxy `latest_reservoir_readings` still shows May 15T00:00 values (~46 h old). Within the 48-hour staleness window but borderline. ORRPB page today confirmed consistent higher values.*

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. **Last Update: 2026-05-15 3:18 PM EDT** (19:18 UTC). **Next Update: 2026-05-19 4:00 PM EDT** (20:00 UTC). Fetched at 22:06 UTC May 16.*

**Unchanged from May 15 brief.** The ORRPB has not issued a new bulletin today; the forecast page still shows the May 15 3:18 PM text. The next update is not expected until May 19 4:00 PM EDT. ORRPB sections in the May 16, 17, and 18 briefs will reference this standing forecast.

Current standing forecast text (verbatim, unchanged from May 15):

> *Spring runoff in the northern part of the basin is slowly receding but remains high. Along the main stem of the Ottawa River, the decline in water levels and flows has slowed down in all locations due to recent rainfall and continued large volumes of water from the north. Over the next few days, water levels are expected to be fairly stable in all locations, remaining near of slightly below minor flood levels from Mattawa to Lake Deschenes. Later next week, levels and flows are expected to decrease in all locations at a rate that will depend on amount of rainfall in northern part of the basin.*

**ORRPB live readings from conditions/?display=river (today, for reference — these are live gauge values, not the midnight-series table which is published at forecast updates):**

| Location | May 16 (live) | May 15 (midnight) | Δ |
|---|---|---|---|
| Mattawa | 154.03 m (14:00 UTC) | 154.14 m | **−11 cm ← sharpest drop in series** |
| Des Joachims GS | 150.51 m (15:00 UTC) | 150.52 m | −1 cm |
| Pembroke | 112.75 m (13:00 UTC) | 112.79 m | −4 cm |
| Fort-Coulonge | 107.70 m (15:00 UTC) | 107.72 m | −2 cm |
| Chenaux GS | 86.10 m (15:00 UTC) | 86.11 m | −1 cm (plateauing) |
| Britannia (Ottawa) | 59.48 m (14:00 UTC) | 59.48 m | 0 cm |
| Gatineau / Hull | 42.91 m (15:00 UTC) | 42.96 m | −5 cm |
| Grenville | 41.40 m (15:00 UTC) | 41.42 m | −2 cm |
| Carillon GS | 40.50 m (15:00 UTC) | 40.51 m | −1 cm |

Notable: Mattawa −11 cm is the sharpest single-day decline in the current monitoring period, far exceeding the −7 cm on May 15. Gatineau/Hull −5 cm (accelerating from −2 cm). Pembroke −4 cm (accelerating from −1 cm). Chenaux GS appears to be plateauing after rising consistently since May 7. These are the strongest basin-wide recession signals since the May 12–13 period.

## Anomaly flags

1. **Carillon §15.3.5.1 directive overshoot — Day 12 (continued) ⚠:** Hull dock 42.91 m (trigger active, +30 cm above 42.61 m servitude). Carillon amont 40.50 m = 42 cm above the 40.08 m spring-flood ceiling. Improvement is negligible (proxy day-over-day: +1 cm in headpond, −4 cm in Hull). Hull dock decline is the most meaningful leading indicator for when the trigger deactivates.

2. **Mattawa −11 cm today — strongest upstream recession signal yet ⚠ (positive):** The northern basin feed point dropped 11 cm in a single day (154.14 → 154.03 m), surpassing the previous maximum of 9 cm/day recorded on May 8–9. If this pace holds, the downstream pulse should reach Fort-Coulonge in approximately 3–5 days and could lift the property's recession rate from the current ~2 cm/day to ~3–5 cm/day.

3. **Bryson headpond +11 cm to 104.32 m:** Not a band breach, but the headpond moved from the bottom edge of the operating band (1 cm clearance) to a comfortable 12 cm above the lower bound. Operators appear to have deliberately reduced total release by 1.4%, allowing the headpond to recover. Worth tracking — if release reduction continues or deepens, it could slightly reduce downstream flow contribution.

4. **Proxy `latest_reservoir_readings` borderline stale (46 h):** All reservoir timestamps show 2026-05-15T00:00 UTC. Still within the 48-hour window specified in the brief template, but only by ~2 hours. ORRPB reservoir page values used as primary for today's table.

None triggered: Bryson >5% change in any flow series, headpond band breach, 2+ reservoirs >10 cm/day, cascade site >5% change, ORRPB forecast update, ORRPB precipitation/climate claim.

## Notes

- **What the upstream Mattawa signal means:** A −11 cm day at Mattawa, 350+ km upstream, is a leading indicator that the northern snowmelt pulse has now substantially cleared. That water travels the main stem at approximately 1–2 metres/second on average, meaning a 3–5 day lag is typical before the signal reaches Fort-Coulonge. Watch for an acceleration in the property's recession rate by May 19–21.

- **Chenaux GS beginning to plateau:** The mid-basin pool between Des Joachims and Carillon (86.10 m today, vs. a consistent multi-day rise since 85.70 m on May 8) appears to be flattening. This pool has been slowly filling for over a week, maintaining headpond pressure at Carillon. If it begins declining, Carillon headpond should follow within 1–2 days.

- **ORRPB live readings vs midnight table:** The "Water levels at 24:00h" series published by ORRPB reflects midnight Eastern readings updated at each forecast bulletin. Since no bulletin was issued today, those series are not updated. The live gauge readings extracted from the ORRPB river page are partial-day snapshots (13:00–15:00 UTC) and will differ from tomorrow's midnight values. They are useful for directional reads only.

- **Forecast cadence note:** With the next ORRPB update on May 19, this brief and the May 17 and May 18 briefs will carry the standing May 15 forecast. The proxy hourly data remains the primary monitoring source during this window.
