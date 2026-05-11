# Canonical Control-Plane Services for Multi-Tenant SaaS

Source: Golding (2024), Chapters 2 and 5.

A complete control plane has the following service families. Each project shall declare which services it implements, which it defers, and which it outsources to a vendor (Auth0, Stripe, etc.).

## 1. Onboarding service

- Accepts new-tenant signup (self-serve, sales-led, or API).
- Provisions tenant record, initial admin user, default tier, default region.
- Triggers tier-specific resource provisioning (DB schema, storage bucket, dedicated stack, etc.).
- Emits `tenant.created` event.
- Optionally schedules welcome workflow.

## 2. Identity service

- Issues tokens (signed JWT with `tenant_id`, `tier`, `region`, `roles`).
- Validates tokens at the boundary.
- Federates with tenant IdPs (SAML, OIDC) — enterprise tier.
- Owns role-based or attribute-based access.

## 3. Tenant Management service

- CRUD on tenants (status, tier, region, contact, contract).
- Handles tier changes (upgrade / downgrade).
- Handles suspension and offboarding state transitions.
- Source of truth for tenant metadata; emits state-change events.

## 4. Metering service

- Ingests usage events from application-plane services.
- Aggregates per-tenant, per-period.
- Feeds billing and FinOps dashboards.
- Retention: 13 months minimum (raw events); 7 years (aggregates) for finance.

## 5. Billing service

- Consumes meters + tier definitions + price book.
- Generates invoices (or hands to Stripe / Chargebee / Recurly).
- Manages dunning, payment failures, refunds.
- Reports revenue (recognised, deferred, RPO) to ERP.

## 6. Deployment automation

- Per-tenant or per-pod provisioning (Terraform, CloudFormation, Helm).
- Tier-aware (Bronze pool deploy → existing stack; Enterprise silo → new account).
- Schema-migration orchestration across all tenant DBs.

## 7. Operations console

- Per-tenant operational view (last activity, health, support cases).
- Internal-only access for support and SRE.
- Audit-logged tenant-impersonation for diagnostics.

## 8. Analytics service

- Cross-tenant aggregate analytics for product (usage, adoption, churn signals).
- Strict separation from tenant-facing reporting.
- Feeds customer-success health scoring.

## 9. (Optional) Notification / comms service

- Owns transactional and lifecycle email/SMS/push.
- Honours tenant region / data-residency rules.
- Integrates with the Lifecycle Email Strategy doc.

## 10. (Optional) Status / Trust service

- Public status page.
- Trust-center attestations.
- Incident comms.

## Coverage matrix (per project)

| Service | Implemented | Deferred | Outsourced to | Owner |
|---------|-------------|----------|---------------|-------|
| Onboarding | | | | |
| Identity | | | | |
| Tenant Management | | | | |
| Metering | | | | |
| Billing | | | | |
| Deployment Automation | | | | |
| Operations Console | | | | |
| Analytics | | | | |
| Notification | | | | |
| Status / Trust | | | | |
