# Readiness Gates

Use these gates to decide whether a release is truly ready for launch.

## Product Gate

- Scope planned for launch is implemented and traced to approved requirements.
- Deferred items are understood and do not invalidate the release.
- Known defects are classified by user and business impact, not only count.

## Technical Gate

- Deployment steps are repeatable and time-bounded.
- Rollback or recovery steps are tested and owned.
- Monitoring, logging, dashboards, and alerts exist for the launch scope.

## Operational Gate

- On-call, support, and incident escalation roles are assigned.
- Runbooks cover the most likely and highest-impact incidents.
- Capacity, backup, restore, and dependency readiness have been reviewed.

## Security And Compliance Gate

- Security signoff issues are resolved or explicitly accepted.
- Access provisioning and secrets handling are ready for production.
- Audit or regulatory obligations for the release are understood.

## Organizational Gate

- Internal teams know what is launching, when, and how to respond.
- Customer communications, enablement, or training materials are ready when needed.
- The business owner agrees that the organization can absorb the release.

## Decision Rule

- `Go`: no blocked gates and residual risk is accepted by accountable owners.
- `Conditional Go`: only bounded conditions remain, with named owners and completion dates before launch.
- `No-Go`: any blocker threatens safety, compliance, data integrity, service continuity, or core business value.
