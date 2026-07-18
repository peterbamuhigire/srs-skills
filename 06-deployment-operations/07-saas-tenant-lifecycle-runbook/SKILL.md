---
name: 07-saas-tenant-lifecycle-runbook
description: Use when producing or updating SaaS tenant-lifecycle runbook for provisioning, suspension, reactivation, export, deletion, isolation, and evidence. Use runbook for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# SaaS Tenant Lifecycle Runbook Skill

<!-- dual-compat-start -->
## Use When

- Produce or update SaaS tenant-lifecycle runbook from approved project evidence.
- Resolve decisions about provisioning, suspension, reactivation, export, deletion, isolation, and evidence.
- Prepare a reviewable handoff for SaaS operations and support.

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
| SaaS Tenant-lifecycle Runbook | SaaS operations and support | Each lifecycle transition has authority, idempotency, tenant-isolation checks, audit evidence, and recovery steps. |
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
- Inspection is read-only by default. Create or edit the named project document only when explicitly authorised. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose lifecycle action from verified tenant state and authority and produce the full artefact. | Cross-tenant or irreversible lifecycle errors. |
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

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when each lifecycle transition has authority, idempotency, tenant-isolation checks, audit evidence, and recovery steps.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

Generates the operational runbook covering the SaaS-distinctive tenant lifecycle events. Captures the procedures, automation hooks, manual gates, audit trail, retention obligations, and customer-comms templates that the generic runbook leaves out.

## When to Use

- The project is multi-tenant SaaS.
- The generic `Runbook.md` already exists in Phase 06.
- The `Multi_Tenancy_Architecture_Spec.md` from Phase 03 exists.
- GDPR / POPIA / DPPA or similar privacy-regulation constraints apply (almost always).

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `Multi_Tenancy_Architecture_Spec.md`, `Runbook.md`, `Compliance_Docs.md`, billing & metering spec |
| **Output** | `projects/<ProjectName>/<phase>/<document>/Tenant_Lifecycle_Runbook.md` and `playbooks/*.md` |
| **Tone** | Procedural, audit-grade, customer-comms-aware |
| **Standard** | SRE Best Practices; GDPR Art.17 (deletion); POPIA / DPPA equivalents |

## Output Files

| File | Description |
|------|-------------|
| Tenant_Lifecycle_Runbook.md | Master runbook indexing each stage |
| playbooks/01-provisioning.md | Provisioning procedure |
| playbooks/02-tier-change.md | Upgrade / downgrade procedure |
| playbooks/03-suspension.md | Suspension procedure (billing / compliance) |
| playbooks/04-reactivation.md | Reactivation procedure |
| playbooks/05-offboarding.md | Self-service offboarding |
| playbooks/06-data-export.md | Customer-requested data export (GDPR portability) |
| playbooks/07-hard-delete.md | Hard delete with verification |
| playbooks/08-retention.md | Retention obligations & destruction schedule |

## Core Instructions

### Step 1: Read inputs

Read the tenancy spec, generic runbook, compliance docs. Identify which lifecycle events the system supports, which control-plane services own each, and what retention obligations apply (per region, per data class).

### Step 2: Generate the tenant-lifecycle event catalogue

| Event | Trigger | Source service | Downstream consumers | SLA |
|-------|---------|----------------|----------------------|-----|
| `tenant.created` | Signup or sales-led | Onboarding | App services, billing, comms | < 5 min self-serve / < 1 business day enterprise |
| `tenant.tier_changed` | Admin upgrade/downgrade | Tenant Management | All app services | < 10 min |
| `tenant.suspended` | Billing failure / compliance / admin | Tenant Management | All app services, comms | immediate |
| `tenant.reactivated` | Payment / admin | Tenant Management | All app services, comms | immediate |
| `tenant.offboarded` | Customer cancellation | Tenant Management | All app services, billing, comms | immediate, with grace |
| `tenant.export_requested` | Customer / DSAR | Operations | Data services | per regulation (GDPR: 30 days) |
| `tenant.hard_deleted` | After grace period | Tenant Management | All app services, audit | per retention policy |

### Step 3: For each stage produce a playbook

Every playbook MUST contain:

