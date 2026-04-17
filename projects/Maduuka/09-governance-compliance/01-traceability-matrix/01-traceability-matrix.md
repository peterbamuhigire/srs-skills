---
title: "Traceability Matrix — Maduuka Phase 1"
project: Maduuka
version: "1.0"
date: 2026-04-05
author: Peter Bamuhigire, Chwezi Core Systems
status: Draft
---

# Traceability Matrix: Maduuka Phase 1

## 1. Document Header

| Field | Value |
|---|---|
| Project | Maduuka — Mobile-First SaaS POS and Bookkeeping |
| Document | Requirements Traceability Matrix (RTM) |
| Version | 1.0 |
| Date | 2026-04-05 |
| Author | Peter Bamuhigire, Chwezi Core Systems |
| Status | Draft — Pending Human Review Gate |
| Standard | IEEE 830-1998, IEEE 1012-2016 |
| Scope | Phase 1: Android + Web (all 10 core modules) |

**Purpose:** This matrix traces every functional requirement in Section 4 of the Maduuka Software Requirements Specification to one or more business goals (BG-001–BG-005), Design Covenant constraints (DC-001–DC-006), and business rules (BR-001–BR-016). It assigns a placeholder test case identifier and a MoSCoW priority classification to each requirement, providing the baseline for test plan authoring, impact analysis, and compliance auditing under IEEE 1012.

---

## 2. Business Goals and Design Covenant Reference

### 2.1 Business Goals

| ID | Business Goal | Source |
|---|---|---|
| BG-001 | Acquire 1,000 paying Ugandan business accounts within 12 months of Phase 1 launch. | vision.md §Goals |
| BG-002 | Provide real-time business health visibility on any Android phone — revenue, stock, debtors. | vision.md §Goals |
| BG-003 | Achieve EFRIS compliance coverage for mandated businesses via the Phase 3 add-on module. | vision.md §Goals |
| BG-004 | Expand to all African markets with configurable currency, language, and mobile money gateways. | vision.md §Goals |
| BG-005 | Displace pirated POS software as the dominant solution in Kampala's downtown business district. | vision.md §Goals |

### 2.2 Design Covenant Constraints

| ID | Constraint | Source |
|---|---|---|
| DC-001 | Mobile-first, web-equal: Android app is primary; web is a full-featured equal. | vision.md §Design Covenant |
| DC-002 | Zero mandatory training: any user who can operate WhatsApp can use the application. | vision.md §Design Covenant |
| DC-003 | Offline-first, always: all sales and data recording functions operate without connectivity. | vision.md §Design Covenant |
| DC-004 | Works on a UGX 250,000 Android phone. | vision.md §Design Covenant |
| DC-005 | Currency-neutral and Africa-ready: no hardcoded currency symbols or country assumptions. | vision.md §Design Covenant |
| DC-006 | Compliance built in: underlying records support EFRIS and fiscal audit requirements. | vision.md §Design Covenant |

---

## 3. Requirements Traceability Matrix

### 3.1 Module 4.1 — Point of Sale (FR-POS-xxx)

#### 3.1.1 Product Discovery

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-001 | Display matching products within 500 ms of last keystroke. | BG-001, BG-005, DC-002 | — | TC-POS-001 | Must Have |
| FR-POS-002 | Scan barcode via Android camera; add product to cart within 1 second. | BG-001, BG-005, DC-001, DC-002 | — | TC-POS-002 | Must Have |
| FR-POS-003 | Display products in category grid; filter within 300 ms. | BG-001, BG-005, DC-002 | — | TC-POS-003 | Should Have |
| FR-POS-004 | Show out-of-stock indicator; allow add to cart with warning. | BG-001, BG-005, DC-002 | — | TC-POS-004 | Must Have |

