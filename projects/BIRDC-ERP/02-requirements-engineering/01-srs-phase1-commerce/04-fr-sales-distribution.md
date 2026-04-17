# 3. Specific Requirements

## 3.1 Module F-001: Sales and Distribution

### 3.1.1 Overview

Module F-001 covers the complete order-to-cash cycle for Tooke products sold through BIRDC's commercial channels. It manages invoice lifecycle, EFRIS real-time fiscal submission, GL auto-posting, credit management, pricing, and sales performance tracking for all sales channels including direct sales to institutions and distributors.

### 3.1.2 Functional Requirements — Sales and Distribution

---

**FR-SAL-001** — Invoice Creation

When a Sales Officer or Accounts Assistant initiates a new invoice, the system shall create an invoice record in `draft` status with a unique sequential identifier in the format `INV-YYYY-NNNN` (where YYYY is the calendar year and NNNN is a zero-padded sequential number within the year), pre-populate the invoice date with the current server date, and require the operator to select a customer from the registered customer list before any line items can be added.

*Traceability: BG-001 (financial integrity), BR-009 (sequential numbering).*

---

**FR-SAL-002** — Invoice Line Item Entry

When an operator adds a line item to a draft invoice, the system shall require selection of a product from the stock catalogue, auto-populate the unit price from the price list assigned to the customer (wholesale, retail, export, or institutional), allow the operator to enter the quantity in the product's sales UOM, calculate the line total as quantity multiplied by unit price, and display the cumulative invoice total after each line addition.

*Traceability: BG-001, DC-001 (self-discoverable).*

---

**FR-SAL-003** — Price List Assignment and Override

When a customer is selected on an invoice, the system shall automatically apply the price list assigned to that customer's account. When no price list is assigned to the customer, the system shall default to the retail price list. The system shall permit a user with the `sales_manager` role to override the unit price on any line item; all price overrides shall be logged in the audit trail with the original price, overridden price, and the overriding user's identity.

*Traceability: BG-001, DC-002 (configurable rules), DC-003 (audit trail).*

---

**FR-SAL-004** — Multiple Price Lists

When the Finance Director or Sales Manager configures a price list, the system shall support unlimited named price lists (at minimum: Wholesale, Retail, Export, Institutional), allow each price list to define a price per product in UGX or any configured currency, and allow assignment of a default price list to any customer account. `[CONTEXT-GAP: GAP-001]` — EFRIS requires UGX as the functional currency for domestic invoices; confirm handling of USD/EUR export invoices with URA.

*Traceability: BG-002 (commercial discipline), DC-002.*

---

**FR-SAL-005** — Time-Bound Promotional Pricing

When a promotional price is configured for a product with a start date and end date, the system shall automatically apply the promotional price instead of the standard list price for invoices dated within the promotion period, and revert to the standard price list price on the day after the promotion end date without any manual intervention.

*Traceability: BG-002, DC-002.*

---

**FR-SAL-006** — Volume Discount Rules

When an invoice line item quantity meets or exceeds a configured volume discount threshold for that product, the system shall automatically apply the configured percentage discount to that line item's unit price, display the discount amount as a separate line on the invoice, and log the discount rule applied in the invoice record.

*Traceability: BG-002, DC-002.*

---

**FR-SAL-007** — Credit Limit Enforcement

When an operator attempts to confirm an invoice for a customer with a credit account, the system shall calculate the customer's current outstanding AR balance (sum of all unpaid and partially paid invoices), add the value of the current invoice, and compare the total to the customer's configured credit limit. When the sum exceeds the credit limit, the system shall block invoice confirmation and display a message stating the credit limit, current exposure, and the amount by which the new invoice would exceed the limit.

*Traceability: BG-003 (agent accountability), BR-003.*

---

**FR-SAL-008** — Credit Limit Manager Override

When a Sales Manager with the `credit_override` permission reviews a blocked invoice (per FR-SAL-007), the system shall permit the manager to approve the invoice by entering a mandatory reason code selected from a configurable list, after which the system shall confirm the invoice, log the override in the audit trail with the manager's identity, timestamp, reason code, and credit exposure at time of override.

*Traceability: BG-003, DC-003 (audit readiness).*

---

**FR-SAL-009** — Invoice Confirmation and Status Transition

