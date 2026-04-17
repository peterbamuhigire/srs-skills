## Inventory & Warehouse Management — TC-INV

---

**TC-INV-001** | Inventory | Dual-track inventory: warehouse report excludes agent stock

*Preconditions:* Warehouse stock `tbl_stock_balance`: Tooke Flour 1kg = 1,000 units. Agent "Test Agent 01" `tbl_agent_stock_balance`: Tooke Flour 1kg = 200 units.

*Test steps:*
1. Navigate to Reports → Warehouse Stock Report.
2. Generate for all products.

*Expected result:* Warehouse Stock Report shows Tooke Flour 1kg = 1,000 units. The report does NOT show 1,200 units. Agent-held stock is absent from this report (BR-001). | **P1**

---

**TC-INV-002** | Inventory | Consolidated stock report includes both ledgers, clearly labelled

*Preconditions:* Same as TC-INV-001.

*Test steps:*
1. Navigate to Reports → Consolidated Stock Report.
2. Generate.

*Expected result:* Report shows: Warehouse Stock: 1,000 units, Agent Stock: 200 units, Total: 1,200 units — all three values labelled distinctly. No row merges the two figures without labelling. | **P1**

---

**TC-INV-003** | Inventory | FEFO: earliest expiry batch allocated for warehouse transfer

*Preconditions:* Tooke Banana Chips (200g): Batch X (expiry 2026-08-01, qty 100), Batch Y (expiry 2026-05-15, qty 50). Transfer request: qty 30 to Distribution Centre.

*Test steps:*
1. Initiate stock transfer: Tooke Banana Chips (200g), qty 30.
2. Confirm transfer.

*Expected result:* System allocates 30 units from Batch Y (earliest expiry 2026-05-15). Batch X untouched. If qty requested exceeds Batch Y, system takes remaining from Batch X in expiry order. | **P1**

---

**TC-INV-004** | Inventory | Expiry alert: product approaching expiry within 30-day threshold

*Preconditions:* Tooke Maize Flour (500g), Batch Z: qty 80, expiry date = today + 28 days. Expiry alert threshold configured at 30 days.

*Test steps:*
1. Log in as Warehouse Manager.
2. Navigate to Inventory → Expiry Alerts.

*Expected result:* Batch Z listed in the 30-day expiry alert list with product name, batch number, expiry date, and qty. Alert notification sent to Warehouse Manager. | **P2**

---

**TC-INV-005** | Inventory | Physical stock count: variance detected and posted on approval

*Preconditions:* Warehouse system shows Tooke Maize Flour (1kg): 500 units. Physical count reveals 485 units.

*Test steps:*
1. Navigate to Inventory → Physical Stock Count → New Count.
2. Freeze stock for Tooke Maize Flour (1kg).
3. Enter physical count: 485.
4. Submit count.
5. Finance Manager approves variance.

*Expected result:* System computes variance: -15 units. On Finance Manager approval, stock adjustment posted: system balance updated to 485 units. GL auto-post: DR Stock Variance Expense / CR Inventory. Adjustment logged in audit trail with approver identity. | **P2**

---

**TC-INV-006** | Inventory | Stock transfer in-transit status

*Preconditions:* Warehouse stock: 200 units Tooke Flour 1kg. Transfer initiated to Distribution Centre.

*Test steps:*
1. Create stock transfer: qty 50, destination: Distribution Centre.
2. Confirm transfer dispatch.
3. Check stock balance before confirmation at destination.

*Expected result:* 50 units show status "In Transit" — neither available at warehouse nor at distribution centre until confirmed received. Warehouse balance shows 150 units available. On GRN at Distribution Centre, status changes to available. | **P2**

---

**TC-INV-007** | Inventory | Barcode scan for stock receipt — Warehouse App (Android)

*Preconditions:* Warehouse App installed on Android device. Purchase order PO-TEST-001 expected to deliver Tooke Flour 1kg qty 500.

*Test steps:*
1. Open Warehouse App on Android device.
2. Navigate to Stock Receipt → Receive against PO-TEST-001.
3. Scan barcode of incoming carton.
4. Enter quantity received: 500.
5. Confirm receipt.

*Expected result:* GRN created against PO-TEST-001. Stock balance increased by 500 units. Batch number assigned. Server updated via API. GRN visible in web ERP. | **P2**

---

## Agent Distribution Management — TC-AGT

---

**TC-AGT-001** | Agent | FIFO remittance allocation oracle — exact values