#### 3.1.2 Cart Management

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-005 | Increment cart line quantity; update total in real time. | BG-001, BG-005, DC-002 | — | TC-POS-005 | Must Have |
| FR-POS-006 | Display stock warning when cart quantity exceeds available stock. | BG-001, BG-005 | — | TC-POS-006 | Must Have |
| FR-POS-007 | Accept per-item discount as percentage or fixed amount; recalculate totals. | BG-001, BG-005 | — | TC-POS-007 | Must Have |
| FR-POS-008 | Apply order-level discount to pre-tax subtotal; display discount breakdown. | BG-001, BG-005 | — | TC-POS-008 | Must Have |
| FR-POS-009 | Suspend active cart with hold reference; persist across app restarts. | BG-001, BG-005, DC-003 | — | TC-POS-009 | Should Have |
| FR-POS-010 | Restore held cart with all items, quantities, prices, and discounts intact. | BG-001, BG-005, DC-003 | — | TC-POS-010 | Should Have |

#### 3.1.3 Payment Processing

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-011 | Calculate and display change due before cashier confirms cash payment. | BG-001, BG-005, DC-002 | — | TC-POS-011 | Must Have |
| FR-POS-012 | Initiate MTN MoMo push payment; handle confirmation, failure, and timeout. | BG-001, BG-004, BG-005 | — | TC-POS-012 | Must Have |
| FR-POS-013 | Initiate Airtel Money push payment; equivalent flow to FR-POS-012. | BG-001, BG-004, BG-005 | — | TC-POS-013 | Must Have |
| FR-POS-014 | Display credit limit before confirming credit sale; block if limit exceeded without manager override. | BG-001, BG-005 | BR-002 | TC-POS-014 | Must Have |
| FR-POS-015 | Track each payment component of a split payment separately; require total equals cart total. | BG-001, BG-005 | BR-010 | TC-POS-015 | Must Have |
| FR-POS-016 | Decrement stock for physical items on sale completion; skip service items. | BG-001, BG-002, BG-005 | BR-004 | TC-POS-016 | Must Have |

#### 3.1.4 Receipt Generation

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-017 | Generate full itemised receipt with business name, cashier, totals, and payment breakdown. | BG-001, BG-005, DC-006 | — | TC-POS-017 | Must Have |
| FR-POS-018 | Print receipt to paired Bluetooth thermal printer (Android) or browser dialog (Web) within 5 seconds. | BG-001, BG-005, DC-001 | — | TC-POS-018 | Must Have |
| FR-POS-019 | Generate PDF receipt and open WhatsApp share sheet pre-populated with receipt. | BG-001, BG-005 | — | TC-POS-019 | Should Have |
| FR-POS-020 | Send SMS receipt summary to customer's registered phone via Africa's Talking. | BG-001, BG-005 | — | TC-POS-020 | Should Have |

#### 3.1.5 Session Management

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-021 | Require opening cash float entry before any sale is processed. | BG-001, BG-005 | BR-007 | TC-POS-021 | Must Have |
| FR-POS-022 | Generate session reconciliation report with float, cash totals, expected, actual, and variance. | BG-001, BG-002, BG-005 | BR-007 | TC-POS-022 | Must Have |
| FR-POS-023 | Detect and record receipt sequence gaps on session close. | BG-001, BG-005, DC-006 | BR-008 | TC-POS-023 | Must Have |

#### 3.1.6 Voids and Refunds

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-024 | Allow manager to void a same-day sale; reverse stock and payment; audit log required. | BG-001, BG-005 | BR-003 | TC-POS-024 | Must Have |
| FR-POS-025 | Process product return; restore stock; credit refund to original payment method or credit balance. | BG-001, BG-005 | BR-003 | TC-POS-025 | Must Have |

#### 3.1.7 Offline Operation

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-026 | Process sales, payments, receipts, and session close with no internet connectivity. | BG-001, BG-005, DC-003, DC-004 | BR-009 | TC-POS-026 | Must Have |
| FR-POS-027 | Upload pending transactions in chronological order within 30 seconds of connectivity restoration. | BG-001, BG-005, DC-003 | BR-009 | TC-POS-027 | Must Have |

#### 3.1.8 Weight-Based and Service Items

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-028 | Prompt for weight entry; calculate line total as Weight × Unit Price to 3 decimal places. | BG-001, BG-005 | — | TC-POS-028 | Should Have |
| FR-POS-029 | Process service item sale without triggering stock decrement. | BG-001, BG-005 | BR-004 | TC-POS-029 | Must Have |

#### 3.1.9 POS Web-Specific

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-POS-030 | Accept barcode scanner keyboard events in web terminal mode without search-field focus. | BG-001, BG-005, DC-001 | — | TC-POS-030 | Should Have |

