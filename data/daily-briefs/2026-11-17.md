# Daily brief — 2026-11-17

*Generated automatically at 22:00 UTC. See `freshet-public/docs/analysis/Freshet_2026_Complete_Summary.md` for project context.*

*Data sources: cluster proxy (`freshet.xgrunt.com/history/`) HTTP 200 ✓ (probed: HTTP 200 / 119b). ORRPB conditions pages (forecast, reservoir, river) all HTTP 000 / 0b on two separate probes — confirmed unreachable (not sandbox-blocked; `latest.json` NOT updated, last-known-good preserved). Vigilance 1195: proxy ingest fresh T21 UTC Nov 17 (106.022 m). V3 posterior: ran successfully (exit 0); anchors on asof 2026-06-07 (unchanged until `lac-coulonge-daily-1990-2026.csv` is extended). Bryson/Carillon/cascade: `dam_releases` + `dam_levels` T19–T20 UTC Nov 17.*

*Nov 16 retro: Témiscaming provisional 559 m³/s (W46 rollup streak table, queried 2026-11-17T00:02 UTC) → finalized **362 m³/s** (sub-400; D2 of new post-break sub-400 streak). W46 rollup claimed "new D1 streak broke the following day [Nov 16]" — that was based on a provisional artifact. D2 confirmed sub-400.*

---

## In plain language

### Upstream — the upper basin

The upper basin remains in a quiet late-season posture. The confirmed picture through November 16 — after overnight finalization that overturned an above-400 provisional reading that had appeared at midnight — is two consecutive sub-400-cubic-metre-per-second days at the Lake Timiskaming outlet since the brief above-400 blip on November 14. Today's preliminary reading at that gauge is a bit higher, sitting just above 400, but the past several weeks have shown that these midnight-hour snapshots frequently revise down when the day's average is finalized; the daily result for November 17 will not be settled until tomorrow.

All fourteen storage reservoirs across the basin are within one centimetre of yesterday's readings in every case — a uniform late-season flat posture with no outliers. Upstream of the main reservoir chain, the Mattawa gauge shows a 13-centimetre drop to 152.20 metres in today's preliminary reading, though that gauge has been volatile at this time of year with same-day readings routinely corrected by 10 or more centimetres; the direction (declining) is likely real but the magnitude should be treated as approximate. The Pembroke gauge is essentially unchanged at 111.12 metres.

### At the property — Lac Coulonge / Mansfield

The gauge at Fort-Coulonge recorded 106.022 metres at 9 PM UTC on November 17, down about 2 centimetres from the same hour yesterday. The lake is comfortably in full normal conditions: 98 centimetres below the first alert level and 148 centimetres below the minor-flood mark. No change in operating posture is visible from any upstream station.

The generating station at Bryson — reached by the long, winding channel from the southern end of Lac Coulonge, well below and separate from the properties — maintained essentially flat output overnight. The spillway share declined modestly from about 20 to 18 percent of total flow, with total discharge roughly 2 percent lower than yesterday. The dam pond behind Bryson (the headpond) remains flat at 105.54 metres — 87 centimetres above its normal operating ceiling for the 173rd consecutive day.

Well downstream at the basin's terminal dam at Carillon, dispatch output stepped up substantially through the late afternoon of November 17, rising from 956 at 6 PM UTC to 1,159 cubic metres per second by 8 PM UTC. This is a routine dispatch ramp-up and has no bearing on lake levels.

The ORRPB conditions website was unreachable today on three separate attempts across all three pages (forecast, reservoir, river). The weekly forecast update expected at 4 PM Eastern was not retrievable. Last known forecast (November 10) called for stable conditions near seasonal norms.

---

## TL;DR

**RETRO: W46 rollup claimed Nov 16 Témiscaming provisional = 559 m³/s (above 400, "new D1 streak broke that day") — finalized 362 m³/s (sub-400, D2 continues). Standard provisional artifact; rollup streak-break claim for Nov 16 was incorrect.** **Today (Day 199):** Lac Coulonge T21 **106.022 m** (−2.0 cm vs T21 yesterday; etat 0, 98 cm below pre-alert). Bryson T19: total **362.93 m³/s** (−2.3% vs yesterday), turbined **297.28**, spilled **65.65** (18.1% share, −11.6% — flag), headpond **105.54 m** (0 cm; Day 173 above band). §15.3.5.1 trigger INACTIVE **Day 176** (Hull 41.24 m). Carillon T20 **1158.80 m³/s** (+30.9% vs yesterday T23 885.14 m³/s — intra-day dispatch ramp, HQ telemetry confirmed). Témiscaming: Nov 16 finalized **362 m³/s** (D2 new sub-400 streak; W46 rollup retro provisional 559 revised); Nov 17 PSPC T00 provisional **414 m³/s** (above 400 — apply W46 HQ item 3, streak D3 UNCERTAIN). Mattawa Nov 17 provisional: **152.20 m** (−13 cm vs Nov 16 152.33 m; treat as provisional). Reservoir balance: **0 falling · 12 steady · 0 rising**. ORRPB unreachable (HTTP 000 — `latest.json` NOT updated, last-known-good preserved).

