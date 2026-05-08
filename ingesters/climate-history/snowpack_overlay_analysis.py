#!/usr/bin/env python3
"""
Compute basin-weighted peak snowpack and spring rain by year, paired with
Lac Coulonge annual peaks. Output is a JSON file consumed by the
Exhibit H climate-overlay HTML, plus a printed summary table for quick
analytical review.

Provenance:
    Built in response to a Northern Reservoirs Flood Watch FB question
    asking what yearly snowpack and spring rain look like overlaid on
    the Exhibit A super-flood frequency chart. The case file's Test B
    (lac_coulonge_climate_regression.py) already establishes that the
    post-2017 peak step-change does not match a coherent climate step;
    this script renders the same finding as a paired-time-series
    visualization rather than a regression-residual.

Method:
    - Stations: Val-d'Or A (upper Ottawa headwaters), Parent (Cabonga
      headwaters), Barrage Témiscamingue (Lac Coulonge main feeder).
      These three are the upstream-of-Lac-Coulonge ECCC stations that
      cover 1972-2025+ continuously and are the most causally relevant
      to Lac Coulonge freshet inflow.
    - Peak snowpack = max daily Snow-on-Ground (cm) in Feb-Mar of each
      year. Captures the late-winter snowpack standing on the ground
      immediately before the freshet begins.
    - Spring rain = sum of Total Precip (mm) over April + May. ECCC
      stopped reporting the separated "Total Rain" field at these
      stations in the late-1990s; only "Total Precip" is continuous
      across the full 1972-present record. By April-May at upper-basin
      stations precip is overwhelmingly rain (sub-zero overnight is
      possible in early April but the daytime mean is well above
      freezing), so total precip is a reasonable proxy for "spring rain
      driving the freshet" and does not bias the comparison.
    - Basin metric = simple unweighted mean across the three stations
      that have data for that year. Documented coverage in output JSON.

Output:
    data/climate-overlay/lac_coulonge_climate_overlay.json — paired
    annual records 1972-2026 (or last available year per station).

Stdlib only.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
PEAKS_CSV = ROOT / "data" / "lac-coulonge-monthly-1972-2026.csv"
ECCC_DIR = ROOT / "data" / "eccc-climate"
OUT_JSON = ROOT / "data" / "climate-overlay" / "lac_coulonge_climate_overlay.json"

# Upper-basin stations causally upstream of Lac Coulonge.
# All start ≥1972 and run continuously (per data/eccc-climate/manifest.csv).
STATIONS = [
    ("val-dor-a", "daily-1972-2025.csv"),
    ("parent", "daily-1972-2026.csv"),
    ("barrage-temiscamingue", "daily-1972-2026.csv"),
]


def load_peaks() -> dict[int, float]:
    out: dict[int, float] = {}
    with PEAKS_CSV.open() as f:
        for row in csv.DictReader(f):
            v = row.get("daily_max")
            if v and v.upper() != "NA":
                try:
                    out[int(row["year"])] = float(v)
                except ValueError:
                    continue
    return out


def load_station(slug: str, csv_name: str) -> list[dict]:
    """Returns a list of (year, month, day, snow_grnd_cm, rain_mm) dicts."""
    path = ECCC_DIR / slug / csv_name
    rows = []
    with path.open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            try:
                y = int(r["Year"])
                m = int(r["Month"])
                d = int(r["Day"])
            except (ValueError, KeyError, TypeError):
                continue
            sog_raw = (r.get("Snow on Grnd (cm)") or "").strip()
            # Use Total Precip (continuous 1972-present) rather than
            # Total Rain (discontinued at these stations in the late-1990s).
            # By April-May, precip ≈ rain at all upper-basin stations.
            precip_raw = (r.get("Total Precip (mm)") or "").strip()
            try:
                sog = float(sog_raw) if sog_raw else None
            except ValueError:
                sog = None
            try:
                precip = float(precip_raw) if precip_raw else None
            except ValueError:
                precip = None
            rows.append({
                "year": y, "month": m, "day": d,
                "sog_cm": sog, "precip_mm": precip,
            })
    return rows


def per_year_metrics(rows: list[dict]) -> dict[int, dict]:
    """For each year: peak snow-on-ground in Feb-Mar, sum of precip in Apr-May."""
    by_year: dict[int, dict] = {}
    for r in rows:
        by_year.setdefault(r["year"], {"sog_feb_mar": [], "precip_apr_may": []})
        if r["month"] in (2, 3) and r["sog_cm"] is not None:
            by_year[r["year"]]["sog_feb_mar"].append(r["sog_cm"])
        if r["month"] in (4, 5) and r["precip_mm"] is not None:
            by_year[r["year"]]["precip_apr_may"].append(r["precip_mm"])

    out = {}
    for y, d in by_year.items():
        peak_sog = max(d["sog_feb_mar"]) if d["sog_feb_mar"] else None
        spring_precip = sum(d["precip_apr_may"]) if d["precip_apr_may"] else None
        # Coverage thresholds — require ≥30 days observed in each window
        sog_n = len(d["sog_feb_mar"])
        precip_n = len(d["precip_apr_may"])
        out[y] = {
            "peak_sog_cm": peak_sog if sog_n >= 30 else None,
            "spring_precip_mm": spring_precip if precip_n >= 30 else None,
            "sog_n": sog_n,
            "precip_n": precip_n,
        }
    return out


def basin_average(per_station: dict[str, dict[int, dict]]) -> dict[int, dict]:
    """Average each year's metric across stations that have data for that year."""
    all_years = sorted({y for s in per_station.values() for y in s.keys()})
    out = {}
    for y in all_years:
        sog_vals = []
        rain_vals = []
        sog_stations = []
        precip_stations = []
        for slug, by_year in per_station.items():
            if y not in by_year:
                continue
            if by_year[y]["peak_sog_cm"] is not None:
                sog_vals.append(by_year[y]["peak_sog_cm"])
                sog_stations.append(slug)
            if by_year[y]["spring_precip_mm"] is not None:
                rain_vals.append(by_year[y]["spring_precip_mm"])
                precip_stations.append(slug)
        out[y] = {
            "peak_sog_cm": round(mean(sog_vals), 1) if sog_vals else None,
            "spring_precip_mm": round(mean(rain_vals), 1) if rain_vals else None,
            "sog_stations": sog_stations,
            "precip_stations": precip_stations,
        }
    return out


