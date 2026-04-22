# Module Overview

## Universality Principle

All modules are universal. Localisation behaviour - country-specific tax rules, statutory integrations, currency handling, regulatory workflows, and chart of accounts defaults - is determined by the tenant's configuration profile, not by module variants. A Ugandan manufacturer and a Kenyan NGO activate modules from the same codebase; their statutory and currency behaviour differs because their localisation profiles differ.

## Core Modules (Always Active - Cannot Be Disabled)

| Code | Module | Description |
|---|---|---|
| `ACCOUNTING` | Accounting & General Ledger | Double-entry General Ledger (GL), IFRS-compliant financial statements, AP, AR, bank reconciliation, multi-currency, VAT/WHT, budgets, record-to-report discipline, close orchestration, consolidation-ready group structures, finance controls/workflow/approvals, and reporting foundations for management, statutory, and investor-grade analytics |
| `INVENTORY` | Inventory Management | Item catalogue, UOM conversion, FIFO/weighted-average costing, Goods Received Note (GRN), stock adjustments, reorder levels, physical count, stock transfers |
| `SALES` | Sales | Customer master, price lists, quotations, sales orders, delivery notes, invoices, credit notes, receipts, returns |
| `PROCUREMENT` | Procurement | Supplier master, purchase requisitions, RFQ, LPO, three-way matching, supplier payments, WHT |
| `USER_MGMT` | User Management & RBAC | User lifecycle, unlimited roles, granular permissions, branch restrictions, approval limits, 2FA, biometric login, USSD access |
| `AUDIT` | Audit Log | Immutable INSERT-only audit trail covering all CRUD and approval actions, external auditor read-only role, 7-year retention |

## Add-On Modules (Per-Tenant Activation)

| Code | Module | Description |
|---|---|---|
| `ADV_INVENTORY` | Advanced Inventory | Multi-location warehousing, batch/serial tracking, First-Expired-First-Out (FEFO), expiry management, inter-branch stock-in-transit, landed cost, stock reservation, recall management |
| `MANUFACTURING` | Manufacturing | Bill of Materials (BOM) with versions, routings, work centres, production orders, raw material issue, Work in Progress (WIP), operation tracking, genealogy, in-process quality, rework, downtime capture, Overall Equipment Effectiveness (OEE), yield/variance, by-products, scrap, overhead absorption, production costing |
| `HR_PAYROLL` | HR & Payroll | Employee master, contracts, org structure, grade/salary scales, leave, attendance (biometric/mobile), payroll processing, bank payment files, mobile money salary, statutory compliance |
| `POS` | Point of Sale | Touch-optimised terminal, barcode scanning, multi-payment modes, mobile money push, thermal receipt, shift management, restaurant/bar table mode, offline mode, real-time GL posting |
| `SALES_CRM` | Sales & CRM | Leads pipeline, opportunities, Kanban view, activity logging, contact management, quotation tracking, sales forecasting, territory management, WhatsApp logging |
| `SALES_AGENTS` | Sales Agents & Commissions | Agent register, target setting, commission rules (flat/tiered/product), commission runs, approval, mobile money bulk payment, agent self-service portal |
| `COOPERATIVE` | Cooperative Procurement | Commodity configuration, farmer/outgrower registration, group/society hierarchy, seasonal intake, weighbridge integration, input loan deductions, mobile money farmer payment, farmer statements |
| `PROJECTS` | Project Management | Project register, budget, milestones, tasks/Work Breakdown Structure (WBS), timesheets, resource allocation, project costs, project billing (T&M and milestone), subcontractors, project P&L, Gantt, portfolio |
| `STRATEGY_BSC` | Strategy & Balanced Scorecard | Strategic framework, Balanced Scorecard (BSC) perspectives, objectives, KPIs, actuals, traffic-light scoring, scorecard dashboard, initiative tracking, executive report, Objectives and Key Results (OKR) mode, NGO logframe |
| `ASSETS` | Asset Management | Asset register, depreciation (straight-line/reducing-balance), revaluation, disposal with gain/loss, transfer, maintenance scheduling, insurance, QR/barcode tagging, physical verification, and vehicle capital-asset control. Transport dispatch and live fleet operations are handled in `TRANSPORTATION` |
| `AI_INTELLIGENCE` | AI Intelligence | Cash flow forecasting, GL anomaly detection, demand forecasting, debtor risk scoring, and narrative financial reports. Paid add-on available on Professional plans and above; off by default |
| `PLM` | Product Lifecycle Management | Engineering item master, revision control, EBOM/MBOM governance, engineering change workflow, effectivity control, NPI stage gates, document control, compliance evidence, and digital-thread release to downstream modules |
| `TRANSPORTATION` | Transportation & Fleet Operations | Shipment planning, route and load planning, dispatch, carrier or internal-fleet assignment, ETA and milestone visibility, proof of delivery, exception management, freight audit, transport analytics, driver assignment, and telematics-ready fleet operations |

