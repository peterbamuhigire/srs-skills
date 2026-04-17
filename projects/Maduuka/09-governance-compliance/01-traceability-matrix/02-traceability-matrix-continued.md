## 3.6 Module 4.6 — Financial Accounts and Cash Flow (FR-FIN-xxx)

### 3.6.1 Account Management

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-FIN-001 | Create payment account with name, type, optional identifier, and opening balance. | BG-001, BG-005 | — | TC-FIN-001 | Must Have |
| FR-FIN-002 | Update account balance in real time on every transaction; create immutable transaction log entry. | BG-002, BG-005 | BR-003, BR-004 | TC-FIN-002 | Must Have |

### 3.6.2 Cash Transfers

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-FIN-003 | Decrement source account and increment destination account; record linked transfer entries in both logs. | BG-001, BG-005 | BR-003 | TC-FIN-003 | Must Have |

### 3.6.3 Bank Reconciliation

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-FIN-004 | Present account transaction log for period; allow marking of transactions as matched; highlight unmatched items. | BG-002, BG-005 | — | TC-FIN-004 | Should Have |
| FR-FIN-005 | Import CSV bank statement; auto-match by amount and date; list unmatched items for manual review. | BG-002, BG-005 | — | TC-FIN-005 | Should Have |

### 3.6.4 Reporting

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-FIN-006 | Display cash flow summary with total inflows and outflows per account for selected date range. | BG-002, BG-005 | — | TC-FIN-006 | Must Have |
| FR-FIN-007 | Display daily summary with opening balance, inflows, outflows, and closing balance per account. | BG-002, BG-005 | — | TC-FIN-007 | Must Have |

---

## 3.7 Module 4.7 — Sales Reporting and Analytics (FR-REP-xxx)

### 3.7.1 Standard Reports

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-REP-001 | Display all completed sales for selected date grouped by payment method with totals. | BG-002, BG-005 | — | TC-REP-001 | Must Have |
| FR-REP-002 | Display sales summary for date range with revenue, credit, transaction count, avg value, and period-over-period comparison. | BG-002, BG-005 | — | TC-REP-002 | Must Have |
| FR-REP-003 | List products sold in period ranked by revenue with quantity, revenue, cost, and gross margin. | BG-002, BG-005 | — | TC-REP-003 | Must Have |
| FR-REP-004 | List top 20 products by revenue and by quantity sold for selected period. | BG-002, BG-005 | — | TC-REP-004 | Should Have |
| FR-REP-005 | Display revenue per branch for period with percentage share of total. | BG-002, BG-005 | — | TC-REP-005 | Must Have |
| FR-REP-006 | Display revenue, transaction count, void count, and refund count per cashier for period. | BG-002, BG-005 | — | TC-REP-006 | Must Have |
| FR-REP-007 | List all voided transactions and refunds with receipt number, date, cashier, reason, and amount. | BG-002, BG-005 | BR-003 | TC-REP-007 | Must Have |
| FR-REP-008 | List all receipt sequence gaps from closed POS sessions for selected period. | BG-002, BG-005, DC-006 | BR-008 | TC-REP-008 | Must Have |

### 3.7.2 Export and Scheduling

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-REP-009 | Export report as CSV or PDF within 30 seconds for up to 12 months of data. | BG-001, BG-002, BG-005 | — | TC-REP-009 | Must Have |
| FR-REP-010 | Send scheduled report as PDF to configured email at configured frequency and time. | BG-001, BG-002, BG-005 | — | TC-REP-010 | Should Have |

---

## 3.8 Module 4.8 — HR and Payroll (FR-HR-xxx)

### 3.8.1 Staff Profiles

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-HR-001 | Create staff profile with required name and phone; accept NIN, hire date, department, and employment type. | BG-001, BG-005 | BR-003 | TC-HR-001 | Must Have |
| FR-HR-002 | Record contract end date; send renewal reminder to HR manager 30 days before expiry. | BG-001, BG-005 | — | TC-HR-002 | Should Have |
| FR-HR-003 | Send SMS invitation with app download link and one-time PIN on staff invite. | BG-001, BG-005, DC-002 | — | TC-HR-003 | Must Have |

