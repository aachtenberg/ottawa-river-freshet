# ORRPB Historical Summaries

CSV archive scraped from the Ottawa River Regulation Planning Board historical
summary pages at:

- https://www.ottawariver.ca/information/historical-data-summaries-water-levels-and-flows/

## Contents

- `manifest.csv`: station inventory, source URLs, measure type, units, and year
  coverage.
- One per-station CSV for each ORRPB historical summary page discovered from the
  hub page.

## Station CSV schema

| Column | Notes |
|---|---|
| `year` | Calendar year |
| `jan`–`dec` | Monthly mean value for the station page's published measure |
| `annual_mean` | Annual mean value |
| `daily_max` | Annual maximum daily value |
| `daily_min` | Annual minimum daily value |

Missing values are preserved as `NA`, matching the ORRPB pages.

## Measure types

- Most pages in this set publish `water_level` values in `metres`.
- `ottawa-river-at-carillon.csv` publishes `discharge` values in
  `cubic_metres_per_second`.

## Regeneration

Refresh the archive with:

```bash
python3 ingesters/orrpb-historical-summaries/scrape.py
```