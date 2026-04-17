## Financial Accounting & General Ledger — TC-GL

---

**TC-GL-001** | GL | Journal entry: balanced debit/credit validation

*Preconditions:* Logged in as Finance Officer.

*Test steps:*
1. Navigate to GL → New Journal Entry.
2. Add line 1: DR Cash UGX 100,000.
3. Add line 2: CR Revenue UGX 90,000 (intentionally unbalanced).
4. Attempt to post.

*Expected result:* System blocks posting. Error: "Journal entry is not balanced. Debits: UGX 100,000. Credits: UGX 90,000. Difference: UGX 10,000." JE remains in draft status. | **P1**

---

**TC-GL-002** | GL | GL hash chain integrity check passes on clean dataset

*Preconditions:* ≥ 500 GL entries in test dataset. No manual database modification has occurred.

*Test steps:*
1. Navigate to GL → Audit → Hash Chain Integrity Check.
2. Trigger check.
3. Record time to complete.

*Expected result:* Check completes. Result: "Hash chain intact — 0 broken links." All entries present. (BR-013.) | **P1**

---

**TC-GL-003** | GL | Hash chain broken when GL entry is manually modified in the database

*Preconditions:* Test dataset with 50 GL entries and intact hash chain. DBA access to the test database.

*Test steps:*
1. Confirm hash chain passes (run TC-GL-002 first).
2. Directly update one GL entry's amount in `tbl_gl_entries` via MySQL (simulating tampering).
3. Run hash chain integrity check again.

*Expected result:* System detects a broken link at the modified entry. Report identifies the entry number and account. Finance Manager alert generated. (BR-013 tamper detection confirmed.) | **P1**

---

**TC-GL-004** | GL | GL auto-posting from sales invoice — correct account split

*Preconditions:* Test invoice posted: 10 units Tooke Maize Flour (1kg), UGX 9,000/unit. FIFO cost of this batch: UGX 6,000/unit.

*Test steps:*
1. Post test invoice (see TC-SAL-001 setup).
2. Navigate to GL → Journal Entries → filter by source invoice.

*Expected result:* Two GL entries auto-posted:
- Entry 1: DR Accounts Receivable UGX 90,000 / CR Revenue UGX 90,000.
- Entry 2: DR COGS UGX 60,000 / CR Inventory UGX 60,000.
No manual journal entry created. Entries reference the source invoice number. | **P1**

---

**TC-GL-005** | GL | Sequential JE numbering — gap detection alert

*Preconditions:* JE-2026-0100 through JE-2026-0104 exist. JE-2026-0105 is missing (simulated gap).

*Test steps:*
1. Navigate to GL → Audit → Sequential Number Check.
2. Run check for current period.

*Expected result:* System detects gap at JE-2026-0105. Finance Manager alerted. Gap logged in audit trail. (BR-009.) | **P2**

---

**TC-GL-006** | GL | Dual-mode: parliamentary and IFRS reports from the same dataset

*Preconditions:* Test dataset contains transactions tagged to both PIBID budget votes and BIRDC commercial accounts.

*Test steps:*
1. Generate PIBID Parliamentary Budget Report (by vote code).
2. Generate BIRDC IFRS P&L Report.
3. Verify totals are consistent with the underlying transactions.

*Expected result:* Both reports generated without error. PIBID report shows expenditure by vote code. IFRS P&L shows revenue and expense by IFRS account class. Grand totals reconcile to the same underlying GL transactions. Report generation time ≤ 10 seconds each. (DC-004.) | **P1**

---

**TC-GL-007** | GL | Trial Balance generates in ≤ 5 seconds

*Preconditions:* ≥ 1,000 GL entries in test dataset. 1,307-account chart of accounts loaded.

*Test steps:*
1. Navigate to GL → Reports → Trial Balance.
2. Select current fiscal period.
3. Click generate. Start timer.

*Expected result:* Trial Balance generated. Total debits = total credits. Generation time ≤ 5 seconds. All 1,307 accounts displayed (including zero-balance accounts if "show all" selected). | **P2**

---

**TC-GL-008** | GL | Accounting period management: July–June fiscal year

*Preconditions:* Fiscal year configured as July 2025 – June 2026.

*Test steps:*
1. Attempt to post a journal entry dated June 30, 2025 (prior period).
2. Attempt to post a journal entry dated July 1, 2025 (current period).

*Expected result:* Entry for June 30, 2025 blocked if the period is closed. Entry for July 1, 2025 posts successfully. Period status (open/closed) visible in GL → Period Management. | **P2**

---

## Accounts Receivable — TC-AR

---

**TC-AR-001** | AR | AR aging report: correct bucket distribution

*Preconditions:* Test customer "Aging Test Customer" has 4 outstanding invoices:
- INV-A: UGX 50,000, 10 days overdue (current bucket).
- INV-B: UGX 75,000, 35 days overdue (31–60 day bucket).
- INV-C: UGX 30,000, 65 days overdue (61–90 day bucket).
- INV-D: UGX 20,000, 125 days overdue (120+ day bucket).

*Test steps:*
1. Navigate to AR → Aging Report.
2. Run report for today's date.