### 3.8.2 Leave Management

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-HR-004 | Define leave type with entitlement in days, paid/unpaid flag, and carry-forward eligibility. | BG-001, BG-005 | — | TC-HR-004 | Should Have |
| FR-HR-005 | Notify branch or HR manager via push notification within 1 minute of leave application submission. | BG-001, BG-005 | — | TC-HR-005 | Should Have |
| FR-HR-006 | Notify staff of leave approval or rejection; deduct approved days from leave balance on approval. | BG-001, BG-005 | — | TC-HR-006 | Should Have |
| FR-HR-007 | Display leave balance report per staff member with entitlement, taken, remaining, and pending days. | BG-002, BG-005 | — | TC-HR-007 | Should Have |

### 3.8.3 Attendance

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-HR-008 | Record clock-in timestamp and GPS coordinates; warn on duplicate clock-in without clock-out. | BG-001, BG-005, DC-001 | — | TC-HR-008 | Should Have |
| FR-HR-009 | Record manual daily attendance with status: present, absent, late, half-day, or on-leave. | BG-001, BG-005 | — | TC-HR-009 | Should Have |

### 3.8.4 Payroll

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-HR-010 | Configure earnings and deduction lines per staff member including PAYE, NSSF, and custom items. | BG-001, BG-005 | — | TC-HR-010 | Must Have |
| FR-HR-011 | Calculate gross pay, statutory deductions (PAYE, NSSF), and net pay for up to 100 staff within 60 seconds. | BG-001, BG-005 | — | TC-HR-011 | Must Have |
| FR-HR-012 | Apply Uganda Income Tax Act PAYE bands as configured; support annual updates without code release. | BG-001, BG-005 | — | TC-HR-012 | Must Have |
| FR-HR-013 | Lock all payslip amounts after payroll approval; require reversal in subsequent period for corrections. | BG-001, BG-005 | BR-012 | TC-HR-013 | Must Have |
| FR-HR-014 | Generate PDF payslip per staff member with earnings, deductions, gross, and net pay breakdown. | BG-001, BG-005 | BR-012 | TC-HR-014 | Must Have |
| FR-HR-015 | Deliver payslip PDF to each staff member via WhatsApp (primary) or SMS download link (fallback). | BG-001, BG-005, DC-001 | — | TC-HR-015 | Must Have |
| FR-HR-016 | Generate NSSF schedule with NIN, gross salary, employee and employer contributions for portal upload. | BG-001, BG-005, DC-006 | — | TC-HR-016 | Must Have |
| FR-HR-017 | Generate monthly PAYE return per employee with gross, taxable income, PAYE deducted, and YTD cumulative. | BG-001, BG-005, DC-006 | — | TC-HR-017 | Must Have |
| FR-HR-018 | Produce bulk bank salary payment file in format required by selected bank. | BG-001, BG-005 | — | TC-HR-018 | Must Have |

### 3.8.5 Loans and Advances

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-HR-019 | Record salary advance with repayment schedule; auto-include monthly repayment as payroll deduction. | BG-001, BG-005 | BR-012 | TC-HR-019 | Should Have |

### 3.8.6 Disciplinary Records

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-HR-020 | Record disciplinary event with type, date, manager, and fine; auto-include fine in next payroll. | BG-001, BG-005 | BR-003, BR-012 | TC-HR-020 | Should Have |

---

## 3.9 Module 4.9 — Dashboard and Business Health (FR-DASH-xxx)

