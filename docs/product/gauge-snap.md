# Snap-to-gauge + override rules

Status: **defined**. Default algorithm + Lac Deschênes shore-zone overrides. Station catalog: [`snap-stations.json`](./snap-stations.json).

Problem this solves: **gauge ≠ shoreline**. On wide lakes, nearest GPS often picks the wrong instrument. Lac Deschênes is the worst case in this corridor (Buckhams vs Britannia routinely confused in local media despite ~15 km and 10–30 cm freshet offset).

---

## Goals

1. From a user pin (GPS or map drop), propose a **home gauge** from the corridor set.
2. Always **confirm** before locking; always allow **override**.
3. Prefer shoreline-correct Deschênes gauges over naive nearest-neighbour when the pin is on that lake.
4. Derive upstream / downstream neighbors from corridor order, not from distance.

Non-goals: inventing new gauges, replacing ORRPB location pages, or auto-picking without a confirm sheet.

---

## Corridor snap set

Use the same upstream→downstream order as `CORRIDOR_BAR_STATIONS` (main stem only — no tributary 1004 in the snap set):

| Order | ID | Name | Source |
|---|---|---|---|
| 0 | 951 | Temiscaming | Vigilance / WSC |
| 1 | 545 | Mattawa | Vigilance / WSC |
| 2 | 1279 | Waltham | Vigilance |
| 3 | 1195 | Lac Coulonge | Vigilance |
| 4 | 99001 | Buckhams Bay | MVCA KiWIS |
| 5 | 984 | Aylmer | Vigilance |
| 6 | 548 | Britannia | Vigilance / WSC |
| 7 | 550 | Hull | Vigilance / WSC |
| 8 | 981 | Masson | Vigilance |
| 9 | 1264 | Rigaud | Vigilance |

Coordinates live in [`snap-stations.json`](./snap-stations.json) (hydrated 2026-07-22 from Vigilance `geom_p` + MVCA KiWIS). Re-hydrate before ship if stations move.

Tributaries (e.g. Coulonge River 1004) may appear as **optional neighbor context**, never as the snapped home gauge, unless the user overrides into an advanced list.

---

## Algorithm

### 1. Inputs

- `pin = { lat, lon }` from GPS or map drop
- Catalog = `snap-stations.json`
- Optional: place-name geocode → same pin shape

### 2. Distance rank (always computed)

Haversine distance from pin to every catalog station. Keep sorted list `candidates[]`.

### 3. Region gate — Lac Deschênes

If pin is inside the Deschênes bbox:

```
lat ∈ [45.35, 45.53]
lon ∈ [-76.15, -75.72]
```

then **replace** the default nearest with the shore-zone result below. Still keep the full distance rank for the confirm sheet’s “other nearby” list.

Outside that bbox → home gauge = `candidates[0]` (nearest corridor station).

### 4. Lac Deschênes shore zones (override nearest)

Lake axis runs roughly **NW (Buckhams / Constance Bay) → SE (Britannia)**, then the river continues to Hull.

Assign by **longitude bands** (primary), with a Hull exception:

| Zone | Lon band | Home gauge | Typical shoreline |
|---|---|---|---|
| NW arm | `lon ≤ -75.95` | **99001 Buckhams Bay** | Constance Bay, Buckhams Bay, Torbolton / northwest ON shore |
| Mid-lake | `-75.95 < lon ≤ -75.83` | **984 Aylmer** | Aylmer marina, Deschênes (QC), mid-lake |
| SE lake | `-75.83 < lon ≤ -75.75` | **548 Britannia** | Britannia, west Nepean / Ottawa end of the lake |
| Below lake | `lon > -75.75` **or** pin clearly downstream of Chaudière | **550 Hull** | Gatineau marina / Hull reach — only if not still on the open lake |

**Hard rule (media confusion):** if the raw nearest station is Britannia (548) but `lon ≤ -75.95`, **force Buckhams (99001)**. Never silently assign Britannia to Constance Bay.

