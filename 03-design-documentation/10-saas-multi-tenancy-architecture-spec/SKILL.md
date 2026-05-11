---
name: "saas-multi-tenancy-architecture-spec"
description: "Generate a Multi-Tenancy Architecture Specification for a SaaS system covering control-plane / application-plane decomposition, per-microservice tenancy pattern (silo / pool / mixed / pod / VPC-per-tenant), tenant-context propagation, isolation strategy, noisy-neighbor controls, and ADR seeds per Golding (2024)."
metadata:
  use_when: "Use when the project is a multi-tenant SaaS and the High-Level Design must capture tenancy decisions that will not be expressed adequately by the generic HLD skill."
  do_not_use_when: "Do not use for single-tenant on-prem systems or simple internal tools without tenant boundaries."
  required_inputs: "SRS_Draft.md (Phase 02), HLD.md (must exist as the generic parent), tech_stack.md, PRD.md or Vision_Statement.md, any regulatory/data-residency constraints, business-model context (B2B SMB vs Enterprise vs B2C)."
  workflow: "Read inputs, declare two-plane decomposition, fill the per-microservice tenancy-pattern matrix, write the tenant-context spec, write the isolation strategy, emit ADR seeds, write the Multi_Tenancy_Architecture_Spec.md."
  quality_standards: "Every microservice in scope shall appear in the tenancy-pattern matrix. Every tenancy pattern shall cite the drivers (regulatory, isolation, blast-radius, cost, noisy-neighbor, performance). Every tenant-touching service shall have a documented context-propagation rule and a fail-safe behaviour."
  anti_patterns: "Do not state a tenancy model without naming the drivers. Do not assert isolation; show how it is enforced and detected. Do not skip control-plane services (onboarding, identity, tenant management, metering, billing) on the assumption they are 'infrastructure'."
  outputs: "Multi_Tenancy_Architecture_Spec.md and a set of ADR seeds in projects/<ProjectName>/<phase>/<document>/adr-seeds/."
  references: "Use references/saas-tenancy-decision-template.md, references/saas-control-plane-services.md, and the book-extraction at book-extractions/saas-architectures-srs-extraction.md."
---

# SaaS Multi-Tenancy Architecture Specification Skill

## Overview

This skill produces the SaaS-distinctive architecture artefact that no generic HLD captures: the explicit two-plane decomposition, the per-microservice tenancy-pattern matrix, tenant-context propagation, isolation strategy, noisy-neighbor controls, per-tenant cost-attribution method, and the ADR seeds. It is the canonical Phase 03 SaaS skill.

