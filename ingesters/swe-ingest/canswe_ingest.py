"""
CanSWE in-situ snow-water-equivalent loader (Ottawa River basin subset).

Loads the Ottawa-basin stations from the "Canadian historical Snow Water
Equivalent database" (CanSWE; Vionnet et al., ESSD 2021) into swe_daily with
source='canswe', one row per (station, observation date). This is the
"boots on the ground" feed — manual snow surveys + automatic snow pillows +
passive-gamma SWE sensors run by Ontario MNR, OPG, Hydro-Québec, MSC, etc. —
the thing the gridded analyses (CaLDAS, ERA5-Land) are meant to approximate.

CanSWE is distributed as a single NetCDF on the Federated Research Data
Repository (DOI 10.20383/103.0329), Open Government Licence — Canada, updated
~annually. It is NOT cron-friendly to download (FRDR uses Globus auth), so this
is a one-shot loader you run when a new CanSWE version drops:

    python3 canswe_ingest.py /path/to/CanSWE-CanEEN_YYYY-YYYY_vN.nc

(or set CANSWE_NC=/path/to/file.nc). It POSTs to the PostgREST proxy like the
cluster ingesters; merge-duplicates upserts make a re-run idempotent. Requires
netCDF4 + numpy.

The CanSWE `snw` variable is "Water equivalent of snow cover" in kg m**-2,
which equals mm of SWE 1:1 — no conversion. Snow surveys are roughly monthly in
winter, so each station contributes ~5-15 points per snow season, not daily.

Env: POSTGREST_URL, CANSWE_NC, CANSWE_BBOX ("S,W,N,E", default Ottawa basin),
CANSWE_POST_BATCH (default 2000).
"""

import json
import os
import sys
import urllib.request
from datetime import date

POSTGREST = os.environ.get("POSTGREST_URL", "http://postgrest.data.svc.cluster.local:3000")
POST_BATCH = int(os.environ.get("CANSWE_POST_BATCH", "2000"))
# bbox = South, West, North, East — generous box over the Ottawa basin (the
# basin is a "C", so a box always catches a few near-edge non-basin stations;
# lat/lon land in swe_locations so a precise polygon clip is a downstream query)
_b = os.environ.get("CANSWE_BBOX", "44.0,-80.0,49.5,-73.0")
S, W, N, E = (float(x) for x in _b.split(","))
SPLIT_LAT = 46.7  # north/south divide — matches the ERA5-Land regions
SUBNET = "upper-ottawa"
MES_KIND = {0: "station-manual", 1: "station-pillow", 2: "station-gamma"}


def post(table, rows):
    for i in range(0, len(rows), POST_BATCH):
        chunk = rows[i:i + POST_BATCH]
        req = urllib.request.Request(
            f"{POSTGREST}/{table}", data=json.dumps(chunk).encode("utf-8"),
            method="POST", headers={"Content-Type": "application/json",
                                    "Prefer": "resolution=merge-duplicates"})
        with urllib.request.urlopen(req, timeout=120) as r:
            print(f"  POST /{table} -> HTTP {r.status} ({len(chunk)} rows, "
                  f"{min(i + POST_BATCH, len(rows))}/{len(rows)})")


def main():
    nc_path = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get("CANSWE_NC"))
    if not nc_path or not os.path.exists(nc_path):
        print("Usage: canswe_ingest.py <CanSWE.nc>  (or set CANSWE_NC). "
              "Download from FRDR DOI 10.20383/103.0329.", file=sys.stderr)
        sys.exit(2)

    import numpy as np
    from netCDF4 import Dataset, num2date

    ds = Dataset(nc_path)
    lat = np.asarray(ds.variables["lat"][:], dtype="float64")
    lon = np.asarray(ds.variables["lon"][:], dtype="float64")
    elev = np.asarray(ds.variables["elevation"][:], dtype="float64")
    sid = [str(x) for x in ds.variables["station_id"][:]]
    sname = [str(x) for x in ds.variables["station_name"][:]]
    sprov = [str(x) for x in ds.variables["source"][:]]
    tmes = np.asarray(ds.variables["type_mes"][:])
    tvar = ds.variables["time"]
    times = num2date(tvar[:], tvar.units, calendar=getattr(tvar, "calendar", "standard"),
                     only_use_cftime_datetimes=False)
    days = [date(t.year, t.month, t.day).isoformat() for t in times]
    snw = ds.variables["snw"]  # kg m**-2 == mm SWE

    in_box = (lat >= S) & (lat <= N) & (lon >= W) & (lon <= E)
    keep = np.where(in_box)[0]
    print(f"CanSWE: {nc_path}  — {len(keep)} of {len(lat)} stations in bbox "
          f"S{S} W{W} N{N} E{E}")

    rows, locs = [], []
    for i in keep:
        col = np.ma.filled(snw[i, :].astype("float64"), np.nan)
        valid = np.where(np.isfinite(col))[0]
        if valid.size == 0:
            continue
        region = sid[i]
        for j in valid:
            rows.append({"time": days[j], "region": region, "source": "canswe",
                         "swe_mm": round(float(col[j]), 2), "swe_dep_mm": None})
        prov = sprov[i].strip()
        nm = sname[i].strip().title()
        locs.append({
            "region": region,
            "name": f"{nm} ({prov})" if prov else nm,
            "kind": MES_KIND.get(int(tmes[i]), "station"),
            "subbasin": SUBNET if lat[i] >= SPLIT_LAT else "lower-mainstem",
            "lat": round(float(lat[i]), 5), "lon": round(float(lon[i]), 5),
            "source": "canswe",
        })
    ds.close()

    if not rows:
        print("No CanSWE rows in the bbox — nothing to load.", file=sys.stderr)
        sys.exit(1)
    span = (min(r["time"] for r in rows), max(r["time"] for r in rows))
    print(f"CanSWE: {len(rows)} SWE observations across {len(locs)} stations, "
          f"{span[0]} .. {span[1]}")
    post("swe_daily", rows)
    post("swe_locations", locs)
    print("Done.")


if __name__ == "__main__":
    main()
