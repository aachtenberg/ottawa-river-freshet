# ORRPB main-stem flows and levels ingester

Daily Python script that scrapes two tables on the ORRPB conditions pages
and upserts them via PostgREST:

| ORRPB table | Page | Target table | Stations |
|---|---|---|---|
| "Average Daily Flows (m3/s)" | `ottawariver.ca/conditions/?display=river` | `orrpb_river_flows` | Temiscaming, Otto Holden, Des Joachims, Chenaux, Chats Falls, Britannia, Carillon |
| "Water levels at 24:00h in metres" | `ottawariver.ca/conditions/` | `orrpb_river_levels` | Otto Holden, Mattawa, Des Joachims, Pembroke, Lake Coulonge, Chenaux, Chats Lake, Britannia, Gatineau, Thurso, Grenville, Carillon |

Stdlib-only (urllib + html.parser). HTTP goes through `orrpb_http.py`
(shipped next to the script, same copy as the other two ORRPB scrapers):
ottawariver.ca sits behind a CDN that sometimes hands out a dead edge
node, so 5xx and network errors are retried a few times, spaced past the
DNS cache.

## Why this exists

The OPG main-stem dams (Otto Holden, Des Joachims, Chenaux, Chats Falls)
are not in the Hydro-Québec open-data feed that `hq-ingest` reads, and
only ORRPB publishes flows and headwater levels for them. The flows table
is what the dashboard's Flow tab and the community's "current vs median"
flow charts ride on; the levels table is the daily "Ottawa River Water
Levels" bar chart that gets re-shared on social media.

ORRPB publishes an 8-day rolling window for both, so each run re-uploads
the window and the `merge-duplicates` upsert picks up revisions. ORRPB's
most recent day is preliminary and often revised; a round number or a `0`
in the latest slot is usually a placeholder, not a reading.

## How it works

1. Fetch each page, walk every `<table>` with `html.parser`, and pick the
   one whose row labels match the station list.
2. The header row carries the dates; each value cell becomes one
   `(station, time)` row with `agency` set from the row label.
3. Upsert via PostgREST POST with `Prefer: resolution=merge-duplicates`.

Station slugs are stable (`temiscaming`, `otto-holden`, `des-joachims`,
`chenaux`, `chats-falls`, `britannia`, `carillon`; levels add `mattawa`,
`pembroke`, `lake-coulonge`, `chats-lake`, `gatineau`, `thurso`,
`grenville`) and match the slugs `orrpb-station-history` uses where the
two overlap.

## Configuration

| Variable | Default | Notes |
|---|---|---|
| `POSTGREST_URL` | `http://postgrest:3000` | PostgREST endpoint: set by the compose file and the k8s manifests; the script's own default is the upstream cluster's `postgrest.data.svc.cluster.local:3000` |
| `ORRPB_RIVER_URL` | the flows page | Override the flows URL |
| `ORRPB_LEVELS_URL` | the conditions page | Override the levels URL |
| `SCRAPE_USER_AGENT` | `freshet-xgrunt-com/1.0 (…)` | Identify your deployment to ORRPB |
| `ORRPB_FETCH_ATTEMPTS` / `ORRPB_FETCH_RETRY_WAIT_S` | `5` / `35` | Retry count and spacing in `orrpb_http.py` |

## Schedule

ORRPB updates mid-afternoon Eastern. The deploy manifests run it daily at
21:40 UTC, between `reservoir-ingest` (21:30) and `orrpb-station-history`
(21:50); the upstream maintainer's cluster runs it 6-hourly. Re-running is
idempotent.

## Schema

`orrpb_river_flows (time date, station text, flow_cms double precision,
agency text, PRIMARY KEY (station, time))` and `orrpb_river_levels (time
date, station text, level_m double precision, agency text, PRIMARY KEY
(station, time))`, plus `latest_orrpb_river_flows` / `latest_orrpb_river_levels`
views, all in [`ingesters/river-history/bootstrap.sql`](../river-history/bootstrap.sql).

## Disclaimer

ORRPB publishes this data "use at your own risk" and states it may not be
reproduced or redistributed. This ingester caches it for case-file
analysis; community-facing output cites ORRPB and presents derived
statistics, not the raw tables.
