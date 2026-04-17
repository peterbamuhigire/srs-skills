---
title: "Stakeholder Analysis -- Maduuka"
project: "Maduuka"
document: "Stakeholder Analysis"
version: "1.0"
date: "2026-04-05"
prepared-by: "Chwezi Core Systems"
classification: "Internal -- Pre-Release"
---

# Stakeholder Analysis: Maduuka

## 1. Document Header

| Field | Value |
|---|---|
| Project | Maduuka -- Mobile-First SaaS POS and Bookkeeping |
| Document Type | Stakeholder Analysis |
| Version | 1.0 |
| Date | 2026-04-05 |
| Prepared By | Chwezi Core Systems |
| Methodology | Hybrid (Water-Scrum-Fall) |
| Scope | Phase 1 Core Modules (Android + Web) |
| Standard | IEEE Std 830-1998 -- Stakeholder Identification and Analysis |

This document identifies all Maduuka stakeholders, classifies them by power and interest, defines engagement protocols for high-influence parties, and maps Phase 1 features to a Responsibility Assignment (RACI) matrix. It serves as the baseline for requirements elicitation, change control, and communication planning throughout the project lifecycle.

---

## 2. Stakeholder Register

The table below catalogues all 16 identified stakeholder groups. *Influence* reflects the stakeholder's power to shape or constrain the system. *Interest* reflects the degree to which the stakeholder's goals are affected by the system's outcomes.

| Stakeholder | Role | Influence | Interest | Primary Needs | Key Concerns | Communication Channel |
|---|---|---|---|---|---|---|
| Platform Admin (Chwezi Core Systems) | Provisions all tenant accounts, manages platform operations | High | High | Tenant management, billing, uptime monitoring, fraud detection | Data isolation between tenants, support impersonation audit trail | Internal Chwezi team channels |
| Business Owner | Pays subscription, configures system, manages all staff | High | High | Real-time dashboard KPIs, consolidated multi-branch view, financial health score | Data security, cost versus pirated alternatives, offline reliability | WhatsApp, push notifications, email |
| Accountant | Reads financial data, reconciles accounts, prepares statutory returns | Medium | High | Cash flow reports, debtors ageing, NSSF/PAYE schedule exports | Data accuracy, audit trail completeness, export formats | In-app notifications, email |
| HR Manager | Manages staff records, leave, and payroll | Medium | High | Payroll computation, payslip delivery, leave approvals, attendance | Uganda tax band accuracy, NSSF schedule format, bank payment file format | In-app notifications, push notifications |
| Branch Manager | Manages daily operations for one branch | Medium | High | Branch dashboard, pending approvals, staff management | Accurate stock levels, cashier session oversight | Push notifications, in-app |
| Stock / Inventory Manager | Manages all stock movements across locations | Medium | High | Real-time stock levels, reorder alerts, purchase orders, stock counts | Stock discrepancies, expiry management, multi-location visibility | Push notifications, in-app |
| Cashier / POS Operator | Processes sales at the point of sale | Low | Medium | Fast POS, barcode scan, multi-payment method, hold and resume | System downtime at checkout, slow barcode scan | In-app |
| Pharmacist | Dispenses drugs, manages prescriptions (Phase 2) | Medium | High | Prescription-linked dispensing, drug reference database, NDA compliance log | Dispensing a recalled batch, missed allergy alert, NDA inspection | In-app, push notifications |
| Front Desk Staff (Hotel) | Manages room assignments and guest billing (Phase 3) | Low-Medium | High | Room status board, reservation management, check-in form | Room double-booking, charges not posting to room account | In-app |
| Waiter / Server (Restaurant) | Takes orders and assigns to tables (Phase 2) | Low | Medium | Table map, order entry on mobile, Kitchen Order Ticket send | KOT not reaching kitchen, wrong items on bill | In-app |
| Kitchen Staff (Restaurant) | Executes kitchen orders from Kitchen Display System (Phase 2) | Low | Medium | KDS auto-refresh, colour-coded urgency, mark-done function | Missing KOTs, illegible display, network downtime in kitchen | In-app KDS |
| Customer (Self-Service Portal) | Views own purchase history and account balance | Low | Medium | Magic-link portal (no login required), clear statement of account | Privacy of transaction history | WhatsApp, SMS |
| MTN Uganda (Partner) | Provides MTN MoMo Business API for push payments | Medium | Low-Medium | Correct API integration, POS push payment flow | API rate limits, Business API credentials approval timeline | Partner API documentation, email |
| Airtel Uganda (Partner) | Provides Airtel Money API for push payments | Medium | Low-Medium | API integration for payment collection | Transaction volume thresholds | Partner API documentation, email |
| Uganda Revenue Authority (URA) | Mandates EFRIS compliance for invoice fiscal reporting (Phase 3) | High | Low | Correct EFRIS submission format, Fiscal Document Number issuance, QR code on receipts | Non-compliant submissions, system unavailability during peak filing | URA EFRIS API documentation, regulatory notices |
| National Drug Authority Uganda (NDA) | Mandates controlled drugs register compliance (Phase 2) | High | Low | Controlled drugs register format, NDA drug codes in product database | Incomplete dispensing records, unregistered drugs in catalogue | NDA regulatory guidelines |

