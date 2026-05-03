# Ottawa River Freshet — community flood-monitoring stack

A self-contained, browser-rendered flood-monitoring dashboard for the **Ottawa
River watershed** (Mansfield / Fort-Coulonge / Lac Coulonge area), with daily
reservoir scraping, threshold-crossing alerts, and 50+ years of historical
context built in. Deploys as a static HTML page + a TimescaleDB-backed
PostgREST API + a handful of Python cron jobs.

> **Status**: production-ready. Running live at the maintainer's homelab; this
> repo is the upstream source.

## What's in the box

```
┌─────────────────────────────────────────────────────────────┐
│  Browser dashboard (static HTML, Chart.js, Leaflet)         │
│   • Hero card for your property gauge                       │
│   • Watershed snapshot bar chart                            │
│   • Per-station charts with 1 h → 30 d windows              │
│   • Reservoirs tab (ORRPB-derived % full + HQ outflow)      │
│   • Tributaries tab (Gatineau + Lièvre cascades)            │
│   • Operations tab (live Hydro-Québec release telemetry)    │
│   • Slide-out map: Dams / Reservoirs / Releases / Cascade   │
│   • EN / FR + light / dark + mobile-responsive              │
└─────────────────────────────────────────────────────────────┘
            ▲                   ▲                ▲
   public APIs                in-cluster       hourly + daily
   (Vigilance,                 PostgREST       cron jobs:
    Hydro-Québec open-data,    + TimescaleDB   • Vigilance/KiWIS ingest
    WSC, ECCC, open-meteo,                     • ORRPB reservoir scrape
    ORRPB)                                     • HQ open-data ingest
                                               • WSC realtime ingest
                                               • ECCC daily-climate ingest
                                               • Threshold alerter (ntfy)
```

## Quick start (Docker Compose)

```bash
git clone https://github.com/aachtenberg/ottawa-river-freshet.git
cd ottawa-river-freshet/deploy/docker-compose
cp .env.example .env   # edit DB password, station list, etc.
docker compose up -d
# Dashboard at http://localhost:8080 — first ingest runs immediately,
# subsequent ones on the cron schedule.
```

See [`deploy/docker-compose/README.md`](deploy/docker-compose/README.md) for
details, or [`deploy/kubernetes/README.md`](deploy/kubernetes/README.md) for a
plain-Kubernetes deployment example.

## Repo layout

| Path | Contents |
|---|---|
| [`dashboard/`](dashboard/) | Static HTML + nginx config. The whole UI is one self-contained `index.html`. |
| [`ingesters/river-history/`](ingesters/river-history/) | Hourly Python ingester for Vigilance + KiWIS gauges → TimescaleDB. Also fetches reanalysis weather observations from open-meteo. |
| [`ingesters/reservoir-ingest/`](ingesters/reservoir-ingest/) | Daily Python scraper for the ORRPB reservoir conditions page. Stdlib-only. |
| [`alerter/`](alerter/) | Hourly threshold-crossing alerter that posts to ntfy. |
| [`data/`](data/) | Reference / archival CSVs: 54-yr Lac Coulonge monthly means, 15-station ORRPB peak history. |
| [`docs/`](docs/) | Architecture, methodology, data-source notes. |
| [`deploy/`](deploy/) | Docker Compose + generic Kubernetes deploy recipes. |

## Configuration

Everything is environment-variable driven. The two main things to customize for
your own watershed/property:

1. **Property GPS** — `HOME_PIN` constant in [`dashboard/index.html`](dashboard/index.html). Or wire a live source via the `/history/esp_gps` view if you have a GPS device feeding the same TimescaleDB.

2. **Property thresholds** — `PROPERTY_THRESHOLDS` constant in `dashboard/index.html` and `THRESHOLDS` list in [`alerter/alerter.py`](alerter/alerter.py). Both hard-coded to match the Mansfield property's 2019 flood observations; replace with your own observed levels.

3. **Stations of interest** — `STATION_IDS` env var on the river-history ingester (Vigilance station numeric IDs). The dashboard's `MAP_STATIONS`, `REGIONAL_STATIONS`, and `CORRIDOR_BAR_STATIONS` arrays should match.

4. **Reservoir limits** — [`dashboard/reservoir-limits.json`](dashboard/reservoir-limits.json). Calibrated against ORRPB-published readings; methodology documented in [`docs/methodology.md`](docs/methodology.md).

## Data sources

| Source | License / terms | Used for |
|---|---|---|
| [Quebec MSP Vigilance](https://vigilance.geo.msp.gouv.qc.ca/) | Public data, no auth | Live river levels for Quebec gauges |
| [ECCC HYDAT real-time](https://api.weather.gc.ca/) | Open Government Licence — Canada | Live levels for Ontario stations + historical annual peaks |
| [open-meteo](https://open-meteo.com/) | CC BY 4.0 (free tier) | Hourly temperature + precipitation forecasts |
| [ORRPB](https://ottawariver.ca/) | Disclaimed — see their site | Reservoir levels and flows (scraped daily) |
| [Kisters KiWIS](https://www.kisters.net/kiwis/) | Per-instance terms (this repo uses the public MVCA endpoint) | Optional: Mississippi Valley Conservation Authority gauges |

See [`docs/data-sources.md`](docs/data-sources.md) for endpoint shapes and
caveats. **None of these sources require auth.** All API calls go either from
the visitor's browser directly or from the in-cluster cron jobs.

## Methodology highlights

- **Reservoir percent-full** — linear interpolation between published low/high
  operating limits per reservoir. Calibrated against community-published
  values. Full notes in [`docs/methodology.md`](docs/methodology.md).
- **Datum offsets** — Ontario gauges via ECCC's "assumed datum" report ~100 m
  below MASL. The dashboard converts on display via per-station offsets.
- **Synthetic flood-state classification** — for stations Vigilance can't
  classify (e.g. Mattawa, Témiscaming village), the dashboard falls back to
  ORRPB reference-year crossings, then ECCC long-record percentile.

## Disclaimers

This is a **community-maintained, unofficial** dashboard. It is not authoritative
for emergency decisions. Always consult the [Ottawa River Regulation Planning
Board](https://ottawariver.ca/forecasts) and local emergency management
authorities for official guidance.

The reservoir percent-full methodology is approximate and uses public-domain
operating limits; operators apply additional non-linear and seasonal factors
that this dashboard doesn't model.

## License

[MIT](LICENSE). Pull requests welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Acknowledgements

- **Dan Poole** for the reservoir percent-full methodology and operating-limit
  calibration.
- **Ottawa River Regulation Planning Board** and the operating agencies (HQ,
  OPG, MELCCFP, Evolugen, PSPC) for the public data feeds.
- The **Northern Reservoirs Ottawa River Tourism Wildlife Flood Watch Group**
  community for context and historical observations.
