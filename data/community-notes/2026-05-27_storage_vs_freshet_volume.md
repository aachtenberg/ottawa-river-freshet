# 5.74 BCM of upper-basin storage against 5-45 BCM of freshet: when storage helps and when it can't

**Compiled 2026-05-27 in response to Stephen Depooter's substantive comment on the FB "Big Picture" thread, which independently arrives at the upper-basin storage figure that the case file pins to the ORRPB / ICOLD-Canada 2020 case study. Companion to [Carillon peaks + volume narrative](2026-05-27_carillon_peaks_volume_narrative.md) and to [Reservoir Drawdown community note](2026-05-22_reservoir_drawdown.md).**

## In one line

**The upper-basin reservoirs above Lac Temiskaming hold 5.74 BCM of usable storage. The Ottawa River's freshet through Carillon ranges from 8.8 to 45 BCM. That tells us when reservoir storage can help and when it cannot.**

## Stephen's claim is exact

Stephen, citing Dan Poole, gave the figure of "approximately 5.74B cubic metres of storage above Temiskaming dam, including the reservoirs upstream." Summing the usable-storage capacities from the authoritative source (ORRPB / ICOLD-Canada 2020 case study, Table 1) for the upper-basin reservoirs gives:

| Reservoir | Usable storage (MCM) |
|---|---|
| Dozois | 1,863 |
| Quinze | 1,308 |
| Timiskaming | 1,217 |
| Kipawa | 673 |
| Decelles (feeds Rapide-7) | 371 |
| Lady Evelyn | 308 |
| **Total** | **5,740 MCM = 5.74 BCM** |

Stephen's number is exact. Different calculation path, same authoritative source, same answer. That cross-check matters for the credibility of the framing.

For reference, the full Ottawa cascade including the Gatineau-Lievre-Madawaska tributary reservoirs (Cabonga, Baskatong, Mitchinamecus, Kiamika, Poisson Blanc, Bark Lake, Des Joachims) brings the total to 12.14 BCM of usable storage across all 13 principal reservoirs. The "5.74 BCM above Temiskaming" is the subset that affects the upper Ottawa main stem, including Lac Coulonge and the property.

## How that 5.74 BCM compares to the freshet

The 2000-2026 Carillon Apr-May-Jun freshet volume range from the [Carillon peaks + volume narrative](2026-05-27_carillon_peaks_volume_narrative.md) is:

| Year category | Volume (BCM) | 5.74 BCM as share |
|---|---|---|
| Smallest freshet (2010) | 8.8 | 65% |
| 27-year average | 23.7 | 24% |
| Largest freshet (2019) | 45.0 | 13% |

At Des Joachims (Stephen's reference station, further upstream), Steve Deon's data has freshet flows ranging 5 to 18 BCM, which is what Stephen cites. Against that range, 5.74 BCM is 32% to 100% of the freshet. Either reference point gives the same conclusion at both ends:

**In a small or average freshet, the upper-basin storage could capture a meaningful fraction (24% to 65%) of the total inflow, if perfectly timed.** That makes pre-freshet drawdown decisions consequential.

**In a large freshet like 2017 or 2019, the upper-basin storage holds 13% of the total water that has to pass.** No timing strategy can absorb the rest. The water must go through.

## The two-class flood model from the case file

The new exhibit's Figure 4 separates the four flood years 2017-2026 into two physically distinct classes based on where they sit in the peak-vs-volume scatter:

- **Volume-driven (on the trend line):** 2017 and 2019. Total water exceeded what the basin's storage could ever absorb. Peak followed volume. Storage was a small-fraction lever; even perfect timing would have shaved the peak by less than 1,000 cms.
- **Peakedness-driven (above the trend line):** 2023 and 2026. Total water was ordinary (16-30 BCM, against a 24 BCM average). The freshet was sharp rather than large. Storage of 5.74 BCM is 20-40% of the freshet, so the reservoirs could in principle have absorbed the inflow pulse while releasing at long-run average rate, shaving the peak meaningfully.

Stephen's operational framing maps directly onto this. He writes:

> "the dam operators need to know when to stop drawing down the dams, to enable the flow to actually exit the system, and not be held in a downstream reservoir, based on how much snow water equivalent they see in their drainage area."

That is exactly the operational lever the case file identifies. In volume-driven years (2017, 2019), the SWE forecast tells you the water is coming and there is no realistic storage strategy that prevents the peak. In peakedness-driven years (2023, 2026), the same SWE forecast plus a temperature forecast plus an inflow timing model would let operators shape the release schedule to absorb the peak rather than pass it through.

## Where this lands the regulatory question

Stephen, Steve Deon, Dan Poole, and Peter James have collectively assembled the quantitative argument that:

1. The cascade's storage is insufficient to buffer big-water years (2017, 2019). This is a physical fact, not an operator failure.
2. The cascade's storage is sufficient to shave sharp years (2023, 2026), provided operators are working from accurate SWE and rain forecasts and have permission to draw deeper than median.
3. The current operating practice (per the [Reservoir Drawdown community note](2026-05-22_reservoir_drawdown.md)) draws to median, not to the licensed floor. The licensed range is wider than the practiced range.

This is exactly the gap ORFA's *Eight Ways to End the Super Floods* Action 4 proposes to close, by writing snowpack-indexed drawdown requirements into the operating licences at the regulator level rather than asking individual operators to volunteer deeper drawdown.

## Method and sources

- **Storage capacities:** ORRPB / ICOLD-Canada case study (2020), Table 1, as encoded in `freshet-public/dashboard/reservoir-limits.json`. Direct source: https://ottawariver.ca/wp-content/uploads/2020/10/ICOLD-CANADA-CASE_STUDY_OTTAWA_RIVER_WATERSHED.pdf
- **Carillon freshet volumes:** computed in [Carillon peaks + volume narrative](2026-05-27_carillon_peaks_volume_narrative.md) from monthly mean flow x days, April-May-June.
- **Des Joachims freshet volumes:** Stephen attributes to Steve Deon's analysis posted to the same FB thread; case file has not independently verified the 5-18 BCM range but it is consistent with Carillon volumes (Des Joachims is roughly halfway up the basin so its freshet would be smaller).
- **Volume-driven vs peakedness-driven split:** Figure 4 of the Carillon peaks + volume narrative.

## Related material

- [Carillon peaks + volume narrative](2026-05-27_carillon_peaks_volume_narrative.md): the main exhibit
- [1970s precedent companion note](2026-05-27_1970s_precedent_for_recent_decade.md): why the recent decade is distinctive at the top tail, not at the body of the distribution
- [Reservoir Drawdown community note](2026-05-22_reservoir_drawdown.md): which reservoirs were drawn down in 2026, and which were not
- [Bryson No-Drawdown community note](2026-05-26_bryson_no_drawdown.md): the run-of-river-band-held-year-round case
- [Pre-freshet reservoir scout](../../ingesters/climate-history/pre_freshet_reservoir_scout.py): 36-year ORRPB archive analysis
