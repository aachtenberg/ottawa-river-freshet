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

NOTIFY pgrst, 'reload schema';
