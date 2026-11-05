# WSC realtime hydrometric ingester

Pulls 5-minute level + discharge readings from Water Survey of Canada's
realtime CSV endpoint and writes to the `wsc_readings` hypertable.

Stdlib-only. Stations and lookback window configurable via env.

## Source

```
https://wateroffice.ec.gc.ca/services/real_time_data/csv/inline
  ?stations[]=02KF005           # WSC alphanumeric station code
  &parameters[]=46              # 46 = water level (m)
  &parameters[]=47              # 47 = discharge (m³/s)
  &start_date=YYYY-MM-DD HH:MM:SS
  &end_date=YYYY-MM-DD HH:MM:SS
```

No auth. Returns CSV with one row per station × timestamp × parameter.

## Why this exists alongside the Vigilance ingester

Vigilance often publishes only level. WSC publishes both level AND discharge
for the same gauges, plus stations Vigilance doesn't cover (e.g. Britannia
02KF005, with continuous flow records back to 1960). The two feeds are
complementary, not duplicative.

## Default stations

Active Ottawa basin gauges (names as WSC publishes them). Main stem first,
then the tributaries the dashboard's Tributaries tab reads from
`wsc_readings`, then two downstream proxies:

| Code | Station | Why |
|---|---|---|
| 02KF005 | Ottawa River at Britannia | main stem at Ottawa, flow record since 1960 |
| 02KF019 | Ottawa River (north shore) at Masson-Angers | main stem below Gatineau |
| 02LA015 | Outaouais (rivière des) à Hull | main-stem level at Hull, the Carillon directive trigger |
| 02LB008 | Bear Brook near Bourget | legacy |
| 02JE013 | Ottawa River at Mattawa | Otto Holden tailwater |
| 02JE020 | Mattawa River below Bouillon Lake | Mattawa tributary, above the confluence |
| 02JE025 | Témiscamingue (lac) à Témiscaming | the dashboard's WSC fallback for Vigilance 951 (level only) |
| 02LH004 | Gatineau River at Farmers Rapids | Gatineau |
| 02LE024 | Lièvre (rivière du) au pont-route 311 | Lièvre |
| 02KB001 | Petawawa River near Petawawa | Petawawa |
| 02KC009 | Bonnechere River near Castleford | Bonnechere |
| 02KD004 | Madawaska River at Palmer Rapids | Madawaska |
| 02KF001 | Mississippi River at Fergusons Falls | Mississippi (ON), upper |
| 02KF006 | Mississippi River at Appleton | Mississippi (ON), lower |
| 02LA004 | Rideau River at Ottawa | Rideau |
| 02LB005 | South Nation River near Plantagenet Springs | South Nation |
| 02OA105 | Deux Montagnes (lac des) à Pointe-Calumet | Carillon tailwater proxy |
| 02OA039 | Lac Saint-Louis at Pointe-Claire | downstream St. Lawrence proxy |

Override via `WSC_STATIONS=<comma-separated codes>`. (Earlier versions of
this list named 02KA004 for the Petawawa; that code is a discontinued Perch
Lake gauge near Chalk River. 02KB001 is the active Petawawa station.)

## Configuration

| Variable | Default | Notes |
|---|---|---|
| `POSTGREST_URL` | `http://postgrest:3000` | PostgREST endpoint: set by the compose file and the k8s manifests; the script's own default is the upstream cluster's `postgrest.data.svc.cluster.local:3000` |
| `WSC_STATIONS`  | (18 default codes above) | Override station list |
| `WSC_LOOKBACK_HOURS` | `24` | Window per pull |
| `WSC_POST_BATCH` | `2000` | Rows per PostgREST POST |

## Schedule

Hourly is plenty given the 5-minute upstream cadence. Stagger from other
ingesters (default `:37 past the hour`).
