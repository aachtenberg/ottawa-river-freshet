# Reference data

Archival CSVs used by the dashboard for historical context. None of these
are queried at runtime by the ingesters — they're either bundled into the
dashboard's JS constants or kept here as the canonical source for those
constants.

## Files

### `lac-coulonge-monthly-1972-2025.csv`

ORRPB monthly mean levels for **Lake Coulonge at Fort-Coulonge**, 54 years
(1972–2025). Schema:

| Column | Unit | Notes |
|---|---|---|
| `year` | — | Calendar year |
| `jan`–`dec` | metres MASL | Monthly means; `NA` for missing months |
| `annual_mean` | metres MASL | Mean across the 12 monthly means |
| `daily_max` | metres MASL | Maximum daily reading observed that year |
| `daily_min` | metres MASL | Minimum daily reading |

`NA` markers: 1972 January, 1979 June, most of 1984.

Used in the dashboard for:
- The percentile rank tag on Lac Coulonge's map callout
- The `HISTORICAL_PEAKS` overlay on the primary chart
- The historical context table in the upstream documentation

### `orrpb-historic-peaks-1972-2025.csv`

Cross-station historical peaks from the ORRPB "Know Your Levels" working
document (May 2025). 15 stations from Mattawa down to Carillon plus the
Gatineau River, with **2017 / 2019 / 2023 peak levels** and one observed
day in 2025. All values in metres MASL.

The `datum_offset_masl` column captures the constant to add to the live API
value to get MASL — `0` for Quebec stations (Vigilance reports MASL natively),
`100` for Ontario stations (ECCC's "assumed datum"), and `173.65` for
Témiscaming village.

Used in the dashboard for:
- Reference-year context labels ("above 2023, 81 cm below 2019" on cards)
- Synthetic flood-state classification when Vigilance has no thresholds
- The 2019-record reference line on the watershed snapshot bar chart

## Source disclaimers

These data are aggregated from ORRPB's public publications. ORRPB asserts
that its data is "use at your own risk" — this repository re-displays them
for community awareness only. For authoritative inquiries consult ORRPB,
Hydro-Québec, OPG, MELCCFP, or the relevant operator directly.

The 2025-05-06 "Know Your Levels" PDF that's the source of
`orrpb-historic-peaks-1972-2025.csv` is community-authored and ORRPB-disclaimed.
Citation: anonymous community publication via the Northern Reservoirs Ottawa
River Tourism Wildlife Flood Watch Group, used under fair-comment reuse for
flood awareness.
