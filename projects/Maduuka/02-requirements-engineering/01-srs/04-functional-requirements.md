# Section 4: Functional Requirements

All requirements in this section are scoped to Phase 1 (Android + Web). Every requirement applies equally to both the Android application and the web application unless explicitly noted. Requirements follow stimulus-response format per the IEEE 830 "Verifiable" criterion.

---

## 4.1 Point of Sale (F-001)

### 4.1.1 Product Discovery

**FR-POS-001:** When a cashier enters text in the POS search field, the system shall display matching products (by name, SKU, or barcode) within 500 ms of the last keystroke, showing product name, current price, and stock availability.

**FR-POS-002:** When a cashier taps the camera icon in the POS search field on Android, the system shall open a full-screen camera view and automatically add the matching product to the active cart within 1 second of successful barcode detection, without requiring a confirmation tap.

**FR-POS-003:** When a cashier activates the product grid view, the system shall display products grouped by category with configurable photo tiles. Selecting a category filter shall update the grid to show only products in that category within 300 ms.

**FR-POS-004:** When a product's current stock level is zero, the system shall display a visible out-of-stock indicator on the product tile and in the search results. The cashier shall still be able to add the product to the cart, but a warning shall be shown before checkout.

### 4.1.2 Cart Management

**FR-POS-005:** When a cashier adds a product to the cart, the system shall increment the cart line item quantity by 1 and update the cart total in real time. If the product already exists in the cart, the existing line item quantity shall be incremented rather than creating a duplicate line.

**FR-POS-006:** When a cashier modifies the quantity of a cart line item to a value greater than current stock, the system shall display a stock warning but shall not prevent the cashier from proceeding.

**FR-POS-007:** When a cashier applies a per-item discount to a cart line, the system shall accept the discount as either a percentage (0-100%) or a fixed amount (not exceeding the line item total), recalculate the line total immediately, and update the cart grand total.

**FR-POS-008:** When a cashier applies an order-level discount, the system shall apply the discount to the pre-tax subtotal and display the discounted total, original total, and discount amount on the cart summary.

**FR-POS-009:** When a cashier selects "Hold Sale," the system shall suspend the active cart, assign it a hold reference number, and present an empty cart for a new transaction. The held cart shall persist across app restarts.

**FR-POS-010:** When a cashier selects a held cart by its hold reference, the system shall restore all items, quantities, prices, and applied discounts to the active cart exactly as they were at the time of hold.

### 4.1.3 Payment Processing

**FR-POS-011:** When a cashier selects cash payment and enters the amount tendered, the system shall calculate and display the change due as: Change = Amount Tendered - Cart Total, before the cashier confirms the transaction.

**FR-POS-012:** When a cashier initiates an MTN MoMo push payment, the system shall send a payment request to the customer's MTN MoMo wallet via the MTN MoMo Business API and display a pending indicator. When the API confirms payment, the system shall mark the payment as collected and proceed to receipt generation. When the API returns failure or timeout, the system shall display the failure reason and allow the cashier to retry or switch payment method.

**FR-POS-013:** When a cashier initiates an Airtel Money push payment, the system shall follow the equivalent flow to FR-POS-012 using the Airtel Money API.

**FR-POS-014:** When a cashier selects a registered customer for a credit sale, the system shall display the customer's current outstanding balance and credit limit before the cashier confirms. If the sale amount would cause the balance to exceed the credit limit, the system shall block completion unless a manager-level user approves the override with a reason code (BR-002).

**FR-POS-015:** When a cashier processes a multi-payment sale (e.g., partial cash + partial MTN MoMo), the system shall track each payment component separately against its payment account, require the total of all payment components to equal the cart total before allowing completion, and record each component in the sale_payments table.

**FR-POS-016:** When a sale is completed, the system shall decrement stock levels for all physical products in the sale in real time. Service items shall not trigger a stock decrement.

### 4.1.4 Receipt Generation

**FR-POS-017:** When a sale is completed, the system shall generate a receipt containing: business name and logo, branch name, cashier name, receipt number, date and time, itemised list (product name, quantity, unit price, line total), applied discounts, payment method breakdown, total amount, and change given (cash payments).

**FR-POS-018:** When a cashier selects "Print Receipt" after a sale, the system shall send the receipt to the paired Bluetooth thermal printer (Android) or the connected receipt printer via the browser print dialog (Web) within 5 seconds of the print action.

