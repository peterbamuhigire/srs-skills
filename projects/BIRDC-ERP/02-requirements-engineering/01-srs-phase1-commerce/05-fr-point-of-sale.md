## 3.2 Module F-002: Point of Sale (POS)

### 3.2.1 Overview

Module F-002 provides three POS contexts: factory gate / showroom (fixed terminal), distribution centre (fixed terminal), and agent checkout (Sales Agent Android App). All three contexts submit transactions to URA EFRIS, post to GL, and support multiple payment methods. Factory gate and distribution centre POS are web-based (Bootstrap 5 / Tabler UI); agent checkout is the Sales Agent Android App with offline capability.

### 3.2.2 Functional Requirements — Point of Sale

---

**FR-POS-001** — POS Session Opening with Float

When a cashier or agent initiates a new POS session, the system shall require entry of the opening float amount (the cash placed in the till or cash bag at the start of the shift) before any sale transactions are permitted. The system shall record the opening float amount, the session start time, the operator's identity, and the POS terminal/context identifier. A session without a recorded opening float shall block all sale transactions per BR-007 enforcement at the session layer.

*Traceability: BR-007, DC-003, STK-019 (cashier).*

---

**FR-POS-002** — POS Context Routing

When a user opens the POS module, the system shall automatically route the session to the correct POS context based on the user's role and assigned location:

- Users with role `cashier_factory_gate` are routed to the factory gate context, which draws stock from the factory gate warehouse location.
- Users with role `cashier_distribution_centre` are routed to the distribution centre context, which draws stock from the distribution centre location.
- Users with role `agent` accessing the Sales Agent App are routed to the agent checkout context, which draws stock from that agent's virtual store (`tbl_agent_stock_balance`).

*Traceability: BR-001, BR-007, DC-001.*

---

**FR-POS-003** — Product Search by Name

When a cashier types 2 or more characters into the product search field, the system shall return all products whose name contains the entered string (case-insensitive), display results in under 500 milliseconds, and allow the cashier to select a product by tapping or clicking the result row. The search shall be performed against products that have available stock at the current POS location.

*Traceability: DC-001, DC-005 (offline: search operates on local cache).*

---

**FR-POS-004** — Product Search by Product Code

When a cashier enters a product code (exact match) in the search field and presses Enter or taps Search, the system shall retrieve and display the matching product in under 500 milliseconds or display "product not found" if no match exists.

*Traceability: DC-001.*

---

**FR-POS-005** — Product Search by Barcode Scan

When a barcode is scanned via USB scanner (fixed terminal) or device camera (mobile), the system shall decode the barcode, match it to a product in the catalogue, and add the product to the current transaction in under 500 milliseconds. When no product matches the scanned barcode, the system shall display "barcode not found" and allow the cashier to search manually. Camera-based scanning on the Sales Agent App shall use Android ML Kit barcode scanning.

*Traceability: DC-001, DC-005 (offline capable).*

---

**FR-POS-006** — Transaction Line Item Entry

When a product is selected for a POS transaction, the system shall display the product name, current unit price from the applicable price list, an editable quantity field defaulting to 1, and the line total. The system shall update the transaction total in real time as quantities are changed. The cashier shall be able to remove a line item before payment is confirmed.

*Traceability: DC-001.*

---

**FR-POS-007** — Quick Keys (Configurable Shortcut Buttons)

When a cashier is on the POS sale screen, the system shall display a configurable grid of Quick Key buttons, each mapped to a frequently sold product. A user with the `pos_manager` role shall be able to add, remove, or rearrange Quick Key buttons via a settings screen. Tapping a Quick Key shall add the associated product to the transaction with quantity 1, equivalent to performing a product search and selection. Quick Key configurations shall be stored per POS context (factory gate, distribution centre) independently.

*Traceability: DC-001, DC-002.*

---

**FR-POS-008** — Multi-Payment: Cash

When a cashier selects Cash as a payment method for a transaction, the system shall display a numeric input for the cash tendered amount, calculate and display the change due (tendered minus transaction total), and confirm the payment only when the tendered amount is greater than or equal to the transaction total.

*Traceability: DC-001.*

---

**FR-POS-009** — Multi-Payment: MTN Mobile Money

When a cashier selects MTN MoMo as a payment method, the system shall prompt for the customer's MTN MoMo phone number, display the amount to be collected, initiate a payment request via the MTN MoMo Business API, display a pending status while awaiting customer confirmation on the customer's phone, and record the payment as confirmed upon receiving a success callback from the MTN API. `[CONTEXT-GAP: GAP-002]` — MTN MoMo Business API sandbox credentials required.

*Traceability: DC-005.*

---

