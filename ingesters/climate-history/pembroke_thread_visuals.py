#!/usr/bin/env python3
"""Two synthesis visualizations for the May-2026 Pembroke FB thread.

1. five_variables_one_signal.png — funnel/elimination infographic.
   Five proposed variables; four eliminated with the statistic that
   killed them; one survives.

2. 2023_vs_2026_isolation.png — four-bar proof that the three
   observable knobs were held the same between 2023 and 2026, while
   the Pembroke shape moved 3x. Isolates the one unobserved knob
   (DJ outflow scheduling) as the only remaining lever.

Outputs:
  data/community-notes/2026-05-23_five_variables_one_signal.png
  data/community-notes/2026-05-23_2023_vs_2026_isolation.png
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[2]
OUTDIR = ROOT / "data" / "community-notes"
STAMP = "2026-05-23"

RED = "#cc3a21"
BLUE = "#2c6aa0"
GREEN = "#0b804b"
GREY = "#999999"
LIGHT = "#efefef"
DARK = "#222222"


def five_variables_one_signal():
    fig, ax = plt.subplots(figsize=(13, 9))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    fig.suptitle(
        "Pembroke peak — five proposed causes, one survives the data",
        fontsize=16, fontweight="bold", y=0.97)
    ax.text(50, 92,
            "May 2026 Facebook thread participants pointed at five different variables.\n"
            "Four come back null on public data. One survives — and the public record\n"
            "cannot measure it directly because the instrument was decommissioned in 1993.",
            ha="center", va="top", fontsize=10, color=DARK)

    # Five variables on the left, target on the right
    variables = [
        ("Total spring volume\npast Des Joachims",
         "chart author",
         "NULL — proxy for Q_pk\nmarginal R² = +0.01 pp",
         False),
        ("Lumped 90-day V\nas summary statistic",
         "Steve Deon",
         "NULL — same regression\nhides the timing variable",
         False),
        ("Pre-freshet reservoir\nstate (winter drawdown)",
         "Marie Bosco Burwell\nSteve LeGault",
         "NULL — 30-yr regression\nr ≈ 0, p ≈ 1",
         False),
        ("Instantaneous flow,\nnot cumulative",
         "timing-pushback commenter",
         "CONFIRMED — Q_pk alone\nexplains 99.7 % of variance",
         "partial"),
        ("Peak-time outflow\nshape at Des Joachims",
         "Dan Poole",
         "SIGNAL — 2023/2026 pair\nisolates this lever",
         True),
    ]

    y_positions = [78, 62, 46, 30, 14]
    box_x = 4
    box_w = 28
    box_h = 11

    for (var, who, result, survives), y in zip(variables, y_positions):
        if survives is True:
            edge, face, txt = GREEN, "#dff5e7", DARK
        elif survives == "partial":
            edge, face, txt = BLUE, "#e6eef7", DARK
        else:
            edge, face, txt = GREY, LIGHT, GREY

        # Variable box
        box = FancyBboxPatch((box_x, y - box_h/2), box_w, box_h,
                              boxstyle="round,pad=0.3", linewidth=1.8,
                              edgecolor=edge, facecolor=face, zorder=2)
        ax.add_patch(box)
        ax.text(box_x + box_w/2, y + 2.2, var,
                ha="center", va="center", fontsize=9.5,
                fontweight="bold", color=txt)
        ax.text(box_x + box_w/2, y - 3, who,
                ha="center", va="center", fontsize=8,
                style="italic", color=txt)

        # Arrow from variable -> target zone
        if survives is True:
            arrow_color = GREEN
            arrow_style = "-"
            lw = 2.5
        elif survives == "partial":
            arrow_color = BLUE
            arrow_style = "-"
            lw = 1.8
        else:
            arrow_color = GREY
            arrow_style = "-"
            lw = 1.2

        arrow = FancyArrowPatch(
            (box_x + box_w, y), (66, 50),
            arrowstyle="->", mutation_scale=18,
            color=arrow_color, linewidth=lw,
            linestyle=arrow_style, zorder=1, alpha=0.85)
        ax.add_patch(arrow)

        # Result label on the arrow midpoint
        mid_x = (box_x + box_w + 66) / 2
        mid_y = (y + 50) / 2
        ax.text(mid_x, mid_y + 1.5, result,
                ha="center", va="center", fontsize=8.5,
                color=edge, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3",
                          facecolor="white", edgecolor="none", alpha=0.9))

        # X-out for eliminated
        if survives is False:
            ax.plot([box_x + 2, box_x + box_w - 2],
                    [y - box_h/2 + 1.5, y + box_h/2 - 1.5],
                    color=RED, linewidth=2.5, zorder=3, alpha=0.7)
            ax.plot([box_x + 2, box_x + box_w - 2],
                    [y + box_h/2 - 1.5, y - box_h/2 + 1.5],
                    color=RED, linewidth=2.5, zorder=3, alpha=0.7)

    # Target / outcome box
    target = FancyBboxPatch((66, 38), 30, 24,
                             boxstyle="round,pad=0.5", linewidth=2.5,
                             edgecolor=DARK, facecolor="white", zorder=2)
    ax.add_patch(target)
    ax.text(81, 56, "PEMBROKE PEAK", ha="center", va="center",
            fontsize=13, fontweight="bold", color=DARK)
    ax.text(81, 51,
            "Why the post-2016\nhigh peaks?",
            ha="center", va="center", fontsize=10, color=DARK, style="italic")
    ax.text(81, 44.5,
            "Surviving lever:\npeak-time gate\nscheduling at\nDes Joachims",
            ha="center", va="center", fontsize=9,
            color=GREEN, fontweight="bold")

    # Footer: missing-instrument note
    footer_y = 4
    ax.text(50, footer_y,
            "The instrument that would have measured the surviving lever directly — "
            "the Westmeath flow gauge below Des Joachims —\n"
            "was decommissioned by OPG in 1993. A 2021 Westmeath council request to "
            "reinstall it was refused.",
            ha="center", va="center", fontsize=9, style="italic", color=DARK,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff8e1",
                      edgecolor="#cc9a00", linewidth=1.2))

    out = OUTDIR / f"{STAMP}_five_variables_one_signal.png"
    fig.savefig(out, dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out.relative_to(ROOT)}")


def isolation_2023_vs_2026():
    """Four panel grouped bars: three knobs identical, one moved 3x."""
    fig, axes = plt.subplots(1, 4, figsize=(14, 6.5))
    fig.suptitle(
        "2023 vs 2026 — three observable knobs held constant, one moved 3×",
        fontsize=15, fontweight="bold", y=0.99)
    fig.text(0.5, 0.93,
             "Same total water budget, same upstream pattern, same tributary rate — "
             "yet Pembroke rose 3× faster in 2023.\n"
             "The only remaining lever for the difference is Des Joachims outflow Q "
             "scheduling during the event (operator-internal).",
             ha="center", va="top", fontsize=10, color=DARK)

    panels = [
        ("Des Joachims\npeak outflow Q",  3324, 3324, "m³/s",  "SAME",   GREY),
        ("Des Joachims\nheadpond pattern", 150.6, 150.6, "m (plateau)", "SAME", GREY),
        ("Petawawa\nrate of rise",           44,   41, "m³/s/day", "≈ SAME (-7 %)", GREY),
        ("Pembroke\nrate of rise",        0.076, 0.026, "m/day",  "3× DIFFERENT",  RED),
    ]

    labels = ["2023", "2026"]
    colors = [RED, BLUE]

    for ax, (title, v23, v26, unit, verdict, verdict_color) in zip(axes, panels):
        bars = ax.bar(labels, [v23, v26], color=colors, edgecolor="black",
                      linewidth=1.2, width=0.55)
        for b, v in zip(bars, [v23, v26]):
            ax.text(b.get_x() + b.get_width()/2, b.get_height(),
                    f"{v:g}", ha="center", va="bottom",
                    fontsize=11, fontweight="bold")
        ax.set_title(title, fontsize=11, fontweight="bold")
        ax.set_ylabel(unit, fontsize=9)
        ax.set_ylim(0, max(v23, v26) * 1.25)
        ax.grid(axis="y", alpha=0.3)
        ax.tick_params(labelsize=10)

        ax.text(0.5, -0.18, verdict,
                transform=ax.transAxes,
                ha="center", va="center", fontsize=11, fontweight="bold",
                color=verdict_color,
                bbox=dict(boxstyle="round,pad=0.4",
                          facecolor="white" if verdict_color == GREY else "#fff0ee",
                          edgecolor=verdict_color, linewidth=1.5))

    # Bottom takeaway
    fig.text(0.5, 0.04,
             "Pembroke peaked 14 cm lower in 2026 (113.31 m → 113.17 m). "
             "Petawawa contributed +80 m³/s MORE in 2026, not less.\n"
             "Three of the four observable variables are the same. "
             "The fourth — Pembroke shape — is 3× different. "
             "The unobservable variable that closes the gap is gate operations at Des Joachims.",
             ha="center", va="bottom", fontsize=9.5, style="italic",
             color=DARK,
             bbox=dict(boxstyle="round,pad=0.5",
                       facecolor="#dff5e7", edgecolor=GREEN, linewidth=1.2))

    fig.tight_layout(rect=(0, 0.10, 1, 0.91))

    out = OUTDIR / f"{STAMP}_2023_vs_2026_isolation.png"
    fig.savefig(out, dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    OUTDIR.mkdir(parents=True, exist_ok=True)
    five_variables_one_signal()
    isolation_2023_vs_2026()