---

### 3.2 Module 4.2 — Inventory and Stock Management (FR-INV-xxx)

#### 3.2.1 Product Catalogue

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-INV-001 | Create product with required name, category, price; accept optional fields. | BG-001, BG-005 | — | TC-INV-001 | Must Have |
| FR-INV-002 | Automatically apply customer-group price tier at POS based on customer assignment. | BG-001, BG-005 | — | TC-INV-002 | Should Have |
| FR-INV-003 | Support multiple selling units; calculate stock consumption in base unit. | BG-001, BG-005 | — | TC-INV-003 | Should Have |
| FR-INV-004 | Validate and import CSV product file; report errors before import; complete within 60 seconds for 5,000 rows. | BG-001, BG-005 | — | TC-INV-004 | Should Have |

#### 3.2.2 Stock Levels

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-INV-005 | Decrement branch stock on sale completion; create immutable stock movement record of type "sale". | BG-001, BG-002, BG-005 | BR-004 | TC-INV-005 | Must Have |
| FR-INV-006 | Increment warehouse stock on goods receipt; create immutable record; update purchase order status. | BG-001, BG-005 | BR-004 | TC-INV-006 | Must Have |
| FR-INV-007 | Generate push notification and dashboard alert when stock falls to or below reorder level. | BG-002, BG-005 | — | TC-INV-007 | Must Have |
| FR-INV-008 | Place transferred stock in "in_transit" status; credit destination on confirmed receipt. | BG-001, BG-005 | BR-004 | TC-INV-008 | Must Have |
| FR-INV-009 | Require reason code for adjustments; hold above-threshold adjustments for manager approval. | BG-001, BG-005 | BR-003, BR-005 | TC-INV-009 | Must Have |

#### 3.2.3 Batch and Expiry Tracking

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-INV-010 | Require batch number, manufacturing date, and expiry date on goods receipt for batch-tracked products. | BG-001, BG-005, DC-006 | BR-006 | TC-INV-010 | Should Have |
| FR-INV-011 | Enforce FEFO batch selection at sale; allow manager-level override. | BG-001, BG-005, DC-006 | BR-006 | TC-INV-011 | Should Have |
| FR-INV-012 | Add near-expiry batches to dashboard alert list within configured threshold (30/60/90 days). | BG-002, BG-005 | — | TC-INV-012 | Should Have |

#### 3.2.4 Stock Valuation and Counting

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-INV-013 | Calculate total stock value using FIFO or weighted average cost; display by product and location. | BG-002, BG-005 | — | TC-INV-013 | Should Have |
| FR-INV-014 | Freeze stock movements during count; record physical quantities; calculate variance; create pending adjustment. | BG-001, BG-005 | BR-005 | TC-INV-014 | Should Have |
| FR-INV-015 | Record supplier return; decrement stock; create immutable record; create supplier credit note. | BG-001, BG-005 | BR-004 | TC-INV-015 | Should Have |
| FR-INV-016 | Record customer return; increment stock (unless damaged); create immutable record; create customer credit note. | BG-001, BG-005 | BR-004 | TC-INV-016 | Must Have |

#### 3.2.5 Reporting

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-INV-017 | Display full stock movement history per product in chronological order. | BG-002, BG-005 | — | TC-INV-017 | Must Have |
| FR-INV-018 | List products with zero sales in last 30 days; sort by days since last sale. | BG-002, BG-005 | — | TC-INV-018 | Should Have |

---

### 3.3 Module 4.3 — Customer Management (FR-CUS-xxx)

#### 3.3.1 Customer Profiles

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-CUS-001 | Create customer with required name and phone; accept district, group, and credit limit. | BG-001, BG-004, BG-005 | — | TC-CUS-001 | Must Have |
| FR-CUS-002 | Automatically apply customer-group price tier at POS on customer selection. | BG-001, BG-005 | — | TC-CUS-002 | Should Have |
| FR-CUS-003 | Deactivate customer reversibly; retain all historical transaction records. | BG-001, BG-005 | BR-003 | TC-CUS-003 | Should Have |

