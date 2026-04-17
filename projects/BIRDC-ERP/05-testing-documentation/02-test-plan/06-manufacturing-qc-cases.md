## Manufacturing & Production — TC-MFG

---

**TC-MFG-001** | Manufacturing | Mass balance oracle: 1,000 kg input balanced to outputs

*Preconditions:* Production order PO-MFG-001 created. Recipe configured. Input: 1,000 kg matooke raw material. Recipe outputs: Tooke Maize Flour = 280 kg, Tooke Banana Chips = 150 kg, Banana Peels (→ biogas) = 50 kg, Banana Fibre = 200 kg, Waste Water (→ bio-slurry) = 320 kg.

*Test steps:*
1. Open PO-MFG-001.
2. Issue 1,000 kg matooke to WIP (material requisition).
3. Enter production completion quantities:
   - Tooke Maize Flour: 280 kg
   - Tooke Banana Chips: 150 kg
   - Banana Peels: 50 kg
   - Banana Fibre: 200 kg
   - Waste Water: 320 kg
4. Attempt to close production order.

*Expected result:* Total output = 280 + 150 + 50 + 200 + 320 = 1,000 kg. Mass balance equation: 1,000 kg input = 1,000 kg output. Variance = 0% (within ±2% tolerance per BR-008). Production order closes successfully. GL posts: DR Finished Goods Inventory / CR WIP. | **P1**

---

**TC-MFG-002** | Manufacturing | Mass balance fails: production order cannot be closed

*Preconditions:* Same as TC-MFG-001 but completion quantities entered as: Flour 280 kg, Chips 150 kg, Peels 50 kg, Fibre 200 kg, Waste Water 280 kg. Total = 960 kg. Variance = 40 kg / 4% — exceeds ±2% tolerance.

*Test steps:*
1. Enter the above quantities.
2. Attempt to close PO-MFG-002.

*Expected result:* System blocks closure. Error: "Mass balance variance 4% exceeds ±2% tolerance. Input: 1,000 kg. Recorded output: 960 kg. Unaccounted: 40 kg. Production Supervisor must review and resolve." Mass balance variance report generated automatically. (BR-008.) | **P1**

---

**TC-MFG-003** | Manufacturing | QC gate: stock transfer blocked until QC status = Approved

*Preconditions:* Production order PO-MFG-003 completed. Finished goods batch FG-BATCH-003 status: "Pending QC."

*Test steps:*
1. Navigate to Inventory → Stock Transfer.
2. Attempt to transfer FG-BATCH-003 from WIP to saleable inventory.

*Expected result:* API returns error: "Stock transfer blocked. Batch FG-BATCH-003 QC status: Pending QC. Transfer permitted only when QC status = Approved. (BR-004.)" | **P1**

---

**TC-MFG-004** | Manufacturing | Material requisition: WIP accounting

*Preconditions:* Raw material inventory: 500 kg matooke. Production order PO-MFG-004 requires 200 kg.

*Test steps:*
1. Issue material requisition for 200 kg matooke against PO-MFG-004.
2. Confirm issue.

*Expected result:* Raw material inventory reduced by 200 kg (now 300 kg). WIP inventory increased by 200 kg (at FIFO cost). GL posts: DR WIP / CR Raw Material Inventory. Material requisition document created with production order reference. | **P2**

---

**TC-MFG-005** | Manufacturing | Factory Floor App: production completion quantities submitted via Android

*Preconditions:* Factory Floor App on Android device. Production order PO-MFG-005 active.

*Test steps:*
1. Open Factory Floor App.
2. Select PO-MFG-005.
3. Enter completion quantities: Flour 280 kg, Chips 150 kg.
4. Submit.

*Expected result:* Completion quantities saved to server. Production order status updated to "Awaiting QC." QC department notified. | **P2**

---

**TC-MFG-006** | Manufacturing | Production order costing: FIFO raw material cost + labour + overhead