When an operator confirms a draft invoice (transitions from `draft` to `pending EFRIS`), the system shall validate that: all required fields are populated, at least one line item exists, the customer's credit limit check has passed or been overridden, and sufficient stock is available in the selected warehouse location. When all validations pass, the system shall lock the invoice against further editing and trigger the EFRIS submission process (FR-SAL-011) and GL auto-posting (FR-SAL-013) simultaneously.

*Traceability: BG-001, BR-003, BR-007, BR-009.*

---

**FR-SAL-010** — Invoice Lifecycle State Machine

The system shall enforce the following invoice status transitions and no others:

| From Status | To Status | Trigger |
|---|---|---|
| `draft` | `pending EFRIS` | Operator confirms invoice |
| `pending EFRIS` | `issued` | EFRIS FDN received successfully |
| `pending EFRIS` | `EFRIS failed` | EFRIS submission fails after 3 retries |
| `issued` | `partially paid` | Payment received, balance > 0 |
| `issued` | `paid` | Full payment received |
| `partially paid` | `paid` | Remaining balance paid |
| `issued` | `void` | Void workflow completed (FR-SAL-020) |
| `partially paid` | `void` | Void workflow completed (FR-SAL-020) |

No other status transitions shall be permitted. Attempts to perform an invalid transition shall return an error.

*Traceability: BG-001, DC-003.*

---

**FR-SAL-011** — EFRIS Real-Time Submission on Invoice Confirmation

When an invoice transitions to `pending EFRIS` status, the system shall immediately submit the invoice data to the URA EFRIS system-to-system REST API with all required fiscal fields. When the EFRIS API returns a Fiscal Document Number (FDN) and QR code, the system shall store the FDN and QR code against the invoice record and transition the invoice status to `issued`. When the EFRIS API returns an error or does not respond within 30 seconds, the system shall place the submission in the retry queue (FR-SAL-012) and notify the Finance Manager. `[CONTEXT-GAP: GAP-001]` — EFRIS API sandbox credentials required.

*Traceability: BG-002 (EFRIS compliance), external: URA EFRIS Technical Specification.*

---

**FR-SAL-012** — EFRIS Retry Queue and Failure Alert

When an EFRIS submission fails, the system shall: queue the submission for automatic retry at 5-minute intervals; alert the Finance Manager by in-app notification after the first failure; escalate to email notification after 3 consecutive failures; and mark the invoice with status `EFRIS failed` after 3 consecutive failures. The system shall allow the Finance Manager to manually trigger a retry from the EFRIS failure queue at any time.

*Traceability: BG-001, DC-003.*

---

**FR-SAL-013** — GL Auto-Posting on Invoice Confirmation

When an invoice is confirmed (transitions from `draft` to `pending EFRIS`), the system shall automatically generate the following GL journal entries without any manual action:

1. DR Accounts Receivable (customer's AR control account) / CR Revenue (product revenue account, segmented by product category)
2. DR Cost of Goods Sold / CR Inventory (at the FIFO or moving-average cost of the specific batches allocated per FR-SAL-014)

The system shall post these entries with the invoice number as the source reference, the operator's identity as the posting user, and the server timestamp as the posting date.

*Traceability: BG-002, DC-003, BR-013.*

---

**FR-SAL-014** — COGS Calculation from FIFO/Moving-Average Batch Valuation

When the GL auto-post for a confirmed invoice is generated (FR-SAL-013), the system shall calculate the Cost of Goods Sold for each line item by: selecting the specific inventory batch(es) allocated to this sale per FEFO rules (BR-007), reading the cost per unit for each batch from the inventory valuation method configured for that product (FIFO or moving average), multiplying by the quantity sold, and using this calculated cost as the CR Inventory / DR COGS value in the journal entry. The batch allocation and cost per unit used shall be recorded against the invoice line item for traceability.

*Traceability: BG-002, BR-007, DC-003.*

---

**FR-SAL-015** — FDN and QR Code on Printed Invoice

When a confirmed invoice (status `issued` or later) is printed or exported to PDF, the system shall include the EFRIS Fiscal Document Number (FDN), the EFRIS QR code image, BIRDC's TIN, and the invoice date on the invoice document in the positions required by URA EFRIS guidelines. The system shall prevent printing of invoices in `pending EFRIS` or `EFRIS failed` status without an explicit override by the Finance Manager.

*Traceability: BG-002, URA EFRIS Technical Specification.*

---

**FR-SAL-016** — Sequential Invoice Numbering with Gap Detection

The system shall assign invoice numbers in the format `INV-YYYY-NNNN` using a database sequence that increments atomically. The system shall monitor the invoice number series daily and, when a gap is detected (a number missing between the lowest and highest issued numbers in a series), generate an automatic in-app alert to the Finance Manager and record the gap detection event in the audit trail. Voided invoices shall retain their assigned number permanently, marked with status `void` — invoice numbers shall never be recycled or reused.

*Traceability: BG-002, BR-009, DC-003.*

---

**FR-SAL-017** — Void Invoice Workflow

When an authorised user initiates a void request on an issued or partially paid invoice, the system shall: require selection of a void reason code from a configurable list (minimum codes: data entry error, customer cancellation, duplicate invoice, fraudulent transaction); route the void request to a Sales Manager for approval (BR-003 — creator cannot approve); upon approval, set the invoice status to `void` and retain the invoice record permanently; and trigger automatic GL reversal (FR-SAL-018).

*Traceability: BG-001, BR-003, DC-003.*

---

**FR-SAL-018** — GL Auto-Reversal on Invoice Void

When an invoice void is approved, the system shall automatically post a reversing journal entry that exactly mirrors the original GL posting (FR-SAL-013) with all debits and credits swapped, using the void approval date as the entry date, the void reference (VOID-INV-YYYY-NNNN) as the source reference, and the approver's identity as the posting user. The reversal journal entry shall be linked to the original journal entry by a foreign key for traceability.

*Traceability: BG-001, DC-003, BR-013.*

---

**FR-SAL-019** — Credit Note Creation and Workflow

When a credit note is initiated against a specific invoice, the system shall: require the originating invoice number; auto-populate customer details and the line items from the originating invoice; allow the operator to select the specific lines and quantities being credited; require a credit reason code; route for Sales Manager approval (BR-003); upon approval, submit the credit note to URA EFRIS as a credit note document type and receive an FDN; post the GL reversal for the credited amount; and link the credit note to the originating invoice for AR aging and audit trail purposes.

*Traceability: BG-001, BR-003, DC-003, URA EFRIS Technical Specification.*

---

**FR-SAL-020** — Credit Note EFRIS Submission

When a credit note is approved, the system shall submit the credit note to URA EFRIS as a credit note document type (not an invoice). The system shall store the FDN and QR code returned by EFRIS against the credit note record and include both on the printed credit note document.

*Traceability: BG-002, URA EFRIS Technical Specification.*

---

**FR-SAL-021** — Territory-Based Sales Tracking

When a sales invoice is confirmed, the system shall associate the invoice with the territory of the assigned sales agent or the territory configured for the customer. The system shall maintain cumulative sales totals (quantity and value) by territory, updated in real time as invoices are confirmed and payments are received.

*Traceability: BG-003 (agent accountability), STK-006 (Sales Manager need).*

---

**FR-SAL-022** — Territory Performance Report

When a Sales Manager or Director requests a territory performance report for a specified date range, the system shall generate a report showing: each territory's total invoiced value, total payments received, outstanding AR balance, number of invoices, and comparison to the territory's sales target for the period.

*Traceability: BG-003, STK-006.*

---

**FR-SAL-023** — Sales Target Configuration

When a Sales Manager configures sales targets, the system shall allow entry of monthly and quarterly sales targets per sales agent and per territory, in UGX. Targets shall be configurable up to 12 months in advance. The system shall retain historical targets for comparison reporting.

*Traceability: BG-003, DC-002.*

---

**FR-SAL-024** — Sales Target Achievement Tracking

When a Sales Manager or Director views a sales performance dashboard, the system shall display, for each sales agent and territory: the current period target (monthly and quarterly), actual invoiced sales to date, percentage achievement, and projected end-of-period total based on current run rate.

*Traceability: BG-003, STK-006.*

---

**FR-SAL-025** — Daily Sales Summary Push Notification

When the system clock reaches 18:00 East Africa Time on any business day, the system shall automatically generate a daily sales summary containing: total invoiced value for the day, total payments received, number of invoices issued, top 5 products by revenue, and top 5 territories by revenue. The system shall send this summary as a push notification to the BIRDC Director and Sales Manager and deliver it via email to their registered addresses.

*Traceability: BG-003, STK-001, STK-006, DC-002.*

---

**FR-SAL-026** — Customer Account Management

When a user with the `sales_manager` role creates or edits a customer account, the system shall capture: customer name, trading name, TIN (optional for non-registered businesses), contact persons, physical address, district, payment terms (cash, 7-day, 14-day, 30-day credit), assigned price list, assigned sales agent, assigned territory, and credit limit. All customer account changes shall be logged in the audit trail.

*Traceability: BG-001, DC-003.*

---

**FR-SAL-027** — Sales Agent Assignment to Invoice

When a sales invoice is created, the system shall allow the operator to assign the invoice to a sales agent. When the invoice is created within the Sales Agent Portal by an agent, the system shall automatically assign the invoice to that agent. Agent assignment determines commission accrual (BR-015) and territory attribution (FR-SAL-021).

*Traceability: BG-003, BR-015.*

---

**FR-SAL-028** — Payment Receipt Against Invoice

When a payment is received and recorded against an invoice, the system shall: record the payment amount, payment method (cash, mobile money, cheque, bank transfer), reference number, and date; reduce the invoice outstanding balance; update the invoice status (`partially paid` or `paid`); and post a GL entry (DR Cash/Bank / CR Accounts Receivable) with the payment date and reference.

*Traceability: BG-001, DC-003.*

---

**FR-SAL-029** — AR Aging Report

When a Finance Director or Accounts Assistant requests an AR aging report, the system shall display all outstanding invoices grouped by aging bucket: current (0-30 days), 31-60 days, 61-90 days, 91-120 days, and 120+ days past due. The report shall include customer name, invoice number, invoice date, invoice value, payments received, and outstanding balance. The report shall be exportable to PDF and Excel.

*Traceability: BG-001, STK-002 (Finance Director).*

---

**FR-SAL-030** — Pro Forma Invoice

When a sales officer creates a pro forma invoice, the system shall generate a document with identical fields to a tax invoice but clearly marked "PRO FORMA — NOT A TAX INVOICE" on every page. The system shall submit the pro forma to EFRIS if required by URA EFRIS guidelines `[CONTEXT-GAP: GAP-001]`. A pro forma shall not trigger GL posting. A pro forma may be converted to a confirmed invoice by the operator, at which point all confirmation rules (FR-SAL-009) apply.

*Traceability: BG-002, STK-006.*

---

**FR-SAL-031** — Invoice Search and Filtering

When a user accesses the invoice list, the system shall provide filtering by: invoice number (partial match), customer name (partial match), status, date range, sales agent, territory, and payment status. The invoice list shall display a minimum of 50 rows per page with pagination and be rendered by DataTables to support the expected data volume.

*Traceability: DC-001.*

---

**FR-SAL-032** — Bulk Invoice Export

When a Finance Director or Accounts Assistant selects multiple invoices and requests an export, the system shall generate an Excel workbook containing all selected invoices with line-item detail, GL posting references, EFRIS FDN numbers, and payment status, using PhpSpreadsheet.

*Traceability: BG-001, STK-002.*

---

**FR-SAL-033** — EFRIS Audit Log

The system shall maintain a dedicated EFRIS submission log for every sales document submitted to URA EFRIS. Each log entry shall record: document number, submission timestamp, HTTP status code returned by EFRIS, FDN received (or null on failure), response payload (stored verbatim), retry count, and final submission status. This log shall be tamper-evident and retained for 7 years per DC-003 and Uganda Companies Act requirements.

*Traceability: BG-002, DC-003, BR-013.*

---

**FR-SAL-034** — Discounts and Surcharges at Invoice Level

When an operator applies a discount or surcharge at the invoice header level, the system shall distribute the adjustment proportionally across all line items, recalculate all line totals, update the invoice total, and log the adjustment amount, type (discount or surcharge), and applying user in the invoice record. Invoice-level discounts require approval from a user with the `sales_manager` role when the discount percentage exceeds a configurable threshold (default: 10%).

*Traceability: BG-002, DC-002.*

---

**FR-SAL-035** — Multi-Currency Invoice Support

When an export invoice is created for an international customer, the system shall allow selection of the invoice currency (UGX, USD, EUR, or any configured currency). The system shall record both the foreign currency amount and the UGX equivalent at the exchange rate configured at the time of invoice creation. GL posting shall always be in UGX. `[CONTEXT-GAP: GAP-001]` — confirm EFRIS requirements for foreign-currency invoices.

*Traceability: BG-002, F-005 (GL multi-currency), DC-002.*