*Expected result:* Report shows Aging Test Customer with: Current = UGX 50,000, 31–60 = UGX 75,000, 61–90 = UGX 30,000, 120+ = UGX 20,000. Total = UGX 175,000. Grand total row matches. | **P2**

---

**TC-AR-002** | AR | Customer statement generation

*Preconditions:* Test customer "Statement Customer" has 3 invoices and 1 payment in the current month.

*Test steps:*
1. Navigate to AR → Customer Statement.
2. Select "Statement Customer." Period: current month.
3. Generate statement.

*Expected result:* Statement lists all 3 invoices, the payment, and the resulting balance. Opening balance, closing balance, and movement total are correct. Statement can be exported as PDF. | **P3**

---

**TC-AR-003** | AR | Auto-allocation: payment allocated to oldest invoice first

*Preconditions:* Customer "Payment Test Customer" has: INV-P1 (oldest, UGX 40,000), INV-P2 (UGX 60,000). Customer makes payment UGX 40,000.

*Test steps:*
1. Record payment UGX 40,000 for "Payment Test Customer."
2. Confirm payment.

*Expected result:* Payment auto-allocated to INV-P1 (oldest). INV-P1 fully cleared. INV-P2 unchanged at UGX 60,000. Customer balance: UGX 60,000. | **P2**

---

## Accounts Payable — TC-AP

---

**TC-AP-001** | AP | Three-way matching: payment blocked without PO and GRN

*Preconditions:* Vendor invoice VI-TEST-001 received for UGX 500,000. No matching Purchase Order exists.

*Test steps:*
1. Navigate to AP → Vendor Invoices → Register Invoice.
2. Enter VI-TEST-001 details, amount UGX 500,000.
3. Attempt to approve for payment.

*Expected result:* System blocks payment approval. Error: "No matching Purchase Order found. Three-way matching required (BR-012)." Invoice remains in "Pending PO Match" status. | **P1**

---

**TC-AP-002** | AP | Three-way matching: price variance > 5% flagged for Finance Manager review

*Preconditions:* PO-TEST-010: Tooke packaging materials, unit price UGX 1,000, qty 1,000. GRN-TEST-010: qty 1,000 received. Vendor invoice: qty 1,000, unit price UGX 1,100 (10% above PO price).

*Test steps:*
1. Register vendor invoice against PO-TEST-010 and GRN-TEST-010.
2. Attempt to approve for payment.

*Expected result:* System flags variance: "Price variance 10% exceeds 5% threshold. PO price: UGX 1,000. Invoice price: UGX 1,100. Finance Manager review required." Payment approval blocked until Finance Manager acknowledges. (BR-012.) | **P1**

---

**TC-AP-003** | AP | WHT certificate generation: 6% deducted from applicable service supplier

*Preconditions:* Vendor "ABC Consulting" is a local service supplier subject to WHT. Invoice: UGX 1,000,000.

*Test steps:*
1. Register and approve vendor invoice for ABC Consulting: UGX 1,000,000.
2. Process payment.

*Expected result:* WHT calculated: UGX 1,000,000 × 6% = UGX 60,000. Net payment to vendor: UGX 940,000. WHT payable to URA: UGX 60,000. URA WHT certificate generated in correct format. GL posts: DR AP UGX 1,000,000 / CR Cash UGX 940,000 / CR WHT Payable UGX 60,000. | **P2**

---

## Budget Management — TC-BDG

---

**TC-BDG-001** | Budget | 80% budget vote alert triggered correctly

*Preconditions:* Parliamentary Development Vote "DV-2026-001" allocated UGX 10,000,000. Current expenditure: UGX 7,500,000 (75%).

*Test steps:*
1. Post a transaction of UGX 1,000,000 against DV-2026-001 (bringing total to 85%).

*Expected result:* After posting, system detects cumulative expenditure ≥ 80%. Alert sent to Finance Director and Director: "Budget vote DV-2026-001 has reached 85% of allocation." (BR-014.) | **P1**

---

**TC-BDG-002** | Budget | 100% budget vote: Director override required

*Preconditions:* Budget vote DV-2026-002 allocated UGX 5,000,000. Current expenditure: UGX 4,950,000 (99%).

*Test steps:*
1. Attempt to post a transaction of UGX 100,000 against DV-2026-002 (would exceed 100%).
2. Finance Officer attempts the post.
3. Director attempts the post with justification.

*Expected result:* Finance Officer's post blocked: "Budget vote exceeded. Director-level override required." Director's override: system requires a written justification text field entry. On Director confirmation, transaction posted. Justification logged in audit trail with Director's identity and timestamp. (BR-014.) | **P1**

---

**TC-BDG-003** | Budget | Budget vs. actual report: dual-mode (parliamentary and commercial)

*Preconditions:* ≥ 5 transactions against PIBID budget votes and ≥ 5 against BIRDC commercial budget lines in the test dataset.

*Test steps:*
1. Navigate to Reports → Budget vs. Actual.
2. Generate for PIBID Parliamentary mode.
3. Generate for BIRDC Commercial mode.

*Expected result:* Both reports show: budget allocated, actual spent, variance (amount and %), and % utilised. Reports generated within 10 seconds. Figures match underlying GL transactions. | **P2**

---
