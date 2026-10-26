# Daily brief — 2026-10-26

*Generated automatically at 22:05 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓. ORRPB forecast HTTP 200 ✓ — **last updated Oct 20 3:46 PM EDT**, next update Oct 27. Vigilance 1195: proxy ingest fresh T20 UTC Oct 26 (106.015 m). V3 posterior: exit 143 (Day 54 consecutive timeout); `freshet-forecast.json` not updated — keeping last-valid output.*

*Oct 25 retro-checks: **Oct 25 Témiscaming final 332 m³/s** — sub-400 streak CONTINUES at D38 confirmed. Oct 25 DJ provisional 281 → final 417 m³/s ✓ exclusion correct. Oct 25 Chenaux provisional 547 → final 487 m³/s; Oct 25 Otto Holden provisional 423 → final 368 m³/s — neither was headlined; finals within expected range.*

---

## In plain language

### Upstream — the upper basin

The basin's upper end remains in late-autumn recession. The October 25 final flow at the Lake Timiskaming control point came in at 332 cubic metres per second — confirming the 38th consecutive day below 400 m³/s, a streak that has now run since September 18. October 26's figure has not yet posted in the ORRPB daily series, but the PSPC cross-check at midnight shows 387 m³/s, keeping the day comfortably sub-400 and extending Day 39. The mid-valley gauge at Mattawa rose 12 centimetres to 152.41 metres (subject to the known provisional underread — see Notes), consistent with somewhat higher Timiskaming outflow. Pembroke nudged up 2 centimetres to 111.10 metres. Thirteen of the 14 storage reservoirs in the system held within 2 centimetres of their October 25 reading; the exception is Lake Timiskaming itself, which rose 3 centimetres — a sign that inflow is slightly outpacing the current controlled outflow, consistent with the PSPC cross-check figure being somewhat higher than yesterday's final.

### At the property — Lac Coulonge / Mansfield

The water level at Fort-Coulonge edged up another centimetre to 106.01 metres, the fifth straight day of roughly 1-centimetre daily gains. The level remains solidly normal: 99 centimetres below the 107.00-metre pre-alert threshold and 149 centimetres below the 107.50-metre minor-flood line. No concern at the property reach.

The dam pond at the Bryson Generating Station — located well downstream from the property, at the end of Lac Coulonge's winding southern outlet channel — showed a notable shift in operating posture today. Total water release climbed about 10 percent to 366 cubic metres per second, but the increase came almost entirely through the spillway: spill volume nearly doubled from about 37 to 70 cubic metres per second, while the turbines held essentially flat. The dam pond itself edged down 2 centimetres to 105.54 metres, so this was not a response to an imminent overflow — more likely a short-term hydraulic management decision. The dam pond continues to sit roughly 87 centimetres above the 104.67-metre ceiling of the normally permitted operating band, a situation that has now persisted for 151 consecutive days.

The ORRPB forecast (last updated October 20) remains unchanged: flows expected to stay fairly stable or slightly decrease through the coming week. The next update is due tomorrow, October 27.

---

## TL;DR

**RETRO ✓:** Oct 25 Témiscaming final 332 m³/s → **D38 confirmed**. DJ exclusion 281 → final 417 ✓; Chenaux 547 → 487, OH 423 → 368 (neither headlined; finals plausible). **Today:** Lac Coulonge **+1 cm** to **106.01 m** (Vigilance T20: 106.015 m; etat 0, 99 cm below pre-alert). **⚠ Bryson posture shift: spill +90.9% (36.75→70.17 m³/s), total +9.5% (333.76→365.56), spill share 11.0%→19.2%.** Headpond 105.54 m (Day 151 above band). Hull dock T19 41.26 m — trigger INACTIVE **Day 154**. Reservoir balance: 0 falling · 13 steady · 1 rising (timiskaming +3 cm). Oct 26 OH provisional 550 m³/s EXCLUDED (check 2 fails: mass balance; DJ=404 + Petawawa=15 m³/s ≠ 550). D39 in progress (PSPC Oct 26: 387 m³/s). Day **177** since May 2 peak.

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T20 UTC Oct 26 (PRIMARY); `orrpb_river_levels lake-coulonge` Oct 26 daily (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T20 UTC Oct 26) | **106.015 m** |
| ORRPB daily Oct 26 | 106.01 m (provisional same-day) |
| 24h delta (ORRPB daily Oct 25→26) | **+1 cm** |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 99 cm below |
| Distance to minor flood (107.50 m) | 149 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19 UTC Oct 26. Yesterday: T23 UTC Oct 25.*

