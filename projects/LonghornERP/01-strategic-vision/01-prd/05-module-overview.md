# Module Overview

## Universality Principle

All modules are universal. Localisation behaviour — country-specific tax rules, statutory integrations, currency handling, regulatory workflows, and chart of accounts defaults — is determined by the tenant's configuration profile, not by module variants. A Ugandan manufacturer and a Kenyan NGO activate modules from the same codebase; their statutory and currency behaviour differs because their localisation profiles differ.

## Core Modules (Always Active — Cannot Be Disabled)

| Code | Module | Description |
|---|---|---|
| `ACCOUNTING` | Accounting & General Ledger | Double-entry General Ledger (GL), IFRS-compliant financial statements, AP, AR, bank reconciliation, multi-currency, VAT/WHT, budgets |
| `INVENTORY` | Inventory Management | Item catalogue, UOM conversion, FIFO/weighted-average costing, Goods Received Note (GRN), stock adjustments, reorder levels, physical count, stock transfers |
| `SALES` | Sales | Customer master, price lists, quotations, sales orders, delivery notes, invoices, credit notes, receipts, returns |
| `PROCUREMENT` | Procurement | Supplier master, purchase requisitions, RFQ, LPO, three-way matching, supplier payments, WHT |
| `USER_MGMT` | User Management & RBAC | User lifecycle, unlimited roles, granular permissions, branch restrictions, approval limits, 2FA, biometric login, USSD access |
| `AUDIT` | Audit Log | Immutable INSERT-only audit trail covering all CRUD and approval actions, external auditor read-only role, 7-year retention |

## Add-On Modules (Per-Tenant Activation)

| Code | Module | Description |
|---|---|---|
| `ADV_INVENTORY` | Advanced Inventory | Multi-location warehousing, batch/serial tracking, First-Expired-First-Out (FEFO), expiry management, inter-branch stock-in-transit, landed cost, stock reservation, recall management |
| `MANUFACTURING` | Manufacturing | Bill of Materials (BOM) with versions, production orders, raw material issue, Work in Progress (WIP), yield/variance, by-products, QC checkpoints, scrap, overhead absorption, production costing |
| `HR_PAYROLL` | HR & Payroll | Employee master, contracts, org structure, grade/salary scales, leave, attendance (biometric/mobile), payroll processing, bank payment files, mobile money salary, statutory compliance |
| `POS` | Point of Sale | Touch-optimised terminal, barcode scanning, multi-payment modes, mobile money push, thermal receipt, shift management, restaurant/bar table mode, offline mode, real-time GL posting |
| `SALES_CRM` | Sales & CRM | Leads pipeline, opportunities, Kanban view, activity logging, contact management, quotation tracking, sales forecasting, territory management, WhatsApp logging |
| `SALES_AGENTS` | Sales Agents & Commissions | Agent register, target setting, commission rules (flat/tiered/product), commission runs, approval, mobile money bulk payment, agent self-service portal |
| `COOPERATIVE` | Cooperative Procurement | Commodity configuration, farmer/outgrower registration, group/society hierarchy, seasonal intake, weighbridge integration, input loan deductions, mobile money farmer payment, farmer statements |
| `PROJECTS` | Project Management | Project register, budget, milestones, tasks/Work Breakdown Structure (WBS), timesheets, resource allocation, project costs, project billing (T&M and milestone), subcontractors, project P&L, Gantt, portfolio |
| `STRATEGY_BSC` | Strategy & Balanced Scorecard | Strategic framework, Balanced Scorecard (BSC) perspectives, objectives, KPIs, actuals, traffic-light scoring, scorecard dashboard, initiative tracking, executive report, Objectives and Key Results (OKR) mode, NGO logframe |
| `ASSETS` | Asset Management | Asset register, depreciation (straight-line/reducing-balance), revaluation, disposal with gain/loss, transfer, maintenance scheduling, insurance, QR/barcode tagging, physical verification |

## Platform Services (Always Active — Not User-Facing Modules)

Platform services are infrastructure components that underpin all tenant operations. They are not activatable or deactivatable per tenant.

| Code | Service | Description |
|---|---|---|
| `LOCALISATION` | Localisation Engine | Configuration-driven localisation: currency, language, tax, statutory, Chart of Accounts (COA) starter, address format, invoice legal text, mobile money gateway — per tenant, no code changes per market |
| `MOBILE_API` | Mobile API | JWT auth, tenant isolation, rate limiting, versioned REST (v1/v2), offline sync, push notifications, SMS fallback, data-lite mode |
| `INTEGRATIONS` | Integration Layer | Africa's Talking, MTN MoMo, Airtel Money, M-Pesa Daraja, URA EFRIS, URA PAYE, NSSF, KRA iTax, NITA-U |
| `BILLING` | Billing & Subscriptions | Subscription plans, a-la-carte add-ons, annual billing, payment via card/bank/MTN MoMo/M-Pesa, tenant lifecycle management (Trial → Active → Overdue → Suspended → Archived) |

## Module Count Summary

| Category | Count |
|---|---|
| Core modules (always active) | 6 |
| Add-on modules (per-tenant activation) | 10 |
| Platform services (infrastructure, always active) | 4 |
| **Total** | **20** |
