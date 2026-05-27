# Why the Ottawa River is a boneyard at Deux Rivières and flooding at Mattawa

**Compiled 2026-05-27 in response to a Facebook thread question from Rudy Dyck, with an answer from Dan Poole, in the Northern Reservoirs / Ottawa River / Tourism / Wildlife / Flood Watch group.**

## Plain language summary

Rudy asked why the Ottawa River runs dry around Deux Rivières every spring while Mattawa, upstream of there, ends up flooding. Dan's answer (paraphrased here for the case file): OPG keeps the Otto Holden head pond at Rolphton drawn down through the early freshet to absorb whatever Temiscaming Reservoir releases without backing water up to Mattawa. Once the upstream peak has passed they refill in two stages, a short stage 1 of about a week, then a pause to check Mattawa, then stage 2.

That tracks with the geography and with the operating pattern this case file has documented elsewhere in the cascade. The Otto Holden head pond extends upstream from Rolphton to roughly the Mattawa area, so its level controls backwater pressure at the town. Drawing the pond down does two things at once: it exposes the shallows around Deux Rivières that Rudy sees as a boneyard, and it gives the pond capacity to absorb a Temiscaming peak without pushing the water surface up at Mattawa. Refilling too aggressively raises that backwater pressure, which is why Dan describes the refill as deliberately staged with a Mattawa-flood-risk check between stages.

The structural point for the case file is that **the two-stage refill Dan describes at Otto Holden is the same pattern this case file documented at Des Joachims** in the [Pembroke 2023 vs 2026 community note](2026-05-23_pembroke_2023_vs_2026.md) and in the [Pembroke Thread Synthesis](../../docs/analysis/Pembroke_Thread_Synthesis.md). Stage 1 is the short refill, the pause is the operator-internal assessment, stage 2 is the longer plateau approach. Seeing the same protocol at two different OPG generating stations in the same cascade in the same year is evidence the protocol is **basin-wide OPG operating procedure, not a Des Joachims peculiarity**.

That matters because the case-file thesis is that the central peak-management lever in the Ottawa cascade is daily release scheduling at each dam, not pre-freshet storage. Dan's Mattawa explanation gives that thesis an upstream instance: the lever at Otto Holden is staged refill timed against Mattawa flood risk, the lever at Des Joachims is staged refill timed against Pembroke peak height, and the chain continues downstream to Chenaux and Carillon. Each dam manages the next-downstream community's risk through release timing, not through pre-positioned empty storage.

## The geography in one paragraph

Upstream to downstream on the Ottawa main stem in this reach: Lake Timiskaming sits at the headwaters, fed by the upper Ottawa and the Blanche; Temiscaming dam at the lake's outlet is operated by Brookfield Renewable (Energy Ottawa); roughly 150 km of river runs south through Deux Rivières to Mattawa; the Mattawa River joins from the east at the town of Mattawa; Otto Holden Generating Station sits about 30 km downstream at Rolphton and is operated by OPG; its head pond (sometimes referred to locally as Holden Lake or Lake la Cave) extends back upstream and includes the Deux Rivières reach. Des Joachims is the next OPG station downstream of Otto Holden, then Chenaux, then Chats Falls, then Carillon.

The hydraulic point: when the Otto Holden head pond is drawn down, the **upper end of that pond at Mattawa drops too**, but only to a point. The water surface in the head pond is governed primarily by the dam at the downstream end and secondarily by inflow at the upstream end. With high Temiscaming inflow, even a drawn-down pond can have its upper end (Mattawa) rise above the dam-end target because the river has to slope downhill to keep flowing. The flatter the pond's profile, the more inflow drives the upstream end up. That is the constraint Dan is describing: at peak inflow, the Mattawa end of the head pond can flood even with Otto Holden held below normal target.

## What is and is not verifiable on public data

Dan's account of the two-stage refill at Otto Holden is **consistent with** the same two-stage signal visible in the Des Joachims head pond ORRPB record (see [Pembroke 2023 vs 2026](2026-05-23_pembroke_2023_vs_2026.md)), but ORRPB does not publish a per-day Otto Holden head pond series on its current location pages. The verification path would be a similar ingest of ORRPB's `/location/otto-holden/` table view, the same one used for the [Lake Coulonge / Bryson](2026-05-26_lake_coulonge_2026.md) and [Chenaux](2026-05-26_chenaux_thread.md) notes. The `orrpb-station-history` ingester already includes Otto Holden as one of its scheduled stations, so the 2026 trace will populate over the coming nights and can be compared to 1991 to 2020 climatology then.

