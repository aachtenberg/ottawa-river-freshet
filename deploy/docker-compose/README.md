# Docker Compose deploy

Single-host deployment of the freshet stack. Brings up TimescaleDB, PostgREST,
nginx serving the dashboard, plus three cron-style sidecars (river ingester,
reservoir scraper, alerter).

## Prerequisites

- Docker Engine ≥ 24
- Docker Compose v2 (`docker compose` not `docker-compose`)

## First run

```bash
cp .env.example .env
$EDITOR .env             # set POSTGRES_PASSWORD and NTFY_TOPIC at minimum
docker compose up -d
```

The dashboard becomes available at `http://localhost:8080` once the
TimescaleDB schema initializes (a few seconds on first start). The
`cron-river` sidecar runs the ingester immediately on startup and then once
per hour; `cron-reservoir` runs once per day; `cron-alerter` once per hour.

## Triggering an immediate ingest

```bash
docker compose exec cron-river python /app/ingest.py
docker compose exec cron-reservoir python /app/scrape.py
```

## Inspecting the database

```bash
docker compose exec timescaledb psql -U freshet -d freshet
freshet=# SELECT reservoir_id, level_m, time
freshet-#   FROM latest_reservoir_readings ORDER BY reservoir_id;
```

## Customizing for your watershed

The default `STATION_IDS` in `.env.example` is the full Ottawa River corridor
ingested by the upstream maintainer. To monitor a different river:

1. Find Vigilance station IDs via [vigilance.geo.msp.gouv.qc.ca](https://vigilance.geo.msp.gouv.qc.ca/).
   Ontario / non-Quebec gauges via ECCC HYDAT (`https://api.weather.gc.ca/`)
   are also supported but require small adaptations to the dashboard's
   `MAP_STATIONS` / `REGIONAL_STATIONS` arrays.
2. Set `STATION_IDS` in `.env`.
3. Edit [`dashboard/index.html`](../../dashboard/index.html) — update the
   relevant station-array constants, `STATION_NAMES`, `RIVER_ROUTE`,
   `HOME_PIN`, etc. The constants are clustered near the top of the script
   block.

## Production hardening

These are deliberate omissions for the quickstart; address them for any
serious deployment:

- The cron sidecars use `sleep` loops. Replace with systemd timers, host
  cron, or a real scheduler (Kubernetes CronJobs — see
  [`../kubernetes/`](../kubernetes/)).
- TimescaleDB has no backups configured.
- PostgREST runs as the DB owner (`PGRST_DB_ANON_ROLE` = the user). For
  production, create a read-only role and use that.
- nginx runs HTTP only. Front with a TLS-terminating reverse proxy
  (Caddy / Traefik / Cloudflare Tunnel) in production.

## Stopping & cleaning up

```bash
docker compose down            # stop, keep volumes
docker compose down -v         # stop and delete the database volume too
```
