---
name: 22-game-release-and-live-operations-runbook
description: "Use when documenting reproducible game builds, signing, artifact promotion, distribution, staged rollout, rollback, crash diagnosis, matchmaking operations, live events, remote config, economy controls, support, or incidents."
metadata: {portable: true, compatible_with: [claude-code, codex]}
---
# Game Release and Live Operations Runbook
<!-- dual-compat-start -->
## Use When
- A tested game needs an operator-grade release, rollback, support or live-change procedure.
## Do Not Use When
- Current channel requirements or artefact identity are unavailable.
- Do not rebuild after approval.
## Required Inputs
| Artefact | Source or provider | Required? | Behaviour when missing |
|---|---|---|---|
| Artefact, checksum, symbols, manifest, signing custody, channels and rollback | Build, QA and platform owners | Yes | Stop promotion. |
| Data/economy/ad config, privacy/child treatment, capacity, support and communications | Specialist owners | Conditional | Disable or block affected live scope. |
## Workflow
1. Verify dated official channel requirements and pinned versions.
2. Validate artefact, symbols, licences, checksum, provenance and signing boundary.
3. Rehearse install/upgrade, low storage, interruption, save migration, offline and credential failures.
4. Promote the tested artefact through cohorts with operational thresholds.
5. Define diagnosis, containment, rollback, communication and postmortem.
6. Gate config/events/economy/ad placements with schema, approval, audience/territory, expiry, wellbeing/trust thresholds, kill switch and reversal. Ads default off when consent, age treatment, creative review or SDK health is unknown.
7. Preserve no-ads/no-analytics degraded play where feasible and rehearse no-fill, offline, consent withdrawal, deletion, vendor outage and child-safe fallback.
8. Stop on missing rollback, symbols, privacy/rights approval or owner; recover by holding rollout or disabling affected live scope.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Game release/liveops runbook | Release, operations and support | Artefact, steps, signals, owners, rollback and communications are executable. |
## Evidence Produced
| Evidence | Reviewer | Acceptance condition |
|---|---|---|
| Promotion/rehearsal ledger | Release approver | Checksums, approvals, failures and rollback proof are retained. |
## Capability and permission boundaries
Read and search are allowed. Signing, submission, production config, messaging or rollback require authorised operators.
## Degraded mode
Return a qualified dry run, mark unavailable checks `not assessed`, and keep promotion blocked.
## Decision Rules
| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| Checksum differs | Reject artefact. | Untested promotion. |
| Threshold breaches | Halt or roll back. | Expanded harm. |
| Live change mutates state | Simulate, version and rehearse reversal. | Corruption. |
## Quality Standards
- Preserve symbols, checksums, manifests and rollback assets; minimise telemetry.
## Anti-Patterns
- Rebuild after QA. Fix: promote exact artifact.
- Secrets in source. Fix: custody boundary.
- Hotfix without migration. Fix: compatibility tests.
- Event without expiry. Fix: kill switch and end state.
- Reviews as telemetry. Fix: triangulate measured signals.
- Ad incident handled only by vendor. Fix: retain studio kill switch, player support, evidence, containment and postmortem ownership.
## References
- [Release manifest](references/game-release-manifest.md)
<!-- dual-compat-end -->
