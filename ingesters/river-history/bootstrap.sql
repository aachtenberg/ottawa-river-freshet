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

NOTIFY pgrst, 'reload schema';
