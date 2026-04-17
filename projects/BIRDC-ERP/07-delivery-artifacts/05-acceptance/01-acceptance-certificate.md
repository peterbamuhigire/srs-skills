---
title: "BIRDC ERP — Milestone Acceptance Certificate Template"
subtitle: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
---

# BIRDC ERP Milestone Acceptance Certificate

**Document:** Milestone Acceptance Certificate Template and Stubs
**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com)
**Client:** PIBID / BIRDC, Nyaruzinga hill, Bushenyi District, Western Uganda
**Date:** 2026-04-05
**Version:** 1.0

---

## Section 1 — Purpose

This Milestone Acceptance Certificate (MAC) is the formal instrument by which BIRDC confirms that a delivery milestone has been completed to specification. Execution of this certificate authorises payment for the milestone and permits development to proceed to the next milestone.

A separate MAC is issued for each of the 7 delivery milestones. No milestone payment is due and no subsequent milestone work begins until the MAC for the preceding milestone is signed by both the Finance Director and the BIRDC Director.

**Certificate numbering convention:** `MAC-BIRDC-M-00X-YYYY`, where `X` is the milestone number and `YYYY` is the calendar year of acceptance.

---

## Section 2 — Certificate Template

---

```
MILESTONE ACCEPTANCE CERTIFICATE
BIRDC ERP System Development

Milestone:          [M-001 to M-007 — milestone name]
Date of Review:     [DD-MMM-YYYY]
Certificate No.:    MAC-BIRDC-[M-00X]-[YYYY]
```

---

### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| [Document 1 name] | Accepted / Rejected / Deferred | [Notes if applicable] |
| [Document 2 name] | Accepted / Rejected / Deferred | [Notes if applicable] |
| [Document N name] | Accepted / Rejected / Deferred | [Notes if applicable] |

---

### PHASE GATE CRITERIA

All criteria for this milestone must be ticked PASS before Unconditional Acceptance is granted. A single FAIL blocks unconditional acceptance; the milestone may be conditionally accepted only if the failing criterion is non-critical and a resolution date is agreed.

| # | Gate Criterion | Result |
|---|---|---|
| 1 | [Gate criterion 1 — exact text from metrics.md] | PASS / FAIL |
| 2 | [Gate criterion 2] | PASS / FAIL |
| N | [Gate criterion N] | PASS / FAIL |

---

### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| [Metric name] | [Target from metrics.md] | [Measured during UAT] | PASS / FAIL |

---

### OPEN ITEMS AT ACCEPTANCE

Critical items must be resolved before acceptance is granted. High items may be accepted with an agreed resolution date entered below.

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|
| 1 | [Description] | Critical / High / Medium / Low | [Owner] | [DD-MMM-YYYY] |

*If no open items, write: None.*

---

### DECISION

Mark one:

```
☐ Unconditional Acceptance — all deliverables and gate criteria met; no open items or all
                             open items are Low severity

☐ Conditional Acceptance   — accepted with the open items listed above; payment authorised;
                             resolution dates are binding commitments

☐ Rejected                 — deficiencies identified; milestone not accepted; payment not
                             due; consultant to address findings and resubmit for review
```

---

### SIGNATURES

**Finance Director (Grace Nakimera or incumbent):**

Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Date: \_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Director, BIRDC/PIBID:**

Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Date: \_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Consultant:**

Name: Peter Bamuhigire, ICT Consultant (techguypeter.com) &nbsp;&nbsp; Date: \_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

### PAYMENT AUTHORISATION

Upon Unconditional or Conditional Acceptance above, the following payment is authorised:

```
Milestone:        [M-00X — milestone name]
Amount (UGX):     [Per engagement letter]
Invoice No.:      [Consultant to issue upon signing]
Payment Due:      30 days from the date of this certificate
```

---

## Section 3 — Milestone Certificate Stubs (M-001 through M-007)

---

### MAC-BIRDC-M-001 — Phase 1: Commerce Foundation

