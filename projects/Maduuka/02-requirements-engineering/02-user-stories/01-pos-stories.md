---
title: "User Stories -- Point of Sale (F-001)"
project: "Maduuka"
module: "POS"
version: "1.0"
date: "2026-04-05"
---

# User Stories: Point of Sale (F-001)

These stories express the POS functional requirements from the perspective of three roles: Cashier (Agnes), Business Owner (Robert), and Branch Manager. Each story maps directly to a functional requirement in the Phase 1 SRS.

---

**US-POS-001:** As a cashier, I want to search for a product by name, SKU, or barcode so that I can add it to the cart without scrolling through the full catalogue.

**Acceptance Criteria:**

- Given the POS search field is active, when the cashier types at least 2 characters, then the system displays matching products within 500 ms of the last keystroke.
- Given a product match is displayed, when the cashier taps the product, then it is added to the active cart immediately.
- Given no product matches the search term, then the system displays a "No products found" message.

**FR Reference:** FR-POS-001

**Priority:** Must Have

---

**US-POS-002:** As a cashier, I want to scan a product barcode using the phone camera so that I can add items to the cart faster than typing.

**Acceptance Criteria:**

- Given the cashier taps the camera icon in the POS search field, when the camera view opens and a barcode is detected, then the matching product is added to the cart within 1 second without a confirmation tap.
- Given the scanned barcode does not match any product, then the system displays a "Product not found" alert.
- Given the barcode scan fails, then the cashier can return to the search field.

**FR Reference:** FR-POS-002

**Priority:** Must Have

---

**US-POS-003:** As a cashier, I want to hold an active cart and start a new transaction so that I can serve another customer while the first waits for a decision.

**Acceptance Criteria:**

- Given the cashier selects "Hold Sale," when the hold is confirmed, then the cart is suspended and assigned a hold reference number.
- Given the cart is held, then the system presents an empty cart for a new transaction.
- Given the held cart has been saved, when the cashier selects the hold reference from the held carts list, then all items, quantities, prices, and discounts are restored exactly.
- Given the app is restarted, then held carts persist and remain recoverable.

**FR Reference:** FR-POS-009, FR-POS-010

**Priority:** Must Have

---

**US-POS-004:** As a cashier, I want to accept a cash payment and see the change amount calculated automatically so that I do not make arithmetic errors under pressure.

**Acceptance Criteria:**

- Given the cashier selects cash as the payment method and enters the amount tendered, when the amount tendered is at least equal to the cart total, then the system displays: Change = Amount Tendered - Cart Total.
- Given the amount tendered is less than the cart total, then the system displays an insufficient funds message and does not allow completion.

**FR Reference:** FR-POS-011

**Priority:** Must Have

---

**US-POS-005:** As a cashier, I want to initiate an MTN Mobile Money push payment so that the customer is prompted on their phone and I do not handle cash.

**Acceptance Criteria:**

- Given the cashier selects MTN MoMo and enters the customer's phone number, when the payment request is sent, then a pending indicator is displayed.
- Given the MTN MoMo API confirms payment, then the system marks the payment as collected and proceeds to receipt generation.
- Given the API returns a failure or timeout, then the system displays the failure reason and allows the cashier to retry or switch payment method.

**FR Reference:** FR-POS-012

**Priority:** Must Have

---

**US-POS-006:** As a cashier, I want to initiate an Airtel Money push payment so that customers who use Airtel can pay without cash.

**Acceptance Criteria:**

- Given the cashier selects Airtel Money and enters the customer's phone number, when the payment request is sent, then the system follows the same flow as MTN MoMo (FR-POS-012).
- Given the Airtel Money API confirms payment, then the system proceeds to receipt generation.
- Given the API returns a failure, then the cashier can retry or switch payment method.

**FR Reference:** FR-POS-013

**Priority:** Must Have

---

**US-POS-007:** As a cashier, I want to split a payment across cash and mobile money so that I can accommodate customers who do not have enough on any single method.

**Acceptance Criteria:**

- Given the cashier selects multiple payment methods, when each component is entered, then the system tracks each component separately against its payment account.
- Given the total of all payment components equals the cart total, then the system allows completion.
- Given the total of all payment components does not equal the cart total, then the system prevents completion and shows the remaining balance.

**FR Reference:** FR-POS-015

**Priority:** Must Have

---

