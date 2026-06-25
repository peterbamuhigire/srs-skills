# Retail Operating Model Reference

Use this reference when generating Software Requirements Specifications (SRS), Product Requirements Documents (PRD), business rules, test cases, or architecture notes for retail software. It converts the Umbrex retail playbook corpus into a reusable requirements vocabulary for retail projects.

## Capability Spine

Retail software requirements must identify which of these capability clusters are in scope:

| Cluster | Capability scope | SRS implication |
|---|---|---|
| Commercial architecture | Assortment, merchandising calendar, pricing, promotions, markdowns | Model item roles, category roles, price zones, event calendars, discount rules, approval gates, and margin guardrails. |
| Customer and digital growth | Loyalty, CRM, conversion, search/navigation | Model identity, consent, segmentation, product discovery, product detail content, checkout trust, campaigns, tests, and lifecycle events. |
| Omnichannel operations | Merchandising, fulfilment, returns | Model channel promises, inventory availability, reservations, routing, pickup, ship-from-store, reverse logistics, disposition, and exception flows. |
| Store execution | Labour scheduling, store operations, new store opening | Model store tasks, SOPs, audits, readiness gates, training evidence, staffing, shift handover, and launch checklists. |
| Profit protection and supplier economics | Shrink, vendor terms, trade spend, private label | Model incident capture, discount/refund controls, supplier funding claims, rebates, landed cost, quality holds, and recovery evidence. |
| Performance management | Planogram, space productivity, KPI dashboard, weekly business review | Model metric definitions, drilldowns, owner/date action logs, variance reasons, and evidence from source transactions. |

Do not reduce retail scope to "catalogue + checkout". A serious retail system is an operating system for product, price, inventory, channel promise, store execution, controls, and performance review.

## Core Retail Entities

Every retail SRS should decide whether these entities are in scope:

- SKU, product, variant, barcode, product attribute, product image, content asset.
- Category, subcategory, collection, item role, category role, assortment decision.
- Store, warehouse, fulfilment node, channel, marketplace, region, price zone.
- Inventory balance, reservation, allocation, purchase order, receipt, transfer, adjustment, stock count.
- Price, price book, promotion, coupon, markdown, offer stack, approval rule.
- Customer, loyalty member, segment, consent record, lifecycle journey, campaign, voucher, reward.
- Cart, order, order line, payment, refund, return, exchange, disposition, credit note.
- Store task, labour forecast, shift, checklist, audit finding, training record.
- Vendor, vendor agreement, allowance, rebate, co-op funding, claim, recovery.
- Private-label product brief, specification, supplier sample, quality hold, launch gate.
- Planogram, fixture, shelf, space allocation, facings, display, space productivity metric.
- KPI, metric definition, dashboard view, weekly business review action, owner, due date.

## Required Workflow Families

For each workflow family in scope, generate requirements for happy path, exception path, approval path, audit evidence, telemetry, and finance/control handoff.

| Workflow family | Required SRS coverage |
|---|---|
| Assortment and SKU rationalisation | Cut/keep/add/test decisions, substitute item logic, category roles, lifecycle status, approval evidence. |
| Merchandising calendar and line review | Seasonal events, launch gates, cross-functional sign-offs, inventory readiness, marketing readiness, post-event review. |
| Pricing and promotions | Price ladders, KVI flags, price zones, offer eligibility, stack prevention, margin floor, approval workflow, test cases. |
| Markdown optimisation | Markdown triggers, discount ladder, aged stock rules, exit strategy, inventory write-down handoff, exception approval. |
| Loyalty and CRM | Enrollment, consent, tiers, points/rewards, segments, lifecycle messaging, suppression, ROI measurement, liability handoff. |
| Search and navigation | Attribute governance, taxonomy, synonyms, zero-result handling, filter/facet logic, relevance tuning, test queries. |
| Fulfilment | Available-to-promise, allocation, routing, pickup, ship-from-store, substitutions, SLA breach, fulfilment cost capture. |
| Returns | Eligibility, initiation, inspection, refund, exchange, restock, quarantine, dispose, fraud review, reverse logistics. |
| Store labour and operations | Labour drivers, scheduling, tasking, SOP checklists, audits, escalation, training evidence, adoption metrics. |
| Shrink and loss prevention | Incident capture, high-risk item controls, stock count variance, investigation workflow, CCTV/evidence references. |
| Planogram and space | Space-to-sales logic, fixture rules, planogram publishing, compliance audit, test-and-learn rollout. |
| Vendor terms and trade spend | Agreement terms, allowance/rebate accruals, claim evidence, recovery tracking, dispute handling. |
| Private label | Product brief, sourcing, cost build-up, packaging approvals, quality tests, launch readiness, performance review. |
| New store opening | Site readiness, inventory load, POS setup, staffing, training, soft opening, issue log, opening review. |
| KPI dashboard and WBR | Metric dictionary, drilldowns, variance reasons, action register, source-to-dashboard lineage. |

## Acceptance Test Pattern

Every retail requirement should expose a deterministic oracle. Prefer this shape:

```text
Given <source state and retail context>
When <actor/event/action occurs>
Then <system state, control evidence, ledger/finance handoff, and dashboard metric> shall match <specific expected value or state>.
```

Examples:

- Given a markdown is approved for Category A in Price Zone 2, when the effective date starts, then eligible SKUs shall receive only the approved markdown price in POS, web, and marketplace channels, and the event log shall record approver, reason code, source ID, and effective period.
- Given an online return is inspected as resellable, when the return is accepted, then the system shall create the refund event, return the unit to sellable stock, link the event to the original order, and expose the transaction to the finance reconciliation queue.
- Given a store count variance exceeds the configured threshold, when the stock count is closed, then the system shall block automatic posting until a controller-approved variance reason and evidence attachment exist.

## Diagnostic Questions

Before drafting SRS content, ask or infer from project context:

1. Which retail capability cluster is in scope?
2. Which channels are active: store, web, app, marketplace, social commerce, wholesale, kiosk?
3. What is the system of record for product, inventory, price, order, customer, and finance data?
4. Which finance/accounting events must be produced: sales, refunds, discounts, markdowns, stock movements, shrink, vendor funding, loyalty, gift cards?
5. Which approvals are required for manual discounts, refunds, stock adjustments, price changes, and supplier claims?
6. Which metrics must be visible in weekly review, and which source events prove them?
7. Which data is personal, payment-sensitive, commercially sensitive, or audit-sensitive?
8. Which offline or low-connectivity store workflows must continue operating?

## Evidence Basis

Derived from the digital-research-engine project `umbrex-retail-playbooks-engine-enhancement`, extracted on 2026-06-25 from 20 public Umbrex retail playbook landing pages and 163 linked chapter/tool pages. Use this reference as internal taxonomy evidence, not as legal, accounting, or market-statistics authority.
