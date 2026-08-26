#!/usr/bin/env python3
"""Barrière diversion restart (August 2026) — figure for the community note.

Community claim (Ottawa River Flood Watch infographic, August 2026):
  * The Barrière diversion structure restarted on August 18, 2026
  * ~90 m³/s is being redirected from the Cabonga reservoir toward Dozois
  * Water that would normally reach the Gatineau is going to the Upper Ottawa

What this script plots, from primary sources:
  1. Hourly total release at Barrière (3-24) and Cabonga (3-62), Aug 11-21,
     straight from Hydro-Québec's open-data feed. The cluster's `dam_releases`
     ingest still carries zeros for Barrière through 2026-08-19T09:00Z, so the
     raw feed is the authoritative series for the opening hours.
  2. Barrière tailwater (station 1-2950) — the physical confirmation that the
     water actually left the structure.
  3. Downstream response: Dozois outflow vs Rapide-7 and Témiscaming, showing
     the pulse has not yet propagated past the first reservoir.

Output:
  data/community-notes/figures/2026-08-21_barriere_diversion_restart.png
"""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

ROOT = Path(__file__).resolve().parents[2]
OUTDIR = ROOT / "data" / "community-notes" / "figures"
STAMP = "2026-08-21"

HQ_FEED = ("https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/"
           "json/Donnees_VUE_CENTRALES_ET_OUVRAGES.json")
PG = "https://freshet.xgrunt.com/history/"
UA = "freshet/1.0 (+https://github.com/aachtenberg/ottawa-river-freshet)"

EDT = timezone(timedelta(hours=-4))
OPEN_UTC = datetime(2026, 8, 18, 17, 0, tzinfo=timezone.utc)  # gate opens
CUT_UTC = datetime(2026, 8, 18, 14, 0, tzinfo=timezone.utc)   # Cabonga closes

GREEN = "#0b804b"
BLUE = "#2c6aa0"
RED = "#cc3a21"
GREY = "#8a8a8a"
DARK = "#222222"


