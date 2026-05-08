# Exhibit A — data correction v3 → v4

**Provenance:** Logged 2026-05-08 alongside the version bump that aligned Exhibit A's hardcoded `peaks` block with the canonical ORRPB Lac Coulonge dataset. Discovered while building Exhibit H (climate forcing overlay) and writing the cross-check script `ingesters/climate-history/cross_check_overlay.py`. This document records what changed, why, and what did not change.

## Why this is on file

The case file's credibility model is *anyone can verify the data*. When a published exhibit's bar values diverge from the canonical dataset that underlies the rest of the case file, even by small amounts, that's an integrity problem — a careful reader cross-checking individual years would find the divergence and could reasonably question the whole exhibit. Recording the correction here serves three purposes:

1. **Public record of the v3 → v4 change**, so anyone who saved or shared the v1–v3 PNG / referenced its specific numbers can find the canonical values.
2. **Provenance clarity** — both the v1–v3 hardcoded data and the v4 canonical data trace back to ORRPB historical summaries; the difference is the *path* by which they were extracted, not the underlying source.
3. **Pattern documentation** alongside the integrity records for the [altered version in circulation](exhibit_a_altered_version_in_circulation.md) and the three popular-narrative refutations. The case file's integrity log should record both external alterations and self-corrections.

This is a **self-correction record** — establishing what the case file got wrong, fixed, and why the fix doesn't change the load-bearing claims.

## Provenance of the two datasets

Both v1–v3 (incorrect) and v4 (canonical) values are derived from ORRPB historical summaries published at https://www.ottawariver.ca/information/historical-data-summaries-water-levels-and-flows/. The difference is the extraction method:

- **v1–v3 hardcoded data** was extracted manually — likely by transcribing or copy-pasting from the ORRPB UI in early case-file work, before the programmatic scraper was written. Subject to transcription errors, browser-snapshot drift, and the absence of a verification step.
- **v4 canonical data** comes from `ingesters/orrpb-historical-summaries/scrape.py` — a stdlib HTML parser that pulls each station's published table from the ORRPB hub URL into a per-station CSV under `data/orrpb-historical-summaries/`. Reproducible, auditable, and the same data the analysis summary, regression scripts, and Exhibit H all use.

The Lac Coulonge canonical CSV ([`data/orrpb-historical-summaries/lake-coulonge.csv`](../../data/orrpb-historical-summaries/lake-coulonge.csv)) and the convenience copy ([`data/lac-coulonge-monthly-1972-2026.csv`](../../data/lac-coulonge-monthly-1972-2026.csv)) match exactly across the 54 overlapping years (verified: 0 value differences). Both reflect ORRPB's currently-published historical record.

## What changed

### Bar heights (per-year `daily_max`)

46 of 54 overlapping years (1972–2025) had value differences > 1 cm between the v1–v3 hardcoded data and the canonical CSV. The largest single-year discrepancies:

| Year | v1–v3 (m) | v4 canonical (m) | Δ |
|---|---|---|---|
| 1985 | 107.20 | **108.40** | +1.20 m |
| 1986 | 108.40 | **107.02** | −1.38 m |
| 1977 | 106.65 | 107.46 | +0.81 m |
| 1978 | 107.85 | 107.15 | −0.70 m |
| 1980 | 108.16 | 107.52 | −0.64 m |
| 1981 | 107.02 | 107.85 | +0.83 m |
| 1983 | 107.65 | 108.16 | +0.51 m |
| 1984 | 107.27 | 106.65 | −0.62 m |
| 2002 | 107.20 | 108.32 | +1.12 m |
| 2008 | 108.32 | 107.49 | −0.83 m |

The 1985 ↔ 1986 swap and the 2002 ↔ 2008 swap suggest some of the v1–v3 errors are paired transpositions rather than independent transcription mistakes. The two-year off-by-one signal across the full record was only 2/54 — so it's not a single shift, it's a mix of swap errors, isolated transcription errors, and possibly a mid-sequence offset in part of the table.

