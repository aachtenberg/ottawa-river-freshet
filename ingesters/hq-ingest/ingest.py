"""
Hydro-Québec open-data ingester.

Pulls two JSON feeds linked from
https://www.hydroquebec.com/production/debits-niveaux-eau.html and writes:

  dam_releases   -- hourly total / turbined / spilled discharge per centrale
  dam_inflows    -- daily filtered local inflow (apport filtré) per centrale
  dam_levels     -- hourly water level per station (amont, aval, river, weather)
  dam_sites      -- combined metadata for centrales + stations

Filtered to the Ottawa basin window (lat 45-48, lon -80 to -74) so we don't
ingest the entire Quebec hydro fleet. Adjust BBOX env vars to widen scope.
"""

import os, json, sys, ssl, urllib.request
from collections import defaultdict
from datetime import datetime, timezone

# hydroquebec.com's CDN refuses Python's default TLS handshake on alpine images
# (SSLV3_ALERT_HANDSHAKE_FAILURE). Lowering the OpenSSL security level to 1
# allows the legacy cipher suites the CDN advertises.
SSL_CTX = ssl.create_default_context()
SSL_CTX.set_ciphers('DEFAULT:@SECLEVEL=1')

CENTRALES_URL = os.environ.get(
    'HQ_CENTRALES_URL',
    'https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/Donnees_VUE_CENTRALES_ET_OUVRAGES.json',
)
STATIONS_URL = os.environ.get(
    'HQ_STATIONS_URL',
    'https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/Donnees_VUE_STATIONS_ET_TARAGES.json',
)
POSTGREST = os.environ.get('POSTGREST_URL', 'http://postgrest.data.svc.cluster.local:3000')

# Ottawa basin bounding box. Première-Chute (47.6, -79.45) is the upper limit;
# Carillon (45.57, -74.38) is the lower. A small margin avoids edge drops.
LAT_MIN = float(os.environ.get('HQ_LAT_MIN', '45.0'))
LAT_MAX = float(os.environ.get('HQ_LAT_MAX', '48.0'))
LON_MIN = float(os.environ.get('HQ_LON_MIN', '-80.0'))
LON_MAX = float(os.environ.get('HQ_LON_MAX', '-74.0'))

POST_BATCH = int(os.environ.get('HQ_POST_BATCH', '2000'))


def fetch_json(url):
    req = urllib.request.Request(url, headers={
        'Accept': 'application/json',
        'User-Agent': 'freshet-hq-ingest/1.0',
    })
    with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as r:
        return json.load(r)


def post_rows(path, rows):
    if not rows:
        return 0
    sent = 0
    for i in range(0, len(rows), POST_BATCH):
        chunk = rows[i:i + POST_BATCH]
        body = json.dumps(chunk).encode('utf-8')
        req = urllib.request.Request(
            f'{POSTGREST}/{path}',
            data=body,
            method='POST',
            headers={
                'Content-Type': 'application/json',
                'Prefer': 'resolution=ignore-duplicates',
            },
        )
        with urllib.request.urlopen(req, timeout=60) as r:
            sent += len(chunk)
            print(f'  POST /{path} -> HTTP {r.status} ({len(chunk)} rows, cumulative {sent}/{len(rows)})')
    return sent


def in_basin(site):
    try:
        lat = float(site.get('ycoord') or 0)
        lon = float(site.get('xcoord') or 0)
    except (TypeError, ValueError):
        return False
    return LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX


def normalize_ts(ts):
    # HQ timestamps look like "2026/05/02T19:00:00Z" — slashes in the date.
    return ts.replace('/', '-')


def parse_date(s):
    if not s:
        return None
    s = s.replace('/', '-')
    for fmt in ('%Y-%m-%d', '%Y-%m-%dT%H:%M:%SZ'):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    return None


def _numeric(v):
    try:
        return float(v) if v not in (None, '') else None
    except (TypeError, ValueError):
        return None


def site_meta_row(site, kind):
    return {
        'site_id':     site['identifiant'],
        'nom':         site.get('nom'),
        'kind':        kind,
        'region':      site.get('RegionQC'),
        'region_code': site.get('CodeRegionQC'),
        'lat':         _numeric(site.get('ycoord')),
        'lon':         _numeric(site.get('xcoord')),
        'date_debut':  parse_date(site.get('date debut')),
        'date_fin':    parse_date(site.get('date fin')),
    }