---

## Lac Coulonge (the property gauge, Vigilance 1195)

*Source: proxy `river_readings` station 1195 T21 UTC Nov 17 (PRIMARY); `orrpb_river_levels lake-coulonge` Nov 17 (cross-check).*

| Metric | Value |
|---|---|
| Current level (Vigilance T21 UTC Nov 17) | **106.022 m** |
| ORRPB daily Nov 17 (provisional) | 106.03 m |
| ORRPB daily Nov 16 (finalized) | 106.05 m |
| 24h delta (Vigilance T21 Nov 17 vs T21 Nov 16) | **−2.0 cm** (106.022 vs 106.042 m) |
| ORRPB daily delta (Nov 16 final 106.05 → Nov 17 prov 106.03) | −2 cm |
| Flood state | **etat 0 — fully normal** |
| Distance to pre-alert (107.00 m) | 98 cm below |
| Distance to minor flood (107.50 m) | 148 cm below |

---

## Bryson operating posture (HQ open-data)

*Source: `dam_releases?site_id=eq.3-46` + `dam_levels?station_id=in.(1-2964,1-2965)`. Today: T19/T20 UTC Nov 17. Yesterday: T23 Nov 16.*

| Metric | Today (T19/T20 Nov 17) | Yesterday (T23 Nov 16) | Δ |
|---|---|---|---|
| Total release (m³/s) | **362.93** | 371.29 | −8.36 (−2.3%) |
| Turbined (m³/s) | **297.28** | 297.00 | +0.28 (+0.1%) |
| Spilled (m³/s) | **65.65** | 74.30 | −8.65 (**−11.6%** — flag) |
| Spill share (%) | **18.1%** | 20.0% | −1.9 pp |
| Headpond / amont (m) | **105.54** (T20) | 105.54 (T23 Nov 16) | 0 cm |
| Tailwater / aval (m) | **86.99** (T20) | 86.99 (T23 Nov 16) | 0 cm |
| Δh (head differential, m) | **18.55** | 18.55 | 0 cm |

Spill decreased 11.6% (flag: >5%). Total release −2.3% (below 5% threshold — not flagged). Headpond flat at 105.54 m = **87 cm above** the 104.67 m band ceiling (Day 173 above band). Normal run-of-river dispatch.

---

## Main-stem cascade (HQ centrales, m³/s total release)

*Source: `latest_dam_releases` T19–T20 UTC Nov 17.*

| Site | Total (m³/s) | Spill % |
|---|---|---|
| Première-Chute (3-33) | **205.07** T19 | 0% |
| Quinze (3-31) | **222.76** T20 | 0.5% (1.03 m³/s) |
| Îles (3-32) | **226.29** T19 | 0% |
| Rapide-2 (3-29) | **158.38** T19 | 0% |
| Rapide-7 (3-28) | **158.00** T19 | 0% |
| Bryson (3-46) | **362.93** T19 | **18.1%** (65.65 m³/s) |
| Paugan — Gatineau R. (3-65) | **162.88** T19 | 0% |
| Rapides-Farmers — Gatineau mouth (3-67) | **172.38** T19 | 0% |
| Carillon — basin terminal (3-60) | **1158.80** T20 | 0% (**+30.9%** vs yesterday T23 885.14 m³/s — intra-day dispatch ramp; T18/T19/T20 progression: 956→1048→1159) |

---

## Upper basin watch (Témiscaming + mid-valley)

*Sources: `orrpb_river_flows` (temiscaming); `reservoir_readings` (timiskaming, PSPC cross-check); `orrpb_river_levels` (mattawa, pembroke). All cluster proxy HTTP 200 ✓.*