**FR-POS-019:** When a cashier selects "WhatsApp Receipt," the system shall generate a PDF receipt image and open the WhatsApp share sheet pre-populated with the receipt, allowing the cashier to select the customer's WhatsApp contact.

**FR-POS-020:** When a cashier selects "SMS Receipt," the system shall send the receipt summary (total, items count, receipt number) as an SMS to the customer's registered phone number via Africa's Talking.

### 4.1.5 Session Management

**FR-POS-021:** When a cashier opens a POS session, the system shall require entry of an opening cash float amount before any sale can be processed. The opening float amount shall be recorded against the session.

**FR-POS-022:** When a cashier closes a POS session, the system shall generate a session reconciliation report showing: opening float, total cash sales, total cash refunds, expected closing cash (opening float + cash sales - cash refunds), and a field for the cashier to enter the actual counted cash. The variance (actual - expected) shall be displayed and recorded.

**FR-POS-023:** When a POS session is closed, the system shall compare the sequence of issued receipt numbers against the expected sequential range. Any gap in the receipt sequence shall be recorded as a receipt gap event and flagged in the receipt gap report (BR-008).

### 4.1.6 Voids and Refunds

**FR-POS-024:** When a manager-level user voids a completed sale, the system shall reverse the stock decrements for all physical items in the sale, reverse the payment account balances, and record the void in the audit log with: voiding user, original cashier, reason code, timestamp, and original receipt number. A void shall be permitted on any sale within the current business day.

**FR-POS-025:** When a refund is processed for a returned product, the system shall increase stock levels for the returned items, credit the refund amount to the original payment method or to the customer's credit balance (cashier's choice), and record the refund in the audit log.

### 4.1.7 Offline Operation

**FR-POS-026:** When the Android application has no internet connectivity, the system shall allow the cashier to process sales, apply payments, generate receipts, and close the session using cached product data and the local Room database. No sale shall be blocked or lost due to connectivity absence.

**FR-POS-027:** When internet connectivity is restored after offline operation, the system shall upload all pending_sync transactions to the server in chronological order via WorkManager. All uploaded transactions shall be confirmed with a sync timestamp. The sync process shall complete within 30 seconds of connectivity restoration for queues of up to 500 transactions.

### 4.1.8 Weight-Based and Service Items

**FR-POS-028:** When a cashier adds a weight-based product to the cart, the system shall prompt for weight entry in the configured unit (kg or g). The line total shall be calculated as: Line Total = Weight x Unit Price. Weight entry shall accept decimal values to 3 places.

**FR-POS-029:** When a cashier adds a service item to the cart, the system shall process the sale without triggering any stock decrement. Service items shall be identifiable by a "service" flag in the product catalogue.

### 4.1.9 POS Web-Specific

**FR-POS-030:** When the web POS is in full-screen terminal mode, the system shall accept barcode scanner input as keyboard events and add the matching product to the cart without requiring the search field to be focused. The scanner input shall be distinguished from keyboard typing by a configurable inter-character delay threshold.

---

## 4.2 Inventory and Stock Management (F-002)

### 4.2.1 Product Catalogue

**FR-INV-001:** When a user creates a product, the system shall require: product name, category, and at least one selling price. The system shall accept optional fields: SKU, barcode, UOM, cost price, photos (max 5 images, max 2 MB each), reorder level, and active/inactive status.

**FR-INV-002:** When a user assigns multiple price tiers to a product (retail, wholesale, distributor), the system shall automatically apply the correct price tier at POS based on the selected customer's customer group.

**FR-INV-003:** When a user defines multiple selling units for a product (e.g., sell by piece and by box of 12), the system shall calculate stock consumption in the base unit regardless of which selling unit is used at POS. The conversion factor (12 pieces per box) shall be stored on the unit definition.

**FR-INV-004:** When a user uploads a CSV product import file, the system shall validate each row for required fields, report all validation errors before importing, and import only valid rows. The import shall complete within 60 seconds for files up to 5,000 product rows.

### 4.2.2 Stock Levels

**FR-INV-005:** When a sale is completed, the system shall decrement the stock level for each physical product at the branch and warehouse where the POS session is open, creating an immutable stock movement record of type "sale" (BR-004).

