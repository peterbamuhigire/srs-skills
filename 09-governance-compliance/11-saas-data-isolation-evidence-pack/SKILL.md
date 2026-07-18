---
name: 11-saas-data-isolation-evidence-pack
description: Use when proving tenant isolation across identity, application, database, storage, cache, queue, analytics, support, and backup boundaries. Use evidence-pack-builder for generic packaging and DPA/privacy-doc-set for processing obligations.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# SaaS Data Isolation Evidence Pack Skill

<!-- dual-compat-start -->

## Use When

- Use when proving tenant isolation across identity, application, database, storage, cache, queue, analytics, support, and backup boundaries. Use evidence-pack-builder for generic packaging and DPA/privacy-doc-set for processing obligations.

## Do Not Use When

- Do not use for single-tenant or internal-only systems.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Target sources: Multi_Tenancy_Architecture_Spec.md, Compliance_Docs.md, Risk_Assessment.md, the Test_Plan.md, the security test results. | Project owner, approved workspace artefacts, or accountable control owner | Yes | Stop dependent claims; list the missing item, owner, and consequence. For review checks, record `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Provenance, integrity, period, or control mapping is absent | Quarantine the item and record the gap | Misleading or tampered evidence |
| Evidence meets scope, integrity, and traceability checks | Index it for the named consumer | Unreviewable evidence dumps |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| SaaS Data Isolation Evidence Pack | Accountable reviewer, control owner, auditor, or release authority | Every claimed isolation mechanism shall have a named evidence artefact (test result, code review, infra config snapshot, audit log). |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| SaaS Data Isolation Evidence Pack evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Every claimed isolation mechanism shall have a named evidence artefact (test result, code review, infra config snapshot, audit log).
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing SaaS Data Isolation Evidence Pack from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if provenance, integrity, period, or control mapping is absent, quarantine the item and record the gap. Record the evidence and result in the validation record; this avoids misleading or tampered evidence.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

Auditors, enterprise procurement, and regulators ask "prove tenants are isolated." This skill produces the pack that answers — for every layer of the architecture — with named, attachable, time-stamped evidence.

## Core Instructions

### Step 1: Inventory tenancy patterns

For each microservice list its pattern (silo / pool / mixed / pod / VPC-per-tenant) and the layers requiring evidence.

### Step 2: Enumerate isolation enforcement per layer

For each layer × pattern combination list the mechanism in place:

| Layer | Mechanism | Service | Evidence artefact | Last verified |
|-------|-----------|---------|-------------------|---------------|
| Network | Per-tenant security group | OrderSvc | `evidence/net-sg-snapshot-YYYYMMDD.json` | |
| Compute | Per-tenant K8s namespace | FulfilSvc | `evidence/k8s-namespace-list.txt` | |
| Storage | Row-level security on tenant_id | All | `evidence/rls-policy-dump.sql` + `evidence/rls-test-results.json` | |
| Storage (Enterprise) | Per-tenant DB / per-tenant KMS key | Enterprise tenants | `evidence/kms-key-list.csv` + `evidence/key-rotation-log.csv` | |
| IAM | Signed JWT with tenant_id claim validated at every boundary | All | `evidence/jwt-validation-test.json` | |
| Code path | TenantScopedRepository + lint rule blocking raw queries | All | `evidence/static-analysis-report.html` + `evidence/repo-base-class.md` | |
| Audit | Cross-tenant impersonation logged with reason | Operations console | `evidence/impersonation-audit-30d.csv` | |
| Test | Penetration test for cross-tenant access | All | `evidence/pentest-YYYYQ.pdf` | |

### Step 3: List test artefacts

Required tests, each producing evidence:

- Negative-path test: request without tenant context → 401/403, audit entry.
- Tampered-context test: forged tenant_id claim → rejected.
- Cross-tenant fuzz test: tenant A query attempts to access tenant B rows → blocked, audit entry.
- Noisy-neighbor test: tenant A saturates → SLO impact on tenant B ≤ NFR threshold.
- Log-access test: tenant A's CSM cannot view tenant B's logs.
- Hard-delete verification: post-delete query returns 0 rows across all stores.

### Step 4: Map to control frameworks

| Control | Framework | NFR | Evidence ref |
|---------|-----------|-----|--------------|
| CC6.1 Logical access | SOC 2 | NFR-IDN-001 | |
| CC6.6 Boundary protection | SOC 2 | NFR-ISO-002 | |
| A.13.1 Network controls | ISO 27001 | NFR-ISO-001 | |
| A.18.1 Compliance with legal | ISO 27001 | NFR-RES-001 | |
| Art.32 Security of processing | GDPR | NFR-ISO-001 | |
| Art.17 Right to erasure | GDPR | NFR-LCY-004 | |
| Reg.12 DPIA | DPPA (UG) | DPIA artefact | |

### Step 5: Assemble the pack

`Data_Isolation_Evidence_Pack.md` with sections: 1) Scope (services, regions, period), 2) Tenancy Pattern Inventory, 3) Layered Isolation Mechanisms, 4) Evidence Index, 5) Test Results Summary, 6) Control Framework Mapping, 7) Open Gaps & Remediation, 8) Attestation (sign-off).

Attach all artefacts under `evidence/`.

### Step 6: Refresh cadence

State the cadence: every test refreshed at least quarterly; pack republished annually or on major architecture change.

## Standards

- SOC 2 (Trust Services Criteria CC6, CC7).
- ISO/IEC 27001 (A.9, A.13, A.18).
- GDPR Art.32, Art.17, Art.20.
- DPPA 2019 (Uganda), POPIA (South Africa).

## Resources

- `logic.prompt`, `README.md`, `references/saas-data-isolation-evidence-pack-template.md`.