#### 3.3.2 Credit Management

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-CUS-004 | Update customer outstanding balance in real time on credit sale completion. | BG-001, BG-002, BG-005 | BR-002 | TC-CUS-004 | Must Have |
| FR-CUS-005 | Record customer payment; decrement balance; generate receipt on request. | BG-001, BG-005 | — | TC-CUS-005 | Must Have |
| FR-CUS-006 | Display debtors ageing report grouped by 0–30, 31–60, 61–90, and over 90 days. | BG-002, BG-005 | — | TC-CUS-006 | Must Have |
| FR-CUS-007 | Generate customer statement with all transactions and running balance for selected date range. | BG-002, BG-005 | — | TC-CUS-007 | Must Have |

#### 3.3.3 Customer Portal

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-CUS-008 | Send magic link to customer via WhatsApp or SMS; expire after 30 days of inactivity. | BG-001, BG-005, DC-002 | — | TC-CUS-008 | Should Have |
| FR-CUS-009 | Display customer portal with purchase history, balance, and PDF statement; no login required; read-only. | BG-001, BG-005, DC-002 | — | TC-CUS-009 | Should Have |

#### 3.3.4 Customer Map

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-CUS-010 | Display customer location pins on Leaflet.js map on web interface; show balance on pin click. | BG-002, BG-005, DC-001 | — | TC-CUS-010 | Could Have |

---

### 3.4 Module 4.4 — Supplier and Vendor Management (FR-SUP-xxx)

#### 3.4.1 Supplier Directory

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-SUP-001 | Create supplier with name, contact, payment terms, and bank account details. | BG-001, BG-005 | — | TC-SUP-001 | Must Have |
| FR-SUP-002 | Display supplier profile with outstanding balance, purchase history, and delivery performance. | BG-002, BG-005 | — | TC-SUP-002 | Should Have |

#### 3.4.2 Purchase Orders

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-SUP-003 | Create purchase order; calculate total; generate PDF formatted with business branding. | BG-001, BG-005 | — | TC-SUP-003 | Must Have |
| FR-SUP-004 | Record goods receipt against purchase order; support partial receipt; update PO status; flag quantity variance. | BG-001, BG-005 | BR-004 | TC-SUP-004 | Must Have |
| FR-SUP-005 | Flag invoice discrepancy vs PO or goods receipt; block payment until manager resolves three-way match. | BG-001, BG-005 | BR-011 | TC-SUP-005 | Must Have |
| FR-SUP-006 | Record supplier payment; decrement outstanding balance; support partial payment. | BG-001, BG-005 | — | TC-SUP-006 | Must Have |
| FR-SUP-007 | Generate supplier statement with all orders, receipts, invoices, and payments for selected date range. | BG-002, BG-005 | — | TC-SUP-007 | Should Have |

---

### 3.5 Module 4.5 — Expenses and Petty Cash (FR-EXP-xxx)

#### 3.5.1 Expense Recording

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-EXP-001 | Record expense with required amount, date, category, and payment method. | BG-001, BG-005 | BR-003 | TC-EXP-001 | Must Have |
| FR-EXP-002 | OCR-extract total and vendor name from receipt photo on Android; allow correction before saving. | BG-001, BG-005, DC-001, DC-002 | — | TC-EXP-002 | Should Have |
| FR-EXP-003 | Set above-threshold expense to "pending_approval"; notify approver; block posting until approved. | BG-001, BG-005 | BR-003 | TC-EXP-003 | Must Have |
| FR-EXP-004 | Post approved expense amount to specified payment account on manager approval. | BG-001, BG-005 | BR-003 | TC-EXP-004 | Must Have |

#### 3.5.2 Petty Cash

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-EXP-005 | Decrement petty cash float on disbursement; link to expense category. | BG-001, BG-005 | — | TC-EXP-005 | Must Have |
| FR-EXP-006 | Increment petty cash float on replenishment; record source payment account. | BG-001, BG-005 | — | TC-EXP-006 | Must Have |
| FR-EXP-007 | Display current float, all disbursements since last replenishment, and expected balance. | BG-002, BG-005 | — | TC-EXP-007 | Must Have |

#### 3.5.3 Recurring Expenses

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-EXP-008 | Auto-create draft recurring expense on configured date; require user confirmation before posting. | BG-001, BG-005 | — | TC-EXP-008 | Should Have |
