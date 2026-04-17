---
title: "Test Cases — F-004 Suppliers, F-005 Expenses, F-006 Financial Accounts"
document-id: "MADUUKA-TC-002"
version: "1.0"
date: "2026-04-05"
standard: "IEEE Std 829-2008"
---

# Test Cases: F-004 Supplier Management, F-005 Expenses, F-006 Financial Accounts

**Document ID:** MADUUKA-TC-002
**Version:** 1.0
**Date:** 2026-04-05
**Parent Plan:** MADUUKA-TP-001

---

## Module F-004: Supplier and Vendor Management

---

### FR-SUP-003 — Purchase Order Creation

---

**TC-SUP-001**

| Field | Content |
|---|---|
| Test Case ID | TC-SUP-001 |
| FR Reference | FR-SUP-003 |
| Title | Verify purchase order is created with correct total and PDF is generated |
| Preconditions | 1. Supplier "Mukwano Industries" exists in the system. 2. Products "Cooking Oil 5L" (agreed price = UGX 28,000) and "Soap Bar" (agreed price = UGX 1,800) are in the catalogue. 3. Tester is authenticated as Stock Manager or Manager. |
| Test Steps | 1. Navigate to Suppliers > "Mukwano Industries" > New Purchase Order. 2. Add line item: "Cooking Oil 5L" × 20 at UGX 28,000. 3. Add line item: "Soap Bar" × 50 at UGX 1,800. 4. Tap "Create Purchase Order". 5. Download or preview the generated PDF. |
| Expected Result | 1. The purchase order is created with: Supplier = "Mukwano Industries"; Line 1: "Cooking Oil 5L" × 20 × UGX 28,000 = UGX 560,000; Line 2: "Soap Bar" × 50 × UGX 1,800 = UGX 90,000; Order Total = UGX 650,000. 2. The PDF is generated and shows the business logo, address, PO number, supplier name, line items, and total. |
| Pass Criteria | PO total = UGX 650,000; PDF generated with all required fields. |
| Priority | High |

---

### FR-SUP-004 / FR-SUP-005 — Three-Way Purchase Matching (BR-011)

---

**TC-SUP-002**

| Field | Content |
|---|---|
| Test Case ID | TC-SUP-002 |
| FR Reference | FR-SUP-004, FR-SUP-005, BR-011 |
| Title | Verify three-way match passes when PO, goods receipt, and invoice all agree |
| Preconditions | 1. Purchase Order PO-001 exists for "Mukwano Industries": "Cooking Oil 5L" × 20 at UGX 28,000 each. PO total = UGX 560,000. 2. Tester is authenticated as Stock Manager or Manager. |
| Test Steps | 1. Navigate to PO-001 > Record Goods Receipt. 2. Enter received quantity = 20 for "Cooking Oil 5L". 3. Confirm the goods receipt. 4. Navigate to PO-001 > Record Supplier Invoice. 5. Enter invoice amount = UGX 560,000 (matches PO total and received value exactly). 6. Save the invoice. |
| Expected Result | 1. After goods receipt: stock for "Cooking Oil 5L" increments by 20; PO status = "fully received". 2. After invoice entry: the system performs the three-way match (PO total UGX 560,000 = received value UGX 560,000 = invoice UGX 560,000). 3. No discrepancy flag is raised. The invoice status = "matched — available for payment". |
| Pass Criteria | No discrepancy flag; invoice status = "matched — available for payment"; stock incremented by 20. |
| Priority | Critical |

---

**TC-SUP-003**