**FR-INV-006:** When goods are received against a purchase order, the system shall increment stock levels at the receiving warehouse, create an immutable stock movement record of type "purchase_receipt," and update the purchase order status to "partially received" or "fully received" based on the received quantity.

**FR-INV-007:** When any product's stock level falls to or below its configured reorder level, the system shall generate a push notification to the business owner and branch manager, and display the product in the low-stock alert section of the dashboard.

**FR-INV-008:** When a stock transfer is initiated from a source warehouse to a destination warehouse, the system shall decrement stock at the source warehouse and place the quantity in "in_transit" status. Stock shall be credited to the destination warehouse only when the receiving user confirms receipt.

**FR-INV-009:** When a user initiates a stock adjustment, the system shall require a reason code. If the adjustment value (quantity x cost price) exceeds the business's configured approval threshold, the adjustment shall be held in "pending_approval" status until a manager approves it (BR-005). Adjustments below the threshold shall be applied immediately.

### 4.2.3 Batch and Expiry Tracking

**FR-INV-010:** When goods are received for a product with batch tracking enabled, the system shall require: batch number, manufacturing date, and expiry date. Multiple batches of the same product shall be tracked with independent stock levels.

**FR-INV-011:** When a batch tracking product is sold or dispensed, the system shall automatically select the batch with the nearest expiry date (FEFO) for stock decrement, unless a manager-level user overrides the batch selection (BR-006).

**FR-INV-012:** When any batch's expiry date is within the configured alert threshold (30, 60, or 90 days -- configurable per business), the system shall add the batch to the near-expiry alert list and display it on the dashboard.

### 4.2.4 Stock Valuation and Counting

**FR-INV-013:** When a user requests a stock valuation report, the system shall calculate the total stock value using the configured method (FIFO or weighted average cost) per product and display the total across all products and locations.

**FR-INV-014:** When a user initiates a physical stock count, the system shall freeze stock movements for the selected products during the count window, allow entry of physical quantities per product per location, calculate the variance (physical - system), and create a pending adjustment for manager approval before applying the count result.

**FR-INV-015:** When a supplier return is recorded, the system shall decrement stock at the returning warehouse, create an immutable stock movement record of type "supplier_return," and create a supplier credit note for the returned value.

**FR-INV-016:** When a customer return is received, the system shall increment stock at the receiving warehouse (unless the returned item is damaged -- configurable), create an immutable stock movement record of type "customer_return," and create a credit note for the customer's account.

### 4.2.5 Reporting

**FR-INV-017:** When a user requests a stock movement history report for a product, the system shall display all movement records (sales, receipts, adjustments, transfers, returns) in chronological order with date, type, quantity, balance after movement, and user who created the movement.

**FR-INV-018:** When a user requests a slow-moving items report, the system shall list all products with zero sales in the last 30 days (configurable threshold), sorted by days since last sale.

---

## 4.3 Customer Management (F-003)

### 4.3.1 Customer Profiles

**FR-CUS-001:** When a user creates a customer, the system shall accept: name (required), phone number (required, used for magic-link portal and SMS), email (optional), district and sub-county (Uganda structure; free-form address for other markets), customer group, and credit limit.

**FR-CUS-002:** When a customer is assigned to a customer group (retail, wholesale, VIP, staff), the system shall automatically apply the price tier associated with that group at POS when the customer is selected for a sale.

**FR-CUS-003:** When a user deactivates a customer, the system shall retain all historical transaction records and the customer profile but prevent the customer from being selected in new sales. Deactivation shall be reversible.

### 4.3.2 Credit Management

**FR-CUS-004:** When a credit sale is completed for a customer, the system shall increment the customer's outstanding balance by the sale amount and decrement it by any payment made at the time of sale, in real time.

**FR-CUS-005:** When a user records a payment against a customer's outstanding balance, the system shall decrement the balance, record the payment with method and date, and generate a receipt if requested.

**FR-CUS-006:** When a user requests the debtors ageing report, the system shall list all customers with outstanding balances grouped by ageing bucket: 0-30 days, 31-60 days, 61-90 days, and over 90 days, with total outstanding per customer and per bucket.

**FR-CUS-007:** When a user generates a customer statement, the system shall produce a document showing all transactions (sales, returns, payments) for the customer within the selected date range, with a running balance and a closing balance.

