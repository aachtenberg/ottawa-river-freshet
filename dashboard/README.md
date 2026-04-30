# Dashboard

Single-file static HTML dashboard. The whole UI is one `index.html` (~165 KB
including inline CSS and JS) plus a few static assets. No build step.

## Files

| File | Purpose |
|---|---|
| `index.html` | Main dashboard — all CSS, JS, HTML inline |
| `nginx.conf` | nginx server config: serves the static files, proxies `/history/` to PostgREST |
| `favicon.svg` | The teal-pulse-on-blue favicon |
| `orw-dams.json` | Hydroelectric stations + major dams + principal reservoirs from the ArcGIS layer (~24 KB) |
| `reservoir-limits.json` | Operating limits + capacities for the % full computation |

## Customizing for your watershed

The dashboard's "shape" comes from a handful of constants near the top of the
`<script>` block in `index.html`. The most relevant ones:

| Constant | What it controls |
|---|---|
| `STATIONS` | Which stations get a per-station chart on the Overview tab |
| `PROPERTY_THRESHOLDS` | Property-specific level thresholds (status banner + property-thresholds card) |
| `HISTORICAL_PEAKS` | Peak years to overlay on the primary chart |
| `HISTORICAL_ANNUAL_MAX_DESC` | Sorted historical peaks for percentile rank |
| `FREEZE_STATIONS` | Basin weather points (lat/lon, role, group) |
| `REGIONAL_STATIONS` | Stations on the regional context row |
| `MAP_STATIONS` / `MAP_STATION_ROLES` | Stations on the map drawer |
| `RIVER_ROUTE` | Hand-curated waypoints for the animated river polyline |
| `STATION_NAMES` | Per-station EN/FR display names |
| `ORRPB_HISTORIC_PEAKS` | Per-station ORRPB reference peaks + datum offset |
| `RESERVOIR_LOCATIONS` | Reservoir lat/lon for the map's reservoir card layer |
| `RESERVOIR_ORDER` | Hydrological upstream→downstream order for the Reservoirs tab |
| `HOME_PIN` | Property location pin (placeholder by default) |

## Theming

Light/dark theme uses CSS variables on `:root`, with explicit overrides via a
`data-theme="light"|"dark"` attribute (set by the toolbar toggle, persisted in
`localStorage.theme`). If neither is set, the OS `prefers-color-scheme`
media query wins.

## Localization

EN/FR toggle lives in the header (also persisted in `localStorage.pageLang`).
Static labels carry `data-i18n="<key>"` attributes; translation lookup happens
in `applyPageLang()`. Map-only strings live in `MAP_LABELS`. Add a third
language by extending each dictionary.

## Backend dependencies

- **Vigilance API** at `https://inedit-ro.geo.msp.gouv.qc.ca/` — fetched
  directly from the browser. No proxy needed.
- **open-meteo** at `https://api.open-meteo.com/` — direct from the browser.
- **ECCC HYDAT OGC API** at `https://api.weather.gc.ca/` — direct from the
  browser, lazy-loaded for the synthetic-etat fallback.
- **ArcGIS Online** at `https://www.arcgis.com/sharing/rest/...` — only
  consulted when refreshing `orw-dams.json` from upstream.
- **PostgREST** under `/history/` — proxied by `nginx.conf` to your in-cluster
  PostgREST instance. This is the only piece that requires non-public
  infrastructure.

## Refreshing `orw-dams.json`

The dam/reservoir feature collection comes from a public ArcGIS web map
(`ab7d7778cb9b4730959f6903c576c6cd` — "Dams in the Ottawa River watershed").
A small Python extractor isn't shipped here yet; happy to upstream one if
useful. For now, the file in this repo is a snapshot.
