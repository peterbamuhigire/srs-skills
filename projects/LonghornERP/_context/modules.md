# Module Inventory - Longhorn ERP

All modules are universal. Localisation behaviour is governed by the Localisation Engine configuration profile for the tenant's jurisdiction. Phase 1 ships all modules.

## Core Modules (Always Active - Cannot Be Disabled)

| # | Module | Code | Description |
|---|---|---|---|
| 1 | Accounting & General Ledger | ACCOUNTING | Double-entry GL, AP, AR, bank reconciliation, tax, budgeting, financial statements, recurring and reversing journals, close orchestration, consolidation-ready finance model, approvals and audit trail, multi-currency, and management reporting foundations |
| 2 | Inventory Management | INVENTORY | Item catalogue, UOM conversion, FIFO/weighted-average, GRN, stock adjustments, reorder levels, physical count, stock transfers |
| 3 | Sales | SALES | Customer master, price lists, quotations, sales orders, delivery notes, invoices, credit notes, receipts, returns |
| 4 | Procurement | PROCUREMENT | Supplier master, purchase requisitions, RFQ, LPO, three-way matching, supplier payments, WHT |
| 5 | User Management & RBAC | USER_MGMT | User lifecycle, unlimited roles, granular permissions, branch restrictions, approval limits, 2FA, biometric login, USSD access |
| 6 | Audit Log | AUDIT | Immutable INSERT-only audit trail, all CRUD and approval actions, external auditor read-only role, 7-year retention |

## Add-On Modules (Per-Tenant Activation)

| # | Module | Code | Description |
|---|---|---|---|
| 7 | Advanced Inventory | ADV_INVENTORY | Multi-location warehousing, batch/serial tracking, FEFO, expiry management, inter-branch stock-in-transit, landed cost, stock reservation, recall management |
| 8 | Manufacturing | MANUFACTURING | BOM with versions, routings, work centres, production orders, raw material issue, WIP, operation tracking, genealogy, in-process QC, rework, downtime capture, OEE, yield/variance, by-products, scrap, overhead absorption, production costing |
| 9 | HR & Payroll | HR_PAYROLL | Employee master, contracts, org structure, job and position governance, grade/salary scales, leave, attendance (biometric/mobile), payroll processing, payroll calendars and validation controls, bank payment files, mobile money salary, manager and employee self-service, operational people analytics, and statutory compliance |
| 10 | Point of Sale | POS | Touch-optimised terminal, barcode scanning, multi-payment modes, mobile money push, thermal receipt, shift management, restaurant/bar table mode, offline mode, real-time GL posting |
| 11 | Sales & CRM | SALES_CRM | Leads pipeline, opportunities, Kanban view, activity logging, contact management, quotation tracking, sales forecasting, territory management, WhatsApp logging |
| 12 | Sales Agents & Commissions | SALES_AGENTS | Agent register, target setting, commission rules (flat/tiered/product), commission runs, approval, mobile money bulk payment, agent self-service portal |
| 13 | Cooperative Procurement | COOPERATIVE | Commodity configuration, farmer/outgrower registration, group/society hierarchy, seasonal intake, weighbridge integration, input loan deductions, mobile money farmer payment, farmer statements |
| 14 | Project Management | PROJECTS | Project register, budget, milestones, tasks/WBS, timesheets, resource allocation, project costs, project billing (T&M + milestone), subcontractors, project P&L, Gantt, portfolio |
| 15 | Strategy & Balanced Scorecard | STRATEGY_BSC | Strategic framework, BSC perspectives, objectives, KPIs, actuals, traffic-light scoring, scorecard dashboard, initiative tracking, executive report, OKR mode, NGO logframe |
| 16 | Asset Management | ASSETS | Asset register, functional locations, criticality, depreciation (SL/RB), revaluation, disposal with gain/loss, transfer, work requests, work orders, maintenance scheduling, reliability history, insurance, QR/barcode tagging, physical verification, condition-based triggers, and vehicle capital-asset control. Transport dispatch, trips, and live fleet operations are owned by the Transportation module |
| 17 | AI Intelligence | AI_INTELLIGENCE | Cash flow forecasting, GL anomaly detection, demand forecasting, debtor risk scoring, and narrative financial reports - paid add-on available on Professional plans and above; off by default |
| 18 | Product Lifecycle Management | PLM | Engineering item master, revision control, EBOM/MBOM governance, engineering change workflow, effectivity control, NPI stage gates, document control, compliance evidence, and digital-thread release to downstream modules |
| 19 | Transportation & Fleet Operations | TRANSPORTATION | Shipment planning, route and load planning, dispatch, carrier or internal-fleet assignment, ETA and milestone visibility, proof of delivery, exception management, freight audit, transport analytics, driver assignment, and telematics-ready fleet operations |
| 20 | Supply Chain Planning | SUPPLY_CHAIN_PLANNING | Demand planning, consensus forecast governance, supply and replenishment planning, inventory policy optimization, capacity and shortage exceptions, S&OP/IBP cycle management, scenario planning, and financial translation of supply plans into decision-ready views |