### 4.3.3 Customer Portal

**FR-CUS-008:** When a user sends a portal magic link to a customer, the system shall generate a unique, expiring URL and send it to the customer's registered phone number via WhatsApp or SMS. The link shall expire after 30 days of inactivity.

**FR-CUS-009:** When a customer accesses their portal via the magic link, the system shall display their full purchase history, current outstanding balance, credit limit, and a download button for their PDF statement. No login or password is required. No data modification is permitted.

### 4.3.4 Customer Map

**FR-CUS-010:** When a user opens the customer map view on the web interface, the system shall display all customers who have a recorded district/sub-county location as pins on a Leaflet.js map. Clicking a pin shall show the customer's name, outstanding balance, and a link to their profile.

---

## 4.4 Supplier and Vendor Management (F-004)

### 4.4.1 Supplier Directory

**FR-SUP-001:** When a user creates a supplier, the system shall accept: supplier name (required), contact person, phone, email, physical address, payment terms (days), and bank account details.

**FR-SUP-002:** When a user views a supplier profile, the system shall display the supplier's outstanding balance (total unpaid purchase invoices), full purchase order history, and delivery performance metrics.

### 4.4.2 Purchase Orders

**FR-SUP-003:** When a user creates a purchase order, the system shall allow selection of products with quantities and agreed unit prices, calculate the order total, and generate a PDF purchase order formatted with the business's logo and address.

**FR-SUP-004:** When goods arrive and a user records a goods receipt against a purchase order, the system shall allow entry of received quantities per line item (partial receipt supported), increment stock at the receiving warehouse, and update the purchase order status. If received quantity differs from ordered quantity, the variance shall be flagged.

**FR-SUP-005:** When a goods receipt is confirmed and the supplier invoice amount differs from the purchase order total or received quantity value, the system shall flag the discrepancy for three-way matching review and prevent payment of the invoice until a manager resolves the discrepancy (BR-011).

**FR-SUP-006:** When a user records a supplier payment, the system shall decrement the supplier's outstanding balance, record the payment method and date, and allow partial payment (reducing balance without clearing it).

**FR-SUP-007:** When a user generates a supplier statement, the system shall produce a document listing all purchase orders, goods receipts, invoices, and payments for the supplier within the selected date range, with closing balance.

---

## 4.5 Expenses and Petty Cash (F-005)

### 4.5.1 Expense Recording

**FR-EXP-001:** When a user records an expense, the system shall require: amount, date, expense category, and payment method. Optional fields: description, receipt photo, and tax-deductibility flag.

**FR-EXP-002:** When a user photographs a receipt in the Android app's expense entry screen, the system shall attempt OCR extraction of the total amount and vendor name, pre-populate those fields, and allow the user to correct the extracted values before saving.

**FR-EXP-003:** When an expense amount exceeds the business's configured approval threshold, the system shall set the expense status to "pending_approval" and send a push notification to the designated approver. The expense shall not be posted to the financial accounts until approved.

**FR-EXP-004:** When a manager approves an expense, the system shall post the amount to the payment account specified in the expense record, reducing that account's balance.

### 4.5.2 Petty Cash

**FR-EXP-005:** When a user records a petty cash disbursement, the system shall decrement the petty cash float balance and link the disbursement to an expense category.

**FR-EXP-006:** When a user records a petty cash replenishment, the system shall increment the petty cash float balance and record the source payment account.

**FR-EXP-007:** When a user views petty cash, the system shall display the current float balance, all disbursements since last replenishment, and the expected balance (opening balance + replenishments - disbursements).

### 4.5.3 Recurring Expenses

**FR-EXP-008:** When a user configures a recurring expense (e.g., monthly rent), the system shall automatically create a draft expense entry on the configured recurrence date with the pre-set amount, category, and payment method. The draft shall not be posted until the user reviews and confirms it.

---

## 4.6 Financial Accounts and Cash Flow (F-006)

### 4.6.1 Account Management

**FR-FIN-001:** When a user creates a payment account, the system shall accept: account name (required), account type (cash/mobile money/bank/SACCO), account number or identifier (optional), and opening balance.

**FR-FIN-002:** When any transaction is completed that involves a payment account (sale, expense, purchase payment, transfer, deposit, withdrawal), the system shall update the account balance in real time and create an immutable transaction record in the account's transaction log.

