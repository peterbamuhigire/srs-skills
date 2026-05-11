---
name: "saas-data-isolation-evidence-pack"
description: "Generate the auditor-grade Data Isolation Evidence Pack proving that tenant data and tenant access are isolated at each layer — network, compute, storage, IAM, code path, audit — with control mappings to SOC 2, ISO 27001, GDPR, and the tenant-isolation NFR catalogue."
metadata:
  use_when: "Use when a SaaS must demonstrate isolation to enterprise buyers, auditors (SOC 2 / ISO 27001), or regulators (GDPR DPA / DPPA)."
  do_not_use_when: "Do not use for single-tenant or internal-only systems."
  required_inputs: "Multi_Tenancy_Architecture_Spec.md, Compliance_Docs.md, Risk_Assessment.md, the Test_Plan.md, the security test results."
  workflow: "Inventory tenancy patterns, enumerate isolation enforcement per layer, list evidence artefacts, map to control frameworks, assemble the pack."
  quality_standards: "Every claimed isolation mechanism shall have a named evidence artefact (test result, code review, infra config snapshot, audit log)."
  anti_patterns: "Do not write 'isolation is logical' without showing the enforcement code path and the test that proves it."
  outputs: "Data_Isolation_Evidence_Pack.md and an `evidence/` index of attached artefacts."
  references: "references/saas-data-isolation-evidence-pack-template.md"
---

# SaaS Data Isolation Evidence Pack Skill

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
