# ECCC daily climate ingester

Pulls daily temperature, precipitation, and snow observations from
Environment and Climate Change Canada's bulk CSV endpoint for the
watershed climate stations relevant to Lac Coulonge freshet analysis,
and writes to the `eccc_climate_daily` hypertable.

Stdlib-only. Six-hourly cron, polite to ECCC's public-funded service.

## Source

```
https://climate.weather.gc.ca/climate_data/bulk_data_e.html
  ?format=csv
  &stationID={ID}                # ECCC numeric station id (NOT climate_id)
  &Year={YYYY}
  &Month=1&Day=1                 # ignored for daily — full year always returned
  &timeframe=2                   # 2 = daily
```

Each per-year CSV has a header on row 1 (preceded by a UTF-8 BOM) and ~365
data rows. Station coverage and column availability vary by station.

## Stations

Watershed-aligned set, kept in sync with the static historical script at
`freshet-public/ingesters/climate-history/eccc_pull.py`:

| station_id | name | role |
|---|---|---|
| 4333  | Ottawa CDA          | South-basin reference |
| 5606  | Maniwaki Airport    | Gatineau (recent) |
| 5977  | Barrage Témiscamingue | Upper Ottawa main feeder |
| 5615  | Mont-Laurier        | Lièvre / Cabonga (Baskatong feed) |
| 5966  | Parent              | Cabonga headwaters (north) |
| 30172 | Val-d'Or            | Upper Ottawa (recent) |
| 10849 | Rouyn               | Témiscamingue watershed |
| 52318 | North Bay A         | Mid-basin wave passage |
| 49068 | Pembroke Climate    | Mid-basin south near Lac Coulonge |

## Why complementary to Open-Meteo

The river-history ingester already pulls `weather_observations` from
Open-Meteo for 6 basin stations. Open-Meteo is **modelled / reanalysis**
data — fast, blanket coverage, no station network gaps, but synthetic.
ECCC is the **official Canadian observation network** — what the historical
record is built on. For freshet correlation work that needs to align with
the historical baseline, ECCC is authoritative.

## Configuration

| Variable | Default | Notes |
|---|---|---|
| `POSTGREST_URL` | `http://postgrest:3000` | PostgREST endpoint |
| `ECCC_YEARS_BACK` | `1` | Pull current + N prior years (covers prior-year tail of provisional data) |
| `ECCC_POST_BATCH` | `500` | Rows per PostgREST POST |

## Schedule

ECCC daily data lags 1-3 days. Six-hourly is plenty (`47 */6 * * *`). Be
polite — this is a public-funded service.

## Cadence + idempotency

Each run re-uploads all rows for current + prior year. Upserts use
`Prefer: resolution=merge-duplicates` so provisional values get overwritten
with final ones as ECCC's QC pipeline catches up.
