# Des Joachims summer cycling is real: hourly ORRPB data confirms daily 0 to ~1,000 m³/s generation cycles and ~0.1 m Pembroke level swings

**Compiled 2026-07-23 in response to Dan's "Is the Ottawa River cycling?" infographic post in the Facebook group. First note to use the ORRPB hourly station export (table view, hourly data type), which resolves questions the daily series cannot answer.**

## Plain language summary

Dan's post to the group claims that the Rapides-des-Joachims generating station peaked at 3,380 m³/s on April 30, that it now runs a controlled day/night cycle of roughly 1,000 m³/s during daytime demand and near zero overnight, averaging just under 400 m³/s over 24 hours, and that Pembroke-area water levels swing at times by up to approximately 0.10 m within a day. All three claims check out against the ORRPB public record, and the third one is slightly conservative.

The hourly data shows the station shutting its discharge to literally 0 m³/s for several overnight hours every day in mid-July, then ramping to daytime and evening peaks of roughly 700 to 1,100 m³/s. Pembroke's level breathes in antiphase with that cycle, rising overnight and sagging mid-morning, by 7 to 14 cm per day. This is normal summer peaking operation at low flows, not a flood signal: Pembroke is sitting more than 2 m below its 2017, 2019, and 2023 flood peaks.

For the case file, this note also establishes something methodological: OPG's Des Joachims operation is invisible in the daily series (which just shows a smooth decline to ~390 m³/s), but the hourly export reveals full on/off peaking. Daily averages hide operating behavior.

## Claim 1: freshet peak of 3,380 m³/s on April 30

Confirmed. The ORRPB hourly discharge series for Des Joachims shows the seasonal maximum on exactly April 30, 2026:

| Date | Hourly max (m³/s) | Daily mean (m³/s) |
|---|---|---|
| 2026-04-28 | 3,260 | 3,145 |
| 2026-04-29 | 3,298 | 3,232 |
| 2026-04-30 | **3,393** (16:00) | **3,324** |
| 2026-05-01 | 3,372 | 3,266 |
| 2026-05-02 | 3,269 | 3,219 |

The infographic's 3,380 sits inside April 30's hourly envelope. It is an instantaneous figure, not the daily mean, and the date is right.

## Claim 2: daily cycling, ~1,000 daytime, near zero overnight, ~390 average

Confirmed, and the overnight claim is understated: the station does not go "near zero", it goes to zero. Daily aggregates of the hourly discharge series, July 17 to 23:

| Date | Overnight min (m³/s) | Daytime max (m³/s) | Daily mean (m³/s) |
|---|---|---|---|
| 2026-07-17 | 0 | 956 | 448 |
| 2026-07-18 | 0 | 1,071 | 420 |
| 2026-07-19 | 0 | 949 | 406 |
| 2026-07-20 | 0 | 746 | 391 |
| 2026-07-21 | 0 | 690 | 351 |
| 2026-07-22 | 0 | 963 | 390 |

The July 18 to 22 mean is 391 m³/s, matching the claimed 390. Three of the six days exceeded 950 m³/s at peak, so "up to ~1,000 m³/s" is fair. A representative day (July 21) ran about 144 m³/s through the pre-dawn hours, stepped up through 430 m³/s midday to a 690 m³/s late-afternoon peak, then cut to 0 by late evening.

Two caveats. First, the daily ORRPB flow table showed 0 for July 23 when compiled; that is a partial-day artifact (only 11 hours of hourly data were in), not a shutdown, and is consistent with the known behavior of ORRPB's preliminary latest day. Second, hour labels are as published on the ORRPB station pages (Eastern Time); the on/off phasing aligns with daytime demand as the infographic describes.

## Claim 3: Pembroke levels varying up to 0.10 m per day

Confirmed, slightly conservative. Intra-day ranges from the hourly Pembroke level series:

| Date | Daily low (m) | Daily high (m) | Intra-day range |
|---|---|---|---|
| 2026-07-17 | 111.07 (11:00) | 111.19 (00:00) | 0.12 m |
| 2026-07-18 | 111.07 (09:00) | 111.21 (23:00) | 0.14 m |
| 2026-07-19 | 111.08 (10:00) | 111.21 (00:00) | 0.13 m |
| 2026-07-20 | 111.06 (08:00) | 111.16 (00:00) | 0.10 m |
| 2026-07-21 | 111.07 (06:00) | 111.14 (22:00) | 0.07 m |
| 2026-07-22 | 111.03 (08:00) | 111.13 (01:00) | 0.10 m |

The daily low lands mid-morning and the high near midnight, in antiphase with the generation cycle upstream: the reach drains down while turbines run through the day and refills overnight while discharge is 0.

The swing attenuates moving downstream through the lakes. The Lac Coulonge property gauge (Vigilance station 1195, hourly) showed intra-day ranges of only 0.011 to 0.048 m over the same July 17 to 23 window. A 7 to 14 cm daily oscillation at Pembroke arrives at Lac Coulonge as 1 to 5 cm.

## Not a flood signal

Pembroke's mid-July 2026 level of roughly 111.03 to 111.21 m sits far below its flood-year peaks: 113.03 m in 2017, 113.69 m in 2019, 113.31 m in 2023 (ORRPB historic peaks compilation in the case-file data set). The cycling described here is a low-water phenomenon: when total river flow is small, a generating station's daily schedule becomes the dominant signal in the water level. The infographic frames it the same way, and that framing is correct.

## Why this matters for the case file

1. **OPG stations run full on/off peaking in summer.** Des Joachims discharge goes to 0 m³/s overnight, daily. The daily-mean series (a smooth ~390 m³/s) completely hides this. Any operating-behavior claim sourced only from daily data understates what operators actually do within a day.
2. **The hourly export is the instrument that shows it.** The ORRPB station pages publish hourly tables behind the filter form (table view, hourly data type). Our ingesters currently scrape only daily values; extending them would make cycling behavior visible in the dashboard and DB.
3. **Community posts citing specific numbers can be adjudicated quickly.** All three quantitative claims in this infographic reproduced against the public record within rounding. That is worth saying publicly; it builds the norm that numbers posted to the group get checked and confirmed rather than argued from vibes.

## Source and methodology

- The post under adjudication: Dan's "Is the Ottawa River cycling?" infographic, Facebook flood watch group, July 2026 (https://www.facebook.com/share/p/1BfcMhq8vZ/).
- Des Joachims discharge and Pembroke level: ORRPB station pages (https://www.ottawariver.ca/location/des-joachims/?type=discharges and https://www.ottawariver.ca/location/pembroke/), hourly table view retrieved 2026-07-23 via the pages' filter form (POST with `data-display=table`, `data-type=hourly`, date window 2026-07-17 to 2026-07-24, and 2026-04-28 to 2026-05-03 for the peak check).
- Daily flow cross-check: `orrpb_river_flows?station=eq.des-joachims` from the cluster PostgREST tier (agency OPG for July, "ORRPB scrape" for April).
- Lac Coulonge attenuation: Vigilance station 1195 hourly levels, `river_readings?station_id=eq.1195`, July 17 to 23, 2026.
- Historic Pembroke peaks: `data/orrpb-historic-peaks-1972-2025.csv` (ottawa-river-freshet repo).
- Note that Des Joachims is OPG-operated and therefore absent from the Hydro-Québec `dam_releases` feed; ORRPB is the only public source for its discharge.
- ORRPB asserts its data "may not be reproduced or redistributed." This note presents derived per-day statistics (minima, maxima, means, ranges) rather than the raw hourly tables, and cites ORRPB as the source.

## Related case-file material

- [Rolphton / Mattawa FB tangent](2026-05-27_rolphton_mattawa_thread.md): earlier note identifying the Des Joachims two-stage refill pattern and basin-wide OPG operating protocol
- [Pembroke 2023 vs 2026](2026-05-23_pembroke_2023_vs_2026.md): prior Pembroke adjudication using the daily series
- [Summer predictability regime](2026-07-10_summer_predictability_regime.md): companion low-flow-season analysis at Britannia
