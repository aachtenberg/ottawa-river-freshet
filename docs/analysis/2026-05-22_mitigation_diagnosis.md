# Mitigation diagnosis — 2026 freshet and the 2017 regime change

*Internal working-notes synthesis, 2026-05-22. Developed alongside the
[`orrpb-2026-drawdown/`](orrpb-2026-drawdown/README.md) dataset and the
case-file exhibits (A, B, the Carillon directive notes, the 2016
management-change claim). **Private working draft — not for FB
distribution or public republication; an analytical position to refine,
not a final statement.** Companion to the public community note at
`freshet-public/data/community-notes/2026-05-22_reservoir_drawdown.md`.*

---

## The question

After the 2026 freshet, given everything in the dataset and the case
file: what could realistically have been done to mitigate it? And what
is actually driving the post-2017 super-flood cluster?

## The hard answer first

**No realistic operating regime would have prevented a major freshet in
2026.** Inflow volume was too large; Steve Deon's volume → peak
observation says the response curve is unchanged from history. The
honest framing is not "could the flood have been prevented" but **"how
much could the peak have been managed down."**

Order-of-magnitude estimate, integrating the data we have:

- **Lower-river crests** (Carillon, Hull, the islands): **15–40 cm** of
  shaveable peak available under the moves listed below.
- **Lac Coulonge / Pembroke**: meaningfully less — **5–15 cm at best** —
  because Lac Coulonge is run-of-river and its crest is hydraulically
  set rather than setpoint-controlled.

These numbers are estimates, not modelled. They are the bounds within
which the policy argument has to live.

## Levers available, ranked by magnitude

### 1. Carillon §2.1 flood-period rules — neither limit invoked in 2026 (largest single *lower-river* move)

The Carillon dam is governed by HQ's **Impounded Water Management Plan
Summary, Carillon Project (October 2004)**, §2.1 "General Constraints
Associated with Forebay Management." The constraint table and four
operating envelopes are already transcribed and analysed in the case
file at
[`../freshet-public/docs/reports/2004_Carillon_IWMP_operating_envelope.md`](../freshet-public/docs/reports/2004_Carillon_IWMP_operating_envelope.md);
that document is the authoritative case-file extract and predates this
diagnosis. The same table also appears as page 3 of the ORFA *Eight
Ways to End the Super Floods* whitepaper (Feb 2025) — see
[`../freshet-public/docs/reports/2025-02-18_ORFA_8_Ways_extract.md`](../freshet-public/docs/reports/2025-02-18_ORFA_8_Ways_extract.md)
— and was independently posted to FB by Alexandre Morin on 2026-05-22.
The §15.3.5.1 reference earlier notes used lives in the longer 2004
*évaluation de sécurité* (Section 15, p.314); both documents express
the same constraint. Documentary chain at
[`case-file/correspondence/2021-2023_Morin_MNRF_Carillon_directive.md`](case-file/correspondence/2021-2023_Morin_MNRF_Carillon_directive.md).

§2.1 sets four forebay constraints:

| | Level | Conditions |
|---|---|---|
| Critical maximum | 41.5 m | per agreement |
| Operating maximum | 41.15 m | **40.08 m** during spring flood when Hull dock > 42.61 m servitude |
| Operating minimum | 39.62 m | outside-boating 40.54 m · boating 40.84 m · **flood-period 39.62 m** |
| Critical minimum | 39.62 m | |

**Precision matters.** The language is *permissive* — "the minimum is
X" sets the allowed floor, it does not mandate reaching it. So §2.1
does **not** *require* HQ to draw down to 39.62 m every freshet — it
*permits* them to, and it *requires* a 40.08 m ceiling once Hull
crosses servitude. Our earlier "HQ should be drawing down to 39.62"
framing overstated the floor side. What 2026 actually shows is a
different and arguably sharper pair of findings.

**2026 result — both limits of §2.1's flood-period regime non-invoked:**

