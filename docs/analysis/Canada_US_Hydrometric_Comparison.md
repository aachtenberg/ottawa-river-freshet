# Canada vs US hydrometric and climate monitoring — the public-data gap behind the Westmeath argument

**Case-file framing note**
**Compiled: 2026-05-25**

> **Why this note exists.** The freshet case file keeps bumping into
> missing or inaccessible datasets — the 1994 end-of-record cliff at
> Bryson / Chats Falls / Carillon, the decommissioned Westmeath stage
> gauge on the long Ottawa main-stem reach upstream of Carillon, the
> absence of a public operator-outflow schedule, the lack of a
> published rating curve at Lac Coulonge. Every time, the operator-
> side answer is some version of "that data isn't publicly available."
> This note documents why, by comparing the public observational
> infrastructure the US and Canadian governments built out over
> 2000–2026. It's the structural background against which the
> Westmeath-reinstall ask makes sense.

---

## Plain-language summary

The United States and Canada faced the same era — accelerating climate
risk, ageing rivers, growing flood costs — but they built out their
public-monitoring infrastructure on completely different funding
models, and the difference is visible on the ground.

In the US, federal law requires that streamflow data from federally
licensed hydroelectric dams enter a public administrative record, and
the country runs a federal climate-reference network purpose-built in
the 2000s for long-term climate detection. Asking *"what flow did this
dam release on April 15?"* is mostly a USGS API call.

In Canada, hydrometric stations are operated under a **cooperative
cost-recovery model** — every gauge needs a paying partner (a province,
a Conservation Authority, a dam operator, sometimes a municipality).
When the partner stops paying, the station dies. There is no Canadian
equivalent of the US Climate Reference Network. There is no Canadian
statute requiring publication of operational flow data at hydroelectric
dams. Crown utilities (Hydro-Québec, OPG, BC Hydro, Manitoba Hydro) do
publish some operational data, but voluntarily, on rolling windows,
with explicit "no quality guarantee" disclaimers, and without machine-
readable historical archives.

So the data-gap pattern the case file keeps hitting isn't an Ottawa-
basin quirk. It is the predictable equilibrium of a system where the
party that would benefit most from public data (the downstream
community, the citizen analyst, the regulator-of-record) is not the
party that decides whether public data gets collected.

This note is not a claim of bad faith on anyone's part. It's a
description of the funding architecture and disclosure regime that
keeps producing the same structural outcome, and a reference for
future case-file material that needs to anchor its "missing data"
argument in something other than rhetoric.

---

## Verified numbers (side by side)

| Category | United States | Canada |
|---|---|---|
| **Real-time streamgages** | ~8,700 (USGS NWIS, full network ~12,000 sites incl. stage-only) [^1] | ~2,100 real-time / ~2,900 total network / ~1,800 active discharge (WSC) [^2] |
| **Streamgage trajectory 2000–2020** | Network maintained at ~8,700 real-time, but with a documented **federal-priority shortfall** — Congress mandated ≥4,700 Federal Priority Streamgages by FY2019 under the SECURE Water Act of 2009; USGS reported only 3,470 operational in FY2020. Non-federal cost-share rose from ~50 % (early 1990s) to ~69 % (FY2020). [^3] | Net **contracted** in the mid-1990s under federal Program Review (Pilon et al. 1996 documented a 5.2 % / 363-station decline 1990–1996); partial recovery since the early 2000s (2,793 → 2,922 stations between 2016 and 2023). Network remains undersampled relative to the late-1980s peak. [^4] |
| **Climate-grade reference network** | **US Climate Reference Network (USCRN)** — 114 CONUS stations, prototype 2000, commissioned 2004, CONUS buildout completed 2008; ~116 operational with Hawaii; 29 Alaska stations still in deployment. Triple-redundant instruments, ungoverned-microclimate siting, weighing precipitation gauges. Purpose-built for climate-quality long-term monitoring. [^5] | **None.** Closest analog is the Reference Climate Stations (RCS) network (~300 stations, ~240 automated), selected from existing MSC stations for long records — but uses standard MSC instrumentation, not the triple-redundant, ungoverned-microclimate, climate-detection-grade design that defines USCRN. [^6] |
| **Surface meteorological network** | >900 ASOS stations (FAA/NWS automated); >10,000 COOP stations with ~8,500 active volunteer observers (NWS). [^7] | ~585 fully-automated MSC stations; ~560 stations with long homogenized records (AHCCD); ~71 stations in the GCOS Surface Network. [^8] |
| **Hydroelectric operator data — federal law on disclosure** | FERC eLibrary publishes all licensee filings (license applications, compliance reports, project studies). 18 CFR 4.41 requires streamflow data with applications. Real-time flow telemetry from FERC-licensed projects typically reaches the public via USGS streamgages whose costs are commonly **shared by the licensee under license conditions.** [^9] | **No statutory disclosure requirement.** Crown utilities publish operational data voluntarily, on rolling windows, with "no quality guarantee" disclaimers, without machine-readable historical archives: Hydro-Québec (10-day rolling, twice-daily refresh, 3-day lag in Nord-du-Québec / Côte-Nord); OPG (Water System Data Portal); BC Hydro (200+ stations, near-real-time, "subject to change"); Manitoba Hydro (daily averages, preliminary unverified). [^10] |