### 4.6.2 Cash Transfers

**FR-FIN-003:** When a user records a cash transfer between accounts, the system shall decrement the source account balance, increment the destination account balance by the same amount, and record both movements as linked transfer entries in each account's transaction log.

### 4.6.3 Bank Reconciliation

**FR-FIN-004:** When a user initiates bank reconciliation for an account, the system shall present the account's transaction log for the selected period and allow the user to mark transactions as "matched" against the bank statement. Unmatched items on either side shall be highlighted.

**FR-FIN-005:** When a user imports a CSV bank statement, the system shall attempt automatic matching of statement transactions against recorded account transactions by amount and date. Matched transactions shall be pre-checked; unmatched transactions shall be listed for manual review.

### 4.6.4 Reporting

**FR-FIN-006:** When a user requests the cash flow summary, the system shall display total inflows (sales receipts, deposits, transfers in) and total outflows (expenses, purchase payments, withdrawals, transfers out) per account and in total for the selected date range.

**FR-FIN-007:** When a user requests the daily summary, the system shall display for each payment account: opening balance, total inflows, total outflows, and closing balance for the selected date.

---

## 4.7 Sales Reporting and Analytics (F-007)

### 4.7.1 Standard Reports

**FR-REP-001:** When a user requests the daily sales report, the system shall display all completed transactions for the selected date, grouped by payment method, with a total per method and an overall total.

**FR-REP-002:** When a user requests the sales summary for a date range, the system shall display: total revenue, total collected payments, total outstanding credit created, total transaction count, average transaction value, and period-over-period comparison (same period last week/month).

**FR-REP-003:** When a user requests sales by product, the system shall list all products sold in the period ranked by revenue, showing: product name, quantity sold, revenue, cost, and gross margin per product.

**FR-REP-004:** When a user requests the top sellers report, the system shall list the top 20 products by revenue and the top 20 by quantity sold for the selected period.

**FR-REP-005:** When a user requests sales by branch, the system shall display total revenue per branch for the selected period, with a percentage share of total revenue per branch.

**FR-REP-006:** When a user requests sales by cashier, the system shall display total revenue processed, transaction count, void count, and refund count per cashier for the selected period.

**FR-REP-007:** When a user requests the voids and refunds report, the system shall list all voided transactions and refunds for the period with: original receipt number, void/refund date, cashier, reason code, and amount.

**FR-REP-008:** When a user requests the receipt gap report, the system shall list all receipt sequence gaps detected in closed POS sessions for the selected period, showing: session ID, cashier, expected receipt number, date of gap.

### 4.7.2 Export and Scheduling

**FR-REP-009:** When a user requests a report export, the system shall generate the report as a CSV or PDF file available for download or sharing within 30 seconds for periods up to 12 months of data.

**FR-REP-010:** When a user configures a scheduled report, the system shall send the configured report as a PDF to the specified email address at the configured frequency (daily or weekly) at the configured time.

---

## 4.8 HR and Payroll (F-008)

### 4.8.1 Staff Profiles

**FR-HR-001:** When a user creates a staff profile, the system shall accept: full name (required), NIN, phone number (required), hire date, department, job title, branch, employment type (permanent/contract/casual), and optional emergency contact and next-of-kin details.

**FR-HR-002:** When a user creates a fixed-term contract, the system shall record the end date and generate a renewal reminder push notification to the HR manager 30 days before the contract expires.

**FR-HR-003:** When a manager invites a new staff member by phone number, the system shall send an SMS invitation containing the app download link and a one-time PIN for first login. The invited staff member shall use the PIN to set their own password.

### 4.8.2 Leave Management

**FR-HR-004:** When an administrator defines a leave type, the system shall accept: leave type name, annual entitlement in days, whether leave is paid or unpaid, and whether it is carry-forward eligible.

**FR-HR-005:** When a staff member submits a leave application through the app, the system shall notify the branch manager or HR manager via push notification within 1 minute of submission.

**FR-HR-006:** When a manager approves or rejects a leave request, the system shall notify the staff member via push notification and record the decision with the manager's name and timestamp. On approval, the system shall deduct the approved days from the staff member's leave balance for the applicable leave type.

