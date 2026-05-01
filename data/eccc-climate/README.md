# ECCC daily climate data — Ottawa River basin stations

Daily precipitation, temperature, snow, and snow-on-ground records pulled
directly from Environment and Climate Change Canada (ECCC) for the
watersheds that feed Lac Coulonge. Used by the freshet climate-regression
analysis (replaces the meteostat-based pull from the earlier web-client
analysis).

## Source

ECCC bulk data download endpoint (one request per station per year returns
all daily rows for that year):

    https://climate.weather.gc.ca/climate_data/bulk_data_e.html
        ?format=csv&stationID={ID}&Year={YYYY}&Month=1&Day=1&timeframe=2

`timeframe=2` selects the daily product. Station IDs come from the ECCC
Station Inventory CSV at:

    https://collaboration.cmc.ec.gc.ca/cmc/climate/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv

## Re-running

    python3 ingesters/climate-history/eccc_pull.py            # all stations
    python3 ingesters/climate-history/eccc_pull.py <slug>     # one station

Per-year files are cached in `<slug>/raw/<year>.csv`; re-runs skip any
year that's already on disk and non-empty. Delete the raw file to force a
re-fetch. The ingester throttles at 1 req/sec.

## Layout

```
manifest.csv                       # station_id, climate_id, name, watershed, source URL pattern, output file
<slug>/
  daily-<first>-<last>.csv         # consolidated daily rows for that station's coverage
  raw/<year>.csv                   # per-year caches (raw ECCC bulk-CSV format)
```

## Stations

| slug | name | watershed | coverage |
|---|---|---|---|
| `ottawa-cda` | OTTAWA CDA | reference (south basin — replicates the meteostat web-session analysis) | 1972–2026 |
| `maniwaki-ua` | MANIWAKI UA | Gatineau (historical) | 1972–2018 |
| `maniwaki-airport` | MANIWAKI AIRPORT | Gatineau (recent) | 1993–2026 |
| `barrage-temiscamingue` | BARRAGE TEMISCAMINGUE | Upper Ottawa main feeder of Lac Coulonge | 1972–2026 |
| `mont-laurier` | MONT LAURIER | Lièvre / Cabonga (Baskatong feed) | 1972–2025 |
| `parent` | PARENT | Cabonga headwaters (north) | 1972–2026 |
| `val-dor-a` | VAL-D'OR A | Upper Ottawa headwaters (high north basin) | 1972–2025 |
| `val-dor` | VAL-D'OR | Upper Ottawa (recent overlap) | 2008–2026 |
| `rouyn` | ROUYN | Témiscaming watershed | 1994–2026 |
| `north-bay-a-old` | NORTH BAY A (legacy) | mid-basin wave-passage (historical) | 1972–2013 |
| `north-bay-a-new` | NORTH BAY A | mid-basin wave-passage (recent) | 2014–2026 |
| `pembroke-climate` | PEMBROKE CLIMATE | mid-basin south near Lac Coulonge | 2010–2026 |

## Coverage caveats

- **Pembroke**: no continuous long-running station exists. PEMBROKE CLIMATE
  starts in 2010, which is past the 1972-base period needed for the regime
  test. The earlier session got "broken Pembroke data" from meteostat
  (winter means at –25 °C) — that turned out to be the meteostat catalog
  conflating multiple stations. There is no clean ECCC fix; the climate
  regression has a coverage gap south of Lac Coulonge.
- **Val-d'Or A** (6081) ends 2025 mid-year; **Val-d'Or** (30172) covers
  the recent overlap so the headwaters series is unbroken.
- **Maniwaki UA** ends 2018; **Maniwaki Airport** picks up from 1993
  onward (long overlap is intentional — useful for cross-station QC).
- **North Bay A**: 4201 retired in 2013 and was replaced by 52318 with
  the same name and coordinates. Treat them as a single time series.

## Schema (consolidated and raw)

The consolidated file uses ECCC's native daily-bulk schema unchanged
(headers preserved, no transformations). Key columns:

| Column | Notes |
|---|---|
| `Date/Time`, `Year`, `Month`, `Day` | ISO calendar date |
| `Max Temp (°C)` / `Min Temp (°C)` / `Mean Temp (°C)` | Daily air temperature |
| `Total Rain (mm)` / `Total Snow (cm)` / `Total Precip (mm)` | Daily liquid-equivalent precipitation; snow stored separately |
| `Snow on Grnd (cm)` | Daily snow-on-ground depth (where reported) |
| `Heat Deg Days (°C)` / `Cool Deg Days (°C)` | Pre-computed degree days |
| `Spd of Max Gust (km/h)` / `Dir of Max Gust (10s deg)` | Wind gust where reported |
| `*_Flag` columns | ECCC quality flags (M = missing, E = estimated, etc.) |

## Why these stations

The web-client analysis used a single Ottawa station (4333 OTTAWA CDA),
which sits in the wrong watershed for Lac Coulonge — it explained only
~14 % of the variance. The stations above sample the watersheds that
actually drain to Lac Coulonge:

- Upper Ottawa (Témiscaming, Val-d'Or, Rouyn) is the dominant feeder
- Gatineau (Maniwaki) and Lièvre (Mont-Laurier) drain into the Ottawa
  downstream of Lac Coulonge but their upstream snowpack is a useful
  cross-check
- Parent samples the Cabonga / north headwaters
- North Bay sits at the wave-passage transition between upper and middle
  basin
- Pembroke is the closest mid-basin south station despite the late start

OTTAWA CDA is included as a reference so the new analysis can be
sanity-checked against the prior meteostat-based regression.
