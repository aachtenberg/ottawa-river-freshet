"""ORRPB per-location historical daily-level scraper.

Each ORRPB location page (https://ottawariver.ca/location/<slug>/) accepts a
POST with date-start / date-end / data-display=table that returns a daily
table with rows: Observed, Median, Historic High, Historic Low. The form
returns at most ~3 years (1095 days) per request, so we chunk.

This is the canonical replacement for the Wayback-mine for everything except
flow_cms (which appears on the conditions page but not on per-location
historical tables). The conditions-page miner stays for current outflow_cms.

Coverage probed:
  1990-2025 daily observed levels for all 13 ORRPB locations.
  Earlier years (1987-1989) return an operating-limits table without
  observed values — limit is somewhere in 1989/1990.

Output:
  data/orrpb-location-history/orrpb_location_daily.csv
    (date, reservoir_id, level_m, median_m, hist_high_m, hist_low_m,
     hist_high_year, hist_low_year)
  data/orrpb-location-history/raw/<slug>_<start>_<end>.html  (cached HTML)

Stdlib only.
"""
from __future__ import annotations
import csv
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
OUTDIR = REPO_ROOT / "freshet-public" / "data" / "orrpb-location-history"
RAW_DIR = OUTDIR / "raw"

USER_AGENT = (
    "freshet/1.0 (+https://github.com/aachtenberg/ottawa-river-freshet; "
    "ORRPB per-location historical archive)"
)
SLEEP_BETWEEN = 1.0

# Slugs match reservoir-limits.json keys (with underscores) but the URL uses
# hyphens. The 13 principal reservoirs in reservoir-limits.json:
LOCATIONS = [
    ("timiskaming",    "timiskaming"),
    ("kipawa",         "kipawa"),
    ("quinze",         "quinze"),
    ("rapide_7",       "rapide-7"),
    ("dozois",         "dozois"),
    ("lady_evelyn",    "lady-evelyn"),
    ("baskatong",      "baskatong"),
    ("cabonga",        "cabonga"),
    ("bark_lake",      "bark-lake"),
    ("mitchinamecus",  "mitchinamecus"),
    ("kiamika",        "kiamika"),
    ("poisson_blanc",  "poisson-blanc"),
    ("des_joachims",   "des-joachims"),
]

YEAR_START = 1990
YEAR_END = 2025
CHUNK_YEARS = 3  # max accepted by the form


def chunks(y0: int, y1: int, span: int):
    y = y0
    while y <= y1:
        end = min(y + span - 1, y1)
        yield y, end
        y = end + 1


def fetch_chunk(slug: str, y_from: int, y_to: int) -> str:
    cache = RAW_DIR / f"{slug}_{y_from}_{y_to}.html"
    if cache.exists() and cache.stat().st_size > 1000:
        return cache.read_text(encoding="utf-8", errors="replace")
    body = urllib.parse.urlencode({
        "data-type": "daily",
        "date-start": f"{y_from}-01-01",
        "date-end": f"{y_to}-12-31",
        "data-display": "table",
    }).encode("utf-8")
    req = urllib.request.Request(
        f"https://www.ottawariver.ca/location/{slug}/",
        data=body, method="POST",
        headers={"User-Agent": USER_AGENT,
                 "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", errors="replace")
    cache.write_text(html, encoding="utf-8")
    time.sleep(SLEEP_BETWEEN)
    return html


def parse_table(html: str) -> dict[str, dict]:
    """Return {date_str -> {level, median, hist_high, hist_low, hh_yr, hl_yr}}.

    Returns empty dict if no observed row present (older years).
    """
    m = re.search(r"<table[^>]*>(.*?)</table>", html, re.DOTALL)
    if not m:
        return {}
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(1), re.DOTALL)
    if not rows:
        return {}

    def cells(row):
        return [re.sub(r"<[^>]+>", "", c).strip()
                for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.DOTALL)]

    header = cells(rows[0])
    if not header or "date" not in header[0].lower():
        return {}
    dates = header[1:]

    by_label: dict[str, list[str]] = {}
    for r in rows[1:]:
        cs = cells(r)
        if not cs:
            continue
        label = re.sub(r"\s+", " ", cs[0]).strip().lower()
        by_label[label] = cs[1:]

    if "observed" not in by_label:
        return {}

    def parse_val_year(s: str) -> tuple[float | None, str]:
        # "178.79 (1997)" -> (178.79, "1997")
        s = re.sub(r"\s+", " ", s).strip()
        if not s or s == "-":
            return None, ""
        mm = re.match(r"^([\d.]+)\s*(?:\((\d{4})\))?", s)
        if not mm:
            return None, ""
        try:
            return float(mm.group(1)), mm.group(2) or ""
        except ValueError:
            return None, ""

    obs = by_label.get("observed", [])
    med = by_label.get("median", [])
    hh  = by_label.get("historic high", [])
    hl  = by_label.get("historic low", [])

    out: dict[str, dict] = {}
    for i, d in enumerate(dates):
        obs_v, _ = parse_val_year(obs[i]) if i < len(obs) else (None, "")
        med_v, _ = parse_val_year(med[i]) if i < len(med) else (None, "")
        hh_v, hh_y = parse_val_year(hh[i]) if i < len(hh) else (None, "")
        hl_v, hl_y = parse_val_year(hl[i]) if i < len(hl) else (None, "")
        if obs_v is None and med_v is None:
            continue
        out[d] = {"level_m": obs_v, "median_m": med_v,
                  "hist_high_m": hh_v, "hist_high_year": hh_y,
                  "hist_low_m": hl_v, "hist_low_year": hl_y}
    return out


def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    all_rows: list[dict] = []
    for res_id, slug in LOCATIONS:
        print(f"\n{res_id} ({slug})")
        res_count = 0
        for y0, y1 in chunks(YEAR_START, YEAR_END, CHUNK_YEARS):
            cache_path = RAW_DIR / f"{slug}_{y0}_{y1}.html"
            cached = cache_path.exists() and cache_path.stat().st_size > 1000
            try:
                html = fetch_chunk(slug, y0, y1)
            except Exception as e:
                print(f"  {y0}-{y1}: ERR {e}", file=sys.stderr)
                continue
            data = parse_table(html)
            tag = "[cache]" if cached else "[fetch]"
            print(f"  {y0}-{y1} {tag} {len(data)} obs")
            for d, vals in data.items():
                all_rows.append({"date": d, "reservoir_id": res_id, **vals})
            res_count += len(data)
        print(f"  total: {res_count}")

    out_csv = OUTDIR / "orrpb_location_daily.csv"
    fields = ["date", "reservoir_id", "level_m", "median_m",
              "hist_high_m", "hist_high_year", "hist_low_m", "hist_low_year"]
    all_rows.sort(key=lambda r: (r["date"], r["reservoir_id"]))
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({k: ("" if r.get(k) is None else r[k]) for k in fields})
    print(f"\nWrote {len(all_rows)} rows to {out_csv.relative_to(REPO_ROOT)}")

    # Coverage summary
    from collections import defaultdict
    by_res: dict[str, list[str]] = defaultdict(list)
    for r in all_rows:
        if r.get("level_m") is not None:
            by_res[r["reservoir_id"]].append(r["date"])
    print(f"\nObserved-level coverage:")
    for rid in sorted(by_res):
        ds = sorted(by_res[rid])
        years = sorted({d[:4] for d in ds})
        print(f"  {rid:25s}  {len(ds):5d} obs  {ds[0]} → {ds[-1]}  ({len(years)} yrs)")


if __name__ == "__main__":
    main()