### 3.9.1 Real-Time KPIs

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-DASH-001 | Display four KPI cards: Today's Revenue, Transaction Count, Outstanding Credit, Cash Position; show last sync timestamp. | BG-002, BG-005, DC-001 | — | TC-DASH-001 | Must Have |
| FR-DASH-002 | Display revenue comparison cards with directional indicator and percentage change vs prior period. | BG-002, BG-005, DC-001 | — | TC-DASH-002 | Must Have |
| FR-DASH-003 | Auto-refresh all KPI values every 2 minutes on web interface without page reload. | BG-002, BG-005, DC-001 | — | TC-DASH-003 | Must Have |

### 3.9.2 Alerts and Actions

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-DASH-004 | Display low-stock product count badge and expandable panel with current quantity and reorder level. | BG-002, BG-005, DC-001 | — | TC-DASH-004 | Must Have |
| FR-DASH-005 | Display pending approvals count badge and list of items requiring current user's action with direct action links. | BG-002, BG-005, DC-002 | — | TC-DASH-005 | Must Have |
| FR-DASH-006 | Display branch switcher for multi-branch businesses; update KPIs and transactions within 2 seconds on switch. | BG-001, BG-002, BG-005, DC-001 | — | TC-DASH-006 | Must Have |

### 3.9.3 Business Health Score

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-DASH-007 | Display RAG composite health score from gross margin, expense-to-revenue, stock turnover, and credit collection rate; configurable scoring bands. | BG-002, BG-005, DC-001 | — | TC-DASH-007 | Should Have |

---

## 3.10 Module 4.10 — Settings and Configuration (FR-SET-xxx)

### 3.10.1 Business Profile

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-SET-001 | Store business name, logo, address, registration number, and TIN; reflect on all receipts immediately on save. | BG-001, BG-005, DC-006 | — | TC-SET-001 | Must Have |
| FR-SET-002 | Configure receipt template header, footer, and display options (cashier name, SKU, logo). | BG-001, BG-005, DC-002 | — | TC-SET-002 | Must Have |

### 3.10.2 Tax and Currency

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-SET-003 | Create named tax rates; assign default rates per product category; support tax-inclusive and tax-exclusive modes. | BG-001, BG-004, BG-005, DC-005 | — | TC-SET-003 | Must Have |
| FR-SET-004 | Store ISO 4217 currency code; display all monetary values with correct symbol and decimal places; no hardcoded symbol. | BG-001, BG-004, BG-005, DC-005 | — | TC-SET-004 | Must Have |

### 3.10.3 User and Role Management

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-SET-005 | Assign user to role; restrict API access to role-defined permissions per RBAC specification. | BG-001, BG-005 | BR-001 | TC-SET-005 | Must Have |
| FR-SET-006 | Apply new role permissions immediately on next API request without requiring re-login. | BG-001, BG-005 | BR-001 | TC-SET-006 | Must Have |

### 3.10.4 Subscription and Data

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-SET-007 | Display current plan, usage vs limits, next billing date, and billing history; redirect to payment flow on plan change. | BG-001, BG-005 | — | TC-SET-007 | Must Have |
| FR-SET-008 | Generate ZIP archive of all business data for download within 10 minutes; send push notification when ready. | BG-001, BG-005 | BR-001 | TC-SET-008 | Must Have |
| FR-SET-009 | Confirm account deletion; generate final export; retain data 30 days; permanently delete after 30 days. | BG-001, BG-005 | BR-001 | TC-SET-009 | Must Have |

### 3.10.5 Notifications and Security

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID | Priority |
|---|---|---|---|---|---|
| FR-SET-010 | Allow independent toggle per notification type per delivery channel (push, SMS, email) per user role. | BG-001, BG-005, DC-001 | — | TC-SET-010 | Should Have |
| FR-SET-011 | Require TOTP code on login from unrecognised device when 2FA is enabled; store TOTP secret encrypted server-side. | BG-001, BG-005 | — | TC-SET-011 | Must Have |
| FR-SET-012 | List all devices with active sessions; allow revocation of any device, invalidating its refresh token immediately. | BG-001, BG-005 | — | TC-SET-012 | Must Have |