**Milestone:** M-001 — Commerce Foundation (Sales, POS, Inventory, Agent Distribution)
**Certificate No.:** MAC-BIRDC-M-001-[YYYY]
**Date of Review:** \_\_\_\_\_\_\_\_\_\_\_\_\_

#### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| Functional Requirements — Sales & Distribution (F-001) | | |
| Functional Requirements — Point of Sale (F-002) | | |
| Functional Requirements — Inventory & Warehouse Management (F-003) | | |
| Functional Requirements — Agent Distribution Management (F-004) | | |
| Sales Agent App (Android) — installed and operational on test device | | |
| Warehouse App (Android) — installed and operational on test device | | |
| EFRIS live integration — invoices and POS receipts submitting to URA | | |
| Dual-track inventory report verified by Store Manager | | |
| UAT sign-off report — Phase 1 | | |

#### PHASE GATE CRITERIA

| # | Gate Criterion | Result |
|---|---|---|
| 1 | All Sales, POS, Inventory, and Agent Distribution functional requirements verified in UAT | PASS / FAIL |
| 2 | EFRIS live on sales invoices and POS receipts — Fiscal Document Numbers returned by URA | PASS / FAIL |
| 3 | Agent cash balance tracking operational — real-time balance visible in system | PASS / FAIL |
| 4 | Dual-track inventory report verified by Store Manager (warehouse stock and agent field stock shown as separate ledgers) | PASS / FAIL |
| 5 | Sales Agent App operational on Android — offline POS, agent stock, remittance submission, commission statement visible | PASS / FAIL |
| 6 | Warehouse App operational on Android — barcode scan for stock receipt, transfer confirmation, physical count | PASS / FAIL |
| 7 | Client sign-off received | PASS / FAIL |

#### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| POS transaction time (search to receipt) — Prossy test | ≤ 90 seconds | | |
| Product search response (barcode or text) | ≤ 500 ms at P95 | | |
| Agent cash balance refresh | Real-time on every transaction post | | |
| Offline POS — data loss on connectivity loss | Zero | | |
| Offline sync time (Android apps, on reconnect) | ≤ 60 seconds | | |

#### OPEN ITEMS AT ACCEPTANCE

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|

*Complete during review.*

#### DECISION

```
☐ Unconditional Acceptance
☐ Conditional Acceptance
☐ Rejected
```

#### SIGNATURES

Finance Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

BIRDC Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

Consultant (Peter Bamuhigire): Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

#### PAYMENT AUTHORISATION

```
Milestone:        M-001 — Commerce Foundation
Amount (UGX):     Per engagement letter
Invoice No.:      [Consultant to issue]
Payment Due:      30 days from certificate date
```

---

### MAC-BIRDC-M-002 — Phase 2: Financial Core

**Milestone:** M-002 — Financial Core (GL, AR, AP, Budget, Executive Dashboard)
**Certificate No.:** MAC-BIRDC-M-002-[YYYY]
**Date of Review:** \_\_\_\_\_\_\_\_\_\_\_\_\_

#### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| Functional Requirements — Financial Accounting & General Ledger (F-005) | | |
| Functional Requirements — Accounts Receivable (F-006) | | |
| Functional Requirements — Accounts Payable (F-007) | | |
| Functional Requirements — Budget Management (F-008) | | |
| Executive Dashboard App (Android) — installed and operational | | |
| Hash chain integrity report — passes on UAT dataset | | |
| Parliamentary budget vote tracking confirmed by Finance Director | | |
| AR aging and agent remittance system UAT report | | |
| Farmer payment batch test report | | |
| UAT sign-off report — Phase 2 | | |

#### PHASE GATE CRITERIA

| # | Gate Criterion | Result |
|---|---|---|
| 1 | Trial Balance, P&L, Balance Sheet, and Cash Flow Statement generate correctly for both PIBID parliamentary and BIRDC commercial modes | PASS / FAIL |
| 2 | Parliamentary budget vote tracking verified by Finance Director | PASS / FAIL |
| 3 | Hash chain integrity check passes on the full UAT GL dataset | PASS / FAIL |
| 4 | AR aging and agent remittance system live and verified | PASS / FAIL |
| 5 | Farmer payment batch tested end-to-end (including MTN MoMo batch payment) | PASS / FAIL |
| 6 | Executive Dashboard App operational on Android — P&L snapshot, Trial Balance summary, cash position, budget variance alerts visible | PASS / FAIL |
| 7 | Client sign-off received | PASS / FAIL |

#### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| Trial balance generation | ≤ 5 seconds | | |
| Report generation (standard report, up to 12 months) | ≤ 10 seconds | | |
| Audit trail query (any 30-day period, any user) | ≤ 5 seconds | | |
| Concurrent web users (peak) | 50 simultaneous without degradation | | |

#### OPEN ITEMS AT ACCEPTANCE

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|

*Complete during review.*

#### DECISION

```
☐ Unconditional Acceptance
☐ Conditional Acceptance
☐ Rejected
```

#### SIGNATURES

Finance Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

BIRDC Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

Consultant (Peter Bamuhigire): Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

#### PAYMENT AUTHORISATION

```
Milestone:        M-002 — Financial Core
Amount (UGX):     Per engagement letter
Invoice No.:      [Consultant to issue]
Payment Due:      30 days from certificate date
```

---

### MAC-BIRDC-M-003 — Phase 3: Supply Chain and Farmers

**Milestone:** M-003 — Supply Chain and Farmers (Procurement, Cooperative Farmer Management)
**Certificate No.:** MAC-BIRDC-M-003-[YYYY]
**Date of Review:** \_\_\_\_\_\_\_\_\_\_\_\_\_

#### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| Functional Requirements — Procurement & Purchasing (F-009) | | |
| Functional Requirements — Farmer & Cooperative Management (F-010) | | |
| Farmer Delivery App (Android) — installed and operational offline | | |
| 5-stage cooperative farmer procurement end-to-end test report | | |
| Individual farmer contribution breakdown test report | | |
| Bulk MTN MoMo farmer payment batch test report | | |
| PPDA procurement documentation checklist verified by Administration Officer | | |
| UAT sign-off report — Phase 3 | | |

#### PHASE GATE CRITERIA

| # | Gate Criterion | Result |
|---|---|---|
| 1 | 5-stage cooperative farmer procurement workflow end-to-end tested with real farmer data | PASS / FAIL |
| 2 | Individual farmer contribution breakdown verified (name, NIN, weight, quality grade, net payable per farmer) | PASS / FAIL |
| 3 | Bulk MTN MoMo farmer payment tested (batch payment file generated and payment confirmed) | PASS / FAIL |
| 4 | PPDA procurement documentation checklist verified by Administration Officer | PASS / FAIL |
| 5 | Farmer Delivery App operational offline — farmer registration, GPS farm profiling, delivery recording, Bluetooth scale integration | PASS / FAIL |
| 6 | Client sign-off received | PASS / FAIL |

#### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| Farmer contribution breakdown (per batch, 100+ farmers) | ≤ 3 seconds | | |
| Offline sync time (Farmer Delivery App, on reconnect) | ≤ 60 seconds | | |
| Report generation (standard report, up to 12 months) | ≤ 10 seconds | | |

#### OPEN ITEMS AT ACCEPTANCE

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|

*Complete during review.*

#### DECISION

```
☐ Unconditional Acceptance
☐ Conditional Acceptance
☐ Rejected
```

#### SIGNATURES

Finance Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

BIRDC Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

Consultant (Peter Bamuhigire): Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

#### PAYMENT AUTHORISATION

```
Milestone:        M-003 — Supply Chain and Farmers
Amount (UGX):     Per engagement letter
Invoice No.:      [Consultant to issue]
Payment Due:      30 days from certificate date
```

---

### MAC-BIRDC-M-004 — Phase 4: Production and Quality

**Milestone:** M-004 — Production and Quality (Manufacturing, QC, Factory Floor App)
**Certificate No.:** MAC-BIRDC-M-004-[YYYY]
**Date of Review:** \_\_\_\_\_\_\_\_\_\_\_\_\_

#### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| Functional Requirements — Manufacturing & Production (F-011) | | |
| Functional Requirements — Quality Control & Laboratory (F-012) | | |
| Factory Floor App (Android) — installed and operational | | |
| Circular economy mass balance verification report | | |
| QC gate blocking test report (inventory release blocked until QC approval) | | |
| Certificate of Analysis (CoA) — domestic format | | |
| Certificate of Analysis (CoA) — minimum 2 export market formats | | |
| UAT sign-off report — Phase 4 | | |

#### PHASE GATE CRITERIA

| # | Gate Criterion | Result |
|---|---|---|
| 1 | Circular economy production order mass balance verified: primary products + by-products + scrap = 100% of input (Business Rule BR-008) | PASS / FAIL |
| 2 | QC gate blocking inventory release tested — stock transfer blocked until QC approves (Business Rule BR-004) | PASS / FAIL |
| 3 | Certificate of Analysis generated for domestic format | PASS / FAIL |
| 4 | Certificate of Analysis generated for minimum 2 export market formats (from: South Korea, EU/Italy, Saudi Arabia, Qatar, USA) | PASS / FAIL |
| 5 | Factory Floor App operational on Android — active order monitoring, worker attendance recording, production completion entry, QC result submission | PASS / FAIL |
| 6 | Client sign-off received | PASS / FAIL |

#### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| Report generation (production and QC reports, up to 12 months) | ≤ 10 seconds | | |
| Mass balance calculation (full production order with by-products) | Completes within report generation threshold ≤ 10 seconds | | |
| Concurrent web users (peak) | 50 simultaneous without degradation | | |

#### OPEN ITEMS AT ACCEPTANCE

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|

*Complete during review.*

#### DECISION

```
☐ Unconditional Acceptance
☐ Conditional Acceptance
☐ Rejected
```

#### SIGNATURES

Finance Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

BIRDC Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

Consultant (Peter Bamuhigire): Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

#### PAYMENT AUTHORISATION

```
Milestone:        M-004 — Production and Quality
Amount (UGX):     Per engagement letter
Invoice No.:      [Consultant to issue]
Payment Due:      30 days from certificate date
```

---

### MAC-BIRDC-M-005 — Phase 5: People

**Milestone:** M-005 — People (Human Resources, Payroll, HR Self-Service App)
**Certificate No.:** MAC-BIRDC-M-005-[YYYY]
**Date of Review:** \_\_\_\_\_\_\_\_\_\_\_\_\_

#### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| Functional Requirements — Human Resources (F-013) | | |
| Functional Requirements — Payroll (F-014) | | |
| HR Self-Service App (Android) — installed and operational | | |
| Payroll calculation verification report (PAYE, NSSF, LST) | | |
| PAYE verification against URA official tax band schedule | | |
| NSSF schedule export in correct NSSF Uganda format | | |
| ZKTeco biometric attendance import test report | | |
| Payroll lock and immutability test report (Business Rule BR-010) | | |
| UAT sign-off report — Phase 5 | | |

#### PHASE GATE CRITERIA

| # | Gate Criterion | Result |
|---|---|---|
| 1 | PAYE calculations verified against Uganda Revenue Authority tax band specification for all income brackets | PASS / FAIL |
| 2 | NSSF calculations verified: employer 10% / employee 5% on correct gross pay base | PASS / FAIL |
| 3 | LST calculations verified per Bushenyi local government ordinance tiers | PASS / FAIL |
| 4 | Biometric attendance import from ZKTeco device tested — daily attendance records imported correctly | PASS / FAIL |
| 5 | Payroll lock and immutability verified — approved payroll run cannot be edited or deleted (Business Rule BR-010) | PASS / FAIL |
| 6 | NSSF contribution schedule generated in the correct NSSF Uganda remittance format | PASS / FAIL |
| 7 | HR Self-Service App operational on Android — leave application, payslip view, leave balance, attendance history visible | PASS / FAIL |
| 8 | Client sign-off received | PASS / FAIL |

#### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| Report generation (payroll summary, up to 12 months) | ≤ 10 seconds | | |
| Payroll calculation run (all active employees) | Completes before approval step — no timeout | | |
| Concurrent web users (peak) | 50 simultaneous without degradation | | |

#### OPEN ITEMS AT ACCEPTANCE

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|

*Complete during review.*

#### DECISION

```
☐ Unconditional Acceptance
☐ Conditional Acceptance
☐ Rejected
```

#### SIGNATURES

Finance Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

BIRDC Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

Consultant (Peter Bamuhigire): Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

#### PAYMENT AUTHORISATION

```
Milestone:        M-005 — People
Amount (UGX):     Per engagement letter
Invoice No.:      [Consultant to issue]
Payment Due:      30 days from certificate date
```

---

### MAC-BIRDC-M-006 — Phase 6: Research, Administration and Compliance

**Milestone:** M-006 — Research, Administration and Compliance (R&D, PPDA, System Administration)
**Certificate No.:** MAC-BIRDC-M-006-[YYYY]
**Date of Review:** \_\_\_\_\_\_\_\_\_\_\_\_\_

#### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| Functional Requirements — Research & Development (F-015) | | |
| Functional Requirements — Administration & PPDA Compliance (F-016) | | |
| Functional Requirements — System Administration / IT (F-017) | | |
| PPDA procurement register — verified by Administration Officer | | |
| PPDA document types verification report (all procurement categories tested) | | |
| R&D banana variety database — loaded with real BIRDC data | | |
| System administration panel functional test report | | |
| User roles and permissions matrix — verified across all modules | | |
| UAT sign-off report — Phase 6 | | |

#### PHASE GATE CRITERIA

| # | Gate Criterion | Result |
|---|---|---|
| 1 | PPDA procurement register operational and all required document types verified by Administration Officer | PASS / FAIL |
| 2 | R&D banana variety performance database loaded with real BIRDC data (cultivar names, yield data, quality scores) | PASS / FAIL |
| 3 | System administration panel fully operational — user management, audit log review, backup scheduling, integration configuration | PASS / FAIL |
| 4 | User roles and permissions matrix verified — 8-layer authorisation tested for all roles across all 17 modules | PASS / FAIL |
| 5 | Client sign-off received | PASS / FAIL |

#### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| Audit trail query (any 30-day period, any user) | ≤ 5 seconds | | |
| Report generation (PPDA procurement register, up to 12 months) | ≤ 10 seconds | | |
| Concurrent web users (peak) | 50 simultaneous without degradation | | |

#### OPEN ITEMS AT ACCEPTANCE

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|

*Complete during review.*

#### DECISION

```
☐ Unconditional Acceptance
☐ Conditional Acceptance
☐ Rejected
```

#### SIGNATURES

Finance Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

BIRDC Director: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

Consultant (Peter Bamuhigire): Date: \_\_\_\_\_\_\_\_\_\_ Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_

#### PAYMENT AUTHORISATION

```
Milestone:        M-006 — Research, Administration and Compliance
Amount (UGX):     Per engagement letter
Invoice No.:      [Consultant to issue]
Payment Due:      30 days from certificate date
```

---

### MAC-BIRDC-M-007 — Phase 7: Integration, Hardening and Go-Live

**Milestone:** M-007 — Integration, Hardening and Go-Live (EFRIS Full Integration, Security Hardening, Production Go-Live)
**Certificate No.:** MAC-BIRDC-M-007-[YYYY]
**Date of Review:** \_\_\_\_\_\_\_\_\_\_\_\_\_

This certificate is the final milestone acceptance for the BIRDC ERP project. Signing this certificate triggers the start of the 12-month warranty period as defined in the Maintenance and Support Plan.

#### DELIVERABLES REVIEWED

