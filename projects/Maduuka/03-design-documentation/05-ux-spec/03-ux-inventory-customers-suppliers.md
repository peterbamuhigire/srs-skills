---
project: Maduuka
document: UX Specification — F-002 Inventory, F-003 Customer Management, F-004 Supplier Management
version: 1.0
date: 2026-04-05
author: Peter Bamuhigire · Chwezi Core Systems
status: Draft
---

# UX Specification: Inventory, Customer Management, and Supplier Management

---

## F-002: Inventory and Stock Management

### Screen I-01: Product List

**Primary user:** David (Stock Manager)

**Entry point:** Tapping "Inventory" in the bottom tab bar (Android) or selecting Inventory → Products from the sidebar (Web).

**Layout description (Android):**

Top section: a search field (full width, 56 dp height) with a filter icon on the trailing edge and a sort icon beside it. Below the search field: a horizontal scrollable row of category filter chips. Active chips use a filled brand-colour style; inactive chips use an outlined style.

Below the filter chips: a product list. Each row is 72 dp tall and contains:
- Product image thumbnail (48 x 48 dp, rounded 4 dp corners) on the left
- Product name (14 sp, bold, 1 line) and SKU (12 sp, secondary colour, 1 line) in the centre column
- Stock level badge on the right: green if ≥ reorder level, amber if at or slightly above reorder level (within 20% of reorder quantity), red if below reorder level or zero
- Selling price (12 sp, right-aligned below the badge)

A floating action button (FAB, 56 dp, brand colour, "+" icon) in the bottom-right corner navigates to the Add Product screen.

**Layout description (Web):**

A data table with columns: Image, Product Name, SKU, Category, Selling Price, Cost Price, Stock Qty, Status. The search and filter bar sits above the table. Sort is available on all columns. A filter panel (collapsible, left of the table on wide viewports) provides category, brand, and status filters. An "Add Product" button (primary, top-right) opens the Product Edit modal.

**Key interactions:**

- Tapping a product row navigates to the Product Detail/Edit screen (Screen I-02).
- Tapping the filter icon opens a filter bottom sheet with: Category, Price Range, Stock Status (In Stock / Low Stock / Out of Stock), Supplier.
- Tapping the sort icon opens a sort bottom sheet with options: Name A–Z, Name Z–A, Lowest Stock, Highest Stock, Recently Added.
- Long-pressing a product row (Android) or selecting a row checkbox (Web) enters multi-select mode. The top bar changes to show a count and action buttons: Delete, Export.

**Offline behaviour:** Product list loads from local SQLite cache. Stock levels shown are from the last sync. Adding or editing products is permitted offline — changes are queued for sync.

**Error states:**

- Empty list after filter: "No products match the selected filters." + "Clear Filters" button.
- Product image fails to load: Replaced by a grey placeholder square with a box icon.

**Android vs Web differences:**

- Web supports bulk export of filtered products as CSV.
- Android FAB for adding products; Web uses a top-right button.

---

### Screen I-02: Product Detail and Edit

**Primary user:** David (Stock Manager)

**Entry point:** Tapping a product row in the Product List.

**Layout description:**

Header: product name with an edit icon (pencil, 24 dp) on the trailing edge. The screen presents information in tabs (Android: tab strip; Web: tab navigation):

- **Details tab:** Product image (full width, 160 dp height, with an "Edit Photo" overlay button). Below the image: fields displayed in a 2-column label-value grid:
  - Product Name, SKU, Barcode, Category, UOM, Cost Price, Selling Price(s) (one row per price tier: Retail, Wholesale, Distributor), Reorder Level, Tax Category, EFRIS-ready status indicator.
- **Stock tab:** Per-branch stock levels displayed as a list of cards (one card per branch). Each card shows: branch name, quantity on hand, value at cost, last movement date. A "Adjust Stock" button on each card navigates to the Add Stock Movement screen (Screen I-04).
- **Batches tab:** Visible only for products with batch/expiry tracking enabled. Shows a list of batches with columns: Batch No., Expiry Date, Quantity, Status (amber if expiring within the configured alert window, red if expired).
- **History tab:** Immutable list of stock movement records for this product: date, type (sale, purchase, adjustment, transfer), quantity (signed: positive for inflows, negative for outflows), balance after movement, and actor (user who created the movement).