| Metric | Today (T19 Oct 26) | Yesterday (T23 Oct 25) | Δ |
|---|---|---|---|
| Total release (m³/s) | **365.56** | 333.76 | **+31.8 (+9.5%) ⚠** |
| Turbined (m³/s) | **295.39** | 297.02 | −1.6 (−0.5%) |
| Spilled (m³/s) | **70.17** | 36.75 | **+33.4 (+90.9%) ⚠** |
| Spill share (%) | **19.2%** | 11.0% | **+8.2 pp ⚠** |
| Headpond / amont (m) | **105.54** | 105.56 | −2 cm |
| Tailwater / aval (m) | **87.01** | 86.88 | +13 cm |
| Δh (head differential, m) | **18.53** | 18.68 | −15 cm |

Total +9.5% and spill +90.9% both exceed the 5% anomaly threshold. Headpond 105.54 m is 87 cm above the 104.67 m band ceiling — **Day 151** above band (ongoing status).

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` — T19 UTC Oct 26. Yesterday comparison: T18 UTC Oct 25.*

| Site | Total (m³/s) | Spill % | vs Yesterday |
|---|---|---|---|
| Première-Chute (3-33) | **206.89** T19 | 0% | −31 (−13.0%) |
| Quinze (3-31) | **209.42** T19 | 0.4% | −14 (−6.3%) |
| Îles (3-32) | **212.29** T19 | 0% | −9 (−4.2%) |
| Rapide-2 (3-29) | **157.33** T19 | 0% | flat |
| Rapide-7 (3-28) | **157.16** T19 | 0% | flat |
| Bryson (3-46) | **365.56** T19 | 19.2% | **+33 (+9.8%) ⚠** |
| Paugan — Gatineau R. (3-65) | **140.69** T19 | 0% | flat |
| Rapides-Farmers — Gatineau mouth (3-67) | **155.41** T19 | 0% | −1 (−0.9%) |
| Carillon — basin terminal (3-60) | **901.22** T19 | 0% | +20 (+2.3%) |

Upper cascade (Première-Chute through Îles) stepped down 4–13%, consistent with intraday HQ dispatch cycling. Rapide-2 and Rapide-7 flat (run-of-river dispatch unchanged). Bryson spill surge is the notable change today. No zero-to-high spill transitions at any other site.

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Oct 19) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Oct 25 final (m³/s) | **332** *(Oct 26 not yet posted)* | 307 (Oct 19) | +25 | **D38 confirmed; D39 in progress** |
| Timiskaming PSPC cross-check Oct 26 T00 | **387 m³/s**, level 178.72 m | — | +55 vs Oct 25 final | sub-400 ✓; level +3 cm (inflow > outflow) |
| Quinze release → into the lake (m³/s) | **209.42** (T19) | ~307 (Oct 19) | — | Baseload dispatch |
| Mattawa level (m) | **152.41** *(provisional — chronic underread caution)* | n/a (limited query) | +12 cm vs Oct 25 | Rising; consistent with higher Timiskaming outflow |
| Pembroke level (m) | **111.10** (Oct 26 daily) | n/a (limited query) | +2 cm vs Oct 25 | Steady rise |

**Reservoir balance (T00 Oct 25 → T00 Oct 26):**
0 falling · 13 steady · 1 rising. timiskaming +3 cm (rising); all other 13 reservoirs within ±2 cm. Late-autumn equilibrium; timiskaming rise is consistent with PSPC cross-check showing outflow slightly trailing inflow.

**Milestone bookkeeping (W42 anchor Oct 18 + Oct 19–26 extension):**

| Milestone | W42 close (Oct 18) | Oct 19 | Oct 20 | Oct 21 | Oct 22 | Oct 23 | Oct 24 | Oct 25 | **Oct 26** |
|---|---|---|---|---|---|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 169 | 170 | 171 | 172 | 173 | 174 | 175 | 176 | **177** |
| Bryson amont above band (104.67 m) | 143 | 144 | 145 | 146 | 147 | 148 | 149 | 150 | **151** |
| §15.3.5.1 trigger INACTIVE | 146 | 147 | 148 | 149 | 150 | 151 | 152 | 153 | **154** |
| Témiscaming sub-400 | D31 (295) | D32 (307) | D33 (312) | D34 (335) | D35 (378) | D36 (345 ✓) | D37 (338 ✓) | D38 (332 ✓) | D39? |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T19 UTC Oct 26.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.26 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 154** (135 cm below trigger; flat from Oct 25) |
| Carillon amont (1-2968) | **41.13 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy HTTP 200 ✓ — T00 UTC Oct 26.*

| Reservoir | Oct 25 (T00) | Oct 26 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.43 m | **219.43 m** | 0 cm | Steady |
| Témiscaming | 178.69 m | **178.72 m** | +3 cm | Rising; inflow outpacing outflow |
| Dozois | 342.24 m | **342.22 m** | −2 cm | Steady (boundary) |
| Bark Lake (OPG) | 313.72 m | **313.71 m** | −1 cm | Steady decline |

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast`, HTTP 200 ✓. **Last Update: 2026-10-20 3:46 PM EDT** (2026-10-20T19:46:00Z UTC). **Next Update: 2026-10-27 4:00 PM EDT** (2026-10-27T20:00:00Z UTC). Cadence: weekly.*