| Field | Content |
|---|---|
| Test Case ID | TC-SUP-003 |
| FR Reference | FR-SUP-004, FR-SUP-005, BR-011 |
| Title | Verify three-way match raises a discrepancy flag when received quantity is less than PO quantity |
| Preconditions | 1. Purchase Order PO-002 exists for "Mukwano Industries": "Cooking Oil 5L" × 20 at UGX 28,000 each. PO total = UGX 560,000. 2. Tester is authenticated as Stock Manager. |
| Test Steps | 1. Navigate to PO-002 > Record Goods Receipt. 2. Enter received quantity = 18 (2 units short). 3. Confirm the goods receipt. 4. Navigate to PO-002 > Record Supplier Invoice. 5. Enter invoice amount = UGX 560,000 (full PO amount, despite only 18 units received). 6. Save the invoice. |
| Expected Result | 1. After goods receipt: stock increments by 18; PO status = "partially received" with variance of -2 units flagged. 2. After invoice entry: the system flags a quantity discrepancy. Received value = 18 × UGX 28,000 = UGX 504,000; Invoice = UGX 560,000; Variance = UGX 56,000. 3. Invoice status = "discrepancy — pending manager review". 4. The invoice payment action is disabled until a manager resolves the discrepancy. |
| Pass Criteria | Discrepancy flag raised; invoice status = "discrepancy — pending manager review"; payment action disabled; variance amount = UGX 56,000 displayed. |
| Priority | Critical |

---

**TC-SUP-004**

| Field | Content |
|---|---|
| Test Case ID | TC-SUP-004 |
| FR Reference | FR-SUP-005, BR-011 |
| Title | Verify three-way match raises a discrepancy flag when invoice price exceeds PO price |
| Preconditions | 1. Purchase Order PO-003 exists: "Soap Bar" × 50 at UGX 1,800 each. PO total = UGX 90,000. 2. Full goods receipt of 50 units has been confirmed. |
| Test Steps | 1. Navigate to PO-003 > Record Supplier Invoice. 2. Enter invoice amount = UGX 100,000 (exceeds agreed PO total by UGX 10,000 — price variance). 3. Save the invoice. |
| Expected Result | The system flags a price discrepancy: Invoice = UGX 100,000; PO total = UGX 90,000; Variance = UGX 10,000. Invoice status = "discrepancy — pending manager review". The payment action is disabled. A notification is sent to the manager. |
| Pass Criteria | Discrepancy flag raised with variance = UGX 10,000; invoice status = "discrepancy — pending manager review"; payment action disabled. |
| Priority | Critical |

---

**TC-SUP-005**

| Field | Content |
|---|---|
| Test Case ID | TC-SUP-005 |
| FR Reference | FR-SUP-005, BR-011 |
| Title | Verify manager can resolve a three-way match discrepancy and release the invoice for payment |
| Preconditions | 1. Continuation of TC-SUP-004: PO-003 invoice has status "discrepancy — pending manager review". 2. Tester is authenticated as Manager. |
| Test Steps | 1. Navigate to the discrepancy queue. 2. Select PO-003's flagged invoice. 3. Review the discrepancy details. 4. Select resolution = "Accept amended price UGX 100,000". 5. Enter reason = "Supplier price increase — verbally agreed". 6. Tap "Resolve Discrepancy". |
| Expected Result | The invoice status changes to "matched — available for payment". The accepted amount = UGX 100,000 is recorded. An audit log entry is created with: manager ID, PO number, original amount, accepted amount, reason, and timestamp. The payment action becomes available. |
| Pass Criteria | Invoice status = "matched — available for payment"; audit log entry present with correct fields; payment action enabled. |
| Priority | High |

---

### FR-SUP-006 — Supplier Payment

---

**TC-SUP-006**

| Field | Content |
|---|---|
| Test Case ID | TC-SUP-006 |
| FR Reference | FR-SUP-006 |
| Title | Verify partial supplier payment reduces outstanding balance without clearing it |
| Preconditions | 1. Supplier "Mukwano Industries" has outstanding balance = UGX 560,000 from a matched and approved invoice. 2. Tester is authenticated as Accountant or Manager. |
| Test Steps | 1. Navigate to Suppliers > "Mukwano Industries" > Record Payment. 2. Enter payment amount = UGX 300,000, method = Bank Transfer, date = today. 3. Save the payment. 4. View "Mukwano Industries"' outstanding balance. |
| Expected Result | The outstanding balance for "Mukwano Industries" = UGX 260,000 (560,000 - 300,000). A payment record is created with amount = UGX 300,000, method = Bank Transfer, and today's date. |
| Pass Criteria | Outstanding balance = UGX 260,000; payment record created with correct fields. |
| Priority | High |

