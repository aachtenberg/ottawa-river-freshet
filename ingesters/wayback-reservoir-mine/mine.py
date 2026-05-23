"""One-shot Wayback Machine miner for ORRPB reservoir history.

ORRPB's live `/conditions/?display=reservoir` page exposes only a rolling
8-day window of reservoir levels; their historical-summaries hub publishes
monthly means for river gauges but NOT for reservoirs; the historical
reservoir record is gated behind the Ottawa River Regulation Secretariat.

The Internet Archive's Wayback Machine has captured the conditions page
multiple times per month since approximately April 2020. Each snapshot
contains the same 8-day reservoir table the live page shows — so by
fetching one snapshot per month (or as many as needed to cover the
pre-freshet window) we can reconstruct daily reservoir levels for
2020 onwards.

Limitations:
  - Wayback coverage starts April 2020 — no snapshots are available for
    2017, 2018, 2019 (the high-freshet years that motivate the question).
  - Coverage density is 1-6 snapshots per month; some months have gaps.
  - Each snapshot's 8-day window is the time AROUND the snapshot date,
    not strictly before, so the effective record is slightly broader
    than the snapshot dates alone.

Stdlib-only. Reuses parsing logic from the live reservoir scraper:
`k3s/base/data/files/reservoir-ingest/scrape.py`.
"""
from __future__ import annotations
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# Reuse the live scraper's table parser (path-resolve to the k3s tree).
REPO_ROOT = Path(__file__).resolve().parents[3]
LIVE_SCRAPER_DIR = REPO_ROOT / "k3s" / "base" / "data" / "files" / "reservoir-ingest"
sys.path.insert(0, str(LIVE_SCRAPER_DIR))
from scrape import TableExtractor, find_reservoir_table, parse_table  # noqa: E402

WAYBACK_CDX = "https://web.archive.org/cdx/search/cdx"
WAYBACK_SNAP = "https://web.archive.org/web/{ts}id_/{url}"
TARGET_URL = "ottawariver.ca/conditions/?display=reservoir"

USER_AGENT = (
    "freshet/1.0 (+https://github.com/aachtenberg/ottawa-river-freshet; "
    "Wayback miner for ORRPB reservoir history)"
)
SLEEP_BETWEEN_FETCHES = 1.0  # be polite to web.archive.org

OUTDIR = REPO_ROOT / "freshet-public" / "data" / "wayback-orrpb-reservoirs"
RAW_DIR = OUTDIR / "raw"                 # cached snapshot HTML — checked in
CDX_CACHE = OUTDIR / "cdx_index.json"    # cached CDX listing — checked in


def cdx_query(url: str, year_from: int, year_to: int) -> list[tuple[str, str]]:
    """Return (timestamp, original_url) pairs for all 200-status snapshots.

    Cached to CDX_CACHE on first call so we don't re-query the CDX server
    on every run. Delete cdx_index.json to force a refresh."""
    if CDX_CACHE.exists():
        with open(CDX_CACHE) as f:
            cached = json.load(f)
        if cached.get("url") == url and cached.get("from") == year_from \
                and cached.get("to") == year_to:
            return [(p[0], p[1]) for p in cached["pairs"]]

    params = {
        "url": url,
        "output": "json",
        "from": f"{year_from}0101",
        "to": f"{year_to}1231",
        "filter": "statuscode:200",
        "matchType": "exact",
        "limit": "500",
    }
    qs = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{WAYBACK_CDX}?{qs}",
                                 headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
    pairs = [(row[1], row[2]) for row in data[1:]]
    CDX_CACHE.parent.mkdir(parents=True, exist_ok=True)
    with open(CDX_CACHE, "w") as f:
        json.dump({"url": url, "from": year_from, "to": year_to,
                   "pairs": pairs, "fetched_ts": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                                                time.gmtime())},
                  f, indent=2)
    return pairs


