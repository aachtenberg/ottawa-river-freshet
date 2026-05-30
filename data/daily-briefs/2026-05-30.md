# Daily brief — 2026-05-30

*Generated automatically at 22:05 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data note: Cluster proxy (freshet.xgrunt.com) is unreachable today — HTTP 530 confirmed on all endpoints (see guardrail below). All dam and station data sourced from Hydro-Québec upstream API fallback (HTTP 200/2.8 MB and 200/15.5 MB confirmed). River and reservoir data from ORRPB conditions pages. Vigilance INEDIT API still showing a May 27T14:00 reading — persistent frontend lag, not a sensor outage. 7-day proxy-dependent historical columns in the upper basin table are omitted.*

---

## In plain language

### Upstream — the upper basin

Twenty-nine days after the spring flood peaked on the Ottawa River, the upper basin is continuing its steady retreat — but the pace of the retreat at the key upstream gauge has slowed sharply. The flow leaving Lake Temiscaming, the large upper reservoir that acts as the basin's outlet valve, came in at about 1,205 cubic metres per second this morning — the first time this season it has been measured below 1,250. That is an important threshold crossing, but it also reveals that the pace of decline has slowed considerably. Earlier in the recession the flow was dropping by 100 cubic metres per second or more each day; now it is dropping by roughly 15 to 20. That means the earlier estimate of "sub-1,000 by June 1" needs to be revised substantially — mid-June is the more realistic target at current rates.

Two storylines in the mid-valley add context to that picture. At Mattawa — roughly midway between Lake Temiscaming and the property — the river gauge reversed course today, rising 11 centimetres after at least twelve consecutive days of flat-to-falling readings. The most likely cause is a timing effect: yesterday Ontario Power Generation substantially increased releases from the Otto Holden generating station upstream of Mattawa, and that extra water is arriving at Mattawa roughly 12–24 hours later. This is not a flood signal; it is the normal lag of water moving through a regulated system. Pembroke, the next downstream gauge, continued its 13th-plus consecutive day of decline (down 8 centimetres to 111.90 metres), confirming the broader recession is intact.

The Des Joachims reservoir — a large mid-valley storage pool operated by Ontario Power Generation between Lake Temiscaming and the property — is in its sixth consecutive day of active refill. The reservoir gained another 19 centimetres today, reaching 151.82 metres. Over six days OPG has added roughly 38 centimetres of storage. This is the expected post-freshet behaviour: operators rebuild summer storage as inflows moderate. That storage is gently cushioning everything downstream from any remaining pulse from the north. Of the 11 major reservoirs tracked today, only Des Joachims is actively filling (rising more than 2 cm per day); nine are essentially flat, and one — Cabonga in the headwaters — is falling slightly.

### At the property — Lac Coulonge / Mansfield

The river at Fort-Coulonge was reading 106.45 metres at 3 in the afternoon — down roughly 14 centimetres since midnight. That continues the steady draining pace of recent days. All warning flags remain off: the nearest threshold is the "pre-alert" line at 107.00 metres, still 55 centimetres away. The lake is well on its way to a summer-normal level around 106 metres.

The dam at the foot of Lac Coulonge — Bryson Generating Station — is in a notable operating posture for a second consecutive day. The backed-up pond between the lake and the turbines (what engineers call the headpond) is 31 centimetres above the top of its normal operating range, at 104.98 metres. The operator cut total releases another 7% and reduced turbine generation by nearly 19% compared to yesterday. More water is flowing through the spillway than through the turbines. The headpond continues to drift slowly higher even under these cuts, because the lake is draining slowly toward the dam and more water is entering the headpond than is being released. The operator will need to either increase releases or accept a temporarily elevated headpond as the lake settles.

At the basin's downstream terminus, the Carillon dam released about 5% more water than yesterday — but notably, it routed a sharply higher share through the spillway rather than the turbines (spillway share up from 15% to 20%). The headpond at Carillon continues to sit high (around 41 metres), and the regulatory monitoring trigger — which was active for 22 days in April and May — remains inactive: the Hull dock gauge at 42.26 metres is 35 centimetres below the trigger threshold. No regulatory ceiling is in effect. The ORRPB forecast is unchanged from the May 26 weekly bulletin ("within seasonal values, expected to remain stable or decrease gradually") with the next scheduled update on June 2.

