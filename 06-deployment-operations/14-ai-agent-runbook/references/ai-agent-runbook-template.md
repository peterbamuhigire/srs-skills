# AI Agent Runbook Template

## 1. Kill-switch Operations

### Global kill-switch

- Surface: ops console `> Agents > Global Kill-Switch`; API `POST /ops/agents/killswitch {scope: "global"}`.
- Auth: two-person rule (two ops roles confirm).
- Propagation SLA: 5 s from flip to last dispatcher.
- Use cases: upstream model-provider compromise; mass irreversible-incident; red-team-confirmed catastrophic vulnerability.
- Recovery: after SEV1 closure, re-enable per the rollback runbook with executive sign-off.

### Per-tenant kill-switch

- Surface: ops console `> Tenants > <tenant> > Agent Kill-Switch`; API `POST /ops/agents/killswitch {scope: "tenant:<id>"}`.
- Auth: single ops role; admin-approved by tenant admin when initiated at customer request.
- Propagation SLA: 5 s.
- Use cases: tenant-scoped incident; contractual obligation; customer request.

### Per-feature kill-switch

- Surface: ops console `> Features > <feature> > Kill-Switch`.
- Auth: single ops role.
- Propagation SLA: 5 s.
- Use cases: feature-wide regression; SLO SEV1 from the agent SLO doc.

### Rehearsal

Monthly in staging via `chaos: agent-killswitch`. Verify each switch achieves the propagation SLA. Record evidence in the runbook log.

## 2. Force-Pause & Resume

### Force-pause a run

- API: `POST /ops/agents/runs/<id>/pause`.
- Effect: run marked `intervened`; in-flight tool calls complete or time-out per the per-tool timeout; no further steps planned.

### Force-pause all runs for a tenant

- API: `POST /ops/agents/runs/pause {scope: "tenant:<id>"}`.
- Effect: existing runs paused; new starts refused until resumed.

### Force-resume

- API: `POST /ops/agents/runs/<id>/resume`.
- Requires: SEV closure review record attached.
- Effect: orchestrator resumes from last durable state with reasoning logged.

## 3. Replay

```
POST /ops/agents/runs/<id>/replay
{
  "target_planner_version": "<current>",
  "target_catalogue_version": "<current>",
  "environment": "eval"
}
```

Returns: replay run ID; metrics compared to original.

## 4. Agent-Task Quarantine

- API: `POST /ops/agents/runs/<id>/quarantine`.
- Effect: run marked `quarantined`; tool calls refused; state preserved for forensic review.
- Notification: tenant admin notified within 24 h.

## 5. Audit-Log Review

| Cadence | Scope | Owner |
|---------|-------|-------|
| Daily | all irreversible-action events from last 24 h | On-call operator |
| Weekly | per-feature audit summary | AI Lead |
| Monthly | per-tenant audit summary (Enterprise) | Customer success + AI Lead |
| Quarterly | tenant-facing audit export offered to Enterprise tenants | Customer success |

Anomaly triggers: irreversible action without `human_approval_event_id`; tool call refused for tenant-claim-mismatch; cost overshoot per run; intervention rate above feature SLO.

## 6. Incident Playbooks

### 6.1 Mass irreversible-action incident

1. Detection: SLO alert; user reports; daily audit review.
2. Declare SEV1.
3. Flip per-feature kill-switch immediately.
4. Contain: per-tenant kill-switches for affected tenants.
5. Investigate: replay sample runs; pull dispatcher logs.
6. Notify: affected tenant admins within 24 h; legal review for regulatory disclosure.
7. Postmortem: within 5 working days; updates to agent eval and red-team registries.

### 6.2 Cross-tenant tool-routing attempt detected

1. Detection: dispatcher emits `tenant-claim-mismatch` refusal at non-zero rate.
2. Declare SEV2 (SEV1 if any succeeded).
3. Pull all matching events; verify no successful cross-tenant call.
4. If any succeeded: SEV1, global kill-switch, legal review, tenant notifications.
5. Postmortem; add a red-team scenario; ADR update if architectural change required.

### 6.3 Indirect prompt injection succeeded in production

1. Detection: user report; daily audit review; nightly eval drop.
2. Declare SEV2.
3. Roll back last planner / prompt / sanitiser change.
4. Add the attack pattern to the red-team registry within 7 d.
5. Postmortem.

### 6.4 Budget-runaway event

1. Detection: cost-burn alert (per-tenant 200% of envelope for 1 h).
2. Throttle the tenant at the dispatcher.
3. If continues, per-tenant feature pause.
4. Notify tenant admin.
5. Adjust budget caps in PRD if pattern repeats; ADR update.

### 6.5 Orchestrator crash

1. Detection: availability SLI drops.
2. Verify resume SLA met for in-flight runs.
3. If not met: SEV2.
4. Drain runs to backup region if available.
5. Postmortem on the root cause.

### 6.6 Tool-provider compromise

1. Detection: external advisory; abnormal tool error spikes.
2. Per-tool kill-switch within 1 h.
3. Flip global kill-switch if scope is broad.
4. Notify affected tenants.
5. Reintroduce the tool only after provider confirms remediation and red-team re-passes.

### 6.7 Agent-action disclosure (regulatory or customer)

1. Trigger: regulator request, audit request, customer subject-access request.
2. Pull audit log for the specified (tenant, user, time-window).
3. Redact per the disclosure policy.
4. Coordinate with DPO and legal.
5. Deliver within the regulatory deadline.

## 7. On-call Rotation

- Primary on-call has: kill-switch console; read-only per-tenant audit access; paging from SLO burn-rate + irreversible-incident triggers.
- Secondary on-call: AI Lead.
- Escalation: AI Lead → Architect → CTO → CEO.
- Handoff: 24 h; documented in `on-call-log/`.

## 8. Rehearsal Cadence

| Drill | Cadence | Owner |
|-------|---------|-------|
| Global kill-switch propagation | Monthly | SRE |
| Per-tenant kill-switch + notification | Quarterly | SRE + Customer success |
| Mass irreversible-incident playbook | Quarterly | AI Lead |
| Cross-tenant routing playbook | Quarterly | Security |
| Replay-a-run | Monthly | On-call |