[^1]: USGS, "USGS Streamgages by the Numbers" — https://www.usgs.gov/mission-areas/water-resources/science/usgs-streamgages-numbers
[^2]: ECCC, "Canada Water Act Annual Report 2023–2024" — https://www.canada.ca/en/environment-climate-change/services/water-overview/publications/canada-water-act-2023-2024.html. Real-time subset per MSC open-data README — https://eccc-msc.github.io/open-data/msc-data/obs_hydrometric/readme_hydrometric_en/. Active-discharge subset per Hamilton et al. 2024 (HESS) — https://hess.copernicus.org/articles/28/4383/2024/.
[^3]: Congressional Research Service R45695, "Streamgages: Background and Issues for Congress" — https://www.everycrsreport.com/reports/R45695.html. Also USGS OFR 2023-1032 — https://pubs.usgs.gov/publication/ofr20231032/full.
[^4]: Pilon, P.J., et al. (1996) on the early-1990s contraction. Mishra & Coulibaly (2009/2010) on network adequacy — https://www.sciencedirect.com/science/article/abs/pii/S0022169409007240. Recovery trend from Canada Water Act Annual Reports series.
[^5]: NOAA NCEI, "US Climate Reference Network" — https://www.ncei.noaa.gov/products/land-based-station/us-climate-reference-network
[^6]: Mekis, É., et al. (2018), "Observed Trends in Precipitation Indicators … in Canada" — https://www.tandfonline.com/doi/full/10.1080/07055900.2018.1433627. Canadian GCOS National Report — https://unfccc.int/sites/default/files/resource/cangcose%20CAN%20e.pdf.
[^7]: NOAA NCEI ASOS — https://www.ncei.noaa.gov/products/land-based-station/automated-surface-weather-observing-systems. NWS COOP — https://www.weather.gov/coop/overview.
[^8]: Vincent et al. (2020), AHCCD third generation — https://www.tandfonline.com/doi/full/10.1080/07055900.2020.1765728. Mekis et al. (2018) for automated-station count.
[^9]: FERC eLibrary — https://www.ferc.gov/ferc-online/elibrary; 18 CFR 4.41 — https://www.ecfr.gov/current/title-18/chapter-I/subchapter-B/part-4/subpart-E/section-4.41.
[^10]: Hydro-Québec open hydrometric data — https://www.hydroquebec.com/documents-data/open-data/hydrometric-data/. OPG Water System Data Portal — https://www.opg.com/power-generation/our-power/hydro/water-system-data-portal/. BC Hydro — https://www.bchydro.com/energy-in-bc/operations/transmission/transmission-system/actual-flow-data.html. Manitoba Hydro — https://www.hydro.mb.ca/corporate/operations/water-levels/.
[^11]: ECCC, "Hydrometric program: a national partnership" — https://www.canada.ca/en/environment-climate-change/services/water-overview/quantity/monitoring/survey/hydrometric-program-national-partnership.html. The 1975-origin bilateral-agreement structure and the National Administrator's Table governance body are described here. Service-level obligations under those agreements are detailed in ECCC's "Hydrometric data and information service standards" — Chapter 2 (program structure and partner roles) https://www.canada.ca/en/environment-climate-change/services/meteorological-service-standards/publications/hydrometric-data-information/chapter-2.html and Chapter 3 (service levels) https://www.canada.ca/en/environment-climate-change/services/meteorological-service-standards/publications/hydrometric-data-information/chapter-3.html.
[^12]: ECCC, "Evaluation of the National Hydrological Services" — https://www.canada.ca/en/environment-climate-change/corporate/transparency/priorities-management/evaluations/national-hydrological-services.html (summative Treasury Board evaluation covering 2018–19 → 2021–22). The 1,144 fully-or-partially-federally-funded station figure is from this evaluation. The "at a glance" summary is at https://www.canada.ca/en/environment-climate-change/corporate/transparency/priorities-management/evaluations/national-hydrological-services/at-a-glance.html.