## Platform Services (Always Active - Not User-Facing Modules)

Platform services are infrastructure components that underpin all tenant operations. They are not activatable or deactivatable per tenant.

| Code | Service | Description |
|---|---|---|
| `LOCALISATION` | Localisation Engine | Configuration-driven localisation: currency, language, tax, statutory, Chart of Accounts (COA) starter, address format, invoice legal text, mobile money gateway - per tenant, no code changes per market |
| `MOBILE_API` | Mobile API | JWT auth, tenant isolation, rate limiting, versioned REST (v1/v2), offline sync, push notifications, SMS fallback, data-lite mode |
| `INTEGRATIONS` | Integration Layer | Africa's Talking, MTN MoMo, Airtel Money, M-Pesa Daraja, URA EFRIS, URA PAYE, NSSF, KRA iTax, NITA-U |
| `BILLING` | Billing & Subscriptions | Subscription plans, a-la-carte add-ons, annual billing, payment via card/bank/MTN MoMo/M-Pesa, tenant lifecycle management (Trial -> Active -> Overdue -> Suspended -> Archived) |

## Module Count Summary

| Category | Count |
|---|---|
| Core modules (always active) | 6 |
| Add-on modules (per-tenant activation) | 13 |
| Platform services (infrastructure, always active) | 4 |
| **Total** | **23** |

## Strategic Depth Note

Longhorn ERP is intended to compete credibly for both small and large African organisations that make, move, and service physical goods. For that reason, three capability boundaries are explicit in the product architecture:

- `PLM` owns engineering truth: released revisions, engineering changes, technical documents, effectivity, and product lifecycle governance.
- `MANUFACTURING` owns production planning, shop-floor execution, costing, quality execution, and operational performance.
- `TRANSPORTATION` owns shipment planning, dispatch, route execution, transport visibility, and live fleet operations.

These boundaries are deliberate. They prevent engineering control, shop-floor execution, and transport operations from collapsing into one oversized module with weak governance.

## Finance Excellence Note

Longhorn ERP treats `ACCOUNTING` as the financial system of record, not a basic bookkeeping add-on. The module is positioned to support both growing SMEs and larger multi-entity organisations that need disciplined finance operations without buying a separate finance stack.

World-class finance capability in Longhorn ERP means:

- record-to-report discipline with controlled journal entry, subledger reconciliation, accounting periods, and audit-ready close evidence
- close orchestration with checklists, task ownership, dependency tracking, review steps, and exception visibility
- consolidation foundations with legal-entity structures, intercompany readiness, elimination support, and group reporting preparation
- finance controls, workflow, and approvals with maker-checker patterns, approval thresholds, segregation of duties, and policy-enforced posting controls
- reporting foundations with trusted dimensional reporting, management packs, statutory statements, board reporting, and analytics-ready finance data

This positioning is deliberate. `ACCOUNTING` remains the core module, while advanced finance excellence is delivered as depth within the same bounded capability so Longhorn ERP can scale from small African businesses to regional enterprise groups without fragmenting the finance operating model.
