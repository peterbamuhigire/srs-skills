---
title: "Inventory and Stock Management"
---

# Inventory and Stock Management

This section covers how to manage your products and stock in Maduuka.

## Viewing Stock Levels

1. Tap **Stock** at the bottom of the screen (on Android) or click **Inventory** in the left sidebar (on web).
2. Tap **Products**.
3. The product list shows each item with its current stock quantity. Items with low stock are shown in orange. Items with zero stock are shown in red.
4. Tap any product to see its full details: current quantity per branch, reorder level, cost price, and selling prices.

To search for a specific product, use the **Search** bar at the top of the product list.

## Adding a New Product

1. Go to **Stock** → **Products**.
2. Tap the **+** button (top right corner).
3. Fill in the product details:
   - **Product Name** — the name as it will appear on receipts
   - **Category** — select an existing category or type a new one
   - **Barcode / SKU** — scan the product barcode or type the code manually (optional but recommended)
   - **Unit of Measure** — for example, `Piece`, `Kilogram`, `Litre`, `Carton`
   - **Cost Price** — what you paid for it
   - **Selling Price** — what you charge customers
   - **Reorder Level** — the quantity at which Maduuka alerts you to restock
4. To add a photo, tap **Add Photo** and take a picture or choose from your gallery.
5. Tap **Save Product**.

The product is now available in the POS search.

## Receiving Stock from a Supplier

When goods arrive from a supplier, record them in Maduuka so your stock levels update.

1. Go to **Stock** → **Receive Stock**.
2. Tap **New Delivery**.
3. Select the **Supplier** from the list.
4. If you issued a Purchase Order for these goods, tap **From Purchase Order** and select the order. Maduuka fills in the expected items.
5. For each item received, check the quantity and adjust if the delivery is partial.
6. If the items have a batch number or expiry date, tap the item and enter the **Batch Number** and **Expiry Date**.
7. Tap **Confirm Receipt**.

Stock levels update immediately. A stock movement record is created automatically.

## Doing a Stock Count

A stock count is when you physically count all your stock and compare it to what Maduuka shows. Do a stock count at least once a month.

1. Go to **Stock** → **Stock Count**.
2. Tap **Start New Count**.
3. Select which products or categories to count, or select **All Products**.
4. Tap **Begin Count**. Maduuka freezes the expected quantities so your count is compared against a fixed snapshot.
5. For each product, count the physical items on your shelves.
6. Enter the physical count in the **Counted** column next to each product.
7. Use the camera icon to scan a barcode and jump directly to that product in the list.
8. When you have counted every item, tap **Submit for Review**.
9. Maduuka shows the **variance** — the difference between what the system expected and what you counted.
10. Review the variances. If a variance is large, recount that item before proceeding.
11. Tap **Approve Count** (managers and owners only) to update stock levels to your physical counts.

*Tip: Do a stock count at the end of the day after the POS session is closed so no sales happen during the count.*

## Checking Expiry Dates and Acting on Alerts

Maduuka tracks expiry dates for any product you set up with batch tracking.

1. Go to **Stock** → **Expiry Alerts**.
2. The list shows all batches expiring within your configured alert window (30, 60, or 90 days — set in **Settings** → **Inventory Settings**).
3. Each item shows: product name, batch number, expiry date, and quantity remaining.

To act on an expiring item:
- **Sell first:** Move the expiring batch to the front of the shelf. Maduuka uses FEFO (First Expired, First Out) automatically — it sells the soonest-expiring batch first.
- **Return to supplier:** Go to **Stock** → **Supplier Returns**, select the batch, and create a return.
- **Write off:** Go to **Stock** → **Stock Adjustment**, select the batch, set quantity to 0, and select reason **"Expired"**. Adjustments above the threshold set by the owner require manager approval.

## Transferring Stock to Another Branch

If your business has more than 1 branch, you can move stock between them.

1. Go to **Stock** → **Stock Transfers**.
2. Tap **New Transfer**.
3. Select the **From Branch** (where the stock is leaving).
4. Select the **To Branch** (where the stock is going).
5. Add each product and the quantity to transfer. Tap **Add Item** for each product.
6. Tap **Send Transfer**.

The stock status changes to **"In Transit"** — it is removed from the sending branch but not yet added to the receiving branch.

At the receiving branch:
1. Go to **Stock** → **Stock Transfers**.
2. Find the incoming transfer and tap it.
3. Confirm the quantities received.
4. Tap **Confirm Receipt**.

The stock is added to the receiving branch.