**Unchanged from prior brief.** Verbatim:

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Flows and levels are expected to remain fairly stable or slightly decrease over the coming week, depending on locations. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

`further_increases_possible`: false. Mode: `weekly-notice`. Next update tomorrow (Oct 27).

---

## Anomaly flags

1. **⚠ Bryson posture shift: spill +90.9%, total +9.5%** (T19 Oct 26 vs T23 Oct 25). Spill volume nearly doubled (36.75 → 70.17 m³/s); total release up from 333.76 to 365.56 m³/s; turbines flat. Spill share jumped from 11.0% to 19.2%. Headpond moved only −2 cm (105.56 → 105.54 m) — posture change was an operational decision, not a headpond overflow response. No 5% threshold breach at any other cascade site.

2. **Oct 26 Otto Holden provisional 550 m³/s EXCLUDED (mandatory sanity check).** Oct 25 final = 368 m³/s → +182 m³/s (+49.5%) ≥ 150 m³/s and ≥ 25%. All four checks run:
   - Check 1 (feasibility floor): 22h elapsed → floor = (22/24)×550 = 504 m³/s. Recent Oct finals range 367–434 m³/s; 504 would be highest in >2-week window. Borderline.
   - **Check 2 (mass balance): FAILS.** Des Joachims provisional = 404 m³/s; Petawawa WSC (02KB001) T20 UTC = 15 m³/s; other tributaries ~15–20 m³/s. Total input ceiling ≈ 435 m³/s, 115 m³/s short of 550. No tributary source available to close the gap; reservoir drawdown at OH unverifiable (no OH pool level in `reservoir_readings`).
   - Check 3 (level/pool consistency): Des Joachims pool Oct 26 = 152.08 m (Oct 25: 152.10, −2 cm — flat). No OH pool data available. Inconclusive.
   - Check 4 (downstream response): Chenaux Oct 26 provisional = 540 m³/s (+53, +10.9% vs Oct 25 final 487); Chats Falls +31 (+5.7%); Carillon +11 (+1.2%). Downstream rising — not in contradiction to OH being higher. Passes.
   - Decision: Check 2 FAILS. Raw value in data table only, marked "provisional — failed sanity check (check 2)." OPG reservoir drawdown at OH cannot be ruled out; see Notes.

None beyond above.

---

## Notes

- **Oct 25 retro summary:** Témiscaming 332 m³/s (D38 confirmed); DJ 281 → 417 (exclusion correct, same artifact as prior days); Chenaux 547 → 487, Otto Holden 423 → 368 (neither headlined; large provisional-to-final swings are the expected pattern for OPG mid-valley stations).
- **Oct 26 Otto Holden 550 provisional:** Unlike the Aug 5 case, the downstream cascade (Chenaux 540, Chats 575, Carillon 901) is coherent and rising, not contradicting the figure. The failure is a mass balance gap (approximately 115 m³/s unexplained by available tributary sources). If OPG chose to draw down the OH reservoir today, the release could exceed inflow — a legitimate operational decision that would not show up in tributary gauges. The exclusion stands because the check formally fails, but the Aug 5 "invented tributary source" scenario is less likely here; this may finalize closer to 500 m³/s than to 368.
- **PSPC Timiskaming +55 m³/s (332→387):** Oct 26 cross-check at 387 m³/s is +55 m³/s (+16.6%) vs Oct 25 final. This is below both the 25% and 150 m³/s mandatory check thresholds; no sanity check required. The level rose +3 cm, consistent with inflow slightly exceeding controlled outflow.
- **Mattawa chronic underread:** Oct 26 provisional 152.41 m (+12 cm vs Oct 25 152.29). Per W42 HQ item 4, Mattawa provisional daily means run 5–12 cm below finals. Use as directional guide only (direction: rising is credible; magnitude uncertain).
- **V3 posterior:** Day 54 consecutive timeout (exit 143). `freshet-forecast.json` unchanged — last-valid output retained (asof 2026-06-07).
- **ORRPB forecast update tomorrow:** Next update expected Oct 27. Check for any seasonal-transition language or precipitation mention.
