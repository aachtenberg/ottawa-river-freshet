# Daily brief — 2026-06-07

*Generated automatically at 22:05 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (freshet.xgrunt.com) — confirmed HTTP 200 via guardrail probe (proxy dam_releases 200/116b, proxy dam_levels 200/77b, ORRPB forecast page 200/130,634b). All PostgREST queries successful via curl. HQ hourly data current to June 7 T18–T19:00 UTC (2–3 PM ET); Vigilance current to June 7 T20:00 UTC (4 PM ET); ORRPB conditions river page scraped at 22:00 UTC; ORRPB PSPC/ORRPB daily series current to June 7.*

---

## In plain language

### Upstream — the upper basin

Today is Day 37 of the recession since the May 2 freshet peak. The flow out of Lake Témiscaming settled at 790 cubic metres per second for today — slightly higher than the 782 recorded yesterday and the 755 the day before, but the three-day range (755–790 m³/s) reflects natural variability rather than a new surge. The river remains at roughly 29% of its May 2 peak (around 2,741 m³/s) and the upper basin is showing every sign of transitioning into early-summer base conditions. The anticipated sub-700 crossing has not materialised — a mild upward wobble over three days — but the system is not loading. Sub-800 m³/s is now three straight days running, which was last seen before the spring flood.

The mid-valley tells the same story. The river at Mattawa — midway between Lake Témiscaming and the property — registered 152.62 metres at midnight, down 9 centimetres from the night before, resolving the one-day blip that appeared on June 6. The river at Pembroke, about 150 kilometres further downstream, is also essentially flat. Among 14 tracked reservoirs, three are gently rising (Bark Lake, Des Joachims, and Mitchinamecus), ten are unchanged, and one (Dozois) is very slowly falling. The three risers are small reservoirs with near-zero outflows — a normal early-summer refill posture in quiet conditions.

### At the property — Lac Coulonge / Mansfield

The lake is in normal territory and continuing a slow drift lower. The live gauge at 4 PM today reads 106.22 metres, down about 2 centimetres from the same time yesterday. The midnight reading on the Ottawa River board (106.23 m tonight vs 106.24 m last night) confirms a modest one-centimetre overnight decline. The lake is 78 centimetres below the first cautionary threshold and in no flood danger. The Ottawa River board forecast remains on its post-freshet weekly schedule — unchanged since June 2, next update Monday June 9 — calling for stable or gradually decreasing levels with no flood concerns and no precipitation flags.

At Bryson — the dam pond immediately downstream of the property at the outlet of Lac Coulonge — the headpond stands at 105.19 metres, essentially unchanged from this morning's reading of 105.20 m. This is 52 centimetres above the top of the dam's normal operating range and matches the event peak set on June 1. This is now Day 10 of the headpond sitting above its normal ceiling, with no sign of imminent relief. Releases are steady and stable; the elevated level is driven by inflows from upstream exceeding the dam's releases, not by any operational change at Bryson itself.

The main afternoon development is at Carillon — the basin's terminal dam near Hawkesbury. Operators made a significant operational shift during the day: turbine generation was reduced by about 13% (from roughly 2,518 m³/s to 2,184 m³/s) while spillway discharge jumped by 127% (from 139 to 315 m³/s). The total outflow from Carillon fell slightly versus this morning, but the mix changed dramatically — from turbine-dominant to notable spill. The Carillon headpond and the downstream Hull dock gauge both fell about 8–9 centimetres during the day, meaning Carillon is releasing water faster than the river above it is supplying. None of this creates a flood concern at the property; Carillon is at the opposite end of the system.

---

## TL;DR

