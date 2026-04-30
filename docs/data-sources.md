# Data sources

Every external data source the dashboard reads from, with endpoint shapes,
licensing, and notes on stability.

## 1. Quebec MSP Vigilance

- **Base URL**: `https://inedit-ro.geo.msp.gouv.qc.ca`
- **Endpoints**:
  - `/station_details_metadata_api?id=eq.<vigilance_id>` — station metadata
  - `/station_details_readings_api?id=eq.<vigilance_id>` — ~72 h reading buffer
- **Auth**: none, CORS-friendly
- **Format**: PostgREST JSON (`[{ ... }]`)
- **Cadence**: Vigilance updates hourly on the hour, data lands within ~10 min.
  This stack polls the browser every 10 min and the cron ingester every hour
  at :12.
- **License**: Public data published by Quebec's Ministry of Public Safety.
- **Stability**: Undocumented but stable for years. Schema evolves rarely.

Used for: live river levels for Quebec gauges + a few mirrored Ontario gauges
(Mattawa, Témiscaming, Britannia).

## 2. ECCC Real-Time Hydrometric

- **Base URL**: `https://api.weather.gc.ca`
- **Endpoints**:
  - `/collections/hydrometric-stations/items?STATION_NUMBER=<wsc_id>` — station metadata
  - `/collections/hydrometric-realtime/items?STATION_NUMBER=<wsc_id>` — live data
  - `/collections/hydrometric-annual-statistics/items?STATION_NUMBER=<wsc_id>` — historical annual peaks (used for percentile fallback)
- **Auth**: none
- **Format**: GeoJSON FeatureCollection
- **Cadence**: ~5 min refresh
- **License**: Open Government Licence — Canada
- **Stability**: ECCC's OGC API is well-documented and stable.

Used for: historical annual peaks (synthetic flood-state classification for
stations Vigilance can't classify).

## 3. open-meteo

- **Base URL**: `https://api.open-meteo.com/v1/forecast`
- **Auth**: none (free tier covers this stack's volume)
- **Format**: JSON
- **Cadence**: refreshed by open-meteo every ~30 min; this stack polls every
  10 min from the browser
- **License**: CC BY 4.0
- **Multi-location support**: pass comma-separated lat/lon and get an array
  back. The dashboard uses this to fetch all 6 freeze-tracker stations in one
  HTTP call (avoids per-IP rate limit on parallel single-location requests).

Used for: hourly temperature + 48 h precipitation forecasts at the basin
weather points.

## 4. ORRPB Conditions

- **URL**: `https://www.ottawariver.ca/conditions/?display=reservoir`
- **Format**: HTML table, 8-day rolling window
- **Auth**: none (public page)
- **Cadence**: ORRPB updates daily, mid-afternoon Eastern. The reservoir
  ingester runs at 21:30 UTC (~17:30 EDT / 16:30 EST) to land just after.
- **License**: ORRPB asserts "use at your own risk"; this stack scrapes the
  public page and re-displays for community awareness only. Always direct
  authoritative inquiries to ORRPB.

Used for: reservoir levels and flows. The HTML structure has been stable but
isn't a contract — if it breaks, the parser at
[`ingesters/reservoir-ingest/scrape.py`](../ingesters/reservoir-ingest/scrape.py)
needs adjustment.

## 5. Kisters KiWIS (optional)

- **Base URL**: instance-specific. The river-history ingester is wired to
  `https://waterdata.quinteconservation.ca/KiWIS/KiWIS` for Mississippi
  Valley Conservation Authority gauges (Buckhams Bay etc.) but easily
  retargetable.
- **Auth**: none for the public MVCA endpoint
- **Format**: JSON via `getTimeseriesValues`
- **Cadence**: ~hourly updates
- **License**: per-instance — check terms for any KiWIS instance you query.

Used for: optional non-Vigilance gauges (set the `MVCA_STATIONS` env var to
enable; default is one station as a working example).

## 6. ntfy (outbound, alerter only)

- **Default**: `https://ntfy.sh` (public free tier)
- **Self-host option**: any ntfy instance reachable from your cron.

Used for: threshold-crossing notifications. Configure via `NTFY_URL` and
`NTFY_TOPIC` env vars on the alerter.

## Storage

The river-history and reservoir-ingest jobs write to a TimescaleDB instance
(any Postgres ≥ 13 with the TimescaleDB extension). Schema:
[`ingesters/river-history/bootstrap.sql`](../ingesters/river-history/bootstrap.sql).

The dashboard reads from TimescaleDB via PostgREST under a `/history/` path —
configured by [`dashboard/nginx.conf`](../dashboard/nginx.conf). PostgREST is
the entire backend: no FastAPI, no Express, no custom middleware. The schema
view layer is the API.

## Caveats summary

| Source | Stability concern | Fallback |
|---|---|---|
| Vigilance | Undocumented JSON | Site change → fix client code |
| ECCC | Stable OGC API | Quota / 429 not seen yet |
| open-meteo | Free-tier limits | Bulk-call pattern stays under |
| ORRPB | HTML scraping | Fix parser if structure changes |
| KiWIS (MVCA) | Per-instance | Skip if endpoint moves |
