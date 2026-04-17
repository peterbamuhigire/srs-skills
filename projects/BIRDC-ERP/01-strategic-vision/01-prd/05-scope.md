# Section 4: Scope

## 4.1 In-Scope: 17 Modules Across 7 Delivery Phases

The BIRDC ERP system comprises 17 functional modules delivered across 7 phases. Each phase produces a working, testable software increment.

### Phase 1 — Commerce Foundation

| Module ID | Module Name | Summary |
|---|---|---|
| F-001 | Sales and Distribution | Order-to-cash cycle, EFRIS invoice submission, territory tracking, credit management |
| F-002 | Point of Sale (POS) | Factory gate, distribution centre, and agent POS; multi-payment; offline POS |
| F-003 | Inventory and Warehouse Management | Dual-track inventory, FEFO enforcement, batch/lot tracking, stock valuation |
| F-004 | Agent Distribution Management | Agent registration, real-time cash balance, FIFO remittance, commission calculation |

### Phase 2 — Financial Core

| Module ID | Module Name | Summary |
|---|---|---|
| F-005 | Financial Accounting and General Ledger | Dual-mode IFRS + parliamentary accounting, hash chain integrity, financial statements on demand |
| F-006 | Accounts Receivable | AR aging, agent receivable tracking, credit control, payment receipts |
| F-007 | Accounts Payable | Three-way matching, vendor payments, farmer bulk payment via mobile money |
| F-008 | Budget Management | Parliamentary vote tracking, commercial budgets, variance alerts |

### Phase 3 — Supply Chain and Farmers

| Module ID | Module Name | Summary |
|---|---|---|
| F-009 | Procurement and Purchasing | PPDA-compliant workflow, RFQ, LPO, GRN, 5-stage cooperative farmer procurement |
| F-010 | Farmer and Cooperative Management | Farmer registration, GPS farm profiling, contribution history, bulk payment |

### Phase 4 — Production and Quality

| Module ID | Module Name | Summary |
|---|---|---|
| F-011 | Manufacturing and Production | Bill of Materials, circular economy recipes, mass balance, production costing |
| F-012 | Quality Control and Laboratory | Inspection templates, CoA generation (domestic and export-grade), SPC charts, NCR management |

### Phase 5 — People

| Module ID | Module Name | Summary |
|---|---|---|
| F-013 | Human Resources | Employee lifecycle, ZKTeco biometric integration, leave management, staff loans |
| F-014 | Payroll | Uganda PAYE, NSSF, LST, payroll lock, bulk mobile money salary disbursement |

### Phase 6 — Research, Administration, and Compliance

| Module ID | Module Name | Summary |
|---|---|---|
| F-015 | Research and Development | Banana variety performance, field trial management, product development register |
| F-016 | Administration and PPDA Compliance | PPDA documentation management, asset register, vehicle logbook, document management |
| F-017 | System Administration | User management, 8-layer RBAC, audit log, backup scheduling, integration configuration |

### Phase 7 — Integration, Hardening, and Go-Live

| Module ID | Module Name | Summary |
|---|---|---|
| F-018 | EFRIS Full Integration | Full URA EFRIS system-to-system API across all transaction types |
| F-019 | Security Hardening and Acceptance | OWASP Top 10 remediation, penetration test, load test, regression, staff training, go-live cutover |

## 4.2 In-Scope: 6 Android Mobile Applications

| App Name | Primary Users | Core Capability |
|---|---|---|
| Sales Agent App | 1,071 field sales agents | Offline POS, agent stock view, remittance submission, commission statements, Bluetooth thermal printing |
| Farmer Delivery App | Field collection officers | Offline farmer registration, GPS farm profiling, individual delivery recording, Bluetooth scale integration |
| Warehouse App | Warehouse staff | Barcode scanning for stock receipts, transfers, and physical counts |
| Executive Dashboard App | Director, Finance Director | Real-time P&L snapshot, Trial Balance summary, cash position, budget variance push notifications |
| HR Self-Service App | All staff (150+) | Leave applications, payslip access, leave balance, attendance view |
| Factory Floor App | Production supervisors, QC staff | Active production order monitoring, worker attendance, production completion entry, QC result submission |

All 6 Android apps require a minimum Android version of 8.0 (API level 26).

## 4.3 Three Web Application Panels

| Panel | URL Path | Primary Users |
|---|---|---|
| Main ERP Workspace | `/public/` | All BIRDC/PIBID staff |
| Sales Agent Portal | `/public/sales-agents/` | 1,071 field sales agents |
| System Administration | `/public/admin/` | IT administrators and super-users |