---

## Module F-005: Expenses and Petty Cash

---

### FR-EXP-003 / FR-EXP-004 — Expense Approval Workflow

---

**TC-EXP-001**

| Field | Content |
|---|---|
| Test Case ID | TC-EXP-001 |
| FR Reference | FR-EXP-001 |
| Title | Verify expense below approval threshold is saved and posted immediately |
| Preconditions | 1. The expense approval threshold = UGX 200,000. 2. The "Cash Drawer" payment account has balance = UGX 500,000. 3. Tester is authenticated as Cashier. |
| Test Steps | 1. Navigate to Expenses > New Expense. 2. Enter amount = UGX 50,000, category = "Transport", method = Cash (from Cash Drawer), date = today. 3. Save the expense. |
| Expected Result | The expense is saved with status = "posted". The "Cash Drawer" balance decrements to UGX 450,000 immediately. No approval notification is sent. |
| Pass Criteria | Expense status = "posted"; Cash Drawer balance = UGX 450,000; no approval notification generated. |
| Priority | High |

---

**TC-EXP-002**

| Field | Content |
|---|---|
| Test Case ID | TC-EXP-002 |
| FR Reference | FR-EXP-003 |
| Title | Verify expense above approval threshold is set to pending_approval and does not post to accounts |
| Preconditions | 1. Expense approval threshold = UGX 200,000. 2. "Cash Drawer" balance = UGX 500,000. 3. Tester is authenticated as Cashier. |
| Test Steps | 1. Navigate to Expenses > New Expense. 2. Enter amount = UGX 350,000, category = "Rent", method = Cash, date = today. 3. Save the expense. |
| Expected Result | The expense is saved with status = "pending_approval". The "Cash Drawer" balance remains UGX 500,000 (unchanged — not posted). A push notification is sent to the designated approver. |
| Pass Criteria | Expense status = "pending_approval"; Cash Drawer balance unchanged at UGX 500,000; push notification sent to approver. |
| Priority | High |

---

**TC-EXP-003**

| Field | Content |
|---|---|
| Test Case ID | TC-EXP-003 |
| FR Reference | FR-EXP-004 |
| Title | Verify manager approval of a pending expense posts the amount to the payment account |
| Preconditions | 1. Continuation of TC-EXP-002: expense for UGX 350,000 is in status "pending_approval". 2. "Cash Drawer" balance = UGX 500,000. 3. Tester is authenticated as Manager. |
| Test Steps | 1. Open the pending approvals list. 2. Find the UGX 350,000 rent expense. 3. Tap "Approve". 4. View the "Cash Drawer" account balance. |
| Expected Result | The expense status changes to "posted". The "Cash Drawer" balance decrements to UGX 150,000 (500,000 - 350,000). An immutable transaction record is created in the "Cash Drawer" account log. |
| Pass Criteria | Expense status = "posted"; Cash Drawer balance = UGX 150,000; transaction record in account log. |
| Priority | High |

---

**TC-EXP-004**

| Field | Content |
|---|---|
| Test Case ID | TC-EXP-004 |
| FR Reference | FR-EXP-003 |
| Title | Verify manager rejection of a pending expense keeps it unposted and records the rejection |
| Preconditions | 1. A second pending expense exists: UGX 250,000 for "Miscellaneous Supplies", status = "pending_approval". 2. "Cash Drawer" balance = UGX 500,000. 3. Tester is authenticated as Manager. |
| Test Steps | 1. Open the pending approvals list. 2. Find the UGX 250,000 miscellaneous expense. 3. Tap "Reject". 4. Enter reason = "No receipt attached". 5. Confirm rejection. 6. View the "Cash Drawer" balance. |
| Expected Result | The expense status changes to "rejected". The "Cash Drawer" balance remains unchanged at UGX 500,000. The rejection is recorded with the manager's name, reason "No receipt attached", and timestamp. |
| Pass Criteria | Expense status = "rejected"; Cash Drawer balance = UGX 500,000 (unchanged); rejection record with manager name, reason, and timestamp. |
| Priority | High |

