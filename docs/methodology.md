# Methodology

How specific numeric outputs in the dashboard are computed. Anyone running
their own deployment should understand these so they know when results are
authoritative vs. approximate.

## 1. Reservoir percent-full

Each reservoir on the Reservoirs tab shows a "% full" value computed from a
**linear interpolation** between published low and high operating limits:

```
pct_full = (current_level − low_limit) / (high_limit − low_limit) × 100
```

Operating limits live in
[`dashboard/reservoir-limits.json`](../dashboard/reservoir-limits.json), one
entry per reservoir. Both limits and the per-reservoir capacity (`capacity_mcm`)
are sourced from the operator-provided System Constraints tables on
[ottawariver.ca](https://www.ottawariver.ca/) per-location pages, with values
spot-checked against community-published readings.

### Why linear?

Real reservoir storage curves are non-linear (surface area changes with depth,
non-uniform basin shape). The linear approximation:

- Is exact at 0 % and 100 %, by construction.
- Is within ~5 percentage points of the true storage curve for most reservoirs
  in the Ottawa basin operating range, based on cross-checks against published
  storage curves.
- Doesn't need operator-internal storage curves that aren't public.
- Matches the methodology used in the community-published gauges this stack is
  modelled on.

### Caveats

- **Point-in-time, not 24 h average.** ORRPB's official daily numbers are the
  24 h mean of all readings on that calendar day; the dashboard renders the
  most recent point reading from the last scrape. Numbers will agree on
  steady-state reservoirs and disagree by up to ~2 percentage points during
  rapid fill/release.
- **Operator non-linearities not modelled.** Real operators apply seasonal
  draw-down rules, ramping limits near the high/low ends, and stoplog
  configurations that change effective limits during freshet. None of those
  are here.
- **Calibrated against one point.** The high-limit values were back-solved
  against a single day's published % full — they'll match that day exactly,
  but may drift a few points in extreme conditions.

If you need authoritative numbers, consult the operator directly.

## 2. Datum offsets

Vigilance reports Quebec gauges in Metres Above Sea Level (MASL, geodetic
datum). It also mirrors a handful of Ontario gauges from ECCC HYDAT — and
those use ECCC's "ASSUMED DATUM," which is offset from MASL by an arbitrary
station-specific constant (typically ~100 m below MASL).

The dashboard's `ORRPB_HISTORIC_PEAKS` constant in `index.html` carries a
`datumOffset` per affected station. The display layer adds the offset to
every raw API value before rendering, so users always see MASL.

| Station (Vigilance ID) | Source | Offset to MASL |
|---|---|---|
| 545 — Mattawa, ON | ECCC `02JE013` | +100.000 m |
| 951 — Temiscaming village, QC | ECCC `02JE025` | +173.65 m |
| Quebec stations (1195, 548, 550, 981, 1264, …) | Vigilance native | 0 m (already MASL) |

The +173.65 m offset for Temiscaming village was calibrated against an
ORRPB-published reading on the day of writing (gauge value 5.002 → published
178.65 MASL). If that gauge's datum is ever rebenchmarked, the offset would
need updating.

## 3. Synthetic flood-state classification

Vigilance assigns each gauge a `etat_niv` (1–6) based on flood-threshold
crossings. But some gauges Vigilance mirrors (Ontario stations, lake-level
gauges) don't have configured thresholds — Vigilance returns `etat_niv = 0`.

To still render a meaningful flood-state colour for those stations, the
dashboard falls back through three layers in priority order:

1. **Vigilance `etat_niv`** if defined (>0) — the canonical answer.
2. **ORRPB reference-year crossing** — if the station has 2017 / 2019 / 2023
   peaks recorded in `ORRPB_HISTORIC_PEAKS`, classify by which reference years
   the current level exceeds:
   - At/above 2019 record → etat 6 (Major flood)
   - Above the second-highest reference year → etat 5
   - Above the third-highest → etat 4
3. **ECCC HYDAT percentile** — for any station whose Vigilance label matches
   the WSC ID pattern (`02XX###`), fetch all historical annual peaks from the
   ECCC `hydrometric-annual-statistics` endpoint and bucket the current
   reading by percentile:
   - ≥ 99 th → etat 6
   - ≥ 95 th → etat 5
   - ≥ 90 th → etat 4
   - ≥ 75 th → etat 3
   - ≥ 50 th → etat 2
   - else → etat 1

Synthetic classifications are flagged with `(est.)` in the badge text so
users know it's not Vigilance-canonical.

## 4. Lac Coulonge percentile rank

The map's Lac Coulonge callout shows e.g. *"94 th %ile (1972–2025)"* — the
season's peak ranked against the 54-year ORRPB record stored in
[`data/lac-coulonge-monthly-1972-2026.csv`](../data/lac-coulonge-monthly-1972-2026.csv).

Computed as:

```
rank = number of historical annual peaks > current_peak, plus 1
percentile = round((54 - rank + 1) / 54 × 100)
```

So a 94th-percentile reading means "higher than 94 % of the 54 historical
annual peaks." Used to communicate "is this an unusual year?" at a glance.

## 5. Daily change (delta vs ~24 h ago)

Most cards show a 24 h change indicator (cm/24h or pp/24h for reservoirs).

For river gauges, computed by walking the Vigilance reading buffer for each
station and finding the reading closest to `now − 24 h`. Rejects results more
than 6 h off the 24 h target to avoid misleading deltas on sparse buffers.

For reservoirs, computed similarly against TimescaleDB history with a 7-day
fetch window and a 12 h "minimum gap" guard so the search can't accidentally
match the latest reading against itself.

## 6. Freeze-night counter

The basin-weather panel counts "basin-wide freeze nights" — nights where
**every** upstream weather station's overnight low went below 0 °C. Three
or more in a 7-day window signals snowmelt is paused or pausing.

Only **upstream** stations count (Val-d'Or QC, Rouyn-Noranda QC, Temiskaming
Shores ON, Pembroke ON). Downstream stations (Ottawa-Gatineau, Hawkesbury ON)
are shown for visitor context but excluded from the freeze-night tally — they
don't drive snowmelt timing for the upper basin.