| Document Name | Status | Notes |
|---|---|---|
| Functional Requirements — EFRIS Full Integration (F-018) | | |
| Functional Requirements — Security Hardening & Acceptance (F-019) | | |
| Full regression test report — all 17 modules | | |
| EFRIS end-to-end integration report — all document types (invoices, credit notes, POS receipts) | | |
| OWASP Top 10 audit report | | |
| Load test report — 140 MT/day peak simulation | | |
| OAG audit trail simulation report | | |
| Staff training completion register — all user groups | | |
| Go-live cutover plan and execution report | | |
| Deployment Guide (final) | | |
| Operations Runbook (final) | | |
| Data Migration Report (final) | | |
| Maintenance and Support Plan | | |

#### PHASE GATE CRITERIA

| # | Gate Criterion | Result |
|---|---|---|
| 1 | All 17 modules pass full regression testing — no open Critical or High defects | PASS / FAIL |
| 2 | EFRIS fully wired across all document types: sales invoices, credit notes, POS receipts — Fiscal Document Numbers returned on every document | PASS / FAIL |
| 3 | OWASP Top 10 audit passed — all identified vulnerabilities remediated | PASS / FAIL |
| 4 | Load test at 140 MT/day peak simulation passed — all performance thresholds met under peak load | PASS / FAIL |
| 5 | OAG audit trail review simulated and passed — auditor can trace every financial transaction without manual reconciliation | PASS / FAIL |
| 6 | All staff trained — training completion register signed for all user groups | PASS / FAIL |
| 7 | Production go-live completed — system live and in use by BIRDC staff | PASS / FAIL |
| 8 | Client sign-off received | PASS / FAIL |

#### PERFORMANCE VERIFICATION

| NFR Metric | Target | Measured Result | Pass / Fail |
|---|---|---|---|
| POS transaction time (search to receipt) — Prossy test | ≤ 90 seconds | | |
| Product search response (barcode or text) | ≤ 500 ms at P95 | | |
| Report generation (standard report, up to 12 months) | ≤ 10 seconds | | |
| Trial balance generation | ≤ 5 seconds | | |
| Farmer contribution breakdown (per batch, 100+ farmers) | ≤ 3 seconds | | |
| Agent cash balance refresh | Real-time on every transaction post | | |
| Offline POS — data loss on connectivity loss | Zero | | |
| Offline sync time (Android apps, on reconnect) | ≤ 60 seconds | | |
| Concurrent web users (peak load test) | 50 simultaneous without degradation | | |
| Audit trail query (any 30-day period, any user) | ≤ 5 seconds | | |
| System uptime (06:00–22:00 EAT, measured over UAT period) | ≥ 99% | | |
| Database backup completion | ≤ 4 hours for full backup, daily | | |

#### OPEN ITEMS AT ACCEPTANCE

| # | Item Description | Severity | Owner | Resolution Due Date |
|---|---|---|---|---|

*Complete during review. No Critical items may remain open at Phase 7 acceptance.*

#### DECISION

```
☐ Unconditional Acceptance — all deliverables and gate criteria met; system accepted for
                             production; 12-month warranty period commences from this date

☐ Conditional Acceptance   — accepted with the open items listed above; payment authorised;
                             warranty commences from this date; resolution dates are binding

☐ Rejected                 — deficiencies identified; milestone not accepted; payment not
                             due; consultant to address findings and resubmit
```

#### SIGNATURES

**Finance Director (Grace Nakimera or incumbent):**

Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Date: \_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Director, BIRDC/PIBID:**

Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Date: \_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Consultant:**

Name: Peter Bamuhigire, ICT Consultant (techguypeter.com) &nbsp;&nbsp; Date: \_\_\_\_\_\_\_\_\_\_\_\_\_ &nbsp;&nbsp; Signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### WARRANTY COMMENCEMENT

```
Warranty Start Date:   [Date of this certificate]
Warranty End Date:     [12 months from certificate date]
Governing Document:    Maintenance and Support Plan — BIRDC ERP
Post-Warranty Contact: Peter Bamuhigire — peter@techguypeter.com
```

#### PAYMENT AUTHORISATION

```
Milestone:        M-007 — Integration, Hardening and Go-Live (Final Milestone)
Amount (UGX):     Per engagement letter
Invoice No.:      [Consultant to issue]
Payment Due:      30 days from the date of this certificate
```
