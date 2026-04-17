# Section 5: David — Store Manager

David uses the Inventory & Warehouse module in the main ERP, and the Warehouse App on Android for scanning and counting on the warehouse floor.

---

## 5.1 Receiving Goods into the Warehouse

1. Log in and click **Warehouse** in the main menu.
2. Click **Receive Goods**.
3. Select the related **Purchase Order** from the list. The expected items and quantities load automatically.
4. For each item:
   a. Enter the **Quantity Received**.
   b. If the item has an expiry date, enter the **Manufacturing Date** and **Expiry Date**.
   c. Enter the **Batch/Lot Number** from the supplier.
5. If the quantity received is different from the PO quantity, the system flags the variance. Enter the reason.
6. Click **Confirm Receipt**. A Goods Receipt Note (GRN) is generated automatically.
7. Stock balances update immediately in the warehouse location you specified.

*When using the Warehouse App on Android: scan the item barcodes and enter quantities on your phone. The app creates the GRN and syncs to the main system.*

---

## 5.2 Issuing Stock to an Agent

1. Click **Warehouse** then **Issue to Agent**.
2. Search for the agent by name or agent code.
3. Add the products and quantities to issue.
4. The system checks the agent's stock float limit. If the new issuance would exceed the agent's limit, the issuance is blocked. You will see a warning: "Float limit exceeded. Current value: UGX X. Limit: UGX Y."
5. If within the limit, click **Confirm Issuance**.
6. Stock moves from the warehouse ledger to the agent's stock ledger. The two are always kept separate.
7. Print the issuance note and attach it to the goods for the agent to sign.

---

## 5.3 Processing a Stock Transfer

To move stock between warehouse locations (e.g., from main warehouse to distribution centre):

1. Click **Warehouse** then **Stock Transfers**.
2. Click **New Transfer**.
3. Select the **From Location** and the **To Location**.
4. Add the products and quantities to transfer.
5. Click **Submit Transfer**. The stock status changes to **In Transit**.
6. At the receiving location, click on the transfer record and click **Confirm Receipt**.
7. Stock updates at both locations. The in-transit status clears.

---

## 5.4 Initiating a Physical Stock Count

A physical stock count freezes stock movements for the affected location while counting is in progress.

1. Click **Warehouse** then **Stock Counts**.
2. Click **New Stock Count**.
3. Select the **Location** to count.
4. Click **Freeze Location**. No stock can be issued from or received into this location until the count is complete.
5. Print the **Count Sheet** (a list of all items expected in the location).
6. Go to the location and count every item. Record the physical count on the count sheet.
7. Return to the system and enter the counted quantities next to each item.
8. Click **Submit Count**.
9. The system shows a variance report: expected quantity vs. counted quantity for each item.
10. Review variances. Enter notes for any discrepancies.
11. Click **Approve Variance** (requires a supervisor) to adjust stock to match the physical count.
12. Click **Unfreeze Location**. Normal stock movements resume.

---

## 5.5 Checking Reorder Alerts

The system sends reorder alerts automatically when stock falls below the reorder level. You can also check manually:

1. Click **Warehouse** then **Reorder Alerts**.
2. The screen lists all items where the current stock quantity is at or below the reorder level.
3. Click on any item to see the current quantity, reorder level, and suggested order quantity.
4. Click **Raise Purchase Request** directly from the alert to start the procurement process.

*Reorder levels are set in the item catalogue. Ask the IT Administrator to update a reorder level if it is set too high or too low.*