**US-POS-008:** As a cashier, I want to send the customer a receipt via WhatsApp so that the customer has a digital record without needing a printed copy.

**Acceptance Criteria:**

- Given a sale is completed, when the cashier selects "WhatsApp Receipt," then the system generates a PDF receipt image and opens the WhatsApp share sheet pre-populated with the receipt.
- Given the share sheet opens, then the cashier can select the customer's WhatsApp contact to send it.

**FR Reference:** FR-POS-019

**Priority:** Must Have

---

**US-POS-009:** As a cashier, I want to process sales when the internet is down so that customers are never turned away due to connectivity issues.

**Acceptance Criteria:**

- Given the Android app has no internet connectivity, when the cashier processes a sale, then the sale is saved to the local database and the receipt is generated normally.
- Given connectivity is restored, then all pending offline sales are uploaded to the server in chronological order within 30 seconds for queues of up to 500 transactions.
- Given a transaction has synced, then it is marked with a sync timestamp.

**FR Reference:** FR-POS-026, FR-POS-027

**Priority:** Must Have

---

**US-POS-010:** As a cashier, I want to apply a per-item discount or an order-level discount so that I can honour negotiated prices during a sale.

**Acceptance Criteria:**

- Given the cashier selects a cart line and applies a discount, when the discount is entered as a percentage or fixed amount, then the line total updates immediately and the cart grand total reflects the change.
- Given the cashier applies an order-level discount, then the system applies it to the pre-tax subtotal and shows the original total, discount amount, and discounted total.

**FR Reference:** FR-POS-007, FR-POS-008

**Priority:** Must Have

---

**US-POS-011:** As a cashier, I want to open a POS session by entering the opening cash float so that the system tracks cash accurately from the start of my shift.

**Acceptance Criteria:**

- Given the cashier attempts to process a sale, when no session is open, then the system requires entry of an opening cash float before any sale can proceed.
- Given the float is entered and confirmed, then the session opens and the float amount is recorded against the session.

**FR Reference:** FR-POS-021

**Priority:** Must Have

---

**US-POS-012:** As a cashier, I want to close my session and see the reconciliation report so that I know whether my cash drawer matches the system total.

**Acceptance Criteria:**

- Given the cashier selects "Close Session," when the reconciliation screen opens, then it shows: opening float, total cash sales, total cash refunds, expected closing cash, and a field to enter actual counted cash.
- Given the cashier enters the actual cash, then the variance (actual - expected) is displayed and recorded.

**FR Reference:** FR-POS-022

**Priority:** Must Have

---

**US-POS-013:** As a business owner, I want to view the void and refund audit report so that I can investigate any suspicious reversal activity.

**Acceptance Criteria:**

- Given the business owner accesses the voids and refunds report, when the report loads, then it lists all voided transactions and refunds for the selected period with: original receipt number, void or refund date, cashier name, reason code, and amount.
- Given the business owner selects a specific void, then the system shows the voiding manager's name and timestamp.

**FR Reference:** FR-POS-024, FR-REP-007

**Priority:** Must Have

---

**US-POS-014:** As a branch manager, I want to review the receipt gap report after session close so that I can detect missing receipts that may indicate unrecorded sales.

**Acceptance Criteria:**

- Given a POS session is closed, when the system detects a gap in the receipt sequence, then the gap is recorded as a receipt gap event.
- Given the branch manager opens the receipt gap report, then the report lists: session ID, cashier name, expected receipt number, and date of the gap.

**FR Reference:** FR-POS-023, FR-REP-008

**Priority:** Must Have

---

**US-POS-015:** As a business owner, I want to view a cashier performance report so that I can compare each cashier's sales volume and void frequency.

**Acceptance Criteria:**

- Given the business owner requests sales by cashier, when the report loads, then it shows for each cashier: total revenue processed, transaction count, void count, and refund count for the selected period.

**FR Reference:** FR-REP-006

**Priority:** Should Have

---

**US-POS-016:** As a branch manager, I want to perform a session reconciliation review for all cashiers at end of day so that branch cash balances are confirmed before the manager closes.

**Acceptance Criteria:**

- Given the branch manager views closed sessions for the day, when a session reconciliation is selected, then the system shows the full session summary including opening float, cash sales, and variance.
- Given a variance exists, then the system highlights it as unresolved until the manager records a note or corrective action.

**FR Reference:** FR-POS-022

**Priority:** Should Have