**Key interactions:**

- Tapping the edit icon (or the "Edit" button on Web) switches all detail fields into an editable form. Fields use standard Material text fields (Android) or Bootstrap form controls (Web).
- Saving edits posts the change to the server (or queues offline). Success: a green snackbar "Product updated." Failure: inline API error message.
- Tapping "Adjust Stock" navigates to Screen I-04 pre-filled with this product.

**Offline behaviour:** Product details read from local cache. Edits are queued. History tab shows local records only if offline; a banner indicates "Full history requires connectivity."

**Error states:**

- Required field left empty on save: Inline validation beneath the empty field.
- Barcode conflict (another product already has the same barcode): Inline error: "Barcode [value] is already assigned to [Product Name]."

**Android vs Web differences:** Tab strip (Android) vs tab navigation bar (Web). Web shows all tabs simultaneously on wide viewports using a two-column layout (details on left, stock/batches on right).

---

### Screen I-03: Stock Levels Screen

**Primary user:** David (Stock Manager)

**Entry point:** Inventory → Stock Levels from the sidebar (Web) or the "More" tab on Android.

**Layout description:**

A filterable list showing all products with their stock levels across branches. On Web, this is a data table. On Android, this is a list with a prominent branch switcher at the top.

Top controls:
- Branch selector (dropdown on Web; chip selector on Android)
- Filter: All Products / Low Stock Only / Out of Stock Only
- Export button (Web only)

Each row (Android) or table row (Web) shows: product name, category, quantity on hand, reorder level, and a stock status badge. Rows with stock below reorder level are highlighted with an amber left border.

A summary strip at the top of the list shows aggregate counts: "Total SKUs: 142 | Low Stock: 12 | Out of Stock: 3."

**Offline behaviour:** Shows last-synced stock levels. An offline banner is shown. Stock levels may be stale — a "Last updated [time]" timestamp is displayed below the summary strip.

---

### Screen I-04: Add Stock Movement

**Primary user:** David (Stock Manager)

**Entry point:** Tapping "Adjust Stock" from Product Detail (pre-filled) or navigating to Inventory → Stock Movements → New.

**Layout description:**

A single-column form screen. Fields:

1. Product field: pre-filled if entered from Product Detail; otherwise a searchable product picker.
2. Movement Type: a segmented control or radio group — Stock In / Stock Out / Adjustment.
3. Branch (if the business has multiple branches).
4. Quantity: numeric input (mandatory, positive integer or decimal per UOM).
5. Unit Cost (shown for Stock In movements only): numeric input.
6. Reason: a dropdown with options dependent on movement type. Stock In options: Purchase Receipt, Opening Stock, Return from Customer. Stock Out options: Damaged, Expired, Consumed (internal), Return to Supplier. Adjustment options: Count Correction, System Error Correction.
7. Batch Number (shown only for products with batch tracking): text field.
8. Expiry Date (shown only for products with batch tracking): date picker.
9. Notes: multi-line text field (optional).
10. Reference (optional): text field for linking to a purchase order number or other document.

At the bottom: "Record Movement" button (primary action, full width).

**Key interactions:**

- If the movement quantity (Stock Out or Adjustment) would result in negative stock, an amber warning is shown inline: "This will result in negative stock ([−x] units). Continue?" with a "Confirm" checkbox that must be checked before the button activates.
- If the movement value exceeds the configurable approval threshold (BR-005), the "Record Movement" button changes to "Submit for Approval." A manager must approve before the stock level changes.

**Offline behaviour:** Stock movements can be recorded offline. They are queued for sync. The local stock level is updated optimistically.

**Error states:**

- Quantity field left empty: "Record Movement" blocked. Inline error beneath field.
- Quantity zero: Inline validation: "Quantity must be greater than zero."

