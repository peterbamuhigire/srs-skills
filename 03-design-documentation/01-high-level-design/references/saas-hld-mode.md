# SaaS HLD Mode

This addendum activates when the project is a multi-tenant SaaS. The base `01-high-level-design` skill must include the following additional sections in the HLD.

## Required additional sections

### S1. Two-Plane Decomposition

A diagram showing the control plane (onboarding, identity, tenant management, metering, billing, deployment automation, operations console, analytics, notification) and the application plane (the domain microservices). Every in-scope service classified.

### S2. Tenant Context Propagation summary

How tenant context (signed JWT with `tenant_id`, `tier`, `region`, `roles`) is issued, propagated, validated, and fail-safe-rejected. Cross-link to the dedicated `Multi_Tenancy_Architecture_Spec.md` for the full spec.

### S3. Tenancy Pattern Summary Table

One row per microservice with: compute placement, storage placement, pattern (silo / pool / mixed / pod / VPC-per-tenant), and one-line driver. Full matrix lives in the multi-tenancy spec.

### S4. Isolation Strategy Summary

A one-paragraph summary of isolation enforcement across layers (network, compute, storage, IAM, code path, audit). Detail in the multi-tenancy spec and evidence pack.

### S5. SaaS Cross-Cutting Concerns

- Tenant-scoped logging.
- Per-tenant metrics + cost attribution.
- Per-tier rate limits and quotas.
- Per-tier SLOs (cross-link to SLO doc).
- Tenant-lifecycle event bus.

## Required cross-links

- `Multi_Tenancy_Architecture_Spec.md`
- `Pricing_And_Packaging_Spec.md`
- `Billing_And_Metering_Spec.md`
- `SLO_And_Error_Budget_Doc.md`
- `Tenant_Lifecycle_Runbook.md`
- `Data_Isolation_Evidence_Pack.md`

## Verification additions

- [ ] Two-plane diagram present.
- [ ] Every microservice classified control-plane or application-plane.
- [ ] Tenant-context propagation summary present.
- [ ] Tenancy-pattern summary table present.
- [ ] Isolation strategy summary present.
- [ ] Cross-links to all SaaS-specific docs present.

## Trigger

Use this addendum whenever vision.md or PRD.md describes a multi-tenant SaaS, or when `Pricing_And_Packaging_Spec.md` exists for the project.
