# Correction: the "mid-valley surge" in the August 5 daily brief was a data artifact

**Compiled 2026-08-06. Retraction and root-cause note for the automated daily brief of 2026-08-05, which led with a triple-flag "MID-VALLEY SURGE" alarm claiming flow at Des Joachims had nearly tripled in a day and that a wave could reach the Lac Coulonge property reach within 1 to 3 days. The finalized record shows there was no surge. This note documents what went wrong, why it was catchable the same night, and the guardrail added to the brief routine so this class of error does not recur.**

## Plain language summary

Yesterday's automated daily brief opened with an alarm: average flow at the Des Joachims Generating Station was reported at 995 cubic metres per second, up 164 percent from the day before, with Otto Holden up 113 percent, and a wave of extra water supposedly in transit toward the Fort-Coulonge and Mansfield shoreline.

That alarm was wrong. The numbers came from the river authority's current-day column, which shows a provisional partial-day figure, not a finished daily average. When the August 5 daily averages were finalized overnight, Des Joachims came in at 474 cubic metres per second (up 26 percent, an ordinary summer wiggle) and Otto Holden at 356 (up 2.6 percent, effectively unchanged). There was no wave, no tributary surge, and no water headed for the property reach that was not already accounted for.

The lake itself never noticed any of this, because there was nothing to notice. The property gauge at Fort-Coulonge has been flat to gently falling for a week and sits about 95 centimetres below the pre-alert threshold, in fully normal state. Nothing in the finalized record changes the quiet-summer picture.

The error was preventable with arithmetic available the same evening, and the automated brief routine has now been patched with a mandatory sanity check (described below) that must pass before any provisional flow figure can be escalated to a headline alarm, plus a mandatory next-day retro-check that issues a correction automatically if a headlined figure fails finalization.

## What the brief said, and what finalized

| Station | Aug 4 (final) | Aug 5 as headlined | Aug 5 (final) | Actual day-over-day |
|---|---|---|---|---|
| Des Joachims | 377 m³/s | 995 m³/s (+164%) | **474 m³/s** | **+26%** |
| Otto Holden | 347 m³/s | 740 m³/s (+113%) | **356 m³/s** | **+2.6%** |

The headlined figures were the ORRPB flow table's current-day values, read at roughly 15:00 EDT and described in the brief as running daily averages through that hour. As a further caution against reading that column literally: on the morning of August 6 the same current-day cells for both stations read 0, a placeholder, not a shutdown.

## Why this was catchable the same night

Four independent checks, all runnable before the brief was published, each of which refutes the surge:

1. **The arithmetic does not work.** If 995 m³/s really were the running average over the first 15 hours of the day, then for the day to finalize at 474 the remaining 9 hours would have to average (24 x 474 - 15 x 995) / 9 = **-394 m³/s**. Otto Holden works out to -284 m³/s. Rivers do not flow backwards through a generating station; the provisional figures were never valid daily averages. The forward-looking form of the same check: even if the river had stopped dead after 15:00, a true 15-hour mean of 995 would floor the final at (15/24) x 995 = 622 m³/s. The final of 474 sits far below that floor, so the 995 was arithmetically impossible as described, not merely revised.
2. **The hypothesized water source was checkable, and dry.** The brief attributed the extra ~640 m³/s to the Petawawa River and neighbouring tributaries responding to the August 2 to 3 rain. The Petawawa gauge (WSC 02KB001) was running about 30 m³/s, and still is.
3. **The station's own pool never moved.** The Des Joachims pool level went 152.22, 152.21, 152.19, 152.17 m across August 3 to 6: flat to gently falling through the claimed near-tripling. The brief's own reservoir table recorded this and even remarked on the contradiction ("pool level flat despite 995 m³/s daily avg") without reconciling it with the headline.
4. **Downstream flows fell while the "wave" was supposedly arriving.** Chenaux finalized August 5 at 645 m³/s and its August 6 provisional reads 570; Chats Falls went 809 to 576 (provisional). A real surge in transit does the opposite.

## Where the river actually stands (August 6)