WSC has one active gauge on this Ottawa-main-stem reach: **02JB013 Ottawa River at Mattawa**, level-only, RHBN. Real-time level at Mattawa is the public-record instrument that would let analysts read out Otto Holden head pond stage at its upstream end. Combined with the Temiscaming outflow (operator-internal, Brookfield) and the Mattawa River tributary input (WSC 02KB001 is downstream of this reach but Mattawa River 02JE013 exists upstream), this reach has more public-data coverage than the Pembroke reach has, and would be a candidate audit target if a future case-file iteration extends upstream.

## What this changes in the case file

Nothing structurally. The thesis is unchanged. What changes is the **breadth** of supporting evidence:

- Before: two-stage refill is a Des Joachims operating signal observed in 2023 and 2026.
- After Dan's Mattawa explanation: two-stage refill is an OPG-cascade operating protocol observed at at least Des Joachims and Otto Holden in 2026.

That is one more line in the *Eight Ways* policy argument that peak-time release scheduling is the lever, and it lands the argument upstream of where the case file's analytical focus has been to date. The [Westmeath / Waltham gauge install proposal](../../docs/reports/2026-05-26_Westmeath_Waltham_Gauge_QC_install_proposal.md) is concerned with the reach immediately downstream of Des Joachims; the analogous instrument upstream of Des Joachims is already in place at Mattawa (WSC 02JB013), so the public-record gap at the upstream end of this same operating pattern is narrower than the gap downstream.

## Caveats

- Dan's account of the two-stage refill protocol at Otto Holden is **unverified against published time-series** in this note. The ORRPB Otto Holden trace once populated will let it be checked against the same Stage 1 / pause / Stage 2 signal documented at Des Joachims.
- The "Holden Lake / Lake la Cave" terminology for the Otto Holden head pond is **local usage**, not a formally named water body in the WSC station registry.
- Temiscaming is **not OPG**. It is operated by Brookfield Renewable (Energy Ottawa). Cascade coordination between Brookfield at Temiscaming and OPG at Otto Holden is governed by the same ORRPB framework that coordinates the rest of the cascade but is a separate operator-to-operator relationship from the Des Joachims to Carillon OPG-internal chain.
- This note attributes Dan Poole and Rudy Dyck at the same level of public engagement they brought to the thread, matching the precedent set in the [May 22 reservoir drawdown note](2026-05-22_reservoir_drawdown.md) and the [May 23 Pembroke comparison](2026-05-23_pembroke_2023_vs_2026.md), per repo [attribution policy](../../CONTRIBUTORS.md).

## Sources

- Dan Poole and Rudy Dyck thread, Northern Reservoirs / Ottawa River / Tourism / Wildlife / Flood Watch FB group, 2026-05-27.
- WSC station 02JB013 Ottawa River at Mattawa, RHBN, level-only, active.
- ORRPB Otto Holden location page at https://www.ottawariver.ca/location/otto-holden/, scheduled for daily ingest via the `orrpb-station-history` cron.
- OPG Otto Holden Generating Station operator metadata via OPG's public site.
- Brookfield Renewable Temiscaming operator metadata via Brookfield's public site.

## Related case-file material

- [Pembroke 2023 vs 2026 community note](2026-05-23_pembroke_2023_vs_2026.md), the Des Joachims two-stage refill signal documented downstream.
- [Pembroke Thread Synthesis](../../docs/analysis/Pembroke_Thread_Synthesis.md), the peak-time scheduling lever as the surviving variable across five FB-thread hypotheses.
- [Westmeath / Waltham gauge install proposal](../../docs/reports/2026-05-26_Westmeath_Waltham_Gauge_QC_install_proposal.md), the analogous downstream public-record gap (Mattawa has a gauge; Westmeath does not).
- [Chenaux FB thread analysis](2026-05-26_chenaux_thread.md), same cascade operator, different dam, same pattern of release timing as the operating lever.
