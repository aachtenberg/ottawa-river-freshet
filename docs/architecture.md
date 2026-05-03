# Freshet Architecture

System-design view of the Ottawa River freshet monitoring stack.
Companion to [`README.md`](./README.md), which covers the user-facing dashboard
and data sources. This document focuses on **how the pieces fit together**:
component responsibilities, data flow, state ownership, and failure modes.

## Goals & non-goals

**Goals**

- Give a Davidson/Mansfield et Pontefract community a dashboard that's accurate, current, and
  useful during freshet — including specifically distinguishing the local
  Buckhams Bay gauge from the often-confused Britannia gauge.
- Push alerts to the property owner when the local gauge (Lac Coulonge) crosses
  configured thresholds.
- Preserve a long-term local history of river readings so the dashboard can
  show ≥7-day windows and historical context that upstream APIs don't retain.

**Non-goals**

- Replacing the official ORRPB / Vigilance / MVCA sources. The stack is
  derivative and, where they disagree, they win.
- Real-time alerting at sub-hourly resolution. The upstream APIs publish hourly;
  we don't try to be faster than the data.
- Authoritative flood forecasting. The dashboard surfaces forecasts but doesn't
  generate them.

## System diagram

```
                 Community / property owner
                          │ HTTPS
                          ▼
              ┌─────────────────────────┐
              │   freshet.xgrunt.com    │  Cloudflare Tunnel
              │   (Cloudflare edge)     │
              └───────────┬─────────────┘
                          │ → NodePort 30082 on headless-gpu
                          ▼
        ┌──────────────────────────────────────┐
        │ k3s/apps  freshet-dashboard          │
        │ ┌────────────────────────────────┐   │
        │ │ nginx                          │   │
        │ │  ┌──────┐  ┌─────────────────┐ │   │
        │ │  │ /    │  │ /history/  ─────┼─┼───┼─► PostgREST → TimescaleDB
        │ │  │ HTML │  │ (GET-only proxy)│ │   │
        │ │  └──────┘  └─────────────────┘ │   │
        │ └────────────────────────────────┘   │
        └──────────────────────────────────────┘
                          ▲              ▲
                          │ browser fetch│ browser fetch
                          │              │
        ┌─────────────────┴──┐   ┌───────┴──────────┐
        │ Vigilance Crues    │   │ open-meteo       │
        │ (QC MSP, Quebec    │   │ (basin weather + │
        │ stations + ECCC    │   │  freeze tracker) │
        │ mirrors)           │   └──────────────────┘
        └────────────────────┘
                          │
                          │  client-side fetch (CORS allowed)
                          ▼  also from the browser:
                    MVCA / Kisters KiWIS
                    (Buckhams Bay gauge)


k3s/apps  freshet-alerter (CronJob, hourly :15)
   │ poll Vigilance for station 1195
   │ compare against THRESHOLDS table
   ▼ (POST when crossed)
ntfy → freshet-mansfield topic → property owner's phone


k3s/data  river-history-ingest (CronJob, hourly :12)
   │ poll Vigilance for 18 stations (main stem + Gatineau + Lièvre cascade)
   │ poll KiWIS for Buckhams Bay
   │ poll open-meteo for 6 basin weather stations
   ▼ (upsert)
TimescaleDB hypertables: river_readings, weather_observations, river_stations


k3s/data  reservoir-ingest (CronJob, daily 21:30 UTC)
   │ scrape ottawariver.ca/conditions
   ▼ (upsert)
TimescaleDB hypertable: reservoir_readings


k3s/data  hq-ingest (CronJob, hourly :27)
   │ pull Hydro-Québec open-data feeds (centrale releases + station levels)
   │ filter to Ottawa basin (lat 45-48, lon -80 to -74)
   ▼ (upsert)
TimescaleDB hypertables: dam_releases, dam_inflows, dam_levels, dam_sites


k3s/data  wsc-ingest (CronJob, hourly :37)
   │ pull WSC realtime CSV (level + discharge)
   │ for active basin gauges (Britannia, Mattawa, Mississippi, Rideau, ...)
   ▼ (upsert)
TimescaleDB hypertable: wsc_readings


k3s/data  eccc-ingest (CronJob, every 6h :47)
   │ pull ECCC daily climate bulk CSV
   │ for 9 watershed climate stations (Maniwaki, Témiscamingue, Val-d'Or, ...)
   ▼ (upsert)
TimescaleDB hypertable: eccc_climate_daily
```

