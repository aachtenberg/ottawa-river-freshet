# Product / UX specs

Specs for the personalized mobile freshet experience (concept → MVP).

| Doc | Todo | Status |
|---|---|---|
| [cottage-wizard.md](./cottage-wizard.md) | ux-validate | Validated mark fields cottagers actually know |
| [gauge-snap.md](./gauge-snap.md) | gauge-snap | Snap-to-gauge + Lac Deschênes overrides |
| [snap-stations.json](./snap-stations.json) | gauge-snap | Corridor lat/lon catalog for snap |
| [mvp-pwa.md](./mvp-pwa.md) | mvp-scope | Mobile Home scope (web + Android shell) |

**Implementation lives in [`freshet-mobile/`](../../../freshet-mobile/)** — Capacitor Android + Vite web MVP. Do **not** confuse with the Mansfield-only dashboard at `apps/files/freshet-dashboard/` or `freshet-public/dashboard/`.

These specs do not change the live Mansfield dashboard. Dashboard constants (`PROPERTY_THRESHOLDS`, `HOME_PIN`, corridor station lists) are the personalization surface the mobile app turns into a user profile.
