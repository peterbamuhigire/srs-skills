# Proposed Solution — Longhorn ERP

## What It Is

Longhorn ERP is a multi-tenant, modular, cloud-hosted SaaS Enterprise Resource Planning platform. It is the flagship product of Chwezi Core Systems and the primary commercial vehicle for the company. Every tenant operates on a shared infrastructure with complete data isolation enforced at the database row level via `tenant_id` on every table.

## What It Does

Longhorn ERP will cover the full operational cycle of a mid-sized organisation across 16 universal modules:

**6 Core modules (always active):**

- Accounting and General Ledger — double-entry, International Financial Reporting Standards (IFRS)-compliant statements, Accounts Payable (AP), Accounts Receivable (AR), bank reconciliation, multi-currency, Value Added Tax (VAT), withholding tax, and budgets.
- Inventory Management — item catalogue, unit-of-measure conversion, First In First Out (FIFO)/weighted-average costing, Goods Received Notes (GRN), reorder levels, stock transfers.
- Sales — quotations, sales orders, delivery notes, invoices, credit notes, receipts, returns.
- Procurement — purchase requisitions, Request for Quotation (RFQ), Local Purchase Order (LPO), three-way matching, supplier payments.
- User Management and Role-Based Access Control (RBAC) — unlimited roles, granular permissions, two-factor authentication (2FA), biometric login.
- Audit Log — immutable audit trail, 7-year retention, external auditor read-only role.

**10 Add-on modules (per-tenant activation):** Advanced Inventory, Manufacturing, HR and Payroll, Point of Sale (POS), Sales and Customer Relationship Management (CRM), Sales Agents and Commissions, Cooperative Procurement, Project Management, Strategy and Balanced Scorecard (BSC), and Asset Management.

## What Makes It Different

**Configuration-driven localisation.** Country-specific tax logic, statutory reporting formats, chart of accounts starters, currency settings, and mobile money gateways are managed as configuration profiles — not code variants. Adding a new country requires no code changes, only a new localisation profile.

**Africa-native integrations, shipped on Day 1.** The integration layer will include: URA EFRIS (Uganda VAT invoice submission), URA PAYE e-returns, NSSF Uganda employer upload, MTN MoMo Application Programming Interface (API) (Uganda, Rwanda), Airtel Money API (Uganda, Kenya, Tanzania), M-Pesa Daraja Business to Customer (B2C) (Kenya, Tanzania), KRA iTax (Kenya), Africa's Talking Short Message Service (SMS) and Unstructured Supplementary Service Data (USSD), and NITA-U SaaS compliance.

**Organisation-wide flat pricing in UGX.** No per-seat fees. A company with 5 users and a company with 30 users pay the same amount at the same tier. Pricing is denominated in Ugandan Shillings, removing exchange rate exposure entirely.

**Zero mandatory training.** Every workflow is designed to be completed without reference to a manual or consultant. If a task requires external guidance, the interface is redesigned. This standard eliminates the hidden implementation cost that makes competing ERP platforms unaffordable in practice.

**Native mobile apps.** Android and iOS mobile applications will feed the same ERP backend via a versioned, rate-limited REST API with offline synchronisation, push notifications, SMS fallback, and data-lite mode for low-bandwidth environments.

**Public API.** A documented public API will allow external systems — including Chwezi sibling products Academia Pro, Medic8, and Kulima — to integrate with Longhorn ERP without proprietary connectors.

Longhorn ERP is designed to beat Odoo and ERPNext on ease of use, and beat SAP and Oracle on price. It is not a feature-reduced simplified tool — it is a full-featured ERP that earns its simplicity through design discipline rather than capability reduction.
