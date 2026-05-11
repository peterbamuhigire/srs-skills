---
name: "saas-tenant-lifecycle-runbook"
description: "Generate an operational runbook covering the SaaS tenant lifecycle: provisioning, tier change, suspension, reactivation, offboarding, data export, hard delete, and retention obligations — each with detection, procedure, verification, audit-trail, and customer-comms requirements."
metadata:
  use_when: "Use when the project is a multi-tenant SaaS and the engine must produce the tenant-lifecycle operational runbook beyond what the generic runbook captures."
  do_not_use_when: "Do not use for single-tenant systems."
  required_inputs: "Multi_Tenancy_Architecture_Spec.md, Runbook.md (generic), Compliance_Docs.md (for retention/deletion rules), DPA / privacy obligations, billing & metering spec."
  workflow: "Read inputs, populate lifecycle event catalogue, write per-stage procedures with detection / actions / verification / customer-comms / audit, write Tenant_Lifecycle_Runbook.md."
  quality_standards: "Every lifecycle stage shall have: trigger, pre-conditions, actor, automated steps, manual gates, verification, rollback, audit-trail entry, customer-comms message, retention-policy reference."
  anti_patterns: "Do not write a generic 'create tenant' procedure with no failure handling. Do not skip the delete procedure on the assumption the cloud handles it. Do not omit audit-trail or retention reference."
  outputs: "Tenant_Lifecycle_Runbook.md plus per-procedure playbooks under playbooks/."
  references: "Use references/saas-tenant-lifecycle-runbook-template.md and book-extractions/saas-architectures-srs-extraction.md."
---

# SaaS Tenant Lifecycle Runbook Skill

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