---

### FR-EXP-005 / FR-EXP-006 / FR-EXP-007 — Petty Cash

---

**TC-EXP-005**

| Field | Content |
|---|---|
| Test Case ID | TC-EXP-005 |
| FR Reference | FR-EXP-005, FR-EXP-007 |
| Title | Verify petty cash disbursement decrements the float and is visible in the disbursement list |
| Preconditions | 1. The petty cash float balance = UGX 100,000. 2. Tester is authenticated as Cashier or Manager. |
| Test Steps | 1. Navigate to Expenses > Petty Cash. 2. Record a disbursement of UGX 15,000 for category "Office Supplies". 3. View the petty cash summary. |
| Expected Result | The petty cash float balance = UGX 85,000 (100,000 - 15,000). The disbursement of UGX 15,000 for "Office Supplies" appears in the disbursements list since last replenishment. Expected balance field = UGX 85,000. |
| Pass Criteria | Float balance = UGX 85,000; disbursement entry visible; expected balance = UGX 85,000. |
| Priority | Medium |

---

**TC-EXP-006**

| Field | Content |
|---|---|
| Test Case ID | TC-EXP-006 |
| FR Reference | FR-EXP-006, FR-EXP-007 |
| Title | Verify petty cash replenishment increments the float and records the source account |
| Preconditions | 1. Petty cash float balance = UGX 85,000. 2. "Cash Drawer" account has balance ≥ UGX 50,000. 3. Tester is authenticated as Manager. |
| Test Steps | 1. Navigate to Expenses > Petty Cash > Replenish. 2. Enter replenishment amount = UGX 50,000, source account = "Cash Drawer". 3. Save. 4. View the petty cash summary. |
| Expected Result | Petty cash float balance = UGX 135,000 (85,000 + 50,000). The replenishment event is recorded with amount = UGX 50,000 and source = "Cash Drawer". The "Cash Drawer" balance decrements by UGX 50,000. |
| Pass Criteria | Petty cash balance = UGX 135,000; Cash Drawer balance decremented by UGX 50,000; replenishment record with source account. |
| Priority | Medium |

---

### FR-EXP-008 — Recurring Expense

---

**TC-EXP-007**

| Field | Content |
|---|---|
| Test Case ID | TC-EXP-007 |
| FR Reference | FR-EXP-008 |
| Title | Verify recurring expense creates a draft entry on the configured recurrence date without posting |
| Preconditions | 1. A recurring expense is configured: Amount = UGX 800,000, Category = "Rent", Method = Bank Transfer, Recurrence = Monthly on the 1st. 2. Today's date is simulated as the 1st of the month (or the scheduler is triggered manually in the test environment). 3. "Bank Account" has balance ≥ UGX 800,000. |
| Test Steps | 1. Advance the system date to the 1st of the next month (test environment clock manipulation), or trigger the scheduler. 2. Navigate to Expenses. 3. Observe the expense list. |
| Expected Result | A draft expense entry is created with: amount = UGX 800,000, category = "Rent", method = Bank Transfer, and status = "draft". The "Bank Account" balance is unchanged (not posted). The draft requires user review and confirmation before posting. |
| Pass Criteria | Draft expense exists with status = "draft"; bank account balance unchanged; draft has correct amount, category, and method. |
| Priority | Medium |

---

## Module F-006: Financial Accounts and Cash Flow

---

### FR-FIN-002 — Real-Time Balance Update

---

**TC-FIN-001**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-001 |
| FR Reference | FR-FIN-002 |
| Title | Verify payment account balance updates in real time when a sale is completed |
| Preconditions | 1. "Cash Drawer" account has balance = UGX 200,000. 2. A POS session is open. 3. Tester is authenticated as Cashier. |
| Test Steps | 1. Complete a cash sale for UGX 30,000. 2. Immediately navigate to Financial Accounts > "Cash Drawer". 3. Observe the balance and transaction log. |
| Expected Result | "Cash Drawer" balance = UGX 230,000 (200,000 + 30,000). An immutable transaction record appears in the log: type = "sale", amount = UGX +30,000, date/time = now. |
| Pass Criteria | Balance = UGX 230,000; transaction record present with type = "sale" and amount = +UGX 30,000. |
| Priority | Critical |

