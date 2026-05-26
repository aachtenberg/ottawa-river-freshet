# ORRPB per-station historical-record ingester

Daily Python script that scrapes the per-station "Table view, Daily"
data on every monitored location at https://www.ottawariver.ca/location/
and upserts the four parallel time series (Observed, Median 1991-2020,
Historic High with year, Historic Low with year) into the
`orrpb_station_history` hypertable via PostgREST.

This unlocks the same multi-decade "current vs median vs envelope" view
that ORRPB renders on the site's chart, queryable from PostgREST for any
of the 13 monitored locations and both metrics (where available). Until
now the case file relied on WSC long-record stations (Britannia 02KF005)
as proxies for upstream locations because the per-station historical
record looked gated; it is not.

Stdlib-only (urllib + html.parser). Same pattern as the
`reservoir-ingest` and `orrpb-river-ingest` scrapers; the differences
are documented under "How it works" below.

## What ORRPB exposes per station

The per-station table response has four data rows plus a header:

| Row label     | Content                                                    |
|---------------|------------------------------------------------------------|
| Date/Time     | ~391 consecutive daily dates spanning ~13 months           |
| Observed      | Current-year daily value at that station                   |
| Median        | 1991-2020 daily 50th percentile (30-year reference)        |
| Historic High | Per-day maximum over the full record + (year) tag          |
| Historic Low  | Per-day minimum over the full record + (year) tag          |

Units depend on `reading-type`:
- `levels`: water level in metres above mean sea level (geodetic)
- `discharges`: average daily flow in m^3/s

The "normal range" 80% envelope (P10 to P90, the light green band on the
on-site graph) is NOT in the table response. The chart computes it but
the underlying values are not published.

## Station coverage

Levels are published for all 13 stations except `temiscaming` (which
the per-location page only renders for discharges). Discharges are
published only at the cascade dam sites: temiscaming, otto-holden,
des-joachims, chenaux, chats-falls, britannia, carillon. The other
mid-cascade locations (mattawa, pembroke, coulonge, hull, thurso,
grenville) publish levels only. Total publishable pairs: 20.

The `discharges` series for each dam site reports total main-stem
Ottawa River flow past that dam in m^3/s, consistent with the per-day
flows already in `orrpb_river_flows`. Use `orrpb_station_history` when
you also need the 1991-2020 median and the per-day historic envelope;
use `orrpb_river_flows` when you just need the most recent observed
value across the cascade (the conditions-page scrape is faster and
covers the same observed series).

## How it works

1. `urllib.request.Request` with `method="POST"` to
   `https://www.ottawariver.ca/location/<slug>/` with form body
   ```
   reading-type = levels | discharges
   data-display = table
   data-type    = daily
   ```
2. `html.parser.HTMLParser` walks every `<table>` and the parser picks
   the single one whose first column contains "Observed" and "Median".
3. Header row supplies the calendar dates; the four data rows are
   indexed by label and combined into one record per date.
4. Historic High / Low cells contain "value (year)" so we parse with
   `r"(-?[\d,]+(?:\.\d+)?)\s*\(?(\d{4})\)?"`. Numbers may include
   thousands separators (e.g. "2,200") which are stripped before
   `float()`.
5. Records are upserted via PostgREST POST with
   `Prefer: resolution=merge-duplicates,return=minimal` keyed on
   `(station, metric, time)`.

A `time.sleep(SLEEP_S)` between requests (default 1.5 seconds) keeps
the run polite. ORRPB's site is on a small WordPress install on
Cloudflare and the table-view path is not a real API; rate-limiting
ourselves is the right thing to do.

## Stations

The default list of 13 stations and their available metrics is in
`DEFAULT_STATIONS` in `scrape.py`. Slugs match the URL segment under
`/location/`:

```
temiscaming, otto-holden, mattawa, des-joachims, pembroke, coulonge,
chenaux, chats-falls, britannia, hull, thurso, grenville, carillon
```

The `ORRPB_STATIONS` env var overrides this with a CSV of
`slug[:metric1+metric2]` tokens, e.g. `chenaux:levels,pembroke:levels`.

## Schedule

ORRPB updates the per-location data shortly after the conditions page
refresh (mid-afternoon Eastern). The window is 13 months rolling so
daily updates only add the latest day-or-two of new data. Running
once per day at 21:50 UTC (just after the conditions-page scrapers at
21:30 / 21:40) is plenty.

Multiple runs per day are safe; the upsert merges on
`(station, metric, time)` so re-running is idempotent.

## Schema

```sql
CREATE TABLE orrpb_station_history (
  time                  date NOT NULL,
  station               text NOT NULL,
  metric                text NOT NULL,   -- 'level_m' or 'flow_cms'
  observed              double precision,
  median                double precision,
  historic_high_value   double precision,
  historic_high_year    smallint,
  historic_low_value    double precision,
  historic_low_year     smallint,
  PRIMARY KEY (station, metric, time)
);
```

Table definition lives in
`k3s/base/data/files/river-history/bootstrap.sql` alongside the rest
of the freshet schema.

## Adding a station

Append the slug + metrics tuple to `DEFAULT_STATIONS` in `scrape.py`.
No schema change required.

## Failure handling

ORRPB sometimes returns 500 for a specific location while others work.
Individual station failures are logged but the run continues. The job
exits nonzero only if zero rows were upserted across all stations
(meaning every station failed, which is the actionable failure mode).

## Disclaimer

ORRPB asserts on-site that their data is "use at your own risk" and
"may not be reproduced or redistributed." This ingester caches
derived statistics into our own database for case-file analysis. We
do not republish ORRPB's raw daily tables in community-facing output;
the case-file notes that use this data cite ORRPB as the source and
present only derived statistics (medians, distances from envelope,
day counts).
