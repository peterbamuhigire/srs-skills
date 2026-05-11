# SaaS Test Strategy Addendum

Supplements the generic `01-test-strategy` skill when the project is a multi-tenant SaaS. Adds the SaaS-distinctive test families that a vanilla test strategy will not cover.

## A. Tenant isolation test family

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| Negative-path (no tenant ctx) | every CI run | Platform | 100% rejection |
| Tampered-context (forged claim) | every CI run | Platform | 100% rejection |
| Cross-tenant fuzz (10k attempts) | weekly | Security | 0 leakage |
| Cross-tenant log access | quarterly | Security | 0 visibility |
| Cross-tenant cache leak | quarterly | Platform | 0 key collision |
| Per-tenant KMS key isolation (Enterprise) | quarterly | Security | passes |
| External pentest (cross-tenant scope) | annually | external | no findings ≥ Medium |

## B. Noisy-neighbor test family

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| Pool saturation: one tenant 5× load | monthly | Platform | cross-tenant interference P95 ≤ 10 ms |
| Quota enforcement | per release | Platform | quota fires within 1 s |
| Throttle fairness | monthly | Platform | per-tier RPS within ±5% of declared |

## C. Tenant-context propagation tests

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| End-to-end ctx propagation across N services | per release | Platform | tenant_id present in every log line |
| Async queue ctx propagation | per release | Platform | jobs without ctx rejected |
| Webhook-out ctx | per release | Platform | ctx in signature |

## D. Billing-event correctness tests

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| Meter emission per priced action | per release | Billing | 100% emission |
| Reconciliation deviation | nightly | RevOps | ≤ 0.1% |
| Idempotency on replay | per release | Billing | zero duplicates |
| Tier change propagation | per release | Platform | all services see new tier within 10 min |
| Refund / credit ERP entry | per refund | Finance | journal posted |

## E. Tenant-lifecycle tests

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| Provisioning idempotency | per release | Platform | replay produces no duplicate |
| Suspension UX | per release | Product | tenant locked + comms sent |
| Reactivation | per release | Platform | full access restored ≤ 10 min |
| Customer-initiated data export | quarterly | Privacy | export delivered within SLA |
| Hard-delete verification | per release | Privacy | zero rows post-delete |
| Legal-hold blocks delete | quarterly | Privacy | delete blocked |

## F. Dunning / churn-recovery tests

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| Payment-failure → dunning sequence fires | per release | Billing | full sequence triggered |
| Recovery → tenant restored | per release | Billing | tenant active |

## G. Compliance / privacy tests

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| DSAR turnaround | quarterly | Privacy | within statutory window |
| Breach-notification drill | annually | Security + Legal | ≤ 72 h to authority |

## H. Performance & SLO tests

| Test | Frequency | Owner | Pass criterion |
|------|-----------|-------|----------------|
| Per-tier latency SLO | nightly synthetic | SRE | meets SLO doc |
| Region failover | quarterly | SRE | RTO < target |

## I. Cross-link

- Multi_Tenancy_Architecture_Spec.md
- SLO_And_Error_Budget_Doc.md
- Billing_And_Metering_Spec.md
- Tenant_Lifecycle_Runbook.md
- Data_Isolation_Evidence_Pack.md
- SaaS NFR Catalog (Phase 02 ref)
