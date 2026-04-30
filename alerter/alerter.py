"""Threshold-crossing alerter for a single Vigilance station.

Compares the latest reading against the previous one and pushes an ntfy
notification on each property-threshold crossing (rising or falling).

Configure via env vars:
  NTFY_URL    base URL of an ntfy server (e.g. https://ntfy.sh, or your own)
  NTFY_TOPIC  ntfy topic to post to
  STATION_ID  Vigilance station id (default: 1195 = Lac Coulonge / Fort-Coulonge)
"""

import os, json, sys, urllib.request

NTFY_URL = os.environ.get('NTFY_URL', 'https://ntfy.sh')
NTFY_TOPIC = os.environ.get('NTFY_TOPIC', 'change-me-freshet-alerts')
STATION_ID = int(os.environ.get('STATION_ID', '1195'))
API = f'https://inedit-ro.geo.msp.gouv.qc.ca/station_details_readings_api?id=eq.{STATION_ID}'

# Each tuple: (level in metres, short description)
# Edit these to match a different property.
THRESHOLDS = [
    (108.30, 'Water approaching property (2019 Apr 25 level)'),
    (108.48, 'Water IN backyard, driveway, big tree'),
    (108.52, 'Crawl space flooded (2017 peak)'),
    (108.75, 'Water at cottage bricks'),
    (109.01, 'Water INSIDE cottage, garage, RV area'),
]

try:
    with urllib.request.urlopen(API, timeout=20) as r:
        readings = json.load(r)[0]['valeurs_niv']
except Exception as e:
    print(f'FETCH_FAIL: {e}', file=sys.stderr)
    sys.exit(1)

if len(readings) < 2:
    print('Not enough readings to compare')
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
    emoji = '🔺' if rising else '🔻'
    title = f'{emoji} Lac Coulonge {direction} {level:.2f} m'
    body = f'{desc}\nLevel: {curr:.3f} m (was {prev:.3f} m)\nTime: {ts}'
    priority = '5' if rising and level >= 108.75 else '4' if rising else '3'
    tags = 'warning' if rising else 'information_source'
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