| Metric | Today / Latest | 7 d ago (Nov 10) | Δ | Milestone |
|---|---|---|---|---|
| Témiscaming Nov 16 finalized — ORRPB/PSPC (m³/s) | **362** | 383 (Nov 10) | −21 | D2 new sub-400 streak (new streak D1=Nov 15 386; prior 57-day streak broke Nov 14 at 419); W46 rollup retro: provisional 559 revised to 362 |
| Témiscaming Nov 17 — PSPC T00 provisional (m³/s) | **414** | — | — | Above 400; W46 HQ item 3 applies — treat as streak UNCERTAIN; no floor calc |
| Quinze release → into lake (m³/s) | **222.76** (T20) | — | — | Steady baseload; trace spill 1.03 m³/s |
| Mattawa level (m) | **152.20** (Nov 17 prov) | 152.34 (Nov 10) | −14 cm | Direction: declining; prov volatile — treat as directional only |
| Pembroke level (m) | **111.12** (Nov 17) | — | — | +2 cm vs Nov 16 (111.10 m); direction: flat/oscillating |

**Nov 16 Témiscaming retro:** W46 rollup (queried 2026-11-17T00:02 UTC) reported Nov 16=559 m³/s in both the streak table and pipeline health freshness check, claiming the new D1 sub-400 streak broke the same day. The DB now shows Nov 16 finalized at 362 m³/s (sub-400). The 559 was a provisional artifact — the same overestimation pattern documented throughout W46 (D55–D57 REVISED by 63–88 m³/s). D1 (Nov 15=386) and D2 (Nov 16=362) are both confirmed sub-400. D3 (Nov 17) status is UNCERTAIN (PSPC T00 414 m³/s > 400; no floor calc per W46 HQ item 3).

**Reservoir balance (T00 Nov 16 → T00 Nov 17):**

| Reservoir | Nov 16 (T00) | Nov 17 (T00) | Δ | Status |
|---|---|---|---|---|
| Baskatong | 219.28 m | **219.27 m** | −1 cm | Steady |
| Dozois | 342.10 m | **342.10 m** | 0 cm | Steady |
| Témiscaming | 178.65 m | **178.64 m** | −1 cm | Steady |
| Bark Lake | 313.54 m | **313.54 m** | 0 cm | Steady (Nov 17 T00 not updated; last Nov 16) |
| Des Joachims | 152.13 m | **152.13 m** | 0 cm | Steady |
| Poisson Blanc | 200.26 m | **200.27 m** | +1 cm | Steady |
| Rapide-7 | 309.01 m | **309.00 m** | −1 cm | Steady |
| Others (7) | — | — | 0 to −1 cm | Steady |

**Balance: 0 falling · 12 steady · 0 rising.** All reservoirs within ±1 cm. Normal late-season flat posture.

**Milestone bookkeeping (W46 rollup anchor Nov 15 + 2 days via DB):**

| Milestone | W46 close (Nov 15) | Nov 16 | **Nov 17** |
|---|---|---|---|
| Days since May 2 peak (2,741 m³/s) | 197 | 198 | **199** |
| Bryson amont above band (104.67 m) | 171 | 172 | **173** |
| §15.3.5.1 trigger INACTIVE | 174 | 175 | **176** |
| Témiscaming sub-400 streak | 57-day streak broke Nov 14 (D58=419); new D1=Nov 15 (386) | D2: 362 finalized (W46 rollup retro provisional 559 revised) | **D3 prov PSPC 414 (above 400) — UNCERTAIN; apply W46 HQ item 3** |

---

## Carillon §15.3.5.1 directive check

*Source: `dam_levels?station_id=in.(1-2968,1-3675)` — cluster proxy HTTP 200 ✓, T20 UTC Nov 17.*

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hull dock (Gatineau, 1-3675) | **41.24 m** | 42.61 m servitude | **BELOW — trigger INACTIVE Day 176** (137 cm below trigger) |
| Carillon amont (1-2968) | **41.12 m** | 40.08 m spring-flood ceiling (when Hull > 42.61) | Ceiling NOT in effect — trigger inactive |

§15.3.5.1 continuously inactive. No change from prior brief.

---

## Reservoir storage (latest_reservoir_readings)

*Source: cluster proxy `latest_reservoir_readings` HTTP 200 ✓ — T00 UTC Nov 17 (Bark Lake last updated Nov 16 T00).*

| Reservoir | Nov 16 (T00) | Nov 17 (T00) | Δ | Note |
|---|---|---|---|---|
| Baskatong | 219.28 m | **219.27 m** | −1 cm | Steady |
| Témiscaming | 178.65 m | **178.64 m** | −1 cm | Steady (PSPC T00 Nov 17 outflow 414 m³/s — provisional above 400; streak D3 uncertain) |
| Dozois | 342.10 m | **342.10 m** | 0 cm | Steady |
| Bark Lake (OPG) | 313.54 m | **313.54 m** | 0 cm | Steady (last updated Nov 16 T00; no Nov 17 row) |

No reservoir rising >10 cm/day. No active retention posture.

---

## ORRPB forecast (today vs yesterday)

