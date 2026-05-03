#!/usr/bin/env python3
"""
One-shot loader: pushes the daily.csv files produced by wsc_hydat_extract.py
into the wsc_daily hypertable via PostgREST.

Reads data/wsc-hydrometric/manifest.csv to find each station's CSV and
station_number. Posts in batches with `Prefer: resolution=ignore-duplicates`
so re-runs are idempotent.

Usage:
    POSTGREST_URL=http://localhost:30300 python3 wsc_hydat_load.py
    POSTGREST_URL=http://localhost:30300 python3 wsc_hydat_load.py --only 02OA105,02OA039

Stdlib only.
"""

from __future__ import annotations
import argparse, csv, json, os, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "wsc-hydrometric"
MANIFEST = DATA / "manifest.csv"
POSTGREST = os.environ.get("POSTGREST_URL", "http://postgrest.data.svc.cluster.local:3000")
BATCH = int(os.environ.get("WSC_LOAD_BATCH", "5000"))


def post_batch(rows: list[dict]) -> None:
    body = json.dumps(rows, separators=(",", ":")).encode("utf-8")
    req = urllib.request.Request(
        f"{POSTGREST}/wsc_daily",
        data=body, method="POST",
        headers={
            "Content-Type": "application/json",
            "Prefer": "resolution=ignore-duplicates",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        if r.status not in (200, 201, 204):
            raise RuntimeError(f"POST failed: HTTP {r.status}")


def load_station(station_code: str, csv_path: Path) -> int:
    n_total = 0
    batch: list[dict] = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            level = row.get("level_m", "").strip()
            flow = row.get("flow_cms", "").strip()
            if not level and not flow:
                continue
            batch.append({
                "time": f"{row['date']}T00:00:00Z",
                "station_code": station_code,
                "level_m": float(level) if level else None,
                "flow_cms": float(flow) if flow else None,
                "level_symbol": row.get("level_symbol") or None,
                "flow_symbol": row.get("flow_symbol") or None,
            })
            if len(batch) >= BATCH:
                post_batch(batch)
                n_total += len(batch)
                batch = []
    if batch:
        post_batch(batch)
        n_total += len(batch)
    return n_total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated station numbers to load (default: all in manifest)")
    args = ap.parse_args()

    if not MANIFEST.exists():
        sys.exit(f"manifest missing: {MANIFEST} (run wsc_hydat_extract.py first)")
    only = set(s.strip() for s in args.only.split(",")) if args.only else None

    with MANIFEST.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    print(f"PostgREST: {POSTGREST}")
    grand = 0
    for r in rows:
        stn = r["station_number"]
        if only and stn not in only:
            continue
        csv_path = DATA / r["consolidated_csv"]
        if not csv_path.exists():
            print(f"  skip {stn}: {csv_path} not found")
            continue
        print(f"  loading {stn} ({r['name']}) from {csv_path.relative_to(ROOT)}…", flush=True)
        n = load_station(stn, csv_path)
        grand += n
        print(f"    -> {n} rows posted")
    print(f"done: {grand} rows total")


if __name__ == "__main__":
    main()
