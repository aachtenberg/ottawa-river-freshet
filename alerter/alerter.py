"""Threshold-crossing alerter for a single Vigilance station.

Compares the latest reading against the previous one and pushes an ntfy
notification on each property-threshold crossing (rising or falling).

When the Vigilance feed is down or serving nulls, falls back to the same
gauge in your own database (via PostgREST) so alerting keeps working.

Configure via env vars:
  NTFY_URL       base URL of an ntfy server (e.g. https://ntfy.sh, or your own)
  NTFY_TOPIC     ntfy topic to post to
  STATION_ID     Vigilance station id (default: 1195 = Lac Coulonge / Fort-Coulonge)
  POSTGREST_URL  PostgREST base URL for the fallback (default: compose service)
"""

import os, json, sys, urllib.request
from datetime import datetime, timedelta, timezone

NTFY_URL = os.environ.get('NTFY_URL', 'https://ntfy.sh')
NTFY_TOPIC = os.environ.get('NTFY_TOPIC', 'change-me-freshet-alerts')
STATION_ID = int(os.environ.get('STATION_ID', '1195'))
# MSP removed the `inedit-ro` read-only replica from DNS on 2026-08-10 during
# a platform migration; the same PostgREST API now lives on `inedit`.
VIGILANCE_BASE = os.environ.get('VIGILANCE_API_BASE', 'https://inedit.geo.msp.gouv.qc.ca')
API = f'{VIGILANCE_BASE}/station_details_readings_api?id=eq.{STATION_ID}'

# Same-gauge fallback in your own database. MSP's 2026-08-10 migration served
# HTTP 200 with valeurs_niv=null for every station, which crashed this script
# on every run and silently stopped all alerting. Point FALLBACKS at an
# independent source where you have one (for 1195 the Hydro-Québec open-data
# gauge 1-2983 kept publishing throughout); otherwise it reads back your own
# ingested Vigilance mirror.
POSTGREST = os.environ.get('POSTGREST_URL', 'http://postgrest:3000')
FALLBACK_LOOKBACK_H = float(os.environ.get('FALLBACK_LOOKBACK_HOURS', '72'))
FALLBACKS = {
    1195: ('dam_levels', 'station_id', '1-2983'),   # HQ Fort-Coulonge
}

# Per-station freshness sweep over everything you ingest, not just STATION_ID.
# The gauges behind Québec's Vigilance API come from several agencies, and they
# fail per-agency: Hydro Météo's eight stations went dark 2026-09-01 -> 09-08
# while the Hydro-Québec and Environnement Canada gauges published normally. A
# check that only watches your own property gauge cannot see that.
#
# Reports the stalled set grouped by `provider`, because a stall that lines up
# exactly with one provider is an upstream outage, not a problem with your
# ingest — that distinction is the whole diagnosis.
STATION_STALE_HOURS = float(os.environ.get('STATION_STALE_HOURS', '12'))
# Past this a gauge is retired or long-dark rather than newly broken. Counting
# those means an alert that fires forever and gets muted.
STATION_DARK_HOURS = float(os.environ.get('STATION_DARK_HOURS', '336'))  # 14d

# Default urllib UA is blocked by some CDNs (Cloudflare 403s Python-urllib).
UA = {'User-Agent': 'freshet-alerter/1.0'}

# Each tuple: (level in metres, short description)
# Edit these to match a different property.
THRESHOLDS = [
    (108.30, 'Water approaching property (2019 Apr 25 level)'),
    (108.48, 'Water IN backyard, driveway, big tree'),
    (108.52, 'Crawl space flooded (2017 peak)'),
    (108.75, 'Water at cottage bricks'),
    (109.01, 'Water INSIDE cottage, garage, RV area'),
]

def get_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        return json.load(r)


def fetch_vigilance():
    """Live readings, or [] when the feed is empty/null — 200-with-[] and
    valeurs_niv=null are both real outage shapes, not crashes."""
    rows = get_json(API)
    vals = (rows[0].get('valeurs_niv') if rows else None) or []
    return [v for v in vals if v and v.get('valeur') is not None]


def fetch_fallback():
    """Same-gauge rows from your own database, in the Vigilance reading shape."""
    fb = FALLBACKS.get(STATION_ID)
    path, key, value = fb if fb else ('river_readings', 'station_id', str(STATION_ID))
    since = datetime.now(timezone.utc) - timedelta(hours=FALLBACK_LOOKBACK_H)
    url = (f'{POSTGREST}/{path}?{key}=eq.{value}'
           f'&time=gte.{since.strftime("%Y-%m-%dT%H:%M:%SZ")}'
           f'&order=time.asc&select=time,level_m')
    rows = get_json(url)
    # level_m > 0 drops upstream glitch rows; these gauges sit far above 0 m.
    return [{'valeur': x['level_m'], 'date_prise_valeur': x['time']}
            for x in rows if x.get('level_m') is not None and x['level_m'] > 0]


