---
name: "ai-agent-runbook"
description: "Generate the AI Agent Runbook: kill-switch (global, per-tenant, per-feature), force-pause, force-resume, replay-a-run, agent-task quarantine, audit-log review cadence, agent-incident handling playbooks, and the operator-on-call rotation for agent-specific incidents."
metadata:
  use_when: "Use whenever a SaaS operates one or more agent features at L1+ in production. Required before any L1+ rollout."
  do_not_use_when: "Do not use for L0 (suggest-only) features with no execution surface; the generic runbook is sufficient."
  required_inputs: "AI_Agent_Architecture_Spec.md, Action_Catalogue_Spec.md, AI_Agent_SLO_Doc.md, AI_Feature_Rollout_Runbook.md, Runbook.md (parent), SaaS_Incident_Response_And_Postmortem.md."
  workflow: "Define the kill-switch operations, define force-pause / force-resume, define replay, define agent-task quarantine, define audit-log review cadence, write playbooks for each agent incident class, define the on-call rotation, write the runbook."
  quality_standards: "Every agent feature shall have a kill-switch procedure with a propagation SLA. Every irreversible-action incident shall have a documented playbook. Audit-log review shall have a cadence and an owner."
  anti_patterns: "Do not require code deploy for kill-switch. Do not omit the two-person rule for global kill-switch. Do not let the audit log accumulate unreviewed."
  outputs: "AI_Agent_Runbook.md."
  references: "Use references/ai-agent-runbook-template.md."
---

# AI Agent Runbook Skill

## Core Instructions

### Step 1: Kill-switch operations

Document three switches with operator-only access:

- **Global kill-switch** — refuses every tool with `kill_switch.global = refuse` across every tenant. Two-person rule. Used for upstream provider compromise, mass irreversible-incident, or red-team-confirmed catastrophic vulnerability.
- **Per-tenant kill-switch** — refuses tools for one tenant. Used for tenant-scoped incident, contractual obligation, or customer request.
- **Per-feature kill-switch** — refuses tools for one agent feature globally. Used for feature-scoped regression or SEV1 from the SLO doc.

State the propagation SLA (default 5 s), the rehearsal cadence (monthly in staging), and the operator surface (ops console + API + on-call paging integration).

### Step 2: Force-pause and force-resume

- **Force-pause an agent run** — orchestrator marks the run `intervened`; in-flight tool calls complete or time-out; no further steps.
- **Force-pause all runs for a tenant** — soft kill-switch; existing runs paused; new starts refused.
- **Force-resume** — orchestrator resumes from last durable state with reasoning logged; available only after a SEV closure review.

### Step 3: Replay a run

Operator can replay any historical run against the current planner + catalogue in the eval environment. Used for postmortems and for "would the fix have caught this?" verification.

### Step 4: Agent-task quarantine

When a run is suspected harmful but not actioned, quarantine the run:

- Mark the run `quarantined`.
- All tool calls refused.
- Run preserved with full state for forensic review.
- Notify the tenant admin within 24 h.

### Step 5: Audit-log review cadence

- Daily: irreversible-action audit log reviewed by an on-call operator; any anomaly creates a ticket.
- Weekly: per-feature audit summary reviewed by the AI lead.
- Quarterly: tenant-facing audit export offered to Enterprise tenants.

### Step 6: Agent-incident playbooks

Define playbooks for:

1. Mass irreversible-action incident.
2. Cross-tenant tool-routing attempt detected.
3. Indirect prompt injection succeeded in production.
4. Budget-runaway event (single tenant > 200% envelope for > 1 h).
5. Agent unresponsive / orchestrator crashed.
6. Tool provider compromise (external write tool with confirmed breach).
7. Disclosure of agent action (regulatory or customer).

Each playbook follows: detection → declare SEV → kill-switch decision → contain → investigate → notify → postmortem.

### Step 7: On-call rotation

Operators on call for agent incidents shall have:

- Kill-switch console access.
- Read-only access to per-tenant audit log.
- Paging from SLO burn-rate alerts and irreversible-incident triggers.
- Documented escalation path: AI Lead → Architect → CTO → CEO.

### Step 8: Write the runbook

`AI_Agent_Runbook.md` sections: 1) Kill-switch Operations, 2) Force-Pause & Resume, 3) Replay, 4) Agent-Task Quarantine, 5) Audit-Log Review, 6) Incident Playbooks, 7) On-call Rotation, 8) Rehearsal Cadence.

## Standards

- Google SRE incident response
- ISO/IEC 27035 (incident management)
- NIST AI RMF MANAGE
- ISO/IEC 42001 Clause 10 (improvement)

## Compliance drill evidence capture

Every drill produces evidence consumed by the SOC 2 / ISO / HIPAA control packs. Capture format and cadence are defined in `09-governance-compliance/25-ai-agent-evidence-pack-spec/references/ai-agent-evidence-frequency-table.md` (rows 15, 16, 17):

| Drill | Evidence | Cadence | Controls |
|-------|----------|---------|----------|
| Kill-switch (global / per-tenant / per-feature) | drill report; audit-log entry; propagation timing | quarterly staging; annual production | SOC2 CC7.4, A1.3; ISO A.5.30, A.8.2; HIPAA 164.308.a.7 |
| Replay-a-run | drill report | quarterly | SOC2 A1.3; ISO A.5.30 |
| Force-pause + force-resume | drill report | quarterly | SOC2 A1.3; ISO A.5.30 |
| Agent-task quarantine | drill report; tenant-admin notification log | annual | SOC2 CC7.3; ISO A.5.25 |

The compliance runbook (`06-deployment-operations/20-ai-agent-compliance-runbook`) sets the calendar.

## Resources

- `logic.prompt`, `README.md`, `references/ai-agent-runbook-template.md`.
