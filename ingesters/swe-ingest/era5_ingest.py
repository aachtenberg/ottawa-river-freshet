"""
ERA5-Land snow-water-equivalent ingester (Ottawa River basin).

Pulls Copernicus ERA5-Land `snow_depth_water_equivalent` (despite the name,
this variable IS snow water equivalent — units: m of water equivalent) for a
bounding box over the Ottawa River basin, one timestep per day (00:00 UTC —
SWE is a slowly-varying state variable, so a daily snapshot is plenty and keeps
the download tiny), and writes swe_daily rows (source='era5land') for:
  - 'basin-total'  — mean over the whole bbox
  - 'north-half'   — mean over the bbox north of 46.7 N (the upper-Ottawa /
                     Témiscaming reach — the "is the north carrying more than
                     the maps showed" question)
  - 'south-half'   — mean over the bbox south of 46.7 N (lower main stem,
                     Gatineau/Lièvre mouths)

ERA5-Land runs 1950 -> ~5 days ago, so this is the deep-history feed (the
CaLDAS-NSRPS ingester only has the current operational analysis). Two modes:
  - rolling (default): request the last ERA5_LOOKBACK_DAYS days.
  - backfill: set ERA5_START / ERA5_END (YYYY-MM-DD) to request a fixed range;
    if the range spans >1 calendar year it is fetched year-by-year so a partial
    run is resumable.

Deps: cdsapi (pure-python) + netCDF4. Image installs them at start (see
swe-ingest.yml). Auth: writes ~/.cdsapirc from CDS_API_URL (default
https://cds.climate.copernicus.eu/api) and CDS_API_KEY (your CDS Personal
Access Token). The dataset licence must be accepted once on the CDS website or
requests 403.

Env: POSTGREST_URL, CDS_API_KEY (required), CDS_API_URL, ERA5_LOOKBACK_DAYS
(default 14), ERA5_START, ERA5_END, ERA5_BBOX ("N,W,S,E", default Ottawa basin).
"""

import json
import os
import sys
import tempfile
import urllib.request
from datetime import date, datetime, timedelta, timezone

POSTGREST = os.environ.get("POSTGREST_URL", "http://postgrest.data.svc.cluster.local:3000")
DATASET = "reanalysis-era5-land"
VARIABLE = "snow_depth_water_equivalent"
# bbox as CDS "area" = [North, West, South, East]; default covers the Ottawa basin
_bbox_env = os.environ.get("ERA5_BBOX", "48.5,-80.0,45.0,-74.0")
NORTH, WEST, SOUTH, EAST = (float(x) for x in _bbox_env.split(","))
SPLIT_LAT = 46.7  # north/south divide ~ Témiscaming reach vs lower basin
LOOKBACK_DAYS = int(os.environ.get("ERA5_LOOKBACK_DAYS", "14"))


def write_cdsapirc():
    key = os.environ.get("CDS_API_KEY")
    if not key:
        print("CDS_API_KEY not set — cannot talk to the Climate Data Store.", file=sys.stderr)
        sys.exit(2)
    url = os.environ.get("CDS_API_URL", "https://cds.climate.copernicus.eu/api")
    rc = os.path.expanduser("~/.cdsapirc")
    with open(rc, "w") as f:
        f.write(f"url: {url}\nkey: {key}\n")
    os.chmod(rc, 0o600)


def day_range(start: date, end: date):
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def fetch_block(client, year, months, days):
    """Download one ERA5-Land NetCDF for (year, months, days) -> temp filepath."""
    target = tempfile.NamedTemporaryFile(suffix=".nc", delete=False).name
    client.retrieve(DATASET, {
        "variable": VARIABLE,
        "year": [str(year)],
        "month": [f"{m:02d}" for m in sorted(set(months))],
        "day": [f"{d:02d}" for d in sorted(set(days))],
        "time": ["00:00"],
        "area": [NORTH, WEST, SOUTH, EAST],
        "data_format": "netcdf",
        "download_format": "unarchived",
    }, target)
    return target


def _maybe_unzip(path):
    """CDS-Beta sometimes wraps the NetCDF in a zip even with download_format
    'unarchived'. If `path` is a zip, extract the first .nc and return it."""
    with open(path, "rb") as f:
        if f.read(4) != b"PK\x03\x04":
            return path
    import zipfile
    with zipfile.ZipFile(path) as z:
        members = [n for n in z.namelist() if n.endswith(".nc")]
        if not members:
            raise RuntimeError(f"zip from CDS contains no .nc: {z.namelist()}")
        out = tempfile.NamedTemporaryFile(suffix=".nc", delete=False).name
        with z.open(members[0]) as src, open(out, "wb") as dst:
            dst.write(src.read())
    os.unlink(path)
    return out