---

## TL;DR

Lac Coulonge **106.45 m** at 15:00 (ORRPB conditions; proxy HTTP 530); estimated **−14 cm** from midnight May 29 (106.59 m); etat 0 (fully normal). **Bryson headpond upper breach Day 2**: 104.98 m, +31 cm above 104.67 ceiling; turbined −18.7% ⚠⚠⚠ / total −7.3% ⚠ / spill share +5.9 pp ⚠. **Carillon spill +40.5% ⚠⚠⚠** (448→630 m³/s); total +4.7% (near-flag). Carillon amont 41.02 m (flat). Hull dock 42.27 m → §15.3.5.1 INACTIVE Day 5. **Temiscaming sub-1,250 NEW milestone** (1,205 m³/s live 09:00, Day 1); sub-1,000 ETA revised to ~mid-June from yesterday's "May 31". **Mattawa reversal +11 cm** (152.91→153.02 m) after 12+ days flat/falling; probable Otto Holden travel-time. Pembroke −8 cm (13th+ day). Des Joachims Day 6 +19 cm (151.82 m). Reservoir: **1 rising · 9 steady · 1 falling** (calmed from 4/3/4 yesterday). ORRPB forecast unchanged (weekly mode, next June 2). **Cluster proxy unreachable** (probed: proxy 530/16b, HQ upstream 200/2.8 MB + 200/15.5 MB).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Sources: ORRPB conditions page `lake-coulonge` (15:00 May 30); yesterday midnight from prior brief; Vigilance thresholds from INEDIT metadata. Proxy `river_readings` unavailable (HTTP 530). Vigilance INEDIT API: HTTP 200/854b but buffer shows last reading 2026-05-27T14:00 (106.785 m) — persistent frontend lag, not sensor outage.*

| Metric | Value |
|---|---|
| Current level (ORRPB conditions, 15:00 May 30) | **106.45 m** |
| Yesterday midnight (ORRPB midnight May 29) | 106.59 m |
| 24h delta (midnight→15:00, partial day) | **−14 cm** (≈ full-day rate −9 to −14 cm/day) |
| Flood state | **etat 0 — fully normal** (no threshold exceeded) |
| Distance to pre-alert (107.00 m) | −55 cm below |
| Distance to minor flood (107.50 m) | −105 cm below |
| Distance to moderate flood (108.00 m) | −155 cm below |

**ORRPB midnight level series (recent):**

| Date | Level (m) | Midnight Δ | Notes |
|---|---|---|---|
| May 24 | 107.13 | −22 cm | |
| May 25 | 106.98 | −15 cm | |
| May 26 | 106.91 | −7 cm | |
| May 27 | 106.77 | −14 cm | |
| May 28 | 106.68 | −9 cm | |
| May 29 | 106.59 | −9 cm | |
| **May 30** | **~106.45** | **~−14 cm** | 15:00 reading; midnight estimate ~106.40–106.45 |

---

## Bryson operating posture (HQ open-data)

*Source: HQ upstream API fallback (`Donnees_VUE_CENTRALES_ET_OUVRAGES.json`, site 3-46; `Donnees_VUE_STATIONS_ET_TARAGES.json`, stations 1-2964 amont, 1-2965 aval). "Today" = May 30T19:00 UTC; "Yesterday" = May 29T19:00 UTC (same source, confirmed from proxy-held prior values). Proxy unavailable — guardrail verified (530/16b; HQ upstream 200/2.8 MB).*

| Metric | Today (May 30T19:00) | Yesterday (May 29T19:00) | Δ |
|---|---|---|---|
| Total release (m³/s) | 549.16 | 592.59 | **−43.4 (−7.3% ⚠)** |
| Turbined (m³/s) | 233.31 | 286.90 | **−53.6 (−18.7% ⚠⚠⚠)** |
| Spilled (m³/s) | 315.85 | 305.68 | +10.2 (+3.3%) |
| Spill share (%) | 57.5% | 51.6% | **+5.9 pp ⚠** |
| Headpond / amont (m) | **104.98** | 104.92 | **+6 cm ← ABOVE UPPER BAND (Day 2)** |
| Tailwater / aval (m) | 87.77 | 87.84 | −7 cm |
| Δh (head differential, m) | 17.21 | 17.08 | +0.13 m |