**FR-HR-007:** When a user requests the leave balances report, the system shall display for each staff member: leave type, annual entitlement, days taken, days remaining, and days pending approval.

### 4.8.3 Attendance

**FR-HR-008:** When a staff member taps "Clock In" on the app, the system shall record the clock-in timestamp and GPS coordinates (if location permission is granted). A staff member who has already clocked in without clocking out shall receive a duplicate clock-in warning.

**FR-HR-009:** When an administrator records manual daily attendance, the system shall accept: staff member, date, and status (present, absent, late, half-day, on-leave).

### 4.8.4 Payroll

**FR-HR-010:** When a user defines a salary structure for a staff member, the system shall allow configuration of earnings lines (basic salary, housing allowance, transport allowance, overtime, custom earnings) and deduction lines (PAYE, NSSF employee, salary advance recovery, custom deductions).

**FR-HR-011:** When a user initiates a monthly payroll run, the system shall calculate gross pay (sum of all earnings), statutory deductions (PAYE per current Uganda tax bands, NSSF employee at 5%), other deductions (advances, custom), and net pay for each staff member in the payroll. The calculation shall complete within 60 seconds for payrolls of up to 100 staff members.

**FR-HR-012:** When PAYE is calculated, the system shall apply the Uganda Income Tax Act tax bands as configured in the system for the financial year. The system shall support annual tax band updates without requiring a code release.

**FR-HR-013:** When a user approves a payroll run, the system shall lock all payslip amounts for that run (BR-012). No modification of a locked payslip is permitted. Corrections require a reversal in the subsequent payroll period.

**FR-HR-014:** When a payroll run is approved, the system shall generate a PDF payslip for each staff member showing: earnings breakdown, deductions breakdown, gross pay, total deductions, and net pay.

**FR-HR-015:** When payslips are generated, the system shall send each staff member their payslip as a PDF via WhatsApp (primary) or SMS notification with download link (fallback) to their registered phone number.

**FR-HR-016:** When a user requests the NSSF schedule, the system shall generate a schedule listing each employee's name, NIN, gross salary, employee NSSF contribution (5%), employer NSSF contribution (10%), and total contribution, formatted for upload to the NSSF Uganda employer portal.

**FR-HR-017:** When a user requests the PAYE return, the system shall generate a monthly tax return listing each employee, their gross salary, taxable income, PAYE deducted, and cumulative PAYE for the year to date, formatted per URA requirements.

**FR-HR-018:** When a user generates the bank salary payment file, the system shall produce a bulk payment file in the format required by the business's selected bank (Centenary, Stanbic, ABSA, KCB, Equity, Dfcu) listing each employee's bank account number, name, and net pay amount.

### 4.8.5 Loans and Advances

**FR-HR-019:** When a salary advance is recorded for a staff member, the system shall store the advance amount and the agreed repayment schedule (number of months). Each subsequent payroll run shall automatically include the monthly repayment as a deduction line until the advance balance is zero.

### 4.8.6 Disciplinary Records

**FR-HR-020:** When a disciplinary record is created for a staff member (warning, suspension, fine), the system shall record: type, date, description, issuing manager, and any associated fine amount. A fine shall be automatically included as a deduction in the next payroll run.

---

## 4.9 Dashboard and Business Health (F-009)

### 4.9.1 Real-Time KPIs

**FR-DASH-001:** When a user opens the dashboard, the system shall display four KPI cards: Today's Revenue (sum of all completed sales for today), Transaction Count (count of completed sales for today), Outstanding Credit (total of all customer outstanding balances), and Cash Position (sum of balances across all active payment accounts). These values shall reflect the state of the data as of the last sync, with the last sync timestamp displayed.

**FR-DASH-002:** When a user views revenue comparison cards, the system shall display today's revenue vs yesterday's revenue and this week's revenue vs last week's revenue, with an up/down directional indicator and percentage change.

**FR-DASH-003:** When the dashboard is displayed on the web interface with an active internet connection, the system shall auto-refresh all KPI values every 2 minutes without requiring a page reload.

### 4.9.2 Alerts and Actions

**FR-DASH-004:** When any product is below its reorder level, the system shall display the count of low-stock products as a badge on the dashboard and list the affected products with their current quantity and reorder level in an expandable low-stock panel.

