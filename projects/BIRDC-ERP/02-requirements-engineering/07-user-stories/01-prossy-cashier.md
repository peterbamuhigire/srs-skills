# Persona 1: Prossy — Factory Gate Cashier

**Profile:** Age 24, secondary school education (S4), basic smartphone user. Processes walk-in retail sales at the factory gate and showroom. Handles cash and mobile money payments, prints 80mm thermal receipts, opens and closes POS shifts.

**DC-001 Benchmark:** Prossy must complete a cash sale from product search to printed receipt in under 90 seconds, first attempt, with no training.

---

## US-001: Open a POS Shift

**US-001:** As Prossy, I want to open my daily POS shift by entering my opening cash float, so that the system records my starting cash balance and I can begin processing sales.

**Acceptance criteria:**

- When Prossy selects "Open Shift" and enters an opening float amount, the system creates a new shift session record with her user ID, opening float, and timestamp, and the shift status is set to "Open."
- The system rejects shift opening if another shift for the same POS terminal is already in "Open" status, displaying the message: "Active shift already open on this terminal. Close the existing shift before opening a new one."
- The shift opening screen displays only 2 required fields (opening float amount, confirmation button) and no additional navigation options that could distract Prossy.
- The system records the shift opening event in the audit log with user ID, terminal ID, float amount, and timestamp.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-001

---

## US-002: Search for a Product by Name

**US-002:** As Prossy, I want to search for a product by typing part of its name, so that I can find the correct Tooke product quickly without scrolling through the full catalogue.

**Acceptance criteria:**

- When Prossy types 3 or more characters into the product search field, the system returns all matching active products within 1 second, displaying product name, pack size, and selling price.
- The search matches against both product name and product code fields (partial match, case-insensitive).
- When a product has an associated barcode, Prossy can tap the barcode icon to activate the device camera and scan the barcode; the correct product is added to the cart automatically.
- If no product matches the search term, the screen displays: "No product found. Contact your supervisor to check the product catalogue."

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-002

---

## US-003: Process a Cash Sale with Thermal Receipt

**US-003:** As Prossy, I want to complete a cash sale and print an 80mm thermal receipt, so that the customer receives proof of purchase and my till is updated immediately.

**Acceptance criteria:**

- When Prossy adds products to the cart and selects "Cash" as payment method, the system displays the total amount due and a numeric keypad for cash tendered entry.
- When cash tendered ≥ total amount due, the system displays the change amount, confirms the sale, and sends the print command to the paired 80mm thermal printer within 3 seconds of payment confirmation.
- The printed receipt includes: BIRDC/Tooke header, date and time, POS terminal ID, list of items with quantities and prices, total, cash tendered, change given, and URA Fiscal Document Number (FDN).
- The transaction is submitted to EFRIS within 30 seconds of sale confirmation; if EFRIS is unavailable, the receipt is printed with a pending FDN and the transaction enters the retry queue.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-003

---

## US-004: Accept Mobile Money Payment at POS

**US-004:** As Prossy, I want to accept MTN MoMo or Airtel Money payment at the POS, so that customers who do not carry cash can still buy Tooke products.

**Acceptance criteria:**

- The POS payment screen displays "Cash," "MTN MoMo," "Airtel Money," "Cheque," and "Bank Deposit" as payment method options.
- When Prossy selects "MTN MoMo" or "Airtel Money," the system prompts for the customer's mobile number and displays the amount to be paid; upon payment confirmation from the mobile money API, the sale is completed and a receipt is printed.
- If the mobile money API returns a timeout or failure within 60 seconds, the system displays: "Payment confirmation pending. Do not process as cash. Ask supervisor for assistance."
- A single sale may be split across multiple payment methods (e.g., partial cash + partial mobile money); the system accepts the split and records each payment leg separately in the transaction record.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-004

---

## US-005: Process a POS Sale When Internet Is Unavailable

**US-005:** As Prossy, I want to continue selling when the internet connection drops, so that the factory gate queue does not stop moving.

**Acceptance criteria:**

- When the POS terminal detects no internet connectivity, it displays an "Offline Mode" indicator in the top-right corner of the screen and continues to accept sales from the locally cached product catalogue and pricing data.
- Offline transactions are stored in local storage with a "pending sync" flag and are submitted to the server and to EFRIS automatically when connectivity is restored, with no manual intervention required from Prossy.
- The product catalogue cache is refreshed automatically whenever Prossy opens a shift and connectivity is available, so offline prices are never more than 24 hours out of date.
- After sync completes, the system displays: "X offline transactions synced successfully" with the count of synced records.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-005

---

## US-006: Close a POS Shift and Reconcile Cash

**US-006:** As Prossy, I want to close my shift and record my closing cash count, so that my supervisor can see whether my till matches the expected cash balance.

**Acceptance criteria:**

- When Prossy selects "Close Shift," the system displays the expected closing cash balance (opening float + total cash sales during the shift) and prompts her to enter the actual cash counted.
- The system calculates and displays the variance: actual counted minus expected balance. A variance of UGX 0 displays "Balanced." A non-zero variance displays the variance amount in red.
- The shift closure report is generated and automatically sent to the Sales & Marketing Manager and Finance Director as a PDF summary within 2 minutes of shift closure.
- Once Prossy confirms shift closure, the shift status changes to "Closed" and no further transactions can be posted to that shift.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-006

---

## US-007: Issue a Refund or Void a Sale at POS

**US-007:** As Prossy, I want to void an incorrect sale within my current shift, so that the customer is refunded and my sales record is accurate.

**Acceptance criteria:**

- Prossy can void a sale from the current shift only; void access requires the supervisor PIN entered by a supervisor-role user (Prossy cannot authorise her own void).
- When a void is approved, the system reverses the inventory allocation, creates a void record linked to the original transaction number, and generates a void receipt marked "VOID" in large text.
- The original transaction number is retained in the system and marked VOID; it is not reused (in compliance with BR-009).
- The EFRIS credit note API call is triggered automatically for the voided transaction.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-007

---

## US-008: Generate an A4 Invoice from a POS Sale

**US-008:** As Prossy, I want to generate an A4 formatted tax invoice for a corporate customer who requires it, so that they can claim their purchase for their own accounts.

**Acceptance criteria:**

- When Prossy selects "A4 Invoice" as the receipt format before confirming a sale, the system generates a PDF invoice with: BIRDC/Tooke header, customer name and address (if entered), TIN, FDN, itemised product list, VAT breakdown, and total in UGX.
- The A4 invoice PDF is available for immediate printing to a connected A4 laser printer or download to a USB drive.
- The invoice is assigned the next sequential invoice number in the invoice series (gap-free, per BR-009).
- The same transaction cannot produce both an A4 invoice and an 80mm receipt simultaneously; the format selection is made before sale confirmation.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-008

---

## US-009: View My POS Session Sales Summary

**US-009:** As Prossy, I want to see a running total of my sales by payment method during my shift, so that I always know how much cash I should have in the till.

**Acceptance criteria:**

- A "My Session" summary panel on the POS home screen shows: number of transactions, total sales value, cash collected, mobile money collected, and other payment types — updated in real time after each sale.
- Prossy can tap the summary panel to view the full list of her transactions in the current shift, with the option to reprint any receipt.
- The summary is read-only; Prossy cannot edit any completed transaction from this view.
- The session summary data matches exactly the data used in the shift closure reconciliation screen.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-009