---

## 3. Power/Interest Grid

The grid below positions each stakeholder group in one of four engagement quadrants based on the influence and interest ratings in Section 2.

```
HIGH POWER
|
|  KEEP SATISFIED          MANAGE CLOSELY
|  - MTN Uganda            - Platform Admin (Chwezi)
|  - Airtel Uganda         - Business Owner
|  - URA (Phase 3)         - Accountant
|  - NDA (Phase 2)         - HR Manager
|
|---------------------------------------------------- HIGH INTEREST
|
|  MONITOR                 KEEP INFORMED
|  - Kitchen Staff         - Branch Manager
|  - Waiter / Server       - Stock Manager
|                          - Cashier / POS Operator
|                          - Pharmacist (Phase 2)
|                          - Front Desk Staff (Phase 3)
|                          - Customer (Portal)
|
LOW POWER
```

### Quadrant Definitions

**Manage Closely (High Power / High Interest):** These stakeholders have both the authority to influence project outcomes and a direct stake in the system's success. They require the most intensive engagement: frequent communication, early involvement in requirements, and prompt escalation of risks.

**Keep Satisfied (High Power / Low Interest):** These stakeholders have significant power to constrain or block the project but are not direct users of the system. Engagement focuses on ensuring compliance requirements and API access agreements are met. Over-communication risks wasting their attention; under-communication risks regulatory or partner blockers.

**Keep Informed (Low Power / High Interest):** These stakeholders are affected by the system daily but have limited authority to shape its direction. They must receive timely communication about changes that affect their workflows, particularly release notes and training materials.

**Monitor (Low Power / Low Interest):** These stakeholders interact with the system in a limited, context-specific role (Phase 2 add-on modules). They require monitoring but not active engagement in Phase 1.

---

## 4. Stakeholder Engagement Plan

This section defines the engagement protocol for each stakeholder in the "Manage Closely" quadrant. These stakeholders must receive specific, timely information through defined channels at defined frequencies.

### 4.1 Platform Admin (Chwezi Core Systems)

| Attribute | Detail |
|---|---|
| Information Needed | Tenant provisioning status, platform uptime metrics, billing events, security incidents, API error rates |
| Frequency | Continuous (automated monitoring alerts); weekly team review |
| Channel | Internal incident management system, weekly engineering review meeting |
| Escalation Path | Any P1 incident (downtime or data isolation breach) escalates immediately to the CTO |
| Key Deliverables | Tenant onboarding runbook, impersonation audit log, subscription billing reconciliation |

### 4.2 Business Owner

| Attribute | Detail |
|---|---|
| Information Needed | Feature release notes, subscription billing notifications, data security advisories, system downtime notices |
| Frequency | Release notes per sprint delivery; billing notifications per cycle; immediate notification for downtime > 5 minutes |
| Channel | WhatsApp (primary), push notification, email (secondary) |
| Escalation Path | Support ticket escalates to account manager within 4 business hours |
| Key Deliverables | Dashboard KPI cards, business health score, multi-branch consolidated view, offline reliability guarantee |

### 4.3 Accountant