def _get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def hq_hourly(site_id: str) -> tuple[list, list]:
    """Hourly total release (m³/s) for one HQ site, from the raw open-data feed."""
    site = next(s for s in _get(HQ_FEED)["Site"] if s.get("identifiant") == site_id)
    series = {}
    for comp in site.get("Composition", []):
        if "total" in comp.get("type_point_donnee", ""):
            series = comp.get("Donnees", {})
            break
    keys = sorted(series)
    times = [datetime.strptime(k, "%Y/%m/%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
             for k in keys]
    return times, [float(series[k] or 0) for k in keys]


def pg_series(query: str, tcol: str, vcol: str) -> tuple[list, list]:
    rows = _get(PG + query)
    times = [datetime.fromisoformat(r[tcol]) for r in rows]
    return times, [None if r[vcol] is None else float(r[vcol]) for r in rows]


def main() -> None:
    bt, bv = hq_hourly("3-24")
    ct, cv = hq_hourly("3-62")

    lt, lv = pg_series(
        "dam_levels?station_id=eq.1-2950&time=gte.2026-08-11&order=time.asc"
        "&select=time,level_m", "time", "level_m")

    doz_t, doz_v = pg_series(
        "reservoir_readings?reservoir_id=eq.dozois&time=gte.2026-08-02"
        "&order=time.asc&select=time,flow_cms", "time", "flow_cms")
    r7_t, r7_v = pg_series(
        "reservoir_readings?reservoir_id=eq.rapide_7&time=gte.2026-08-02"
        "&order=time.asc&select=time,flow_cms", "time", "flow_cms")
    tem_t, tem_v = pg_series(
        "orrpb_river_flows?station=eq.temiscaming&time=gte.2026-08-02"
        "&order=time.asc&select=time,flow_cms", "time", "flow_cms")

    fig, (ax1, ax2, ax3) = plt.subplots(
        3, 1, figsize=(13, 12), gridspec_kw={"height_ratios": [3, 2, 2.4]})

    # --- 1. the switch ------------------------------------------------------
    ax1.plot(bt, bv, color=GREEN, linewidth=2.4, label="Barrière (3-24): to Dozois / Upper Ottawa")
    ax1.plot(ct, cv, color=BLUE, linewidth=2.4, label="Cabonga (3-62): to the Gatineau")
    ax1.fill_between(bt, 0, bv, color=GREEN, alpha=0.15)
    ax1.axvline(OPEN_UTC, color=RED, linestyle="--", linewidth=1.5, alpha=0.8)
    ax1.annotate("Aug 18, 13:00 EDT\nBarrière opens (0 → 92 m³/s in 2 h)",
                 xy=(OPEN_UTC, 92), xytext=(bt[0] + timedelta(hours=96), 66),
                 fontsize=10, fontweight="bold", color=RED,
                 arrowprops=dict(arrowstyle="->", color=RED, alpha=0.8))
    ax1.annotate("Cabonga cut 40 → 7 m³/s\nstarting 10:00 EDT, same day",
                 xy=(CUT_UTC, 40), xytext=(bt[0] + timedelta(hours=60), 20),
                 fontsize=10, fontweight="bold", color=BLUE,
                 arrowprops=dict(arrowstyle="->", color=BLUE, alpha=0.8))
    ax1.set_ylabel("total release (m³/s)", fontsize=11)
    ax1.set_title("Barrière diversion restart: hourly release, Hydro-Québec open data",
                  fontsize=14, fontweight="bold")
    ax1.set_ylim(0, 105)
    ax1.legend(loc="center left", fontsize=10)
    ax1.grid(alpha=0.25)

    # --- 2. tailwater confirmation -----------------------------------------
    ax2.plot(lt, lv, color=DARK, linewidth=2.2)
    ax2.axvline(OPEN_UTC, color=RED, linestyle="--", linewidth=1.5, alpha=0.8)
    if lv:
        base = next(v for t, v in zip(lt, lv) if t >= OPEN_UTC)
        rise = (lv[-1] - base) * 100
        ax2.text(lt[0] + timedelta(hours=12), lv[-1] - 0.02,
                 f"flat for a week, then +{rise:.0f} cm in the {len(lt) - lt.index(next(t for t in lt if t >= OPEN_UTC))} h\n"
                 "since the gate opened, still rising",
                 fontsize=11, fontweight="bold", color=DARK, va="top")
    ax2.set_ylabel("level (m)", fontsize=11)
    ax2.set_title("Barrière tailwater (station 1-2950): the water really left the structure",
                  fontsize=12, fontweight="bold")
    ax2.grid(alpha=0.25)

    # --- 3. downstream ------------------------------------------------------
    ax3.plot(doz_t, doz_v, color=GREEN, linewidth=2.2, marker="o", markersize=4,
             label="Dozois outflow (first reservoir below Barrière)")
    ax3.plot(r7_t, r7_v, color=BLUE, linewidth=2.2, marker="o", markersize=4,
             label="Rapide-7 outflow (next station down)")
    ax3.plot(tem_t, tem_v, color=GREY, linewidth=2.2, marker="o", markersize=4,
             label="Témiscaming outflow (upper-basin exit)")
    ax3.axvline(OPEN_UTC, color=RED, linestyle="--", linewidth=1.5, alpha=0.8)
    ax3.set_ylabel("daily flow (m³/s)", fontsize=11)
    ax3.set_xlabel("date (UTC)", fontsize=11)
    ax3.set_title("Downstream response: only Dozois has moved so far (+29 m³/s), "
                  "Rapide-7 and Témiscaming flat", fontsize=12, fontweight="bold")
    ax3.legend(loc="center left", fontsize=10)
    ax3.grid(alpha=0.25)

    for ax in (ax1, ax2, ax3):
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))

    fig.text(0.01, 0.005,
             "Sources: Hydro-Québec open data (hourly release, sites 3-24 / 3-62); "
             "cluster PostgREST dam_levels 1-2950, reservoir_readings (dozois, rapide_7), "
             "orrpb_river_flows (temiscaming). Compiled " + STAMP + ".",
             fontsize=8, color=GREY)

    plt.tight_layout(rect=(0, 0.015, 1, 1))
    OUTDIR.mkdir(parents=True, exist_ok=True)
    out = OUTDIR / f"{STAMP}_barriere_diversion_restart.png"
    plt.savefig(out, dpi=140)
    plt.close()
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
