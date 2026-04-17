## Sales & Distribution — TC-SAL

---

**TC-SAL-001** | Sales & Distribution | Invoice lifecycle: draft to issued with EFRIS FDN

*Preconditions:* Logged in as Sales Officer. Test customer "BIRDC Test Customer 01" exists. Tooke Maize Flour (500g) in stock: 100 units at UGX 4,500/unit.

*Test steps:*
1. Navigate to Sales → New Invoice.
2. Select customer "BIRDC Test Customer 01."
3. Add line item: Tooke Maize Flour (500g), qty 10, unit price UGX 4,500.
4. Save as draft.
5. Confirm invoice.

*Expected result:* Invoice status changes to "Pending EFRIS." System submits invoice to EFRIS sandbox. EFRIS returns a valid FDN and QR code. Invoice status changes to "Issued." Invoice displays FDN and QR code. GL auto-posts: DR Accounts Receivable UGX 45,000 / CR Revenue UGX 45,000. COGS entry posted: DR COGS / CR Inventory. | **P1**

---

**TC-SAL-002** | Sales & Distribution | Credit limit enforcement blocks invoice confirmation

*Preconditions:* Test customer "BIRDC Test Customer 02" has credit limit UGX 100,000 and existing unpaid balance UGX 80,000.

*Test steps:*
1. Create a new invoice for Test Customer 02: Tooke Banana Chips (200g), qty 50, unit price UGX 2,000 (total UGX 100,000).
2. Attempt to confirm the invoice.

*Expected result:* System blocks confirmation. Error message: "Credit limit exceeded. Available credit: UGX 20,000. Invoice total: UGX 100,000." Invoice remains in draft status. No GL entry posted. | **P2**

---

**TC-SAL-003** | Sales & Distribution | Void invoice retains number and posts reversal

*Preconditions:* Invoice INV-TEST-001 exists in "Issued" status. No payment applied.

*Test steps:*
1. Open INV-TEST-001.
2. Click **Void**. Enter void reason: "Customer order cancelled."
3. Confirm void.

*Expected result:* Invoice status changes to "Void." Invoice number INV-TEST-001 is retained with "VOID" watermark. A reversal GL entry is posted (reversing the original DR AR / CR Revenue and DR COGS / CR Inventory). The sequential number is not reused. Finance Manager receives void notification. | **P2**

---

**TC-SAL-004** | Sales & Distribution | Credit note reduces AR balance

*Preconditions:* Invoice INV-TEST-002 exists in "Issued" status, value UGX 45,000. Customer returned 2 units.

*Test steps:*
1. Navigate to INV-TEST-002 → **Issue Credit Note**.
2. Enter qty: 2, unit price UGX 4,500. Reason: "Goods returned — quality issue."
3. Confirm credit note.

*Expected result:* Credit note CN-TEST-001 issued. AR balance for customer reduced by UGX 9,000. GL posts: DR Revenue UGX 9,000 / CR AR UGX 9,000. Inventory restocked: DR Inventory / CR COGS UGX 9,000. EFRIS sandbox notified with credit note document. | **P2**

---

**TC-SAL-005** | Sales & Distribution | Territory-based sales report

*Preconditions:* At least 10 test invoices posted across 3 test territories in the current month.

*Test steps:*
1. Navigate to Reports → Sales by Territory.
2. Filter: current month, all territories.
3. Generate report.

*Expected result:* Report displays each territory with: total invoices, total revenue (UGX), and % of total revenue. Grand total revenue matches sum of all test invoices. Report generation time ≤ 10 seconds. | **P3**

---

**TC-SAL-006** | Sales & Distribution | Daily sales summary push notification

*Preconditions:* Director and Sales Manager accounts exist with push notification enabled.

*Test steps:*
1. Post 5 sales invoices during business hours.
2. Trigger end-of-day summary (or wait for scheduled job).

*Expected result:* Director and Sales Manager receive push notification with: total invoices count, total revenue for the day, and top-selling product. | **P3**

---

## Point of Sale — TC-POS

---

**TC-POS-001** | POS | Factory gate POS: cash sale with 80mm thermal receipt

*Preconditions:* POS session opened by cashier "Test Cashier 01" with opening float UGX 50,000. Tooke Banana Chips (200g) in warehouse stock: 200 units.

*Test steps:*
1. Open POS session.
2. Search product by name: "chips."
3. Select Tooke Banana Chips (200g). Qty: 3.
4. Payment method: Cash. Amount tendered: UGX 10,000.
5. Complete sale.
6. Print 80mm thermal receipt.

