# Customer, Revenue, and Service Architecture

## Purpose

This document defines the high-level architecture for LonghornERP CRM so the platform can support both revenue CRM and service CRM without collapsing customer workflow into ERP execution logic.

The CRM architecture follows a strict boundary:

- CRM owns customer intent, relationship workflow, pipeline governance, service interactions, and account intelligence.
- ERP owns executable transactions, inventory and fulfilment, invoicing, receivables, taxation, and financial truth.

This split keeps customer-facing teams productive while preserving operational and accounting integrity.

---

## CRM Capability Scope

LonghornERP CRM covers six capability groups:

1. Revenue CRM: lead, opportunity, pipeline, forecast, and account planning.
2. Service CRM: case intake, SLA management, escalation, and case resolution workflow.
3. Customer master workflow: account hierarchy, contact relationships, segmentation, and account ownership.
4. Quote-to-cash coordination: quote intent, commercial approvals, and controlled handoff into ERP execution.
5. Customer intelligence: activity history, health signals, renewal watchlists, and customer financial context snapshots.
6. Channel support: partner registry, partner deal registration, and shared customer-account relationships.

CRM does not replace the ERP modules that execute orders, issue invoices, settle receivables, or post accounting entries.

---

## Boundary Model: CRM Workflow vs ERP Execution

### CRM Owns

- lead capture and qualification
- account and contact relationship management
- opportunity stages, forecast, and commercial exception approvals
- sales activities, account plans, and customer segmentation
- service cases, comments, timelines, SLA clocks, and escalations
- renewal watchlists, health signals, and customer-success workflow
- quote preparation context and quote-to-cash handoff records
- partner and channel relationship workflow

### ERP Owns

- item master, stock availability, and fulfilment commitments
- executable quotations where legal, tax, and pricing controls apply
- sales orders, delivery, shipment, and invoicing
- receivables, collections, ageing, and credit-control truth
- tax determination, revenue postings, and financial statements
- service-related inventory consumption, field-work costing, and warranty accounting

### Shared but Controlled

- customer master references:
  - CRM can maintain selling and service relationship views.
  - ERP customer execution records remain the source of truth once a customer is transacting.
- quote and order coordination:
  - CRM originates selling intent and governed commercial context.
  - ERP validates execution details and creates executable quote or order records.
- customer financial context:
  - CRM receives read-only financial context from ERP for account planning, service prioritization, and renewal decisions.
  - CRM cannot alter receivable balances, credit limits, or invoice truth.

---

## Core CRM Object Model

### Accounts

`Account` is the commercial and service relationship anchor. It represents a customer, prospect, distributor, government entity, donor, buyer group, or other commercial party.

Key account concerns:

- segmentation and tiering
- territory and ownership
- parent-child hierarchy
- partner attachment
- financial-context snapshots from ERP
- service posture, health, and renewal state

### Contacts

`Contact` represents a person linked to one or more accounts, with roles such as decision-maker, approver, service requester, finance contact, or executive sponsor.

### Leads

`Lead` captures unqualified or partially qualified demand before the relationship is normalized into account, contact, and opportunity objects.

### Opportunities

`Opportunity` represents governed revenue intent. It owns:

- pipeline stage
- value and probability
- expected close timing
- competition and win strategy
- approval gates for discounting or non-standard terms
- quote-to-cash handoff status

### Cases

`Case` represents a service issue, complaint, request, or incident. It owns:

- case type and severity
- SLA policy
- response and resolution clocks
- status, comments, timeline events, and escalations
- linkage to account, contact, assets, orders, or invoices where relevant

### Activities

`Activity` captures sales and service engagement events such as calls, visits, emails, tasks, demos, and follow-ups.

### Quote and Order Coordination

CRM stores quote intent, commercial context, and approval state. ERP owns the executable quote or order and returns the resulting execution reference back to CRM.

### Customer Financial Context

CRM exposes a read-only context layer sourced from ERP:

- credit status
- receivables ageing summary
- overdue exposure
- open orders and disputed invoices
- payment behavior indicators

This is used for selling and service prioritization, not for transaction posting.

---

## Integration Boundaries

### CRM to Sales and Order Execution

The integration contract between CRM and ERP order execution must support:

- quote or order handoff payloads
- item and pricing validation feedback
- execution acceptance or rejection
- created ERP quote, order, and invoice references
- account credit warnings returned to CRM

### CRM to Accounting and Finance

CRM consumes but does not own:

- customer balance and ageing
- credit blocks and release status
- payment performance indicators
- disputed invoice indicators

Any financial figure shown in CRM must be traceable to an ERP-owned source.

### CRM to Service and Asset Context

Service CRM can reference:

- sold products or service contracts
- registered assets or installed base
- shipment and order history
- warranty or entitlement signals

Those records remain mastered by the relevant ERP modules.

### CRM to Channel and Partner Ecosystem

CRM must support:

- partner registry
- partner-owned or partner-assisted opportunities
- partner-linked accounts
- deal registration and protection windows

Commercial settlement with partners remains an ERP and finance workflow.

---

## High-Level Service Domains

### Revenue CRM Domain

Owns account, contact, lead, opportunity, activity, forecast, and account-planning workflow.

### Service CRM Domain

Owns case intake, SLA policy selection, assignment, escalation, resolution, and customer-facing service timeline history.

### Quote-to-Cash Coordination Domain

Owns governed transfer of opportunity and quote context from CRM into ERP execution flows.

### Customer Intelligence Domain

Owns account segmentation, health signals, renewal watchlists, relationship history, and next-action cues.

### Partner and Channel Domain

Owns partner registry, partner-account links, partner opportunity participation, and channel governance workflow.

---

## Architectural Guardrails

1. CRM must never be the source of financial truth.
2. Opportunity forecasts must exclude or flag deals that are missing required commercial approvals.
3. Case SLA clocks must run from governed policy definitions, not from ad hoc manual interpretation.
4. Customer financial context shown in CRM must be time-stamped and attributable to ERP source data.
5. Quote-to-cash handoff must be idempotent and auditable.
6. Customer hierarchy and duplication controls must prevent fragmented views of the same enterprise account.
7. Partner relationships must not weaken direct customer ownership, financial controls, or reporting integrity.

---

## Outcome

With this architecture, LonghornERP CRM becomes a first-class customer workflow layer for both growth and service operations while preserving the integrity of ERP execution and finance.