def upsert_sites(rows):
    """dam_sites is a regular table (not a hypertable); we want true upsert
    so name/coord changes propagate. Use Prefer: resolution=merge-duplicates."""
    if not rows:
        return 0
    body = json.dumps(rows).encode('utf-8')
    req = urllib.request.Request(
        f'{POSTGREST}/dam_sites',
        data=body,
        method='POST',
        headers={
            'Content-Type': 'application/json',
            'Prefer': 'resolution=merge-duplicates',
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f'  POST /dam_sites -> HTTP {r.status} ({len(rows)} sites)')
    return len(rows)


def ingest_centrales():
    payload = fetch_json(CENTRALES_URL)
    sites = [s for s in payload.get('Site', []) if in_basin(s)]
    print(f'centrales: {len(sites)} basin sites in window')

    site_rows = [site_meta_row(s, 'centrale') for s in sites]

    release_rows = []   # one row per (site_id, time), columns total/turbined/spilled
    inflow_rows = []    # one row per (site_id, day)

    for s in sites:
        site_id = s['identifiant']
        # Group hourly series by timestamp so we emit one row per (site, time)
        # carrying total/turbined/spilled together. Multiple "déversé"/"turbiné"
        # streams (e.g. multi-spillway sites) are summed.
        per_time = defaultdict(lambda: {'total': None, 'turbined': 0.0, 'spilled': 0.0,
                                        'has_turb': False, 'has_spill': False})
        for c in s.get('Composition', []):
            tpd = c.get('type_point_donnee') or ''
            unit = c.get('nom_unite_mesure') or ''
            if unit != 'm³/s':
                continue
            data = c.get('Donnees') or {}
            if tpd == 'Apport filtré':
                for ts, val in data.items():
                    try:
                        v = float(val)
                    except (TypeError, ValueError):
                        continue
                    inflow_rows.append({
                        'time': normalize_ts(ts),
                        'site_id': site_id,
                        'inflow_cms': v,
                    })
                continue
            if tpd == 'Débit total':
                for ts, val in data.items():
                    try:
                        v = float(val)
                    except (TypeError, ValueError):
                        continue
                    per_time[ts]['total'] = v
            elif tpd.startswith('Débit turbiné'):
                for ts, val in data.items():
                    try:
                        v = float(val)
                    except (TypeError, ValueError):
                        continue
                    per_time[ts]['turbined'] += v
                    per_time[ts]['has_turb'] = True
            elif tpd.startswith('Débit déversé'):
                for ts, val in data.items():
                    try:
                        v = float(val)
                    except (TypeError, ValueError):
                        continue
                    per_time[ts]['spilled'] += v
                    per_time[ts]['has_spill'] = True

        for ts, vals in per_time.items():
            release_rows.append({
                'time': normalize_ts(ts),
                'site_id': site_id,
                'total_cms':    vals['total'],
                'turbined_cms': vals['turbined'] if vals['has_turb']  else None,
                'spilled_cms':  vals['spilled']  if vals['has_spill'] else None,
            })

    print(f'  releases: {len(release_rows)} rows; inflows: {len(inflow_rows)} rows')
    upsert_sites(site_rows)
    post_rows('dam_releases', release_rows)
    post_rows('dam_inflows', inflow_rows)


def ingest_stations():
    payload = fetch_json(STATIONS_URL)
    stations = [s for s in payload.get('Station', []) if in_basin(s)]
    print(f'stations: {len(stations)} basin sites in window')

    site_rows = [site_meta_row(s, 'station') for s in stations]

    level_rows = []
    for s in stations:
        sid = s['identifiant']
        for c in s.get('Composition', []):
            if c.get('type_point_donnee') != 'Niveau':
                continue
            for ts, val in (c.get('Donnees') or {}).items():
                try:
                    v = float(val)
                except (TypeError, ValueError):
                    continue
                level_rows.append({
                    'time': normalize_ts(ts),
                    'station_id': sid,
                    'level_m': v,
                })

    print(f'  levels: {len(level_rows)} rows')
    upsert_sites(site_rows)
    post_rows('dam_levels', level_rows)


def main():
    started = datetime.now(timezone.utc)
    try:
        ingest_centrales()
    except Exception as e:
        print(f'centrales ingest failed: {e}', file=sys.stderr)
        raise
    try:
        ingest_stations()
    except Exception as e:
        print(f'stations ingest failed: {e}', file=sys.stderr)
        raise
    elapsed = (datetime.now(timezone.utc) - started).total_seconds()
    print(f'HQ ingest complete in {elapsed:.1f}s')


if __name__ == '__main__':
    main()