1. **Floor side — treated flood as boating season.** Carillon's
   pre-freshet level was **40.82 m on April 1**, declining to a low of
   **40.43 m on May 13**. That minimum sits right at the
   *outside-boating-season* minimum of 40.54 m. **HQ effectively ran
   the 2026 freshet at boating-season-equivalent operating rules**,
   not at the flood-period rules §2.1 makes available. The 81–92 cm
   between the floor they used (~40.43–40.54) and the flood-period
   floor on offer (39.62) is room they chose not to invoke. This is
   *non-invocation* of a permitted option, not *non-compliance* with a
   mandate.

2. **Ceiling side — non-compliance, not just non-invocation.** Hull
   dock crossed the 42.61 m servitude on **April 13** and stayed above
   through **May 21 — 39 consecutive days**. Per §2.1 the Carillon
   maximum during that window *is* 40.08 m. Carillon sat **above
   40.08 m on all 39 of those days**, with a peak overshoot of
   **+0.44 m on April 15** (Carillon 40.52 m, Hull 43.31 m). This is a
   binding constraint, not a permitted option — so this side is actual
   non-compliance with §2.1.

The same §2.1 that *permitted* deeper drawdown also *required* a lower
operating maximum once Hull crossed servitude, and **neither was
operationalised** during the 2026 freshet. The ceiling side is the
stronger finding because it is a regulatory non-compliance, not a
discretionary non-invocation.

**Geographic reach of this lever.** The Carillon impoundment extends
upstream to roughly **Britannia / Deschênes**. So both findings above
directly affected the lower ~80 km of the river — **Lac des
Deux-Montagnes, Île Bizard, Hudson, Vaudreuil, Hawkesbury, Grenville,
Thurso and the Hull / Gatineau lowlands**. They do **not** reach Lac
Coulonge, Fort-Coulonge, Pembroke or anything above Chats Falls; those
reaches sit above the Carillon impoundment with multiple dams between,
and Carillon's level is hydraulically irrelevant to them.

For the communities **inside the Carillon impoundment**, this is the
single largest tens-of-cm move available, and the cleanest political
ask, because it is compliance with HQ's own published §2.1 — not new
policy. For the upper-river communities (Lac Coulonge / Fort-Coulonge
/ Pembroke / Mansfield), Carillon is **not a lever at all**; their
flood is set by the upper-Ottawa cascade, addressed by the moves below
that act on the upper system.

### 2. Gatineau / Lièvre storage drawn deeper

On April 1, 2026 (per [`reservoir_drawdown_apr1.csv`](orrpb-2026-drawdown/reservoir_drawdown_apr1.csv)):

- **Cabonga** — 60 % of band, low point Jan 20 (54 %); never drew down
  for the freshet
- **Kiamika** — 45 %, low point Apr 2
- **Mitchinamecus** — 43 %, low point Apr 1

Combined unused buffer to floor: approximately **1,100 Mm³** — roughly
1–2 days of peak freshet flow at the lower Ottawa. The Gatineau joins
at Gatineau city and the Lièvre at Masson — **both below the Gatineau
confluence**, so this lever does nothing for Lac Coulonge or the upper
river. It is purely a lower-Ottawa lever.

### 2a. Quantified target gap — what "lower and earlier" actually means

Working from `orrpb-2026-drawdown/raw/` daily series for the 13 principal
reservoirs (excluding the Haileybury duplicate gauge), and weighting each
reservoir by its **usable storage (Mm³)** from the ICOLD-Canada case
study, the 2026 storage-weighted standing was:

| Quantity (storage-weighted across 13 reservoirs) | Value |
|---|---|
| Total usable storage in the system | 12,144 Mm³ |
| Average % of operating band on April 1 | **23.24 %** |
| Volume held above the operating floor on April 1 | **2,822 Mm³** |

If the under-drawn four (Cabonga, Kiamika, Mitchinamecus, Bark Lake)
had been brought to the same 5–7 % of band that the well-drawn upper-
Ottawa cluster (Kipawa –2 %, Des Joachims 6 %, Poisson Blanc 8 %,
Timiskaming 10 %, Dozois 18 %) actually achieved, the gap closes:

| Target | Volume above floor at target | Buffer recovered vs 2026 actual |
|---|---|---|
| 0 % (absolute floor) | 0 Mm³ | **2,822 Mm³** |
| 5 % (deep best-of-class) | 607 Mm³ | **2,215 Mm³** |
| 7 % (achievable mean) | 850 Mm³ | **1,972 Mm³** |
| 10 % | 1,214 Mm³ | 1,608 Mm³ |

So the **drawdown gap is roughly 17 percentage points lower on a
storage-weighted basis** (23 % → 6 %), recovering on the order of
**~2,000 Mm³ of additional pre-freshet buffer**. Routed through the
cascade at ~30 % transfer efficiency from upstream buffer to downstream
peak, that translates to roughly the 15–40 cm of shaveable lower-Ottawa
crest already estimated above — the two estimates are internally
consistent.

**Timing gap.** Date of seasonal minimum, by reservoir, 2026:

| Hit minimum by mid-March (best-of-class) | Hit minimum at/after April 1 (late) |
|---|---|
| Cabonga Jan 20 *(but at 54 % — early but trivial)* | Kipawa Apr 1 |
| Lady Evelyn Feb 16 | Mitchinamecus Apr 1 |
| Bark Lake Mar 4 *(per WMP)* | Baskatong Apr 2 |
| Timiskaming Mar 8 | Kiamika Apr 2 |
| Dozois Mar 14 | Poisson Blanc Apr 2 |
| | Des Joachims Mar 27 |
| | Quinze Mar 30 |
| | Rapide-7 Apr 12 *(during the rising limb)* |