---

### Screen I-05: Stock Count Workflow

**Primary user:** David (Stock Manager)

The stock count is a multi-step workflow. The steps are presented as a linear flow with a progress indicator at the top: Freeze → Count Entry → Variance Review → Approve.

**Step 1: Freeze**

A confirmation screen explaining that initiating a count will freeze stock movements for the selected product category or all products. Fields:
- Scope: "All Products" or "Selected Category" (dropdown).
- Branch (if multi-branch).

Warning banner: "Stock movements will be paused for the selected scope during the count. This affects live sales." A "Start Count" button initiates the freeze and generates a count sheet.

**Step 2: Count Entry**

A list of all products in the frozen scope. Each row shows: product name, SKU, expected quantity (shown only after the count is submitted — hidden during counting to prevent bias), and a "Counted Qty" numeric input field. Products can be sorted by location or name.

A "Scan to Find" mode toggles camera scanning — scanning a product barcode jumps the list to that product row.

A progress indicator at the top shows: "42 of 142 items counted."

The user saves progress at any point. The list persists across sessions until submitted.

A "Submit Count" button at the bottom is enabled only when all items have an entry (including zeros — entering 0 is an explicit zero-count confirmation, not the same as leaving blank).

**Step 3: Variance Review**

After submission, the system reveals the expected quantities and calculates variances. The list now shows three columns: Expected, Counted, Variance. Rows with non-zero variance are sorted to the top and highlighted. Positive variance (counted more than expected) is shown in green. Negative variance (counted fewer than expected) is shown in red.

An "Approve and Post" button and a "Return to Count" button are shown. Returning to count is permitted if the variance review reveals a data entry error.

**Step 4: Approve**

For adjustments above the configured threshold (BR-005), manager approval is required. The Approve step shows a summary: total variance value, count by category, and an "Approve and Post Adjustments" button. On approval, stock levels are updated via immutable adjustment records (BR-004).

**Offline behaviour:** Count entry works offline (the count list is local). Freeze initiation and final approval require connectivity.

---

### Screen I-06: Stock Transfer Screen

**Primary user:** David (Stock Manager)

**Entry point:** Inventory → Transfers → New Transfer.

**Layout description:**

A form with the following fields:

1. From Branch: dropdown of branches.
2. To Branch: dropdown (excludes From Branch selection).
3. Transfer Items: a product picker list. The user adds products one at a time using a product search field. Each added row shows: product name, available stock at the From Branch, and a quantity input.
4. Notes: text field.
5. Expected Delivery Date: date picker (optional).

"Submit Transfer" button at the bottom.

After submission, the transfer is in "In Transit" status. The stock is deducted from the From Branch immediately and added to the To Branch only when the receiving manager confirms receipt on the Goods Receipt screen.

**Offline behaviour:** Transfer submission is queued offline. Stock deduction from the source branch is applied optimistically.

---

### Screen I-07: Expiry Alerts List

**Primary user:** David (Stock Manager)

**Entry point:** Dashboard alert card → "View Expiring Stock" or Inventory → Expiry Alerts.

**Layout description:**

A filterable list. Top filter tabs: "Expiring in 30 days" / "Expiring in 60 days" / "Expiring in 90 days" / "Expired."

Each row shows: product name, batch number, expiry date, quantity, and branch. Rows in the "Expired" tab have a red background tint. Rows within the 30-day window have an amber tint.

Actions on each row (long-press on Android; row action buttons on Web): "Mark for Return to Supplier," "Write Off (Stock Out — Expired)," "View Batch History."

---

## F-003: Customer Management

### Screen C-01: Customer List

**Primary user:** Agnes (Cashier) for quick lookup; Grace (Accountant) for account management

**Entry point:** "Customers" from the More tab (Android) or sidebar (Web).

**Layout description:**

Search field at the top. Below: filter chips — All / VIP / Wholesale / Retail / Staff / With Overdue Balance.