**FR-DASH-005:** When there are pending items requiring the current user's action (expense approvals, leave requests, stock adjustment approvals), the system shall display a pending approvals count badge on the dashboard and list each pending item with a direct action link.

**FR-DASH-006:** When a business has multiple branches, the system shall display a branch switcher on the dashboard. Switching branches shall update all KPI cards and recent transactions to reflect the selected branch's data within 2 seconds.

### 4.9.3 Business Health Score

**FR-DASH-007:** When a user views the business health score, the system shall display a RAG (Red/Amber/Green) composite indicator calculated from: gross margin % (this month), expense-to-revenue ratio (this month), stock turnover rate (this month), and credit collection rate (last 30 days). The scoring bands for each metric shall be configurable by the business owner.

---

## 4.10 Settings and Configuration (F-010)

### 4.10.1 Business Profile

**FR-SET-001:** When a user updates the business profile, the system shall store: business name, logo (PNG/JPEG, max 2 MB), physical address, contact phone, email, business registration number, and TIN. These values shall appear on all receipts and invoices immediately after saving.

**FR-SET-002:** When a user customises the receipt template, the system shall allow configuration of: header text (up to 3 lines), footer text (up to 3 lines), whether to show the cashier name, whether to show item SKU codes, and whether to show the business logo.

### 4.10.2 Tax and Currency

**FR-SET-003:** When a user configures tax settings, the system shall allow creation of named tax rates (e.g., "VAT 18%", "Zero Rated", "Exempt") and assignment of default tax rates per product category. The system shall support both tax-inclusive and tax-exclusive pricing modes, configurable per product category.

**FR-SET-004:** When a user sets the functional currency, the system shall store the ISO 4217 currency code and display all monetary values formatted with the appropriate symbol and decimal places. No currency symbol shall be hardcoded in the application.

### 4.10.3 User and Role Management

**FR-SET-005:** When a business owner creates a user, the system shall assign the user to a role (Business Owner, Branch Manager, Cashier, Stock Manager, Accountant, HR Manager) and restrict the user's API access to the permissions associated with that role. The permission mapping for each role is documented in the system RBAC specification.

**FR-SET-006:** When a user's role is changed, the system shall apply the new role's permissions immediately on the user's next API request. Active sessions shall inherit the new permissions without requiring re-login.

### 4.10.4 Subscription and Data

**FR-SET-007:** When a business owner views the subscription screen, the system shall display the current plan name, current usage vs plan limits (users, branches, products, storage), next billing date, and billing history. An upgrade or downgrade action shall redirect to the payment flow.

**FR-SET-008:** When a user requests a full data export, the system shall generate a ZIP archive containing CSV exports of all business data (products, customers, sales, expenses, staff, payroll) and make it available for download within 10 minutes. The system shall send a push notification when the export is ready.

**FR-SET-009:** When a business owner initiates account deletion, the system shall require confirmation, generate a final data export, retain the data for 30 days post-deletion for recovery, and permanently delete all tenant data after 30 days.

### 4.10.5 Notifications and Security

**FR-SET-010:** When a user configures notification preferences, the system shall allow independent toggling of each notification type (low stock, payment received, leave request, expense approval, daily summary, payment reminder) per delivery channel (push notification, SMS, email) per user role.

**FR-SET-011:** When a business owner enables two-factor authentication (2FA), the system shall require TOTP code entry (Google Authenticator compatible) on every login from an unrecognised device. The TOTP secret shall be stored server-side encrypted, never transmitted after initial setup.

**FR-SET-012:** When a user views connected devices, the system shall list all devices that have active sessions or refresh tokens, showing device name, last active date, and IP address. The user shall be able to revoke any device's access, immediately invalidating its refresh token.

---

## FR-AI: AI Business Intelligence Module

---

### FR-AI-001: Sales Forecasting

**FR-AI-001:** When the daily forecast job runs at 06:00 EAT for a tenant with at least 30 days of sales history, the system shall retrieve the daily revenue totals for every calendar day in the preceding 90-day window, group records by day-of-week, compute the per-day-of-week mean and standard deviation, apply a 4-week exponential moving average trend factor (smoothing constant α = 0.3) to the most recent 4 weeks of same-day-of-week totals, and write a forecast record for the current date to `ai_sales_forecast` with tenant ID, forecast date, day-of-week, lower bound (mean − 1 standard deviation), base estimate (mean × trend factor), upper bound (mean + 1 standard deviation), and calculation timestamp. The system shall display the base estimate and range on the Dashboard module's KPI row as "Expected Today: UGX [lower]–[upper]" alongside the live revenue figure. For tenants with fewer than 30 days of history, the system shall display "Insufficient history for forecast" in place of a range. The forecast job shall complete for all active tenants within 10 minutes of the 06:00 EAT trigger.

