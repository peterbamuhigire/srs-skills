# SaaS Definition-of-Done Addendum

Supplements the generic `02-definition-of-done` skill when the project is a multi-tenant SaaS. Adds mandatory SaaS hygiene items.

## A. Tenant-context hygiene

- [ ] Every new API endpoint validates `tenant_id` in the signed context.
- [ ] Every new query uses the `TenantScopedRepository` or has an explicit cross-tenant tag with reviewer approval.
- [ ] Every new log call includes `tenant_id`.
- [ ] Every new cache key is `tenant_id`-prefixed.
- [ ] Every new background job carries tenant context in the payload.

## B. Billing & metering hygiene

- [ ] If the change affects a priced action, the meter event emission is in place and tested.
- [ ] If the change affects a quota, the tier-aware enforcement is server-side.
- [ ] If the change touches a price-book entry, an ADR + versioned price-book file is updated.

## C. Isolation regression

- [ ] Cross-tenant test suite remains green.
- [ ] No new code path introduces a query without a tenant filter.

## D. Observability

- [ ] If the change emits a new metric, it appears on the relevant dashboard.
- [ ] If the change introduces a new failure mode, an alert exists.

## E. Lifecycle compatibility

- [ ] Schema migration is backward-compatible across at least one prior release.
- [ ] If the change affects a tenant-lifecycle event, the lifecycle runbook is updated.

## F. Compliance

- [ ] If the change touches personal data, ROPA is updated; retention rule applies; DSAR / erasure works.
- [ ] If the change introduces a new sub-processor, the public list is updated with 30 days notice.

## G. Customer comms

- [ ] If the change affects user UX visibly, release notes are drafted.
- [ ] If the change affects pricing or terms, customer-comms is queued by Marketing/Lifecycle.

## H. Cross-link

- Multi_Tenancy_Architecture_Spec.md
- Billing_And_Metering_Spec.md
- Tenant_Lifecycle_Runbook.md
- DPA_And_Privacy_Pack.md