1. **Trigger** — who or what initiates.
2. **Pre-conditions** — billing status, tier, contractual state, regulatory holds (legal-hold suspends deletion).
3. **Actor** — automated / on-call / customer success / privacy officer.
4. **Automated steps** — control-plane orchestration in order.
5. **Manual gates** — when human approval is required (high-tier offboarding, legal hold).
6. **Per-service propagation** — which app-plane services receive the event, what they MUST do.
7. **Verification** — how success is confirmed (post-conditions, smoke tests, query asserting absence/presence).
8. **Rollback / abort** — if the procedure fails mid-way, what state is the tenant in, who is paged.
9. **Audit-trail entry** — what is logged, where, retention.
10. **Customer-comms message** — template (email subject, body, in-app banner).
11. **Retention-policy reference** — link to the retention/destruction schedule.

### Step 4: Provisioning playbook specifics

- Idempotency rule — replay of `tenant.created` MUST NOT create duplicate resources.
- Tier-aware resource fan-out — Bronze pool stack vs Enterprise dedicated VPC.
- Identity bootstrap — initial admin user, password-reset link, MFA enrolment policy.
- Cost-estimate snapshot at provisioning time (feeds FinOps).
- Welcome workflow enqueue (Onboarding Journey Spec).

### Step 5: Suspension playbook specifics

- Trigger classes — billing past due (N days), compliance (DPA breach), admin (security incident on tenant side).
- Sequence — feature-flag toggle (read-only), comms sent before suspension, blockings at API gateway, audit entry.
- Tenant-visible UX — what the suspended tenant sees, how they self-recover.
- Reactivation path.

### Step 6: Offboarding + data-export + hard-delete

This is the regulated path. GDPR Art.17 / Art.20 obligations:

- **Soft delete** at offboarding — data preserved for the contractual grace period (e.g. 30 days), tenant locked out.
- **Customer-initiated export** — DSAR within statutory window (30 days GDPR). Document the export format (JSON, CSV, per-table dump), the delivery mechanism (signed URL, expires in 7 days), the authentication required, the audit entry.
- **Hard delete** — at end of grace, run destruction across every data store (primary DB, replicas, backups within retention, search index, cache, object storage, log archives where personally identifiable), assert zero rows remain via a verification query, sign the destruction certificate, retain certificate for required years (typically 5-7).
- **Legal hold** — explicit pre-condition check. If legal hold is set on a tenant, hard delete MUST NOT proceed.
- **Backups** — backup data containing the tenant remains until the backup's own retention expires; document this.

### Step 7: Write the master runbook

`Tenant_Lifecycle_Runbook.md` shall index every stage, link each playbook, document the event catalogue, list audit-trail destinations, list retention obligations per region, and list customer-comms templates. Cross-link to `09-governance-compliance/13-saas-dpa-and-privacy-doc-set`.

## Verification Checklist

- [ ] Every event in the catalogue has a playbook.
- [ ] Every playbook has trigger, pre-conditions, actor, steps, manual gates, verification, rollback, audit, customer-comms, retention reference.
- [ ] Hard-delete playbook proves destruction across every data store and produces a destruction certificate.
- [ ] Legal-hold pre-condition is enforced on hard-delete.
- [ ] Customer-comms templates exist for every stage that touches the customer.
- [ ] Audit-trail destination is named for every state change.
- [ ] Retention obligations are stated per region and per data class.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `03-design-documentation/10-saas-multi-tenancy-architecture-spec` | Provides the event catalogue and pattern context |
| Upstream | `06-deployment-operations/02-runbook` | Generic runbook is the parent |
| Parallel | `09-governance-compliance/13-saas-dpa-and-privacy-doc-set` | Retention and DSAR obligations |
| Parallel | `09-governance-compliance/11-saas-data-isolation-evidence-pack` | Hard-delete verification feeds the evidence pack |
| Downstream | `08-end-user-documentation/05-saas-customer-success-playbook` | Customer-comms templates flow into CS plays |

## Standards

- **SRE Best Practices** — Google Site Reliability Engineering.
- **GDPR Art.17 / Art.20** — Right to erasure / Right to portability.
- **POPIA s.14, s.23** — Retention and access rights (South Africa).
- **DPPA 2019** — Uganda Data Protection and Privacy Act.

## Resources

- `logic.prompt` — Executable prompt.
- `README.md` — Quick-start.
- `references/saas-tenant-lifecycle-runbook-template.md` — Master template.