*Source: `ottawariver.ca/conditions/?display=forecast` — UNREACHABLE today (probed: HTTP 000 / 0b from two separate curl probes across all three ORRPB conditions pages: forecast, reservoir, river; WebFetch timeout; not a sandbox-blocked domain). Last Update: 2026-11-10 2:19 PM EST (2026-11-10T19:19:00Z UTC). Next Update: 2026-11-17 4:00 PM EST (expected; not retrieved due to outage). `forecast/latest.json` NOT updated — last-known-good preserved.*

**ORRPB conditions page unreachable today** (HTTP 000/0b, three probe attempts across two curl invocations, plus WebFetch timeout — all three pages). Last known forecast text (Nov 10):

> *Flows and water levels along the main stem of the Ottawa River are close to seasonal values for this time of year. Water levels and flows are expected to remain fairly stable over the coming week. At some locations, water levels are below navigational chart datums. See the SPECIAL FEATURE section on our Home Page for our summertime message.*

---

## Anomaly flags

1. **Bryson spill −11.6%** (65.65 vs 74.30 m³/s yesterday, −8.65 m³/s). Normal dispatch adjustment; total release −2.3% (below 5% flag — not independently flagged). Run-of-river; total flow conserved. Day 173 of headpond above 104.67 m continues (no change).
2. **Carillon intra-day dispatch ramp +30.9%** vs yesterday T23 (1158.80 vs 885.14 m³/s, +273.66 m³/s; T18→T20 progression within today: 956→1048→1159). HQ telemetry confirmed. ORRPB daily provisional 963 m³/s (+10.6% vs Nov 16 finalized 871 m³/s — more moderate daily view). Routine dispatch at the terminal dam; passes ORRPB daily sanity check (10.6% < 25%, 92 m³/s < 150 m³/s).
3. **Témiscaming D3 provisional UNCERTAIN** (PSPC T00 414 m³/s > 400; W46 HQ item 3 guidance — any provisional above 380 m³/s = streak uncertain; Nov 15=386 D1 and Nov 16=362 D2 both confirmed sub-400). No floor calc applied.
4. **ORRPB website unreachable** (HTTP 000/0b, all three conditions pages, two probe attempts; not in sandbox-blocked list; `latest.json` not updated). No flood implications.
5. **RETRO — W46 rollup Nov 16 Témiscaming claim corrected:** Rollup streak table stated "Nov 16=559 m³/s (outside window) shows the new day-1 streak already broke the following day." Nov 16 DB finalized: **362 m³/s** (sub-400). The rollup's Nov 16 figure was a provisional artifact queried at 00:02 UTC before finalization. D2 (Nov 16) is confirmed sub-400. This retro does not affect the broader streak history (57-day streak correctly ended Nov 14; rollup's D1 Nov 15=386 and D1 label are correct).

No flood-risk implications. Lac Coulonge etat 0, 98 cm below pre-alert.

---

## Notes

- **V3 posterior CSV stale:** Script runs (exit 0) but anchors on asof 2026-06-07 (164+ days stale). `freshet-forecast.json` regenerated without change. W46 HQ item 4 remains open.
- **Mattawa provisional volatility** continues (W46 HQ item ongoing). Today's −13 cm reading should be treated as directional only.
- **ORRPB outage:** This is the first outage to affect the forecast retrieval since tracking began. The Nov 17 4:00 PM ET weekly update (which was expected today) was not retrievable. If the site is back up tomorrow, the Nov 18 brief should report the Nov 17 update text.
- **Pipeline gaps:** This is the first brief after the W46 pipeline gaps (Nov 9 and Nov 15). Those gaps are logged in the W46 rollup. This brief covers Nov 17; Nov 15 and Nov 16 remain without a published brief. The streak retro in flags #5 above addresses the most consequential unresolved item from those gaps.
- **Floor-feasibility method:** W46 HQ item 3 guidance (treat provisionals > 380 as uncertain, no floor calc) applied today to the PSPC T00 414. No floor calculation performed.

---

## HQ capture table addendum (Nov 16–Nov 17)

*Extends W46 rollup table (last entry: Nov 15). Single-hour snapshots (T23 Nov 16, T20 Nov 17) — not daily min/max. T20 UTC Nov 17.*

| Date | Bryson amont 1-2964 (m) | Carillon amont 1-2968 (m) | Hull dock 1-3675 (m) |
|---|---|---|---|
| 2026-11-16 | 105.54 (T23) | — | — |
| 2026-11-17 | 105.54 (T20) | 41.12 (T20) | 41.24 (T20) |

Bryson amont 105.54 m = 87 cm above 104.67 m ceiling. Hull max ≤41.24 m (trigger 42.61 m; 137 cm clearance). No threshold breach.
