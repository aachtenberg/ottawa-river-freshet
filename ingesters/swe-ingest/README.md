# Snow-water-equivalent ingesters

Three scripts write the same table, `swe_daily (time, region, source,
swe_mm, swe_dep_mm)`, one row per region per day, so the snowpack feeding
a freshet can be compared across sources and years. They are the input to
the case file's snowpack analyses (the "is the north carrying more than
the maps showed" question), not to the dashboard.

| Script | Source | Cadence | Auth | Regions |
|---|---|---|---|---|
| `caldas_ingest.py` | ECCC GeoMet, CaLDAS-NSRPS 2.5 km SWE analysis | daily, forward only | none | 16 named points across the sub-basins (`source='caldas-nsrps'`) |
| `era5_ingest.py` | Copernicus ERA5-Land `snow_depth_water_equivalent` | daily, history back to 1950 | CDS token + licence | `basin-total`, `north-half`, `south-half` means (`source='era5land'`) |
| `canswe_ingest.py` | CanSWE in-situ archive (snow courses, pillows, gamma sensors) | one-shot, when a new release drops | manual download | Ottawa-basin stations (`source='canswe'`) |

## CaLDAS-NSRPS (`caldas_ingest.py`)

Samples the GeoMet WMS layer `CaLDAS-NSRPS_2.5km_SnowWaterEquiv` with
`GetFeatureInfo` at a fixed list of points: upper Ottawa and the northern
headwaters (Témiscaming, Ville-Marie, Rouyn-Noranda, Val-d'Or, Parent,
Dozois, Mattawa), the Gatineau (Maniwaki, Baskatong, Sainte-Anne-du-Lac),
the Lièvre (Mont-Laurier, Lac-du-Cerf) and the lower main stem (Pembroke,
Petawawa headwaters, Fort-Coulonge, Ottawa). Points rather than an area
mean because `python:3.12-alpine` has no GDAL and `GetFeatureInfo` needs
no dependencies; the points were chosen to match the labels on ORRPB's
biweekly SWE map and the ECCC climate stations the case file already uses.
Sub-basin means are an aggregate over `swe_locations.subbasin`.

GeoMet serves only the current analysis, so there is no historical pull:
the archive accumulates from the day the cron starts. A snow-free point
comes back as an empty feature collection and is stored as `0.0`, not a
gap. Stdlib only. Env: `POSTGREST_URL`.

## ERA5-Land (`era5_ingest.py`)

Pulls one 00:00 UTC snapshot per day over an Ottawa-basin bounding box
(`ERA5_BBOX`, default `48.5,-80.0,45.0,-74.0` as N,W,S,E) and stores the
bbox mean plus the means north and south of 46.7 N. ERA5-Land runs from
1950 to about five days ago, so this is the deep-history feed.

It needs a Copernicus Climate Data Store account: set `CDS_API_KEY` to
your personal access token (the script writes `~/.cdsapirc` from it and
`CDS_API_URL`), and accept the ERA5-Land licence once on the CDS website
or every request returns 403. Dependencies `cdsapi`, `netCDF4` and `numpy`
are pip-installed at container start, which is why it runs on
`python:3.12-slim` rather than the alpine image the other ingesters share.

Modes: rolling (default, the last `ERA5_LOOKBACK_DAYS` days, 14) or
backfill (`ERA5_START` / `ERA5_END`, fetched year by year so a partial run
is resumable). The 1950-to-present backfill is a one-shot job; the comment
block in `deploy/kubernetes/85-swe-ingest-cron.yaml` has the recipe.

In the public tier this runs **on Kubernetes only**. The docker-compose
deploy carries CaLDAS and not ERA5: the credential, the licence step and
the hours-long first backfill do not belong in a stack whose point is that
it needs nothing beyond `docker compose up`. Run `era5_ingest.py` by hand
against the compose PostgREST if you want the history there.

## CanSWE (`canswe_ingest.py`)

Loads the Ottawa-basin stations from the Canadian historical Snow Water
Equivalent database (Vionnet et al., ESSD 2021; DOI 10.20383/103.0329,
Open Government Licence Canada) into `swe_daily` with `source='canswe'`.
This is the ground truth the gridded analyses approximate: manual snow
surveys, snow pillows and passive-gamma sensors run by Ontario MNR, OPG,
Hydro-Québec and MSC, roughly monthly in winter. The archive is a single
NetCDF behind Globus auth, so it is not cron-friendly: download it, then

```bash
python3 canswe_ingest.py /path/to/CanSWE-CanEEN_YYYY-YYYY_vN.nc
```

(or `CANSWE_NC=…`). Needs `netCDF4` and `numpy`. Re-running is idempotent.
There is no manifest for it in `deploy/kubernetes/`; the upstream maintainer's
private cluster keeps a suspended `swe-canswe-bootstrap` CronJob as the place
to run it from, and the archive itself is checked in under
[`data/canswe/`](../../data/canswe/).

## Schema

`swe_daily`, `swe_locations` and the `latest_swe_daily` view are in
[`ingesters/river-history/bootstrap.sql`](../river-history/bootstrap.sql).
CanSWE's `snw` is kg m⁻², which is mm of SWE 1:1; ERA5-Land's variable is
metres of water equivalent and is converted to mm on write.