## Components

### Browser (the dashboard)

The dashboard is a **single-page static HTML application** served by nginx
([`index.html`](../k3s/base/apps/files/freshet-dashboard/index.html)). It does
its own fetching client-side and renders with Chart.js + Leaflet. Three classes
of data source:

1. **Vigilance Crues** for Quebec stations (and ECCC-mirrored Ontario stations
   like Mattawa). The shape is `{metadata, readings}` with `valeurs_niv` for
   the rolling ~72-hour buffer.
2. **MVCA Kisters KiWIS** for Buckhams Bay (`fetchKiwisStation()`). The
   adapter returns the same `{metadata, readings}` shape so all renderers
   work unchanged.
3. **PostgREST via the in-house `/history/` proxy** for >72-hour windows. Only
   used when the user selects a 7-day chart.

The dashboard uses **synthetic integer station IDs** (`>=99000`) for non-Vigilance
sources. The IDs only need to be unique within the dashboard's namespace.
99001 = Buckhams Bay (MVCA).

### Alerter (k3s/apps · `freshet-alerter`)

Hourly Python CronJob. Polls Vigilance for station 1195 (Lac Coulonge),
compares the latest reading against a hardcoded threshold table, POSTs to ntfy
on crossing. Stateless — no de-duplication. Alerts are intentionally noisy at
threshold boundaries; rely on the user to dismiss.

Runtime: stdlib-only Python in a `python:3.12-alpine` image. Script delivered
via configMapGenerator so editing the script auto-rolls the next CronJob.

### River-history ingester (k3s/data · `river-history-ingest`)

Hourly Python CronJob. Three responsibilities in one script:

1. Poll Vigilance for 18 stations (main stem + Gatineau cascade 442/994/982/983 + Lièvre cascade 522/196/211/300) → write `river_readings`.
2. Poll MVCA KiWIS for configured stations (currently just Buckhams Bay) →
   write `river_readings` with synthetic IDs ≥99000.
3. Poll open-meteo for 6 basin weather stations → write `weather_observations`.

The init container reruns `bootstrap.sql` on every invocation. The SQL is
idempotent (`CREATE TABLE IF NOT EXISTS`, `SELECT create_hypertable(... if_not_exists => TRUE)`)
so schema changes roll forward without fighting Job immutability.

Lookback is configurable per source (`MVCA_LOOKBACK_HOURS` env var, default 24).
For backfill, run a one-off Job with the lookback set to thousands of hours;
the `Prefer: resolution=ignore-duplicates` POST header makes overlap safe.

### Reservoir ingester (k3s/data · `reservoir-ingest`)

