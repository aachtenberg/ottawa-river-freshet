# Kubernetes deploy

Generic Kubernetes manifests for the freshet stack. No Kustomize, no Helm —
just plain YAML you can `kubectl apply -f` against any cluster (managed K8s,
k3s, microk8s, etc.). The bootstrap SQL, dashboard files, and ingester
scripts are inlined into the manifests, so a fresh cluster is one
`kubectl apply -f .` away from a running stack.

## Prerequisites

- Kubernetes ≥ 1.27 (required for `CronJob` `timeZone` support)
- An ingress controller (NGINX Ingress, Traefik, etc.) — or change the
  dashboard service to `LoadBalancer` / `NodePort` if you don't have one.
- A persistent volume class (`PersistentVolumeClaim` is `ReadWriteOnce`,
  works on any class).

## Files

| File | What it deploys |
|---|---|
| `00-namespace.yaml` | The `freshet` namespace |
| `10-timescaledb.yaml` | TimescaleDB StatefulSet, headless Service, Secret with the DB password, ConfigMap of the bootstrap SQL |
| `20-postgrest.yaml` | PostgREST Deployment + Service |
| `30-dashboard.yaml` | nginx Deployment + Service + dashboard ConfigMap (the static files) + Ingress |
| `40-river-history-cron.yaml` | Hourly Vigilance + KiWIS + open-meteo ingester CronJob + script ConfigMap |
| `50-reservoir-ingest-cron.yaml` | Daily ORRPB scraper CronJob + script ConfigMap |
| `55-hq-ingest-cron.yaml` | Hourly Hydro-Québec open-data ingester (centrale + station telemetry) |
| `56-orrpb-river-ingest-cron.yaml` | Daily ORRPB "Average Daily Flows" scrape → `orrpb_river_flows` (Temiscaming · Otto Holden · Des Joachims · Chenaux · Chats Falls · Britannia · Carillon — incl. the OPG dams not in the HQ feed) |
| `60-alerter-cron.yaml` | Hourly threshold-crossing alerter CronJob + script ConfigMap |
| `70-wsc-ingest-cron.yaml` | Hourly WSC realtime CSV ingester (level + discharge) |
| `80-eccc-ingest-cron.yaml` | Six-hourly ECCC daily-climate bulk-CSV ingester |
| `85-swe-ingest-cron.yaml` | Daily snow-water-equivalent ingesters → `swe_daily`: CaLDAS-NSRPS (ECCC GeoMet, no auth) + ERA5-Land (Copernicus CDS — needs `CDS_API_KEY` in `10-timescaledb.yaml` and the ERA5-Land licence accepted on the CDS website) |

## First-time apply

Two values must be edited before the first apply: the DB password in
`10-timescaledb.yaml` and the ntfy topic in `60-alerter-cron.yaml`. (Optionally
also `CDS_API_KEY` in `10-timescaledb.yaml`, if you want the ERA5-Land SWE feed —
otherwise that one cron just fails harmlessly.) The dashboard ingress hostname in
`30-dashboard.yaml` (`freshet.example.com`) should also be changed if you want to
expose it.

```bash
# 1. Set a real DB password.
sed -i 's|REPLACE_PASSWORD|'$(openssl rand -base64 32)'|' 10-timescaledb.yaml

# 2. Set a private ntfy topic (long random string — only your devices
#    should subscribe).
sed -i 's|REPLACE_WITH_PRIVATE_TOPIC|'$(openssl rand -hex 16)'|' 60-alerter-cron.yaml

# 3. Optional: set your dashboard hostname.
sed -i 's|freshet.example.com|freshet.your-domain.tld|' 30-dashboard.yaml

# 4. Apply everything. The namespace must exist first; after that order is
#    not strict but Timescale should be ready before PostgREST/cronjobs
#    start hitting it.
kubectl apply -f 00-namespace.yaml
kubectl apply -f 10-timescaledb.yaml
kubectl rollout status -n freshet statefulset/timescaledb --timeout=120s

kubectl apply -f 20-postgrest.yaml
kubectl apply -f 30-dashboard.yaml
kubectl apply -f 40-river-history-cron.yaml
kubectl apply -f 50-reservoir-ingest-cron.yaml
kubectl apply -f 55-hq-ingest-cron.yaml
kubectl apply -f 56-orrpb-river-ingest-cron.yaml
kubectl apply -f 60-alerter-cron.yaml
kubectl apply -f 70-wsc-ingest-cron.yaml
kubectl apply -f 80-eccc-ingest-cron.yaml
kubectl apply -f 85-swe-ingest-cron.yaml

# 5. Trigger initial ingests so the dashboard has data immediately rather
#    than waiting for the first scheduled run.
kubectl create job -n freshet --from=cronjob/river-history-ingest river-init
kubectl create job -n freshet --from=cronjob/reservoir-ingest reservoir-init
kubectl create job -n freshet --from=cronjob/hq-ingest hq-init
kubectl create job -n freshet --from=cronjob/orrpb-river-ingest orrpb-river-init
kubectl create job -n freshet --from=cronjob/wsc-ingest wsc-init
kubectl create job -n freshet --from=cronjob/eccc-ingest eccc-init
kubectl create job -n freshet --from=cronjob/swe-caldas-ingest swe-caldas-init
# (the ERA5-Land 1950→present backfill is a separate one-shot — see the comment
#  block in 85-swe-ingest-cron.yaml)
```

## Updating after editing source files

The dashboard files, ingester scripts, and bootstrap SQL are inlined into
the YAMLs in this directory. If you edit any of the upstream sources
(`dashboard/`, `ingesters/`, `alerter/`), regenerate the affected ConfigMap
in-place and (for the dashboard) restart the Deployment:

```bash
# Dashboard
kubectl create configmap freshet-dashboard \
  --from-file=index.html=../../dashboard/index.html \
  --from-file=nginx.conf=../../dashboard/nginx.conf \
  --from-file=favicon.svg=../../dashboard/favicon.svg \
  --from-file=orw-dams.json=../../dashboard/orw-dams.json \
  --from-file=reservoir-limits.json=../../dashboard/reservoir-limits.json \
  -n freshet --dry-run=client -o yaml | kubectl apply -f -
kubectl rollout restart -n freshet deployment/dashboard

# River-history script
kubectl create configmap river-history-script \
  --from-file=ingest.py=../../ingesters/river-history/ingest.py \
  -n freshet --dry-run=client -o yaml | kubectl apply -f -

# Reservoir-ingest script
kubectl create configmap reservoir-ingest-script \
  --from-file=scrape.py=../../ingesters/reservoir-ingest/scrape.py \
  -n freshet --dry-run=client -o yaml | kubectl apply -f -

# Alerter script
kubectl create configmap freshet-alerter-script \
  --from-file=alerter.py=../../alerter/alerter.py \
  -n freshet --dry-run=client -o yaml | kubectl apply -f -
```

The bootstrap SQL ConfigMap (`timescaledb-bootstrap`) only takes effect on
the very first boot of an empty PVC — once the database is initialized,
schema changes need to be applied with `kubectl exec` + `psql`, not by
re-applying the ConfigMap.

For the upstream maintainer's homelab this whole flow is automated via
Kustomize `configMapGenerator` (which hashes file content into the
ConfigMap name and auto-rolls the consuming Deployment); if you want that
behaviour, swap these manifests for a Kustomize overlay.

## Customizing for your watershed

Same as the docker-compose deploy — edit `STATION_IDS` env in
`40-river-history-cron.yaml`, plus the relevant constants in
[`dashboard/index.html`](../../dashboard/index.html) (and re-run the
dashboard ConfigMap regenerate command above).