def parse_nc(path):
    """Yield (date, region, swe_mm) from an ERA5-Land NetCDF file."""
    import numpy as np
    from netCDF4 import Dataset, num2date

    path = _maybe_unzip(path)
    ds = Dataset(path)
    # locate the SWE variable (CDS NetCDF naming has drifted: 'sd' / 'swe' / full name)
    candidates = [v for v in ds.variables if v.lower() in ("sd", "swe", "snow_depth_water_equivalent")]
    if not candidates:
        candidates = [v for v, var in ds.variables.items()
                      if "snow" in getattr(var, "long_name", "").lower()
                      and "equiv" in getattr(var, "long_name", "").lower()]
    if not candidates:
        ds.close()
        raise RuntimeError(f"no SWE variable in {path}; vars={list(ds.variables)}")
    vname = candidates[0]
    var = ds.variables[vname]
    units = getattr(var, "units", "").lower()
    scale = 1000.0 if ("m of water" in units or units in ("m", "metre", "meter")) else 1.0

    # time coord (named 'time' or 'valid_time' in newer CDS files)
    tname = next((t for t in ("valid_time", "time") if t in ds.variables), None)
    tvar = ds.variables[tname]
    times = num2date(tvar[:], tvar.units, only_use_cftime_datetimes=False)

    lats = ds.variables["latitude"][:]
    lons = ds.variables["longitude"][:]
    lat2d = np.asarray(lats)[:, None] * np.ones((1, len(lons)))
    north_mask = lat2d >= SPLIT_LAT
    south_mask = ~north_mask

    arr = np.ma.filled(var[:].astype("float64"), np.nan)  # shape (time, lat, lon)
    out = []
    for i, t in enumerate(times):
        d = date(t.year, t.month, t.day)
        plane = arr[i]
        for region, mask in (("basin-total", np.ones_like(plane, dtype=bool)),
                             ("north-half", north_mask), ("south-half", south_mask)):
            vals = plane[mask]
            vals = vals[~np.isnan(vals)]
            if vals.size:
                out.append((d, region, round(float(vals.mean()) * scale, 3)))
    ds.close()
    return out


def post_rows(rows):
    if not rows:
        return
    payload = [{"time": d.isoformat(), "region": r, "source": "era5land",
                "swe_mm": v, "swe_dep_mm": None} for d, r, v in rows]
    for i in range(0, len(payload), 2000):
        chunk = payload[i:i + 2000]
        req = urllib.request.Request(
            f"{POSTGREST}/swe_daily", data=json.dumps(chunk).encode(),
            method="POST", headers={"Content-Type": "application/json",
                                    "Prefer": "resolution=merge-duplicates"})
        with urllib.request.urlopen(req, timeout=120) as r:
            print(f"  POST /swe_daily -> HTTP {r.status} ({len(chunk)} rows)")


def post_locations():
    locs = [
        {"region": "basin-total", "name": "Ottawa River basin (bbox mean)", "kind": "basin",
         "subbasin": None, "lat": (NORTH + SOUTH) / 2, "lon": (WEST + EAST) / 2, "source": "era5land"},
        {"region": "north-half", "name": "Ottawa basin north of 46.7°N (bbox mean)", "kind": "subbasin",
         "subbasin": "upper-ottawa", "lat": (NORTH + SPLIT_LAT) / 2, "lon": (WEST + EAST) / 2, "source": "era5land"},
        {"region": "south-half", "name": "Ottawa basin south of 46.7°N (bbox mean)", "kind": "subbasin",
         "subbasin": "lower-mainstem", "lat": (SPLIT_LAT + SOUTH) / 2, "lon": (WEST + EAST) / 2, "source": "era5land"},
    ]
    req = urllib.request.Request(f"{POSTGREST}/swe_locations", data=json.dumps(locs).encode(),
                                 method="POST", headers={"Content-Type": "application/json",
                                                         "Prefer": "resolution=merge-duplicates"})
    with urllib.request.urlopen(req, timeout=60) as r:
        print(f"  POST /swe_locations -> HTTP {r.status} ({len(locs)} rows)")


def main():
    write_cdsapirc()
    import cdsapi
    client = cdsapi.Client()

    start_env, end_env = os.environ.get("ERA5_START"), os.environ.get("ERA5_END")
    if start_env and end_env:
        start = date.fromisoformat(start_env)
        end = date.fromisoformat(end_env)
        mode = "backfill"
    else:
        # ERA5-Land lags ~5 days; pull a generous trailing window
        end = datetime.now(timezone.utc).date() - timedelta(days=6)
        start = end - timedelta(days=LOOKBACK_DAYS)
        mode = "rolling"
    print(f"ERA5-Land SWE ingest [{mode}]: {start} .. {end}  bbox N{NORTH} W{WEST} S{SOUTH} E{EAST}")

    # group requested days by calendar year so a big backfill is chunked/resumable
    by_year = {}
    for d in day_range(start, end):
        by_year.setdefault(d.year, []).append(d)

    total = 0
    for year in sorted(by_year):
        days = by_year[year]
        months = {d.month for d in days}
        # ERA5-Land is happy with the full day-of-month list even if some
        # (month, day) combos don't exist; it just returns the valid ones.
        dom = {d.day for d in days}
        print(f"  year {year}: {len(days)} days ({min(days)}..{max(days)})")
        try:
            nc = fetch_block(client, year, months, dom)
        except Exception as e:
            msg = str(e)
            if "403" in msg or "licence" in msg.lower() or "license" in msg.lower():
                print("  -> 403 / licence not accepted. Accept the ERA5-Land licence on the "
                      "CDS website (dataset 'ERA5-Land hourly data from 1950 to present' -> Download "
                      "-> tick the licence), then re-run.", file=sys.stderr)
                sys.exit(3)
            print(f"  -> retrieve failed for {year}: {e}", file=sys.stderr)
            continue
        try:
            rows = [(d, r, v) for (d, r, v) in parse_nc(nc) if start <= d <= end]
        finally:
            try:
                os.unlink(nc)
            except OSError:
                pass
        post_rows(rows)
        total += len(rows)

    if total:
        post_locations()
    print(f"Done: {total} swe_daily rows (source=era5land).")
    if total == 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
