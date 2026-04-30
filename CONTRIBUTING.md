# Contributing

Thanks for considering a contribution. This is a small community project — we
keep it light.

## Bugs and feature requests

Open a GitHub issue. For bugs, include:

- Browser / OS (for dashboard issues)
- The console output (open dev tools, paste any red errors)
- A screenshot if it's visual
- Whether you're running the upstream `freshet.xgrunt.com` deploy, your own
  docker-compose, or your own Kubernetes manifests

For feature requests, mention which area: dashboard UI, ingesters, alerter,
docs, deploy.

## Pull requests

PRs welcome. Some guidance:

- **Stick to stdlib in the ingesters.** Adding `requests`, `bs4`, etc. is a
  real cost — they have to be `pip install`-ed every cron tick. The current
  scripts are intentionally stdlib-only.
- **Don't break the docker-compose quickstart.** It's the on-ramp for new
  deployments; please test `docker compose up -d` before sending the PR.
- **Sanitize personal data.** No real cottage GPS, no real ntfy topics, no
  real internal hostnames in commits. The existing code uses placeholders
  for a reason.
- **Match existing code style.** No formatter or linter is enforced; just
  read the surrounding code and don't go too far afield.

## Calibration data submissions

If you have **better operating limits** for any reservoir (especially if
sourced from operator documentation), open a PR that updates
`dashboard/reservoir-limits.json` and add a note to the
`_calibration_source` field. Cross-checks against published ORRPB readings
welcome — see [`docs/methodology.md`](docs/methodology.md) for the back-solve
procedure.

If you've **observed flood thresholds at a different property** in the
basin and want them documented for community reference, please open an issue
rather than a PR — we'll figure out the right place for that data.

## Adapting for a different watershed

The framework is reusable beyond the Ottawa River. The pieces that need
swapping:

- The Vigilance station list (your river's gauges)
- ORRPB-equivalent reservoir scraper (different watershed, different
  publishing authority, different HTML to parse)
- Reservoir limits + capacities
- Reference data CSVs (your watershed's historical record)
- Property thresholds (your specific property's observations)

Happy to chat about adaptation for other watersheds — open an issue and let's
talk.

## Code of Conduct

Treat people with respect. Don't post real-name info about anyone without
their consent. We're trying to make a useful flood-monitoring tool, not a
gossip channel.
