# Alerter

Hourly Python script that fetches the latest two readings for a single
Vigilance station and POSTs an ntfy notification on each property-threshold
crossing (rising or falling).

Stdlib-only.

## Configuration (env)

| Variable | Default | Notes |
|---|---|---|
| `NTFY_URL` | `https://ntfy.sh` | Any ntfy server reachable from your cron |
| `NTFY_TOPIC` | `change-me-freshet-alerts` | **Use a private random topic** — anyone subscribed sees your alerts |
| `STATION_ID` | `1195` | Vigilance station ID to monitor (Lac Coulonge by default) |

## Editing thresholds

The `THRESHOLDS` list in [`alerter.py`](alerter.py) is hard-coded to the
2019 flood observations at the upstream maintainer's Mansfield property:

```python
THRESHOLDS = [
    (108.30, 'Water approaching property (2019 Apr 25 level)'),
    (108.48, 'Water IN backyard, driveway, big tree'),
    (108.52, 'Crawl space flooded (2017 peak)'),
    (108.75, 'Water at cottage bricks'),
    (109.01, 'Water INSIDE cottage, garage, RV area'),
]
```

Replace with your own observed levels. Keeping a few well-anchored "I saw water
do X at level Y" reference points makes the alerts much more actionable than
abstract numbers.

## How it determines a crossing

Each run compares the latest reading against the immediately previous one in
the Vigilance buffer:

- **Rising crossing**: `prev < threshold ≤ curr`
- **Falling crossing**: `curr < threshold ≤ prev`

So a single run only fires for thresholds the river crossed in the last hour,
in either direction. No threshold fires repeatedly while the river hovers.

## ntfy topic security

Anyone who guesses your topic name can read your alerts. Use a long random
string (e.g. `freshet-mansfield-h7ng3p2qk9rw5t`) and only share with the
people/devices that should receive notifications.
