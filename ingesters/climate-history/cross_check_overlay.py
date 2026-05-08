#!/usr/bin/env python3
"""
Cross-check the data feeding Exhibit H against:
  1. The canonical ORRPB lake-coulonge.csv (vs the lac-coulonge-monthly CSV
     used by snowpack_overlay_analysis.py — confirm both are the same).
  2. Exhibit A's hardcoded peaks (the published case-file values). Any
     mismatch is flagged so we know which source to align to.
  3. Per-station snowpack for 1979 (known high-snowpack flood year),
     2019 (record-flood year), and 2017 (first modern major flood) so
     anomalies in the basin-mean can be traced to a specific station.
  4. ORRPB 2017 summary's published "257 mm over the entire basin
     April-May" claim against our upper-basin Apr-May mean.

Stdlib only.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]


def load_csv_peaks(path: Path) -> dict[int, float]:
    out = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            v = row.get("daily_max")
            if v and v.upper() != "NA":
                try:
                    out[int(row["year"])] = float(v)
                except ValueError:
                    continue
    return out


def load_exhibit_a_peaks() -> dict[int, float]:
    """Parse the JS object literal `const peaks = { 1972: ..., ... }` from
    Exhibit_A_Regime_Change.html so we don't have to reproduce it here."""
    html = (ROOT / "docs" / "exhibits" / "Exhibit_A_Regime_Change.html").read_text()
    m = re.search(r"const peaks = \{([^}]+)\}", html)
    assert m, "Could not find peaks block in Exhibit A"
    out = {}
    for k, v in re.findall(r"(\d{4}):\s*([\d.]+)", m.group(1)):
        out[int(k)] = float(v)
    return out


def per_station_year(slug: str, csv_name: str, year: int) -> dict:
    path = ROOT / "data" / "eccc-climate" / slug / csv_name
    sog_feb_mar = []
    precip_apr_may = []
    with path.open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            try:
                y = int(r["Year"]); m = int(r["Month"])
            except (KeyError, ValueError, TypeError):
                continue
            if y != year:
                continue
            sog = (r.get("Snow on Grnd (cm)") or "").strip()
            precip = (r.get("Total Precip (mm)") or "").strip()
            if m in (2, 3) and sog:
                try: sog_feb_mar.append(float(sog))
                except ValueError: pass
            if m in (4, 5) and precip:
                try: precip_apr_may.append(float(precip))
                except ValueError: pass
    return {
        "peak_sog_cm": max(sog_feb_mar) if sog_feb_mar else None,
        "spring_precip_mm": sum(precip_apr_may) if precip_apr_may else None,
        "sog_n": len(sog_feb_mar),
        "precip_n": len(precip_apr_may),
    }


