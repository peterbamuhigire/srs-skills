# Inventory Officer Guide

**Role:** Inventory Officer

**Accessible modules:** Inventory, GRN, Stock Counts, Stock Transfers

---

## Adding a New Item to the Catalogue

1. In the sidebar, click **Inventory**, then click **Item Catalogue**.
2. Click **New Item**.
3. Enter the item name in the **Item Name** field.
4. Enter the item code in the **Item Code** field, or click **Auto-Generate** to let the system assign one.
5. Select the **Category** from the dropdown (for example, Raw Materials, Finished Goods, Consumables).
6. Select the **Unit of Measure** (for example, Each, Kg, Litre).
7. Enter the **Reorder Level** — the stock quantity at which a reorder alert is triggered.
8. Enter the **Default Purchase Price** and **Default Selling Price** if applicable.
9. If the item has a barcode, enter it in the **Barcode** field.
10. Click **Save Item**.

---

## Receiving a Goods Receipt Note (GRN) Against a Purchase Order

1. In the sidebar, click **Inventory**, then click **GRN**.
2. Click **New GRN**.
3. In the **Source** field, select **Against Purchase Order**.
4. Select the relevant **Purchase Order** from the dropdown (type the LPO number to search).
5. The system pre-fills the item lines from the purchase order.
6. For each line, enter the **Quantity Received** — adjust downward if the full order quantity was not delivered.
7. Confirm the **Warehouse / Store** where the stock will be held.
8. Enter the **Delivery Note Number** from the supplier in the **Reference** field.
9. Attach the supplier delivery note by clicking **Attach File**.
10. Click **Post GRN**.
11. Click **Confirm** in the dialog. Stock quantities update immediately.

---

## Recording a Standalone GRN (No PO)

1. In the sidebar, click **Inventory**, then click **GRN**.
2. Click **New GRN**.
3. In the **Source** field, select **Standalone (No PO)**.
4. Select the **Supplier** from the dropdown.
5. Enter the **GRN Date** using the date picker.
6. Click **Add Line** in the items table.
7. Select the **Item** from the dropdown and enter the **Quantity Received** and **Unit Cost**.
8. Repeat step 7 for each item received.
9. Select the **Warehouse / Store**.
10. Enter the supplier delivery note number in the **Reference** field.
11. Click **Post GRN**, then click **Confirm**.

---

## Posting a Stock Adjustment

Use a stock adjustment to correct quantities — for example, to record breakage, spoilage, or a counting correction.

### Positive Adjustment (Adding Stock)

1. In the sidebar, click **Inventory**, then click **Stock Adjustments**.
2. Click **New Adjustment**.
3. Set the **Adjustment Date**.
4. Select the **Warehouse**.
5. Click **Add Line**, then select the item.
6. In the **Adjustment Type** column, select **Positive**.
7. Enter the quantity to add in the **Quantity** column.
8. Enter a reason in the **Reason** field (for example, "Supplier short-delivery correction").
9. Click **Post Adjustment**, then click **Confirm**.

### Negative Adjustment (Removing Stock)

Follow the same steps above, but in step 6 select **Negative** in the **Adjustment Type** column. Enter the quantity to remove. The system will warn if the adjustment would result in negative stock.

---

## Initiating a Stock Transfer Between Branches

1. In the sidebar, click **Inventory**, then click **Stock Transfers**.
2. Click **New Transfer**.
3. Select the **From Warehouse** and the **To Warehouse** from their respective dropdowns.
4. Set the **Transfer Date**.
5. Click **Add Line** and select the item to transfer.
6. Enter the **Quantity to Transfer**.
7. Repeat steps 5–6 for all items in the transfer.
8. Click **Submit Transfer**. The status changes to **In Transit**. Stock is deducted from the source warehouse immediately.
9. When the receiving warehouse confirms receipt, they open the transfer and click **Receive Transfer**, then **Confirm**. Stock is added to the destination warehouse at that point.

---

## Creating a Physical Stock Count Session

1. In the sidebar, click **Inventory**, then click **Stock Counts**.
2. Click **New Stock Count**.
3. Enter a name for the count session in the **Count Name** field (for example, "April 2026 Full Count").
4. Select the **Warehouse** to be counted.
5. Choose the **Scope**: **Full Count** (all items) or **Partial Count** (selected categories or items).
6. If partial, select the categories or items to include.
7. Click **Generate Count Sheet**. The system creates a count sheet with current system quantities hidden (to avoid bias).
8. Print the count sheet by clicking **Print Count Sheet**, or distribute it digitally to counting staff.
9. The session status changes to **In Progress**.

---

## Entering Stock Count Results

1. Open the active stock count session from **Inventory > Stock Counts**.
2. Click **Enter Results**.
3. For each row in the count sheet, enter the physically counted quantity in the **Counted Qty** column.
4. The **Variance** column (Counted Qty minus System Qty) updates automatically.
5. Add a note in the **Notes** column for any line with a significant variance.
6. Click **Save Progress** frequently to avoid losing data.
7. When all lines are complete, click **Submit Count Results**.

---

## Posting the Stock Count Variance

1. After count results are submitted, open the count session.
2. Review the variance report. Lines with variances are highlighted.
3. Click **Post Variance Adjustments**.
4. A summary dialog shows total positive and negative adjustments about to be posted.
5. Click **Confirm Post**. The system posts stock adjustment entries for each variance line, bringing system quantities in line with counted quantities.
6. The session status changes to **Closed**.

---

## Viewing the Stock Ledger for an Item

1. In the sidebar, click **Inventory**, then click **Stock Ledger**.
2. Select the **Item** from the dropdown (type to search).
3. Select the **Warehouse**, or choose **All Warehouses**.
4. Set the **From Date** and **To Date**.
5. Click **Generate**.
6. The ledger table shows every transaction affecting that item in the period: GRNs, sales, adjustments, and transfers. Each row shows the movement quantity, running balance, and the source document reference.
7. Click **Export to Excel** to download the ledger.
