# Volume vs Peak Flow at Pembroke — what actually explains peak flood height

**Companion to the Pembroke-thread analysis — case-file note**
**Compiled: May 23, 2026**

> **Attribution note.** This note responds to a public Facebook-group
> thread (May 2026) in which one participant posted a "Des Joachims
> freshet volume vs Pembroke peak flood level, 1951–2015 vs 2016–2026"
> scatter, argued the historic relationship is unchanged, and concluded
> dam operators are not to blame for recent Pembroke peak heights. Other
> participants pushed back on three different grounds — total cumulative
> volume is not what causes peak height; pre-freshet reservoir state was
> ignored; and the cumulative metric throws away timing and shape. This
> note runs those rebuttals as statistics. Per the repo
> [attribution policy](../../CONTRIBUTORS.md), thread participants are
> referred to by role, not by name.

---

## Plain-language summary

Someone posted a chart showing that *total spring water volume passing
the upstream dam* (Des Joachims) and *peak spring flood height at
Pembroke* line up nicely across the years, and that the 2016–2026 points
sit on the same curve as the 1951–2015 points. The chart-author's
conclusion: dam operators aren't to blame for how high recent Pembroke
peaks have been.

The hidden problem is that **total volume is not what causes a peak**. A
flood gauge reading is determined by the *instantaneous* flow rushing past
it. Total volume over 90 days is a summary statistic of the whole spring
— it can be big either because the freshet was long and steady, or because
it was short and spiky. Those two scenarios produce very different peaks.
So total volume is a proxy for the thing that actually causes peak height
(peak daily flow), not the cause itself.

We tested that on the longest piece of daily Ottawa main-stem flow we
have access to (Britannia, 1960–2024, 59 spring seasons). Here is the
result in one paragraph:

- **Total volume alone explains 80 % of peak height variance.** That
  matches the original chart (it reported 73 %, we got 80 % with a
  slightly tighter window).
- **Peak daily flow alone explains 99.7 %.**
- **Total volume *plus* peak daily flow explains 99.7 %.**
- **Total volume's unique contribution after peak flow is known is 0.01
  percentage points** — essentially zero.

The diagnostic interpretation: total volume isn't doing the explanatory
work in the original chart. It correlates with peak daily flow at r =
0.89, and peak daily flow is what physically sets peak height. The 80 %
that volume "explains" is borrowed from a stronger variable that wasn't
in the regression. Once peak daily flow joins the model, volume becomes
statistically silent.

Two consequences for the thread argument:

1. **The 73 % R² doesn't prove what the chart author thinks it proves.**
   It is what you would see if volume were a perfect cause *or* a noisy
   proxy. The decisive test — putting both variables in the same
   regression and asking which contributes uniquely — was not run. We
   ran it. Volume's marginal contribution rounds to zero; peak flow's is
   20 percentage points. Volume is the proxy, not the cause.

2. **The chart cannot test the operator question even in principle.**
   Total volume passing Des Joachims is itself the output of upstream
   reservoir management. If operators released more water in the spring,
   both volume and peak rise together along the same hydraulic curve —
   the relationship between the two does not move. The chart shows
   hydraulics are unchanged. It is structurally silent on whether
   operating decisions are.

The honest restatement of the original chart's finding is therefore:
*given the water that came down through Des Joachims, Pembroke peaked
about as it always has*. That is a fact about the rating curve at the
gauge, not an answer to the dam-management question.

---

## Three thread arguments, three readings

The thread surfaced three distinct pushbacks. Each is correct in its own
domain, and each is addressable with the analysis here or with data the
case file already collects:

| Pushback | Author's role | Reading |
|---|---|---|
| "Total cumulative flow is irrelevant to water height — that is caused by instantaneous flow." | the timing-pushback commenter | **Correct, in the causal sense.** Peak gauge height is set by peak daily flow. Cumulative volume is associated with peak height only because it correlates with peak flow (r = 0.89 in our data). The marginal-R² test below makes this concrete. |
| "Pre-freshet reservoir levels should be normalized for." | the reservoir-state commenter | **Correct, and a separate variable.** Upper-basin reservoir storage entering the freshet determines how much inflow can be absorbed before water has to be passed. Not testable here without OPG/ORRPB reservoir storage series — a follow-up. |
| "Total volume captures most of it (R² = 0.72), so it is statistically very relevant." | the chart's author | **The math is right, the inference is wrong.** R² = 0.72 is the squared correlation of volume with the actual causal variable, not evidence that volume is itself the causal variable. The marginal-R² test below distinguishes proxies from causes. |

---

## What was tested

For each spring 1961–2024 on Britannia daily flow:

| | |
|---|---|
| **V**          | Total spring volume = Σ Q_daily × 86 400 (m³) over a window |
| **Q_pk**       | Peak daily mean discharge in the window (m³ s⁻¹) |
| **Q_mean**     | Mean daily discharge across the window |
| **peakedness** | Q_pk / Q_mean (dimensionless concentration) |
| **COM**        | Day-of-year of half-cumulative-volume (timing center) |

Response: **Britannia annual spring (Mar–Jun) maximum level**.

