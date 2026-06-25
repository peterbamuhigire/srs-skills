---
name: "retail-operating-model-srs"
description: "Generate retail SRS sections for omnichannel retail, merchandising, pricing, promotions, markdowns, loyalty, CRM, e-commerce, fulfilment, returns, store operations, shrink, vendor funding, private label, planograms, and KPI/WBR dashboards as testable software requirements with finance/control gates."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  use_when: "Use when a software project touches retail, stores, POS, e-commerce, product catalogue, inventory, orders, fulfilment, returns, loyalty, merchandising, pricing, promotions, markdowns, vendor funding, private label, shrink, planograms, or retail dashboards."
  do_not_use_when: "Do not use for generic websites with no retail transaction, inventory, fulfilment, or customer-commerce operations."
  required_inputs: "projects/<ProjectName>/_context/, domains/retail/INDEX.md, domains/retail/references/retail-operating-model.md, domains/retail/references/finance-control-gates.md, and the relevant domains/retail/features/*.md files."
  workflow: "Classify the retail capability scope, build the entity/workflow/event catalogue, apply finance/control gates, write stimulus-response FRs, measurable NFRs, interfaces, data model, acceptance tests, and traceability."
  quality_standards: "Every requirement must have source context, deterministic acceptance criteria, event/audit implications where relevant, and finance-engine routing where inventory, payments, refunds, discounts, vendor funding, shrink, or dashboards are in scope."
  anti_patterns: "Do not reduce retail software to catalogue plus checkout. Do not omit inventory, returns, controls, source events, or dashboard lineage. Do not invent market statistics or accounting treatment."
  outputs: "Retail_Domain_SRS.md, Retail_Event_Catalogue.md, Retail_Finance_Control_Gates.md, Retail_Acceptance_Tests.md."
  references: "domains/retail/references/retail-operating-model.md, domains/retail/references/finance-control-gates.md"
---

# Retail Operating Model SRS Skill

<!-- dual-compat-start -->
## Use When

Use when a software project touches retail, stores, POS, e-commerce, product catalogue, inventory, orders, fulfilment, returns, loyalty, merchandising, pricing, promotions, markdowns, vendor funding, private label, shrink, planograms, or retail dashboards.

## Do Not Use When

Do not use for generic websites with no retail transaction, inventory, fulfilment, or customer-commerce operations.

## Required Inputs

Project context, `domains/retail/INDEX.md`, `domains/retail/references/retail-operating-model.md`, `domains/retail/references/finance-control-gates.md`, and the relevant `domains/retail/features/*.md` files.

## Workflow

Classify retail capability scope, build the entity/workflow/event catalogue, apply finance/control gates, write stimulus-response functional requirements, define measurable NFRs and interfaces, then produce acceptance tests and traceability.

## Quality Standards

Every requirement has source context, deterministic acceptance criteria, event/audit implications where relevant, and finance-engine routing where inventory, payments, refunds, discounts, vendor funding, shrink, or dashboards are in scope.

## Anti-Patterns

Do not reduce retail software to catalogue plus checkout. Do not omit inventory, returns, controls, source events, or dashboard lineage. Do not invent market statistics or accounting treatment.

## Outputs

Retail domain SRS sections, retail event catalogue, finance/control gates, acceptance tests, and traceability matrix.

## References

Use `domains/retail/references/retail-operating-model.md`, `domains/retail/references/finance-control-gates.md`, and the relevant retail feature references.
<!-- dual-compat-end -->

## Overview

This skill turns retail project context into complete, testable retail software requirements. It uses the retail domain pack as the controlled vocabulary and the finance doctrine engine as the required cross-check whenever money, inventory, refunds, discounts, vendor funding, shrink, POS, or reporting is affected.

## Core Workflow

### Step 1: Classify the Retail Scope

Read `projects/<ProjectName>/_context/` and classify which capability clusters are in scope:

| Cluster | Trigger terms |
|---|---|
| Commercial architecture | assortment, category, merchandising, line review, pricing, promotion, coupon, discount, markdown |
| Customer and digital growth | loyalty, CRM, lifecycle, conversion, product page, search, navigation, faceted filters |
| Omnichannel operations | inventory, fulfilment, available-to-promise, pickup, ship-from-store, returns, reverse logistics |
| Store execution | POS, cashier, store task, SOP, labour, schedule, audit, new store opening |
| Profit protection and supplier economics | shrink, loss prevention, vendor terms, rebate, allowance, trade spend, private label |
| Performance management | dashboard, KPI, weekly business review, planogram, space productivity, action register |