---

## Three structural causes

The differences in the table above are not accidents of budget cycles
or partisan turnover. They follow from three durable structural
features of how Canada funds and governs water-monitoring
infrastructure.

### 1. Cooperative cost-recovery funding model

WSC hydrometric stations are not funded out of a single federal budget
line. The **National Hydrometric Program** has been administered since
**1975** under bilateral hydrometric agreements between ECCC and each
provincial / territorial government, plus Crown–Indigenous Relations
and Northern Affairs Canada for Nunavut — 12 partner agreements in
total, governed through the **National Administrator's Table**. Each
station has a federal share and a partner share — provincial agency,
Conservation Authority, dam operator, municipality, sometimes more
than one — with cost-sharing apportioned "in accordance with each
party's need for the data." [^11] As of the most recent Treasury Board
evaluation (2018-19 → 2021-22), of the ECCC-operated stations, **only
1,144 are fully or partially federally funded** — the remainder are
operated by ECCC on behalf of provincial / territorial governments or
third-party partners. [^12] When a partner pulls out, the federal share
is rarely sufficient to keep the station running on its own, and the
gauge goes dark.

The mid-1990s contraction (Pilon et al. 1996 documented 363 stations /
5.2 % of the network lost between 1990 and 1996) maps onto the
federal **Program Review** of 1995–97, which forced cooperative
partners to renegotiate or exit, in a window where every level of
government was cutting budgets in parallel. The Ottawa basin in
particular shows a concentrated end-of-record cluster around 1993–94
in the HYDAT archive at stations downstream of Chats Falls / Bryson /
Carillon — a case-file observation, recoverable from a HYDAT scan but
not, to our knowledge, separately published as a regional study.

USGS funding is more directly federal, which makes it more stable but
also more politically visible when cuts come. The SECURE Water Act of
2009 created a **Federal Priority Streamgages** statutory minimum
(≥4,700 stations); FY2020 actuals were 3,470 — the shortfall is
public, congressionally tracked, and the subject of GAO and CRS
reports.

The key asymmetry isn't *amount of money*. It's that the US system
makes underfunding **legible** (a published shortfall against a
statutory floor), while the Canadian system makes underfunding
**invisible** (a station goes dark, a single line of metadata changes
in HYDAT, no one writes a report).

### 2. Constitutional fragmentation of water governance

Water management in Canada is provincial. CEHQ (Québec), MNRF
(Ontario), BC Environment, MELCC, Manitoba Sustainable Development —
each runs its own monitoring network with its own access policy. The
federal WSC/ECCC layer is partly redundant, partly complementary,
never unified. There is no single Canadian water-data API.

The US has more unified federal hydrometric data despite states' rights
because USGS sits federally and the FERC licensing framework operates
federally over the dams. The constitutional reality is that water *is*
federally regulated in the US for navigable rivers and federally
licensed dams, in a way it isn't in Canada.

For the case-file's purposes, this matters because Ottawa basin dams
sit across two provinces (Ontario and Québec) plus a federal-Crown
operator (Hydro-Québec). There is no single regulator who could be
asked to publish a unified flow record across all of them. The
fragmentation is the architecture.

### 3. No Canadian FERC-equivalent for hydroelectric operators

This is the single biggest difference for the Westmeath argument. In
the US, **18 CFR 4.41** requires that any application to FERC for a
hydroelectric license include streamflow data, and the entire FERC
docket (license applications, compliance reports, environmental
studies, post-licensing monitoring) is publicly accessible via FERC
eLibrary — no registration, no FOIA process. License conditions
commonly require that the licensee operate or cost-share a USGS
streamgage that publishes real-time flow to NWIS. So even for
privately-operated hydroelectric projects, the public has structural
visibility into operational decisions.

Canada has no equivalent statute. The Canada Water Act, the
International Joint Commission treaties, the provincial Water Acts,
the Crown-corporation enabling statutes — none of them require
publication of operational hydroelectric flow data. Crown utilities
publish what they choose to publish, when they choose to publish it,
with the disclaimers they choose to attach.