The skill is anchored in Tod Golding, *Building Multi-Tenant SaaS Architectures* (O'Reilly, 2024). It assumes a generic `HLD.md` already exists (from `01-high-level-design`) and that the present skill augments it with the SaaS-specific viewpoints.

## When to Use

- The project's `vision.md` or `PRD.md` describes a multi-tenant SaaS (B2B, B2C, vertical, horizontal).
- A generic `HLD.md` already exists or will be created in the same Phase 03 run.
- Tenancy decisions, isolation evidence, or per-tenant cost attribution are in scope.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`, `HLD.md`, `projects/<ProjectName>/_context/tech_stack.md`, `PRD.md` |
| **Output** | `projects/<ProjectName>/<phase>/<document>/Multi_Tenancy_Architecture_Spec.md` plus ADR seeds |
| **Tone** | Architectural, decision-driven, evidence-bearing |
| **Standard** | IEEE 1016-2009 Sec 5 (Design Viewpoints); ISO/IEC 25010 (Quality Model) |
| **Source** | Golding, *Building Multi-Tenant SaaS Architectures* (2024) |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| SRS_Draft.md | Phase-02 output dir | Yes | Functional and NFR requirements |
| HLD.md | Phase-03 output dir | Yes | Generic architecture being augmented |
| tech_stack.md | `_context/` | Yes | Cloud / framework constraints |
| PRD.md | Phase-01 output dir | Recommended | Tiering, ICP, business model |
| vision.md | `_context/` | Recommended | Strategic context |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Multi_Tenancy_Architecture_Spec.md | Phase-03 output dir | Full SaaS multi-tenancy spec |
| `adr-seeds/0001-tenancy-pattern-<service>.md` | Phase-03 output dir | One ADR seed per microservice |
| `adr-seeds/0002-control-plane-boundary.md` | Phase-03 output dir | Boundary between control plane and application plane |

## Core Instructions

Follow these nine steps in order. Halt if any required input is missing.

### Step 1: Read context

Read `SRS_Draft.md`, `HLD.md`, `tech_stack.md`, `PRD.md`, `vision.md`. Identify regulatory constraints, data-residency requirements, target ICP segments, expected tier mix, and any "enterprise must have dedicated infra" obligations. Log all source citations.

### Step 2: Declare the two-plane decomposition

Per Golding Ch.2, every SaaS architecture has a **control plane** (onboarding, identity, tenant management, metering, billing, deployment automation, operations, analytics) and an **application plane** (the domain microservices that carry tenant context).

Produce a Mermaid diagram showing the two planes, the services in each, and the events/APIs crossing the boundary. Every service in scope shall be classified as control-plane or application-plane.

```mermaid
flowchart LR
    subgraph CP[Control Plane]
        Onb[Onboarding]
        Idn[Identity]
        TMg[Tenant Management]
        Met[Metering]
        Bil[Billing]
        Dep[Deployment Automation]
        Ops[Operations Console]
    end
    subgraph AP[Application Plane]
        Svc1[Domain Service 1]
        Svc2[Domain Service 2]
        SvcN[Domain Service N]
    end
    CP -- "tenant lifecycle events" --> AP
    AP -- "metering events" --> CP
```

### Step 3: Fill the per-microservice tenancy-pattern matrix

For every microservice in the application plane, fill the following table:

| Service | Compute | Storage | Pattern | Drivers | Trade-offs accepted | ADR ref |
|---------|---------|---------|---------|---------|---------------------|---------|
| Service A | pooled / siloed / pod | pooled / siloed / pod | Full-Stack Pool / Full-Stack Silo / Mixed-Mode / Pod / VPC-per-tenant | regulatory / blast-radius / cost / perf / noisy-neighbor / migration | what was traded away | `0001-tenancy-pattern-service-a.md` |

Patterns are drawn from Golding Ch.3:

- **Full-Stack Silo** — dedicated compute *and* storage per tenant. Highest isolation, simplest cost attribution, hardest cost efficiency.
- **Full-Stack Pool** — shared compute and storage. Best efficiency, requires explicit isolation, noisy-neighbor controls, per-tenant metering.
- **Mixed-Mode** — pool one resource (e.g. compute) while silo another (e.g. storage).
- **Pod** — group N tenants per stack; rebalance as needed.
- **Account-per-Tenant / VPC-per-Tenant** — silo at the cloud-account or network boundary; often used by migrating ISVs or strict-isolation industries.

Every row shall name **at least one** driver from the regulated list. Drivers without measurable thresholds are not drivers — replace with a measurable threshold (e.g. "P95 cross-tenant latency interference < 10 ms" not "low interference").

### Step 4: Write the tenant-context specification

Document the token format, claims (`tenant_id`, `tier`, `region`, `roles`), how the token is issued (control-plane → application-plane), how it is propagated across services (HTTP header, gRPC metadata, async-event envelope), how it is validated at each service boundary, and the fail-safe behaviour when the context is missing or invalid (reject request, audit log, alarm).

Cite SRS-section identifiers for each rule and write a *Verification Procedure* table — how each rule is tested in CI.

### Step 5: Write the isolation strategy

For each tenancy pattern in use, document the isolation enforcement at each layer:

- **Network** — VPC, subnet, security groups, service mesh policy.
- **Compute** — process, container, namespace, dedicated worker, throttling.
- **Storage** — database, schema, row-level security, encryption-key boundary (per-tenant KMS key?), index partitioning.
- **IAM** — IAM role-per-tenant, attribute-based access, signed-context propagation.
- **Code path** — repository query helpers that reject queries without tenant filter, lint rules, runtime assertions.

Cross-link to `09-governance-compliance/11-saas-data-isolation-evidence-pack` which produces the evidence artefact.

### Step 6: Document noisy-neighbor controls and per-tier SLOs

For every pooled service, document:

- Throttling / rate-limit per tenant and per tier.
- Quotas (concurrent jobs, request-rate, queue depth).
- Per-tier SLOs (Bronze / Silver / Gold / Enterprise) for latency, availability, support response.
- Burst headroom and the back-off behaviour.

Cross-link to `06-deployment-operations/08-saas-slo-and-error-budget-doc`.

### Step 7: Document per-tenant cost attribution

For every pooled service, state the method by which infrastructure cost is attributed back to the tenant: metered usage events (API calls, storage GB-month, compute seconds), allocation of shared costs (per-tenant share of base infrastructure), reporting cadence (daily / monthly), and the destination (FinOps dashboard, finance ERP). This feeds the **Pricing & Packaging Spec** and the **Billing & Metering SRS**.

### Step 8: Emit ADR seeds

For each microservice, emit one ADR file at `adr-seeds/0001-tenancy-pattern-<service>.md` using the template at `references/saas-tenancy-decision-template.md`. Each ADR contains: context, decision, status, consequences, drivers, alternatives considered, evidence references, sign-off owners.

Also emit one ADR for the control-plane / application-plane boundary: where API calls cross the boundary, what events propagate, what isolation exists.

### Step 9: Write the spec

Write `Multi_Tenancy_Architecture_Spec.md` with the following sections in order:

1. Two-Plane Decomposition Diagram
2. Control-Plane Services Inventory
3. Application-Plane Services Inventory
4. Per-Microservice Tenancy-Pattern Matrix
5. Tenant Context Specification
6. Isolation Strategy (per layer × per pattern)
7. Noisy-Neighbor & Per-Tier SLOs
8. Per-Tenant Cost Attribution
9. Tenant Lifecycle Event Catalogue (cross-link to lifecycle runbook)
10. ADR Seed Index
11. Traceability Matrix (every section → SRS clause or PRD requirement)

Log the section count and ADR-seed count.

## Output Format

Strict heading order as above. Mermaid for all diagrams. LaTeX for any quota / cost formulas. Tables for the tenancy-pattern matrix and SLOs. No vague adjectives — every NFR has a measurable threshold per `02-requirements-engineering/references/saas-nfr-catalog.md`.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Treating the whole system as one tenancy pattern | Fill the matrix per microservice; mixed-mode is the norm |
| Naming a pattern without drivers | Every row must cite at least one driver from {regulatory, isolation, blast-radius, cost, performance, noisy-neighbor} |
| "Isolation is logical" without enforcement evidence | Cross-link to the Data Isolation Evidence Pack and the test artefacts |
| No noisy-neighbor controls in a pool service | Throttle, quota, back-off, per-tier SLO are mandatory |
| No tenant-context fail-safe | Every service must define the reject + audit behaviour when context is missing |
| Cost attribution missing for pool services | Pool means you cannot tell who is expensive — fix that with metering, not later |

## Verification Checklist

- [ ] Every microservice appears in the tenancy-pattern matrix.
- [ ] Every row cites at least one driver with a measurable threshold.
- [ ] Tenant context spec defines token format, claims, propagation rule, validation rule, fail-safe behaviour.
- [ ] Isolation strategy covers network, compute, storage, IAM, code path for every pooled pattern.
- [ ] Per-tier SLOs exist for every pooled service.
- [ ] Per-tenant cost attribution method exists for every pooled service.
- [ ] One ADR seed exists per microservice plus one for the control-plane boundary.
- [ ] Traceability matrix maps every section to SRS or PRD.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `01-high-level-design` | Consumes the generic HLD as the architectural baseline |
| Upstream | Phase 02 SRS | Consumes NFRs, regulatory constraints |
| Downstream | `02-low-level-design` | Tenancy patterns drive module-level helpers (tenant-aware repos, scoped logging) |
| Downstream | `04-database-design` | Storage tenancy pattern drives schema strategy (separate-DB / separate-schema / shared-schema-RLS) |
| Downstream | `06-deployment-operations/07-saas-tenant-lifecycle-runbook` | Lifecycle events defined here are operationalised in the runbook |
| Downstream | `06-deployment-operations/08-saas-slo-and-error-budget-doc` | Per-tier SLOs declared here feed the SLO doc |
| Downstream | `09-governance-compliance/11-saas-data-isolation-evidence-pack` | Isolation strategy here is the design; the evidence pack is the proof |
| Downstream | `09-governance-compliance/05-architecture-decision-records` | ADR seeds graduate to the ADR catalog |

## Standards

- **IEEE 1016-2009 Sec 5** — Architectural Design Viewpoints.
- **ISO/IEC 25010** — Quality model (capability, performance, security, maintainability, portability).
- **AWS Well-Architected SaaS Lens** — control-plane / application-plane vocabulary.
- **Golding (2024)** — silo / pool / mixed / pod taxonomy.

## Resources

- `logic.prompt` — Executable prompt.
- `README.md` — Quick-start.
- `references/saas-tenancy-decision-template.md` — ADR template per service.
- `references/saas-control-plane-services.md` — Canonical control-plane service catalogue.
- `book-extractions/saas-architectures-srs-extraction.md` — Source synthesis.