def main():
    peaks = load_peaks()
    print(f"Loaded {len(peaks)} Lac Coulonge yearly peaks ({min(peaks)}-{max(peaks)})")

    per_station = {}
    for slug, csv_name in STATIONS:
        rows = load_station(slug, csv_name)
        per_station[slug] = per_year_metrics(rows)
        years_with_data = sum(1 for d in per_station[slug].values()
                              if d["peak_sog_cm"] is not None
                              or d["spring_precip_mm"] is not None)
        print(f"  {slug}: {years_with_data} years with usable data")

    basin = basin_average(per_station)

    # Combine: every year that has BOTH a Lac Coulonge peak and at least
    # one climate metric.
    records = []
    for y in sorted(basin.keys()):
        if y not in peaks:
            continue
        b = basin[y]
        records.append({
            "year": y,
            "lac_coulonge_peak_m": peaks[y],
            "peak_sog_cm": b["peak_sog_cm"],
            "spring_precip_mm": b["spring_precip_mm"],
            "sog_n_stations": len(b["sog_stations"]),
            "precip_n_stations": len(b["precip_stations"]),
        })

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w") as f:
        json.dump({
            "schema_version": 1,
            "stations": [s for s, _ in STATIONS],
            "snowpack_window": "Feb-Mar (peak Snow-on-Ground)",
            "rain_window": "Apr-May (sum of Total Rain)",
            "records": records,
        }, f, indent=2)
    print(f"Wrote {len(records)} paired records to {OUT_JSON}")

    # Print summary by era
    print("\n=== Era comparison ===")
    for label, lo, hi in (("Pre-2017 (1972-2016)", 1972, 2016),
                          ("Post-2017 (2017-2026)", 2017, 2026)):
        rs = [r for r in records if lo <= r["year"] <= hi]
        peaks_m = [r["lac_coulonge_peak_m"] for r in rs]
        sog = [r["peak_sog_cm"] for r in rs if r["peak_sog_cm"] is not None]
        precip = [r["spring_precip_mm"] for r in rs if r["spring_precip_mm"] is not None]
        print(f"{label}:  n={len(rs)}")
        print(f"  Lac Coulonge peak (m):   mean={mean(peaks_m):.2f}  max={max(peaks_m):.2f}")
        if sog:
            print(f"  Peak snowpack (cm):      mean={mean(sog):.1f}   max={max(sog):.1f}   n_yrs={len(sog)}")
        if precip:
            print(f"  Spring precip (mm):      mean={mean(precip):.1f}   max={max(precip):.1f}   n_yrs={len(precip)}")

    # Print top-5 super-flood years for inspection
    print("\n=== Lac Coulonge super-flood years (peak ≥ 108.5 m) ===")
    sf = sorted([r for r in records if r["lac_coulonge_peak_m"] >= 108.5],
                key=lambda r: -r["lac_coulonge_peak_m"])
    for r in sf:
        print(f"  {r['year']}: peak {r['lac_coulonge_peak_m']:.2f} m  "
              f"snowpack {r['peak_sog_cm']} cm  precip {r['spring_precip_mm']} mm")


if __name__ == "__main__":
    main()
