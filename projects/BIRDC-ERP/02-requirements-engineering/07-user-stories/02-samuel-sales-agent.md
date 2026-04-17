# Persona 2: Samuel — Field Sales Agent

**Profile:** Age 31, diploma holder, confident smartphone user. Visits 10–15 retail shops per day in assigned territory. Sells Tooke products from his van (agent stock). Collects cash. Submits daily remittance via the Sales Agent Android app. Checks commission weekly.

**Critical requirement:** Offline POS that syncs without losing any transaction.

---

## US-010: Sell Products from My Agent Stock Offline

**US-010:** As Samuel, I want to process a sale from my agent stock using my Android phone without an internet connection, so that I can keep selling in areas with poor 3G coverage.

**Acceptance criteria:**

- The Sales Agent App operates fully in offline mode: product catalogue, agent stock balances, and pricing data are cached locally on the device and remain functional with no internet connection.
- When Samuel confirms a sale offline, the transaction is stored in the device's local database with a timestamp and a "pending sync" status flag.
- When internet connectivity is restored, all pending transactions are synchronised to the server in chronological order with no duplicates; Samuel receives an in-app notification: "X sales synced."
- Agent stock balance on the device is decremented immediately upon sale confirmation (offline), so Samuel never oversells his available stock.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-010

---

## US-011: Check My Agent Stock Balance

**US-011:** As Samuel, I want to see my current agent stock balance by product, so that I know what I have available to sell before visiting the next customer.

**Acceptance criteria:**

- The Sales Agent App home screen displays Samuel's current agent stock balance: product name, quantity available, and monetary value — sourced from `tbl_agent_stock_balance`, completely separate from warehouse stock (per BR-001).
- Stock balance is updated in real time when connectivity is available and reflects the most recent sync when offline.
- When any product quantity falls below a configurable reorder threshold, the app displays an amber alert: "Low stock: [product name]. Contact warehouse for replenishment."
- The agent stock balance displayed in the app matches the agent stock balance visible to the Store Manager in the web ERP at the time of the last sync.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-001

---

## US-012: Submit a Cash Remittance

**US-012:** As Samuel, I want to submit my daily cash remittance through the Sales Agent App, so that the system records my payment and allocates it to my outstanding invoices correctly.

**Acceptance criteria:**

- The remittance submission screen displays Samuel's total outstanding agent balance (sum of all unpaid invoices), the amount to remit (numeric input), and a list of his oldest outstanding invoices sorted FIFO.
- When Samuel submits a remittance, the system creates a pending remittance record; the app displays: "Remittance submitted. Awaiting supervisor verification. Your balance will update once verified."
- After supervisor verification, the stored procedure `sp_apply_remittance_to_invoices` allocates the remittance to outstanding invoices in FIFO order (oldest first, per BR-002) without any manual invoice selection by Samuel.
- Samuel cannot select which invoices to pay off; the FIFO allocation is enforced and the allocation result is displayed to Samuel after verification as a read-only summary.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-002

---

## US-013: View My Live Agent Cash Balance

**US-013:** As Samuel, I want to see my current cash balance at any time, so that I know exactly how much I owe BIRDC and can plan my remittances to avoid being blocked.

**Acceptance criteria:**

- The Sales Agent App displays Samuel's live agent cash balance prominently on the home screen: Total Sales (invoiced) minus Total Verified Remittances = Outstanding Balance.
- The balance reflects all synced transactions; the timestamp of the last sync is displayed beside the balance.
- When Samuel's outstanding balance exceeds a configurable warning threshold (set by the Sales Manager), the balance is displayed in red with the message: "High balance. Please remit today."
- Samuel cannot modify or dispute his balance from within the app; a "Contact Supervisor" button links to the supervisor's phone number.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-003

---

## US-014: View My Commission Statement

**US-014:** As Samuel, I want to view my commission statement for the current and previous months, so that I can verify my earnings before payday.

**Acceptance criteria:**

- The Sales Agent App provides a "Commission" section that displays: period, total invoiced sales, total verified remittances, commissionable sales (invoices cleared by verified remittances, per BR-015), commission rate (%), and commission amount earned.
- Commission is shown as accrued only on verified remittances — not on sales or unverified remittances (per BR-015).
- Samuel can view the breakdown by individual invoice: which invoices were cleared, which remittance cleared them, and the commission earned per invoice.
- The commission figure in the app matches the commission figure in the payroll module (F-014) for the same period to within UGX 0 rounding tolerance.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-004

---

## US-015: Print a Customer Receipt via Bluetooth Printer

**US-015:** As Samuel, I want to print an 80mm thermal receipt for my customer from my Android phone via Bluetooth, so that the shop owner has documented proof of purchase.

**Acceptance criteria:**

- The Sales Agent App detects paired Bluetooth 80mm printers and displays them in the printer selection list.
- After a sale is confirmed, the app sends the receipt to the paired printer within 3 seconds and displays a "Printing..." indicator.
- If the Bluetooth printer is unavailable, the app offers the option to send the receipt as an SMS or WhatsApp message to the customer's mobile number.
- The printed receipt includes: BIRDC/Tooke header, Samuel's agent ID and name, customer name (if entered), date, items, quantities, prices, total, payment method, and a transaction reference number.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-011