*Expected result:* POS receipt generated with: item name, qty, unit price, total UGX 6,000, cash tendered UGX 10,000, change UGX 4,000, FDN and QR code (EFRIS). Thermal receipt prints correctly formatted on 80mm paper. Warehouse stock reduced by 3 units. GL auto-posts: DR Cash / CR Revenue, DR COGS / CR Inventory. | **P1**

---

**TC-POS-002** | POS | Multi-payment split: MTN MoMo + cash

*Preconditions:* POS session open. Product in stock: Tooke Maize Flour (1kg), UGX 9,000/unit.

*Test steps:*
1. Add 2 units of Tooke Maize Flour (1kg). Total: UGX 18,000.
2. Select split payment: MTN MoMo UGX 10,000, Cash UGX 8,000.
3. Confirm MoMo payment (sandbox confirmation).
4. Complete sale.

*Expected result:* Transaction recorded with two payment legs. GL posts: DR Cash UGX 8,000 + DR MoMo Receivable UGX 10,000 / CR Revenue UGX 18,000. Receipt shows both payment methods and amounts. | **P2**

---

**TC-POS-003** | POS | Offline POS: 10 transactions with no network, full sync on reconnect

*Preconditions:* Sales Agent App installed on test Android device (Android 8.0+). Device set to Airplane Mode. Agent "Test Agent 01" logged in offline.

*Test steps:*
1. Record 10 POS transactions offline (varied products, varied payment types: cash and MoMo).
2. After all 10 transactions, restore network connectivity.
3. Observe sync.

*Expected result:* All 10 transactions stored locally in Room database during offline period. On reconnect, WorkManager sync job runs. All 10 transactions appear on the server within 60 seconds. GL auto-posts for all 10 transactions confirmed. Agent cash balance updated on server. Zero transactions lost. | **P1**

---

**TC-POS-004** | POS | POS session reconciliation: variance detected

*Preconditions:* POS session for "Test Cashier 02." Opening float: UGX 100,000. 5 cash sales totalling UGX 75,000 recorded.

*Test steps:*
1. End POS session.
2. Enter physical cash count: UGX 170,000 (expected: UGX 175,000).

*Expected result:* System calculates variance: UGX 175,000 expected - UGX 170,000 counted = UGX -5,000 shortage. Variance report generated. Finance Manager alerted. POS session closed with variance flag. | **P2**

---

**TC-POS-005** | POS | FEFO enforcement at POS — earliest expiry batch selected automatically

*Preconditions:* Tooke Maize Flour (1kg) in stock: Batch A (expiry 2026-06-30, qty 50), Batch B (expiry 2026-03-15, qty 30). FEFO rule active (BR-007).

*Test steps:*
1. Add Tooke Maize Flour (1kg), qty 5 to POS transaction.
2. Observe batch allocation.

*Expected result:* System automatically allocates from Batch B (earliest expiry 2026-03-15). Batch A not touched. Cashier cannot override batch selection at POS screen. | **P1**

---

**TC-POS-006** | POS | Barcode scan product lookup ≤ 500 ms

*Preconditions:* Product catalogue loaded with ≥ 100 products. Barcode scanner connected (ML Kit camera).

*Test steps:*
1. Scan barcode of Tooke Banana Chips (200g).
2. Measure time from scan to product display.

*Expected result:* Product name, unit price, and available stock displayed within 500 ms of scan. | **P2**

---

**TC-POS-007** | POS | Agent POS uses agent virtual inventory — not warehouse stock

*Preconditions:* Agent "Test Agent 02" has virtual stock: Tooke Banana Chips (200g) qty 40. Warehouse stock for same product: 500 units. Agent sells 5 units via Agent POS.

*Test steps:*
1. Log in as Test Agent 02 in the Sales Agent Portal.
2. Open Agent POS. Add Tooke Banana Chips (200g), qty 5.
3. Complete sale.

*Expected result:* Agent virtual stock (`tbl_agent_stock_balance`) reduced by 5 units: now 35. Warehouse stock (`tbl_stock_balance`) remains 500 units — unchanged. Dual-track integrity maintained (BR-001). | **P1**

---

**TC-POS-008** | POS | POS total transaction time ≤ 90 seconds (DC-001 cashier test)

*Preconditions:* POS session open. Test cashier "Prossy" (new user, not trained on the system).

*Test steps:*
1. Start timer.
2. Prossy searches for "Tooke Maize Flour 1kg" by name.
3. Adds qty 2.
4. Selects cash payment, enters amount, completes sale.
5. Receipt printed.
6. Stop timer.

*Expected result:* Total elapsed time from search to receipt print ≤ 90 seconds. (DC-001 compliance test.) | **P2**

---
