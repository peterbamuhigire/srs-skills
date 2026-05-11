# Building Multi-Tenant SaaS Architectures — SRS-Engine Extraction

**Source:** Tod Golding, *Building Multi-Tenant SaaS Architectures: Principles, Practices and Patterns Using AWS*, O'Reilly Media, 2024.

**Lens:** What documents must this engine produce so an AI can write world-class SDLC artifacts for a multi-tenant SaaS system?

## One-line takeaway

A SaaS architecture is defined less by the application plane than by the **control plane** (onboarding, identity, tenant management, metering, billing, deployment, operations) that wraps every tenant — so the engine must produce a distinct family of *tenancy*, *isolation*, *control-plane*, *deployment-model*, *tiering*, and *operations* documents that ordinary SRSs do not capture.

## Distinctive documentation surface this book reveals

### 1. The two-plane model

Every multi-tenant SaaS has a **control plane** and an **application plane**. Documentation must split along this seam:

- **Control plane SRS/HLD** — onboarding service, identity service, tenant management service, billing service, metering service, deployment automation, operations console, analytics. These services exist regardless of business domain. The engine currently has no skill that recognizes them as a category.
- **Application plane SRS/HLD** — the domain microservices that carry tenant context end to end.
- **Plane-integration spec** — how control-plane events (tenant created, tenant suspended, tier changed) propagate into the application plane.

### 2. Tenancy-model decision documents

The book rejects the binary "single-tenant vs. multi-tenant" framing and replaces it with deployment patterns:

| Pattern | Compute | Storage | Doc artefact required |
|---------|---------|---------|-----------------------|
| Full-Stack Silo | dedicated | dedicated | per-tenant infra inventory, blast radius doc, cost-attribution method |
| Full-Stack Pool | shared | shared | noisy-neighbor SLOs, per-tenant cost-attribution method, isolation evidence |
| Mixed-Mode | mix (e.g. shared compute, siloed storage) | mix | per-microservice tenancy decision matrix, isolation evidence |
| Pod | grouped tenants share a stack | grouped | pod assignment policy, pod-rebalancing runbook |
| Account-per-Tenant / VPC-per-Tenant | dedicated cloud account or VPC | dedicated | landing-zone SRS, identity-federation spec, automation runbook |

A **Tenancy Decision Document** must capture: chosen pattern per microservice, drivers (regulatory, performance, isolation, cost, blast radius), trade-offs accepted, and the ADR pointer.

### 3. Tenant lifecycle

The book treats onboarding, tiering, provisioning, suspension, offboarding, and deletion as first-class. Each is a runbook:

- **Onboarding runbook** — automated tenant provisioning, identity bootstrap, tier-specific resource creation, welcome workflow.
- **Tier-change runbook** — upgrade/downgrade resource provisioning, data migration, feature-flag toggles.
- **Suspension runbook** — billing-driven or compliance-driven suspension, what tenant sees, audit trail.
- **Offboarding & deletion runbook** — data export within X days, hard delete with verification, retention obligations.

### 4. Tenant context

Every request must carry tenant context (tenant ID, tier, role, region). The engine should produce a **Tenant Context Specification** covering: token format (JWT claims), propagation across services, audit-logging requirements, fail-safe behavior when context missing.

### 5. Isolation evidence

The book argues isolation is more than "a separate database." Evidence must be produced at multiple layers — network, compute, storage, IAM, code path. The engine should produce a **Tenant Isolation Evidence Pack** showing how cross-tenant access is prevented and how violations are detected.

### 6. Noisy-neighbor SLOs and tiering

Pool models require explicit per-tenant throttling, quotas, and SLO-per-tier documents. Tiering documents must specify what bronze/silver/gold/enterprise tiers each get on compute, storage, feature access, support, and SLA.

### 7. Per-tenant cost attribution

In pool models, cost-attribution is non-obvious. The engine should produce a **Per-Tenant Cost Attribution Method** document — what is metered, how shared costs are allocated, how this feeds finance and pricing.

### 8. Control-plane operations

The control plane is *itself* a system that needs SLOs, runbooks, security architecture, and DR. The engine must not let consultants treat the control plane as an implementation detail.

## Documentation patterns the book recommends

- Diagram-driven (every architectural concept is shown as a topology figure).
- Decision-record-driven (silo vs. pool is the canonical ADR family).
- Runbook-driven for tenant lifecycle.
- SLO-driven (per-tier SLOs exposed in contracts).
- Evidence-driven (isolation is something you must *prove*, not assert).

## Implications for the SDLC-Docs-Engine

1. Add a Phase 03 skill **`10-saas-multi-tenancy-architecture-spec`** that produces a control-plane/application-plane HLD section, plus per-microservice tenancy decision matrix, plus ADR seeds.
2. Add a Phase 06 skill **`07-saas-tenant-lifecycle-runbook`** covering provisioning, tier change, suspension, offboarding, deletion.
3. Add Phase 09 skill **`11-saas-data-isolation-evidence-pack`**.
4. Add cross-cutting templates: `saas-tenancy-decision-template.md`, `saas-nfr-catalog.md`, `saas-slo-and-error-budget-template.md`.
5. Enhance `03-design-documentation/01-high-level-design` with a "SaaS mode" addendum requiring the two-plane decomposition and per-microservice tenancy decision.
6. Enhance `09-governance-compliance/05-architecture-decision-records` with a SaaS-tenancy ADR catalogue.

## Source mapping

- "The SaaS Mindset" (Ch.1) → drives the **Strategic-vision SaaS Definition** addendum.
- "Multi-Tenant Architecture Fundamentals" (Ch.2) → drives the **two-plane HLD addendum** and the control-plane skill.
- "Deployment Models" (Ch.3) → drives the **Tenancy Decision Template** and per-microservice matrix.
- Tiering, noisy-neighbor, cost attribution → drive the **Tiering & SLO** templates.
- Tenant context, isolation, data partitioning → drive the **Isolation Evidence Pack**.
- Onboarding, identity, billing, metering, deployment as control-plane concerns → drive the **Tenant Lifecycle Runbook** family.