Each customer row (72 dp) shows:
- Customer initials avatar (40 dp circle, coloured by group) on the left
- Name (bold, 14 sp) and phone number (12 sp, secondary)
- Credit status badge on the right: green "Good" / amber "Near Limit" / red "Overdue"
- Outstanding balance amount (12 sp, right-aligned, shown only if > 0)

FAB (Android) / "Add Customer" button (Web) navigates to a new customer form.

**Offline behaviour:** Customer list loaded from local cache.

---

### Screen C-02: Customer Detail

**Primary user:** Grace (Accountant), Agnes (Cashier)

**Entry point:** Tapping a customer row in the Customer List.

**Layout description:**

Tabbed view. Header card (always visible above tabs): customer name, phone, group badge, and a "Record Payment" button (primary action — used to collect a credit payment).

Tabs:

- **Profile:** All customer fields in read/edit mode — name, phone, email, district/sub-county, customer group, credit limit, notes.
- **Credit:** Credit Limit (editable by managers), Current Outstanding Balance, Available Credit, Last Payment Date, Next Payment Due. A "Collect Payment" button triggers a payment collection modal.
- **Transactions:** Chronological list of all transactions — sales, payments, adjustments. Each row: date, type, amount (signed), and a "View" link to the original receipt/document.
- **Statement:** A date-range selector and a "Generate Statement" button. The statement preview shows opening balance, movements, closing balance. Export: PDF, WhatsApp.

**Key interactions:**

- "Record Payment" opens a modal: payment amount (pre-filled with full outstanding balance but editable), payment method (Cash, MoMo), reference number (optional). On confirm, the payment is recorded and the credit balance updated.
- Credit Limit edit is restricted to manager-level users. Non-managers see the credit limit as read-only.

**Offline behaviour:** Profile and Transaction tabs load from local cache. Statement generation requires connectivity.

---

### Screen C-03: Magic-Link Customer Portal

**Primary user:** Customer (self-service, no Maduuka account)

**Entry point:** Customer taps a link received via WhatsApp or SMS. The link is a time-limited token (30-day inactivity expiry per Section 3.1.3 of the External Interfaces spec).

**Layout description:**

A mobile web view (not a native app). The portal is intentionally minimal. It opens directly to the customer's account overview with no login form.

Header: business logo + business name. Greeting: "Hello [Customer Name]."

Content sections (vertical scroll):

1. **Account Balance card:** Outstanding Balance (large, 24 sp), Credit Limit, Available Credit.
2. **Recent Purchases:** List of the last 10 transactions. Each row: date, receipt number, amount, payment method. "View All" link shows full history.
3. **Download Statement** button: generates a PDF statement for the last 3 months.

No buttons to modify any data. No form inputs. The portal is strictly read-only. If the link has expired, the page shows: "This link has expired. Ask [Business Name] to send you a new one." — with no login option.

**DC-002 compliance:** No login credentials. No account creation. No terminology that requires accounting knowledge.

---

### Screen C-04: Debtors Ageing Report Screen

**Primary user:** Grace (Accountant), Robert (Business Owner)

**Entry point:** Customers → Debtors Ageing or Reports → Debtors Ageing.

**Layout description:**

A report screen with a date-as-of selector (defaults to today). Below: a summary strip showing total outstanding across all customers and count of customers with overdue balances.

The main table shows columns: Customer Name, Phone, Credit Limit, Current (0–30 days), 31–60 Days, 61–90 Days, 90+ Days, Total Outstanding. Rows are sortable by any column.

Rows with any amount in the 90+ Days column are highlighted with a red left border. Rows with amounts in 31–90 Days use an amber left border.

Actions (Web only): Export CSV, Export PDF, Print, Send WhatsApp Reminder (bulk action: sends a WhatsApp payment reminder to all selected customers).

**Offline behaviour:** Report loads from local cache data. An "As of last sync" timestamp is shown. Export and WhatsApp send require connectivity.

---

## F-004: Supplier and Vendor Management

### Screen S-01: Supplier List

**Primary user:** David (Stock Manager), Grace (Accountant)

**Entry point:** Suppliers from the sidebar (Web) or More tab (Android).

