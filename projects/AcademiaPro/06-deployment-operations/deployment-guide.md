# Deployment Guide — Academia Pro

> Top-of-phase deployment playbook. The detailed per-environment SOP lives in `01-deployment-guide/01-deployment-guide.md`; this file is the authoritative index and rollback reference.

## Environments

- local — Docker Compose. See `04-development/env-setup.md`.
- staging — AWS eu-west-1, single-AZ, auto-scaling 2–4 instances.
- production — AWS eu-west-1, multi-AZ, auto-scaling 4–12 instances. MySQL read replica in us-east-1 for DR.

## Deployment Pipeline

1. PR merged to `develop` — CI runs the full suite and deploys to staging.
2. Staging smoke tests pass — tag `release/vX.Y.Z` and deploy to production within the declared change window.
3. Production canary: 10% traffic, 5-minute health check, then 100%. Automatic rollback on P95 error rate > 1%.

## Rollback Procedure

Every deploy must be reversible within 10 minutes.

1. Application rollback — AWS CodeDeploy auto-rollback on `deploy-health` alarm. Manual: `./scripts/rollback.sh <previous-release-tag>`.
2. Database rollback — every migration reversible. `php artisan migrate:rollback --step=1` (staging) or run a forward-fix migration (production — never reverse in prod unless the migration is destructive and the defect is caught within 10 minutes).
3. Feature-flag rollback — every new FR merges behind a feature flag defaulting OFF. Flip OFF via LaunchDarkly without a redeploy.

Rollback is practised every sprint on staging.

## Cutover Sequence

Cutover for a net-new customer tenant is documented in `01-deployment-guide/`. Go-live readiness is checked against `go-live-readiness.md`. Change-window policy in `change-window.md`.

## Traces

- FR-OPS-001, FR-OPS-002.
- NFR-AVAIL-001 (99.5% production uptime).
- CTRL-ISO-A12 (operations security).
