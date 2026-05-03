# Hydro-Québec open-data snapshots

Point-in-time CSV exports from the rolling Hydro-Québec public flow/level
JSON feed, ingested into TimescaleDB by the `hq-ingest` cron and snapshotted
here when an exhibit cites a specific value.

The snapshots exist because the case file references **specific live numbers**
(Bryson spill share, headpond elevation, Δh, cascade comparison) and those
numbers will not match the dashboard a few hours from now. Each snapshot is
a frozen, primary-source artifact suitable for citation.

## Source

- HQ open-data feed (release telemetry):
  `https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/Donnees_VUE_CENTRALES_ET_OUVRAGES.json`
- HQ open-data feed (water levels):
  `https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/Donnees_VUE_STATIONS_ET_TARAGES.json`
- Linked from `https://www.hydroquebec.com/production/debits-niveaux-eau.html`
- Refresh cadence: HQ refreshes ~twice daily; the rolling window covers ~10 days

## Files in this directory

### `bryson-daily-2026-04-22_to_2026-05-03.csv`

Bryson Generating Station (HQ site_id `3-46`) daily-mean release telemetry
for the freshet 2026 capture window. One row per day. Columns:

- `date` — YYYY-MM-DD (UTC)
- `hours` — hourly observations averaged into the daily row
- `total_cms_mean` / `_min` / `_max` — total release in m³/s (turbined + spilled)
- `turbined_cms_mean` — mean of hourly turbined m³/s (zero when turbines idle)
- `spilled_cms_mean` — mean of hourly spilled m³/s
- `spill_share_pct` — `spilled / total × 100` for the day

This is the source for the "Bryson is operating at 82–91% spill" claim in
Exhibit D. Note the unusual stability post-Apr 30: total release fixed at
~1,355 m³/s and turbined throughput fixed at ~232 m³/s for 4+ consecutive
days, even as Lac Coulonge crested (Apr 20 peak 108.633 m) and began to
recede. The operator is holding a fixed posture, not reactively adjusting.

### `bryson-headpond-2026-04-22_to_2026-05-03.csv`

Bryson amont (upstream / headpond, station_id `1-2964`) and aval (downstream
/ tailwater, `1-2965`) hourly water-level pair, with the head differential
already computed. Columns:

- `time_utc` — hourly timestamp (Z)
- `amont_m` — headpond elevation in MASL
- `aval_m` — tailwater elevation in MASL
- `head_diff_m` — `amont − aval`, the operating head used to compute the
  Mansfield case file's "high-head operations" claim

This is the source for the "Δh = 14.80 m mean during freshet 2026" claim.

### `cascade-snapshot-<timestamp>.csv`

A single point-in-time row per HQ centrale across the Ottawa main stem and
Gatineau cascade, ordered upstream → downstream. Used for the cascade
comparison figure showing Bryson's spill share against its peers (Première-
Chute, Quinze, Îles, Rapide-2, Rapide-7 upstream; Cabonga, Mercier, Paugan,
Chelsea, Rapides-Farmers on the Gatineau; Carillon downstream).

## Rebuilding from live data

If you want to refresh the snapshots from the live database:

```bash
# (Internal) PostgREST endpoint, no auth required from the cluster network.
PG=http://192.168.0.150:30300

# Bryson hourly release (10-day rolling window):
curl -s "$PG/dam_releases?site_id=eq.3-46&order=time.asc"

# Bryson amont/aval pair:
curl -s "$PG/dam_levels?station_id=in.(1-2964,1-2965)&order=time.asc"

# Cascade snapshot:
curl -s "$PG/latest_dam_releases"
```

The snapshot script lives inline in the `git log` for the commit that added
this directory. Rerun it (or copy from the commit) when you need a new
exhibit-day snapshot.
