# POS Cashier Guide

**Role:** POS Cashier

**Accessible module:** POS Terminal

---

## Opening a POS Session

You must open a session before processing any sale.

1. In the sidebar, click **POS**, then click **Open Session**.
2. Select the **Till / Register** assigned to you from the dropdown.
3. Count the physical cash in your till.
4. Enter the opening cash amount in the **Opening Float** field.
5. Click **Open Session**. The POS terminal screen loads and you are ready to process sales.

---

## Adding Items to the Cart

### Using Barcode Scan

1. On the POS screen, click inside the **Scan or Search** field at the top.
2. Scan the item barcode using a connected barcode scanner. The item is added to the cart automatically.
3. If the scanned quantity is more than 1, click the quantity field on the cart row and enter the correct number.

### Using Item Search

1. Click the **Scan or Search** field.
2. Type the item name or code. A dropdown list of matching items appears.
3. Click the correct item to add it to the cart.
4. Adjust the quantity in the cart row if needed.

---

## Applying a Discount

1. In the cart, click the line item you want to discount.
2. Click the **Discount** icon (percentage symbol) on that row.
3. Enter the discount percentage (for example, `10` for 10%) or a fixed discount amount.
4. Click **Apply**. The line total and cart total update immediately.

*Discounts above your authorised limit require manager approval. The system will prompt you to enter a manager PIN if the discount exceeds your limit.*

---

## Processing Payment

### Cash

1. With items in the cart, click **Charge** (or **Pay**).
2. Select **Cash** as the payment method.
3. Enter the amount tendered by the customer in the **Cash Tendered** field.
4. The **Change Due** calculates automatically.
5. Click **Confirm Payment**. The receipt is generated.

### MTN MoMo Push

1. Click **Charge**, then select **MTN MoMo**.
2. Enter the customer's MoMo phone number.
3. Click **Send Push Request**. The customer receives a prompt on their phone to approve the payment.
4. Wait for the on-screen confirmation that the payment was approved.
5. Click **Confirm Payment** once approved.

### Airtel Money

1. Click **Charge**, then select **Airtel Money**.
2. Enter the customer's Airtel Money number.
3. Click **Send Push Request** and wait for the approval confirmation.
4. Click **Confirm Payment** once approved.

### Card

1. Click **Charge**, then select **Card**.
2. Enter the card transaction reference number from the card terminal in the **Reference** field.
3. Click **Confirm Payment**.

---

## Issuing a Receipt

After confirming payment, the receipt dialog appears automatically.

- To print a receipt, click **Print Receipt**. The receipt prints to the connected receipt printer.
- To send via WhatsApp, click **Send via WhatsApp**, enter the customer's WhatsApp number, and click **Send**.
- To skip the receipt, click **No Receipt**.

---

## Handling a Return and Refund

1. On the POS screen, click **Returns**.
2. Enter the original receipt number in the **Receipt Number** field, then click **Find**.
3. The original sale items appear. Select the items being returned by ticking the checkbox next to each one.
4. Enter the **Return Quantity** for each selected item.
5. Select the **Return Reason** from the dropdown.
6. Click **Process Return**.
7. Select the **Refund Method**: Cash or MoMo.
8. Click **Confirm Refund**. The system reverses the sale and updates stock.

---

## Closing a POS Session

1. On the POS screen, click **Close Session**.
2. Count the physical cash in your till.
3. Enter the **Closing Cash Count** in the cash count fields, broken down by denomination.
4. The system shows the **Expected Cash** (opening float plus cash sales minus cash refunds) and the **Variance** (difference between expected and counted).
5. Review the session summary: total sales, total refunds, and payment method breakdown.
6. Enter any notes in the **Closing Notes** field, especially if there is a cash variance.
7. Click **Close Session**, then click **Confirm**.
8. The session is closed. A session summary report is available to print or download.
