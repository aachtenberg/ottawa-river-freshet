# Cottage-setup wizard — validated mark fields

Status: **validated against lived cottager observations** (Mansfield / Lac Coulonge 2017–2019 diary + 2026 freshet case file). Ready to drive the MVP marks editor.

This is the answer to: *which wizard fields do shoreline residents actually know?*

---

## Validation source

We did **not** invent flood science or surveyor jargon. Fields were checked against marks a real cottager recorded while watching the same gauge the app will use:

| Source | What it contributes |
|---|---|
| [Appendix A — 2019 Original Property Observations](../analysis/Freshet_2026_Complete_Summary.md) | Day-by-day shoreline landmarks correlated to Lac Coulonge (1195) levels |
| Dashboard `PROPERTY_THRESHOLDS` + footer | Same lived marks vs Lebel survey lines (explicitly *not* personal observations) |
| Alerter `THRESHOLDS` | Which marks are worth notifying on (lived only — no survey lines) |
| 2026 action thresholds in the complete summary | Decision language cottagers already use (pumps, sandbags) |

**Honest limit:** the corpus is one property on Lac Coulonge. The *shape* of the marks (shoreline landmarks in metres on the home gauge) generalizes; absolute elevations and which optional marks apply do not. Additional reaches should refine labels, not the schema.

---

## Verdict: what cottagers actually know

Cottagers know **shoreline landmarks**, not flood-recurrence lines.

They can usually answer:

1. “When did water first reach the lot / lawn?”
2. “When was the backyard / driveway wet?”
3. “When did water touch the building (bricks, foundation, crawl-space joists)?”
4. “When did water get inside?”

They usually **cannot** answer without a survey or official map:

- 20-year / 100-year flood elevations
- Geodetic vs gauge datum offsets
- Exact centimetres unless they wrote down the gauge reading on that day

**Critical UX honesty (unchanged from the plan):** cottage *margin* (“47 cm to bricks”) requires at least one structural mark. Without personal marks, the green panel may only show official Vigilance état (minor / moderate / major).

---

## Validated wizard schema

### Step 0 — cold start (required)

| Field | Required | Notes |
|---|---|---|
| Property name | Yes | Free text, e.g. “Cottage — Constance Bay” |
| Home gauge | Yes | From snap + confirm ([gauge-snap.md](./gauge-snap.md)); editable |
| Mode | Yes | `personal_marks` (default path) or `vigilance_only` (skip marks; weaker home panel) |

### Step 1 — lived marks (core)

Ask for **metres on the home gauge** (same mental model as today’s property card). Order ascending. Allow skip-per-field; require at least **one** of `approaching` / `backyard` / `structure` to leave `vigilance_only`.

| Key | Prompt (EN) | Cottager knows this? | Role in UI / alerts |
|---|---|---|---|
| `approaching` | Water approaching property (lot / lawn edge, not yet in the yard you use) | **Yes** — first “uh oh” day | Soft amber; early alert |
| `backyard` | Water in backyard / driveway / outdoor living space | **Yes** — most memorable mid mark | Amber/orange zone; pumps language |
| `structure` | Water at foundation / bricks / siding (building envelope) | **Yes** — the margin target | Red zone start; sandbag language; **cottage margin** |
| `inside` | Water inside living space / garage / finished areas | **Yes** when it happened | Deep red; highest-priority alert |

**Do not** force all four. Partial profiles are valid:

- Only `structure` → margin works; zones above/below are thinner
- Only `approaching` + `backyard` → early warnings work; no brick margin until refined
- Empty → `vigilance_only`

### Step 2 — conditional lived mark (optional)

| Key | Prompt | When to show | Why optional |
|---|---|---|---|
| `crawl_space` | Water in crawl space / up to floor joists | Only if user says they have a crawl space / pier foundation | Mansfield’s 2017 peak lived here; many slab or raised cottages have no equivalent |

Place it **between** `backyard` and `structure` when present. Never invent a crawl-space mark for properties that don’t have one.

### Step 3 — survey lines (optional, clearly labeled)

| Key | Prompt | Cottager knows this? |
|---|---|---|
| `survey_20yr` | Surveyed 20-year flood line (metres) | Only if they have a survey |
| `survey_100yr` | Surveyed 100-year flood line (metres) | Only if they have a survey |

Footer copy must match the dashboard: survey lines are **not** personal observations; datum may differ from the gauge by centimetres. On Lac Coulonge the Lebel lines happen to sit near lived marks; that alignment is **not** guaranteed elsewhere.

### Step 4 — provenance (optional, skippable)

| Key | Values | Purpose |
|---|---|---|
| `how_known` | `photo_hwm` · `recollection` · `gauge_diary` · `survey` · `refine_later` | Trust + future refinement UX |
| `reference_year` | Free / year chip (e.g. 2019) | Helps them recall which flood they are describing |

---

## Mapping to today’s Mansfield constants

| Lived key | Mansfield example (m) | In alerter today? |
|---|---|---|
| `approaching` | 108.30 | Yes |
| `backyard` | 108.48 | Yes |
| `crawl_space` | 108.52 | Yes |
| `structure` | 108.75 (bricks) | Yes — margin baseline |
| `inside` | 109.01 | Yes |
| `survey_20yr` | 109.05 | No (dashboard only) |
| `survey_100yr` | 109.34 | No (dashboard only) |

2019 record (109.17) is **gauge history**, not a cottage mark — do not ask for it in the wizard; surface it later if that gauge has a history pack.

---

## Copy rules (validated language)

Prefer landmark verbs cottagers used:

- “approaching property” / “in backyard” / “at bricks” / “inside”
- Action glosses when useful: “pumps operational”, “sandbag foundation”

Avoid:

- “1:20 / 1:100 recurrence” as required fields
- Asking for elevations in feet without a clear unit toggle (basin gauges are metres MASL)
- Implying the app’s marks are official flood lines

---

## Green-panel behaviour by completeness

| Profile completeness | Status panel can show |
|---|---|
| `vigilance_only` | Official état + corridor context; **no** cottage margin |
| ≥1 lived mark, no `structure` | Zones from known marks; margin omitted or “add foundation mark for margin” |
| Has `structure` | Full green / amber / red grammar + **cottage margin** (today’s 108.75 behaviour) |
| Has survey lines | Extra ticks on the bar; never override lived alert priorities |

---

## Follow-up validation (other reaches)

Before claiming multi-reach copy is settled, spot-check 2–3 cottagers outside Lac Coulonge (esp. Constance Bay / Lac Deschênes and Britannia) with this prompt set:

1. Which of the four core landmarks can you name from memory?
2. Do you have a crawl space equivalent?
3. Do you have a survey with elevations you trust against Britannia / Buckhams / your local gauge?
4. Would you rather enter metres from a flood diary, or tap “use official flood states only” first?

Expect schema to hold; expect **labels** (“bricks” vs “siding” vs “breakwall”) to need per-property synonyms — store `structure_label` as free text defaulting to “foundation / bricks”.

---

## Implementation notes

- Persist profile in `localStorage` first (see [mvp-pwa.md](./mvp-pwa.md)).
- Validate: marks must be strictly increasing when multiple are set (`approaching` < `backyard` < `crawl_space` < `structure` < `inside`).
- Same keys feed alerts; survey keys never fire push alone.