*Preconditions:* Agent "Test Agent 03" has outstanding invoices:
- INV-001: UGX 150,000 (oldest)
- INV-002: UGX 200,000
- INV-003: UGX 80,000

Agent submits remittance of UGX 300,000.

*Test steps:*
1. Navigate to Agents → Remittances → Record Remittance.
2. Select Test Agent 03.
3. Enter remittance amount: UGX 300,000.
4. Save (pending verification).
5. Supervisor verifies remittance (different user — BR-003).
6. Check invoice allocation results.

*Expected result:*
- INV-001: fully cleared (UGX 150,000 applied). Outstanding balance = UGX 0.
- INV-002: partially cleared. UGX 150,000 applied. Outstanding balance = UGX 50,000.
- INV-003: unchanged. Outstanding balance = UGX 80,000.
- Agent cash balance reduced by UGX 300,000.
- `sp_apply_remittance_to_invoices` executed correctly (BR-002).
- Commission accrual: commission calculated on the value of INV-001 (fully cleared) and the cleared portion of INV-002 only (BR-015). | **P1**

---

**TC-AGT-002** | Agent | Segregation of duties: creator cannot verify remittance

*Preconditions:* "Sales Officer A" records a remittance for Test Agent 03.

*Test steps:*
1. "Sales Officer A" creates a remittance record.
2. "Sales Officer A" attempts to verify the same remittance via API (direct API call, bypassing UI).

*Expected result:* API returns HTTP 403 Forbidden. Remittance remains in "Pending Verification" status. Audit trail records the failed verification attempt with Sales Officer A's identity and IP address. (BR-003 enforced at API layer, not just UI.) | **P1**

---

**TC-AGT-003** | Agent | Agent stock float limit blocks issuance

*Preconditions:* Agent "Test Agent 04" float limit: UGX 500,000. Current agent stock value: UGX 420,000. Requested stock issuance value: UGX 100,000 (would result in UGX 520,000 — exceeds limit).

*Test steps:*
1. Navigate to Agents → Stock Issuance.
2. Select Test Agent 04.
3. Add issuance items totalling UGX 100,000.
4. Attempt to confirm issuance.

*Expected result:* System blocks issuance. Error message: "Agent float limit exceeded. Current stock value: UGX 420,000. Issuance value: UGX 100,000. Float limit: UGX 500,000. Remaining capacity: UGX 80,000." Issuance not processed. (BR-006.) | **P1**

---

**TC-AGT-004** | Agent | Agent cash balance real-time update

*Preconditions:* Agent "Test Agent 05" current cash balance: UGX 250,000. A new invoice is posted against this agent: UGX 30,000.

*Test steps:*
1. Post a new sale invoice for Test Agent 05, amount UGX 30,000.
2. Immediately check agent cash balance on the Agent Cash Balance report.

*Expected result:* Agent cash balance updates to UGX 280,000 within 2 seconds of invoice posting. No manual refresh required. | **P1**

---

**TC-AGT-005** | Agent | Commission accrues only on verified remittance (BR-015)

*Preconditions:* Agent "Test Agent 06" submits remittance UGX 50,000 covering INV-001 (UGX 50,000). Commission rate: 5%.

*Test steps:*
1. Record remittance (unverified).
2. Check commission accrual — should be UGX 0.
3. Supervisor verifies remittance.
4. Check commission accrual.

*Expected result:* Before verification: commission = UGX 0. After verification: commission = UGX 50,000 × 5% = UGX 2,500. Commission appears in agent's commission statement. | **P1**

---

**TC-AGT-006** | Agent | Agent performance report: territory ranking

*Preconditions:* ≥ 5 test agents with varied sales volumes in 3 territories.

*Test steps:*
1. Navigate to Reports → Agent Performance → Territory Ranking.
2. Select current month.

*Expected result:* Report lists territories ranked by total verified sales (descending). Within each territory, agents are ranked by verified sales. Report generated within 10 seconds. | **P3**

---

**TC-AGT-007** | Agent | Sales Agent App: offline remittance submission syncs correctly

*Preconditions:* Sales Agent App on Android device, Airplane Mode on. Agent "Test Agent 07" submits remittance offline: UGX 75,000.

*Test steps:*
1. Submit remittance offline in the Sales Agent App.
2. Restore connectivity.
3. Check server for remittance record.

*Expected result:* Remittance appears in server pending verification queue within 60 seconds of reconnect. Amount: UGX 75,000. Agent identity correct. No duplicate records. | **P2**

---