| Attribute | Detail |
|---|---|
| Information Needed | Report format changes, export file format updates, statutory compliance changes (NSSF rates, PAYE bands, VAT rules) |
| Frequency | Monthly for statutory updates; per-release for format changes |
| Channel | In-app notification, email |
| Escalation Path | Statutory compliance discrepancies escalate to the product owner for hotfix prioritisation |
| Key Deliverables | Debtors ageing report, NSSF schedule, PAYE return, bank reconciliation, cash flow summary |

### 4.4 HR Manager

| Attribute | Detail |
|---|---|
| Information Needed | PAYE tax band updates, NSSF rate changes, payroll computation changes, bank payment file format changes |
| Frequency | Immediate notification for any statutory rate change; per-release for feature changes |
| Channel | Push notification, in-app announcement, email |
| Escalation Path | PAYE or NSSF calculation discrepancy escalates to the product owner within 24 hours |
| Key Deliverables | Monthly payroll run result, NSSF schedule, PAYE return, bank salary payment file, payslip delivery confirmation |

---

## 5. RACI Matrix

The matrix below assigns responsibility, accountability, consultative input, and information rights for each Phase 1 feature. Role abbreviations used: **BO** = Business Owner, **BM** = Branch Manager, **CA** = Cashier, **SM** = Stock Manager, **AC** = Accountant, **HR** = HR Manager, **PA** = Platform Admin.

| Feature | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| POS transactions | Cashier (CA) | Branch Manager (BM) | Business Owner (BO) | Accountant (AC) |
| POS session open / close | Cashier (CA) | Branch Manager (BM) | Business Owner (BO) | Accountant (AC) |
| Void and refund processing | Branch Manager (BM) | Business Owner (BO) | Accountant (AC) | Cashier (CA) |
| Offline sale sync | Platform Admin (PA) | Business Owner (BO) | Branch Manager (BM) | Cashier (CA) |
| Product catalogue management | Stock Manager (SM) | Business Owner (BO) | Branch Manager (BM) | Cashier (CA) |
| Goods receiving (purchase order) | Stock Manager (SM) | Branch Manager (BM) | Accountant (AC) | Business Owner (BO) |
| Stock adjustment and approval | Branch Manager (BM) | Business Owner (BO) | Stock Manager (SM) | Accountant (AC) |
| Physical stock count | Stock Manager (SM) | Branch Manager (BM) | Business Owner (BO) | Accountant (AC) |
| Stock transfer between branches | Stock Manager (SM) | Branch Manager (BM) | Business Owner (BO) | Accountant (AC) |
| Customer credit management | Branch Manager (BM) | Business Owner (BO) | Accountant (AC) | Cashier (CA) |
| Debtors ageing and statements | Accountant (AC) | Business Owner (BO) | Branch Manager (BM) | Customer (portal) |
| Supplier payment and matching | Accountant (AC) | Business Owner (BO) | Stock Manager (SM) | Branch Manager (BM) |
| Expense recording and approval | Accountant (AC) | Business Owner (BO) | Branch Manager (BM) | Platform Admin (PA) |
| Bank reconciliation | Accountant (AC) | Business Owner (BO) | Platform Admin (PA) | Branch Manager (BM) |
| Payroll computation | HR Manager (HR) | Business Owner (BO) | Accountant (AC) | All Staff |
| PAYE and NSSF schedule generation | HR Manager (HR) | Business Owner (BO) | Accountant (AC) | URA / NSSF portal |
| Payslip delivery | HR Manager (HR) | Business Owner (BO) | Platform Admin (PA) | All Staff |
| Leave request and approval | HR Manager (HR) | Business Owner (BO) | Branch Manager (BM) | Cashier / All Staff |
| Dashboard KPI display | Platform Admin (PA) | Business Owner (BO) | All roles | All roles |
| Business health score | Platform Admin (PA) | Business Owner (BO) | Accountant (AC) | Branch Manager (BM) |
| 2FA and security settings | Business Owner (BO) | Platform Admin (PA) | -- | All roles |
| Tenant provisioning | Platform Admin (PA) | Platform Admin (PA) | Business Owner (BO) | -- |
| Subscription management | Platform Admin (PA) | Business Owner (BO) | -- | Business Owner (BO) |
| Full data export | Platform Admin (PA) | Business Owner (BO) | -- | Business Owner (BO) |