### Stat band

| Element | v1–v3 | v4 |
|---|---|---|
| Mean peak shift between eras | +61 cm | **+59 cm** |

The +59 cm value matches what the case-file analysis summary uses consistently throughout ([`Freshet_2026_Complete_Summary.md`](../analysis/Freshet_2026_Complete_Summary.md) lines 590, 605, 823, 1093, 1303, 1532). v1–v3's +61 cm was the outlier within the case file.

### Footer framing footnote

The footnote *"The +61 cm is in the inflow distribution (more years produce big freshets now), not in lake response per inflow"* is updated to use +59 cm.

### Version

v3 → v4 in both the visible footer and the SVG-baked source line.

## What did *not* change

The case file's load-bearing claims about Exhibit A are unchanged because they derive from the *structure* of the data (super-flood threshold crossings) rather than the exact peak values:

| Claim | v1–v3 | v4 canonical |
|---|---|---|
| Pre-2017 super-flood count (peak ≥ 108.5 m) | 1 (1979) | 1 (1979) ✓ |
| Post-2017 super-flood count | 4 (2017, 2019, 2023, 2026) | 4 (2017, 2019, 2023, 2026) ✓ |
| Pre-2017 super-flood rate | 2.22% | 2.22% ✓ |
| Post-2017 super-flood rate | 40.0% | 40.0% ✓ |
| Rate ratio | 18× | 18× ✓ |
| Headline ("In 10 years, the Ottawa River flooded as often as it did in 45.") | unchanged | unchanged ✓ |

The mean peak shift moved by 2 cm (61 → 59), within rounding of the load-bearing finding.

## What this means

- **Anyone holding a v1–v3 PNG of Exhibit A**: the bars for 1985, 1986, 2002, 2008 (and 42 other smaller-Δ years) are wrong relative to the canonical ORRPB record. The headline conclusions and super-flood counts are correct. Recommend replacing with v4.
- **Anyone who cited "+61 cm mean peak shift"**: the canonical figure is +59 cm. Difference is small but the v4 number aligns with the rest of the case file.
- **Anyone challenging the case file by cross-checking individual bars**: a v1–v3 cross-check would have caught the discrepancy and could legitimately ask whether the case file's data is reliable. v4 is now reproducible from the public scrape script and matches the rest of the case file.

## Mitigation for future exhibits

The v1–v3 issue arose because Exhibit A's data was hardcoded into the HTML directly, with no automated verification against the canonical source. Future exhibits (starting with Exhibit H) should:

1. **Derive embedded data from the canonical CSV via a generation script** rather than transcribed manually. Exhibit H follows this pattern — values are produced by `ingesters/climate-history/snowpack_overlay_analysis.py` and the JS literals are mechanically generated.
2. **Have a cross-check script** (e.g. `cross_check_overlay.py`) that verifies hardcoded values against the canonical sources and can be re-run anytime.
3. **Note the canonical source and last-checked date** in a code comment near the embedded data block, so future maintainers know what to verify against.

Exhibit A v4 now includes such a comment block above its `peaks` declaration.

## Related case-file material

- [`docs/exhibits/Exhibit_A_Regime_Change.html`](../exhibits/Exhibit_A_Regime_Change.html) — the v4 corrected exhibit
- [`ingesters/orrpb-historical-summaries/scrape.py`](../../ingesters/orrpb-historical-summaries/scrape.py) — canonical-data scraper
- [`ingesters/climate-history/cross_check_overlay.py`](../../ingesters/climate-history/cross_check_overlay.py) — verification script that surfaced the discrepancy
- [`exhibit_a_altered_version_in_circulation.md`](exhibit_a_altered_version_in_circulation.md) — separate integrity record for an externally-altered version of Exhibit A in FB circulation (different issue: external misattribution of a quote, not internal data drift)