---

### FR-AI-002: Smart Reorder Advisor

**FR-AI-002:** When the Sunday reorder advisory job runs at 07:00 EAT for a tenant with at least 30 days of stock movement history, the system shall — for each active product with at least one sale in the preceding 30 days — compute the 30-day weighted average daily sales quantity (weight for each day = day index from most recent / sum of all day indices), project days of stock remaining as `current_stock ÷ weighted_avg_daily_sales` (or display "No recent sales" if the product has zero sales in 30 days), and compute recommended order quantity as `(30 × weighted_avg_daily_sales) − current_stock` floored at zero. The system shall write the recommendation to `ai_reorder_recommendations` with tenant ID, product ID, current stock, weighted daily sales, projected days remaining, and recommended order quantity. Products with projected days of stock ≤ 14 shall appear in the Inventory module's **Buy This Week** panel, sorted by days remaining ascending. The Business Owner shall be able to share the **Buy This Week** list via the Android native share sheet as plain text (product name, quantity, unit) with a single tap. The job shall complete within 5 minutes of the Sunday 07:00 EAT trigger for tenants with up to 2,000 active products.

---

### FR-AI-003: Fraud and Anomaly Alerts

**FR-AI-003:** When the nightly anomaly scan runs at 23:30 EAT after each business day, the system shall evaluate all transactions posted during that business day against the following four anomaly detectors, each producing a boolean flag: (a) *Void Ratio Anomaly* — the day's void count for a given cashier exceeds 3× that cashier's 30-day average void count for the same day of week; (b) *Refund Without Sale* — a refund transaction references a receipt number with no corresponding completed sale of the same product within the preceding 7 days; (c) *After-Hours Transaction* — a sale or refund transaction is recorded more than 30 minutes outside the tenant's configured operating hours; (d) *Round-Number Cash Sale* — 3 or more cash sales in a single cashier session are exact multiples of 10,000 UGX with zero change calculated. For each transaction triggering 2 or more flags, the system shall write an anomaly record to `ai_anomaly_flags` with transaction ID, cashier ID, branch ID, triggered flag codes, composite flag count, detection timestamp, and review status defaulting to Unreviewed. The system shall dispatch a push notification to all users holding the Business Owner role: "X suspicious event(s) at [Branch] yesterday — tap to review." The Business Owner shall be able to mark events as Reviewed — No Issue or Escalated. The nightly scan shall complete within 5 minutes for tenants with up to 10,000 daily transactions.

---

### FR-AI-004: Business Health Advisor

**FR-AI-004:** When the Monday 08:00 EAT report generation job runs for a tenant with at least 14 days of sales history, the system shall: (a) compute last week's total revenue, calculate percentage change versus the preceding week and versus the same week 4 weeks prior, and select a directional indicator (↑ if growth > 5%, ↓ if decline > 5%, → otherwise); (b) identify the top 3 products by revenue for last week; (c) identify any product with projected days of stock ≥ 30 days and flag it as an over-stock watch item; (d) identify any product with projected days of stock ≤ 7 days and flag it as a reorder-urgent item; (e) identify the branch with the highest revenue and the branch with the lowest revenue for the week; (f) compose a 4-sentence plain-English Business Health summary using the Claude API (`claude-sonnet-4-6` model) in the form: one sentence on revenue trend with the directional indicator and percentage, one sentence naming the top-selling product and its contribution, one sentence on the most critical inventory watch item, one sentence recommending a single specific action for the coming week. The system shall deliver the summary as a push notification to all users holding the Business Owner role at 08:00 EAT Monday. The full report (all computed data points plus the 4-sentence summary) shall be accessible from the Notifications panel. The generation job shall complete within 60 seconds of trigger. For tenants with fewer than 14 days of history, the system shall skip generation, log an "Insufficient history" record, and send no notification.