---

### FR-FIN-003 — Inter-Account Cash Transfer

---

**TC-FIN-002**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-002 |
| FR Reference | FR-FIN-003 |
| Title | Verify cash transfer decrements source and increments destination by the same amount |
| Preconditions | 1. "Cash Drawer" balance = UGX 300,000. 2. "MTN MoMo Account" balance = UGX 50,000. 3. Tester is authenticated as Manager or Accountant. |
| Test Steps | 1. Navigate to Financial Accounts > Transfer. 2. Select source = "Cash Drawer", destination = "MTN MoMo Account", amount = UGX 100,000. 3. Save the transfer. 4. View both account balances. |
| Expected Result | "Cash Drawer" balance = UGX 200,000 (300,000 - 100,000). "MTN MoMo Account" balance = UGX 150,000 (50,000 + 100,000). Both accounts' transaction logs contain linked transfer entries for UGX 100,000 with the same transfer reference number. |
| Pass Criteria | Cash Drawer = UGX 200,000; MTN MoMo = UGX 150,000; both transaction logs contain linked entries with same transfer reference. |
| Priority | High |

---

**TC-FIN-003**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-003 |
| FR Reference | FR-FIN-003 |
| Title | Verify cash transfer fails if source account has insufficient balance |
| Preconditions | 1. "Cash Drawer" balance = UGX 80,000. 2. Tester is authenticated as Manager. |
| Test Steps | 1. Initiate a transfer: source = "Cash Drawer", destination = "MTN MoMo Account", amount = UGX 100,000. 2. Tap "Confirm Transfer". |
| Expected Result | The system rejects the transfer with the message: "Insufficient balance. Cash Drawer balance: UGX 80,000. Transfer amount: UGX 100,000." No balance changes occur on either account. |
| Pass Criteria | Transfer rejected; error message with correct balances displayed; no balance changes. |
| Priority | High |

---

### FR-FIN-004 / FR-FIN-005 — Bank Reconciliation

---

**TC-FIN-004**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-004 |
| FR Reference | FR-FIN-004 |
| Title | Verify bank reconciliation allows manual marking of matched transactions |
| Preconditions | 1. "Centenary Bank" account has 5 transaction records for March 2026: T1 = +UGX 150,000, T2 = -UGX 30,000, T3 = +UGX 200,000, T4 = -UGX 80,000, T5 = +UGX 100,000. 2. A paper bank statement confirms T1, T2, T3, T5 are present on the statement. T4 does not appear on the bank statement. 3. Tester is authenticated as Accountant or Manager. |
| Test Steps | 1. Navigate to Financial Accounts > "Centenary Bank" > Reconcile. 2. Select period: March 2026. 3. Mark T1, T2, T3, T5 as "matched". 4. Leave T4 unmatched. 5. Save the reconciliation. |
| Expected Result | T1, T2, T3, T5 display as "matched". T4 remains highlighted as "unmatched". A reconciliation summary shows: Total matched = 4 transactions; 1 unmatched item on the book side (T4 = -UGX 80,000). |
| Pass Criteria | 4 transactions show status = "matched"; T4 shows status = "unmatched"; reconciliation summary counts are correct. |
| Priority | High |

---

**TC-FIN-005**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-005 |
| FR Reference | FR-FIN-005 |
| Title | Verify CSV bank statement import auto-matches transactions by amount and date |
| Preconditions | 1. "Centenary Bank" account has 3 unreconciled transaction records for April 2026: T1 = +UGX 200,000 on 2026-04-01, T2 = -UGX 50,000 on 2026-04-02, T3 = +UGX 75,000 on 2026-04-03. 2. A CSV bank statement file is prepared with 3 rows matching T1, T2, and T3 exactly by amount and date. |
| Test Steps | 1. Navigate to Financial Accounts > "Centenary Bank" > Reconcile > Import Statement. 2. Upload the CSV file. 3. Observe the auto-match results. |
| Expected Result | T1, T2, and T3 are automatically pre-checked as matched. The "Matched" column shows 3 matches. No items appear in the unmatched list. The user may confirm or deselect matches before saving. |
| Pass Criteria | 3 transactions auto-matched; all 3 appear pre-checked; 0 unmatched items. |
| Priority | High |