*Preconditions:* Production order PO-MFG-006: 500 kg matooke at FIFO cost UGX 600/kg. Direct labour: UGX 150,000. Absorbed overhead (configured rate): UGX 100,000.

*Test steps:*
1. Complete and close PO-MFG-006 with correct mass balance.
2. View production order cost breakdown.

*Expected result:*
- Raw material cost: 500 × UGX 600 = UGX 300,000.
- Direct labour: UGX 150,000.
- Absorbed overhead: UGX 100,000.
- Total production cost: UGX 550,000.
- Cost per unit distributed across output products by weight proportion. | **P2**

---

## Quality Control & Laboratory — TC-QC

---

**TC-QC-001** | QC | Finished goods batch approved: stock transfer unblocked

*Preconditions:* Batch FG-BATCH-010 status: "Pending QC." QC Officer logs in.

*Test steps:*
1. Navigate to QC → Inspection → FG-BATCH-010.
2. Complete all inspection parameters (all pass).
3. Set batch quality status to "Approved."
4. Issue Certificate of Analysis.

*Expected result:* Batch FG-BATCH-010 status = "Approved." CoA generated with: batch number, product name, all test parameters and results, QC Officer name, and date. Stock transfer to saleable inventory now permitted. (BR-004.) | **P1**

---

**TC-QC-002** | QC | Incoming matooke inspection: quality grading A, B, C assigned

*Preconditions:* Cooperative batch delivery GRN-COOP-002 awaiting incoming inspection.

*Test steps:*
1. Navigate to QC → Incoming Inspection → GRN-COOP-002.
2. Run inspection template: moisture content (numeric), visual appearance (pass/fail), foreign matter (pass/fail).
3. Assign grade based on results: Grade A.
4. Submit.

*Expected result:* Inspection record saved with all parameter values. Grade A assigned to GRN-COOP-002. Procurement module shows Grade A for this batch, applying Grade A price per kg. | **P2**

---

**TC-QC-003** | QC | Export CoA: South Korea format with market-specific parameters

*Preconditions:* Batch FG-BATCH-011 approved for export (status: "Approved for Export — South Korea"). South Korea QC parameter template configured.

*Test steps:*
1. Navigate to QC → Certificate of Analysis → FG-BATCH-011.
2. Select market: South Korea.
3. Generate export CoA.

*Expected result:* Export CoA generated with South Korea-specific test parameters (as configured). Header includes BIRDC TIN, batch number, product name, manufacturing date, expiry date, FDN (if applicable). CoA exportable as PDF. (BR-017.) | **P1**

---

**TC-QC-004** | QC | NCR raised on quality failure with root cause tracking

*Preconditions:* Batch FG-BATCH-012 inspection fails moisture content parameter.

*Test steps:*
1. Run inspection for FG-BATCH-012 — moisture content: 18% (limit: 14%).
2. Batch status auto-set to "Rejected."
3. Raise Non-Conformance Report.
4. Enter root cause: "Drying equipment malfunction." Corrective action: "Equipment serviced; re-run drying."

*Expected result:* NCR created with: batch reference, failed parameter (moisture content 18% vs. 14% limit), root cause, corrective action, and responsible officer. NCR assigned to QC Manager for sign-off. Batch cannot be released without NCR closure. | **P2**

---

**TC-QC-005** | QC | Domestic-only batch cannot be dispatched on export order (BR-017)

*Preconditions:* Batch FG-BATCH-013 status: "Approved for Domestic." Export sales order SO-EXP-001 (South Korea) references FG-BATCH-013.

*Test steps:*
1. Attempt to dispatch FG-BATCH-013 against SO-EXP-001.

*Expected result:* System blocks dispatch. Error: "Batch FG-BATCH-013 is approved for Domestic only. An export-grade CoA with South Korea parameters is required before this batch can be dispatched on an export order. (BR-017.)" | **P1**

---