Lac Coulonge **106.22 m live (T20 UTC) / 106.23 m midnight** (live −2 cm/24h; midnight −1 cm; etat 0, 78 cm below pre-alert). **⚠⚠⚠ Bryson headpond Day 10 at event peak: 105.19 m, 52 cm above band ceiling 104.67 m — flat vs this morning.** Bryson releases all within ±1% threshold. **⚠⚠⚠ CARILLON MAJOR AFTERNOON SHIFT: turbined −13.3% (2,518→2,184 m³/s); spilled +127% (139→315 m³/s; 5.22%→12.61%); total −5.9% since morning. Vs yesterday EOD: turbined −5.6% ⚠; spill 0%→12.61% ⚠⚠; total +8.1%.** Carillon amont −9 cm intraday (41.10→41.01 m); Hull dock −8 cm intraday (41.85→41.77 m). **⚠ Paugan −5.1%; ⚠⚠ Rapides-Farmers −9.3%.** Témiscaming **790 m³/s** (updated PSPC June 7) — sub-800 Day 3 continues; 755→782→790 mild uptick, not strong decline; Day 37 post-peak. Mattawa −9 cm (152.71→152.62 m; resumed decline). Reservoir balance: **3 rising · 10 steady · 1 falling**. Hull dock 41.77 m → §15.3.5.1 INACTIVE Day 13 (84 cm below 42.61 m trigger). ORRPB forecast: unchanged (weekly; next update June 9).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Sources: proxy `river_readings` station 1195 (June 7 T20:00 UTC / 4:00 PM ET — most recent; T18:00–T19:00 also queried for trend); proxy `orrpb_river_levels` station `lake-coulonge` (midnight series); ORRPB conditions river page (June 7 15:00 ET — confirms 106.22 m, consistent).*

| Metric | Value |
|---|---|
| Current level (proxy station 1195, June 7 T20:00 UTC / 4:00 PM ET) | **106.22 m** |
| ORRPB conditions page (June 7 15:00 ET) | **106.22 m** |
| ORRPB midnight (June 7) | **106.23 m** |
| ORRPB midnight (June 6) | 106.24 m |
| 24h delta (same-hour proxy: June 6 T20:00 106.239 → June 7 T20:00 106.219) | **−2.0 cm** |
| 24h delta (midnight-to-midnight: June 6 → June 7) | **−1 cm** |
| Flood state | **etat 0 — fully normal** (no threshold exceeded) |
| Distance to pre-alert (107.00 m) | **78 cm below** |
| Distance to minor flood (107.50 m) | 128 cm below |
| Distance to moderate flood (108.00 m) | 178 cm below |

**ORRPB midnight level series (recent):**

| Date | Level (m) | Midnight Δ | Notes |
|---|---|---|---|
| May 30 | 106.41 | −12 cm | |
| May 31 | 106.36 | −5 cm | Deceleration begins |
| June 1 | 106.36 | 0 cm | Des Joachims pulse front |
| June 2 | 106.36 | 0 cm | Flat |
| June 3 | 106.32 | −4 cm | Brief resumption |
| June 4 | 106.31 | −1 cm | Near-flat |
| June 5 | 106.32 | +1 cm | Tick-up |
| June 6 | 106.24 | **−8 cm** | Resumed decline |
| **June 7** | **106.23** | **−1 cm** | **Essentially flat at midnight; live 106.22 m at 4 PM ET** |

*7-day pace (May 31 → June 7): 106.36 → 106.23 = −13 cm / 7 = −1.9 cm/day avg. Lake near seasonal equilibrium; very slow recession.*

---

## Bryson operating posture (HQ proxy)

*Source: proxy `dam_releases` (site 3-46, June 7 T18:00 UTC — most recent hourly) and `dam_levels` (stations 1-2964 amont T19:00 UTC, 1-2965 aval T19:00 UTC). "Yesterday" = June 6 T23:00 UTC. Guardrail: proxy dam_releases 200/116b, dam_levels 200/77b.*

| Metric | Today (June 7 T18–19 UTC / 2–3 PM ET) | Yesterday (June 6 T23:00 UTC) | Δ |
|---|---|---|---|
| Total release (m³/s) | 495.9 | 494.05 | +1.85 (+0.4%) |
| Turbined (m³/s) | 294.33 | 294.02 | +0.31 (+0.1%) |
| Spilled (m³/s) | 201.57 | 200.03 | +1.54 (+0.8%) |
| Spill share (%) | **40.65%** | 40.49% | +0.16 pp |
| Headpond / amont (1-2964, m) | **105.19** | 105.17 | **+2 cm — Day 10 breach; 52 cm above ceiling** |
| Tailwater / aval (1-2965, m) | 87.49 | 87.46 | +3 cm |
| Δh (head differential, m) | **17.70** | 17.71 | −0.01 m |