def parse_ts(ts):
    """Vigilance emits naked UTC ("...T17:00:00"); rows read back from
    PostgREST carry a real offset ("...+00:00"). Parse both, treating a naive
    value as UTC."""
    dt = datetime.fromisoformat(str(ts).replace('Z', '+00:00'))
    return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt


def sweep_station_freshness():
    """Freshness of every ingested gauge, grouped by upstream provider.

    Best-effort and side-effect free apart from logging: this runs before the
    threshold logic and must never be able to stop a property alert going out.
    Emits one STALE_STATION line per stale gauge plus a single STALE_SWEEP
    summary per run — point your log alerting at the summary, so that a single
    run can't satisfy a "seen twice" threshold on its own.
    """
    now = datetime.now(timezone.utc)
    stations = get_json(f'{POSTGREST}/river_stations?select=station_id,label,provider')
    stale, dark = [], 0
    for st in stations:
        sid = st.get('station_id')
        if sid is None:
            continue
        rows = get_json(f'{POSTGREST}/river_readings?station_id=eq.{sid}'
                        f'&order=time.desc&limit=1&select=time')
        age = None
        if rows:
            age = (now - parse_ts(rows[0]['time'])).total_seconds() / 3600
        if age is None or age >= STATION_DARK_HOURS:
            dark += 1
            continue
        if age >= STATION_STALE_HOURS:
            stale.append((sid, st.get('label'), st.get('provider') or 'unknown', age))

    for sid, label, provider, age in stale:
        print(f'STALE_STATION vigilance_station station_id={sid} label={label} '
              f'provider="{provider}" age_hours={age:.1f}', file=sys.stderr)

    if stale:
        providers = sorted({p for _, _, p, _ in stale})
        scope = providers[0] if len(providers) == 1 else f'{len(providers)} providers'
        print(f'STALE_SWEEP vigilance_stations stale={len(stale)} '
              f'of={len(stations) - dark} dark={dark} scope="{scope}" '
              f'oldest_age_hours={max(a for *_, a in stale):.1f}', file=sys.stderr)
    else:
        print(f'SWEEP_OK {len(stations) - dark} station(s) fresh '
              f'(<{STATION_STALE_HOURS:.0f}h), {dark} long-dark')


# Runs before the early exit below: your property gauge being dry is exactly
# when the wider picture matters, so don't gate the sweep on it.
try:
    sweep_station_freshness()
except Exception as e:
    print(f'SWEEP_FAIL: {e}', file=sys.stderr)

try:
    readings = fetch_vigilance()
except Exception as e:
    print(f'FETCH_FAIL: {e}', file=sys.stderr)
    readings = []

if len(readings) < 2:
    try:
        fallback = fetch_fallback()
        if len(fallback) >= 2:
            print(f'FALLBACK: Vigilance empty for {STATION_ID}; '
                  f'using {len(fallback)} rows from PostgREST', file=sys.stderr)
            readings = fallback
    except Exception as e:
        print(f'FALLBACK_FAIL: {e}', file=sys.stderr)

if len(readings) < 2:
    # Exit 0: a dry upstream is not a job failure, and retrying it into
    # BackoffLimitExceeded helps nobody.
    print(f'NODATA station_id={STATION_ID} (live feed and fallback both empty)',
          file=sys.stderr)
    sys.exit(0)

prev_r, curr_r = readings[-2], readings[-1]
prev, curr, ts = prev_r['valeur'], curr_r['valeur'], curr_r['date_prise_valeur']

fired = 0
for level, desc in THRESHOLDS:
    rising = prev < level <= curr
    falling = curr < level <= prev
    if not (rising or falling):
        continue
    direction = 'CROSSED ABOVE' if rising else 'dropped below'
    # Titles must be latin-1 (HTTP headers); put icons in Tags, not Title.
    title = f'Lac Coulonge {direction} {level:.2f} m'
    body = f'{desc}\nLevel: {curr:.3f} m (was {prev:.3f} m)\nTime: {ts}'
    priority = '5' if rising and level >= 108.75 else '4' if rising else '3'
    tags = 'arrow_up,warning' if rising else 'arrow_down,information_source'
    req = urllib.request.Request(
        f'{NTFY_URL}/{NTFY_TOPIC}',
        data=body.encode('utf-8'),
        headers={'Title': title, 'Priority': priority, 'Tags': tags},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f'SENT ({resp.status}): {title}')
            fired += 1
    except Exception as e:
        print(f'POST_FAIL {level}: {e}', file=sys.stderr)

if fired == 0:
    print(f'No crossings. prev={prev:.3f} curr={curr:.3f} ts={ts}')
