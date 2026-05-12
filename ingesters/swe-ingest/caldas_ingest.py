"""
CaLDAS-NSRPS snow-water-equivalent ingester (Ottawa River basin).

Samples ECCC GeoMet layer `CaLDAS-NSRPS_2.5km_SnowWaterEquiv` ("Snow water
equivalent (land surface) [mm]" — the Canadian operational land-data-
assimilation analysis, 2.5 km) via WMS GetFeatureInfo at a fixed list of
named points across the basin's sub-basins, and writes one swe_daily row per
point per day (source='caldas-nsrps').

Why points and not an area mean: python:3.12-alpine has no GDAL/rasterio, and
GetFeatureInfo is dependency-free. The named points are chosen to (a) match the
labels on the ORRPB's biweekly SWE map and (b) line up with the ECCC stations
the case file already uses (Val-d'Or, Parent, Témiscaming), so the series are
directly comparable. Sub-basin means are then just an aggregate query over
swe_locations.subbasin.

GeoMet serves only the current analysis (its `time` dimension is a single
timestamp), so there's no historical pull — the archive accumulates forward
from when this cron starts. ERA5-Land (era5_ingest.py) carries the back-history.

A snow-free point in the CaLDAS domain returns an empty GetFeatureInfo feature
collection; we record that as 0.0 mm (not a gap). Coordinates outside the
NSRPS domain would also return empty — all the points below are in-domain.

Stdlib only. Env: POSTGREST_URL (default in-cluster service).
"""

import json
import os
import sys
import time as _time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

POSTGREST = os.environ.get("POSTGREST_URL", "http://postgrest.data.svc.cluster.local:3000")
GEOMET = "https://geo.weather.gc.ca/geomet"
LAYER = "CaLDAS-NSRPS_2.5km_SnowWaterEquiv"
USER_AGENT = "homelab-freshet-swe-ingest/1 (+https://github.com/aachtenberg/ottawa-river-freshet)"

# region slug, display name, sub-basin slug, lat, lon.
# Sub-basins: upper-ottawa (Témiscaming reach + Quebec headwaters / Cabonga-
# Dozois), gatineau, lievre, lower-mainstem (Pembroke down to Ottawa, incl.
# Petawawa / Coulonge / Bonnechère drainage on either bank).
POINTS = [
    # --- upper Ottawa main stem & northern headwaters (the dominant freshet feeder) ---
    ("temiscaming",        "Témiscaming, QC",            "upper-ottawa",   46.72, -79.10),
    ("ville-marie",        "Ville-Marie, QC",            "upper-ottawa",   47.33, -79.43),
    ("rouyn-noranda",      "Rouyn-Noranda, QC",          "upper-ottawa",   48.24, -79.02),
    ("val-dor",            "Val-d'Or, QC",               "upper-ottawa",   48.05, -77.78),
    ("parent",             "Parent, QC (Cabonga hdw.)",  "upper-ottawa",   47.92, -74.62),
    ("dozois",             "Dozois reservoir area, QC",  "upper-ottawa",   47.50, -77.00),
    ("mattawa",            "Mattawa, ON",                "upper-ottawa",   46.32, -78.70),
    # --- Gatineau River sub-basin ---
    ("maniwaki",           "Maniwaki, QC",               "gatineau",       46.38, -75.97),
    ("baskatong",          "Baskatong reservoir, QC",    "gatineau",       46.80, -75.85),
    ("sainte-anne-du-lac", "Sainte-Anne-du-Lac, QC",     "gatineau",       46.87, -75.33),
    # --- Lièvre River sub-basin ---
    ("mont-laurier",       "Mont-Laurier, QC",           "lievre",         46.55, -75.50),
    ("lac-du-cerf",        "Lac-du-Cerf, QC (Lièvre)",   "lievre",         46.45, -75.36),
    # --- lower main stem (Pembroke -> Ottawa, both banks) ---
    ("pembroke",           "Pembroke, ON",               "lower-mainstem", 45.82, -77.11),
    ("petawawa",           "Petawawa R. headwaters, ON", "lower-mainstem", 45.90, -78.00),
    ("fort-coulonge",      "Fort-Coulonge, QC",          "lower-mainstem", 45.84, -76.73),
    ("ottawa",             "Ottawa, ON",                 "lower-mainstem", 45.42, -75.70),
]


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