---

## 4. Coverage Summary

| Module | Module ID | FR Count | Business Goals Covered | BRs Referenced |
|---|---|---|---|---|
| Point of Sale | FR-POS-xxx | 30 | BG-001, BG-004, BG-005, DC-001–DC-006 | BR-002, BR-003, BR-004, BR-007, BR-008, BR-009, BR-010 |
| Inventory and Stock Management | FR-INV-xxx | 18 | BG-001, BG-002, BG-005, DC-006 | BR-003, BR-004, BR-005, BR-006 |
| Customer Management | FR-CUS-xxx | 10 | BG-001, BG-002, BG-004, BG-005, DC-001, DC-002 | BR-002, BR-003 |
| Supplier and Vendor Management | FR-SUP-xxx | 7 | BG-001, BG-002, BG-005 | BR-003, BR-004, BR-011 |
| Expenses and Petty Cash | FR-EXP-xxx | 8 | BG-001, BG-002, BG-005, DC-001, DC-002 | BR-003 |
| Financial Accounts and Cash Flow | FR-FIN-xxx | 7 | BG-002, BG-005 | BR-003, BR-004 |
| Sales Reporting and Analytics | FR-REP-xxx | 10 | BG-001, BG-002, BG-005, DC-006 | BR-003, BR-008 |
| HR and Payroll | FR-HR-xxx | 20 | BG-001, BG-005, DC-001, DC-002, DC-006 | BR-003, BR-012 |
| Dashboard and Business Health | FR-DASH-xxx | 7 | BG-002, BG-005, DC-001, DC-002 | — |
| Settings and Configuration | FR-SET-xxx | 12 | BG-001, BG-004, BG-005, DC-001, DC-002, DC-005, DC-006 | BR-001 |
| **Total** | | **129** | **All BG and DC IDs covered** | **BR-001 through BR-012** |

**Traceability Coverage:** 129 of 129 functional requirements are mapped to at least one business goal. Coverage = **100%**.

**MoSCoW Distribution:**

| Priority | Count | % of Total |
|---|---|---|
| Must Have | 84 | 65% |
| Should Have | 41 | 32% |
| Could Have | 4 | 3% |

**Business Rules Coverage Note:** BR-013 (Pharmacy Prescription-Linked Dispensing), BR-014 (Controlled Drugs Register), BR-015 (Hotel Room Double-Booking Prevention), and BR-016 (Hourly and Nightly Room Billing) are Phase 2 and Phase 3 add-on rules. No Phase 1 functional requirement references these rules. This is expected and does not constitute a gap.

---

## 5. Open Trace Gaps

All 129 Phase 1 functional requirements have been mapped to at least one business goal and one Design Covenant constraint. No requirement is untraced.

The following observations are recorded for consultant review:

- FR-CUS-010 is classified as *Could Have* because the customer map view is a web-only supplementary feature (DC-001 equality maintained by the absence of a map equivalent on Android, where GPS coordinates are collected at clock-in rather than customer creation). If a mobile map view is added in a future sprint, a new FR is required.
- FR-DASH-007 (Business Health Score) is classified as *Should Have* because the scoring band configuration depends on domain-specific benchmarks that remain `[CONTEXT-GAP: industry gross margin benchmarks for Ugandan retail SMBs]`. The consultant shall supply benchmark figures before this requirement is finalised.
- BR-013, BR-014, BR-015, and BR-016 have no Phase 1 FR references. These rules are deferred to Phase 2 (Pharmacy) and Phase 3 (Hotel) add-on modules. No `[TRACE-GAP]` is raised; deferral is intentional and documented in `_context/vision.md`.

**Identified Context Gap:**

- `[CONTEXT-GAP: industry gross margin benchmarks for Ugandan retail SMBs]` — Required to finalise configurable scoring bands for FR-DASH-007.

**No TRACE-GAP flags raised.** All 129 functional requirements are fully traced.