If the brief does not identify the cluster, flag `[CONTEXT-GAP: retail capability scope]`.

### Step 2: Build the Retail Entity Catalogue

For each in-scope cluster, list entities, state transitions, source events, owners, and systems of record. Use `domains/retail/references/retail-operating-model.md` as the minimum entity vocabulary.

Every source event row must include:

- event name;
- source system;
- actor or integration;
- timestamp;
- affected entity;
- prior state;
- new state;
- evidence pointer;
- idempotency key;
- downstream finance/reporting handoff, if any.

### Step 3: Apply Finance and Control Gates

Load `domains/retail/references/finance-control-gates.md`. If any finance trigger is present, route to `C:\wamp64\www\chwezi-accounting-doctrine` and record the route in the generated artefact.

Do not write final requirements for these items without a finance/control section:

- inventory valuation, movement, count, write-down, shrink, damage, or disposal;
- sale, payment, refund, exchange, credit note, split tender, cash drawer, card settlement, or mobile money;
- price override, promotion, manual discount, coupon, markdown, vendor funding, rebate, co-op funding, or scanback;
- loyalty points, gift cards, wallet balance, store credit, or customer advance;
- financial KPI, gross margin, markdown rate, return rate, shrink rate, vendor funding recovery, or POS reconciliation.

### Step 4: Write Stimulus-Response Functional Requirements

Use the SRS engine's normal requirement pattern:

```text
When <stimulus> occurs, the system shall <response> so that <controlled outcome> can be verified by <test oracle/evidence>.
```

Each requirement must include:

- actor or source event;
- precondition;
- system response;
- exception path;
- audit evidence;
- measurable acceptance criterion;
- traceability to retail capability and business goal.

### Step 5: Write Retail NFRs

Apply the existing retail defaults plus the added requirements:

- RET-NFR-001 Cardholder Data Protection
- RET-NFR-002 Checkout Performance
- RET-NFR-003 Consumer Data Rights
- RET-NFR-004 Inventory Accuracy
- RET-NFR-005 Peak Sales Availability
- RET-NFR-006 Product Data Quality
- RET-NFR-007 Retail Event Auditability
- RET-NFR-008 Dashboard Freshness and Lineage

Adapt thresholds only when project context provides stronger local targets. Do not weaken security, auditability, or evidence requirements without a documented waiver.

### Step 6: Specify Interfaces

Retail SRS interface coverage should include the relevant systems:

- POS and payment terminal;
- payment gateway, card settlement, mobile money, wallet, cash drawer;
- product information management;
- inventory service, warehouse management system, third-party logistics;
- order management system;
- CRM, email/SMS/push, loyalty platform;
- ERP/general ledger, tax/fiscal device, source-document archive;
- supplier/vendor portal or claims register;
- analytics warehouse and dashboard.

For each interface, define payload, direction, cadence, failure mode, retry/idempotency, reconciliation, and owner.

### Step 7: Produce Acceptance Tests

Create retail acceptance tests for:

- price/promotion/markdown effective-dated rollout;
- offer-stack prevention;
- inventory reservation and release;
- order fulfilment routing;
- return inspection and disposition;
- refund approval and reconciliation;
- manual discount approval;
- stock count variance control;
- vendor funding claim evidence;
- dashboard source lineage and stale-data warning.

## Output Structure

Use this structure for `Retail_Domain_SRS.md`:

1. Retail scope classification
2. Entity and state model
3. Source event catalogue
4. Functional requirements by capability cluster
5. Non-functional requirements
6. Interface requirements
7. Finance and control gates
8. Reporting and dashboard requirements
9. Acceptance tests
10. Traceability matrix

## Quality Gate

Before release, confirm:

- No requirement uses vague retail claims without source context.
- Every finance-triggering workflow has a finance/control gate.
- Every inventory-changing event has an audit trail and reconciliation route.
- Every price/promotion/markdown workflow has effective date, approval, rollback, and exception handling.
- Every dashboard metric has owner, formula, source, refresh cadence, and reconciliation status.
- Every requirement is testable with a deterministic pass/fail oracle.

## Evidence Basis

This skill operationalises the internal research project `umbrex-retail-playbooks-engine-enhancement` from the digital-research-engine. The Umbrex corpus is used as a taxonomy and project-scope evidence base; legal, statutory, accounting, tax, and market-size claims still require the relevant primary authority and reviewer route.