**Headpond operating band (104.20–104.67 m):** At 105.19 m, the headpond is **52 cm above the upper bound** — Day 10 of the upper breach. Today's reading is essentially identical to the event peak of 105.20 m (June 1 and this morning at T10:00). No series crossed the 5% flag threshold today; Bryson is in a stable-but-elevated posture. The headpond has fluctuated within 105.03–105.20 m since Day 4 with no clear downward trend.

**Headpond series (Day 10):**

| Date (approx. T19–T23 UTC) | Headpond (m) | vs. band ceiling 104.67 m |
|---|---|---|
| May 29 | 104.92 | +25 cm — Day 1 |
| May 30 | 104.98 | +31 cm (Day 2) |
| May 31 | 105.08 | +41 cm (Day 3) |
| June 1 | 105.20 | +53 cm (Day 4 — event peak) |
| June 2 | 105.05 | +38 cm (Day 5) |
| June 3 | 105.06 | +39 cm (Day 6) |
| June 4 | 105.03 | +36 cm (Day 7; minimum recovery) |
| June 5 | 105.10 | +43 cm (Day 8) |
| June 6 | 105.17 | +50 cm (Day 9, T23:00) |
| **June 7** | **105.19** | **+52 cm (Day 10, T19:00)** |

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: proxy `dam_releases`, June 7 T18:00–T19:00 UTC. "Yesterday" = June 6 T23:00 UTC.*

| Site | Total (m³/s) | Spill % | Δ total vs yesterday | Notes |
|---|---|---|---|---|
| Première-Chute (3-33) | 447.1 | 5.19% | −1.1 (−0.2%) | Stable |
| Quinze (3-31) | 459.01 | 1.59% | +0.2 (+0.0%) | Flat |
| Îles (3-32) | 469.0 | 2.33% | −2.1 (−0.4%) | Flat |
| Rapide-2 (3-29) | 344.12 | 3.28% | −0.4 (−0.1%) | Flat |
| Rapide-7 (3-28) | 341.74 | 0.0% | +1.5 (+0.4%) | Flat; 0% spill |
| Bryson (3-46) | 495.9 | 40.65% | +1.9 (+0.4%) | Flat; headpond Day 10 ⚠ |
| Paugan — Gatineau R. (3-65) | 377.98 | 0.0% | **−20.3 (−5.1%) ⚠** | Just crosses 5% flag |
| Rapides-Farmers — Gatineau mouth (3-67) | 379.78 | 8.85% | **−39.0 (−9.3%) ⚠⚠** | Sharp Gatineau step-down |
| Carillon — basin terminal (3-60) | 2,499.3 | **12.61%** | **+186.5 (+8.1%) ⚠** | **Turbined −5.6% ⚠; spill 0%→12.61% ⚠⚠; see cascade notes** |

**Cascade notes:**

- **Upper cascade (Première-Chute, Quinze, Îles):** Flat at 447–469 m³/s. No coordinated step-downs.
- **Rapide-2, Rapide-7, Bryson:** All flat; intraday headpond rise is inflow-driven, not release-driven.
- **Paugan −5.1% ⚠:** 398.30→377.98 m³/s. Just crosses the 5% alert threshold. Gatineau step-down in progress; 0% spill.
- **Rapides-Farmers −9.3% ⚠⚠:** 418.76→379.78 m³/s. Well above 5% threshold. Spill also fell (71.87→33.6 m³/s, 17.2%→8.85%). Gatineau mouth contribution to Ottawa declining sharply.
- **Carillon ⚠⚠⚠:** Day-over-day (vs June 6 T23:00): total +186.5 (+8.1%); turbined 2,312.76→2,184.17 (−128.6, **−5.6% ⚠**, crosses 5% flag); spill 0→315.12 m³/s (**0%→12.61% ⚠⚠**). Intraday change vs this morning's brief (June 7 T10:00 reading of 2,656.85 m³/s / 5.22% spill): total −157.6 (−5.9%), turbined −333.8 (−13.3%), spilled +176.4 (+127%). The Carillon headpond (amont) fell 9 cm since this morning (41.10→41.01 m); Hull dock fell 8 cm (41.85→41.77 m). The turbine reduction was sharp enough to shift most additional outflow to spill while total release fell vs the morning peak. Cause of turbine reduction unknown (grid dispatch, unit maintenance, deliberate drawdown).

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: proxy `orrpb_river_flows` (station `temiscaming`, PSPC, updated June 7 value); proxy `reservoir_readings` (`reservoir_id=timiskaming`, PSPC cross-check); proxy `orrpb_river_levels` (`mattawa`, `pembroke`, `lake-coulonge`, `britannia`, `carillon`); proxy `dam_releases` Quinze (3-31, T19:00 UTC). "7 d ago" = May 31.*