**Headpond operating band (104.20–104.67 m):** At 104.98 m, the headpond is **31 cm above the upper bound** — Day 2 of the upper breach. History: the headpond spent 8 days below the lower bound (May 21–28, bottoming at 103.90 m on May 27), re-entered the band on May 28, then overshot the upper ceiling on May 29 (+25 cm) and continued rising today (+31 cm). The operator is reducing releases aggressively (total −7.3%, turbined −18.7%), but the headpond continues drifting higher, likely because lake inflow still exceeds the reduced total throughput.

**Three flag thresholds exceeded:** total −7.3% ⚠, turbined −18.7% ⚠⚠⚠, spill share +5.9 pp ⚠. Spill +3.3% below individual 5% threshold.

**Updated headpond series:**

| Date/Time (UTC) | Headpond (m) | vs. band (104.20–104.67 m) |
|---|---|---|
| May 21 | 104.16 | −4 cm below floor (breach begins) |
| May 27 23:00 | 103.90 | −30 cm (worst point) |
| May 28 19:00 | 104.22 | +2 cm — breach ends, re-enters band |
| May 29 19:00 | 104.92 | +25 cm above ceiling (upper breach Day 1) |
| **May 30 19:00** | **104.98** | **+31 cm above ceiling (upper breach Day 2)** |

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: HQ upstream API fallback (`Donnees_VUE_CENTRALES_ET_OUVRAGES.json`), May 30T19:00 UTC. "Yesterday" = May 29T19:00 UTC from same source. Îles spill = combined principal (0.00) + secondary (422.59) m³/s.*

| Site | Total (m³/s) | Spill % | Δ total % | Δ spill note |
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

- **Upper Ottawa (Première-Chute through Rapide-7):** All essentially flat (±2%), consistent with a slow, regulated recession.
- **Bryson −7.3% ⚠ / turbined −18.7% ⚠⚠⚠ / spill share +5.9 pp ⚠:** Continued operational shift away from generation and toward spilling, driving the headpond above its upper bound.
- **Gatineau (Paugan / Rapides-Farmers):** Total down ~4.5% each; spill down −23% and −18% respectively ⚠. The Gatineau tributary is in post-peak recession with operators reducing spillway throughput.
- **Carillon +4.7% total / spill +40.5% ⚠⚠⚠:** A 182 m³/s increase in spillway flow while turbined changed little (−1.6%). This is the largest percentage change at any cascade site today. The Carillon headpond is high (41.02 m) and the operator appears to be routing additional flow through the spillway rather than the turbines, possibly to modulate forebay level without adding turbine wear.

**ORRPB average daily flows (May 30 preliminary, ORRPB conditions page at 10:00–15:00):**

| Station | May 29 (m³/s) | May 30 live (m³/s) | Δ |
|---|---|---|---|
| Otto Holden | 1,237 | 1,187 | −50 (−4.0%) |
| Des Joachims | 1,217 | 1,493 | **+276 (+22.7% ⚠⚠)** |
| Chenaux | 1,859 | 1,580 | −279 (−15.0%) |
| Chats Falls | 2,078 | 1,881 | −197 (−9.5%) |
| Britannia | 2,190 | 2,060 | −130 (−5.9%) |
| Carillon | 2,947 | 3,147 | **+200 (+6.8%)** |

*Note: "May 29" values are ORRPB daily flows from yesterday's brief; "May 30 live" are ORRPB conditions page real-time readings at noted timestamps (not yet finalized daily averages).*

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: ORRPB conditions page river/reservoir data (May 30); prior brief milestone bookkeeping. Proxy `orrpb_river_flows` and `orrpb_river_levels` unavailable (HTTP 530) — 7-day historical column uses milestone estimates from yesterday's brief. PSPC cross-check (`reservoir_readings`) unavailable; Timiskaming at Temiscaming flow from ORRPB conditions page used as primary.*

