# Kubernetes deploy

Generic Kubernetes manifests for the freshet stack. No Kustomize, no Helm —
just plain YAML you can `kubectl apply -f` against any cluster (managed K8s,
k3s, microk8s, etc.).

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
| `40-river-history-cron.yaml` | Hourly Vigilance + KiWIS ingester CronJob + script ConfigMap |
| `50-reservoir-ingest-cron.yaml` | Daily ORRPB scraper CronJob + script ConfigMap |
| `60-alerter-cron.yaml` | Hourly threshold-crossing alerter CronJob + script ConfigMap |

## First-time apply

```bash
# Replace the placeholder password before applying:
sed -i 's|REPLACE_PASSWORD|'$(openssl rand -base64 32)'|' 10-timescaledb.yaml

kubectl apply -f 00-namespace.yaml
kubectl apply -f 10-timescaledb.yaml
kubectl rollout status -n freshet statefulset/timescaledb --timeout=120s

kubectl apply -f 20-postgrest.yaml
kubectl apply -f 30-dashboard.yaml
kubectl apply -f 40-river-history-cron.yaml
kubectl apply -f 50-reservoir-ingest-cron.yaml
kubectl apply -f 60-alerter-cron.yaml

# Trigger initial ingests:
kubectl create job -n freshet --from=cronjob/river-history-ingest river-init
kubectl create job -n freshet --from=cronjob/reservoir-ingest reservoir-init
```

The dashboard's Ingress points at `freshet.example.com` by default — update
to your hostname before applying `30-dashboard.yaml`.

## Updating the dashboard after editing index.html

The dashboard is shipped via a ConfigMap. Easiest update flow:

```bash
kubectl create configmap freshet-dashboard \
  --from-file=index.html=../../dashboard/index.html \
  --from-file=nginx.conf=../../dashboard/nginx.conf \
  --from-file=favicon.svg=../../dashboard/favicon.svg \
  --from-file=orw-dams.json=../../dashboard/orw-dams.json \
  --from-file=reservoir-limits.json=../../dashboard/reservoir-limits.json \
  -n freshet --dry-run=client -o yaml | kubectl apply -f -

kubectl rollout restart -n freshet deployment/dashboard
```

(For the real upstream maintainer's homelab, this is automated via Kustomize
`configMapGenerator` which auto-rolls the deployment when file content
changes; if you want that behaviour, swap the manifests for a Kustomize
overlay.)

## Customizing for your watershed

Same as the docker-compose deploy — edit `STATION_IDS` env in
`40-river-history-cron.yaml`, plus the relevant constants in
[`dashboard/index.html`](../../dashboard/index.html).

For the alerter, edit the `NTFY_TOPIC` env value in `60-alerter-cron.yaml`.
Use a private topic (long random string) so only your devices subscribe.