**Soft rule:** if nearest and shore-zone disagree, prefer shore-zone and flag `ambiguous: true` on the confirm sheet.

### 5. Neighbors

Given corridor index `i` of the chosen home gauge:

- Upstream = station at `i - 1` (omit if `i == 0`)
- Downstream = station at `i + 1` (omit if last)
- Optional second upstream for “incoming” strip when home is on Deschênes: show Buckhams → Aylmer → Britannia as the three-card strip when home ∈ {99001, 984, 548}

### 6. Confirm sheet (mandatory)

Never silently persist. Sheet copy:

> We’ll watch **{name}** for you — ~{N} km from your pin.  
> Upstream lead: **{up}**. Downstream: **{down}**.

Show:

1. Proposed gauge (primary)
2. Top 3 by distance (even if shore-zone overrode)
3. Explicit **Change gauge** → full corridor picker
4. If `ambiguous` or distance to proposed > **12 km**: warning chip *“Wide lake / sparse gauges — please confirm”*

### 7. Override rules

| Action | Result |
|---|---|
| Accept proposed | Persist `homeGaugeId`, `homePin`, `snapMethod` (`nearest` \| `deschenes_zone`), `snapDistanceKm` |
| Pick from top-3 or corridor list | Persist with `snapMethod: 'override'`; keep original proposal in `snapProposedId` for analytics |
| Move pin later | Re-run snap; if new proposal ≠ saved gauge, re-confirm (don’t silently switch) |
| GPS denied | Map-drop only; same pipeline |

User override always wins until they change it again.

---

## Worked examples (Deschênes)

Using catalog coords (Buckhams 45.500/−76.105, Aylmer 45.394/−75.858, Britannia 45.364/−75.806, Hull 45.432/−75.706):

| Pin story | Lon | Naive nearest (typical) | Rule result |
|---|---|---|---|
| Constance Bay cottage | ~−76.08 | Could be Buckhams (good) or, from mid-bay quirks, something else | Zone NW → **99001** |
| Mid-lake ON shore near −75.90 | ~−75.90 | Often Aylmer or Britannia | Zone mid → **984** |
| Britannia / Lincoln Fields shore | ~−75.81 | Britannia | Zone SE → **548** |
| Gatineau marina | ~−75.71 | Hull | Below lake → **550** |
| Pin near Britannia but lon −76.05 (bad GPS / wrong drop) | −76.05 | Might still prefer Britannia by some paths | Hard rule → **99001** + ambiguous confirm |

---

## Other wide-water notes

| Reach | Guidance |
|---|---|
| Lac Coulonge | Usually 1195; pin near Fort-Coulonge / Mansfield snaps cleanly. Keep override for Westmeath / Pembroke-edge users who may want Waltham (1279) as upstream home instead. |
| Lac Deschênes | **Must** use shore zones above. |
| Narrow main stem (Mattawa, Waltham, Masson, Rigaud) | Nearest is enough; still confirm. |

---

## Implementation sketch

```text
function proposeHomeGauge(pin, catalog):
  ranked = sortByHaversine(pin, catalog)
  if inDeschenesBbox(pin):
    proposed = deschenesShoreZone(pin)   // may set ambiguous
  else:
    proposed = ranked[0]
  return { proposed, ranked, ambiguous, neighbors: corridorNeighbors(proposed) }
```

Persist under the MVP profile key (see [mvp-pwa.md](./mvp-pwa.md)). Catalog refresh: one-time hydrate from Vigilance metadata + KiWIS station list; commit JSON; do not require a live coord fetch for snap to work offline after install.

---

## Acceptance checks

1. Constance Bay pin → Buckhams, not Britannia.
2. Britannia pin → Britannia; upstream Aylmer or Buckhams, downstream Hull.
3. Mansfield pin → Lac Coulonge (1195).
4. Override to a non-nearest gauge persists across reload.
5. Moving the pin across a Deschênes zone boundary prompts re-confirm.
