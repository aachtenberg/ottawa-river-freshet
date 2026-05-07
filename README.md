# Ottawa River Freshet — community flood-monitoring stack and case file

A self-contained, browser-rendered flood-monitoring dashboard for the **Ottawa
River watershed** (Mansfield / Fort-Coulonge / Lac Coulonge area), paired with
a multi-year analytical case file investigating the post-2017 regime change in
freshet behaviour at the regulated reach. Live telemetry + historical context +
quantitative analysis + community engagement, all in one repository.

> **Status**: production-ready monitoring stack + actively maintained case file.
> Live at the maintainer's homelab; this repo is the upstream source.

## What this project is

Two complementary halves around the same data:

```
┌─────────────────────────────────────┐  ┌─────────────────────────────────────┐
│  LIVE MONITORING STACK              │  │  ANALYTICAL CASE FILE               │
│                                     │  │                                     │
│  • Browser dashboard with live      │  │  • 8-exhibit editorial-style        │
│    gauge + reservoir + cascade      │  │    argument (Exhibits 0, A–G)       │
│    telemetry, EN/FR, mobile-ready   │  │  • Test A peak step-location at     │
│  • Hourly ingest from Vigilance,    │  │    2017                             │
│    HQ open-data, WSC, ECCC, ORRPB   │  │  • Test B climate forcing           │
│  • Daily reservoir storage scrape   │  │  • Test C annual volume + Test C    │
│  • TimescaleDB + PostgREST proxy    │  │    addendum (window cherry-pick,    │
│  • Threshold alerter via ntfy       │  │    snow-vs-rain decomposition)      │
│  • Daily brief routine (Claude      │  │  • Carillon §15.3.5.1 directive     │
│    agent committing to git)         │  │    enforcement gap                  │
│  • Carillon §15.3.5.1 directive     │  │  • Bryson refurbishment timeline    │
│    auto-check                       │  │  • Community-notes archive of FB    │
│                                     │  │    threads, CBC article, contacts   │
└─────────────────────────────────────┘  └─────────────────────────────────────┘
            ▲                                        ▲
            │                                        │
   Public APIs (no auth):                Multi-decade historical
   Vigilance, HQ open-data,              (1915–2026, depending on
   WSC HYDAT + realtime, ECCC,           gauge): WSC HYDAT bulk
   open-meteo, ORRPB                     archive, ORRPB monthly
                                         summaries, ECCC station
                                         daily climate, plus
                                         operator open-data feeds
```

## The case-file argument in brief

The Ottawa River had **one major flood at Lac Coulonge between 1972 and
2016** (45 years, one event). Since 2017, it has had **four**: 2017, 2019,
2023, 2026. That's an 18-fold increase in super-flood frequency in a single
decade.

The case file decomposes that regime change into **two simultaneous co-drivers**:

1. **A basin-wide ~+17 % increase in annual integrated flow volume** at
   Britannia (Welch t = 2.85, p ≈ 0.004), preserved through downstream gauges
   at Pointe-Calumet (+0.18 m annual mean) and Pointe-Claire (+0.21 m). About
   half is associated with annual-precipitation increases at watershed
   stations; the other half is unexplained at station-level data and likely
   reflects land-use change or upper-basin precipitation the case file's
   station sample misses. **This part is climate / land-use driven and not
   in operator control.**
2. **A sharp peak-shape step at exactly 2017** at Lac Coulonge (+59 cm in
   mean annual peak), spatially concentrated near the regulated reach, that
   dissipates by Pointe-Claire downstream of Beauharnois. Climate-forcing
   tests cannot reproduce its shape or its spatial concentration. **This
   part is operations-attributable and aligned in time with the Bryson
   2017–2023 refurbishment.**

The two findings are **additive, not competing** — bigger river plus
operator-amplified peaks. The policy ask is correspondingly two-part: yes,
adapt to climate; AND adapt the operating playbook (snowpack-indexed earlier
drawdown, enforce HQ's own published Carillon Water Management Plan
ceilings during freshet).