Two windows: **Mar 15 – Jun 15** (the original chart's choice) and
**Apr 1 – Jun 15** (the WMP-conventional date a commenter flagged) as a
robustness check.

**Why Britannia and not Pembroke.** There is no multi-decade daily-flow
record at Pembroke in the local archive — Pembroke shows up only as a
recent rolling level feed. Britannia (02KF005) is the only Ottawa
main-stem gauge with sufficient daily flow data (1960–2024). It sits
downstream of Pembroke and downstream of all the upper-basin reservoirs,
so it is a different reach. The findings about variable structure
(volume as a proxy for peak flow) are properties of how rivers work and
generalise to Pembroke; the specific Pembroke replication needs OPG's
operational Pembroke or Des Joachims daily flow series and is a clear
follow-up if you can get it.

**Script:**
[`ingesters/climate-history/freshet_volume_vs_peakedness.py`](../../ingesters/climate-history/freshet_volume_vs_peakedness.py)

---

## Headline result — the proxy-variable diagnostic

### Mar 15 – Jun 15 window (the chart author's choice), n = 59

| Model | R² | What it tests |
|---|---|---|
| V only (poly2)               | **0.7964** | The chart author's univariate fit |
| Q_pk only (poly2)            | **0.9970** | If peak flow alone causes peak height |
| V *and* Q_pk together (both poly2) | **0.9971** | Joint fit |

**Marginal contributions** — what does each variable add *uniquely*?

| | ΔR² | Reading |
|---|---|---|
| V's unique contribution beyond Q_pk | **+0.0001 (+0.01 pp)** | V adds essentially nothing once Q_pk is known |
| Q_pk's unique contribution beyond V | **+0.2007 (+20.07 pp)** | Q_pk adds 20 points of new information beyond V |
| Correlation V vs Q_pk | **r = 0.892** | V is a tight proxy for Q_pk |

### Apr 1 – Jun 15 window (robustness), n = 59

| Model | R² |
|---|---|
| V only       | 0.7825 |
| Q_pk only    | 0.9796 |
| V *and* Q_pk | 0.9812 |

Marginal: V over Q_pk = **+0.16 pp**; Q_pk over V = **+19.86 pp**;
r(V, Q_pk) = 0.904. **Same pattern**, slightly weaker absolute R² as
expected (shorter window captures less of the freshet hydrograph).

### Reading

The proxy-variable diagnostic distinguishes a *causal* predictor from a
*correlated* one. If a variable is doing the causal work, putting another
correlated variable into the regression alongside it should not shrink
its marginal contribution much. If a variable is along for the ride, its
marginal contribution collapses when the actual cause is admitted to the
model.

Total volume's marginal contribution is **0.01 percentage points** —
rounding error. Peak daily flow's marginal contribution is **20
percentage points**. Total volume's 80 % R² in the univariate regression
is its squared correlation with peak daily flow (0.892² = 0.795) playing
through the strong peak-flow-to-peak-level relationship. It is borrowed
explanatory power, not earned.

Stated as a single sentence: **at Britannia, peak daily flow alone
explains 99.7 % of peak level variance; total volume, after you account
for peak flow, explains 0.01 % more.**

---

## Supporting findings

The original analysis (`v1` of this note) framed the question as
"does shape add to volume." It does, and the answer is in three smaller
results that survive but are subordinate to the marginal-R² finding above.

### Hydrograph-shape model comparison

| Model | R² (Mar 15–Jun 15) | R² (Apr 1–Jun 15) |
|---|---|---|
| V only (poly2)                       | 0.7964 | 0.7825 |
| V + Q_pk                             | 0.9969 | 0.9803 |
| V + peakedness (Q_pk / Q_mean)       | 0.9889 | 0.9728 |

Either shape variable closes most of the 20-percentage-point gap. The
dimensionless peakedness ratio — which could be computed from the same
upstream gauge the original chart used — captures essentially the same
information as peak Q.

### Has the post-2016 era shifted on these residuals?

Pre-2016: 1961–2015 (n = 50). Post-2016: 2016–2024 (n = 9).

| Quantity | Pre mean | Post mean | t-test p |
|---|---|---|---|
| Residual from V-only model (Mar 15–Jun 15), m | −0.013 | **+0.070** | 0.36 |
| Residual from V-only model (Apr 1–Jun 15), m  | −0.015 | **+0.083** | 0.22 |
| Peakedness residual conditional on V (Mar 15–Jun 15) | −0.012 | **+0.065** | 0.39 |
| Peakedness residual conditional on V (Apr 1–Jun 15)  | −0.018 | **+0.099** | 0.20 |
| Raw peakedness median (Mar 15–Jun 15) | 1.74 | 1.80 | — |
| Freshet center-of-mass DOY (Mar 15–Jun 15) | 122 (May 2) | 121 (May 1) | 0.78 |

**Reading.** Every directional indicator points the same way: post-2016
springs sit ~7–8 cm above the volume-only prediction line, are slightly
more peaked at the same total volume, and have not moved earlier in
timing. With n = 9 post-2016 the t-tests come back at p ≈ 0.2–0.4 —
**directional, not significant**. Reported here for completeness; the
headline result of this note does not depend on these.

### Figures (`data/community-notes/`)

- `2026-05-23_peakedness_volume_mar15_jun15.png` — V vs peak level,
  pre/post coloured, poly2(V) curve
- `2026-05-23_peakedness_volume_apr01_jun15.png` — same, WMP window
- `2026-05-23_peakedness_vs_V_mar15_jun15.png` — peakedness vs V,
  pre/post coloured
- `2026-05-23_peakedness_vs_V_apr01_jun15.png` — same, WMP window
- `2026-05-23_residuals_mar15_jun15.png` — model-[A] residuals by year
- `2026-05-23_residuals_apr01_jun15.png` — same, WMP window

---

## Why this matters for the thread argument

The chart's conclusion was that, because the 1951–2015 volume-vs-peak
relationship is unchanged in 2016–2026, dam operators are not to blame
for recent Pembroke peak heights. Two structural problems make that
conclusion unreachable from that chart:

**Problem 1 — wrong variable on the X-axis.** Peak gauge height is
caused by peak instantaneous flow, not by 90-day cumulative volume.
Volume is a 0.89-correlated proxy. The univariate R² = 0.72 the chart
reports is volume's correlation with the real cause playing through the
rating curve, not evidence that volume is itself the right predictor.
Once peak daily flow is in the regression, volume contributes 0.01
percentage points beyond it — it is statistically silent. The dam-system
exists precisely to flatten peak flow at fixed volume (timing
redistribution), so testing on the axis where the dams *can't* act
(cumulative volume) and concluding the dams *didn't* act is a
mis-pointed test.

**Problem 2 — the X-axis is itself the operator's output.** Total volume
passing Des Joachims in spring equals the natural inflow to the upper
basin minus the change in reservoir storage over the window. The second
term — storage change — is exactly the operator's discretion. If
operators released more water through DJ in the spring (under any rule
set, old or new), both V and the peak rise together along the same
hydraulic curve, and the curve through the points does not move because
hydraulics did not move. The chart cannot distinguish "operators didn't
change anything" from "operators changed something but the change moved
both axes together."

A test that *could* speak to the operator question needs an
exogenous-forcing variable on the X-axis — basin snow water equivalent
plus spring precipitation, or a reconstructed unregulated inflow —
against peak height. That isolates what is controlled (operations) from
what is not (forcing). With reservoir storage data on hand, it would
also be possible to test pre-freshet storage levels against peak height
or against the V passed at DJ. Both are follow-ups; neither was in the
original chart.

---

## Relationship to existing case-file findings

This note **does not overturn** any of the existing analyses
([Pembroke-thread Britannia top-3, May 17, 2026](Pembroke_Thread_Trend_Changepoint.md);
Test A 2017 flow step). It addresses an upstream question — whether the
variable in the original chart is the right one — and the answer is no,
volume is a proxy for peak flow. The structural critique is independent
of any time-period finding.

| | Test A | Britannia top-3 (May 17) | This note |
|---|---|---|---|
| Variable | Britannia **flow** | Britannia **level** | Britannia **flow → level** |
| Window | 1960+ , Apr–Jul | full 1915–2024 | 1960+ , Mar–Jun |
| Question | given a break, which year? | any single step / cycle? | does volume cause peak height? |
| Answer | 2017 (+19.3 % median) | none unconditional; top-3 = 2019/2017/2023 | **no — peak flow does; volume is a 0.89-correlated proxy** |

---

## Caveats & follow-ups

- **Pembroke replication.** The Pembroke claim is not directly testable
  without OPG operational daily-flow data at Pembroke or Des Joachims.
  The findings here about *variable structure* — volume is a proxy for
  peak flow — are properties of how rivers work and apply at Pembroke;
  the specific numbers do not transfer one-to-one. If the OPG data is
  available the same script runs on it unchanged.
- **Bryson and Portage-du-Fort daily flow are too short in the local
  archive** (1985–1994 and 1942–1948 respectively). WSC HYDAT may have
  longer underlying records — worth a re-pull. Bryson is the cleanest
  available DJ-outflow proxy and would help.
- **n = 9 post-2016 is small.** The directional finding that recent
  years sit ~7 cm above the volume-only prediction line is real in
  direction but not in significance. Adding 2025 + 2026 when the WSC
  archive catches up (currently ends 2024) would meaningfully strengthen
  it.
- **Pre-freshet reservoir state is the other variable to add.** The
  reservoir-state commenter's pushback in the thread is well-posed and
  not addressed by the analysis here. Upper-basin storage going into the
  freshet should be tested against (i) peak level directly, and (ii) V
  passed at DJ — the latter is the most direct test of whether
  storage-management choices are pushing volume downstream. Needs OPG /
  ORRPB / HQ reservoir level series; a data scout is the next step.

## Reproduce

```bash
python3 ingesters/climate-history/freshet_volume_vs_peakedness.py
# requires numpy, scipy, matplotlib (precedent: thread_trend_changepoint_cycle.py)
```
