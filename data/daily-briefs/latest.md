# Daily brief — 2026-05-30

*Generated automatically at 22:15 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data note: Cluster proxy (freshet.xgrunt.com) is healthy today — HTTP 200 confirmed (contrast yesterday's backfill which ran against an HTTP 530 proxy outage). All dam releases and levels sourced from proxy (HQ telemetry). ORRPB conditions page used for May 30 daily flows and midnight levels (proxy ingests ORRPB daily data with a ~12–24 h lag, so the proxy's `orrpb_river_flows` and `orrpb_river_levels` tables top out at May 29 midnight; today's values taken directly from ottawariver.ca). Important data quality correction: the proxy table `orrpb_river_flows` carries an erroneous value `temiscaming 2026-05-29 = 1493`, which is actually the Des Joachims May 30 figure incorrectly labelled; the correct ORRPB/PSPC finalized value for Temiscaming May 29 is 1,207 m³/s (confirmed on the ORRPB conditions page). This error caused yesterday's backfill to misreport the Sub-1,250 milestone as May 30 (Day 1); the corrected milestone is May 29 (Day 1). Today (May 30) is **Sub-1,250 Day 2** and **Sub-1,200 Day 1 (new)**.*

---

## In plain language

### Upstream — the upper basin

The Ottawa River's upper basin is now 29 days into its post-peak recession, and the retreat is deepening into its quieter second phase. The flow leaving Lake Temiscaming — the large upper reservoir at the Quebec-Ontario border that acts as the basin's outlet valve — has fallen to roughly 1,200 cubic metres per second on a preliminary basis today. That is the first time this season the flow has dropped below 1,200 — a meaningful milestone given that the river was running at nearly 2,750 at its May 2 spring peak. Put another way, the Temiscaming outflow is now running at less than 45% of peak flow and still declining, though the pace of decline has slowed considerably compared to early in the recession.

The most significant story in the upper basin today is at the Des Joachims reservoir, a large mid-valley storage pool operated by Ontario Power Generation (OPG) on the Ontario side between Lake Temiscaming and the property. For seven straight days, OPG has been actively storing water rather than passing it downstream — the reservoir level rose more than 1.2 metres over that span. Today, OPG opened the gates substantially: preliminary flows through Des Joachims jumped from roughly 1,200 cubic metres per second yesterday to about 1,490 today, an increase of nearly 24%. This pulse of roughly 290 extra cubic metres per second is now propagating downstream. It should arrive near the Pembroke gauge area in one to two days and reach the Lac Coulonge area (the property) in roughly two to three days. At the lake's current level — more than half a metre below the first warning threshold — this pulse poses no flood risk, but it will likely slow the rate of lake decline for a few days.

The gauge at Mattawa, roughly halfway between Lake Temiscaming and the property, has now risen 11 centimetres for the second consecutive day, reaching 153.02 metres. This is the expected lagged response to elevated releases from the OPG dams upstream. Pembroke, further downstream, is still falling (9 centimetres lower today), confirming that the broader recession remains intact.

### At the property — Lac Coulonge / Mansfield

The river at Fort-Coulonge stood at 106.45 metres as of midnight last night, 14 centimetres lower than the night before. The automated sensor in the river (maintained by Hydro-Québec) confirms a level of 106.48 metres this morning at 9 a.m. Eastern time, consistent with continued slow decline. All warning flags are off: the lake is now 55 centimetres below the pre-alert mark (107.00 metres) and more than a metre below the minor-flood threshold (107.50 metres). The summer-normal level around 106 metres is close at hand.

The dam at the foot of Lac Coulonge — Bryson Generating Station — remains in an unusual operating posture for the second consecutive day. The backed-up pond between the lake and the turbines (known as the headpond) is still sitting 31 centimetres above the top of its normal 47-centimetre operating range. Normal is between 104.20 and 104.67 metres; the headpond today was 104.98 metres. The operator has continued to cut turbine generation sharply (down 19% from the previous day) and has also reduced total releases (down 7%), but the headpond has continued drifting upward, now for a second day — though the pace of rise has slowed markedly (6 centimetres today versus 70 centimetres the day before). The operator appears to be making progress toward restoring equilibrium. The incoming Des Joachims pulse arriving in 2–3 days may briefly add inflow pressure to the pond before conditions stabilise.

At the basin's downstream end, the Carillon dam sharply increased its spillway flow today (up 40%) while adding only modestly to total releases (+5%). The regulatory monitoring trigger — which was active for 22 days in April and May and requires the Carillon headpond to stay below 40.08 metres when the Hull dock gauge exceeds 42.61 metres — remains inactive: the Hull dock at 42.27 metres has been 34 centimetres below the trigger threshold for five consecutive days. The ORRPB weekly forecast (unchanged since May 26, next update June 2) calls for conditions "within seasonal values…expected to remain stable or decrease gradually."

---

## TL;DR

Lac Coulonge **106.45 m** midnight May 30 (ORRPB) / **106.48 m** live at 14:00 UTC (proxy station 1195); −14 cm overnight; etat 0 (fully normal, 55 cm below pre-alert). **Bryson headpond upper breach Day 2**: 104.98 m, +31 cm above 104.67 ceiling; turbined −18.7% ⚠⚠⚠ / total −7.3% ⚠ / spill share +5.9 pp ⚠ — rise decelerating (+6 cm today vs +70 cm Day 1). **Carillon spill +40.5% ⚠⚠⚠** (448→630 m³/s); total +4.7%; Hull dock 42.27 m → §15.3.5.1 INACTIVE Day 5. **Temiscaming (PSPC) 1,199 m³/s — Sub-1,200 Day 1 (NEW)**; backfill milestone error corrected (sub-1,250 Day 1 was May 29, not May 30; today = Day 2). Day 29 since May 2 peak (~2,741 m³/s). Sub-1,000 ETA ~June 5–10 at current pace. **Des Joachims SURGE +23.9%** (1,205→1,493 m³/s): Day 7 storage ends; 290 m³/s extra pulse propagating downstream; expect Pembroke tick-up ~June 1, Lac Coulonge recession deceleration ~June 2. Mattawa +11 cm (153.02 m) Day 2 reversal; Pembroke −9 cm (111.90 m, 13th+ consecutive decline day). Reservoir: **2 rising · 10 steady · 2 falling** (Des Joachims +24 cm; Mitchinamecus +3 cm; Baskatong −4 cm; Quinze −3 cm). ORRPB forecast unchanged (May 26 bulletin, weekly mode, next June 2). **Proxy back online** (HTTP 200; yesterday backfill ran on HTTP 530).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Sources: proxy `river_readings` station 1195 (HQ telemetry direct, live through May 30T14:00 UTC); ORRPB conditions page `lake-coulonge` (midnight series, May 23–30). Vigilance INEDIT API: HTTP 200 confirmed but frontend continues to show May 27T14:00 as last update (106.785 m) — persistent lag in the INEDIT web layer only; HQ telemetry is live via proxy. No outage language warranted.*

| Metric | Value |
|---|---|
| Current level (proxy, May 30T14:00 UTC / 09:00 ET) | **106.48 m** |
| Midnight level (ORRPB midnight May 30) | **106.45 m** |
| Yesterday midnight (ORRPB midnight May 29) | 106.59 m |
| 24h delta (midnight-to-midnight) | **−14 cm** |
| Flood state | **etat 0 — fully normal** (no threshold exceeded) |
| Distance to pre-alert (107.00 m) | −55 cm below |
| Distance to minor flood (107.50 m) | −105 cm below |
| Distance to moderate flood (108.00 m) | −155 cm below |

**ORRPB midnight level series (recent):**

| Date | Level (m) | Midnight Δ | Notes |
|---|---|---|---|
| May 23 | 107.35 | −22 cm | |
| May 24 | 107.13 | −22 cm | |
| May 25 | 106.98 | −15 cm | |
| May 26 | 106.91 | −7 cm | |
| May 27 | 106.77 | −14 cm | |
| May 28 | 106.68 | −9 cm | |
| May 29 | 106.59 | −9 cm | |
| **May 30** | **106.45** | **−14 cm** | ORRPB midnight; proxy live 106.48 at 14:00 UTC |

---

## Bryson operating posture (HQ proxy)

*Source: proxy `dam_releases` (site 3-46, May 30T19:00 UTC) and `dam_levels` (stations 1-2964 amont, 1-2965 aval, May 30T19:00 UTC). "Yesterday" = May 29T19:00 UTC (same proxy tables).*

| Metric | Today (May 30T19:00) | Yesterday (May 29T19:00) | Δ |
|---|---|---|---|
| Total release (m³/s) | 549.16 | 592.59 | **−43.4 (−7.3% ⚠)** |
| Turbined (m³/s) | 233.31 | 286.90 | **−53.6 (−18.7% ⚠⚠⚠)** |
| Spilled (m³/s) | 315.85 | 305.68 | +10.2 (+3.3%) |
| Spill share (%) | 57.5% | 51.6% | **+5.9 pp ⚠** |
| Headpond / amont (1-2964, m) | **104.98** | 104.92 | **+6 cm — ABOVE upper band (Day 2; rise decelerating)** |
| Tailwater / aval (1-2965, m) | 87.77 | 87.84 | −7 cm |
| Δh (head differential, m) | 17.21 | 17.08 | +0.13 m |

**Headpond operating band (104.20–104.67 m):** At 104.98 m, the headpond is **31 cm above the upper bound** — Day 2 of the upper breach. The rate of rise has decelerated markedly: +70 cm on Day 1 (May 29), +6 cm on Day 2 (May 30). The operator has cut turbining by 18.7% and total releases by 7.3%, and appears to be gradually reining in the overshoot. However, the headpond is still drifting up — equilibrium has not yet been restored. The incoming Des Joachims release pulse (arriving Lac Coulonge area ~June 2) may briefly slow the rate of headpond decline once the lake inflow moderates.

**Flags exceeded (>5% change threshold):** total −7.3% ⚠, turbined −18.7% ⚠⚠⚠, spill share +5.9 pp ⚠. Spill +3.3% below individual threshold.

**Updated headpond series:**

| Date/Time (UTC) | Headpond (m) | vs. band (104.20–104.67 m) |
|---|---|---|
| May 21 | 104.16 | −4 cm below floor (lower breach begins) |
| May 27 23:00 | 103.90 | −30 cm below floor (worst point) |
| May 28 19:00 | 104.22 | +2 cm — breach ends, back in band |
| May 29 19:00 | 104.92 | **+25 cm above ceiling (upper breach Day 1; +70 cm swing)** |
| **May 30 19:00** | **104.98** | **+31 cm above ceiling (upper breach Day 2; +6 cm, decelerating)** |

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: proxy `dam_releases` via `latest_dam_releases` view, May 30T18:00–19:00 UTC. "Yesterday" = proxy May 29T19:00 UTC. Spill % = spilled / total.*

| Site | Total (m³/s) | Spill % | Δ total | Δ spill note |
|---|---|---|---|---|
| Première-Chute (3-33) | 766.1 | 43.5% | +1.0% | Flat |
| Quinze (3-31) | 727.0 | 37.6% | +1.0% | Flat |
| Îles (3-32) | 819.4 | 51.6% | +2.2% | Flat (−1.9 pp) |
| Rapide-2 (3-29) | 444.5 | 45.5% | −2.3% | Flat |
| Rapide-7 (3-28) | 439.5 | 23.2% | +0.2% | Flat |
| Bryson (3-46) | 549.2 | 57.5% | **−7.3% ⚠** | Spill +3.3%; see Bryson table |
| Paugan — Gatineau R. (3-65) | 594.7 | 13.9% | −4.3% | **Spill −22.7% ⚠** (107→83 m³/s) |
| Rapides-Farmers — Gatineau mouth (3-67) | 589.6 | 20.5% | −4.6% | **Spill −17.8% ⚠** (147→121 m³/s) |
| Carillon — basin terminal (3-60) | 3,115.5 | 20.2% | +4.7% | **Spill +40.5% ⚠⚠⚠** (448→630 m³/s) |

**Cascade notes:**

- **Upper Ottawa (Première-Chute through Rapide-7):** All essentially flat (±2%), consistent with a slow regulated recession. No individual flag thresholds breached.
- **Bryson −7.3% ⚠ / turbined −18.7% ⚠⚠⚠ / spill share +5.9 pp ⚠:** Continued operational shift away from turbines toward spilling as operator tries to stabilise the elevated headpond.
- **Gatineau (Paugan / Rapides-Farmers):** Both down ~4.5% each; spillway flow down −23% and −18% respectively ⚠. The Gatineau tributary is in post-peak recession with operators reducing spillway throughput.
- **Carillon +4.7% total / spill +40.5% ⚠⚠⚠:** A 182 m³/s increase in spillway flow while turbined changed very little (−1.6%). Carillon is routing additional flow through gates rather than turbines, likely to modulate headpond level. §15.3.5.1 trigger remains inactive.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: ORRPB conditions page `?display=river` (May 30 midnight levels; PSPC Temiscaming flows May 23–30); proxy `dam_releases` (Quinze May 30T19:00). Proxy `orrpb_river_flows` has an erroneous entry for Temiscaming May 29 (shows 1,493; correct ORRPB/PSPC finalized value is 1,207) — ORRPB conditions page values used throughout this section. For PSPC cross-check: ORRPB conditions page and PSPC are the same source for this gauge; proxy `reservoir_readings` `timiskaming` shows May 28 flow = 1,322 (vs ORRPB's 1,277 for May 28) — 45 m³/s discrepancy below 50 m³/s flag threshold; not flagged. "7 d ago" = May 23.*

| Metric | Today (May 30) | 7 d ago (May 23) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming outflow — ORRPB/PSPC (m³/s) | **1,199** (preliminary) | 1,464 | −265 (−18.1%) | **Day 29 past May 2 peak (~2,741). Sub-1,200 Day 1 ← NEW. Sub-1,250 Day 2 (corrected: Day 1 was May 29). Day 10 sub-2,000; Day 8 sub-1,500; Day 5 sub-1,400; Day 3 sub-1,300.** Sub-1,000 ETA ~June 5–10 at current 7-day average pace (~38 m³/s/day). |
| Témiscaming — PSPC cross-check | Same source as ORRPB | — | — | ORRPB and PSPC in agreement (proxy May 28 shows 1,322 vs ORRPB's 1,277 — 45 m³/s, below 50 m³/s flag). |
| Quinze release → Lake Temiscaming (m³/s) | 727 (proxy May 30T19:00) | ~778 est. | ~−51 | Modest continuing decline |
| Mattawa level (m) | **153.02** (midnight May 30) | 153.09 | −7 cm | **Day 2 of reversal (+11 cm both days from May 29 base 152.91 m). OPG Otto Holden travel-time effect. Otto Holden May 30 = 1,187 m³/s (declining from May 29 peak 1,240), so reversal may ease tomorrow.** |
| Pembroke level (m) | **111.90** (midnight May 30) | 112.33 | −43 cm | **−9 cm day-over-day; 13th+ consecutive day of decline.** Direction only — no flood threshold in this table. |

**Des Joachims release surge (downstream implications):**

| Station | May 29 daily (m³/s) | May 30 daily (m³/s) | Δ |
|---|---|---|---|
| Des Joachims (OPG) | 1,205 | **1,493** | **+288 (+23.9% ⚠⚠)** |

After 7 consecutive days of accumulation at Des Joachims (level rose from 150.58 m on May 23 to 151.82 m on May 30 midnight = +1.24 m), OPG substantially increased releases today. The 290 m³/s extra pulse will propagate downstream with an estimated travel time of 1–2 days to Pembroke, 2–3 days to Lac Coulonge. At current Lac Coulonge levels (106.45 m, 105 cm below minor-flood threshold), no flood implication. The pulse may temporarily slow the rate of lake decline.

**Main-stem level snapshot (ORRPB conditions page, May 29 midnight → May 30 midnight):**

| Station | May 29 midnight (m) | May 30 midnight (m) | Δ |
|---|---|---|---|
| Otto Holden GS | 177.20 | 177.27 | +7 cm |
| Mattawa | 152.91 | **153.02** | **+11 cm ← reversal Day 2** |
| Des Joachims GS | 151.58 | **151.82** | **+24 cm (Day 7 accumulation ends; releases surged)** |
| Pembroke | 111.99 | 111.90 | −9 cm |
| Lake Coulonge | 106.59 | **106.45** | −14 cm |
| Chenaux GS | 86.06 | 85.85 | −21 cm |
| Chats Lake at Arnprior | 74.19 | 74.11 | −8 cm |
| Britannia | 58.94 | 58.85 | −9 cm |
| Gatineau (Hull) | 42.28 | 42.26 | −2 cm |
| Thurso | 41.52 | 41.60 | +8 cm (Carillon backwater) |
| Grenville | 41.32 | 41.39 | +7 cm (Carillon backwater) |
| Carillon GS | 40.95 | 41.02 | +7 cm |

**Reservoir balance (May 29 midnight → May 30 midnight, ORRPB conditions `?display=reservoir`):**

| Reservoir | May 29 (m) | May 30 (m) | Δ | Direction |
|---|---|---|---|---|
| Des Joachims | 151.58 | **151.82** | **+24 cm** | **Rising — Day 7 (final day of accumulation; releases now surging)** |
| Mitchinamecus | 381.04 | 381.07 | +3 cm | Rising |
| Timiskaming (at Haileybury, WSC) | 179.08 | 179.09 | +1 cm | Steady |
| Timiskaming (at Temiscaming, WSC) | 179.05 | 179.06 | +1 cm | Steady |
| Bark Lake | 313.72 | 313.74 | +2 cm | Steady |
| Kipawa | 269.50 | 269.50 | 0 cm | Steady |
| Kiamika | 268.17 | 268.16 | −1 cm | Steady |
| Lady Evelyn | 289.16 | 289.15 | −1 cm | Steady |
| Cabonga | 360.43 | 360.42 | −1 cm | Steady |
| Dozois | 345.50 | 345.49 | −1 cm | Steady |
| Rapide-7 | 308.99 | 308.98 | −1 cm | Steady |
| Poisson Blanc | 201.38 | 201.36 | −2 cm | Steady |
| Quinze | 263.06 | 263.03 | −3 cm | Falling |
| Baskatong | 221.80 | 221.76 | −4 cm | Falling |

**Balance (±2 cm = steady, 14 reservoirs): 2 rising · 10 steady · 2 falling.** Active basin-wide retention flag (2+ reservoirs >10 cm/day): **not triggered** — only Des Joachims (+24 cm) exceeds the threshold.

**Milestone bookkeeping:**

| Milestone | Date first crossed | Day count today (May 30) |
|---|---|---|
| Freshet peak (~2,741 m³/s at Temiscaming) | ~May 2 | Day 29 |
| Sub-2,000 | ~May 21 | Day 10 |
| Sub-1,500 | ~May 23 | Day 8 |
| Sub-1,400 | ~May 26 | Day 5 |
| Sub-1,300 | May 28 (1,277 m³/s finalized PSPC) | Day 3 |
| Sub-1,250 | **May 29** (1,207 m³/s; backfill error corrected) | Day 2 |
| Sub-1,200 | **May 30** (1,199 m³/s preliminary) | **Day 1 — NEW** |
| Sub-1,000 (forecast) | ~June 5–10 | — |

*Sub-1,000 ETA: 7-day average pace from May 23 (1,464) to May 30 (1,199) = −265/7 = ~38 m³/s/day. At 38 m³/s/day from 1,199: (1,199−1,000)/38 ≈ 5 days ≈ June 4. Last-day pace (1,207→1,199 = −8 m³/s/day) would push this to late June. Given recession deceleration is normal (exponential tail), a June 5–10 range is realistic.*

---

## Carillon §15.3.5.1 directive check

*Source: proxy `dam_levels` (station 1-2968 Carillon amont, station 1-3675 Hull dock, May 30T19:00 UTC). ORRPB conditions cross-check (midnight May 30): Hull/Gatineau 42.26 m, Carillon GS 41.02 m — consistent.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (1-3675, May 30T19:00) | **42.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 5** (34 cm below threshold) |
| Hull dock delta vs yesterday | 0 cm (42.27→42.27 m) | — | Flat for second consecutive day |
| Carillon amont (1-2968, May 30T19:00) | **41.02 m** | 40.08 m spring-flood ceiling (active when Hull > 42.61) | **Ceiling NOT in effect — trigger inactive** |
| Carillon amont delta vs yesterday | +3 cm (40.99→41.02 m) | — | Slight continued fill |

The §15.3.5.1 monitoring period closed on May 26 (Day 22 of trigger activation). The Hull dock has been below 42.61 m for five consecutive days. The spring-flood ceiling at Carillon (40.08 m) is not in effect. Carillon amont is now 94 cm above the now-inactive ceiling and continuing to drift upward (the Carillon headpond is filling as total releases lag inflow). The Hull dock is flat for two consecutive days at 42.27 m — 34 cm below the trigger. Monitor whether the Hull dock resumes decline or stalls/rises (Carillon total release increased +4.7% today, which should help pull the headpond down eventually).

---

## Reservoir storage (latest_reservoir_readings proxy + ORRPB page)

*Source: proxy `latest_reservoir_readings` dated 2026-05-28 (46 h old — within 48 h stale threshold). ORRPB conditions page `?display=reservoir` used for May 30 levels (more current). Day-over-day delta = ORRPB May 29 → May 30.*

| Reservoir | May 29 (m) | May 30 (m) | Δ | Agency | Notes |
|---|---|---|---|---|---|
| Baskatong | 221.80 | 221.76 | −4 cm | HQ | Slowly drawing down; outflow 455 m³/s |
| Timiskaming (at Temiscaming) | 179.05 | 179.06 | +1 cm | WSC/PSPC | Stable; outflow 1,199 m³/s (preliminary) |
| Dozois | 345.50 | 345.49 | −1 cm | HQ | Flat; outflow 357 m³/s |
| Bark Lake | 313.72 | 313.74 | +2 cm | OPG | Stable; outflow 29 m³/s |

Active basin-wide retention flag (2+ reservoirs rising >10 cm/day): **not triggered.** Des Joachims is the dominant storage event but is not in the top-4 priority list. Baskatong is slowly drawing down (outflow exceeds net inflow). The top-4 are all near-flat.

---

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. **Last Update: 2026-05-26 3:35 PM EDT** (19:35 UTC). **Next Update: 2026-06-02 4:00 PM EDT** (20:00 UTC). Fetched at 22:15 UTC May 30. Cadence: weekly (7-day gap). Mode: weekly-notice.*

**Unchanged from prior brief** (May 26 bulletin; fifth consecutive brief with identical text; next scheduled update June 2, 2026):

> *Flows and water levels along the main stem of the Ottawa River are within seasonal values for this time of year, and are expected to remain stable or decrease gradually over the coming week depending on location.*

No further increases flagged. No precipitation or flood-watch language. No new climate or window-record claim to test.

---

## Anomaly flags

1. **Des Joachims release surge +23.9% ⚠⚠ (1,205→1,493 m³/s, May 30 preliminary):** After 7 consecutive days of OPG storage accumulation (level +1.24 m since May 23), releases jumped substantially today. The 290 m³/s extra pulse will propagate downstream. Expect a temporary slowing of the Lac Coulonge recession and a possible Pembroke level uptick around June 1–2. Not a flood concern at current elevations but worth tracking against the headpond/lake balance at Bryson.

2. **Bryson headpond upper breach — Day 2 (104.98 m, +31 cm above 104.67 ceiling):** Headpond remains above the operating band's upper limit for the second consecutive day. Rate of rise has decelerated sharply (+70 cm Day 1 → +6 cm Day 2), suggesting the operator is approaching equilibrium. Turbined −18.7% ⚠⚠⚠, total −7.3% ⚠, spill share +5.9 pp ⚠. Combined with the preceding 8-day lower breach (May 21–28), the headpond has oscillated from −30 cm below the floor to +31 cm above the ceiling within 10 days.

3. **Carillon spill +40.5% ⚠⚠⚠ (448→630 m³/s):** Large spillway surge (+182 m³/s) with only modest total release increase (+4.7%). Operator rerouting flow from turbines to spillway. §15.3.5.1 trigger inactive (Hull 42.27 m, 34 cm below 42.61 threshold). Hull dock flat two consecutive days — monitor for potential rebound.

4. **Paugan spill −22.7% ⚠ / Rapides-Farmers spill −17.8% ⚠:** Gatineau River tributary sharply reducing spillway throughput as the Gatineau post-peak recession accelerates.

5. **Sub-1,200 Temiscaming — new milestone (Day 1, preliminary):** First reading below 1,200 m³/s at Temiscaming. 29 days past May 2 peak. Note: today's value (1,199) is preliminary; final daily average may differ slightly. The preceding sub-1,250 milestone (Day 1) is **corrected to May 29** — the proxy had an erroneous value (`temiscaming 2026-05-29 = 1493`; correct ORRPB/PSPC finalized value = 1,207). See data note at top of brief.

6. **Proxy `orrpb_river_flows` data quality — Temiscaming May 29 entry is wrong:** Proxy shows `temiscaming 2026-05-29 = 1493`; correct value (ORRPB conditions page) is 1,207. This appears to be the Des Joachims May 30 value incorrectly ingested against the temiscaming slug with a May 29 date. The DB entry should be investigated and corrected. Backfill brief (May 30) was generated from this wrong data, incorrectly placing Sub-1,250 Day 1 on May 30 instead of May 29.

7. **Mattawa reversal Day 2 (+11 cm to 153.02 m):** Second consecutive day of upward movement after 12+ days of flat/falling. Otto Holden May 30 flow is declining (1,187 m³/s from 1,240), so the pulse energy is dissipating. Expect Mattawa to resume declining shortly.

---

## Notes

- **Des Joachims cascade timing:** The 290 m³/s extra release from Des Joachims today (1,205 → 1,493 m³/s) will reach Pembroke approximately June 1–2 (via the Chenaux/Chats Falls chain). It will reach Lac Coulonge approximately June 2–3. The current Lac Coulonge decline rate (~14 cm/day) should slow to perhaps 5–10 cm/day during the pulse passage, then resume its underlying decline. The lake is 105 cm below the minor-flood threshold; the pulse has no flood implication.

- **Bryson headpond oscillation — Day 10 perspective:** The headpond has now been outside the normal 104.20–104.67 m operating band for 10 of the last 10 days: 8 below the floor (May 21–28) and 2 above the ceiling (May 29–30). The rapid swings (−30 cm to +31 cm from worst-to-worst = 61 cm total spread through a 47 cm band) suggest the operator is struggling to find the equilibrium release rate as Lac Coulonge transitions from flood stage to normal summer level. The incoming Des Joachims pulse may complicate this: if it adds measurably to headpond inflow in 2–3 days, the operator will face additional adjustment pressure.

- **Sub-1,000 ETA reassessment:** Three different estimation approaches give different answers: (a) 7-day average pace: −38 m³/s/day from 1,199 → ~June 4. (b) Most recent day: −8 m³/s/day → late June. (c) The ORRPB weekly forecast ("stable or decrease gradually") is consistent with continued slow decline. June 5–10 appears the most likely range, with high uncertainty. The recession curve is clearly entering its exponential tail.

- **Vigilance 1195 INEDIT lag (Day 4):** The INEDIT frontend (`station_details_metadata_api`) still shows 2026-05-27T14:00 as the last reading (106.785 m). The proxy is sourcing directly from HQ telemetry and has current data (106.48 m at 14:00 UTC May 30). No outage language is warranted. The INEDIT frontend lag appears unrelated to the sensor or HQ transmission.

- **Proxy data confirmed healthy:** After yesterday's HTTP 530 outage (which forced the backfill to use HQ upstream API fallback), today the proxy is fully operational (HTTP 200, all tables current through May 30T19:00 for HQ-sourced data). The proxy `orrpb_river_flows` and `orrpb_river_levels` tables still lag by ~1 day (top out at May 29), which is normal — they will update overnight when the ORRPB conditions page is scraped for May 30 finalized values.
