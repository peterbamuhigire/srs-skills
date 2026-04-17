# Sales Transactions

## 3.1 Item Selection and Basket

**FR-POS-013** — When a cashier opens a new sale, the system shall create a transaction record linked to the active terminal session, the cashier user ID, and the current UTC timestamp; each transaction shall receive a unique sale ID in the format `SALE-YYYY-NNNN`.

**FR-POS-014** — The system shall allow item selection via: (a) barcode scan (USB scanner, Bluetooth scanner, or device camera), (b) item name search with autocomplete returning results within 300 ms, and (c) category tile grid browsable on the touch interface.

**FR-POS-015** — When a barcode is scanned, the system shall resolve the barcode against the item catalogue using the GS1 EAN-13/UPC-A mapping and add the matched item at the quantity 1 to the active basket; if the barcode is not found, the system shall display a "Not found" message and allow manual item selection.

**FR-POS-016** — The system shall display a running basket showing: item name, quantity, unit price, VAT amount per line, line total, and cumulative basket total; the basket shall refresh within 200 ms of any item addition or removal.

**FR-POS-017** — The system shall apply the applicable price list for the transaction's branch and date; if no price list is active for the current date, the system shall fall back to the item's default selling price.

**FR-POS-018** — The system shall support item-level discounts: when a cashier applies a percentage or fixed-amount discount to a basket line, the system shall validate that the discount does not exceed the cashier's configured discount authorisation limit and shall record the discount reason.

**FR-POS-019** — The system shall support transaction-level discounts: when a supervisor overrides the total transaction price, the system shall require supervisor authentication, record the original total, discounted total, and the supervisor's identity.

## 3.2 Customer Credit Sales

**FR-POS-020** — When a cashier selects a registered customer on a transaction, the system shall display the customer's outstanding balance and credit limit; if the transaction total would cause the customer's outstanding balance to exceed their credit limit, the system shall warn the cashier and require supervisor override to proceed.

**FR-POS-021** — When a credit sale is confirmed, the system shall post the transaction to the customer's Accounts Receivable balance in real time and generate an invoice document in the Sales module.

## 3.3 Returns and Voids

**FR-POS-022** — When a cashier initiates a sale return, the system shall require the original sale ID; the system shall reverse the stock deduction, credit the customer's payment method, and post a reversal entry to the GL.

**FR-POS-023** — When a cashier voids an open basket (not yet completed), the system shall discard all basket items without posting any stock or GL entries, log the void with the cashier identity and timestamp, and require a void reason if the basket contained items worth more than the configurable void threshold.

## 3.4 Receipt and Printing

**FR-POS-024** — When a sale is confirmed, the system shall print a thermal receipt via the terminal's configured ESC/POS printer; the receipt shall include: tenant logo, branch name, terminal ID, cashier name, date and time, itemised lines (item name, qty, unit price, line total), VAT subtotal, discount, grand total, and payment method.

**FR-POS-025** — When EFRIS integration is active, the system shall transmit the confirmed sale to URA EFRIS and print the EFRIS-issued fiscal receipt number and QR code on the thermal receipt; if the EFRIS API is unreachable, the system shall queue the submission per FR-POS-065 `[CONTEXT-GAP: GAP-001 — EFRIS API integration specification]`.

**FR-POS-026** — The system shall support re-printing the last receipt on cashier request without re-posting any transaction data.

## 3.5 Real-Time Inventory and GL Posting

**FR-POS-027** — When a sale is confirmed, the system shall deduct the sold quantities from the on-hand stock of the relevant items at the terminal's branch within the same database transaction as the sale record; if a stock deduction would result in negative inventory for an item configured as "no negative stock", the system shall block the sale and notify the cashier.

**FR-POS-028** — Cash session GL posting shall occur at session close, not per transaction, to minimise write amplification; the GL entry shall summarise all transactions in the session by payment method: Debit Cash/MoMo/Card accounts, Credit Sales Revenue account.

**FR-POS-029** — When a VAT-registered tenant confirms a sale, the system shall compute VAT per line as: $VAT = ItemPrice \times VATRate$ and post the VAT amount to the Output VAT liability account during session GL posting.