**FR-POS-010** — Multi-Payment: Airtel Money

When a cashier selects Airtel Money as a payment method, the system shall follow the same workflow as MTN MoMo (FR-POS-009) using the Airtel Money API. `[CONTEXT-GAP: GAP-003]`

*Traceability: DC-005.*

---

**FR-POS-011** — Multi-Payment: Cheque

When a cashier selects Cheque as a payment method, the system shall require entry of: cheque number, bank name, account name, and cheque date. The cheque payment shall be recorded as pending clearance. A user with the `finance` role shall confirm cheque clearance separately, which triggers the GL posting for that payment.

*Traceability: DC-003.*

---

**FR-POS-012** — Multi-Payment: Bank Deposit

When a cashier selects Bank Deposit as a payment method, the system shall require entry of the bank deposit slip reference number, bank name, and deposit date. The bank deposit payment shall be recorded and the GL posting generated immediately (pending bank reconciliation confirmation).

*Traceability: DC-003.*

---

**FR-POS-013** — Split Payment Across Multiple Methods

When a customer pays using a combination of payment methods for a single transaction, the system shall allow the cashier to enter partial amounts against each payment method, validate that the sum of all payment amounts equals the transaction total before confirming the sale, and record each payment method and amount separately against the transaction record.

*Traceability: DC-001.*

---

**FR-POS-014** — EFRIS Submission for POS Receipts

When a POS sale is confirmed (all payments recorded and total balanced), the system shall immediately submit the transaction to URA EFRIS as a POS receipt. When the EFRIS API returns an FDN and QR code, the system shall store both against the transaction record. When the system is offline, the EFRIS submission shall be queued and processed automatically upon connectivity restoration per FR-POS-027. `[CONTEXT-GAP: GAP-001]`

*Traceability: BG-002, URA EFRIS Technical Specification.*

---

**FR-POS-015** — Receipt Generation: 80mm Thermal

When a POS sale is confirmed, the system shall generate a receipt formatted for 80mm thermal printers (ESC/POS protocol) containing: BIRDC name and address, TIN, POS context name, cashier name, transaction date and time, product lines (name, quantity, unit price, line total), payment method breakdown, transaction total, EFRIS FDN, EFRIS QR code, and a system-generated transaction reference number. The receipt shall print automatically or on cashier demand.

*Traceability: DC-001, URA EFRIS Technical Specification.*

---

**FR-POS-016** — Receipt Generation: A4 Invoice

When a cashier or customer requests a full A4 invoice for a POS transaction, the system shall generate a PDF invoice using mPDF with the same content as the thermal receipt plus the customer's name, address, and TIN (if the customer account is registered), formatted per BIRDC's standard invoice template.

*Traceability: DC-001.*

---

**FR-POS-017** — Receipt Generation: SMS and WhatsApp Digital Receipt

When a customer requests a digital receipt via SMS or WhatsApp, the system shall send the transaction total, FDN, product summary, and a link to the full PDF receipt to the phone number provided by the customer via the configured SMS/WhatsApp gateway. `[CONTEXT-GAP: GAP-001]` — confirm SMS/WhatsApp gateway provider for BIRDC.

*Traceability: DC-001.*

---

**FR-POS-018** — GL Auto-Posting for POS Transactions

When a POS sale is confirmed, the system shall automatically post GL entries: DR Cash/Bank (by payment method account) / CR Revenue (by product category), and DR Cost of Goods Sold / CR Inventory (at FIFO/moving average cost of allocated batches). When the POS system is offline, GL posting shall be queued and executed on sync.

*Traceability: BG-001, DC-003, BR-013.*

---

**FR-POS-019** — FEFO Batch Allocation at POS

When a POS sale includes a product with batch/expiry tracking, the system shall automatically allocate the sale from the batch with the earliest expiry date (FEFO, BR-007). The cashier shall not be presented with a batch selection option. If the earliest-expiry batch has insufficient quantity, the system shall automatically continue allocation from the next-earliest batch.

*Traceability: BR-007.*

---

**FR-POS-020** — Stock Availability Check at POS

When a cashier adds a product to a POS transaction, the system shall verify that the required quantity is available at the current POS location (factory gate, distribution centre, or agent virtual store). When the quantity entered exceeds available stock, the system shall display the available quantity and prevent the sale from proceeding with the excess quantity.

*Traceability: BR-001.*

---

**FR-POS-021** — POS End-of-Shift Reconciliation

When a cashier closes a POS session, the system shall display the session summary: opening float, total sales by payment method, expected cash in till (opening float plus cash sales), and a field for the cashier to enter the actual cash counted. The system shall calculate the variance (expected minus actual) and record it against the session. The session closure report shall be sent to the cashier's supervisor and available for manager review.