| Metric | Today | 7 d ago (May 23) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming outflow — ORRPB live (m³/s) | **1,205** (09:00, preliminary) | ~1,520 est.¹ | ~−315 (~−21%) | **29 days past May 2 peak (~2,741). Sub-1,250 Day 1 ← NEW. Day 10 sub-2,000; Day 8 sub-1,500; Day 5 sub-1,400; Day 3 sub-1,300. Sub-1,000 ETA revised to ~mid-June (pace slowed to ~15 m³/s/day).** |
| Témiscaming — PSPC cross-check (m³/s) | N/A (proxy down) | — | — | May 28 discrepancy (ORRPB 1,220 / PSPC 1,322) likely resolved now that both near 1,200. |
| Quinze release → into the lake (m³/s) | 727 (May 30T19:00, HQ) | ~760 est. | ~−33 | Modest continuing decline |
| Mattawa level (m) | **153.02** (10:00) | ~153.0 est.¹ | ~+0 cm | **⚠ REVERSAL: +11 cm from yesterday (152.91 m). 12+ consecutive decline days broken. Probable Otto Holden travel-time effect (OPG surged +27.8% May 29; arriving today).** |
| Pembroke level (m) | **111.90** (10:00) | ~112.30 est.¹ | ~−40 cm | **13th+ consecutive day of decline from 112.75 m May 20 high.** Direction only — no flood threshold. |

¹ 7-day historical unavailable (proxy down); estimates from milestone records in yesterday's brief.

**Sub-1,000 ETA revision:** Yesterday's brief projected ~May 31–June 1 based on a ~107 m³/s/day decline rate. Today's pace appears ~15 m³/s/day. At that pace from 1,205 m³/s, sub-1,000 takes ~13 more days (~June 12). This reflects the natural exponential decay of a recession — the early steep descent has given way to a prolonged shallow tail. Note: the ORRPB live reading is a single 09:00 snapshot; the finalized May 30 daily average may differ.

**Reservoir balance (May 29 → May 30, ORRPB conditions page):**

| Reservoir | May 29 (m) | May 30 (m) | Δ | Direction |
|---|---|---|---|---|
| Des Joachims | 151.63 | **151.82** | **+19 cm** | **Rising — Day 6 accumulation** |
| Mitchinamecus | 381.07 | 381.07 | 0 cm | Steady |
| Timiskaming (Haileybury) | ~179.10 | 179.09 | ~−1 cm | Steady |
| Bark Lake | 313.72 | 313.74 | +2 cm | Steady (edge) |
| Lady Evelyn | 289.17 | 289.15 | −2 cm | Steady |
| Kipawa | 269.49 | 269.50 | +1 cm | Steady |
| Dozois | 345.48 | 345.49 | +1 cm | Steady |
| Rapide-7 | 308.98 | 308.98 | 0 cm | Steady |
| Quinze | 263.05 | 263.03 | −2 cm | Steady |
| Baskatong | 221.76 | 221.76 | 0 cm | Steady |
| Cabonga | 360.45 | 360.42 | **−3 cm** | Falling |

**Balance (±2 cm = steady, 11 reservoirs): 1 rising · 9 steady · 1 falling.** Dramatic calming vs yesterday's 4 rising · 3 steady · 4 falling. The basin's storage network has largely settled; only Des Joachims (+19 cm) is actively accumulating. Active basin-wide retention flag (2+ reservoirs >10 cm/day): **not triggered** — only Des Joachims exceeds the threshold.

**Milestone bookkeeping:**

| Milestone | Date first crossed | Day count today (May 30) |
|---|---|---|
| Freshet peak (~2,741 m³/s) | ~May 2 | 29 days ago |
| Sub-2,000 | May 21 | Day 10 |
| Sub-1,500 | May 23 | Day 8 |
| Sub-1,400 | May 26 | Day 5 |
| Sub-1,300 | May 28 (ORRPB 1,220) | Day 3 |
| Sub-1,250 | **May 30** (1,205 at 09:00) | **Day 1 — NEW** |
| Sub-1,000 (forecast) | ~mid-June | — |

---

## Carillon §15.3.5.1 directive check

