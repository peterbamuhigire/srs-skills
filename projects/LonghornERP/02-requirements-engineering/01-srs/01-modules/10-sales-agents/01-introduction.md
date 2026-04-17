# Introduction to the Sales Agents and Commissions Module

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Sales Agents and Commissions module of Longhorn ERP. It is authoritative for design, development, and acceptance testing of this module. The intended readers are the lead developer, quality assurance engineers, and any future development team members onboarding to this module.

## 1.2 Scope

The Sales Agents and Commissions module (hereafter "the module") is a first-class feature set within Longhorn ERP, a multi-tenant Software-as-a-Service (SaaS) Enterprise Resource Planning (ERP) platform developed by Chwezi Core Systems. The module manages the full lifecycle of a field sales agent: registration, territory and product assignment, target setting, sales attribution, commission calculation, approval, mobile money disbursement, agent self-service, stock management, remittance verification, and daily activity reporting.

The module is scoped to the following tenant-configurable capabilities:

- Agent registration and lifecycle management
- Sales target definition and progress tracking
- Commission rule engine (flat, tiered, and product-specific)
- Monthly commission run with multi-stage approval workflow
- Mobile money bulk disbursement (MTN Uganda / Airtel Uganda)
- Agent self-service portal accessible via web browser and mobile-responsive layout
- Agent stock issuance, return, and balance tracking
- Cash remittance collection and verification
- Daily activity summaries per agent

The module does not cover general sales order processing, invoicing, or accounts receivable reconciliation; those functions are handled by the Sales and Invoicing module. This module consumes invoice data produced by that module through internal service integration.

## 1.3 Integrations

| Integration Point | Module / System | Direction | Description |
|---|---|---|---|
| Sales Invoices | Sales and Invoicing module | Inbound | Invoice records linked to agents for attribution and commission calculation |
| Chart of Accounts | Accounting module | Inbound | Commission expense accounts for posting payable entries |
| Inventory Ledger | Inventory and Stock module | Bidirectional | Issue and return of stock held by agents |
| Mobile Money Gateway | MTN Mobile Money API / Airtel Money API | Outbound | Bulk payment initiation and callback confirmation |
| User and Role Management | System Administration module | Inbound | Agent portal authentication and role-based access control |
| Notifications | Notification / Messaging subsystem | Outbound | Approval alerts, payout confirmations, and target milestone alerts |

## 1.4 Business Goals

| ID | Business Goal | Priority |
|---|---|---|
| BG-01 | Eliminate manual spreadsheet-based commission calculations and reduce calculation errors to 0% | High |
| BG-02 | Disburse verified commissions to agents via mobile money within 2 business days of approval | High |
| BG-03 | Provide each agent with real-time visibility into their sales performance and earnings | High |
| BG-04 | Enable management to configure flexible commission structures without developer intervention | High |
| BG-05 | Ensure full audit trail for every commission run, adjustment, and payment | High |
| BG-06 | Track agent-held stock and cash remittances to reduce field reconciliation errors | Medium |
| BG-07 | Provide daily activity summaries to enable proactive field force management | Medium |

## 1.5 Definitions

| Term | Definition (IEEE Std 610.12-1990 aligned) |
|---|---|
| Agent | A registered sales representative associated with one tenant, assigned a territory and a set of active products |
| Commission Run | A batch process that calculates commission amounts for all eligible agents for a specified period, typically one calendar month |
| Commission Rule | A tenant-configured rule specifying the method (flat rate, tiered, or product-specific) and rate(s) used to compute a commission amount |
| Remittance | Cash or mobile money collected by an agent on behalf of the tenant that must be verified against attributed sales invoices |
| Territory | A geographic or organisational subdivision assigned to an agent, used to scope sales attribution and target setting |
| Tiered Rate | A commission structure in which the applicable rate changes based on cumulative sales thresholds within a period |
| MTN MoMo | MTN Mobile Money, a mobile-network-based payment service operating in Uganda and other African markets |
| Airtel Money | Airtel's mobile payment service operating in Uganda and other African markets |
| Attribution | The act of associating a posted sales invoice with a specific agent, establishing ownership for commission calculation purposes |
| SaaS | Software-as-a-Service: a software delivery model in which the application is hosted centrally and accessed over the internet by multiple tenants |
| ERP | Enterprise Resource Planning: an integrated system managing core business processes |
| SRS | Software Requirements Specification: this document, conforming to IEEE Std 830-1998 |

## 1.6 Document Overview

| Section | Title | Content Summary |
|---|---|---|
| 1 | Introduction | Purpose, scope, integrations, business goals, definitions |
| 2 | Agent Register | Agent record management, territory, and product assignment requirements |
| 3 | Targets and Attribution | Sales target setting and invoice-to-agent attribution rules |
| 4 | Commission Rules | Rule engine: flat rate, tiered, and product-specific commission configuration |
| 5 | Commission Run and Payout | Batch calculation, approval workflow, and mobile money disbursement |
| 6 | Agent Self-Service Portal | Portal access, sales and commission views, target progress, statements |
| 7 | Stock Management and Remittance | Agent stock balances, issuance, returns, remittance verification, daily summaries |
| 8 | Non-Functional Requirements | Performance, reliability, security, and compliance constraints |
| 9 | Traceability Matrix | Requirements-to-business-goals mapping and V&V notes |
