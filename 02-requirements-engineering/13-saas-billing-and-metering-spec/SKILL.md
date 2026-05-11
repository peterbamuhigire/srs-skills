---
name: "saas-billing-and-metering-spec"
description: "Generate a SaaS Billing & Metering Specification: the event catalogue, granularity, tenant-context propagation, transport bus, retention, aggregation, ERP/finance handoff, revenue-recognition rules per ASC 606 / IFRS 15, dunning, refund/credit handling — all as testable requirements."
metadata:
  use_when: "Use for any SaaS where usage, seats, features, or any consumption is metered for billing or for tier enforcement."
  do_not_use_when: "Do not use for flat-fee internal tools with no usage instrumentation."
  required_inputs: "PRD.md, vision.md, pricing & packaging spec, Multi_Tenancy_Architecture_Spec.md (or HLD.md), tech_stack.md."
  workflow: "Catalogue metered events, define granularity and tenant-context fields, define transport and retention, define aggregation and pricing engine inputs, define revenue-recognition rules, define dunning and refund flows, write the spec."
  quality_standards: "Every meter shall have: event name, schema, granularity, source service, sink, retention, used-for. Every revenue rule shall cite ASC 606 / IFRS 15 trigger."
  anti_patterns: "Do not define meters without retention. Do not skip tenant-context propagation on events. Do not write 'usage-based' without naming the unit and the formula."
  outputs: "Billing_And_Metering_Spec.md."
  references: "references/saas-billing-and-metering-srs-template.md, references/saas-revenue-recognition-spec-template.md"
---

# SaaS Billing & Metering Spec Skill

## Overview

Generates the requirements specification for the SaaS billing-and-metering pipeline. Sourced from Mersch (financial-metrics rigor) and Golding (control-plane responsibilities).

## Core Instructions

### Step 1: Inventory metered events

For every billable or quota-limited action, produce a row:

| Event name | Schema | Granularity | Source service | Sink | Retention raw / aggregate | Used for | Tenant fields |
|------------|--------|-------------|----------------|------|---------------------------|----------|---------------|
| `api.request.completed` | {tenant_id, endpoint, ts, status, bytes_in, bytes_out, duration_ms} | per request | Gateway | metering bus | 13 mo / 7 y | rate limit + per-call pricing + analytics | tenant_id, tier |
| `storage.snapshot` | {tenant_id, bytes_used, ts} | hourly | Storage service | metering bus | 13 mo / 7 y | GB-hour pricing | tenant_id, tier |
| `seat.assigned` | {tenant_id, user_id, ts, role} | per change | Identity | metering bus | 13 mo / 7 y | per-seat pricing | tenant_id |
| `feature.used` | {tenant_id, feature_id, ts} | per use | App services | metering bus | 13 mo / 7 y | tier enforcement + analytics | tenant_id, tier |

### Step 2: Tenant-context propagation rules

Every event MUST include `tenant_id`. Every billable event MUST also include `tier`, `region`, and source `trace_id`. Events missing `tenant_id` MUST be rejected at the bus ingress and logged.

### Step 3: Transport, ordering, retention

- Transport: append-only event bus (Kafka / Kinesis / SQS-FIFO).
- Ordering: per-tenant partition key.
- Delivery: at-least-once with idempotency keys.
- Retention raw: 13 months (audit-able billing dispute window).
- Retention aggregates: 7 years (SOX / financial-records).

### Step 4: Aggregation & pricing engine

- Rollups: minute → hour → day → month per tenant per meter.
- Pricing engine: consumes aggregates + tier price book + contract overrides → produces invoice line items.
- Tier price book is versioned; price changes require a versioned price book and an ADR.

### Step 5: Revenue-recognition rules (ASC 606 / IFRS 15)

- Identify the contract.
- Identify performance obligations (subscription, professional services, usage overages).
- Determine transaction price.
- Allocate to performance obligations.
- Recognise revenue as obligations satisfied (typically subscription ratable, services on milestone, usage on consumption).

Document for each price-list line: revenue-recognition pattern (ratable / point-in-time / milestone / usage).

### Step 6: Dunning, refunds, credits

- Dunning sequence: D+0 reminder, D+3 first warning, D+7 second warning + read-only flag, D+14 suspension, D+45 offboarding.
- Refunds: who can issue, dollar thresholds, audit, ERP entry.
- Credits (service-credit from SLA breach): how applied, expiration, ERP entry.

### Step 7: Audit & reconciliation

- Daily reconciliation: metering aggregate vs gateway raw count vs charged amount.
- Discrepancy alarm threshold: 0.1%.
- Annual external audit (for series-B+ companies).

### Step 8: ERP / finance handoff

- Export cadence (daily journals).
- Format (CSV / API / Avro).
- Mapping: meter → GL account → cost centre.
- Period-end close cutoff rules.

### Step 9: Write the spec

`Billing_And_Metering_Spec.md` with sections: 1) Metered Event Catalogue, 2) Tenant Context Rules, 3) Transport / Retention / Ordering, 4) Aggregation & Pricing Engine, 5) Revenue Recognition (ASC 606 / IFRS 15), 6) Dunning / Refunds / Credits, 7) Audit & Reconciliation, 8) ERP Handoff, 9) Traceability to PRD pricing and SRS NFRs.

## Standards

- ASC 606 / IFRS 15 — Revenue recognition.
- SOX (for public-co targets) — internal controls over financial reporting.
- ISO/IEC 25010 — quality (correctness as an SLI).

## Resources

- `logic.prompt`, `README.md`, `references/saas-billing-and-metering-srs-template.md`, `references/saas-revenue-recognition-spec-template.md`.
