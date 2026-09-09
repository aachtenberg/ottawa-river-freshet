# MVP PWA scope — personalized Home

Status: **in build** under [`freshet-mobile/`](../../../freshet-mobile/). Web core matches this doc; **Android ships via Capacitor** (same UI in a WebView APK). Not a full dashboard port; Mansfield dashboard stays separate.

One sentence: **Home = green panel + my gauge + up/down neighbors + marks editor**, with location→gauge from [gauge-snap.md](./gauge-snap.md) and mark fields from [cottage-wizard.md](./cottage-wizard.md).

---

## In scope (v1)

### Onboarding (once)

1. **Where is your place?** — map pin / GPS → snap-to-gauge → confirm / override  
2. **Cottage marks** — wizard using the validated schema (or **Vigilance-only** skip)

### Home tab (default)

Vertical phone stack, one job per block:

| Block | Behaviour | Replaces today |
|---|---|---|
| **Status panel** | Green / amber / red from *their* marks (or Vigilance état only) | `#summary-box` / `renderSummary()` hardcoded to 1195 + 108.75 |
| **My gauge** | Level, 24h/72h Δ, état, sparkline; tap → chart | Featured Lac Coulonge card + fixed `STATIONS` trio |
| **Incoming / outgoing** | Compact upstream · me · downstream from corridor neighbors | Fixed Mattawa / Waltham / Coulonge River hero strip |
| **Marks entry point** | “Edit cottage marks” → same editor as onboarding | Hardcoded `PROPERTY_THRESHOLDS` |

Optional on Home if cheap: highlight *their* station on a horizontal corridor-bar strip. Do **not** dump Reservoirs / Operations / full Stations tab onto first paint.

### Marks editor (reachable from onboarding + Me/Home)

- Lived keys: `approaching`, `backyard`, `structure`, `inside` (+ conditional `crawl_space`)
- Optional survey keys
- Strictly increasing validation
- Persist locally

### Shell

- Installable PWA: `manifest.webmanifest` + service worker (app shell + last readings cache)
- Bottom nav max 4: **Home · Corridor · Alerts · Me** — Corridor/Alerts can be thin stubs in v1
- EN/FR + theme reuse existing dashboard patterns
- Unofficial footer (ORRPB / local authorities remain authoritative)

### Data

- Same PostgREST `/history/` + Vigilance + MVCA KiWIS sources as the dashboard
- No new ingest
- Profile in `localStorage` (no accounts)

Suggested profile shape:

```json
{
  "propertyName": "Cottage — Constance Bay",
  "homePin": { "lat": 45.49, "lon": -76.08 },
  "homeGaugeId": 99001,
  "snapMethod": "deschenes_zone",
  "mode": "personal_marks",
  "marks": {
    "approaching": null,
    "backyard": null,
    "crawl_space": null,
    "structure": null,
    "inside": null,
    "survey_20yr": null,
    "survey_100yr": null
  },
  "structureLabel": "foundation / bricks",
  "howKnown": "refine_later",
  "alerts": { "enabled": false }
}
```

### Local notifications (MVP-thin)

If time: threshold crossings for `approaching` / `backyard` / `structure` via browser Notification API while the PWA is installed. Else: Alerts tab stub that lists the same crossings as in-app banners. Full ntfy/cloud push = post-MVP.

---

## Out of scope (defer)

| Defer | Why |
|---|---|
| Native iOS / Play Store polish | Android debug APK via Capacitor in `freshet-mobile/`; iOS later |
| Accounts / cloud sync / multi-property | Local profile is enough for one cottage |
| Lac-Coulonge-quality historic rank / Bayesian forecast for every gauge | Only gauges with history packs get rank; others show état |
| Full Reservoirs / HQ Operations / Tributaries / Cascade map | Deeper “More” later |
| Alerter CronJob multi-tenant rewrite | Keep Mansfield alerter as-is; PWA local alerts are separate |
| Perfect offline freshet science | Cache shell + last payload only |

---

## Mapping to current code

Personalization = turn these constants into the profile, then re-render Overview around `homeGaugeId`:

| Constant / site | MVP use |
|---|---|
| `PROPERTY_THRESHOLDS` | Profile `marks` |
| `HOME_PIN` | Profile `homePin` |
| `REGIONAL_STATIONS` / `CORRIDOR_BAR_STATIONS` | Snap catalog + neighbors ([snap-stations.json](./snap-stations.json)) |
| `STATIONS` / `renderCards()` | My gauge + up/down only |
| `renderSummary()` | Drive zones + margin from profile marks; margin baseline = `structure` |
| Alerter `THRESHOLDS` | Template for local notification rules (not shared process yet) |

Canonical science/UI reference: `apps/files/freshet-dashboard/index.html` (public mirror under `freshet-public/dashboard/`). **App code:** `freshet-mobile/` (do not overwrite the dashboard).

---

## Suggested build order

1. Profile model + `localStorage` + marks editor (can dogfood with Mansfield numbers pre-filled)
2. Snap-to-gauge + confirm using `snap-stations.json`
3. Home status panel parameterized by profile
4. My gauge card + up/down strip
5. PWA manifest / SW
6. Local threshold notifications or Alerts stub

---

## Acceptance (ship checklist)

- [ ] Cold start: pin on Constance Bay → proposes Buckhams; override to Britannia works
- [ ] Vigilance-only mode: green panel shows état, no fake cottage margin
- [ ] With `structure` mark: margin cm matches dashboard grammar
- [ ] Home shows exactly: status · my gauge · up/down · edit marks (no ops dump)
- [ ] Reload restores profile without an account
- [ ] Footer still says unofficial

---

## Success metric

A cottager on a non-Mansfield reach can open the PWA, set pin + one foundation mark, and see a Home screen that feels like Lac-Coulonge monitoring **for their reach** — without reading the full desktop dashboard.
