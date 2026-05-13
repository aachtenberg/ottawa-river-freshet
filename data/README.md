# Reference data

Archival CSVs used by the dashboard for historical context, the
primary-source climate and hydrometric series that back the freshet
climate-regression analysis, and the generated artifacts that the daily
brief routine and dashboard produce. The dashboard reference files are
not queried at runtime by the ingesters — they're either bundled into
the dashboard's JS constants or kept here as the canonical source for
those constants. The analysis datasets are consumed by ad-hoc analysis
scripts only. The generated artifacts at the bottom of this README are
written by scheduled jobs and read live by the dashboard / brief routine.

## Datasets for analysis (primary sources)

### `hq-opendata/`

Point-in-time snapshots of Hydro-Québec open-data telemetry cited by Exhibit D
(Bryson freshet 2026 daily ledger, headpond/tailwater hourly pair, cascade
peer comparison). The live data flows through the `hq-ingest` cron into
TimescaleDB; these CSVs are the static citation artifacts. See
[`hq-opendata/README.md`](hq-opendata/README.md).

### `eccc-climate/`

Daily precipitation, temperature, and snow records from 12 ECCC stations
covering the watersheds that drain to Lac Coulonge (1972–2026). Replaces
the meteostat-based pull from the earlier web-client analysis. See
[`eccc-climate/README.md`](eccc-climate/README.md) for stations, coverage
caveats, and re-run instructions.

### `wsc-hydrometric/`

Daily flow and water-level records from 9 WSC HYDAT stations on the
Ottawa River basin — Britannia, Bryson, Chats Falls, Coulonge (Fort-Coulonge
and Pontefract-Golf), Gatineau at Maniwaki, Portage-du-Fort, plus the
Pointe-Calumet and Pointe-Claire Carillon proxies on Lac des Deux-Montagnes /
Lac St-Louis. See [`wsc-hydrometric/README.md`](wsc-hydrometric/README.md) —
note the critical post-1994 coverage gap for Lac Coulonge area flow data,
which constrains the rating-curve verification question.

### `canswe/`

The Canadian historical Snow Water Equivalent database (CanSWE), Vionnet
et al., *Earth System Science Data* (2021) — v8 release covering 2963
stations × 35,642 daily timesteps (1928–2025) of manual snow surveys, snow
pillows, and passive-gamma SWE sensors. The committed `.nc` is the canonical
input the `swe-canswe-bootstrap` Job loads into the `swe_daily` hypertable
(Ottawa-basin subset only). See [`canswe/README.md`](canswe/README.md).

## Dashboard reference files

### `orrpb-historical-summaries/`

Scraped archival CSVs from the ORRPB historical-summary station pages. Includes
11 per-station CSVs plus a `manifest.csv` with source URLs, units, and year
coverage.

Schema for each station CSV:

| Column | Unit | Notes |
|---|---|---|
| `year` | — | Calendar year |
| `jan`–`dec` | page-dependent | Monthly means from the published ORRPB table |
| `annual_mean` | page-dependent | Annual mean |
| `daily_max` | page-dependent | Annual maximum daily value |
| `daily_min` | page-dependent | Annual minimum daily value |

Measure types currently present:
- `water_level` in `metres`
- `discharge` in `cubic_metres_per_second` (Carillon)

### `lac-coulonge-monthly-1972-2026.csv`

ORRPB monthly mean levels for **Lake Coulonge at Fort-Coulonge**, 55 years
(1972–2026). The 2026 row is partial — only `daily_max` is populated; the
monthly cells are `NA` until ORRPB publishes the end-of-year summary. Schema:

| Column | Unit | Notes |
|---|---|---|
| `year` | — | Calendar year |
| `jan`–`dec` | metres MASL | Monthly means; `NA` for missing months |
| `annual_mean` | metres MASL | Mean across the 12 monthly means |
| `daily_max` | metres MASL | Maximum daily reading observed that year |
| `daily_min` | metres MASL | Minimum daily reading |

