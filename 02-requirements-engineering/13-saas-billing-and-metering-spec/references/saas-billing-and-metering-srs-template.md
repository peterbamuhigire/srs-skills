# SaaS Billing & Metering SRS Template

## 1. Metered event catalogue

| Event | Schema | Granularity | Source | Sink | Retention raw / agg | Used for | Tenant fields |
|-------|--------|-------------|--------|------|---------------------|----------|---------------|
| `api.request.completed` | tenant_id, endpoint, ts, status, bytes_in, bytes_out, duration_ms | per request | API Gateway | metering-bus | 13 mo / 7 y | quota + per-call price + analytics | tenant_id, tier, region, trace_id |
| `storage.snapshot` | tenant_id, bytes, ts | hourly | Storage | metering-bus | 13 mo / 7 y | GB-hour price | tenant_id, tier, region |
| `seat.assigned` | tenant_id, user_id, ts, role | per change | Identity | metering-bus | 13 mo / 7 y | per-seat price | tenant_id |
| `feature.used` | tenant_id, feature_id, ts | per use | App | metering-bus | 13 mo / 7 y | tier enforce + analytics | tenant_id, tier |
| `compute.job.completed` | tenant_id, job_id, cpu_seconds, mem_gb_seconds | per job | Compute | metering-bus | 13 mo / 7 y | usage price | tenant_id, tier |

## 2. Tenant context rules

- Mandatory: every event has `tenant_id`.
- Mandatory billable: also `tier`, `region`, `trace_id`.
- Bus ingress rejects events without `tenant_id` and writes a `metering.reject` event with the source service.

## 3. Transport

- Bus: append-only (Kafka / Kinesis / SQS-FIFO).
- Partition key: `tenant_id`.
- Delivery: at-least-once with idempotency key `{source}:{event_id}`.
- Raw retention: 13 months.
- Aggregate retention: 7 years.

## 4. Aggregation & pricing engine

- Rollups: minute → hour → day → month.
- Pricing engine inputs: aggregates + versioned tier price book + contract overrides → invoice line items.
- Price-book versioning: every change is an ADR + a versioned JSON file in `price-books/`.

## 5. Revenue recognition (ASC 606 / IFRS 15)

For each price-list line declare:

| Line item | Performance obligation | Recognition pattern | Trigger |
|-----------|------------------------|---------------------|---------|
| Subscription (per tier) | Right to access SaaS | Ratable over contract term | Daily accrual |
| Professional services | Onboarding milestones | Point-in-time per milestone | Milestone acceptance |
| Usage overage | Consumption of meter | Point-in-time | Invoice generation |
| One-time setup | Activation event | Point-in-time | Activation |

## 6. Dunning sequence

| Day offset | Action | Channel | Tenant state |
|------------|--------|---------|--------------|
| D+0 | Payment reminder | email | active |
| D+3 | First warning | email + in-app | active |
| D+7 | Second warning + read-only flag | email + in-app banner | read-only |
| D+14 | Suspension | email + suspension banner | suspended |
| D+45 | Offboarding initiated | email + final notice | offboarding |

## 7. Refunds & credits

- Refund authority: CSM up to $5k; Director up to $25k; CFO above.
- Credit (service-credit from SLA): applied within 1 invoice cycle, expires at contract end.
- Every refund/credit creates an ERP journal entry tagged with reason code.

## 8. Audit & reconciliation

- Daily reconciliation: meter aggregate vs raw count vs invoiced amount.
- Discrepancy alarm: > 0.1% deviation pages RevOps.
- Annual external audit on revenue (typical for Series B+ or public-co track).

## 9. ERP / finance handoff

- Cadence: daily journals; monthly close package.
- Format: CSV initially; API once mature.
- Meter-to-GL mapping: per-meter table, owned by Finance, reviewed quarterly.
- Period-end cutoff: 2 business days after month-end; late events accrue to next period.
