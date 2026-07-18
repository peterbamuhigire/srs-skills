---
name: 09-saas-incident-response-and-postmortem
description: Use when producing or updating SaaS incident response and postmortem procedure for incident command, containment, recovery, communication, evidence, and blameless learning. Use runbook for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# SaaS Incident Response & Postmortem Skill

<!-- dual-compat-start -->
## Use When

- Produce or update SaaS incident response and postmortem procedure from approved project evidence.
- Resolve decisions about incident command, containment, recovery, communication, evidence, and blameless learning.
- Prepare a reviewable handoff for SRE, support, and service owners.

## Do Not Use When

- The task is primarily owned by runbook; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| SaaS Incident Response And Postmortem Procedure | SRE, support, and service owners | The procedure restores service safely, preserves a source-attributed timeline, and tracks corrective actions to closure. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose response from observable customer impact and service criticality and produce the full artefact. | Slow recovery or unactionable postmortems. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring runbook concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when the procedure restores service safely, preserves a source-attributed timeline, and tracks corrective actions to closure.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

Produces the SaaS-tuned Incident Response & Postmortem doc pack. The generic runbook covers severity tiers and escalation, but SaaS adds a critical dimension: **tenant scope**. A SEV1 affecting one Enterprise tenant is operationally different from a SEV1 affecting all tenants. This skill captures that.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Multi_Tenancy_Architecture_Spec.md, SLO_And_Error_Budget_Doc.md, Runbook.md, pricing spec |
| **Output** | `IR_and_Postmortem.md` + `templates/customer-comms-<sev>.md` |
| **Standard** | Google SRE; FCC / NIST incident-comms norms |

## Core Instructions

### Step 1: Define the two-dimensional severity matrix

| Severity × Scope | Single tenant | Tenant cohort | Platform-wide |
|------------------|---------------|---------------|---------------|
| SEV1 | Tier-Enterprise customer down or data-impacting incident | Pod or region down | All-tenant outage / data corruption |
| SEV2 | Tier-Gold customer down | Multiple Gold tenants degraded | Significant feature degraded for most |
| SEV3 | Single Silver/Bronze customer down | Cohort degraded | Minor feature degraded for some |
| SEV4 | Cosmetic | Cosmetic | Cosmetic |

Override the matrix per project but the two dimensions are mandatory.

### Step 2: Define detection sources

Monitoring alerts (linked to SLO burn-rate), customer support tickets, status-page subscriber reports, partner/SDK error reports, security telemetry.

### Step 3: Define IR phases

Detect → Triage → Contain → Mitigate → Resolve → Postmortem. State the time targets per severity (SEV1: triage in 5 min, customer-comms in 15 min; SEV2: triage in 15 min, comms in 30 min).

### Step 4: Customer-comms templates per severity

For SEV1 and SEV2 produce:

- Initial acknowledgement (within X min of detection).
- Status updates (cadence: every 30 min for SEV1, every hour for SEV2).
- Resolution announcement.
- Postmortem publication (within 5 business days for SEV1, 10 for SEV2).

Each template carries: subject line, in-app banner copy, status-page entry, dedicated email to affected tenants. Include placeholder for tenant scope (`{affected_tenants}` or "all tenants in the EU region").

### Step 5: Status-page protocol

Define when to post (any SEV1, any SEV2 lasting > 15 min, any maintenance). Define who can post (on-call + comms-on-call). Define the components mapped (per-region per-service). Define subscriber notification.

### Step 6: Blameless postmortem template

Sections: timeline, impact (tenants affected, duration, error-budget burn, financial impact estimate, support load), root cause (5 whys), what went well, what went poorly, contributing factors, action items (with owner, severity, due date, status), lessons learned.

### Step 7: Action-item tracking

State the system where action items are tracked (ticketing tool) and the review cadence (weekly action-item burn-down meeting). Postmortem closure is independent of incident closure.

### Step 8: Write IR_and_Postmortem.md

Sections: 1) Severity Matrix, 2) Detection Sources, 3) IR Phases & Time Targets, 4) Customer-Comms Protocol, 5) Status-Page Protocol, 6) Blameless Postmortem Template, 7) Action-Item Tracking, 8) Tenant-Impact Reporting, 9) Cross-Refs (runbook, SLO doc, lifecycle runbook).

## Standards

- Google SRE — blameless postmortems.
- NIST SP 800-61 — incident handling guide (adapted for SaaS-customer reporting).

## Resources

- `logic.prompt`, `README.md`, `references/saas-incident-response-and-postmortem-template.md`.