*Source: HQ upstream API fallback (`Donnees_VUE_STATIONS_ET_TARAGES.json`), stations 1-2968 Carillon amont, 1-3675 Quai-de-Hull, May 30T19:00 UTC. ORRPB conditions page cross-check (15:00): Hull/Gatineau 42.26 m, Carillon GS 41.02 m — consistent.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (1-3675, May 30T19:00) | **42.27 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 5** (34 cm below threshold) |
| Hull dock delta vs yesterday | −0 cm (42.27→42.27 m) | — | Essentially flat |
| Carillon amont (1-2968, May 30T19:00) | **41.02 m** | 40.08 m spring-flood ceiling (active when Hull > 42.61) | **Ceiling NOT in effect — trigger inactive** |
| Carillon amont delta vs yesterday | +3 cm (40.99→41.02 m) | — | Near-flat; minor continued fill |

The §15.3.5.1 monitoring period closed on May 26 (Day 22 of trigger activation). The Hull dock has been below 42.61 m for five consecutive days. The spring-flood ceiling at Carillon (40.08 m) is not in effect. Carillon amont is currently 94 cm above the now-inactive ceiling. The Carillon headpond is high and stable; the Hull dock decline has essentially stalled (flat for two days). Monitor whether the Hull dock resumes decline or stabilises.

**Main-stem level snapshot (ORRPB conditions page, May 29 midnight → May 30 at 10:00–15:00):**

| Station | May 29 (m) | May 30 (m) | Δ |
|---|---|---|---|
| Otto Holden GS | 177.24 | 177.27 | +3 cm (minor fill) |
| Mattawa | 152.91 | **153.02** | **+11 cm ← REVERSAL** |
| Des Joachims GS | 151.63 | **151.82** | **+19 cm (Day 6 storage)** |
| Pembroke | 111.98 | 111.90 | −8 cm |
| Lake Coulonge | 106.59 | 106.45 | −14 cm |
| Chenaux GS | 86.01 | 85.85 | −16 cm |
| Chats Falls | 74.16 | 74.11 | −5 cm |
| Britannia | 58.93 | 58.85 | −8 cm |
| Hull/Gatineau | 42.26 | 42.26 | 0 cm (flat) |
| Thurso | 41.55 | 41.60 | +5 cm (Carillon backwater) |
| Grenville | 41.35 | 41.39 | +4 cm (Carillon backwater) |
| Carillon GS | 41.00 | 41.02 | +2 cm (near-flat) |

---

## Reservoir storage (latest_reservoir_readings)

*Source: ORRPB conditions `?display=reservoir` page (May 30, 24:00h values). Proxy `latest_reservoir_readings` unavailable (HTTP 530). Day-over-day delta computed from prior brief May 29 values.*

| Reservoir | May 29 (m) | May 30 (m) | Δ | Agency | Notes |
|---|---|---|---|---|---|
| Baskatong | 221.76 | 221.76 | 0 cm | HQ | Flat; outflow 455 m³/s |
| Timiskaming (at Temiscaming) | ~179.06 | 179.06 | ~0 cm | ORRPB/PSPC | Outflow 1,205 m³/s (live) |
| Dozois | 345.48 | 345.49 | +1 cm | HQ | Slightly rising; outflow 357 m³/s |
| Bark Lake | 313.72 | 313.74 | +2 cm | OPG | Near-flat; outflow 29 m³/s |

Active basin-wide retention flag (2+ reservoirs rising >10 cm/day): **not triggered.** Top-4 reservoirs all near-flat. Des Joachims (+19 cm) is the season's dominant storage event but is not in the top-4 relevance list.

---

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. **Last Update: 2026-05-26 3:35 PM EDT** (19:35 UTC). **Next Update: 2026-06-02 4:00 PM EDT** (20:00 UTC). Fetched at 22:05 UTC May 30. Cadence: weekly (7-day gap). Mode: weekly-notice.*

**Unchanged from prior brief** (May 26 bulletin; next scheduled update June 2, 2026):

> *Flows and water levels along the main stem of the Ottawa River are within seasonal values for this time of year, and are expected to remain stable or decrease gradually over the coming week depending on location.*

No further increases flagged. No precipitation or flood-watch language. No new climate or window-record claim. Forecast text has been identical for four consecutive briefs.

---

## Anomaly flags