The four major Canadian crown hydro operators (Hydro-Québec, OPG, BC
Hydro, Manitoba Hydro) **do** publish operational data — that part of
the case-file framing was outdated and is corrected here. But the
publication regime has three structural features that distinguish it
from the FERC-USGS architecture:

- **Rolling windows, not archives.** Hydro-Québec's hydrometric open
  feed is a 10-day rolling window. There is no machine-readable
  historical archive of operational flow at Hydro-Québec dams.
- **No quality guarantee.** Every operator portal carries explicit
  "preliminary, subject to change, no quality guarantee" disclaimers.
  This is not unusual for raw telemetry — but in the US case, the
  ratified version of the same data lands in USGS NWIS within months,
  with quality control. In the Canadian case, there is no ratified
  public version.
- **Voluntary, not statutory.** The operator can change publication
  cadence, format, depth, or terms of use without notice and without
  legal consequence. There is no regulator who can compel restoration.

The Westmeath case study lives at the precise intersection of these
three features. The gauge (WSC 02KC005, at 45.895° N 76.912° W,
operated by Ontario Power Generation, stage-only record 1935-1995,
not in the federal Reference Hydrometric Basin Network) was
decommissioned (cooperative funding model collapse: OPG walked, no
RHBN-priority budget caught it). The province cannot reinstall it
unilaterally (constitutional fragmentation). And the operator whose
scheduling decisions would be constrained by it has no statutory
obligation to fund it (no FERC equivalent). All three structural
features point the same way: the absence of the gauge is the
equilibrium, not the anomaly.

The historical record is also instructive about what "reinstall"
would and would not buy us. Across 60 years (1935-1995), 02KC005
published level only, never discharge, so a literal reinstall under
its old terms would give stage, not flow. To make Westmeath useful
for operator-decision auditing, the reinstall needs to be paired
with a published rating-curve program (repeated ADCP boat surveys
across the flow range, with maintenance after every channel-shaping
flood). That second step is what the federal RHBN designation
historically funded at priority stations. Without it, even a
reinstalled Westmeath would be a level gauge in an "assumed datum",
useful for downstream-response inference but not directly comparable
to upstream operator releases.

---

## Why "climate awareness" didn't fix this

The natural follow-up question is: surely twenty years of growing
climate awareness should have moved this? It hasn't, and the reason is
clarifying.

Climate funding from roughly 2005 to 2025 in Canada flowed
overwhelmingly to four buckets: **modelling** (CMIP-style projections,
ensemble downscaling), **mitigation** (emissions reduction
infrastructure), **adaptation infrastructure** (flood walls,
stormwater retrofits, building-code updates), and **communication**
(public dashboards, school curricula). Long-term observational
networks were considered the existing departments' operational
responsibility — i.e., ECCC's and WSC's base budgets — which were
under repeated restraint pressure: Program Review (1995–97),
Conservative-era cuts (2012–15), and a series of restraint budgets
since.

There was, to our knowledge, **no Canadian climate-adaptation line
item dedicated to hydrometric station preservation or expansion** over
that twenty-year window. A less-cynical reading is that the climate-
research community moved its attention to **satellite and reanalysis
products** (GRACE, Sentinel, ERA5, CMIP archives) where Canada
participates internationally without ground-station maintenance.
Those products are excellent for global climate science and largely
useless for local flood operations, which need hour-by-hour discharge
at named cross-sections.

The US made the opposite choice. USCRN exists because the question
"how do we know the surface temperature record is real?" was answered
in the early 2000s by building a purpose-designed climate-detection
network out of NOAA-NCEI's institutional budget. That network now
publishes the most defensible surface-temperature record in the world.
Canada watched it happen and did not replicate.

---

## One-paragraph version for community / case-file use

> The United States built out climate-grade observational
> infrastructure during exactly the same period Canada was contracting
> hydrometric and climate-grade ground-station networks. The
> difference shows up most starkly at regulated-river segments where
> operational accountability matters most. In the US, the question
> *"did this dam pass 800 m³/s on April 15?"* can be answered with a
> USGS API call against a streamgage whose continued operation is
> often a FERC license condition cost-shared by the operator. In
> Canada, the same question requires scraping ORRPB daily PDFs,
> back-solving through downstream-gauge response, and — when the
> downstream gauge has been decommissioned and refused for reinstall,
> as at Westmeath — accepting that the public record cannot answer
> it. That is not an Ottawa-basin quirk. It is the design of a
> cost-recovery funding model with no statutory disclosure backstop.

