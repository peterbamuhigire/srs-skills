# Section 1: Prossy — Factory Gate Cashier

Prossy uses the Point of Sale (POS) screen on the desktop or tablet at the factory gate or showroom. She handles walk-in retail customers buying Tooke products.

---

## 1.1 Opening a POS Shift

Before you can process any sale, you must open a session and record your opening float (the cash already in the till).

1. Log in to the BIRDC ERP with your username and password.
2. Click **Point of Sale** in the main menu.
3. Click **Open New Session**.
4. Count the cash in the till and type the total into the **Opening Float** field.
5. Click **Open Session**.
6. The screen changes to the POS sale screen. You are now ready to sell.

*If you skip the opening float, the end-of-shift report will show a variance. Always count and enter the float before making your first sale.*

---

## 1.2 Processing a Sale — Cash Payment

1. On the POS sale screen, click inside the **Product Search** box.
2. Type the product name (for example, "Tooke Flour"), product code, or scan the barcode with the barcode scanner.
3. The product appears in the list. Click it to add it to the sale.
4. If the customer wants more than 1 unit, change the **Quantity** field to the correct number.
5. To add another product, search again and click it.
6. When you have added all products, click **Payment**.
7. The total appears. Under **Payment Method**, click **Cash**.
8. Type the amount the customer is handing you in the **Amount Received** field.
9. The system calculates the change. Confirm the change shown is correct.
10. Click **Complete Sale**.
11. The receipt prints automatically on the 80mm thermal printer.
12. Hand the receipt and the change to the customer.

*The system submits the sale to URA EFRIS automatically. A Fiscal Document Number (FDN) is printed on the receipt.*

---

## 1.3 Processing a Sale — Mobile Money Payment (MTN MoMo or Airtel Money)

1. Add the products to the sale following steps 1–5 in Section 1.2.
2. Click **Payment**.
3. Under **Payment Method**, click **MTN MoMo** or **Airtel Money** (whichever the customer uses).
4. Type the customer's mobile money number in the **Mobile Number** field.
5. Click **Request Payment**. The customer receives a mobile money prompt on their phone.
6. Ask the customer to enter their mobile money PIN on their phone.
7. Wait for the on-screen message **Payment Confirmed**.
8. Click **Complete Sale**.
9. The receipt prints automatically.

*Do not click Complete Sale before you see Payment Confirmed. If the customer's phone is off or out of network, ask them to pay cash instead.*

---

## 1.4 Printing or Sending a Receipt

The system prints an 80mm thermal receipt automatically at the end of every sale. If the customer wants a copy by WhatsApp or SMS:

1. After the sale is complete, click **Resend Receipt**.
2. Choose **WhatsApp** or **SMS**.
3. Type the customer's phone number.
4. Click **Send**. The customer receives a digital copy.

To print a full A4 invoice instead of a thermal receipt:

1. After the sale is complete, click **Print A4 Invoice**.
2. The invoice opens in the printer dialog. Select your printer and click **Print**.

---

## 1.5 Processing a Refund

*Only process a refund if a supervisor has approved it.*

1. In the POS screen, click **Refund / Return**.
2. Type the original receipt number in the **Receipt Number** field and press Enter.
3. The original sale appears. Select the item(s) the customer is returning.
4. Enter the **Quantity** being returned.
5. Select the **Return Reason** from the drop-down list.
6. Click **Process Refund**.
7. The system reverses the sale, updates stock, and prints a credit receipt.
8. Return the cash or process the mobile money reversal as instructed on screen.

---

## 1.6 Closing a POS Shift

At the end of your shift:

1. Click **Close Session** at the top right of the POS screen.
2. Count all the cash in the till. Enter the total in the **Closing Cash Count** field.
3. Click **Reconcile**. The system compares your count to the expected cash from all sales.
4. If there is a variance, a warning appears. Count again. If you still find a difference, enter a note explaining it in the **Variance Notes** field.
5. Click **Close Session** to confirm.
6. The system prints the End of Shift report. Hand a copy to your supervisor.
7. You are now logged out of the POS session.

*You cannot process any new sales after you click Close Session. If you need to make a sale after closing, open a new session.*
