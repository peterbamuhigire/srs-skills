## Procurement & Purchasing — TC-PRO

---

**TC-PRO-001** | Procurement | PPDA approval workflow: micro procurement — Department Head only

*Preconditions:* PPDA micro procurement threshold: ≤ UGX 500,000. Purchase request PR-TEST-001: UGX 200,000 for stationery.

*Test steps:*
1. Create purchase request PR-TEST-001 (Department Head logs in).
2. Department Head approves the request.
3. Attempt to proceed to LPO.

*Expected result:* PR-TEST-001 approved by Department Head. LPO generated. No Finance Manager or Director approval required for micro threshold. (BR-005.) | **P2**

---

**TC-PRO-002** | Procurement | PPDA: large procurement blocked without Director approval

*Preconditions:* Purchase request PR-TEST-002: UGX 15,000,000 (large procurement threshold). Finance Manager and Procurement Officer have approved.

*Test steps:*
1. Attempt to generate LPO / process payment without Director approval.

*Expected result:* System blocks LPO generation. Error: "Large procurement requires Director approval. Current approvals: Finance Manager ✓, Procurement Officer ✓. Missing: Director." (BR-005.) | **P1**

---

**TC-PRO-003** | Procurement | Payment blocked for procurement missing PPDA documents

*Preconditions:* PO-TEST-020 is a small procurement (UGX 2,000,000) with PO and GRN present but the RFQ document is missing from the PPDA checklist.

*Test steps:*
1. Navigate to AP → Vendor Invoices.
2. Register vendor invoice against PO-TEST-020.
3. Attempt to approve payment.

*Expected result:* System blocks payment. Error: "PPDA documentation incomplete. Missing: Request for Quotation (RFQ). Complete PPDA checklist before payment can be authorised." (BR-005.) | **P1**

---

**TC-PRO-004** | Procurement | RFQ: side-by-side supplier comparison

*Preconditions:* RFQ sent to 3 suppliers. All 3 have responded with prices.

*Test steps:*
1. Navigate to Procurement → RFQ → View Responses for test RFQ.

*Expected result:* Side-by-side comparison table shows all 3 suppliers with: unit price, total price, delivery lead time, and evaluation score. Lowest-price supplier highlighted. Procurement Officer can select winning supplier and generate LPO from this screen. | **P3**

---

**TC-PRO-005** | Procurement | Three-way matching validated on GRN vs. LPO

*Preconditions:* LPO-TEST-005: 100 units of packaging, unit price UGX 500. GRN: 95 units received (5% short).

*Test steps:*
1. Record GRN against LPO-TEST-005: qty 95.
2. Register vendor invoice: 100 units, UGX 500.
3. Attempt payment approval.

*Expected result:* System flags quantity variance: "GRN quantity 95 vs. Invoice quantity 100. Variance 5% — within 5% tolerance. Payment may proceed with Finance Manager acknowledgement." Finance Manager acknowledges and approves. (BR-012: qty variance > 2% flagged.) | **P2**

---

## Farmer & Cooperative Management — TC-FAR

---

**TC-FAR-001** | Farmer | 5-stage cooperative procurement: batch cannot advance to Stage 4 without all farmer contributions allocated

*Preconditions:* Batch GRN-COOP-001: 1,000 kg matooke from "Kigezi Cooperative." System shows 3 farmers allocated: Farmer A (400 kg), Farmer B (350 kg), Farmer C (200 kg). Total allocated: 950 kg. Unallocated: 50 kg.

*Test steps:*
1. Navigate to Procurement → Cooperative Procurement → GRN-COOP-001.
2. Attempt to advance to Stage 4 (Stock Receipt).

*Expected result:* System blocks advancement. Error: "Individual farmer contributions incomplete. Allocated: 950 kg of 1,000 kg. Unallocated: 50 kg. All kg must be allocated to a registered farmer before proceeding." (BR-011.) | **P1**

---

**TC-FAR-002** | Farmer | 5-stage procurement: full end-to-end with GL posting

*Preconditions:* "Masaka Cooperative" exists with 5 registered test farmers. Season purchase order SPC-TEST-001 raised.

*Test steps:*
1. Stage 1: Confirm bulk PO for Masaka Cooperative.
2. Stage 2: Record batch goods receipt: 500 kg matooke, Grade A.
3. Stage 3: Break down to individual farmer contributions: Farmer 1 (120 kg, Grade A), Farmer 2 (100 kg, Grade A), Farmer 3 (90 kg, Grade B), Farmer 4 (110 kg, Grade A), Farmer 5 (80 kg, Grade B). Total: 500 kg.
4. Stage 4: Confirm stock receipt into factory inventory (batch number assigned).
5. Stage 5: Confirm GL posting.

*Expected result:* Stage 5 posts: DR Raw Material Inventory / CR Cooperative Payable (Masaka Cooperative). Individual farmer payable amounts visible in Farmer → Payment Due report. Farmer contribution history updated for all 5 farmers. | **P1**

---

**TC-FAR-003** | Farmer | Farmer registration offline (Farmer Delivery App)

*Preconditions:* Farmer Delivery App on Android device, Airplane Mode on. Field collection officer logged in.

*Test steps:*
1. Register new farmer: "James Tumwine," NIN UG2000000001234, mobile 0772123456, cooperative: Kigezi, GPS farm coordinates.
2. Record 1 delivery: 80 kg Grade A matooke.
3. Print farmer receipt via Bluetooth printer.
4. Restore connectivity.

*Expected result:* Farmer "James Tumwine" syncs to server. NIN unique check passes on server. Delivery record of 80 kg appears in Stage 2 receipt queue. Receipt printed correctly offline. | **P2**

---

**TC-FAR-004** | Farmer | Bulk MTN MoMo farmer payment file generation

*Preconditions:* 10 test farmers with outstanding payment balances (after deductions). All have MTN MoMo numbers registered.

*Test steps:*
1. Navigate to AP → Farmer Payments → Generate Bulk Payment.
2. Select period: current season.
3. Apply deductions (loan repayments: UGX 5,000 per farmer where applicable).
4. Generate payment file.

*Expected result:* Bulk MoMo payment file generated in correct format for MTN Uganda MoMo API. File includes: farmer name, MoMo number, net payment amount (gross minus deductions). GL pre-payment entry: DR Cooperative Payable / CR Cash. [CONTEXT-GAP: GAP-002 — MoMo sandbox required for end-to-end test.] | **P1**

---

**TC-FAR-005** | Farmer | Quality grading: Grade A and Grade B price tiers

*Preconditions:* Price configuration: Grade A matooke = UGX 600/kg, Grade B = UGX 450/kg.

*Test steps:*
1. Record cooperative batch with 2 farmers: Farmer A (50 kg Grade A), Farmer B (50 kg Grade B).
2. Calculate payable amounts.

*Expected result:* Farmer A payable: 50 × UGX 600 = UGX 30,000. Farmer B payable: 50 × UGX 450 = UGX 22,500. Net payables shown in payment schedule. | **P2**

---

**TC-FAR-006** | Farmer | Farmer contribution breakdown generates in ≤ 3 seconds for 100+ farmers

*Preconditions:* Test cooperative batch with 120 farmer contributions loaded in staging.

*Test steps:*
1. Open the Stage 3 farmer contribution breakdown screen for the batch.
2. Start timer. Load all 120 records.

*Expected result:* All 120 farmer contribution records displayed within 3 seconds. | **P2**

---
