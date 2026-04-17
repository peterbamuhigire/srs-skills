# Section 4: Robert — Procurement Manager

Robert uses the Procurement module in the main ERP web application. He manages both standard supplier purchases and the 5-stage cooperative farmer procurement workflow.

---

## 4.1 Raising a Purchase Request

1. Log in and click **Procurement** in the main menu.
2. Click **Purchase Requests**, then click **New Request**.
3. Fill in the **Item Description**, **Quantity**, **Unit of Measure**, and **Estimated Unit Price**.
4. Select the **Department** making the request.
5. Click **Save as Draft**.
6. Review the request and click **Submit for Approval**.
7. The system checks the estimated value against PPDA procurement thresholds:
   - Micro procurement: the Department Head receives an approval notification.
   - Small procurement: the Finance Manager receives an approval notification.
   - Large procurement: the Director receives an approval notification.
8. You can track the approval status in the **Purchase Requests** list.

---

## 4.2 Processing a Cooperative Batch Delivery — All 5 Stages

The cooperative procurement workflow has 5 stages. Each stage must be completed in order.

**Stage 1 — Issue a Bulk Purchase Order:**

1. Click **Procurement** then **Cooperative Procurement**.
2. Click **New Cooperative PO**.
3. Select the **Cooperative** from the list.
4. Enter the **Season**, **Expected Quantity (kg)**, and **Price per kg per grade** (Grade A, B, C).
5. Click **Issue PO**. The PO is sent to the cooperative.

**Stage 2 — Record Batch Goods Receipt at the Factory Gate:**

1. When matooke arrives at the factory gate, click **Cooperative Procurement**, then find the relevant PO.
2. Click **Record Batch Receipt**.
3. Enter the **Batch Number**, **Date of Arrival**, and **Total Weight (kg)** on the vehicle.
4. Click **Save Batch Receipt**. The batch status moves to **Stage 2: Received**.

**Stage 3 — Record Individual Farmer Contributions:**

*The batch cannot advance until every kilogramme is assigned to a specific farmer.*

1. Click on the batch in **Cooperative Procurement**.
2. Click **Record Farmer Contributions**.
3. For each farmer in the batch:
   a. Search for the farmer by name or National Identification Number (NIN).
   b. Enter the **Weight (kg)** delivered by that farmer.
   c. Select the **Quality Grade** (A, B, or C).
   d. The system calculates the net payable based on the grade price.
   e. Click **Add Farmer**.
4. Continue until all farmers in the batch are recorded and the total weight matches the batch weight.
5. Click **Complete Farmer Breakdown**. The batch status moves to **Stage 3: Farmers Recorded**.

**Stage 4 — Stock Receipt into Factory Inventory:**

1. Click **Move to Inventory** on the batch record.
2. Confirm the **Warehouse Location** where the matooke will be stored.
3. Click **Confirm Stock Receipt**. Inventory is updated. The batch status moves to **Stage 4: In Stock**.

**Stage 5 — GL Posting:**

1. Click **Post to General Ledger** on the batch record.
2. The system creates the accounting entry: Debit Raw Material Inventory / Credit Cooperative Payable (for each cooperative).
3. Click **Confirm Posting**. The batch status moves to **Stage 5: Posted**.

---

## 4.3 Recording Individual Farmer Contributions

See Stage 3 in Section 4.2 above. If you need to add a contribution to an existing batch after initial recording:

1. Open the batch in **Cooperative Procurement**.
2. Click **Edit Farmer Contributions**.
3. Add the missing farmer entry.
4. Click **Save**.

*Changes to farmer contributions after Stage 5 (GL posting) require Finance Director approval.*

---

## 4.4 Generating a Farmer Payment Schedule

1. Click **Procurement** then **Farmer Payments**.
2. Click **Generate Payment Schedule**.
3. Select the cooperative and the season or batch.
4. The system calculates net payment per farmer: gross amount minus any input loan repayments and cooperative levies.
5. Review the schedule. Check that deductions are correct.
6. Click **Export to Excel** to save the schedule or click **Submit for Approval** to route it to the Finance Director.
7. Once approved, click **Generate Bulk Payment File** to produce the MTN MoMo or Airtel Money batch payment file.
