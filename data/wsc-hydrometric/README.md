# WSC hydrometric data — Ottawa River basin stations

Daily flow (m³/s) and water-level (m) records extracted from the Water
Survey of Canada HYDAT database for the Ottawa River basin.

## Source

WSC publishes the entire Canadian hydrometric record as a SQLite database,
refreshed quarterly:

    https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/

This extract is from `Hydat_sqlite3_20260417.zip` (modified 2026-04-17).

## Re-running

    # Download and unzip the latest HYDAT to /tmp/hydat/Hydat.sqlite3, then:
    python3 ingesters/climate-history/wsc_hydat_extract.py

The script reads from `/tmp/hydat/Hydat.sqlite3` and writes
`<slug>/daily.csv` for each station plus a `manifest.csv`. Bump the
`HYDAT_SOURCE_URL` constant in the script when a newer HYDAT is published.

## Layout

```
manifest.csv                       # station_number, slug, name, coverage, source URL, output file
<slug>/
  daily.csv                        # date, flow_cms, flow_symbol, level_m, level_symbol
```

## Stations

| station | slug | what | coverage |
|---|---|---|---|
| `02KF005` | `britannia-ottawa-river` | Ottawa River at Britannia (downtown Ottawa) | flow + level 1960–2024 |
| `02KC017` | `bryson-centrale` | Bryson generating station (the dam) | flow only, **1985–1994** |
| `02KC011` | `portage-du-fort` | Ottawa River at Portage-du-Fort (just downstream of Lac Coulonge) | flow only, **1942–1948** |
| `02KG001` | `coulonge-fort-coulonge` | Coulonge River near Fort-Coulonge | flow only, **1926–1993** |
| `02KG005` | `coulonge-pontefract-golf` | Coulonge River at Terry Fox bridge (Pontefract golf course) | flow + level, **2004–2008** |
| `02LH001` | `gatineau-maniwaki` | Gatineau River at Maniwaki | level 1925–1998, flow 1925–1926 |
| `02KF009` | `chats-falls-ottawa-river` | Ottawa River at Chats Falls | flow only, **1915–1994** |

## Critical coverage gap (relevant to the regime-change case file)

**There is no public WSC flow data for the Lac Coulonge gauge or the
Bryson dam after 1994.** The Bryson station (02KC017) was discontinued
the same year, and the upstream Ottawa River flow stations
(Portage-du-Fort, Chats Falls) were also discontinued in or before 1994.

This matters for **Goal 4 of the climate analysis** (rating-curve check):

> *Did Water Survey of Canada update the rating curve at Lac Coulonge
> gauge after the 2019 super-flood? A rating curve translates flow (m³/s)
> to level (m). Major floods scour channels; if the post-2019 channel
> passes the same flow at a higher level, the same water now produces a
> higher gauge reading — making it look like floods are worse when
> actually flows are the same.*

That check is **not directly possible from public data**. The Quebec
provincial Vigilance API publishes Lac Coulonge level only; no flow.
WSC's historical flow record at the Lac Coulonge / Bryson area ends in
the early 1990s. A rating-curve verification would need to either:

1. Request the current and historical rating curves directly from the
   Centre d'expertise hydrique du Québec (CEHQ), or
2. Use Britannia (02KF005) as an indirect proxy — Britannia flow is
   downstream of Lac Coulonge and would show any whole-river regime
   shift, though it can't isolate channel changes specific to the
   Lac Coulonge cross-section.

The Britannia 2019 super-flood peak in this dataset is **5980 m³/s on
2019-05-01**, matching the year-overlay panels published by community
analysts.

## Stations that ARE useful

- **Britannia (02KF005)** — the long-running flagship Ottawa River
  station. Flow + level 1960–2024 with daily resolution. Suitable for:
  Dan's year-overlay reproduction; whole-river flow context for
  Lac Coulonge peaks; downstream-proxy estimates for rating-curve
  questions.
- **Coulonge near Fort-Coulonge (02KG001)** — 67 years of flow on the
  user's actual local tributary, useful for pre-regime-change baseline
  even though it ends in 1993.
- **Coulonge at Pontefract (02KG005)** — only four years of data, but
  the gauge sits at Mansfield-et-Pontefract right by the user's
  property. Worth keeping for reference.

## Schema

| column | unit | notes |
|---|---|---|
| `date` | ISO date | YYYY-MM-DD |
| `flow_cms` | m³/s | daily mean discharge; empty if not measured |
| `flow_symbol` | code | WSC quality code (E = estimated, B = ice-affected, etc.); blank = unflagged |
| `level_m` | m above local datum | daily mean stage; empty if not measured |
| `level_symbol` | code | WSC quality code for the level reading |

WSC quality codes are documented at
<https://wateroffice.ec.gc.ca/contactus/faq_e.html>.