- **The property reach is quiet.** Fort-Coulonge (Vigilance 1195) read 106.05 m at 9 AM Eastern, declining slowly and monotonically for about a day and a half, roughly 95 cm below the 107.00 m pre-alert threshold, flood state fully normal. Pembroke is sitting mid-band in its 10-day range; the small overnight uptick there is noise, not an arrival.
- **The one call the August 5 brief got right was Bryson.** The abrupt posture change it flagged (turbines cut to ~136 m³/s, spillway surged to ~341 m³/s, 71 percent spill share) has been sustained through this morning, and the headpond responded as predicted: 105.39 to 105.32 m, the first meaningful drawdown in weeks. The pond remains about 65 cm above its normal summer operating ceiling, day 70 of continuous exceedance.
- **The genuine flow increase in the basin is far downstream of the property.** Carillon, the basin-terminal dam, is passing roughly 2,100 m³/s and rising, but Britannia (upstream of it) accounts for only a fraction of the increase; most of the added water enters below Britannia from the Gatineau, Lievre, and Rouge systems, the delayed response to the August 2 to 3 rain, and the Gatineau stations are already easing. None of this reaches back upstream to the Lac Coulonge reach.
- **Témiscaming finalized August 5 at 318 m³/s**, the third consecutive day finalized below the provisional value the prior brief cited. The brief itself had flagged this systematic upward bias in provisional figures for Témiscaming, twice, and still built its headline on a provisional partial-day figure from the same table.

## The fix

The daily-brief routine prompt (`freshet-public/routines/freshet-daily-brief.md`) now carries a mandatory provisional-flow sanity check guardrail, alongside the verify-before-outage guardrail added after the May 5 false-outage incident. Before any day-over-day flow change of 25 percent or more resting on a current-day value can appear in the TL;DR or an escalated anomaly flag, the routine must run and pass all four checks above (feasibility back-out, mass balance against the actual tributary gauges, pool and level consistency, downstream response) and print the results next to the claim. Placeholder zeros are named for what they are. And every brief must now retro-check the previous day's headlined flow figures against finalized values, opening with an explicit correction if one fails.

## Source and methodology

- Daily average flows: `orrpb_river_flows` from the cluster PostgREST tier, retrieved 2026-08-06 (stations des-joachims, otto-holden, chenaux, chats-falls, temiscaming, britannia, carillon; agencies OPG, PSPC, WSC, HQ as recorded per row). August 6 values cited as provisional.
- Des Joachims pool level: `reservoir_readings?reservoir_id=eq.des_joachims` (ORRPB source rows, agency OPG).
- Petawawa River: `wsc_readings?station_code=eq.02KB001` (Water Survey of Canada real-time), 30.6 m³/s at 2026-08-06T12:35Z.
- Fort-Coulonge level: Vigilance station 1195, `river_readings?station_id=eq.1195`, 106.05 m at 2026-08-06T13:00Z.
- Bryson posture: Hydro-Québec open data via `dam_releases?site_id=eq.3-46` and `dam_levels?station_id=eq.1-2964`, current to 2026-08-06T09:00Z to 10:00Z.
- The retracted claims are quoted from `freshet-public/data/daily-briefs/2026-08-05.md` (automated brief, committed f7e23bd).
- Des Joachims and Otto Holden are OPG-operated and absent from the Hydro-Québec feed; the ORRPB tables are the only public source for their discharge. Per ORRPB's terms, this note presents derived statistics (daily means, deltas, implied-remainder arithmetic) rather than reproducing the raw tables, and cites ORRPB as the source.

## Related case-file material

- [Des Joachims summer cycling](2026-07-23_des_joachims_cycling.md): established that Des Joachims runs full on/off peaking in summer (0 to ~1,100 m³/s within a day), which is exactly why a partial-day running mean at this station is unrepresentative of the daily average, in either direction
- [Daily brief 2026-08-05](../daily-briefs/2026-08-05.md): the brief under correction
- The May 5 false-outage incident and its guardrail: `freshet-public/routines/freshet-daily-brief.md`, verify-before-declaring-outage section