---

## US-016: Request Stock Replenishment from the Warehouse

**US-016:** As Samuel, I want to request additional stock from the warehouse when my agent stock falls below my minimum level, so that I do not run out of products mid-route.

**Acceptance criteria:**

- The Sales Agent App provides a "Request Stock" function where Samuel selects products and quantities to request.
- The request is submitted as a pending stock replenishment order visible to the Store Manager in the web ERP.
- Samuel receives an in-app notification when the Store Manager approves and dispatches the stock, with estimated delivery date and quantities.
- If the requested issuance would cause Samuel's stock balance to exceed his float limit (per BR-006), the system rejects the request and displays: "Request exceeds your stock float limit. Contact your Sales Manager."

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-005

---

## US-017: Return Unsold Stock to the Warehouse

**US-017:** As Samuel, I want to initiate a stock return for products I cannot sell, so that the inventory is correctly moved back to the warehouse and my agent stock balance is adjusted.

**Acceptance criteria:**

- Samuel initiates a stock return from the Sales Agent App by selecting products and quantities to return.
- The return request is approved by the Store Manager in the web ERP before the stock transfer is posted.
- Upon approval, the agent's stock balance (`tbl_agent_stock_balance`) is decremented and the warehouse stock (`tbl_stock_balance`) is incremented, with a transfer document linking the two entries.
- The GL auto-posts the transfer; no manual journal entry is required.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-006

---

## US-018: View My Territory Sales Performance

**US-018:** As Samuel, I want to see my sales performance against my territory target for the current month, so that I know whether I am on track to meet my quota.

**Acceptance criteria:**

- The Sales Agent App displays: this month's total sales, monthly target (configured by Sales Manager), % achieved, and number of active customers in territory.
- Performance data is updated with every sync and shows the last-sync timestamp.
- Samuel can see a list of customers he has not visited in the last 14 days, highlighted as "At risk — no recent visit."
- The territory performance data in the app matches the territory performance report in the web ERP for Samuel's agent ID.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-001-001

---

## US-019: Receive a Push Notification When My Remittance Is Verified

**US-019:** As Samuel, I want to receive a push notification on my phone when my remittance is verified by a supervisor, so that I know my balance has been updated without having to keep checking.

**Acceptance criteria:**

- When a supervisor verifies Samuel's remittance in the web ERP, the system sends a push notification to the Sales Agent App on Samuel's device within 60 seconds of verification.
- The notification message reads: "Remittance of UGX [amount] verified. Outstanding balance: UGX [new balance]. Commission accrued: UGX [amount]."
- If Samuel's device is offline, the notification is delivered the next time the app connects.
- Push notifications are opt-in and can be disabled by Samuel in app settings without affecting system functionality.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-007

---

## US-020: View My Outstanding Invoices

**US-020:** As Samuel, I want to see a list of all my outstanding invoices with amounts and due dates, so that I can prioritise collections and avoid overdue accounts.

**Acceptance criteria:**

- The Sales Agent App displays Samuel's outstanding invoices sorted by invoice date (oldest first), showing: invoice number, customer name, invoice date, invoice amount, and amount outstanding.
- Invoices overdue by more than 30 days are highlighted in red.
- The total outstanding balance matches the agent cash balance figure on the app home screen.
- Samuel cannot edit or delete invoices from this view; invoices are read-only.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-006-001

---

## US-021: Accept a Credit Sale Against an Approved Customer Credit Limit

**US-021:** As Samuel, I want to record a credit sale for a customer who has an approved credit limit, so that their purchase is recorded and their credit utilisation is tracked.

**Acceptance criteria:**

- When Samuel selects a credit customer, the app displays the customer's approved credit limit and current outstanding balance.
- If the new sale would cause the customer's outstanding balance to exceed their approved credit limit, the system blocks the sale and displays: "Credit limit exceeded. Cash sale only, or contact Sales Manager to increase limit."
- Credit sales are synchronised to the AR module (F-006) and appear in the customer's AR aging report.
- Samuel receives a confirmation message after sync: "Credit sale recorded. Customer balance: UGX [amount]."

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-006-002

---

## US-022: Access the Sales Agent App Without Internet on First Launch

**US-022:** As Samuel, I want the Sales Agent App to work immediately after installation even if I am in a no-signal area, so that my first day in the field is not wasted.

**Acceptance criteria:**

- After installation and one successful initial sync (which downloads the product catalogue, price lists, and Samuel's agent data), the app operates fully offline for subsequent sessions.
- The app does not require internet to log in after the first authenticated session; the login token is cached locally for 72 hours.
- If the cached token expires while offline, Samuel receives a clear message: "Login token expired. Please connect to the internet once to refresh your session."
- The app size does not exceed 25 MB to accommodate low-storage Android devices common in the field.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-002-012