*Traceability: DC-003, STK-019.*

---

**FR-POS-022** — Variance Reporting to Supervisor

When a POS session is closed with a cash variance, the system shall generate an automatic in-app notification to the direct supervisor of the cashier, displaying the cashier name, session date, expected cash, actual cash, and variance amount. Variances exceeding a configurable threshold (default: UGX 5,000) shall also generate an email alert.

*Traceability: DC-003, DC-002.*

---

**FR-POS-023** — POS Session Transaction Log

When a supervisor or Finance Director requests a POS session report, the system shall display all transactions within the selected session with: transaction time, products sold, quantities, amounts, payment methods, EFRIS FDN, and cashier identity. The report shall be exportable to PDF.

*Traceability: DC-003.*

---

**FR-POS-024** — Agent POS Context — Virtual Store Deduction

When an agent confirms a sale in the agent checkout context (Sales Agent App), the system shall deduct the sold quantities and value from the agent's virtual stock balance in `tbl_agent_stock_balance`, not from any physical warehouse location. This separation enforces BR-001 at every agent POS transaction.

*Traceability: BR-001, BR-007.*

---

**FR-POS-025** — Offline POS — Local Transaction Storage

When the Sales Agent App or factory gate POS terminal has no internet connectivity, the system shall continue to accept and record transactions in the local storage (Android Room / SQLite for mobile; browser local storage / service worker for web terminal), display a clear offline indicator to the cashier, and queue all transactions for sync on connectivity restoration. No transaction data shall be lost during offline operation.

*Traceability: DC-005, BR-009.*

---

**FR-POS-026** — Offline POS — Sync on Reconnect

When internet connectivity is restored, the system shall automatically initiate a sync of all offline transactions to the server via the REST API, assign the sequential transaction reference numbers (maintaining gap-free sequence per BR-009), submit all pending transactions to EFRIS (FR-POS-014), and post all pending GL entries (FR-POS-018). The sync shall complete in the background without interrupting ongoing POS operations. Sync status shall be visible to the cashier.

*Traceability: DC-005, BR-009.*

---

**FR-POS-027** — Offline POS — Offline Product Catalogue Cache

When the Sales Agent App or POS terminal initialises, the system shall download and cache the complete product catalogue, current stock balances for the relevant location, and applicable price list to local storage. This cache shall be refreshed on every successful online session start. Product searches (FR-POS-003 through FR-POS-005) shall operate against the local cache when offline.

*Traceability: DC-005.*

---

**FR-POS-028** — POS Transaction Void

When a cashier or supervisor initiates a void of a POS transaction within the same session, the system shall require a void reason code, require supervisor approval (BR-003 — cashier cannot approve own void), reverse the stock allocation, void the GL entry, and submit the void to EFRIS. Voided transactions shall be visible in the session log marked as VOID and shall retain their original transaction number.

*Traceability: BR-003, BR-009, DC-003.*

---

**FR-POS-029** — POS Refund Workflow

When a customer returns goods previously purchased at POS, a supervisor shall initiate a refund transaction referencing the original POS transaction number. The system shall: verify the original transaction exists and is not already fully refunded; create a refund transaction for the returned items; reverse the stock allocation (return items to the POS location stock); post a GL reversal; and issue a credit receipt to the customer. EFRIS credit note submission shall be triggered per FR-SAL-020.

*Traceability: DC-003, URA EFRIS Technical Specification.*

---

**FR-POS-030** — POS Access Control and Role Enforcement

When a user attempts to access a POS function that requires elevated permissions (void, refund, discount override, session access to a different location), the system shall deny access and display the required role. A user with the required role may authenticate on the same terminal to authorise the specific action (manager PIN override), without handing over the terminal or logging out the cashier.

*Traceability: BR-003, DC-001.*

---

**FR-POS-031** — POS Daily Sales Report

When a Sales Manager or Finance Director requests a POS daily sales report for a selected date and POS context, the system shall generate a report showing: total transactions, total revenue by product category, total revenue by payment method, number of voided transactions and their value, and cashier-level breakdown. The report shall be available in PDF and Excel formats.

*Traceability: STK-006, STK-002.*

---

**FR-POS-032** — Bluetooth Thermal Printing on Sales Agent App

When an agent confirms a sale on the Sales Agent Android App, the system shall send the receipt data to a paired Bluetooth 80mm thermal printer via ESC/POS protocol. The app shall retain the last paired printer across sessions. When no Bluetooth printer is paired or available, the app shall offer to send a digital receipt via SMS/WhatsApp (FR-POS-017) as the fallback.

*Traceability: DC-005, STK-015 (field agent).*
