# Reservoir ingester

Daily Python script that scrapes the ORRPB conditions page
(`https://www.ottawariver.ca/conditions/?display=reservoir`), parses its
8-day rolling reservoir-levels-and-flows table, and upserts into TimescaleDB
via PostgREST.

Stdlib-only (urllib + html.parser) — no `pip install` needed.

## How it works

1. `urllib.request` fetches the conditions HTML.
2. `html.parser.HTMLParser` walks every `<table>` on the page and captures
   the cell content. We pick the right table by content (the one with
   `Level - <agency>` / `Flow - <agency>` rows).
3. Header row is parsed for date columns; each value cell is matched to its
   reservoir, type (Level/Flow), and date.
4. Values upserted via PostgREST POST with
   `Prefer: resolution=merge-duplicates,return=minimal`.

## Schedule

ORRPB publishes daily, mid-afternoon Eastern. Run at `30 21 * * *` UTC
(≈ 17:30 EDT / 16:30 EST). Multiple runs per day are safe — readings have
date precision (00:00 UTC of the column date) and the upsert merges by
`(reservoir_id, time)`.

## Adding a reservoir

1. Add an entry to `RESERVOIR_KEY_MAP` in [`scrape.py`](scrape.py) mapping
   the ORRPB-published display name → your stable slug.
2. Add an entry in [`dashboard/reservoir-limits.json`](../../dashboard/reservoir-limits.json)
   with the operating limits and capacity.
3. Add an entry in `dashboard/index.html` `RESERVOIR_LOCATIONS` map for the
   marker on the map drawer.
4. Add the slug to `RESERVOIR_ORDER` in `dashboard/index.html` to slot it
   into the upstream→downstream sort.

## ORRPB structure changes

The HTML scraper is the most fragile piece in the stack. ORRPB's table
structure has been stable through the 2025–2026 season but isn't a contract.
If the page layout changes, `parse_table()` and `find_reservoir_table()` are
the spots to adjust.

## Disclaimer

ORRPB asserts on-site that their data is "use at your own risk." This stack
re-displays values for community awareness only; for authoritative numbers
consult ORRPB or the operating agencies directly.