| Metric | Today (June 7) | 7 d ago (May 31) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming outflow — PSPC (m³/s) | **790** | 1,206 | −416 | **Day 37 post-peak. Sub-800 Day 3 (755→782→790; maintained). Sub-1,000 Day 5. Sub-900 Day 3. Mild uptick — not yet resumed decline.** |
| Témiscaming outflow — PSPC cross-check (reservoir_readings midnight) | 179.08 m / **777 m³/s** | — | — | *\|777 − 790\| = 13 m³/s — within 50 m³/s threshold; no flag. (June 7 ORRPB preliminary revised +10 from morning brief's 780; within threshold.)* |
| Quinze release → into Lake Témiscaming (m³/s) | 459.01 (T19:00) | ~1,206 (est.) | — | Flat at ~459 m³/s |
| Mattawa level (m) | **152.62** | 153.11 (May 31 peak) | −49 cm from peak | June 6 blip (+8 cm) resolved. **June 7: −9 cm** (152.71→152.62). Resumed decline. |
| Pembroke level (m) | **111.71 midnight / 111.67 (15:00 ET)** | — | +1 cm midnight | Direction only — table carries no flood threshold. Essentially flat to slightly declining intraday. |

**Main-stem level snapshot (ORRPB midnight series):**

| Station | June 5 | June 6 | June 7 | Δ (June 6→7) |
|---|---|---|---|---|
| Mattawa | 152.63 | 152.71 | **152.62** | **−9 cm** |
| Pembroke | 111.77 | 111.70 | **111.71** | +1 cm |
| Lake Coulonge | 106.32 | 106.24 | **106.23** | −1 cm |
| Britannia | 58.52 | 58.52 | **58.50** | −2 cm (midnight); ORRPB page 58.43 m at 15:00 ET |
| Carillon GS | 41.10 | 41.09 | **41.10** | +1 cm midnight; ORRPB page 41.02 m at 15:00 ET |

*Britannia declining intraday (58.50 midnight → 58.43 m at 15:00 ET, −7 cm). Consistent with reduced Gatineau inflows and Carillon's afternoon drawdown. Carillon GS midnight shows +1 cm but the afternoon real-time reading confirms continued decline — the midnight-to-midnight value reflects a timing artifact, not a net rise.*

**Milestone bookkeeping:**

| Milestone | Date first crossed | Day count (June 7) |
|---|---|---|
| Freshet peak (~2,741 m³/s at Témiscaming) | ~May 2 | **Day 37** |
| Sub-1,000 | June 3 (973 m³/s) | **Day 5** (continuous) |
| Sub-900 | June 5 (755 m³/s) | **Day 3** (June 5–7) |
| Sub-800 | June 5 (755 m³/s) | **Day 3** (June 5–7; all ≤790) |
| Plateau / mild uptick range | June 5 | Range 755–790 over 3 days; mildly upward direction, not resumed decline |
| Mattawa reversal peak | May 31 (153.11 m) | 152.62 m today; −49 cm from peak; blip resolved |
| Bryson headpond upper breach Day 1 | May 29 T19:00 (104.92 m) | **Day 10** (105.19 m — event peak) |
| Carillon spillway re-closed | June 5 | **Reversed June 7: spill 5.22% at morning; 12.61% by evening** |
| ORRPB weekly cadence transition | ~May 26 | Confirmed; next update June 9 |

**Reservoir balance (June 6 midnight → June 7 midnight, proxy `reservoir_readings`):**

| Reservoir | June 6 (m) | June 7 (m) | Δ | Direction |
|---|---|---|---|---|
| Bark Lake | 313.82 | 313.86 | +4 cm | **Rising** |
| Baskatong | 221.64 | 221.65 | +1 cm | Steady |
| Cabonga | 360.44 | 360.44 | 0 cm | Steady |
| Des Joachims | 152.06 | 152.13 | +7 cm | **Rising** |
| Dozois | 345.35 | 345.32 | −3 cm | **Falling** |
| Kiamika | 268.07 | 268.09 | +2 cm | Steady |
| Kipawa | 269.51 | 269.50 | −1 cm | Steady |
| Lady Evelyn | 289.12 | 289.11 | −1 cm | Steady |
| Mitchinamecus | 381.22 | 381.27 | +5 cm | **Rising** |
| Poisson Blanc | 201.13 | 201.12 | −1 cm | Steady |
| Quinze | 263.02 | 263.03 | +1 cm | Steady |
| Rapide-7 | 308.98 | 308.99 | +1 cm | Steady |
| Timiskaming (PSPC) | 179.07 | 179.08 | +1 cm | Steady |
| Timiskaming Haileybury (WSC) | 179.04 | 179.01 | −3 cm | Steady (boundary) |

**Balance (±2 cm = steady, 14 reservoirs): 3 rising · 10 steady · 1 falling.** Unchanged from prior June 7 draft. Des Joachims (+7 cm, outflow 933 m³/s) and the two small risers (Bark Lake, Mitchinamecus) are consistent with low-outflow passive accumulation. Active retention flag (2+ reservoirs rising >10 cm/day): **not triggered.**

---

## Carillon §15.3.5.1 directive check

*Source: proxy `dam_levels` (station 1-3675 Hull dock T19:00 UTC, station 1-2968 Carillon amont T19:00 UTC, June 7). Guardrail: proxy 200/77b.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (1-3675, June 7 T19:00 UTC / 3 PM ET) | **41.77 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 13** (84 cm below; −8 cm intraday from T10:00) |
| Hull dock Δ vs yesterday EOD | ~−4 cm | — | Declining; rose +4 cm in the morning then fell −8 cm by afternoon — net day decline |
| Carillon amont (1-2968, June 7 T19:00 UTC) | **41.01 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | **Ceiling NOT in effect — trigger inactive** |
| Carillon amont Δ vs morning (T10:00) | −9 cm (41.10→41.01) | — | Falling as Carillon releases exceed headpond inflows |

The §15.3.5.1 trigger has been inactive for 13 consecutive days. Hull dock is 84 cm below the trigger and declining. The −8 cm intraday drop is the most notable single-day movement at Hull dock in several days, consistent with the Carillon afternoon operational shift drawing down the headpond.

---

## Reservoir storage (latest_reservoir_readings)

*Source: proxy `reservoir_readings` dated 2026-06-07T00:00:00Z. Day-over-day delta = June 6 → June 7 midnight.*

| Reservoir | June 6 (m) | June 7 (m) | Δ | Flow (m³/s) | Notes |
|---|---|---|---|---|---|
| Baskatong | 221.64 | 221.65 | +1 cm | 282 | Flat; stable outflow |
| Timiskaming (PSPC) | 179.07 | 179.08 | +1 cm | 777 | Essentially flat; PSPC cross-check 777 m³/s (ORRPB: 790) |
| Dozois | 345.35 | 345.32 | −3 cm | 282 | Gently falling; stable outflow |
| Bark Lake | 313.82 | 313.86 | +4 cm | 18 | Rising — very low outflow, passive accumulation |

Active basin-wide retention flag (2+ reservoirs rising >10 cm/day): **not triggered.** Passive refill in small reservoirs only.

---

## ORRPB forecast (today vs yesterday)

*Source: ottawariver.ca/conditions/?display=forecast. Guardrail: 200/130,634b confirmed. **Last Update: 2026-06-02 3:33 PM EDT** (2026-06-02T19:33:00Z). **Next Update: 2026-06-09 4:00 PM EDT** (2026-06-09T20:00:00Z). Fetched 22:05 UTC June 7. Cadence: weekly (7-day gap). Mode: weekly-notice.*

**Unchanged from prior brief (June 5).** No update since June 2. Forecast text (verbatim):

> *Flows and water levels along the main stem of the Ottawa River are within seasonal values for this time of year, and are expected to remain stable or decrease gradually over the coming week depending on location.*

No "further increases cannot be ruled out" language. No flood-watch or precipitation text. No Lac Coulonge–specific language. The June 9 update will be the first new ORRPB forecast text since June 2; watch for any revised language on Carillon posture or Bryson headpond.

---

## Anomaly flags

1. **⚠⚠⚠ CARILLON MAJOR AFTERNOON OPERATIONAL SHIFT:** Between this morning (T10:00 UTC) and this evening (T19:00 UTC): turbined fell 2,518→2,184 m³/s (−13.3%); spilled rose 139→315 m³/s (+127%); total fell 2,657→2,499 m³/s (−5.9%). Day-over-day (vs June 6 T23:00): turbined **−5.6% ⚠** (crosses 5% flag); spill **0%→12.61% ⚠⚠** (site going from 0% to significant spill — template criterion met). Carillon headpond (amont) −9 cm intraday (41.10→41.01 m); Hull dock −8 cm intraday (41.85→41.77 m). Cause unknown; candidates include turbine unit dispatch/maintenance and deliberate headpond drawdown.

2. **⚠⚠⚠ BRYSON HEADPOND DAY 10 — AT EVENT PEAK:** 105.19 m at T19:00; 52 cm above band ceiling (104.67 m). Unchanged from this morning (T10:00: 105.20 m). This is the 10th consecutive day above the operating band's upper limit. Releases flat and stable. Rapide-7 (key upstream feeder) flat at 341.74 m³/s, 0% spill. No relief mechanism visible.

3. **⚠⚠ RAPIDES-FARMERS −9.3%:** 418.76→379.78 m³/s. Well above 5% flag threshold. Spill also fell significantly (71.87→33.6 m³/s, 17.2%→8.85%). Gatineau River mouth contribution to Ottawa declining sharply.

4. **⚠ PAUGAN −5.1%:** 398.30→377.98 m³/s. Just crosses the 5% flag threshold. Gatineau main dam step-down in progress; 0% spill.

5. **Témiscaming mild uptick (755→782→790):** Sub-800 Day 3 is maintained, but the three-day directional trend is mildly upward (+35 m³/s). The anticipated sub-700 crossing has not materialised. Not yet anomalous, but worth tracking — if June 8 PSPC continues rising toward 800, the sub-800 streak ends.

6. **§15.3.5.1 trigger INACTIVE Day 13:** Hull dock 41.77 m (−8 cm today), 84 cm below 42.61 m trigger. Carillon amont 41.01 m (−9 cm today). No directive issue; recording for state continuity.

---

## Notes

- **Carillon turbine/spill shift.** Two plausible explanations: (a) turbine units went offline (dispatch order, maintenance, nameplate constraint) forcing the balance onto spillways; (b) operators deliberately chose to drawdown the Carillon headpond while grid pricing made turbine generation uneconomical. Either way, the headpond is falling (−9 cm in a day), which is consistent with releases exceeding the combined inflows from the upper Ottawa and Gatineau. The June 9 ORRPB update may include any public statement from operators.

- **Paugan and Rapides-Farmers step-downs.** The concurrent decline at both Gatineau River dams (Paugan −5.1%, Rapides-Farmers −9.3%) signals the Gatineau sub-basin transitioning to base-flow conditions. This is expected for early June. The Gatineau contribution at Carillon will continue to ease over the coming days, which may counteract the present Carillon headpond drawdown.

- **Bryson headpond outlook.** The pattern over Days 5–10 (105.03–105.20 m; oscillating within 17 cm of the event peak) suggests the inflow-outflow balance at Bryson is roughly in equilibrium near 105.15–105.20 m. For the headpond to start declining, either Rapide-7 inflows must drop or Bryson releases must increase. Neither is currently happening. Watch for any coordinated HQ step-down at Rapide-7 / Rapide-2 as the key leading indicator.

- **Britannia intraday decline.** Britannia fell from 58.50 m (midnight) to 58.43 m (15:00 ET), a 7 cm intraday drop. This is consistent with reduced Gatineau inflows and the Carillon afternoon drawdown. The midnight June 7 vs June 6 comparison (−2 cm) understates the actual daytime decline.

- **June 9 ORRPB update watch.** First new forecast text since June 2. The two major developments to watch for are: (1) any acknowledgment of or commentary on the Carillon turbine/spill posture change; (2) any revised language on Bryson/Lac Coulonge given the sustained headpond breach. The current "stable or decrease gradually" framing does not reflect the Carillon turbine reduction.

- **Revision note.** Témiscaming June 7 PSPC revised from 780 (preliminary, morning brief) to 790 m³/s (+10; within 50 m³/s threshold; no flag). Sub-800 milestone unaffected.