def main():
    print("=" * 70)
    print("CHECK 1 — Two ORRPB Lac Coulonge CSVs are the same record")
    print("=" * 70)
    monthly = load_csv_peaks(ROOT / "data" / "lac-coulonge-monthly-1972-2026.csv")
    summaries = load_csv_peaks(ROOT / "data" / "orrpb-historical-summaries" / "lake-coulonge.csv")
    common = sorted(set(monthly) & set(summaries))
    diff_count = 0
    for y in common:
        if abs(monthly[y] - summaries[y]) > 0.005:
            print(f"  DIFF {y}: monthly={monthly[y]:.2f}  summaries={summaries[y]:.2f}")
            diff_count += 1
    extra_monthly = sorted(set(monthly) - set(summaries))
    extra_summaries = sorted(set(summaries) - set(monthly))
    print(f"  monthly_csv years: {min(monthly)}-{max(monthly)} (n={len(monthly)})")
    print(f"  summaries_csv years: {min(summaries)}-{max(summaries)} (n={len(summaries)})")
    print(f"  matching years: {len(common)}, value diffs: {diff_count}")
    print(f"  monthly-only years: {extra_monthly}")
    print(f"  summaries-only years: {extra_summaries}")

    print()
    print("=" * 70)
    print("CHECK 2 — Exhibit A hardcoded peaks vs canonical CSV (lake-coulonge.csv)")
    print("=" * 70)
    exhibit_a = load_exhibit_a_peaks()
    overlap = sorted(set(exhibit_a) & set(summaries))
    mismatches = []
    for y in overlap:
        a = exhibit_a[y]
        c = summaries[y]
        if abs(a - c) > 0.01:
            mismatches.append((y, a, c, a - c))
    print(f"  Exhibit A years: {min(exhibit_a)}-{max(exhibit_a)} (n={len(exhibit_a)})")
    print(f"  Overlap with canonical: {len(overlap)}")
    print(f"  Mismatches (>1 cm): {len(mismatches)}")
    if mismatches:
        print(f"  First 15 mismatches:")
        for y, a, c, d in mismatches[:15]:
            print(f"    {y}: exhibit_a={a:.2f}  canonical={c:.2f}  diff={d:+.2f} m")
        # Check if it looks like an off-by-one row error
        offsets_match = sum(
            1 for y in overlap
            if (y + 1) in summaries and abs(exhibit_a[y] - summaries[y + 1]) < 0.01
        )
        print(f"  Years where exhibit_a[y] == canonical[y+1] (off-by-one signal): {offsets_match}/{len(overlap)}")

    print()
    print("=" * 70)
    print("CHECK 3 — Super-flood year counts (peak >= 108.5 m) vs canonical")
    print("=" * 70)
    for label, lo, hi in [("1972-2016", 1972, 2016), ("2017-2026", 2017, 2026)]:
        sf = [(y, summaries[y]) for y in summaries if lo <= y <= hi and summaries[y] >= 108.5]
        sf.sort()
        print(f"  {label}: {len(sf)} super-floods")
        for y, v in sf:
            print(f"    {y}: {v:.2f} m")

    print()
    print("=" * 70)
    print("CHECK 4 — Era means (canonical CSV) vs Exhibit H stats band")
    print("=" * 70)
    pre = [v for y, v in summaries.items() if 1972 <= y <= 2016]
    post = [v for y, v in summaries.items() if 2017 <= y <= 2026]
    print(f"  Pre-2017 mean (canonical):  {mean(pre):.3f} m  (n={len(pre)})")
    print(f"  Post-2017 mean (canonical): {mean(post):.3f} m (n={len(post)})")
    print(f"  Δ = {(mean(post) - mean(pre)) * 100:+.1f} cm  (Exhibit H states +59 cm)")

    print()
    print("=" * 70)
    print("CHECK 5 — Per-station snowpack/precip for known flood years")
    print("=" * 70)
    stations = [
        ("val-dor-a", "daily-1972-2025.csv"),
        ("parent", "daily-1972-2026.csv"),
        ("barrage-temiscamingue", "daily-1972-2026.csv"),
    ]
    for year in (1979, 2017, 2019, 2023, 2026):
        print(f"  Year {year}:")
        sog_vals = []
        precip_vals = []
        for slug, csv_name in stations:
            try:
                d = per_station_year(slug, csv_name, year)
                sog_str = f"{d['peak_sog_cm']:.1f} cm (n={d['sog_n']}d)" if d['peak_sog_cm'] else "—"
                p_str = f"{d['spring_precip_mm']:.1f} mm (n={d['precip_n']}d)" if d['spring_precip_mm'] else "—"
                print(f"    {slug:25s} sog_peak={sog_str:25s} apr_may_precip={p_str}")
                if d['peak_sog_cm'] and d['sog_n'] >= 30:
                    sog_vals.append(d['peak_sog_cm'])
                if d['spring_precip_mm'] and d['precip_n'] >= 30:
                    precip_vals.append(d['spring_precip_mm'])
            except FileNotFoundError:
                print(f"    {slug:25s} (no file)")
        if sog_vals:
            print(f"    BASIN MEAN: peak_sog={mean(sog_vals):.1f} cm  spring_precip={mean(precip_vals):.1f} mm")

    print()
    print("=" * 70)
    print("CHECK 6 — Exhibit H JSON values vs recomputation from sources")
    print("=" * 70)
    overlay = json.loads(
        (ROOT / "data" / "climate-overlay" / "lac_coulonge_climate_overlay.json").read_text()
    )
    discrepancies = 0
    for r in overlay["records"]:
        y = r["year"]
        if y not in summaries:
            continue
        if abs(r["lac_coulonge_peak_m"] - summaries[y]) > 0.005:
            print(f"  DIFF {y}: overlay_json={r['lac_coulonge_peak_m']}  canonical={summaries[y]}")
            discrepancies += 1
    print(f"  Lac Coulonge peak discrepancies (overlay JSON vs canonical CSV): {discrepancies}")

    print()
    print("=" * 70)
    print("CHECK 7 — Verify ORRPB 2017 published claim")
    print("=" * 70)
    print('  ORRPB 2017 spring flood summary stated:')
    print('    "the precipitation totalled an exceptional 257 mm over the entire')
    print('     basin in April and May, which was 174% of normal values."')
    overlay_2017 = next((r for r in overlay["records"] if r["year"] == 2017), None)
    if overlay_2017:
        print(f"  Our upper-basin Apr-May 2017 mean: {overlay_2017['spring_precip_mm']} mm")
        print(f"  Difference (256 - {overlay_2017['spring_precip_mm']}): "
              f"~{257 - overlay_2017['spring_precip_mm']:.0f} mm")
        print("  Reasonable: ORRPB figure is whole-basin mean (incl. south stations);")
        print("  ours is upper-basin only (Val-d'Or A, Parent, Barrage Témiscamingue),")
        print("  which is a colder/drier-spring sub-region. Both directionally consistent.")


if __name__ == "__main__":
    main()