`NA` markers: 1972 January, 1979 June, most of 1984, all of 2026 except
`daily_max`.

Used in the dashboard for:
- The percentile rank tag on Lac Coulonge's map callout
- The `HISTORICAL_PEAKS` overlay on the primary chart
- The historical context table in the upstream documentation

### `climate-overlay/lac_coulonge_climate_overlay.json`

Derived per-year overlay joining Lac Coulonge peaks to Feb–Mar peak
Snow-on-Ground and Apr–May total precipitation, aggregated across the three
upper-basin ECCC stations Val-d'Or A, Parent, and Barrage-Témiscamingue.
Produced by [`ingesters/climate-history/snowpack_overlay_analysis.py`](../ingesters/climate-history/snowpack_overlay_analysis.py)
from `eccc-climate/` + the Lac Coulonge monthly CSV; cross-checked by
`cross_check_overlay.py`. Schema is documented in `schema_version` plus the
top-level `stations`, `snowpack_window`, and `precip_window` keys. Backs
Exhibit H (climate overlay).

### `orrpb-historic-peaks-1972-2025.csv`

Cross-station historical peaks from the ORRPB "Know Your Levels" working
document (May 2025). 15 stations from Mattawa down to Carillon plus the
Gatineau River, with **2017 / 2019 / 2023 peak levels** and one observed
day in 2025. All values in metres MASL.

The `datum_offset_masl` column captures the constant to add to the live API
value to get MASL — `0` for Quebec stations (Vigilance reports MASL natively),
`100` for Ontario stations (ECCC's "assumed datum"), and `173.65` for
Témiscaming village.

Used in the dashboard for:
- Reference-year context labels ("above 2023, 81 cm below 2019" on cards)
- Synthetic flood-state classification when Vigilance has no thresholds
- The 2019-record reference line on the watershed snapshot bar chart

## Generated artifacts

These are written by scheduled jobs and the daily-brief routine, not edited
by hand. Committed so the public mirror has the same view the dashboard does.

### `forecast/latest.json`

Structured snapshot of the ORRPB conditions/forecast page, written by the
[`freshet-daily-brief`](../routines/freshet-daily-brief.md) routine alongside
each daily brief (not a separate cron). Captures the freshet-active flag,
further-increases language, station forecast lines, and the
`last_update_iso` / `next_update_expected_iso` ORRPB stamp. Read live by the
dashboard's post-peak status text via the GitHub raw URL — schema is
documented in the routine's "Structured forecast snapshot" section.

### `daily-briefs/`

Markdown briefs produced by the
[`freshet-daily-brief`](../routines/freshet-daily-brief.md) routine — one
per day named `YYYY-MM-DD.md`, plus `latest.md` pinned to the newest dated
brief. The routine itself updates `latest.md`; the
`mirror-freshet-public.yml` GitHub Actions workflow re-pins it via a fixup
commit when the routine forgets. Briefs cover freshet posture, ORRPB framing
checks, Carillon §15.3.5.1 compliance, and Bryson cascade state. The
routine runs at 22:00 UTC daily, after the ORRPB afternoon update.

### `community-notes/`

Hand-written briefs and one-off hydrograph snapshots authored as freshet
events warrant — e.g. the 2026-05-07 "freshet shape" and 2026-05-12
"freshet size" briefs, plus the Britannia hydrograph PNG referenced by
the latter. Less structured than `daily-briefs/`; treat as analytical
notes, not telemetry.

## Source disclaimers

These data are aggregated from ORRPB's public publications. ORRPB asserts
that its data is "use at your own risk" — this repository re-displays them
for community awareness only. For authoritative inquiries consult ORRPB,
Hydro-Québec, OPG, MELCCFP, or the relevant operator directly.

The 2025-05-06 "Know Your Levels" PDF that's the source of
`orrpb-historic-peaks-1972-2025.csv` is community-authored and ORRPB-disclaimed.
Citation: anonymous community publication via the Northern Reservoirs Ottawa
River Tourism Wildlife Flood Watch Group, used under fair-comment reuse for
flood awareness.