> **AI Intelligence Module:** Available on Professional, Business, and Enterprise plans only. Off by default. Account owners activate individual AI features from **Settings -> AI Intelligence**. Requires at least 90 days of transaction history for meaningful forecasting outputs.

## Platform Services (Not User-Facing Modules - Always Active)

| # | Service | Code | Description |
|---|---|---|---|
| P1 | Localisation Engine | LOCALISATION | Configuration-driven localisation: currency, language, tax, statutory, COA starter, address format, invoice legal text, mobile money gateway - per tenant, no code changes per market |
| P2 | Mobile API | MOBILE_API | JWT auth, tenant isolation, rate limiting, versioned REST (v1/v2), offline sync, push notifications, SMS fallback, data-lite mode |
| P3 | Integration Layer | INTEGRATIONS | Africa's Talking, MTN MoMo, Airtel Money, M-Pesa Daraja, URA EFRIS, URA PAYE, NSSF, KRA iTax, NITA-U |
| P4 | Billing & Subscriptions | BILLING | Subscription plans, a-la-carte add-ons, annual billing, payment: card/bank/MTN MoMo/M-Pesa, tenant lifecycle (Trial->Active->Overdue->Suspended->Archived) |

## Subscription Plans

*All prices in Ugandan Shillings (UGX). Annual billing: 10 months charged, 12 months access (2 months free). USD equivalents at ~UGX 3,750/$1.*

| Plan | UGX/month | USD equiv. | Users | Branches | Add-ons Included |
|---|---|---|---|---|---|
| Starter | 250,000 | ~$67 | Up to 5 | Up to 2 | Core 6 modules only |
| Small Business | 500,000 | ~$133 | Up to 15 | Up to 5 | Core + any 2 add-ons |
| Professional | 1,000,000 | ~$267 | Up to 30 | Up to 10 | Core + any 5 add-ons |
| Business | 1,750,000 | ~$467 | Up to 60 | Up to 20 | Core + all add-ons |
| Enterprise | 2,500,000 | ~$667 | Unlimited | Unlimited | All modules + priority support + dedicated onboarding |

*Note: Starter locks out add-on modules. Upgrade to unlock. No per-user fees - price covers the whole organisation.*

## A-La-Carte Add-On Pricing (Small Business and Professional Plans)

| Module | UGX/month | USD equiv. |
|---|---|---|
| HR & Payroll | 150,000 | ~$40 |
| Point of Sale | 100,000 per terminal | ~$27/terminal |
| Advanced Inventory | 150,000 | ~$40 |
| Sales & CRM | 120,000 | ~$32 |
| Sales Agents & Commissions | 100,000 | ~$27 |
| Manufacturing | 250,000 | ~$67 |
| Cooperative Procurement | 250,000 | ~$67 |
| Project Management | 150,000 | ~$40 |
| Strategy & BSC | 120,000 | ~$32 |
| Asset Management | 100,000 | ~$27 |
| Product Lifecycle Management | TBD | TBD |
| Transportation & Fleet Operations | TBD | TBD |
| Supply Chain Planning | TBD | TBD |

## Pricing Rationale

- **UGX-denominated pricing** removes USD exchange rate anxiety for Ugandan SMEs.
- **Org-wide pricing** (not per-seat) is the primary competitive differentiator vs. Odoo and Dynamics - a 50-person company pays the same as a 30-person company at the same tier.
- **Starter at UGX 250,000/month** (~$67) is attainable for a small trading company with 3-5 office staff - comparable to a staff airtime budget.
- **Enterprise at UGX 2,500,000/month** (~$667) is a fraction of Odoo's cost for the same organisation and includes dedicated onboarding.
- **Annual billing incentive** (2 months free) encourages long-term commitment and reduces churn.
- Add-on pricing is stacked. Final standalone pricing for **Product Lifecycle Management** and **Transportation & Fleet Operations** remains subject to packaging review; when approved, the stack shall preserve the natural upgrade trigger toward the Enterprise plan.

## Revenue Milestones

| Phase | Market | MRR Target (UGX) | MRR Target (USD equiv.) |
|---|---|---|---|
| Phase 1 | Uganda | UGX 56M | ~$15K |
| Phase 2 | East Africa | UGX 188M | ~$50K |
| Phase 3 | Francophone Africa | UGX 450M | ~$120K |
| Phase 4 | Enterprise + Global | UGX 1.1B+ | ~$300K+ |

## Module Count Summary

| Category | Count |
|---|---|
| Core modules (always active) | 6 |
| Add-on modules (per-tenant activation) | 14 |
| Platform services (infrastructure, always active) | 4 |
| **Total** | **24** |
