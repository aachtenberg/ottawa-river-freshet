# CanSWE — Canadian historical Snow Water Equivalent database

`CanSWE-CanEEN_1928-2025_v8.nc` — the v8 release of the Canadian historical
Snow Water Equivalent database (CanSWE), Vionnet et al., *Earth System Science
Data* (2021). Manual snow surveys + automatic snow pillows + passive-gamma SWE
sensors run by provincial/territorial agencies, utilities (OPG, Hydro-Québec,
…), and the Meteorological Service of Canada. 2963 stations × 35,642 daily
timesteps (1928–2025); `snw` is water equivalent of snow cover in kg m⁻² (= mm).

**Source / licence:** Federated Research Data Repository, DOI
`10.20383/103.0329` — distributed under the Open Government Licence — Canada.
FRDR's download is via Globus, so this file is committed here for reproducibility
of the ingest (it's the canonical input the `swe-canswe-bootstrap` Job pulls).

**Use:** [`ingesters/swe-ingest/canswe_ingest.py`](../../ingesters/swe-ingest/canswe_ingest.py)
loads the Ottawa-basin subset into `swe_daily` (source `canswe`) +
`swe_locations`. It's a one-shot loader, not a cron — when a new CanSWE version
drops, download it from FRDR, drop it here, point the ingester at it, and re-run
(merge-duplicates upserts make a re-run idempotent). The cluster runs it via the
suspended `swe-canswe-bootstrap` CronJob (`k3s/base/data/swe-canswe-bootstrap.yml`),
which `curl`s this file from the public mirror.