---

**TC-FIN-006**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-006 |
| FR Reference | FR-FIN-005 |
| Title | Verify CSV bank statement import lists a transaction as unmatched when no system record matches |
| Preconditions | 1. "Centenary Bank" account has 2 unreconciled records: T1 = +UGX 200,000 on 2026-04-01, T2 = -UGX 50,000 on 2026-04-02. 2. The CSV bank statement contains 3 rows: T1 (200,000, 2026-04-01), T2 (50,000, 2026-04-02), and T3 (99,000, 2026-04-04) — T3 has no matching system record. |
| Test Steps | 1. Navigate to Financial Accounts > "Centenary Bank" > Reconcile > Import Statement. 2. Upload the CSV file. 3. Observe the auto-match results. |
| Expected Result | T1 and T2 are auto-matched. T3 (+UGX 99,000 on 2026-04-04) appears in the unmatched items list on the statement side, highlighted for manual review. |
| Pass Criteria | T1 and T2 auto-matched; T3 appears in unmatched list with amount = UGX 99,000 and date = 2026-04-04. |
| Priority | High |

---

### FR-FIN-006 / FR-FIN-007 — Cash Flow and Daily Summary

---

**TC-FIN-007**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-007 |
| FR Reference | FR-FIN-006 |
| Title | Verify cash flow summary correctly totals inflows and outflows for a date range |
| Preconditions | 1. For the period 2026-04-01 to 2026-04-05: Total cash sales receipts = UGX 1,200,000; Total expense payments = UGX 300,000; Total purchase payments = UGX 450,000; Total transfers in = UGX 100,000; Total transfers out = UGX 50,000. 2. Tester is authenticated as Owner or Accountant. |
| Test Steps | 1. Navigate to Financial Accounts > Cash Flow. 2. Select date range 2026-04-01 to 2026-04-05. 3. View the summary. |
| Expected Result | Total Inflows = UGX 1,300,000 (sales UGX 1,200,000 + transfers in UGX 100,000). Total Outflows = UGX 800,000 (expenses UGX 300,000 + purchase payments UGX 450,000 + transfers out UGX 50,000). Net Cash Flow = UGX 500,000. Figures match at both the individual account and total levels. |
| Pass Criteria | Total Inflows = UGX 1,300,000; Total Outflows = UGX 800,000; Net = UGX 500,000. |
| Priority | High |

---

**TC-FIN-008**

| Field | Content |
|---|---|
| Test Case ID | TC-FIN-008 |
| FR Reference | FR-FIN-007 |
| Title | Verify daily summary shows correct opening balance, inflows, outflows, and closing balance |
| Preconditions | 1. "Cash Drawer" opening balance for 2026-04-05 = UGX 75,000 (the session opening float). 2. Cash sales during the day = UGX 200,000. 3. Cash expenses paid during the day = UGX 40,000. 4. Cash refund given = UGX 10,000. |
| Test Steps | 1. Navigate to Financial Accounts > Daily Summary. 2. Select date = 2026-04-05. 3. View "Cash Drawer" summary. |
| Expected Result | Opening Balance = UGX 75,000. Total Inflows = UGX 200,000 (sales). Total Outflows = UGX 50,000 (expenses UGX 40,000 + refund UGX 10,000). Closing Balance = UGX 225,000 (75,000 + 200,000 - 50,000). |
| Pass Criteria | Opening = UGX 75,000; Inflows = UGX 200,000; Outflows = UGX 50,000; Closing = UGX 225,000. |
| Priority | High |

---

*End of MADUUKA-TC-002 v1.0 — Test Cases: F-004 Suppliers, F-005 Expenses, F-006 Financial Accounts*

**Total test cases in this file: 21**
