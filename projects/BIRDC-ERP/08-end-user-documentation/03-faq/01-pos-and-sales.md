# Topic 1: POS and Sales

---

**Q1. Can I process a sale when the internet is down?**

Yes. The factory gate POS and the Sales Agent App are both designed to work without an internet connection. When the internet is unavailable, sales are saved on the device. When connectivity returns, the app automatically submits all queued sales to the server and to URA EFRIS. No action is required from you — but you should check the sync indicator turns green after reconnecting to confirm all sales have uploaded.

---

**Q2. What happens if I forget to open a session float before making my first sale?**

The system will not allow a sale until a POS session is opened with an opening float. If you attempt to make a sale without opening a session, the system shows the message "No active session. Please open a session first." Open the session, enter your float amount (even if it is zero), and then proceed with the sale. Your end-of-shift report will show a variance if your closing cash count does not match expectations, so always count and enter the float accurately at the start.

---

**Q3. How do I send a receipt to a customer via WhatsApp?**

After completing a sale, tap or click **Resend Receipt**, then select **WhatsApp**. Enter the customer's phone number (including the country code, for example +256 for Uganda). Tap **Send**. The customer receives a digital receipt via WhatsApp. This works whether you are online or offline — if offline, the WhatsApp message is queued and sent when connectivity returns.

---

**Q4. Can a sales agent sell products directly from the main warehouse, bypassing the agent stock system?**

No. Agent sales always come from the agent's own virtual stock (the agent stock ledger), not from the warehouse stock. When the agent sells a product, the quantity is deducted from their personal stock balance, not from the warehouse. This separation is a core system rule (BR-001) and cannot be bypassed. If an agent needs more stock, the Store Manager must issue it from the warehouse to the agent's stock account first.

---

**Q5. What if I void a sale by mistake?**

A void cannot be undone once confirmed. The voided receipt retains its receipt number and is marked VOID in the system — receipt numbers are never reused. The stock is returned to inventory automatically. If the customer still wants the products, open a new sale. If the void was in error and has already been confirmed, contact the Finance Manager. They can review the voided transaction in the audit log and, if appropriate, process a correction. Voiding a sale creates a full audit record showing who voided it and when.

---

**Q6. What is the Fiscal Document Number (FDN) on a receipt, and why does it matter?**

The Fiscal Document Number is the unique reference number that Uganda Revenue Authority's EFRIS system assigns to every sale. It confirms that the sale has been officially recorded with URA for tax purposes. Every receipt or invoice printed by the BIRDC ERP includes an FDN and a QR code. If URA or an auditor queries a transaction, the FDN is used to look it up. If a receipt shows "FDN: Pending", it means the internet was down when the sale was made. The FDN will appear on the receipt once the sale syncs with EFRIS.

---

**Q7. Can I process a split payment — part cash and part mobile money?**

Yes. At the payment screen, select the first payment method (for example, Cash) and enter the amount the customer is paying in cash. Then tap **Add Payment Method**, select **MTN MoMo** or **Airtel Money**, and enter the remaining amount. The system accepts multiple payment methods on a single sale. The receipt shows each payment method and amount separately.