**Layout description:**

Search field at top. List of suppliers, each row showing: supplier name, contact person, phone, and a "Balance Due" badge (amber if > 0, green if zero).

FAB (Android) / "Add Supplier" button (Web) opens a supplier creation form (modal on Web, full screen on Android). Supplier form fields: Business Name, Contact Person, Phone, Email, Physical Address, Payment Terms, Bank Name, Account Number.

---

### Screen S-02: Purchase Order Creation

**Primary user:** David (Stock Manager)

**Entry point:** Suppliers → [Supplier Name] → New PO, or Inventory → Purchase Orders → New.

**Layout description:**

A form-style screen divided into two sections:

**Header section (always visible):**
- Supplier (pre-filled if entered from supplier context, otherwise a searchable supplier picker)
- PO Date (date picker, defaults to today)
- Expected Delivery Date (date picker)
- Delivery Address (branch picker)

**Line items section:**
- A list of PO line items. Each row: product picker (searchable), quantity input, unit cost input, line total (calculated, read-only).
- "Add Item" button appends a new empty row.
- Rows can be reordered (drag handle on Android, up/down arrows on Web).
- A row can be removed via a trailing trash icon.

**Totals strip (bottom):**
- Subtotal, Discount (optional), Total.

**Action buttons:**
- "Save as Draft" (secondary) and "Submit PO" (primary). Submitted POs generate a PDF and can be emailed to the supplier directly from the confirmation screen.

**Offline behaviour:** POs can be drafted offline. Submission is queued.

---

### Screen S-03: Goods Receipt Screen

**Primary user:** David (Stock Manager)

**Entry point:** Suppliers → Purchase Orders → [PO] → Receive Goods, or via a notification when a PO delivery date is reached.

**Layout description:**

Header: PO reference number, supplier name, expected delivery date.

A list of PO line items with columns: Product, Ordered Qty, Previously Received, Receiving Now (editable numeric input), Remaining. The "Receiving Now" column is pre-filled with the full remaining quantity for each item. The user reduces quantities for partial deliveries.

Fields below the item list:
- Delivery Note Number (optional reference field)
- Batch Number and Expiry Date (shown per item if batch tracking is enabled for that product)
- Notes

"Confirm Receipt" button at the bottom. If the received quantities are less than ordered, a summary message appears: "Partial receipt: [X] of [Y] items fully received. The PO will remain open for the remaining items."

Three-way matching trigger: After confirming the receipt, if a supplier invoice has been recorded against this PO, the system automatically runs the three-way match check (BR-011) and navigates to Screen S-04 if discrepancies are found.

**Offline behaviour:** Goods receipt can be recorded offline. Stock is updated locally. Three-way matching runs when connectivity is restored.

---

### Screen S-04: Three-Way Matching Review

**Primary user:** Grace (Accountant), Robert (Business Owner / Manager)

**Entry point:** Automatically after a goods receipt when a linked invoice has discrepancies, or via Suppliers → Pending Matches.

**Layout description:**

Header: "Purchase Matching Review — PO [reference]."

A 3-column comparison table:

| Item | PO | Goods Receipt | Invoice |
|---|---|---|---|
| [Product Name] | [Qty × Unit Price] | [Received Qty × Unit Price] | [Invoiced Qty × Unit Price] |

Discrepant rows are highlighted in amber. A "Discrepancy" badge shows the delta for quantity and price mismatches.

Below the table: a "Resolution" section for each discrepancy. Options (radio buttons):
- Accept invoice as-is (overpayment noted)
- Accept GRN quantity (short invoice supplier)
- Request credit note from supplier
- Flag for manual review

A "Notes" field per discrepancy row.

"Submit Resolution" button at the bottom. Unresolved discrepancies block finalisation per BR-011.

**Offline behaviour:** Three-way matching review requires connectivity to access all three source documents.

**Error states:**

- Attempting to finalise a purchase with unresolved discrepancies: "Submit Resolution" button disabled. Inline message: "Resolve all flagged discrepancies before finalising."
