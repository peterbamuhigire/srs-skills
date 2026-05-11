---
name: "saas-slo-and-error-budget-doc"
description: "Generate the SaaS SLO and Error-Budget Specification: SLIs per service, per-tier SLO targets (Bronze / Silver / Gold / Enterprise), error-budget math, burn-rate alerts, freeze rules, and the mapping from internal SLOs to customer-facing SLA commitments."
metadata:
  use_when: "Use for any SaaS where per-tier SLO commitments will be made to customers, or where SRE error-budget discipline will be operated."
  do_not_use_when: "Do not use for internal-only tools or where no tiering / SLA exists."
  required_inputs: "Multi_Tenancy_Architecture_Spec.md, Monitoring_Setup.md, quality_standards.md, pricing & packaging spec, PRD.md."
  workflow: "Define SLIs, set per-tier SLO targets, compute error budgets, define burn-rate alerts, define release/feature freeze rules, map SLOs to customer SLAs."
  quality_standards: "Every customer-facing tier shall have its own SLO row. Every SLI shall be measurable, sourced from a named metric, and sampled at a stated cadence."
  anti_patterns: "Do not write 'three nines uptime' without the SLI definition. Do not omit the customer-SLA mapping. Do not skip burn-rate alerts."
  outputs: "SLO_And_Error_Budget_Doc.md."
  references: "Use references/saas-slo-and-error-budget-template.md."
---

# SaaS SLO and Error-Budget Doc Skill

## Overview

Produces the SLO/error-budget document for a SaaS system, with per-tier targets and customer-SLA mapping. Anchored in Google SRE practice and Golding (2024) tiering.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | Multi_Tenancy_Architecture_Spec.md, Monitoring_Setup.md, quality_standards.md, pricing & packaging spec |
| **Output** | `SLO_And_Error_Budget_Doc.md` |
| **Standard** | Google SRE / ISO/IEC 25010 |

## Core Instructions

### Step 1: Inventory SLIs

For every service-tier combination, list Service Level Indicators:

- Availability (success ratio of valid requests).
- Latency P95 / P99.
- Throughput (requests/sec).
- Correctness (e.g. billing-event-emission rate).
- Freshness (data lag, replication lag).
- Durability (data loss probability).

Each SLI declares: definition, measurement source, sampling window, exclusions (planned maintenance).

### Step 2: Set per-tier SLOs

| Tier | Availability | Latency P95 | Latency P99 | Support response | Notes |
|------|--------------|-------------|-------------|------------------|-------|
| Bronze | 99.5% | 800 ms | 2000 ms | next business day | shared pool |
| Silver | 99.9% | 400 ms | 1000 ms | 4 h | shared pool with reserved capacity |
| Gold | 99.95% | 200 ms | 500 ms | 1 h | pod-isolated |
| Enterprise | 99.99% | 150 ms | 300 ms | 15 min, named CSM | silo or dedicated pod |

### Step 3: Compute error budgets

- Bronze 99.5% over 30 d = 3 h 36 min downtime allowed.
- Silver 99.9% over 30 d = 43 min 12 s.
- Gold 99.95% over 30 d = 21 min 36 s.
- Enterprise 99.99% over 30 d = 4 min 19 s.

State error budget per SLO and the formula `error_budget_minutes = (1 - SLO) × period_minutes`.

### Step 4: Burn-rate alerts

Define multi-window multi-burn-rate alerts:

| Alert | Severity | Burn rate | Window | Threshold |
|-------|----------|-----------|--------|-----------|
| Fast burn | SEV2 | 14.4× | 1 h | 2% of monthly budget |
| Medium burn | SEV3 | 6× | 6 h | 5% of monthly budget |
| Slow burn | SEV4 | 1× | 3 d | 10% of monthly budget |

### Step 5: Freeze rules

State the rules that take effect when error budget is exhausted: no risky deploys, increased review, postmortem actions blocked from being skipped, executive notification at < 0% budget remaining.

### Step 6: Customer-SLA mapping

For each tier, map the internal SLO to the contractual SLA commitment (which is typically more conservative — internal 99.95% backs external 99.9%). Define service-credit schedule (% credit per breach band), the exclusions, the measurement method, the credit-request process.

### Step 7: Write the doc

`SLO_And_Error_Budget_Doc.md` with sections: 1) SLI Inventory, 2) Per-Tier SLO Targets, 3) Error-Budget Math, 4) Burn-Rate Alerts, 5) Freeze Rules, 6) Customer-SLA Mapping & Service Credits, 7) Review Cadence (monthly SLO review, quarterly target review).

## Standards

- Google SRE: SLO/Error Budget, Multi-Burn-Rate Alerting.
- ISO/IEC 25010 — Quality model.

## Resources

- `logic.prompt`, `README.md`, `references/saas-slo-and-error-budget-template.md`.
