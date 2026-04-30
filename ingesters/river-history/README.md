# River-history ingester

Hourly Python script that pulls live river readings + reanalysis weather
observations and upserts them into TimescaleDB via PostgREST.

Stdlib-only — no `pip install` required at runtime, just Python 3.10+.

## What it ingests

1. **Vigilance readings**, one HTTP call per station listed in `STATION_IDS`.
   Writes to `river_readings` (level + flow) and metadata to `river_stations`.
2. **MVCA / KiWIS readings** (optional), for stations listed in
   `MVCA_STATIONS`. Writes to the same `river_readings` hypertable using
   synthetic station IDs ≥ 99000.
3. **Open-meteo weather observations** for the points listed in `UPSTREAM_WX`.
   One bulk call (comma-separated lat/lon) writes to `weather_observations`.

## Schema

[`bootstrap.sql`](bootstrap.sql) creates four hypertables and one view. Idempotent
— safe to rerun on every cron tick (which is what the upstream homelab deploy
does).

## Configuration (env)

| Variable | Default | Notes |
|---|---|---|
| `POSTGREST_URL` | `http://postgrest:3000` | Your PostgREST endpoint (docker-compose service name by default; in K8s use `http://postgrest.<namespace>.svc.cluster.local:3000`) |
| `STATION_IDS` | `1195,1004,951,545,1279,984,548,550,981,1264` | Comma-separated Vigilance numeric IDs |
| `MVCA_STATIONS` | `99001:48242042:Buckhams Bay` | `stationId:kiwisTsId:Label`, comma-separated. Empty disables MVCA ingest. |
| `MVCA_LOOKBACK_HOURS` | `24` | Override for one-shot historical backfill |

## Schedule

Vigilance updates hourly on the hour with ~10 min publish delay. Run at `:12`
past each hour for the freshest data.

## Cadence + idempotency

Each hourly run pulls Vigilance's ~72 h reading buffer, plus a configurable
window of MVCA history. Upserts are `Prefer: resolution=ignore-duplicates`
(server-side conflict resolution on the `(station_id, time)` PK), so re-runs
are free.
