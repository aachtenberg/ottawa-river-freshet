"""Shared ottawariver.ca fetch for the ORRPB scrapers: retry 5xx and network
errors, spaced past the cluster DNS cache.

www.ottawariver.ca is a CNAME into QUIC.cloud's CDN, which answers by resolver
location. On 2026-10-08 Google DNS (8.8.8.8) handed out a CDN node,
199.59.247.242, that returned 520 "Origin Server Unavailable" to every request,
while 1.1.1.1 / 9.9.9.9 / the router resolved to a node that served 200.
CoreDNS forwards to each node's /etc/resolv.conf, and one node lists 8.8.8.8,
so a pod got the dead node on roughly half its lookups. reservoir-ingest failed
7 of 8 runs.

The job's own backoffLimit didn't help: the pod restarts within CoreDNS's 30s
cache and resolves to the same dead node again. Waiting past the cache gets a
fresh lookup, and a fair chance of a working node, on each attempt.

Shipped into each scraper's ConfigMap next to the script, so `import
orrpb_http` resolves from the script's own directory (/app).
"""
import http.client
import os
import sys
import time
import urllib.error
import urllib.request

# At least one attempt: 0 would skip the loop and hand the caller None.
ATTEMPTS = max(1, int(os.environ.get("ORRPB_FETCH_ATTEMPTS", "5")))
# CoreDNS `cache 30` caps answers at 30s; wait a little longer than that.
RETRY_WAIT_S = float(os.environ.get("ORRPB_FETCH_RETRY_WAIT_S", "35"))


def fetch_text(req, timeout=30):
    """urlopen(req) and return the decoded body, retrying 5xx and network
    errors. 4xx raises at once: that's a real answer, not a bad edge node.

    Retries replay the request, so pass only requests that are safe to repeat.
    The station-history POST qualifies: it's the read-only table-view form
    (reading-type / data-display / data-type), not a write."""
    for attempt in range(1, ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code < 500:
                raise
            err = e
        # HTTPException covers a body cut short mid-read (IncompleteRead).
        except (urllib.error.URLError, http.client.HTTPException,
                TimeoutError, ConnectionError) as e:
            err = e
        if attempt == ATTEMPTS:
            raise err
        print(f"  {req.full_url}: {err} (attempt {attempt}/{ATTEMPTS}); "
              f"retrying in {RETRY_WAIT_S:.0f}s", file=sys.stderr, flush=True)
        time.sleep(RETRY_WAIT_S)
