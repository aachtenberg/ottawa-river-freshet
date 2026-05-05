---
trigger_id: trig_01Crnt5XxTEkpYYtKtZmkibT
name: freshet-mvca-ingest-health-check
schedule_kind: one_shot
run_once_at: "2026-06-11T13:00:00Z"
schedule_human: "Once at 2026-06-11 13:00 UTC (~6 weeks after deploy)"
environment: env_015L3icFtPvpzLnE2iJfyBRR
environment_name: aa-personal-cloud01
model: claude-sonnet-4-6
sources:
  - https://github.com/aachtenberg/homelab-infra
allowed_tools:
  - Bash
  - Read
  - Grep
  - Glob
mcp_connections:
  - name: Gmail
    connector_uuid: 3ac70ff0-439c-4512-ac42-954001e95c02
    url: https://gmailmcp.googleapis.com/mcp/v1
  - name: Google-Drive
    connector_uuid: 00eec8c7-229b-425b-9c18-0f29ba8b954d
    url: https://drivemcp.googleapis.com/mcp/v1
  - name: Indeed
    connector_uuid: 59a1dd4f-858f-443f-ab94-00bc7629844a
    url: https://mcp.indeed.com/claude/mcp
target_data: MVCA Buckhams Bay (KiWIS ts_id 48242042 → river_readings station_id 99001)
deploy_anchor: "2026-04-30 (35,665 rows in river_readings at deploy)"
---

<!--
This file is the source of truth for the freshet-mvca-ingest-health-check routine.
Everything below the closing `---` is the verbatim prompt that the agent runs.
See freshet-public/routines/README.md for how to edit and re-push.
-->

You are doing a health-check on a freshet-monitoring data pipeline that was deployed on 2026-04-30. The setup polls MVCA's Kisters KiWIS API hourly for water-level readings at 'Gauge - Ottawa River at Buckhams Bay' (KiWIS ts_id 48242042) and writes them to a TimescaleDB instance running in a private k3s homelab. You can't reach the cluster directly, but the user exposes a read-only PostgREST proxy at https://freshet.xgrunt.com/history/ via Cloudflare Tunnel. nginx restricts that path to GET/HEAD/OPTIONS, so you can read but cannot mutate. No auth needed.

Check four things and report a 6-line summary at the end:

1. Cluster ingest freshness. GET https://freshet.xgrunt.com/history/river_readings?station_id=eq.99001&order=time.desc&limit=1&select=time,level_m → parse the timestamp, compute age in hours. RED if >6h old, YELLOW if >2h, GREEN otherwise. Print the actual timestamp + level.

2. Cluster row growth. GET with header 'Prefer: count=exact' and 'Range: 0-0' on https://freshet.xgrunt.com/history/river_readings?station_id=eq.99001&select=* → parse the Content-Range header. Total was 35,665 rows on 2026-04-30. Six weeks later you should expect ~6 weeks × 24h × 7d ≈ +1,000 rows; anything <100 new rows is a RED flag (cron probably stopped). Print delta vs. 35,665.

3. Upstream API liveness. curl 'https://waterdata.quinteconservation.ca/KiWIS/KiWIS?service=kisters&type=queryServices&request=getTimeseriesValues&datasource=0&format=json&ts_id=48242042&header=true&dateformat=UNIX&from=<48h ago in YYYY-MM-DDTHH:MM:SSZ form>' and check that it returns rows with timestamps in the last 48h. If it doesn't, MVCA itself broke (not the cron).

4. 2026 freshet peak (sanity check). Same KiWIS endpoint with from=2026-03-15 to=2026-06-15 → max value. The 2023 peak at this gauge was 60.40m. Just print the 2026 max for the user's reference; don't alarm unless it's null/missing.

If anything is RED, also: clone aachtenberg/homelab-infra (default), look at git log --since='6 weeks ago' for k3s/base/data/files/river-history/ and k3s/base/data/river-history.yml, and include any commits touching those paths in your report.

Do NOT open issues, PRs, push commits, or attempt to fix anything — read-only investigation. Report concisely.
