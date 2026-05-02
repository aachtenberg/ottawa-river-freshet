# HQ-ingest

Hourly Python script that pulls Hydro-Québec's two public open-data JSON feeds
and upserts them into TimescaleDB via PostgREST. Captures release telemetry
(turbine + spillway + total) for every HQ generating station in the Ottawa
basin, plus headpond/tailwater levels for the gauging stations near each dam.

Stdlib-only — no `pip install` required at runtime, just Python 3.10+.

## What it ingests

1. **`Donnees_VUE_CENTRALES_ET_OUVRAGES.json`** — per-station hourly discharge
   series (`Débit total`, `Débit turbiné - <name>`, `Débit déversé - <name>`)
   plus daily filtered local inflow (`Apport filtré`). Writes to:
   - `dam_releases` — hourly total/turbined/spilled by `site_id`.
   - `dam_inflows` — daily filtered local inflow.
   - `dam_sites` — site metadata (name, region, coords, commissioning date).
2. **`Donnees_VUE_STATIONS_ET_TARAGES.json`** — hourly water-level readings at
   the gauging-station network. (Despite "TARAGES" in the filename, no
   Q-vs-H rating curves are included — these are pure level series.) Writes to:
   - `dam_levels` — hourly level by `station_id`.
   - `dam_sites` — same metadata table, with `kind='station'`.

Each pull contains roughly 10 days of hourly history (~245 readings per series),
which keeps inserts cheap and lets the cron tolerate missed runs.

## Schema

Schema lives in the consuming TimescaleDB bootstrap file (see
`deploy/kubernetes/10-timescaledb.yaml` in this repo's `freshet/init-sql`
ConfigMap, or whatever your equivalent is). Five hypertables/views are
created idempotently:

- `dam_releases` (hypertable)
- `dam_inflows` (hypertable)
- `dam_levels` (hypertable)
- `dam_sites` (regular table — used for upserts via merge-duplicates)
- `latest_dam_releases`, `latest_dam_levels` (views)

## Geographic filter

The script filters to the Ottawa basin window by default (lat 45–48, lon
-80 to -74). Adjust `HQ_LAT_MIN`/`HQ_LAT_MAX`/`HQ_LON_MIN`/`HQ_LON_MAX` to
cover the Saguenay, Manicouagan, La Grande, etc.

## TLS quirk

`hydroquebec.com`'s CDN refuses Python's default Alpine OpenSSL handshake
with `SSLV3_ALERT_HANDSHAKE_FAILURE`. The script lowers the security level
to 1 (`ctx.set_ciphers('DEFAULT:@SECLEVEL=1')`) and sets a polite UA.
Don't remove either if you refactor.

## Configuration (env)

| Variable | Default | Notes |
|---|---|---|
| `POSTGREST_URL` | `http://postgrest:3000` | Your PostgREST endpoint |
| `HQ_CENTRALES_URL` | (HQ canonical URL) | Override for testing against a local file |
| `HQ_STATIONS_URL`  | (HQ canonical URL) | Same — both URLs accept `file://` paths |
| `HQ_LAT_MIN` / `HQ_LAT_MAX` | `45.0` / `48.0` | Bounding box (degrees) |
| `HQ_LON_MIN` / `HQ_LON_MAX` | `-80.0` / `-74.0` | Bounding box (degrees) |
| `HQ_POST_BATCH` | `2000` | Rows per PostgREST POST; 2000 keeps each request well under 1 MB |

## Schedule

HQ refreshes its open-data JSON roughly twice per day. Pulling hourly is
overkill but cheap (~26 s, ~21 k rows ignored as duplicates) and gives
prompt visibility when the upstream feed lands. Offset the cron from your
other ingesters (e.g. `:27 past the hour`) so the API hits don't all stack
on `:00`.

## Cadence + idempotency

Each pull re-uploads the full ~10-day buffer. Upserts use
`Prefer: resolution=ignore-duplicates` for the hypertable rows (against the
`(site_id, time)` and `(station_id, time)` PKs) and
`Prefer: resolution=merge-duplicates` for site metadata so name/coordinate
corrections propagate.