---

## What this means for the case file

Three operational implications for case-file material:

1. **Anchor "missing data" arguments in the funding architecture, not
   in suppression language.** Hydro-Québec, OPG, and ECCC are not
   hiding the data. They are operating exactly as the cooperative
   cost-recovery model and voluntary-publication regime permit. The
   argument the case file should make is *the architecture itself is
   unfit for adaptive flood management in a changing climate*, not
   *they're withholding records*. The first claim is structural and
   defensible; the second is rhetorical and easy to dismiss.

2. **The Westmeath reinstall ask is structurally analogous to the
   USCRN-equivalent ask.** Both are "build a public observational
   instrument that the system, left to its own incentives, will not
   build." Both require political force above the partner-funding
   layer to succeed. Both fail in the same way (the level at which the
   decision is made cannot internalise the benefit), and both succeed
   in the same way (an external mandate with a budget line that
   bypasses the cost-recovery negotiation). The Westmeath argument is
   strongest when it's framed as a missing-statutory-instrument
   problem, not a missing-Westmeath problem.

3. **Private-stage-gauge installation is a tactical fit, not a
   substitute.** A private pressure-transducer stage gauge at
   Westmeath would generate uncalibrated but real-time evidence the
   operator cannot make go away by walking from a partnership. Its
   purpose is to make the absence of the federal-public instrument
   politically un-ignorable, not to replace it. The structural goal
   remains a FERC-equivalent disclosure regime — or, failing that, a
   WSC station reinstall with a federal-only budget line that does
   not depend on the operator agreeing to cost-share its own audit.

---

## Caveats and verification notes

- **Station counts are 2024–2026 best-available figures.** Methods of
  counting (active vs network vs real-time vs continuous discharge)
  differ between WSC and USGS and the published numbers reflect those
  definitions. The table above uses the most-conservative-comparable
  definition where available; specific subsets are footnoted.
- **The 1994 Ottawa-basin cluster** is presented as a case-file
  observation recoverable from HYDAT, not an externally peer-reviewed
  finding. A clean published treatment would require a full HYDAT
  end-of-record scan limited to drainage areas 02J/02K/02L. The
  pattern is consistent with Pilon et al. 1996's national finding for
  the same period; tighter local replication is a worthwhile
  follow-up.
- **The "no statute requires disclosure" claim** is defensible at the
  federal level for hydroelectric flow data. Provincial water-quality
  reporting statutes (e.g., Ontario Safe Drinking Water Act, Québec
  Loi sur la qualité de l'environnement) do require *some* publication
  in specific contexts (drinking-water source protection, environmental
  assessment), but none of them generates a continuous public record
  of operational flow at hydroelectric dams.
- **"USGS net-added"** as a streamgage claim is **incorrect** and the
  original case-file framing has been corrected. The defensible
  contrast is: US streamgage network *maintained at ~8,700 real-time
  sites against a published federal-priority shortfall*; Canadian
  network *contracted in mid-1990s, partially recovered since 2000*.
  The genuine US net-add over this period is on the climate side
  (USCRN, 2002–2008), which has no Canadian counterpart at all.

---

## Sources

The footnoted citations above are the load-bearing ones. The
following are useful for further context:

- WSC HYDAT bulk download — https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/
- USGS NWIS Web Services — https://waterservices.usgs.gov/
- ORRPB conditions page (the regional regulator) — https://www.ottawariver.ca/
- Hydro-Québec open data portal landing — https://www.hydroquebec.com/documents-data/open-data/
- ECCC MSC Open Data — https://eccc-msc.github.io/open-data/
- ORFA, *Eight Ways to End the Super Floods* (2025) — the policy frame
  this note supplies the structural background for.

---

*Related case-file material:* the [Pembroke FB thread
synthesis](Pembroke_Thread_Synthesis.md) describes how the absence of
a Westmeath stage gauge in the long Ottawa reach upstream of Carillon
is the load-bearing data gap for the 2023-vs-2026 attribution
question. The [Freshet 2026 Complete
Summary](Freshet_2026_Complete_Summary.md) describes how the broader
case-file argument depends on inferences that would not be necessary
under a US-style disclosure regime.