Median date of seasonal minimum: **2026-03-30**, only 6 days before the
rising limb began (~April 5). Best-of-class that *meaningfully* drew
down (excluding Cabonga's trivial January minimum at 54 %) reached
their floors **2–3 weeks earlier** — Timiskaming Mar 8, Dozois Mar 14.

**The numeric ask:** target **~7 % of band, storage-weighted, hit by
mid-March, held to late April.** Roughly *17 percentage points lower
than 2026 ran, ~2 weeks earlier to seasonal minimum.* That's the
quantified form of ORFA's Action 7 ("lowered to absolute minimum +
delay refill").

**Two ways to frame the target — both valid, slightly different gaps.**
Dan Poole arrived at the same finding independently on the FB thread,
benchmarking against the **30-year historical median** rather than
best-of-class achievement: Quinze drew down to the 30-yr median of
260.81 m (= 23.8 % of band, 311 Mm³ remaining); Baskatong drew slightly
below its 30-yr median of 210.02 m to 209.61 m (= 12.9 %, 393 Mm³
remaining). Cross-checked against the same ORRPB data both numbers
match to the second decimal. His implicit target is *the absolute low-
limit* (0 %); mine is *what best-of-class operators actually achieved*
(~7 %). Both surface the same underlying problem:

| Target framing | Storage above floor at target | Gap vs 2026 actual |
|---|---|---|
| Dan's absolute low-limit (0 %) | 0 Mm³ | **2,822 Mm³** |
| My "best-of-class achievable" (7 %) | 850 Mm³ | **1,972 Mm³** |

The ~850 Mm³ difference between framings is the operationally-cautious
buffer the operators choose to keep even when they're drawing down
hard. Dan's framing is the more rhetorically pointed FB-audience
version ("they didn't go to floor"); mine is the realistic-operational
target. Both belong in the case file.

The more important point both framings converge on: operators **drew
down to long-standing median practice but no further**. They are not
deviating from how they have always operated — they are doing what has
always been done. The problem is not operator misbehaviour; it is that
median practice is calibrated to a climatology that no longer matches
the inflows we are getting. That's the 30-year-baseline diagnosis
showing up in operator-by-operator numbers.

**Two honest caveats.**

- **Bark Lake's 43 % is partly by design.** Its OPG Madawaska Water
  Management Plan (2009, §9.2.5) schedules refill to begin April 1
  toward the 313.62 m summer-min target. So Bark Lake's April-1 figure
  is *partly compliant with its own WMP, not pure non-compliance*. The
  HQ-controlled trio (Cabonga, Kiamika, Mitchinamecus) is the cleaner
  "should have drawn deeper" set.
- **Volume → peak transfer is not 1:1.** The ~2,000 Mm³ recovered
  buffer would not translate to 2,000 Mm³ of crest reduction; routing
  through the regulated cascade, the transfer efficiency to the
  lower-Ottawa peak is on the order of 20–40 %, consistent with the
  15–40 cm shave estimated in the "hard answer first" section above.

Numbers verified against `orrpb-2026-drawdown/raw/` 2026-05-23.

### 2b. What the storage lever would have done for Lac Coulonge — honestly, not much

The 17-pp / 2,000-Mm³ gap above is a **system-wide** number, and the
geographic asymmetry matters. For the upper-river communities (Lac
Coulonge / Fort-Coulonge / Mansfield / Pembroke), the storage lever is
much smaller than the headline figure suggests, and it's worth being
honest about that before the case file lands in front of those
residents.

**The under-drawn reservoirs do not feed Lac Coulonge.** All four
(Cabonga, Kiamika, Mitchinamecus, Bark Lake) sit on the Gatineau, the
Lièvre, and the Madawaska — every one of those tributaries joins the
Ottawa River *downstream* of Lac Coulonge. So closing the 2,000 Mm³
system gap delivers buffer to Hull, Gatineau, Hawkesbury, Île Bizard,
Lac des Deux-Montagnes — but **none to Lac Coulonge**.

**The reservoirs that do feed Lac Coulonge were already drawn down
well in 2026.** Storage upstream of Lac Coulonge on April 1:

| Reservoir upstream of Lac Coulonge | Apr 1 % of band |
|---|---|
| Kipawa | –2 % (at floor) |
| Timiskaming | 10 % |
| Dozois | 18 % |
| Rapide-7 | 20 % (touched –1 % during freshet) |
| Quinze | 24 % |
| Lady Evelyn (Montreal River) | 33 % |

Marginal additional drawdown on these is small — most are already at
or near their operating floors. Best-case 5 cm of additional crest
relief at Lac Coulonge from squeezing more out of the upper-Ottawa
cascade.

**Available levers, with honest order-of-magnitude estimates for the
2026 Lac Coulonge crest:**

| Lever | Best-case Lac Coulonge crest shave |
|---|---|
| Even-deeper drawdown of upper-Ottawa storage (already near floor) | ~5 cm |
| Bryson headpond drawn lower (Exhibit B winter baseline; the early-March drawdown-and-refill cycle proved the operator can move it) | ~5–15 cm (1:1 winter→peak transfer assumption is uncertain) |
| Chenaux headpond drawn lower (downstream backwater reduction) | ~5–10 cm (uncertain) |
| **Realistic combined shave at Lac Coulonge** | **~10–25 cm at the 2026 peak** |

So the 108.63 m peak might have become 108.40–108.53 m under the full
case-file ask. Still a major flood. Still above the property-survey
108.48 m backyard threshold and the 108.52 m crawl-space threshold.

**What this implies — four honest reframes:**

1. **The 2026 freshet at Lac Coulonge was largely unavoidable at that
   magnitude given the upper-Ottawa inflow volume.** No reasonable
   operating regime stops a 108-plus event when the inflow is what
   2026 delivered. The upstream reservoirs were already doing their
   job; squeezing another 5 cm out of them doesn't change the
   headline.
2. **2026 also wasn't the worst case it could have been — partly
   because the weather did some of the operator-work.** The April
   19–21 sub-zero overnight freeze stopped active melt for three
   nights and slowed the rising limb, holding the crest below where a
   faster melt would have put it. Dan Poole made this point on the FB
   thread, and the case-file complete summary documents it as one of
   the three factors that kept the first peak below worst-case. So
   the "managed the recession well" framing (Jim Coffey) is partly
   real operator skill on the second peak and partly weather luck on
   the first — both should be named honestly.
3. **The Bryson piece is the only meaningful single-year Lac-Coulonge
   lever** — and it's the part that's a deliberate operating choice
   by HQ (the elevated winter setpoint, the early-March drawdown-then-
   refill cycle). Politically the right thing to press on; the
   peak-reduction is small but the *operator-choice* framing is real.
4. **The big system lever (Cabonga / Kiamika / Mitchinamecus / Bark
   Lake) benefits the lower river, not the upper.** That's a real ask
   but it's an ask Joan LaCroix's reach should be making, not Lac
   Coulonge's. The case file should not present the 17-pp gap as
   addressing Lac Coulonge's concerns when it geographically does not.

**The case for Lac Coulonge is fundamentally a multi-year,
frequency-reduction case** — four super-floods in 10 years vs one in
the prior 45. Any single year doesn't move much for Lac Coulonge under
the full ask; the *frequency* of super-flood years dropping back
toward the historical baseline is where the win lives. That's the
honest case the upper-river communities have. It's not as immediately
satisfying as "draw the reservoirs down and the flood stops," but
it's true, it's defensible, and it's consistent with everything the
data shows.

### 3. Bryson headpond lower

Wayne Freeland's three feet. Lac Coulonge demonstrably sat at 105.67 m
in October 2025 and the all-time recorded low is 105.07 m, against a
2026 winter setpoint of 106.55 m. The early-March 2026
drawdown-then-refill cycle proved on the record that the operator can
move the pond 24 cm in days. Lowering the headpond would have
meaningfully helped **rising-limb timing** and given shoreline residents
days of low water before the freshet arrived. **For the crest itself,
the benefit is small** — run-of-river arithmetic limits it to a few cm
at the peak. This lever lives on the upper Ottawa and is HQ's call.

### 4. Snowpack-indexed coordination (the structural fix)

Today the system draws to fixed April-1 targets regardless of basin
loading. A snowpack-indexed protocol — deeper drawdown in heavy-snow
years, across storage reservoirs **and** run-of-river reaches together —
is the structural fix. Exhibit B's scope note articulates this. The
2026 data argues for it: the storage reservoirs were drawn down
competently, but the run-of-river reaches were not, and the cumulative
buffer was less than the snowpack warranted.

None of these levers alone prevents a flood. Cumulatively they shrink
it — and in a regime where 108-plus is happening every 2–3 years
instead of every 45, the year-over-year shrinkage is the point, not
the single 2026 event.

## On the 2017 step change

Exhibit A: pre-2017 super-flood rate 2.22 %; post-2017 40 %; an 18×
increase. Four super-floods in 10 years (2017, 2019, 2023, 2026) versus
one in the prior 45.

The land-use observation is correct and important: **there is no
development driver** in these reaches. Upper Ottawa is Crown forest;
the inflow basins are largely unchanged in cover and use over the
relevant period. So what changed?

Ranked by my confidence:

### A. Climate is doing some of it

The volume → peak relationship is unchanged (Steve Deon, Exhibit A);
what has changed is the **inflow distribution**. Bigger snowpacks,
faster simultaneous southern + northern tributary melt, rain-on-snow
events. The operating envelope was sized for 1972–2010 hydrology and
is now being exceeded routinely. This is the structural driver.

### B. Operations drifted in the wrong direction over the same window

The case file documents a 2016 management-change claim
([`freshet-public/docs/reports/2016_management_change_claim.md`](../freshet-public/docs/reports/2016_management_change_claim.md));
the Bryson refurbishment timeline (Hydro-Québec, ~2017 onward) lines
up; this conversation's fresh data work has now added the elevated
2026 winter baseline, the de-facto Carillon floor sitting 88 cm above
directive, and the deliberate Lac Coulonge setpoint with the
early-March test refill. **None of these are conspiratorial** — each is
defensible by some local objective (hydraulic head, generation, ice
stability, downstream flow management) — but cumulatively they hold
back pre-freshet water that historically was not held back.

### C. The two compound

This is the honest answer. Climate made the inflows larger, and the
operating regime — which never updated to match — drifted in the
*opposite* direction, toward more retention. An 18× super-flood-rate
change is what that compound looks like.

## The diagnosis

Each operator — HQ at Carillon, HQ at Bryson, OPG on the Madawaska,
MELCC on the Quebec reservoirs — is optimizing for their own licence,
their own constraints, their own revenue. The directive floor nobody
honours; the Bryson headpond carried high; Cabonga at 60 % on April 1
— each is individually defensible by some local objective.

But cumulatively: **the system is being run with less pre-positioned
buffer than it used to be, in a climate that needs more, and there is
no single entity whose explicit job is to look at the whole picture and
say *this is no longer in balance.*** The ORRPB coordinates but does
not bind. Licensing is fragmented across two provinces and a federal
regulator. The 2017–2026 super-flood cluster is what that gap looks
like under stress.

## What would actually fix it

Not a single operating decision; not negotiations between operators.

**A binding requirement, written into each operator's licence**, that
the whole system precondition itself to a snowpack-indexed target every
spring — with each operator's share enforceable by their licensing
regulator (CEHQ in Quebec, MNRF / dam safety in Ontario, federal where
it applies).

That is **regulator-level action**, not operator goodwill. The political
precondition for it is residents being able to point to specific,
defensible, reproducible exhibits showing the gap. Which is what the
case file is for — and why the case-file strategy (build verifiable
exhibits, target the licensing-renewal proceedings) is the correct one.
FB threads are not where this gets won; the licensing proceedings are.

## Honest framing of what 2026 was

The 2026 freshet was a test the operators were given an open-book
exam for, with each writing different answers in different books. The
right correction is not grading their papers harder — it is **writing a
single, snowpack-indexed exam** the whole system has to write together.

---

## What I am confident in vs what I am inferring

**Confident** (data-supported):

- Storage drawdown was largely competent except Cabonga/Kiamika/Mitchinamecus
- Lac Coulonge winter baseline was deliberately elevated and held flat
- The early-March drawdown-then-refill cycle is operator-driven, not hydrology
- Bryson is HQ; refurbishment ~2017–2023 timeline
- The post-2017 super-flood rate change is real and large
- Volume → peak relationship at Lac Coulonge is statistically unchanged
- **Carillon §2.1 ceiling non-compliance in 2026: Hull dock above the
  42.61 m servitude for 39 consecutive days (Apr 13 → May 21), Carillon
  above the 40.08 m flood-period ceiling on all 39 of those days, peak
  overshoot +0.44 m on Apr 15. Source: §2.1 of the 2004 IWMP Summary
  (publicly posted) plus ORRPB Hull/Carillon daily series.**

**Inferring / arguing** (defensible but not proven):

- That the elevated 2026 winter baseline is consistent with a deliberate
  higher-headpond operating posture (user's external knowledge plus the
  data shape; no public regulatory citation yet)
- That climate + operational drift compound, with climate as the
  dominant structural driver
- The 15–40 cm and 5–15 cm peak-shave estimates are order-of-magnitude,
  not modelled
- The diagnosis of fragmented licensing and "no system-level entity" is
  structural reading, not a single sourced citation

**Open / would strengthen the position**:

- Any regulatory paper trail on a Bryson headpond setpoint change since
  the refurb (ORRPB notice, CEHQ filing, WMP amendment)
- A formal modelled estimate of how much the 2026 peaks would have
  responded to deeper Gatineau drawdown and Carillon directive
  compliance
- Pre-2017 vs post-2017 winter-baseline statistics across multiple
  reaches (we have Lac Coulonge; Pembroke, Chenaux, Britannia would
  strengthen the case)