Daily Python CronJob (21:30 UTC, after ORRPB's mid-afternoon-Eastern refresh).
Scrapes the 8-day rolling reservoir-conditions table from
`ottawariver.ca/conditions`, parses with stdlib `html.parser`, upserts into
`reservoir_readings`. Same configMapGenerator + init-container schema-bootstrap
pattern as the river ingester.

### Hydro-Québec ingester (k3s/data · `hq-ingest`)

Hourly Python CronJob (`:27`). Pulls two HQ open-data JSON feeds linked from
`hydroquebec.com/production/debits-niveaux-eau.html`:

1. **Centrale release telemetry** (~3 MB) — hourly turbined / spilled / total
   m³/s + daily filtered local inflow per generating station. Writes to
   `dam_releases` (wide: total/turbined/spilled per `(site_id, time)`) and
   `dam_inflows` (daily incremental).
2. **Station levels** (~15 MB; misnamed "TARAGES") — hourly water-level
   readings at the gauging-station network. Writes to `dam_levels`.

Filters both to the Ottawa basin window (lat 45–48, lon -80 to -74) so the
ingester targets ~21 centrales + ~77 level stations rather than the entire
Quebec hydro fleet. Each pull contains ~10 days of hourly data.

The HQ CDN refuses Python's default Alpine TLS handshake; the ingester sets
`ctx.set_ciphers('DEFAULT:@SECLEVEL=1')` to work around. Site metadata is
upserted (`merge-duplicates`); time-series data is `ignore-duplicates`.

### WSC realtime ingester (k3s/data · `wsc-ingest`)

Hourly Python CronJob (`:37`). Pulls the WSC realtime CSV inline endpoint for
configured station codes (`02KF005` Britannia, `02JE013` Mattawa, etc.) — both
**level** (parameter 46) and **discharge** (parameter 47), 5-minute cadence,
24-hour lookback. Writes to `wsc_readings` keyed by `(station_code, time)`.

Why complementary to Vigilance: Vigilance often publishes only level. WSC
publishes both for the same gauges, plus stations Vigilance doesn't carry.

### ECCC daily climate ingester (k3s/data · `eccc-ingest`)

Six-hourly Python CronJob (`47 */6 * * *`). Pulls daily climate bulk CSV from
`climate.weather.gc.ca/climate_data/bulk_data_e.html` for 9 watershed stations
(Ottawa CDA, Maniwaki, Barrage Témiscamingue, Mont-Laurier, Parent, Val-d'Or,
Rouyn, North Bay, Pembroke). Writes to `eccc_climate_daily`. Used for the
climate-residual analysis in Exhibit E and the step-change watershed test.

### TimescaleDB + PostgREST (k3s/data)

TimescaleDB is the **only durable state** in the stack. Hypertables:

| Table | Key | Source | Cadence |
|---|---|---|---|
| `river_readings` | `(station_id, time)` | Vigilance + MVCA KiWIS | hourly |
| `weather_observations` | `(station, time)` | open-meteo | hourly |
| `reservoir_readings` | `(reservoir_id, time)` | ORRPB scrape | daily |
| `dam_releases` | `(site_id, time)` | HQ open-data centrales | hourly |
| `dam_inflows` | `(site_id, time)` | HQ open-data centrales | daily |
| `dam_levels` | `(station_id, time)` | HQ open-data stations | hourly |
| `wsc_readings` | `(station_code, time)` | WSC realtime CSV | 5-min |
| `eccc_climate_daily` | `(station_id, time)` | ECCC bulk CSV | daily |

`river_stations` (provider-tagged) and `dam_sites` (centrales + stations
metadata) are regular tables for upsert-on-change semantics.

PostgREST sits in front of the DB and exposes a JSON API. The dashboard's nginx
proxies `/history/*` to PostgREST with **GET/HEAD/OPTIONS only** ([nginx.conf:24-30](../k3s/base/apps/files/freshet-dashboard/nginx.conf#L24-L30))
so browsers can read but not mutate. This is also the path remote agents use
for cluster-state visibility (the route is exposed via Cloudflare; no auth).

## Data flow

### Read path: dashboard load

```
1. Browser → CDN (Cloudflare) → freshet-dashboard nginx → static index.html
2. JS runs renderAll():
   a. fetchPrimary() → Vigilance × 4 stations (1195, 1004, 1279, 545)
   b. fetchRegional() → 8 stations, dispatching by source:
      - 7 Vigilance (parallel)
      - 1 MVCA KiWIS (Buckhams Bay)
   c. fetchWeather() → open-meteo, 6 locations in one bulk call
   d. fetchSeasonPeak() → /history/river_readings (PostgREST) for 1195
3. If user selects >72h window: fetchStationHistory() → /history/river_readings
4. If user opens Map: leaflet lazy-loaded, MAP_STATIONS rendered using
   already-cached lastData (or refetched per-station as needed)
```

Browser caches: none enforced beyond Chart.js / Leaflet bundles. Each load
is fresh.

### Write path: ingest

```
1. CronJob fires (hourly :12 for river, daily 21:30 for reservoirs)
2. Init container runs bootstrap.sql via psql (idempotent)
3. Main container script:
   a. Vigilance loop → POST /river_readings (PostgREST)
   b. MVCA loop      → POST /river_readings (synthetic IDs)
   c. open-meteo     → POST /weather_observations
   d. (reservoir job): scrape → POST /reservoir_readings
4. Each POST uses Prefer: resolution=ignore-duplicates to make replays safe
5. ttlSecondsAfterFinished cleans up the Job pod after 1h (24h for reservoirs)
```

### Alert path

```
1. CronJob fires hourly at :15 (after Vigilance's :05-:10 publish + buffer)
2. Script fetches Vigilance for station 1195
3. Compares latest reading to hardcoded THRESHOLDS table
4. On crossing: POST to ntfy → push to subscribed clients
5. No state, no de-duplication
```

## State ownership

Everything that survives a pod restart is in **TimescaleDB** (a StatefulSet
with a PVC on `headless-gpu`). All other components are stateless:

- Dashboard: static HTML + JS, nothing persists between page loads.
- Alerter: stateless; replaying the same threshold-crossing alert is acceptable
  cost.
- Ingesters: stateless; lookback windows always overlap previous runs and
  duplicate inserts are ignored.

The TimescaleDB PVC is the **single point of recovery concern**. Backups are
out of scope for this doc but the data is reconstructable: Vigilance and MVCA
both serve full history on demand, and a backfill Job can rebuild
`river_readings` from scratch if needed (~35k rows for Buckhams Bay alone,
~hundreds of thousands across all stations).

## External dependencies

| Dependency | Used by | Criticality | Failure behaviour |
|---|---|---|---|
| Vigilance Crues (QC MSP) | Dashboard, alerter, ingester | Hard — drives 7 of 8 regional stations + property gauge | Dashboard shows skeleton/error; alerter logs and exits 0; ingester logs partial success |
| open-meteo | Dashboard freeze tracker | Soft — ancillary forecast info | Freeze tracker hides; rest of dashboard unaffected |
| MVCA Kisters KiWIS | Dashboard (Buckhams Bay), ingester | Soft — one regional card, doesn't gate property alerts | Buckhams Bay card shows "Unavailable"; rest of corridor unchanged |
| ORRPB conditions page | Reservoir ingester only | Soft — reservoir context, not real-time | Daily scrape job logs and exits 0; stale data persists |
| ntfy | Alerter | Hard for alerts only | Alerter logs and exits 1 (no fallback channel) |
| Cloudflare tunnel | Public dashboard access | Hard for external users | Local NodePort still works for in-network access |

## Failure modes

**Vigilance silence.** If Vigilance stops publishing (rare but happens —
seasonal maintenance, infra issues), the alerter is silent (no crossings
detected) and the ingester writes no new rows. The dashboard's regional cards
fail individually but the layout stays intact. There's currently no monitoring
that flags this; a remote agent or Prometheus rule could close that gap.

**MVCA endpoint changes.** KiWIS exposes ts_ids that, in principle, could be
re-numbered if MVCA migrates platforms. The dashboard would show "Unavailable"
on the Buckhams Bay card; the ingester would log fetch failures but keep
running for Vigilance. The configured ts_id (`48242042`) is in
`MVCA_STATIONS` env var — single point of update.

**Schema drift between dashboard and DB.** The dashboard's `fetchStationHistory`
maps `{time, level_m}` from PostgREST → `{date_prise_valeur, valeur}` shape.
If the bootstrap SQL ever changed those column names, the merge would silently
return wrong data. The init-container pattern means schema is always whatever
the latest `bootstrap.sql` says.

**TimescaleDB outage.** Dashboard 7-day window fails (PostgREST returns
errors); 72h-and-under continues working from Vigilance directly. Ingester
fails closed (Job retries); no data loss because Vigilance retains its 72h
buffer and the next successful Job catches up.

**Ingester drift / silent failure.** The cron runs hourly but if the pod
crashes consistently, hours of data go uningested. Recovery: bump
`MVCA_LOOKBACK_HOURS` (or the equivalent for Vigilance) for one run. The
upstream APIs hold enough history to backfill multiple weeks.

## Deployment topology

Single-cluster k3s, two namespaces:

- **`apps`** — user-facing components: `freshet-dashboard` (Deployment + Service +
  external NodePort), `freshet-alerter` (CronJob).
- **`data`** — durable storage and ingesters: TimescaleDB (StatefulSet),
  PostgREST (Deployment), `river-history-ingest` (CronJob),
  `reservoir-ingest` (CronJob).

`headless-gpu` is the node with the PVC for TimescaleDB; node affinity in the
StatefulSet pins it there. Other workloads schedule freely.

ConfigMapGenerator delivers all script files (HTML, Python, SQL) to their
Deployments / CronJobs. Hash-suffixed ConfigMap names mean editing a script
auto-rolls the consuming workload — no manual restart needed.

## Integration points & extension

**Adding a new gauge.** Two cases:

1. *Vigilance station.* Add the integer ID to `STATION_IDS` in the
   river-history-ingest env, add an entry to `REGIONAL_STATIONS` in the
   dashboard's `index.html`, optionally add to `MAP_STATIONS`,
   `CORRIDOR_BAR_STATIONS`, `STATIONS_TAB_IDS`. Ingester picks it up on next
   run.
2. *Non-Vigilance source (KiWIS, custom sensor, etc.).* Pick a synthetic
   integer ID ≥99000. Write a new fetch adapter that returns the
   `{metadata, readings}` shape (see `fetchKiwisStation` for the template).
   Add to `REGIONAL_STATIONS` with a `source` discriminator and any
   adapter-specific fields. Update the dispatch in `fetchRegional()` and the
   map fallback. Optional: extend `ingest.py` with the same source so the DB
   captures long-term history.

**Adding a new threshold alert.** Edit the `THRESHOLDS` table in
[`alerter.py`](../k3s/base/apps/files/freshet-alerter/alerter.py). The cron
auto-rolls on configmap change.

**Adding a new external sink.** The alerter only POSTs to ntfy; adding e.g. a
Discord webhook is a few lines + a secret reference. Keep both behind the same
threshold-crossing logic so notifications stay aligned.

## What's deliberately not here

- **Email / SMS alerts.** ntfy push is sufficient for the property owner; SMS
  was considered and skipped on cost.
- **A second physical gauge on the property.** Stubbed in
  [`sensor-bom.md`](./sensor-bom.md) but not built. If added, write to
  `river_readings` with a station ID like 9001 and add a card to the
  dashboard — no schema or ingest changes required.
- **Automated freshet-peak forecasting.** The dashboard surfaces ORRPB
  forecasts but doesn't model them. The historical CSV
  ([`data/orrpb-historic-peaks-1972-2025.csv`](./data/orrpb-historic-peaks-1972-2025.csv))
  feeds the dashboard's percentile-context chips but isn't used for
  prediction.
- **Authentication / authorization.** Dashboard is fully public via
  Cloudflare; PostgREST proxy is GET-only. No write paths are exposed
  externally. Adding auth would be straightforward (Cloudflare Access on the
  hostname) but currently unnecessary.