Read [`docs/exhibits/Exhibit_0_Plain_Language.html`](docs/exhibits/Exhibit_0_Plain_Language.html)
first for the plain-English version. Lettered exhibits show the work. Full
case file: [`docs/analysis/Freshet_2026_Complete_Summary.md`](docs/analysis/Freshet_2026_Complete_Summary.md).

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
| [`alerter/`](alerter/) | Hourly threshold-crossing alerter that posts to ntfy. |
| **Live ingesters** | |
| [`ingesters/river-history/`](ingesters/river-history/) | Hourly Vigilance + KiWIS ingest → TimescaleDB; reanalysis weather from open-meteo. |
| [`ingesters/reservoir-ingest/`](ingesters/reservoir-ingest/) | Daily ORRPB reservoir scrape (stdlib only). |
| [`ingesters/hq-ingest/`](ingesters/hq-ingest/) | Hourly Hydro-Québec open-data ingest (centrales releases + station levels). |
| [`ingesters/wsc-ingest/`](ingesters/wsc-ingest/) | Hourly Water Survey Canada realtime ingest. |
| [`ingesters/eccc-ingest/`](ingesters/eccc-ingest/) | ECCC daily climate ingest (precipitation, temperature). |
| **Historical / analytical ingesters** | |
| [`ingesters/climate-history/`](ingesters/climate-history/) | One-shot loaders and analytical scripts: `wsc_hydat_load.py` (178k rows from 9 Ottawa-basin stations 1915–2025), `stepchange_analysis.py` (Test A), `lc_brit_regression.py` (per-event amplification), `annual_volume_test.py` (Test C), `seasonal_window_analysis.py` (Test C addendum), `lac_coulonge_climate_regression.py`. |
| [`ingesters/orrpb-historical-summaries/`](ingesters/orrpb-historical-summaries/) | One-shot loader for ORRPB published monthly summaries 1972–2025. |
| **Analysis and exhibits** | |
| [`docs/analysis/`](docs/analysis/) | `Freshet_2026_Complete_Summary.md` — the full case file with all tests, regulatory analysis, and findings. |
| [`docs/exhibits/`](docs/exhibits/) | Editorial-style HTML+PNG exhibits: 0 (plain-language reader), A (regime change), B (winter baseline), C (storage capacity), D (Bryson timeline), E (climate tested), F (corrective failure), G (selected window). Rendered via `render_pngs.js`. |
| [`docs/reports/`](docs/reports/) | Primary-source documents: McNeil 2019 PDF, 2004 Carillon IWMP operating envelope, 2002 Haxton-Chubbuck extract. |
| [`docs/`](docs/) | `architecture.md`, `methodology.md`, `data-sources.md`, `backlog.md`. |
| **Reference and community data** | |
| [`data/`](data/) | Reference / archival CSVs: 54-year Lac Coulonge monthly means, ORRPB historic peaks 1972–2025, ORRPB monthly summaries by gauge (Britannia, Carillon, Pembroke, etc.), WSC HYDAT extracts (9 stations), ECCC climate (8 stations), HQ open-data ledger. |
| [`data/daily-briefs/`](data/daily-briefs/) | Daily basin-state briefs generated by the freshet-daily-brief routine, committed automatically. |
| [`data/community-notes/`](data/community-notes/) | Dated archives of community-discussion artifacts (CBC article + FB threads, named contributors, validation tables). |
| **Scheduled remote agents** | |
| [`routines/`](routines/) | Prompt-as-code source for scheduled Claude Code routines (daily brief, ingest health-check). Live routines on claude.ai are kept in sync with these files. |
| **Deployment** | |
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
| [Hydro-Québec open-data](https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/) | Open Data Licence | Live centrales releases (turbined / spilled / total) and station headpond / tailwater levels |
| [ECCC HYDAT real-time](https://api.weather.gc.ca/) | Open Government Licence — Canada | Live levels for Ontario stations |
| [WSC HYDAT bulk archive](https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/) | Open Government Licence — Canada | Daily flow / level historical record (1915–) at 9 Ottawa-basin stations |
| [ECCC daily climate](https://climate.weather.gc.ca/) | Open Government Licence — Canada | Multi-decade daily precipitation + temperature at 8 watershed stations |
| [open-meteo](https://open-meteo.com/) | CC BY 4.0 (free tier) | Hourly temperature + precipitation forecasts |
| [ORRPB](https://ottawariver.ca/) | Disclaimed — see their site | Reservoir levels and flows (scraped daily); published monthly historical summaries |
| [Kisters KiWIS](https://www.kisters.net/kiwis/) | Per-instance terms (this repo uses the public MVCA endpoint) | Optional: Mississippi Valley Conservation Authority gauges |

See [`docs/data-sources.md`](docs/data-sources.md) for endpoint shapes and
caveats. **None of these sources require auth.** All API calls go either from
the visitor's browser directly or from the in-cluster cron jobs.

## Daily-brief routine

A scheduled remote Claude Code agent runs at 11:00 UTC daily, queries the
PostgREST proxy, scrapes the ORRPB conditions page, and commits a structured
markdown brief to [`data/daily-briefs/`](data/daily-briefs/). The brief
auto-checks: Lac Coulonge level + flood state, Bryson operating posture,
the full HQ cascade, the Carillon §15.3.5.1 directive, top-4 reservoir
storage deltas, and ORRPB forecast text changes. Anomalies above documented
thresholds are flagged in a dedicated section.

The prompt source-of-truth lives at [`routines/freshet-daily-brief.md`](routines/freshet-daily-brief.md).
Live routine is kept in sync via the `RemoteTrigger` API — see
[`routines/README.md`](routines/README.md).

## Methodology highlights

- **Reservoir percent-full** — linear interpolation between published low/high
  operating limits per reservoir. Calibrated against community-published
  values. Full notes in [`docs/methodology.md`](docs/methodology.md).
- **Datum offsets** — Ontario gauges via ECCC's "assumed datum" report ~100 m
  below MASL. The dashboard converts on display via per-station offsets.
- **Synthetic flood-state classification** — for stations Vigilance can't
  classify (e.g. Mattawa, Témiscaming village), the dashboard falls back to
  ORRPB reference-year crossings, then ECCC long-record percentile.
- **Step-change tests** — Britannia annual-peak shift maximises sharply at
  2017 (+19.3 % median); Pointe-Calumet AMJ-mean +40 cm in 2016–24 with no
  equivalent step at the more distant Pointe-Claire (spatial signature of
  operations, not climate). Detail in
  [`docs/analysis/Freshet_2026_Complete_Summary.md`](docs/analysis/Freshet_2026_Complete_Summary.md)
  and the source scripts in [`ingesters/climate-history/`](ingesters/climate-history/).
- **Annual integrated volume** — Britannia daily-flow integration 1960–2024;
  +17 % step pre/post-2017 confirmed at downstream Pointe-Calumet and
  Pointe-Claire annual-mean levels. Cherry-pick check on the ORRPB May 2026
  "50-year record precipitation" claim shows it survives only in the
  selected 6-week window; surrounding seasonal windows show 2026 as
  middle-of-the-pack or 2nd-driest. Temperature decomposition shows the
  upper-basin "precipitation" was snowfall on a frozen basin, not rain.

## Community engagement

The case file develops in dialogue with the local riparian community,
particularly the Northern Reservoirs / Ottawa River / Tourism / Wildlife /
Flood Watch Facebook group. Major threads, technical exchanges, and named
contributors are archived in [`data/community-notes/`](data/community-notes/)
with engagement-validation tables tying community claims to repository
analyses. Active investigation tracks (e.g. **Exhibit H — Ecological
regime change**) are scoped in [`docs/backlog.md`](docs/backlog.md) and
mirrored to public GitHub issues for collaborator visibility.

## Disclaimers

This is a **community-maintained, unofficial** project. The monitoring
dashboard is not authoritative for emergency decisions — always consult the
[Ottawa River Regulation Planning Board](https://ottawariver.ca/forecasts)
and local emergency management authorities for official guidance.

The reservoir percent-full methodology is approximate and uses public-domain
operating limits; operators apply additional non-linear and seasonal factors
that this dashboard doesn't model.

The case-file analyses are the maintainer's own work, drawing on community
contributions where credited. Findings are reproducible from the source
scripts and public data, but conclusions are the maintainer's
interpretation; all claims are open to review and refutation.

## License

[MIT](LICENSE). Pull requests welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Acknowledgements

- **Contributor A** for the regime-change empirical analysis (Lac Coulonge
  yearly peaks 1972–2026; the 18-fold super-flood frequency increase that
  anchors Exhibit A).
- **Contributor B** for the reservoir percent-full methodology,
  operating-limit calibration, and operator-side mechanism validation.
- The **Northern Reservoirs / Ottawa River / Tourism / Wildlife / Flood
  Watch** Facebook group community for context, historical observations,
  and continuing challenge of the case-file argument. Public-thread
  contributions and verbatim quotes are archived (with attribution to the
  posters' public posts) in [`data/community-notes/`](data/community-notes/).
- The **Ottawa River Regulation Planning Board** and the operating agencies
  (Hydro-Québec, Ontario Power Generation, MELCCFP, Evolugen, Public
  Services and Procurement Canada) for the public data feeds.
- The **Ottawa Riverkeeper** for ecological-monitoring research that
  informs the Exhibit H ecological-regime scoping.

See [`CONTRIBUTORS.md`](CONTRIBUTORS.md) for the full attribution policy.
Specific community members whose private/working-document contributions
underpin case-file analysis are referenced by placeholder labels rather
than by name.