1. **Bryson headpond upper breach — Day 2 (104.98 m, +31 cm above 104.67 ceiling):** The headpond continues to drift above the upper limit of its normal operating range. Turbined −18.7% ⚠⚠⚠, total −7.3% ⚠, spill share +5.9 pp ⚠. The operator is cutting releases but has not yet arrested the headpond rise. Combined with the preceding 8-day lower breach (May 21–28), the headpond has now oscillated through the full 47 cm band and out both sides within 10 days.

2. **Carillon spill +40.5% ⚠⚠⚠ (448→630 m³/s):** A 182 m³/s surge in Carillon spillway flow with only modest total release increase (+4.7%). The operator is routing more water through gates rather than turbines. §15.3.5.1 trigger remains inactive (Hull 42.27 m, 34 cm below 42.61 threshold).

3. **Paugan spill −22.7% ⚠ / Rapides-Farmers spill −17.8% ⚠:** Gatineau River tributary sharply reducing spillway throughput as the Gatineau post-peak recession accelerates.

4. **Mattawa reversal (+11 cm):** First upward reading at Mattawa after 12+ consecutive declining/flat days. Probable cause: OPG's Otto Holden GS surged output by +27.8% on May 29 (to 1,237 m³/s); that pulse is propagating downstream. Not a flood signal but breaks the streak. Pembroke (downstream of Des Joachims) continues to fall (−8 cm), consistent with Des Joachims absorbing the surge before it reaches Pembroke.

5. **Sub-1,250 Temiscaming — new milestone (Day 1, May 30):** First confirmed reading below 1,250 m³/s. More importantly, the pace of decline has slowed to ~15 m³/s/day, pushing the sub-1,000 ETA from "May 31" to ~mid-June.

6. **Des Joachims Day 6 accumulation (+19 cm, 151.82 m):** Sixth consecutive rising day. Cumulative gain ~38 cm since May 25. Single reservoir, not triggering the basin-wide 2+ threshold.

7. **Cluster proxy unreachable — HTTP 530 on all endpoints (probed: proxy 530/16b; HQ upstream 200/2.8 MB + 200/15.5 MB):** All dam and level data drawn from HQ upstream API fallback. ORRPB conditions pages used for river/reservoir data. Historical (7-day) proxy columns omitted. PSPC cross-check unavailable today.

---

## Notes

- **Bryson headpond oscillation:** The band (104.20–104.67 m) is 47 cm wide. The headpond went from −30 cm below the floor to +31 cm above the ceiling in just 3 days (May 27 night to May 30). This is a 78 cm swing through and past the band. The operator appears to be struggling to find an equilibrium release rate as Lac Coulonge normalises. Worth tracking whether the headpond returns toward the band centre or oscillates further.

- **Sub-1,000 ETA revision is significant:** Yesterday's "~May 31" call was based on the prior ~107 m³/s/day decline rate. With today showing ~15 m³/s/day pace, a ~2-week revision is necessary. This is normal — recession curves are exponential, not linear, and the tail is always longer. The sub-1,000 level was previously associated with "true base flow" and normal summer operating. Mid-June is the updated estimate.

- **Hull dock stalling:** The Hull dock has been at 42.26–42.27 m for two consecutive days — essentially flat after five days of gradual decline. If this stalling continues and Carillon headpond keeps rising, there is a non-zero probability the Hull dock could tick back up. At 34 cm below the §15.3.5.1 trigger, this is not an immediate concern, but worth monitoring given the large Carillon spill increase today.

- **Des Joachims outflow +22.7% (1,217→1,493 m³/s):** OPG released substantially more from Des Joachims today. This is flowing downstream toward Pembroke and Lac Coulonge. Despite this increase, Pembroke fell −8 cm, suggesting Pembroke is still draining faster than it's receiving inflow. Lac Coulonge also continues falling. The increased Des Joachims outflow may slow the rate of lake decline slightly in coming days, but at current levels there is no flood risk.

- **Vigilance INEDIT frontend lag (Day 4):** The INEDIT API (`station_details_metadata_api`) still shows 2026-05-27T14:00 as last update (106.785 m). However, the ORRPB conditions page (which sources from HQ telemetry via a different path) shows 106.45 m today — 34 cm below the stale INEDIT value. The sensor is transmitting; the INEDIT frontend has been lagging since May 27. No outage claim is warranted.
