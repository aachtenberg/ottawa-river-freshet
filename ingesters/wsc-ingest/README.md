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

Active Ottawa basin gauges with discharge data:

| Code | River |
|---|---|
| 02KF005 | Ottawa River at Britannia |
| 02KF019 | Ottawa River at Masson-Angers |
| 02LA015 | Mississippi River near Appleton |
| 02LB008 | Rideau River at Ottawa |
| 02JE013 | Ottawa River at Mattawa |
| 02LH004 | Gatineau River at Farmers Rapids |
| 02LE024 | Lièvre River at Pont 311 |
| 02KA004 | Petawawa River near Petawawa |

Override via `WSC_STATIONS=<comma-separated codes>`.

## Configuration

| Variable | Default | Notes |
|---|---|---|
| `POSTGREST_URL` | `http://postgrest:3000` | PostgREST endpoint |
| `WSC_STATIONS`  | (8 default codes above) | Override station list |
| `WSC_LOOKBACK_HOURS` | `24` | Window per pull |
| `WSC_POST_BATCH` | `2000` | Rows per PostgREST POST |

## Schedule

Hourly is plenty given the 5-minute upstream cadence. Stagger from other
ingesters (default `:37 past the hour`).
