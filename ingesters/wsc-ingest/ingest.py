"""
Water Survey of Canada real-time hydrometric ingester.

Pulls 5-minute level (parameter 46) and discharge (parameter 47) readings
for a configurable list of WSC station codes from
wateroffice.ec.gc.ca/services/real_time_data/csv/inline and writes to
the wsc_readings hypertable.

Why this exists: Vigilance often publishes only level — WSC publishes both
level AND discharge for the same gauges, plus stations Vigilance doesn't
cover (e.g. Britannia 02KF005 with continuous flow back to 1960).
"""

import os, sys, csv, io, urllib.request, urllib.parse
from collections import defaultdict
from datetime import datetime, timezone, timedelta

WSC_BASE = 'https://wateroffice.ec.gc.ca/services/real_time_data/csv/inline'
POSTGREST = os.environ.get('POSTGREST_URL', 'http://postgrest.data.svc.cluster.local:3000')

# Default station list — Ottawa basin, active gauges with discharge data.
# Add more by setting WSC_STATIONS env var (comma-separated codes).
DEFAULT_STATIONS = (
    '02KF005,'  # OTTAWA RIVER AT BRITANNIA — main-stem at Ottawa, ~91,260 km² drainage
    '02KF019,'  # OTTAWA RIVER (NORTH SHORE) AT MASSON-ANGERS
    '02LA015,'  # MISSISSIPPI RIVER NEAR APPLETON
    '02LB008,'  # RIDEAU RIVER AT OTTAWA
    '02JE013,'  # OTTAWA RIVER AT MATTAWA — combined Ottawa+Mattawa flow at confluence
    '02JE020,'  # MATTAWA RIVER BELOW BOUILLON LAKE — Mattawa-only signal upstream of confluence
    '02LH004,'  # GATINEAU RIVER AT FARMERS RAPIDS
    '02LE024,'  # LIEVRE (RIVIERE DU) AU PONT-ROUTE 311
    '02KA004,'  # PETAWAWA RIVER NEAR PETAWAWA
    '02OA105,'  # LAKE OF TWO MOUNTAINS AT POINTE-CALUMET — Carillon tailwater proxy (level 1986-)
    '02OA039'   # LAC SAINT-LOUIS AT POINTE-CLAIRE — downstream proxy via St-Lawrence (level 1915-)
)

STATIONS = [s.strip() for s in os.environ.get('WSC_STATIONS', DEFAULT_STATIONS).split(',') if s.strip()]
LOOKBACK_HOURS = int(os.environ.get('WSC_LOOKBACK_HOURS', '24'))
POST_BATCH = int(os.environ.get('WSC_POST_BATCH', '2000'))

# WSC parameter codes:
#   46 = water level (m)
#   47 = discharge (m³/s)
PARAMS = ['46', '47']


def fetch_csv(stations, params, start, end):
    """Returns the raw CSV text body for the given stations/params/window."""
    qs = []
    for s in stations:
        qs.append(('stations[]', s))
    for p in params:
        qs.append(('parameters[]', p))
    qs.append(('start_date', start.strftime('%Y-%m-%d %H:%M:%S')))
    qs.append(('end_date',   end.strftime('%Y-%m-%d %H:%M:%S')))
    url = WSC_BASE + '?' + urllib.parse.urlencode(qs, doseq=False)
    req = urllib.request.Request(url, headers={'Accept': 'text/csv'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode('utf-8-sig')


def post_rows(rows):
    if not rows:
        return 0
    sent = 0
    for i in range(0, len(rows), POST_BATCH):
        chunk = rows[i:i + POST_BATCH]
        body = ('[' + ','.join(
            '{"time":"%s","station_code":"%s","level_m":%s,"flow_cms":%s}' % (
                r['time'], r['station_code'],
                'null' if r.get('level_m') is None else f"{r['level_m']}",
                'null' if r.get('flow_cms') is None else f"{r['flow_cms']}",
            ) for r in chunk
        ) + ']').encode('utf-8')
        req = urllib.request.Request(
            f'{POSTGREST}/wsc_readings',
            data=body, method='POST',
            headers={'Content-Type': 'application/json',
                     'Prefer': 'resolution=ignore-duplicates'},
        )
        with urllib.request.urlopen(req, timeout=60) as r:
            sent += len(chunk)
            print(f'  POST /wsc_readings -> HTTP {r.status} ({len(chunk)} rows, cumulative {sent}/{len(rows)})')
    return sent


def main():
    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(hours=LOOKBACK_HOURS)
    print(f'WSC: pulling {len(STATIONS)} stations, {LOOKBACK_HOURS}h window ({start.isoformat()} → {end.isoformat()})')

    text = fetch_csv(STATIONS, PARAMS, start, end)
    reader = csv.reader(io.StringIO(text))
    header = next(reader, None)
    if not header:
        print('WSC: empty response', file=sys.stderr)
        return

    # Group readings by (station_code, time) so level + flow merge into one row.
    grouped = defaultdict(lambda: {'level_m': None, 'flow_cms': None})
    n_in = 0
    for row in reader:
        if len(row) < 4:
            continue
        station, ts, param, val = row[0], row[1], row[2], row[3]
        if not val.strip():
            continue
        try:
            v = float(val)
        except ValueError:
            continue
        # Normalize timestamp: WSC emits UTC like '2026-05-02T19:00:00Z'.
        ts_norm = ts if ts.endswith('Z') else ts + 'Z'
        key = (station, ts_norm)
        if param == '46':
            grouped[key]['level_m'] = v
        elif param == '47':
            grouped[key]['flow_cms'] = v
        n_in += 1

    rows = [
        {'station_code': st, 'time': ts, 'level_m': v['level_m'], 'flow_cms': v['flow_cms']}
        for (st, ts), v in grouped.items()
    ]
    by_st = defaultdict(int)
    for r in rows:
        by_st[r['station_code']] += 1
    print(f'WSC: parsed {n_in} CSV cells into {len(rows)} rows across {len(by_st)} stations')
    for st, n in sorted(by_st.items()):
        print(f'  {st}: {n} rows')

    post_rows(rows)
    print('WSC ingest complete')


if __name__ == '__main__':
    main()
