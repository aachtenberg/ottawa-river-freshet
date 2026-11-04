CREATE TABLE IF NOT EXISTS river_readings (
  time        timestamptz   NOT NULL,
  station_id  integer       NOT NULL,
  level_m     double precision NOT NULL,
  flow_cms    double precision,
  PRIMARY KEY (station_id, time)
);

SELECT create_hypertable('river_readings', 'time', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS river_readings_station_time_idx
  ON river_readings (station_id, time DESC);

CREATE TABLE IF NOT EXISTS river_stations (
  station_id   integer PRIMARY KEY,
  label        text,
  description  text,
  water_body   text,
  provider     text,
  updated_at   timestamptz DEFAULT now()
);

-- Upstream weather observations (open-meteo reanalysis).
-- Used for freshet correlation — e.g. "did N freeze nights at Val-d'Or
-- correlate with a capped peak at Lac Coulonge?". Station is a stable slug
-- ('val-dor', 'pembroke', ...) rather than a numeric id so new stations can
-- be added without coordinating ids with upstream sources.
CREATE TABLE IF NOT EXISTS weather_observations (
  time        timestamptz NOT NULL,
  station     text        NOT NULL,
  temp_c      double precision,
  precip_mm   double precision,
  PRIMARY KEY (station, time)
);

SELECT create_hypertable('weather_observations', 'time', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS weather_observations_station_time_idx
  ON weather_observations (station, time DESC);

-- Reservoir readings (Ottawa River basin). Source: daily scrape of
-- ottawariver.ca/conditions/?display=reservoir, which publishes an 8-day
-- rolling window. reservoir_id is a stable slug ('dozois', 'baskatong',
-- 'timiskaming', ...) — see k3s/base/data/files/reservoir-ingest/scrape.py
-- for the ORRPB-label → slug mapping.
CREATE TABLE IF NOT EXISTS reservoir_readings (
  time          timestamptz NOT NULL,
  reservoir_id  text        NOT NULL,
  level_m       double precision,
  flow_cms      double precision,
  agency        text,
  source        text NOT NULL DEFAULT 'orrpb',
  PRIMARY KEY (reservoir_id, time)
);

SELECT create_hypertable('reservoir_readings', 'time', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS reservoir_readings_id_time_idx
  ON reservoir_readings (reservoir_id, time DESC);

-- Latest reading per reservoir — convenience view for the dashboard.
CREATE OR REPLACE VIEW latest_reservoir_readings AS
SELECT DISTINCT ON (reservoir_id)
  reservoir_id, time, level_m, flow_cms, agency
FROM reservoir_readings
ORDER BY reservoir_id, time DESC;

-- Hydro-Québec generating-station release telemetry.
-- Source: Donnees_VUE_CENTRALES_ET_OUVRAGES.json (~10 days hourly per pull,
-- public open-data feed referenced from hydroquebec.com/production/debits-niveaux-eau.html).
-- site_id is HQ's stable identifier ('3-46' = Bryson, '3-60' = Carillon, etc.).
CREATE TABLE IF NOT EXISTS dam_releases (
  time           timestamptz NOT NULL,
  site_id        text        NOT NULL,
  total_cms      double precision,
  turbined_cms   double precision,
  spilled_cms    double precision,
  PRIMARY KEY (site_id, time)
);

SELECT create_hypertable('dam_releases', 'time', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS dam_releases_site_time_idx
  ON dam_releases (site_id, time DESC);

-- Daily filtered local incremental inflows for each HQ generating station
-- (apport filtré). Distinct from dam_releases because cadence differs.
CREATE TABLE IF NOT EXISTS dam_inflows (
  time         timestamptz NOT NULL,
  site_id      text        NOT NULL,
  inflow_cms   double precision,
  PRIMARY KEY (site_id, time)
);

SELECT create_hypertable('dam_inflows', 'time', if_not_exists => TRUE);

-- Hydro-Québec basin water-level stations.
-- Source: Donnees_VUE_STATIONS_ET_TARAGES.json. station_id is HQ's identifier
-- ('1-2964' = Bryson amont / headpond, '1-2965' = Bryson aval / tailwater, etc.).
-- Filtered to Ottawa basin (lat 45-48, lon -80 to -74) by the ingester.
CREATE TABLE IF NOT EXISTS dam_levels (
  time         timestamptz NOT NULL,
  station_id   text        NOT NULL,
  level_m      double precision,
  PRIMARY KEY (station_id, time)
);

SELECT create_hypertable('dam_levels', 'time', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS dam_levels_station_time_idx
  ON dam_levels (station_id, time DESC);

-- Combined metadata for HQ centrales and stations.
CREATE TABLE IF NOT EXISTS dam_sites (
  site_id      text PRIMARY KEY,
  nom          text,
  kind         text,             -- 'centrale' | 'station'
  region       text,
  region_code  text,
  lat          double precision,
  lon          double precision,
  date_debut   date,
  date_fin     date,
  updated_at   timestamptz DEFAULT now()
);

CREATE OR REPLACE VIEW latest_dam_releases AS
SELECT DISTINCT ON (site_id)
  site_id, time, total_cms, turbined_cms, spilled_cms
FROM dam_releases
ORDER BY site_id, time DESC;

CREATE OR REPLACE VIEW latest_dam_levels AS
SELECT DISTINCT ON (station_id)
  station_id, time, level_m
FROM dam_levels
ORDER BY station_id, time DESC;

-- Water Survey of Canada real-time hydrometric readings.
-- Source: wateroffice.ec.gc.ca/services/real_time_data/csv/inline endpoint.
-- station_code is the WSC alphanumeric (e.g. '02KF005' = Ottawa River at Britannia).
-- Why a separate table from river_readings: WSC publishes both level AND
-- discharge (Vigilance often only level), at 5-minute cadence (vs Vigilance's
-- hourly), and the station-id space is alphanumeric (vs Vigilance's integer).
CREATE TABLE IF NOT EXISTS wsc_readings (
  time          timestamptz NOT NULL,
  station_code  text        NOT NULL,
  level_m       double precision,
  flow_cms      double precision,
  PRIMARY KEY (station_code, time)
);

SELECT create_hypertable('wsc_readings', 'time', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS wsc_readings_station_time_idx
  ON wsc_readings (station_code, time DESC);

CREATE OR REPLACE VIEW latest_wsc_readings AS
SELECT DISTINCT ON (station_code)
  station_code, time, level_m, flow_cms
FROM wsc_readings
ORDER BY station_code, time DESC;

-- Hourly continuous aggregate over wsc_readings.
-- The Tributaries tab needs ~30 days of sparkline data per station; the raw
-- table is 5-minute resolution (8.6K rows per station for 30d), which makes
-- the multi-station fetch CPU-bound on postgrest and clogs Chart.js. This CA
-- pre-materializes hourly means, cutting the row count 12× while preserving
-- enough detail to see freshet pulses.
CREATE MATERIALIZED VIEW IF NOT EXISTS wsc_readings_hourly
WITH (timescaledb.continuous) AS
SELECT
  station_code,
  time_bucket('1 hour', time) AS time,
  AVG(level_m)  AS level_m,
  AVG(flow_cms) AS flow_cms
FROM wsc_readings
GROUP BY station_code, time_bucket('1 hour', time)
WITH NO DATA;

SELECT add_continuous_aggregate_policy('wsc_readings_hourly',
  start_offset      => INTERVAL '3 days',
  end_offset        => INTERVAL '30 minutes',
  schedule_interval => INTERVAL '30 minutes',
  if_not_exists     => TRUE);

-- Same pattern for river_readings, which is hourly-ish from Vigilance.
-- The hourly CA is mostly a passthrough but standardizes the schema and
-- gives the dashboard a stable view to query regardless of source cadence.
CREATE MATERIALIZED VIEW IF NOT EXISTS river_readings_hourly
WITH (timescaledb.continuous) AS
SELECT
  station_id,
  time_bucket('1 hour', time) AS time,
  AVG(level_m)  AS level_m,
  AVG(flow_cms) AS flow_cms
FROM river_readings
GROUP BY station_id, time_bucket('1 hour', time)
WITH NO DATA;

SELECT add_continuous_aggregate_policy('river_readings_hourly',
  start_offset      => INTERVAL '3 days',
  end_offset        => INTERVAL '30 minutes',
  schedule_interval => INTERVAL '30 minutes',
  if_not_exists     => TRUE);

-- ECCC Climate Data daily observations.
-- Source: api.weather.gc.ca / climate.weather.gc.ca CSV exports.
-- station_id is the ECCC numeric identifier (e.g. 4337 = Maniwaki).
-- Used for snow water equivalent + precipitation correlation against the
-- freshet peak. Distinct from open-meteo weather_observations which carries
-- modelled / reanalysis data; ECCC is the official Canadian observation network.
CREATE TABLE IF NOT EXISTS eccc_climate_daily (
  time         date NOT NULL,
  station_id   integer NOT NULL,
  station_name text,
  max_temp_c   double precision,
  min_temp_c   double precision,
  mean_temp_c  double precision,
  total_precip_mm    double precision,
  total_rain_mm      double precision,
  total_snow_cm      double precision,
  snow_on_ground_cm  double precision,
  PRIMARY KEY (station_id, time)
);

SELECT create_hypertable('eccc_climate_daily', 'time', if_not_exists => TRUE,
  chunk_time_interval => INTERVAL '1 year');

CREATE INDEX IF NOT EXISTS eccc_climate_daily_station_time_idx
  ON eccc_climate_daily (station_id, time DESC);

-- Snow water equivalent (mm), daily, Ottawa River basin.
-- Distinct from eccc_climate_daily.snow_on_ground_cm (that's snow *depth* at a
-- handful of ECCC stations; SWE = depth x density and is the hydrologically
-- meaningful quantity for predicting freshet runoff). region is either a named
-- sampling point ('temiscaming', 'maniwaki', ...) for gridded point-samples, a
-- sub-basin slug ('upper-ottawa', 'gatineau', ...) or 'basin-total' for area
-- means, or an in-situ station id. source distinguishes the feed:
--   'caldas-nsrps' — ECCC GeoMet CaLDAS-NSRPS 2.5 km operational SWE analysis,
--                    sampled at named points (current-analysis only; archive
--                    builds forward from when ingest started).
--   'era5land'     — Copernicus ERA5-Land snow_depth_water_equivalent, basin
--                    bbox mean, daily, ~5-day lag, history back to 1950.
--   'canswe'       — in-situ snow course / pillow SWE (Vionnet et al. CanSWE).
-- See k3s/base/data/files/swe-ingest/ for the ingesters.
CREATE TABLE IF NOT EXISTS swe_daily (
  time        date NOT NULL,
  region      text NOT NULL,
  source      text NOT NULL,
  swe_mm      double precision,
  swe_dep_mm  double precision,        -- departure from normal, mm (NULL unless the source provides it)
  PRIMARY KEY (region, source, time)
);

SELECT create_hypertable('swe_daily', 'time', if_not_exists => TRUE,
  chunk_time_interval => INTERVAL '1 year');

CREATE INDEX IF NOT EXISTS swe_daily_region_time_idx
  ON swe_daily (region, source, time DESC);

-- Metadata for swe_daily regions that are geographic points / sub-basins.
-- Upserted by the ingesters (cf. dam_sites). In-situ station regions may or
-- may not have a row here depending on whether the source supplies coordinates.
CREATE TABLE IF NOT EXISTS swe_locations (
  region      text PRIMARY KEY,
  name        text,
  kind        text,             -- 'point' | 'subbasin' | 'basin' | 'station'
  subbasin    text,             -- sub-basin slug this region rolls up into (NULL for 'basin')
  lat         double precision,
  lon         double precision,
  source      text,             -- the feed that defined this region
  updated_at  timestamptz DEFAULT now()
);

CREATE OR REPLACE VIEW latest_swe_daily AS
SELECT DISTINCT ON (region, source)
  region, source, time, swe_mm, swe_dep_mm
FROM swe_daily
ORDER BY region, source, time DESC;

-- ORRPB "Average Daily Flows (m3/s)" — main-stem Ottawa River discharge at the
-- monitored points: Temiscaming, Otto Holden, Des Joachims, Chenaux, Chats
-- Falls, Britannia, Carillon. Source: daily scrape of
-- ottawariver.ca/conditions/?display=river (8-day rolling window). `station` is
-- a stable slug ('des-joachims', 'otto-holden', ...). These are river flows ≈
-- the run-of-river dam releases at those structures — useful because the OPG
-- main-stem dams (Otto Holden, Des Joachims, Chenaux, Chats Falls) are not in
-- the Hydro-Québec open-data feed (dam_releases). See
-- k3s/base/data/files/orrpb-river-ingest/ingest.py.
CREATE TABLE IF NOT EXISTS orrpb_river_flows (
  time        date NOT NULL,
  station     text NOT NULL,
  flow_cms    double precision,
  agency      text,
  PRIMARY KEY (station, time)
);

SELECT create_hypertable('orrpb_river_flows', 'time', if_not_exists => TRUE,
  chunk_time_interval => INTERVAL '1 year');

CREATE INDEX IF NOT EXISTS orrpb_river_flows_station_time_idx
  ON orrpb_river_flows (station, time DESC);

CREATE OR REPLACE VIEW latest_orrpb_river_flows AS
SELECT DISTINCT ON (station)
  station, time, flow_cms, agency
FROM orrpb_river_flows
ORDER BY station, time DESC;

-- ORRPB "Water levels at 24:00h in metres" — main-stem Ottawa River 24:00h
-- water-surface elevation at the 12 monitored points: Otto Holden, Mattawa,
-- Des Joachims, Pembroke, Lake Coulonge, Chenaux, Chats Lake, Britannia,
-- Gatineau, Thurso, Grenville, Carillon. Source: daily scrape of
-- ottawariver.ca/conditions/ (default ?display, 8-day rolling window).
-- Distinct from river_readings (CEHQ Vigilance live, hourly, 4 stations
-- overlap) because the ORRPB table is the only public source for OPG-dam
-- headwater elevations (Otto Holden, Des Joachims, Chenaux, Chats Lake,
-- Carillon — none on CEHQ Vigilance) and is what the public-facing
-- "Ottawa River Water Levels" community chart matches.
-- Sibling of orrpb_river_flows; same ingester populates both. See
-- k3s/base/data/files/orrpb-river-ingest/ingest.py.
CREATE TABLE IF NOT EXISTS orrpb_river_levels (
  time        date NOT NULL,
  station     text NOT NULL,
  level_m     double precision,
  agency      text,
  PRIMARY KEY (station, time)
);

SELECT create_hypertable('orrpb_river_levels', 'time', if_not_exists => TRUE,
  chunk_time_interval => INTERVAL '1 year');

CREATE INDEX IF NOT EXISTS orrpb_river_levels_station_time_idx
  ON orrpb_river_levels (station, time DESC);

CREATE OR REPLACE VIEW latest_orrpb_river_levels AS
SELECT DISTINCT ON (station)
  station, time, level_m, agency
FROM orrpb_river_levels
ORDER BY station, time DESC;

-- ORRPB per-station historical-record table. Each (station, metric, date)
-- row carries the four series ORRPB publishes on its /location/<slug>/
-- pages: current-year observed, 1991-2020 daily median (P50), per-day
-- historic high with year tag, per-day historic low with year tag.
-- Window is ~13 months rolling. Populated by the orrpb-station-history
-- scraper which POSTs to /location/<slug>/ with table-view form params.
-- Source: k3s/base/data/files/orrpb-station-history/scrape.py
-- Note: the per-station "discharges" series can mean turbined-only flow
-- at some dam sites (e.g. chenaux) and total main-stem flow at others
-- (e.g. chats-falls, des-joachims). Cross-check against orrpb_river_flows
-- when total flow is what you need.
CREATE TABLE IF NOT EXISTS orrpb_station_history (
  time                  date NOT NULL,
  station               text NOT NULL,
  metric                text NOT NULL,   -- 'level_m' or 'flow_cms'
  observed              double precision,
  median                double precision,
  historic_high_value   double precision,
  historic_high_year    smallint,
  historic_low_value    double precision,
  historic_low_year     smallint,
  PRIMARY KEY (station, metric, time)
);

SELECT create_hypertable('orrpb_station_history', 'time', if_not_exists => TRUE,
  chunk_time_interval => INTERVAL '1 year');

CREATE INDEX IF NOT EXISTS orrpb_station_history_station_metric_time_idx
  ON orrpb_station_history (station, metric, time DESC);

CREATE OR REPLACE VIEW latest_orrpb_station_history AS
SELECT DISTINCT ON (station, metric)
  station, metric, time, observed, median,
  historic_high_value, historic_high_year,
  historic_low_value, historic_low_year
FROM orrpb_station_history
ORDER BY station, metric, time DESC;

-- Operating-limit rows from the "System Constraints" table on ORRPB's
-- /location/<slug>/ pages (principal reservoirs publish one; most river
-- stations do not). category is 'Operation' (all-year lower/upper limit),
-- 'Navigation' or 'Recreation' (seasonal, often lower-only). footnoted
-- means ORRPB printed a '*' beside a value. Refreshed every scrape
-- (OTTAW-28). Source: k3s/base/data/files/orrpb-station-history/scrape.py
CREATE TABLE IF NOT EXISTS orrpb_station_limits (
  station     text NOT NULL,
  category    text NOT NULL,
  period      text,
  lower_m     double precision,
  upper_m     double precision,
  footnoted   boolean NOT NULL DEFAULT false,
  scraped_at  timestamptz NOT NULL,
  PRIMARY KEY (station, category)
);

-- Usable storage of the 13 principal reservoirs, keyed by ORRPB /location/
-- slug. Source: ORRPB / ICOLD-Canada case study (2020), Table 1 -- the same
-- figures the dashboard's reservoir-limits.json carries. rapide-7 is the
-- gauge on Reservoir Decelles (impounded by the Rapide-7 dam), so Decelles'
-- 371 Mm3 sits under that slug. Total 12,515 Mm3. Rolled forward with
-- ON CONFLICT DO UPDATE so a corrected figure propagates. (OTTAW-28)
CREATE TABLE IF NOT EXISTS reservoir_capacity (
  station     text PRIMARY KEY,
  name        text NOT NULL,
  usable_mcm  double precision NOT NULL,
  source      text NOT NULL
);

INSERT INTO reservoir_capacity (station, name, usable_mcm, source) VALUES
  ('dozois',        'Dozois',                 1863, 'ICOLD-Canada 2020 Table 1'),
  ('rapide-7',      'Rapide-7 (Decelles)',     371, 'ICOLD-Canada 2020 Table 1 (Decelles)'),
  ('quinze',        'Quinze',                 1308, 'ICOLD-Canada 2020 Table 1'),
  ('lady-evelyn',   'Lady Evelyn',             308, 'ICOLD-Canada 2020 Table 1'),
  ('kipawa',        'Kipawa',                  673, 'ICOLD-Canada 2020 Table 1'),
  ('timiskaming',   'Timiskaming',            1217, 'ICOLD-Canada 2020 Table 1'),
  ('des-joachims',  'Des Joachims',            229, 'ICOLD-Canada 2020 Table 1'),
  ('bark-lake',     'Bark Lake',               374, 'ICOLD-Canada 2020 Table 1'),
  ('cabonga',       'Cabonga',                1565, 'ICOLD-Canada 2020 Table 1'),
  ('baskatong',     'Baskatong',              3049, 'ICOLD-Canada 2020 Table 1'),
  ('mitchinamecus', 'Mitchinamecus',           554, 'ICOLD-Canada 2020 Table 1'),
  ('kiamika',       'Kiamika',                 379, 'ICOLD-Canada 2020 Table 1'),
  ('poisson-blanc', 'Poisson Blanc',           625, 'ICOLD-Canada 2020 Table 1')
ON CONFLICT (station) DO UPDATE
  SET name = EXCLUDED.name, usable_mcm = EXCLUDED.usable_mcm, source = EXCLUDED.source;

-- Stage-storage shape for the proxy below. ORRPB does not publish per-
-- reservoir stage-storage curves, only an annual chart of total storage
-- (Spring Freshet Review, p.4). A reservoir's surface shrinks as it empties,
-- so volume is convex in level: fill_frac ** exponent, with one exponent
-- for the whole cascade, fitted to that chart by
-- scripts/orrpb-storage-proxy-calibrate.py. Single-row table so the
-- dashboard can show the provenance next to the number. (OTTAW-28)
CREATE TABLE IF NOT EXISTS reservoir_storage_proxy_calibration (
  id                smallint PRIMARY KEY DEFAULT 1 CHECK (id = 1),
  exponent          double precision NOT NULL,
  scale             double precision NOT NULL,
  fitted_on         date NOT NULL,
  reference         text NOT NULL,
  rmse_median_bcm   double precision,
  rmse_current_bcm  double precision
);

INSERT INTO reservoir_storage_proxy_calibration
  (id, exponent, scale, fitted_on, reference, rmse_median_bcm, rmse_current_bcm) VALUES
  (1, 1.3, 0.97, DATE '2026-11-04',
   'ORRPB 2026 Spring Freshet Review p.4 "Water stored in principal reservoirs", digitized; 1991-2020 median curve (275 d) and 2026 curve (108 d)',
   0.14, 0.16)
ON CONFLICT (id) DO UPDATE
  SET exponent = EXCLUDED.exponent, scale = EXCLUDED.scale, fitted_on = EXCLUDED.fitted_on,
      reference = EXCLUDED.reference, rmse_median_bcm = EXCLUDED.rmse_median_bcm,
      rmse_current_bcm = EXCLUDED.rmse_current_bcm;

-- Per-reservoir, per-day storage PROXY. fill_frac is the level's position in
-- the Operation band from orrpb_station_limits (clamped 0..1; fill_frac_raw
-- is unclamped so an overshoot stays visible). storage_mcm applies the
-- calibrated exponent and scale to the ICOLD usable capacity. median_* uses
-- ORRPB's 1991-2020 daily median level, giving a "normal" storage curve to
-- plot against. This is an estimate of ORRPB's chart, not a reproduction:
-- label it a proxy wherever it is shown. (OTTAW-28)
CREATE OR REPLACE VIEW reservoir_storage_proxy AS
WITH lim AS (
  SELECT station, lower_m, upper_m
  FROM orrpb_station_limits
  WHERE category = 'Operation' AND lower_m IS NOT NULL AND upper_m IS NOT NULL
    AND upper_m > lower_m
), cal AS (
  SELECT exponent, scale FROM reservoir_storage_proxy_calibration WHERE id = 1
), f AS (
  SELECT h.time, h.station, c.name, c.usable_mcm, l.lower_m, l.upper_m,
         h.observed AS level_m, h.median AS median_level_m,
         (h.observed - l.lower_m) / (l.upper_m - l.lower_m) AS fill_frac_raw,
         (h.median   - l.lower_m) / (l.upper_m - l.lower_m) AS median_fill_frac_raw
  FROM orrpb_station_history h
  JOIN reservoir_capacity c USING (station)
  JOIN lim l USING (station)
  WHERE h.metric = 'level_m'
), g AS (
  -- GREATEST/LEAST skip NULLs in PostgreSQL, so a NULL level would clamp to
  -- 0 (an "empty" reservoir) instead of staying unknown. Keep NULL as NULL so
  -- the total view's completeness gate sees it.
  SELECT f.*,
         CASE WHEN f.fill_frac_raw IS NULL THEN NULL
              ELSE LEAST(GREATEST(f.fill_frac_raw, 0), 1) END        AS fill_frac,
         CASE WHEN f.median_fill_frac_raw IS NULL THEN NULL
              ELSE LEAST(GREATEST(f.median_fill_frac_raw, 0), 1) END AS median_fill_frac
  FROM f
)
SELECT g.time, g.station, g.name, g.usable_mcm, g.lower_m, g.upper_m,
       g.level_m, g.median_level_m, g.fill_frac_raw, g.fill_frac, g.median_fill_frac,
       cal.scale * g.usable_mcm * power(g.fill_frac, cal.exponent)        AS storage_mcm,
       cal.scale * g.usable_mcm * power(g.median_fill_frac, cal.exponent) AS median_storage_mcm
FROM g CROSS JOIN cal;

-- Cascade total per day: the counterpart of ORRPB's chart. storage_mcm is
-- NULL unless every reservoir in reservoir_capacity has a level that day
-- (a partial sum would read as a drawdown). n_observed / n_reservoirs says
-- how complete the day is; n_with_limits < n_reservoirs means a reservoir
-- has no usable Operation band in orrpb_station_limits, which is why the
-- total is NULL every day (fix the limits scrape rather than the gate).
CREATE OR REPLACE VIEW reservoir_storage_proxy_total AS
WITH n AS (
  SELECT count(*)::int AS n_reservoirs,
         count(*) FILTER (WHERE EXISTS (
           SELECT 1 FROM orrpb_station_limits l
           WHERE l.station = c.station AND l.category = 'Operation'
             AND l.lower_m IS NOT NULL AND l.upper_m IS NOT NULL
             AND l.upper_m > l.lower_m))::int AS n_with_limits
  FROM reservoir_capacity c
)
SELECT p.time,
       count(p.storage_mcm)::int        AS n_observed,
       count(p.median_storage_mcm)::int AS n_median,
       n.n_with_limits,
       n.n_reservoirs,
       CASE WHEN count(p.storage_mcm) = n.n_reservoirs
            THEN sum(p.storage_mcm) END AS storage_mcm,
       CASE WHEN count(p.median_storage_mcm) = n.n_reservoirs
            THEN sum(p.median_storage_mcm) END AS median_storage_mcm
FROM reservoir_storage_proxy p CROSS JOIN n
GROUP BY p.time, n.n_with_limits, n.n_reservoirs;

NOTIFY pgrst, 'reload schema';