def fetch_snapshot(ts: str, original_url: str) -> tuple[str, bool]:
    """Return (html, from_cache_bool). HTML is also written to disk on miss
    so future runs are free."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = RAW_DIR / f"{ts}.html"
    if cache_path.exists() and cache_path.stat().st_size > 0:
        return cache_path.read_text(encoding="utf-8", errors="replace"), True
    snap_url = WAYBACK_SNAP.format(ts=ts, url=original_url)
    req = urllib.request.Request(snap_url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", errors="replace")
    cache_path.write_text(html, encoding="utf-8")
    return html, False


def parse_snapshot(html: str):
    p = TableExtractor()
    p.feed(html)
    tbl = find_reservoir_table(p.tables)
    if tbl is None:
        return []
    return parse_table(tbl)


def select_pre_freshet_snapshots(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Keep ALL snapshots in the pre-freshet / spring window each year
    (Jan-Jun), plus one per month outside that window for context.

    Pre-freshet density matters for the question being asked; the rest
    of the year just needs sketch coverage."""
    in_window: list[tuple[str, str]] = []
    out_window_by_month: dict[str, tuple[str, str]] = {}
    for ts, url in pairs:
        month = int(ts[4:6])
        if 1 <= month <= 6:
            in_window.append((ts, url))
        else:
            ym = ts[:6]
            if ym not in out_window_by_month or ts < out_window_by_month[ym][0]:
                out_window_by_month[ym] = (ts, url)
    out = sorted(set(in_window) | set(out_window_by_month.values()))
    return out


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Querying Wayback CDX for snapshots of {TARGET_URL} (2018-2025)…")
    pairs = cdx_query(TARGET_URL, 2018, 2025)
    print(f"  found {len(pairs)} total snapshots in CDX")
    pairs = select_pre_freshet_snapshots(pairs)
    print(f"  keeping {len(pairs)} snapshots (all Jan-Jun + 1/mo Jul-Dec)")
    print(f"  date range: {pairs[0][0][:8] if pairs else 'n/a'} → "
          f"{pairs[-1][0][:8] if pairs else 'n/a'}")

    cached_n = sum(1 for ts, _ in pairs if (RAW_DIR / f"{ts}.html").exists())
    print(f"  already cached on disk: {cached_n} / {len(pairs)}")

    all_rows: list[dict] = []
    failed: list[tuple[str, str, str]] = []
    for i, (ts, url) in enumerate(pairs, 1):
        try:
            html, from_cache = fetch_snapshot(ts, url)
            rows = parse_snapshot(html)
        except Exception as e:
            failed.append((ts, url, str(e)))
            print(f"  [{i}/{len(pairs)}] {ts}  ERR: {e}", file=sys.stderr)
            continue
        for r in rows:
            r["source_snapshot"] = ts
        all_rows.extend(rows)
        tag = "[cache]" if from_cache else "[fetch]"
        print(f"  [{i}/{len(pairs)}] {ts} {tag} {len(rows)} rows "
              f"({len({r['reservoir_id'] for r in rows})} reservoirs)")
        if not from_cache:
            time.sleep(SLEEP_BETWEEN_FETCHES)

    # De-dup by (reservoir_id, date): a date can appear in multiple
    # snapshots (8-day windows overlap). Keep the snapshot whose timestamp
    # is *closest to but not after* the date — that one is freshest.
    by_key: dict[tuple[str, str], dict] = {}
    for r in all_rows:
        date = r["time"][:10]
        key = (r["reservoir_id"], date)
        existing = by_key.get(key)
        if existing is None:
            by_key[key] = r
            continue
        # Prefer the snapshot taken on or after the obs date, with the
        # smallest gap. If both are after, take the smaller; if one is
        # before and one is after, prefer the after.
        snap_ts = r["source_snapshot"][:8]
        existing_ts = existing["source_snapshot"][:8]
        snap_date_norm = date.replace("-", "")
        existing_after = existing_ts >= snap_date_norm
        new_after = snap_ts >= snap_date_norm
        if new_after and not existing_after:
            by_key[key] = r
        elif new_after and existing_after and snap_ts < existing_ts:
            by_key[key] = r
        elif (not new_after) and (not existing_after) and snap_ts > existing_ts:
            by_key[key] = r

    deduped = sorted(by_key.values(), key=lambda r: (r["time"], r["reservoir_id"]))
    out_csv = OUTDIR / "wayback_reservoir_levels.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "date", "reservoir_id", "level_m", "flow_cms", "agency", "source_snapshot"])
        w.writeheader()
        for r in deduped:
            w.writerow({
                "date": r["time"][:10],
                "reservoir_id": r["reservoir_id"],
                "level_m": r.get("level_m") or "",
                "flow_cms": r.get("flow_cms") or "",
                "agency": r.get("agency") or "",
                "source_snapshot": r["source_snapshot"],
            })
    print(f"\nWrote {len(deduped)} rows to {out_csv.relative_to(REPO_ROOT)}")
    if failed:
        print(f"  ({len(failed)} fetches failed)")

    # Summary report
    from collections import defaultdict
    by_res: dict[str, list[str]] = defaultdict(list)
    by_year_res: dict[tuple[str, str], list[str]] = defaultdict(list)
    for r in deduped:
        by_res[r["reservoir_id"]].append(r["time"][:10])
        by_year_res[(r["time"][:4], r["reservoir_id"])].append(r["time"][:10])
    print(f"\nCoverage by reservoir:")
    for rid in sorted(by_res):
        dates = sorted(by_res[rid])
        years = sorted({d[:4] for d in dates})
        print(f"  {rid:25s}  {len(dates):4d} obs  {dates[0]} → {dates[-1]}  "
              f"years: {','.join(years)}")

    print(f"\nApril-1 ± 7-day coverage by year (pre-freshet snapshot availability):")
    print(f"  {'year':6s}  {'reservoirs with Apr 1 ±7d':30s}  {'snapshots':30s}")
    for y in sorted({d[:4] for r in deduped for d in [r["time"][:10]]}):
        from datetime import date as D
        target = D(int(y), 4, 1)
        hits = set()
        for r in deduped:
            obs = D.fromisoformat(r["time"][:10])
            if abs((obs - target).days) <= 7:
                hits.add(r["reservoir_id"])
        print(f"  {y}    {len(hits):4d} of 14")


if __name__ == "__main__":
    main()