def sample_point(lat, lon):
    """Return (swe_mm, analysis_iso) for the point, or (None, None) on error.
    Empty feature collection (in-domain, snow-free) -> (0.0, None)."""
    d = 0.05  # ~5-6 km half-box; the 5x5 grid + centre pixel lands inside it
    bbox = f"{lat - d},{lon - d},{lat + d},{lon + d}"  # WMS 1.3.0 EPSG:4326 axis order = lat,lon
    params = {
        "SERVICE": "WMS", "VERSION": "1.3.0", "REQUEST": "GetFeatureInfo",
        "LAYERS": LAYER, "QUERY_LAYERS": LAYER, "CRS": "EPSG:4326",
        "BBOX": bbox, "WIDTH": "5", "HEIGHT": "5", "I": "2", "J": "2",
        "INFO_FORMAT": "application/json", "STYLES": "",
    }
    url = GEOMET + "?" + urllib.parse.urlencode(params)
    try:
        body = get_json(url)
    except Exception as e:
        print(f"    GetFeatureInfo error: {e}", file=sys.stderr)
        return None, None
    try:
        j = json.loads(body)
    except json.JSONDecodeError:
        # GeoMet returns an XML ServiceException on bad requests
        print(f"    non-JSON response: {body[:200]}", file=sys.stderr)
        return None, None
    feats = j.get("features") or []
    if not feats:
        return 0.0, None  # in-domain, no snow
    props = feats[0].get("properties", {})
    val = props.get("value")
    if val is None:
        return 0.0, None
    return float(val), props.get("time")


def post(table, rows, prefer="resolution=merge-duplicates"):
    if not rows:
        return
    body = json.dumps(rows).encode("utf-8")
    req = urllib.request.Request(
        f"{POSTGREST}/{table}", data=body, method="POST",
        headers={"Content-Type": "application/json", "Prefer": prefer},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        print(f"  POST /{table} -> HTTP {r.status} ({len(rows)} rows)")


def main():
    today = datetime.now(timezone.utc).date()
    rows, locs = [], []
    analysis_iso = None
    for slug, name, subbasin, lat, lon in POINTS:
        swe, t_iso = sample_point(lat, lon)
        if t_iso and not analysis_iso:
            analysis_iso = t_iso
        if swe is None:
            print(f"  {slug:20s} -> SKIP (fetch failed)")
        else:
            # date the row to the analysis day if GeoMet gave one, else today UTC
            day = (datetime.fromisoformat(t_iso.replace("Z", "+00:00")).date()
                   if t_iso else today)
            rows.append({"time": day.isoformat(), "region": slug,
                         "source": "caldas-nsrps", "swe_mm": round(swe, 2),
                         "swe_dep_mm": None})
            print(f"  {slug:20s} -> {swe:7.2f} mm  ({day})")
        locs.append({"region": slug, "name": name, "kind": "point",
                     "subbasin": subbasin, "lat": lat, "lon": lon,
                     "source": "caldas-nsrps"})
        _time.sleep(0.3)  # be polite to GeoMet

    if not rows:
        print("No SWE rows produced — aborting (did GeoMet change the layer name?).", file=sys.stderr)
        sys.exit(1)

    print(f"Analysis timestamp: {analysis_iso or '(none — all points snow-free)'}")
    post("swe_daily", rows)
    post("swe_locations", locs, prefer="resolution=merge-duplicates")
    print(f"Done: {len(rows)} swe_daily rows, {len(locs)} swe_locations upserts.")


if __name__ == "__main__":
    main()
