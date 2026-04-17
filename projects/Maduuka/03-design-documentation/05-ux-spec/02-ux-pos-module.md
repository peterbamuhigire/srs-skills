---
project: Maduuka
document: UX Specification — F-001 Point of Sale Module
version: 1.0
date: 2026-04-05
author: Peter Bamuhigire · Chwezi Core Systems
status: Draft
---

# UX Specification: F-001 Point of Sale Module

## Overview

The POS module is the highest-frequency screen in Maduuka. Agnes (the cashier) may complete 50–200 transactions per day entirely within these screens. Every interaction is optimised for speed and error recovery. The design priority order is: speed of sale completion > error prevention > feature discoverability.

---

## Screen 1: POS Main Screen

**Primary user:** Agnes (Cashier)

**Entry point:** Tapping the POS tab in the bottom navigation bar (Android) or selecting POS from the sidebar (Web). If no session is open, the system redirects to the Open Session screen first (see Screen 10).

**Layout description (Android):**

The screen is divided into two vertical zones:

- Top zone (approximately 55% of screen height): Product discovery area. Contains a search field at the top (full width, 56 dp height, with a barcode-scan icon on the trailing edge). Below the search field is a horizontal scrollable row of category filter chips (All, Beverages, Food, Household, etc.). Below the filters is a product grid: 3 columns on phones, 5 columns on 7-inch tablets. Each product card is square, contains the product image (top 60% of card), product name (2 lines max, truncated with ellipsis), and price (1 line, bold, brand colour). Cards have no borders — they use an 8 dp card elevation shadow. Card tap target is the full card area.
- Bottom zone (approximately 45% of screen height): Active cart. A horizontal divider separates the zones. The cart shows: item count badge ("3 items"), a scrollable list of cart line items, and at the bottom a totals strip showing Subtotal, Discount (if any), and Total. Below the totals strip is a full-width "Charge [Total]" button (primary action, 56 dp height, brand colour fill, white text). The button label dynamically shows the current cart total using the configured currency symbol.

**Layout description (Web):**

Two-column layout. Left column (60% width): product search field, category filter chips, product grid (4 columns). Right column (40% width): cart panel fixed to the full column height, showing cart line items, totals, and the Charge button at the bottom. The right column does not scroll with the page — it is a fixed panel.

**Key interactions:**

- Tapping a product card adds 1 unit of that product to the cart. A brief scale animation (100 ms, scale 1.0 → 1.05 → 1.0) confirms the add — this animation is conditional on device capability; it is skipped if the frame rate drops below 60 fps.
- Tapping the barcode icon in the search field activates the camera barcode scanner (Android) or prompts for USB/Bluetooth scanner input (Web). A scanned barcode that matches a product adds that product to the cart immediately without requiring a tap.
- Tapping a cart line item opens the line item edit sheet (quantity, per-item discount, note).
- Swiping a cart line item left (Android) reveals a red "Remove" action.
- Tapping the Charge button navigates to the Payment Screen (Screen 4).
- Long-pressing a product card opens a bottom sheet with: View Product, Edit Price (manager only), and Mark Out of Stock.

**Offline behaviour:**

The product grid and cart function fully offline. Products are loaded from the local SQLite cache. New sales are queued for sync (BR-009). The offline banner is visible. The Charge button remains active. Mobile money payment options are hidden when offline (they require API calls); only Cash and Credit payment methods are available offline.

**Error states:**

- Product not found by barcode: Inline message below the search field: "Barcode [value] not found. Add a new product?" with an "Add Product" button.
- Cart total is zero: The Charge button is disabled (greyed, 0.4 opacity). Tooltip on tap: "Add at least one item to proceed."
- Session not open: Automatic redirect to Open Session screen; no error shown on POS Main.

**Android vs Web differences:**

- Barcode scanning via camera is Android-only. Web relies on USB/Bluetooth scanner or manual barcode entry.
- Full-screen POS mode (status bar and system navigation hidden) is Android-only.
- Web supports keyboard shortcut `F2` to focus the search field.

---

## Screen 2: Product Search Results

**Primary user:** Agnes (Cashier)

**Entry point:** Typing 2 or more characters into the POS search field. Results appear as the user types (debounced at 300 ms). There is no search button — results are live.

**Layout description:**

The product grid replaces its contents with search results matching the query. The category filter chips are hidden during active search. Above the grid, a result count label appears: "12 results for 'sugar'". If the search returns more than 30 results, only the first 30 are shown with a "Show more results" link at the bottom of the grid.

Results are ranked: exact name match first, then SKU/barcode match, then partial name match. Each result card shows the same layout as the main product grid card with an additional stock level badge in the top-right corner of the card (green badge if in stock, red badge if out of stock).

**Key interactions:**

- Adding a product from search results works identically to the main grid: single tap adds 1 unit to the cart.
- Clearing the search field (via the X icon that appears when text is present) returns to the full product grid with category filters.
- If exactly 1 result is returned and the search was triggered by a barcode scan, the product is added to the cart automatically without requiring a tap.

**Offline behaviour:** Search operates on the local cache. Results are available offline. Stock levels shown are from the last sync.

**Error states:**

- Zero results: Empty state with the search term highlighted, message "No products match '[term]'", and a primary button "Add New Product."
- Search field contains only spaces: Search is not triggered; the field is cleared on blur.

**Android vs Web differences:** No functional differences. Web displays a wider grid (4 columns vs 3 on phone).

---

## Screen 3: Cart Detail

**Primary user:** Agnes (Cashier)

**Entry point:** Tapping a line item in the active cart on the POS Main Screen, or tapping a cart-expand icon when the cart is in collapsed state on small screens.

**Layout description (Android):**

Full-screen view (or large bottom sheet on tablets). Header: "Cart" with an item count ("4 items"). Below the header is a scrollable list of cart line items. Each line item row contains:

- Product name (left, 14 sp, bold, 2 lines max)
- Unit price (right of name, 12 sp, secondary colour)
- Quantity control: a minus button (32 dp circle), a quantity display field (48 dp width, centre-aligned, editable by tap), and a plus button (32 dp circle)
- Line total (right-aligned, 14 sp, bold)
- Per-item discount field (below quantity, shown only if a discount has been applied; tapping opens a discount input sheet)
- A trailing trash icon (32 dp, red) to remove the item

Below the list is the totals section:
- Subtotal row
- Discount row (shown only if a discount is applied; a "Add Discount" link shows if no discount is active)
- Tax row (shown only if tax is configured as exclusive)
- Total row (larger text: 18 sp, bold)

At the bottom: two buttons side by side — "Hold Sale" (secondary style, 50% width) and "Charge [Total]" (primary style, 50% width).

**Key interactions:**

- Tapping the quantity display field opens a numeric keypad (Android: system numeric keyboard; Web: inline number input). The user enters the new quantity directly.
- Tapping the minus button decrements quantity by 1. At quantity 1, tapping minus shows the confirmation "Remove this item?" with "Remove" and "Keep" options.
- Tapping "Add Discount" opens a discount input bottom sheet. The user enters a percentage (0–100) or a fixed amount. The discount is validated: a fixed discount cannot exceed the line total.
- Tapping Hold Sale navigates to the Hold Sale confirmation (Screen 8a).
- Tapping Charge navigates to the Payment Screen (Screen 4).

**Offline behaviour:** All cart operations are local. No network calls. Full functionality available offline.

**Error states:**

- Quantity field left empty: On blur, the field reverts to the previous valid quantity.
- Discount percentage > 100: Inline validation: "Discount cannot exceed 100%."
- Discount amount > line total: Inline validation: "Discount cannot exceed line total of [amount]."

**Android vs Web differences:**

- Web displays the cart detail as a persistent right-hand panel rather than a full-screen view. The layout is otherwise equivalent.
- Web quantity controls include keyboard increment/decrement (up/down arrow keys when the quantity field is focused).

---

## Screen 4: Payment Screen

**Primary user:** Agnes (Cashier)

**Entry point:** Tapping "Charge [Total]" from the POS Main Screen or Cart Detail.

**Layout description:**

Header: "Payment" with a back arrow. Directly below: a large display of the sale total ("Total Due: [currency symbol] [amount]", 24 sp, bold, centred).

Below the total is a section titled "Payment Method." This section displays payment method tiles in a 2-column grid. Each tile is a card (72 dp height, full-width of its grid cell) showing the method icon and label:

- Cash
- MTN MoMo
- Airtel Money
- Credit (customer account)
- Split Payment (multi-method)

The selected tile has a brand-blue border (2 dp) and a light-blue fill. The default selected method is Cash.

Below the payment method grid: a "Selected Method" summary area. When Cash is selected, it shows a large "Tendered Amount" input and the calculated change (see Screen 5). When MoMo/Airtel is selected, it shows the phone number input. When Credit is selected, it shows the customer selector.

At the bottom: a full-width "Confirm Payment" button (primary action, 56 dp, brand colour).

**Key interactions:**

- Tapping a payment method tile selects it and updates the "Selected Method" summary area instantly.
- Tapping "Split Payment" activates multi-method mode: the summary area shows a list where the user assigns amounts to each method.
- Tapping "Confirm Payment" triggers the payment processing flow for the selected method.

**Offline behaviour:**

MoMo and Airtel Money tiles are shown but disabled (with a tooltip: "Mobile Money requires internet connection"). Cash and Credit remain available. The Charge button proceeds with Cash or Credit flows.

**Error states:**

- Attempting to proceed with MoMo/Airtel offline: Tile is tappable but shows a non-blocking bottom sheet: "Mobile money is unavailable offline. Use Cash or Credit."
- Sale total is zero: The Confirm Payment button is disabled.
- Credit selected but no customer chosen: The Confirm Payment button remains disabled until a customer is selected.

**Android vs Web differences:**

- Web displays payment method selection as large radio-button cards in a single column on the left, with the summary panel on the right.
- Web keyboard shortcut `F4` focuses this screen.

---

## Screen 5: Cash Payment Modal

**Primary user:** Agnes (Cashier)

**Entry point:** Tapping "Confirm Payment" on the Payment Screen when Cash is selected.

**Layout description:**

A bottom sheet modal (Android) or a centred dialog (Web, 400 px wide). Contents:

- Header: "Cash Payment"
- Sale total displayed prominently: "[currency symbol] [amount]", 20 sp, bold
- "Amount Tendered" label with a large numeric input field below it (height: 64 dp on Android, 48 px on Web). The input is pre-focused and the keyboard opens automatically. The input shows the full amount as a default (no change scenario). An "Exact" chip next to the field auto-fills the exact sale amount.
- Change Due section: updates in real time as the user types. Label: "Change Due." Amount displayed in 20 sp, green (#388E3C) if positive, red if the tendered amount is less than the total.
- Quick-amount chips: rows of common denomination buttons (e.g., 1000, 2000, 5000, 10000, 20000, 50000) appropriate to the configured currency. Tapping a chip adds that value to the tendered amount field.
- "Complete Sale" button (full width, 56 dp, primary action). Disabled if tendered amount is less than total.

**Key interactions:**

- Typing in the tendered field updates the Change Due display in real time (no submit needed).
- Tapping a denomination chip sets the tendered amount to that denomination if the field is empty, or adds it to the current value if the field already has an entry.
- Tapping "Complete Sale" records the sale, deducts stock, and navigates to the Receipt Options Screen (Screen 9).

**Offline behaviour:** Full functionality. Cash sales are the primary offline payment method.

**Error states:**

- Tendered amount less than total: "Complete Sale" button disabled. Change Due shown in red with the label "Insufficient — short by [amount]."
- Non-numeric input: The numeric keyboard prevents non-numeric entry on Android. On Web, the field rejects non-numeric characters on input.

**Android vs Web differences:** Modal presentation (bottom sheet vs dialog). Functionally identical.

---

## Screen 6: Mobile Money Payment Modal

**Primary user:** Agnes (Cashier)

**Entry point:** Tapping "Confirm Payment" on the Payment Screen when MTN MoMo or Airtel Money is selected.

**Layout description:**

A bottom sheet modal (Android) or centred dialog (Web, 440 px wide). States progress through: Input → Pending → Success/Failure.

**State: Input**

- Header: "MTN MoMo" or "Airtel Money" with the carrier logo icon (32 dp).
- "Customer Phone Number" label with a phone input field (pre-filled if the sale is linked to a customer with a phone number on file).
- Amount display: "[currency symbol] [amount]", 18 sp, bold.
- "Send Payment Request" button (full width, primary action). On tap, transitions to Pending state.

**State: Pending**

- A centred circular progress indicator (48 dp).
- Status label: "Request sent to [phone number]. Waiting for customer to approve on their phone…"
- Amount displayed.
- A countdown timer (120-second timeout): "Expires in 1:45."
- "Cancel Request" link (secondary text button, centred below).

**State: Success**

- A large green checkmark icon (64 dp).
- "Payment Confirmed" in 18 sp, green.
- Transaction reference number displayed in monospace: "Ref: [MoMo TXN ID]."
- "View Receipt" button and "Done" button.

**State: Failure / Timeout**

- A large red X icon (64 dp).
- Failure reason: "Customer declined" / "Request timed out" / "Network error" — specific to the API response code.
- "Retry" button (primary action) and "Use Different Method" button (secondary action).

**Key interactions:**

- The system polls the MoMo/Airtel API every 5 seconds during the Pending state.
- At 120 seconds without a confirmed response, the system transitions to the Failure state automatically with reason "Request timed out."
- Tapping "Cancel Request" sends a cancellation to the API and returns to the Payment Screen.
- Tapping "Retry" returns to the Input state with the phone number pre-filled.
- Tapping "Use Different Method" returns to the Payment Screen.

**Offline behaviour:** This screen is inaccessible offline (Mobile Money tiles are disabled on the Payment Screen when offline).

**Error states:**

- Phone number field empty: "Send Payment Request" button disabled. Label turns red: "Phone number is required."
- Invalid phone number format: Inline validation: "Enter a valid [MTN/Airtel] number starting with [07X]."
- API returns "insufficient funds" response: Failure state with message: "Customer has insufficient MoMo balance."

**Android vs Web differences:** Bottom sheet vs dialog presentation. On Web, the countdown timer is displayed as a progress bar rather than a text countdown.

---

## Screen 7: Credit Sale Screen

**Primary user:** Agnes (Cashier) with manager override capability

**Entry point:** Tapping "Confirm Payment" on the Payment Screen when Credit is selected.

**Layout description:**

A bottom sheet (Android) or right-panel expansion (Web). Contents:

- Header: "Credit Sale"
- Customer search field (full width, with placeholder "Search customer by name or phone"). The field auto-focuses on screen open.
- As the user types, a list of matching customers appears below the field. Each result row shows: customer name (bold), phone number (secondary), and a credit status badge — "Available: [currency symbol] [available credit]" in green or "Limit Reached" in red.
- After a customer is selected, the screen shows a customer credit summary card:
  - Customer name and phone
  - Credit Limit: [amount]
  - Outstanding Balance: [amount]
  - Available Credit: [calculated: Limit − Balance] in green if positive, red if zero or negative
  - Sale Amount: [current cart total]
  - New Balance After Sale: [Outstanding + Sale Amount] — shown in red if it exceeds the limit
- "Approve Credit Sale" button (primary action, full width). Disabled if the new balance would exceed the credit limit.
- "Request Manager Override" button (secondary action). Visible only when the credit limit would be exceeded.

**Key interactions:**

- Typing in the customer search field shows live results (debounced 300 ms).
- Selecting a customer populates the credit summary card.
- If the sale amount exceeds available credit, the "Approve Credit Sale" button is disabled per BR-002.
- Tapping "Request Manager Override" displays a PIN entry field. A manager enters their PIN to unlock the sale. The override is recorded in the audit log (BR-002, BR-003).
- Tapping "Approve Credit Sale" records the sale against the customer's credit account and navigates to the Receipt Options Screen.

**Offline behaviour:** Customer credit balances are read from the local cache. The credit limit check runs locally. The sale is queued for sync. Manager override is permitted offline — the override is recorded locally and synced.

**Error states:**

- No customer selected: "Approve Credit Sale" button disabled with tooltip "Select a customer first."
- Customer balance would exceed limit (without override): Button disabled, the New Balance row is highlighted in red with an icon.
- Manager PIN incorrect: Inline error below the PIN field: "Incorrect PIN. Try again."

**Android vs Web differences:**

Web displays this as a right-panel slide-in rather than a bottom sheet. Customer search results show a 5-column mini-table (name, phone, credit limit, balance, available).

---

## Screen 8: Hold Sale and Resume Sale

**Primary user:** Agnes (Cashier)

**Entry point (Hold):** Tapping "Hold Sale" from the Cart Detail screen.

### Screen 8a: Hold Sale Confirmation

**Layout description:**

A bottom sheet (Android) or small modal dialog (Web). Contents:

- Title: "Hold This Sale?"
- Optional "Hold Note" field (single line, placeholder "e.g., Customer left to get cash"). The note is optional.
- "Hold Sale" button (primary, amber fill) and "Cancel" button (secondary).

**Key interactions:**

- Tapping "Hold Sale" saves the current cart with all line items, discounts, and the optional note. The POS Main Screen resets to an empty cart. A success snackbar appears: "Sale held. Tap Resume to continue."
- Up to 5 sales can be held simultaneously per session. If 5 are already held, the "Hold Sale" button is disabled with a message: "Maximum 5 held sales reached. Resume or void a held sale."

### Screen 8b: Resume Sale

**Entry point:** Tapping the "Resume" icon on the POS Main Screen (a clock/tray icon in the top-right of the POS screen, with a badge showing the count of held sales).

**Layout description:**

A bottom sheet (Android) or modal (Web) showing a list of held sales. Each held sale row shows:

- Hold number (e.g., Hold #2)
- Item count ("3 items")
- Cart total
- Hold time ("Held 4 minutes ago")
- Hold note (if provided)
- "Resume" button (primary text button, right-aligned) and "Void" button (destructive text, red)

**Key interactions:**

- Tapping "Resume" on a held sale loads that cart into the active POS cart. If the current cart has items, a confirmation appears: "Replace current cart with this held sale?"
- Tapping "Void" on a held sale shows a confirmation dialog: "Void this held sale?" with reason code selection.

**Offline behaviour:** Held sales are stored locally. Full functionality offline.

**Error states:**

- Attempting to hold a 6th sale: Button disabled with inline message (see above).
- Resuming a sale where a product has since gone out of stock: A warning badge appears on the product row in the resumed cart. The sale can still proceed; the out-of-stock warning is advisory.

**Android vs Web differences:** Bottom sheet vs modal presentation. Functionally identical.

---

## Screen 9: Receipt Options Screen

**Primary user:** Agnes (Cashier)

**Entry point:** Automatically after a successful payment (Cash, MoMo, or Credit).

**Layout description:**

A full-screen confirmation view (not a modal — this is a deliberate full-screen design to mark the completion of a sale). Top section: a large green checkmark icon (72 dp), "Sale Complete" in 20 sp green, and the total amount paid in 24 sp bold. Below: a subtle divider and a receipt preview area showing the first 5 lines of the receipt (business name, receipt number, date, item count, total) in a receipt-style monospace font inside a card.

Below the preview: a section titled "Send Receipt." Options presented as full-width action tiles (each 56 dp height):

- Print Receipt (Bluetooth thermal printer icon)
- Send via WhatsApp (WhatsApp green icon)
- Send via SMS (speech bubble icon)
- Download PDF (download icon)
- No Receipt (ghost button / text link at the bottom)

Below the action tiles: a "New Sale" button (primary action, full width, 56 dp). This button navigates back to the POS Main Screen with a fresh empty cart.

**Key interactions:**

- Tapping Print Receipt: Sends the receipt to the paired Bluetooth printer. A loading indicator overlays the tile. On success, the tile shows a green checkmark. On failure (no printer found), a snackbar appears: "Printer not found. Check Bluetooth pairing."
- Tapping Send via WhatsApp: Opens the WhatsApp share intent (Android) or WhatsApp API send (Web). The receipt PDF is attached automatically.
- Tapping Send via SMS: Prompts for a phone number (pre-filled if a customer is linked to the sale) and sends a receipt summary via Africa's Talking.
- Tapping Download PDF: Generates and downloads the receipt as an A4 PDF.
- Tapping No Receipt: Dismisses receipt options and navigates to a fresh POS sale without sending a receipt. The receipt number is still issued (BR-008 gap detection integrity maintained).
- Tapping New Sale: Equivalent to No Receipt but visually primary — it is the most prominent action, designed so Agnes can proceed immediately without deciding about receipt delivery.

**Offline behaviour:**

- Print Receipt: Available if printer is paired.
- WhatsApp/SMS: Queued and sent when connectivity is restored. A notification informs Agnes: "Receipt will be sent when reconnected."
- Download PDF: Available offline — PDF generated locally.

**Error states:**

- WhatsApp not installed (Android): Falls back to sharing the PDF via the Android share sheet.
- SMS send failure: Snackbar: "SMS could not be sent. Download PDF instead."
- Printer connection failure: Described above.

**Android vs Web differences:**

- Print Receipt on Web uses the browser print dialog.
- WhatsApp on Web opens the WhatsApp Web API link in a new tab.
- Android shows a WhatsApp share intent for the native app.

---

## Screen 10: POS Session — Open Session

**Primary user:** Agnes (Cashier)

**Entry point:** Automatically when the user navigates to POS and no active session exists for their user account at the current branch.

**Layout description:**

A full-screen, single-purpose screen (not a modal). Header: "Open POS Session." The screen is centred vertically with:

- A brief instruction: "Enter your opening cash float to start the session."
- "Opening Float Amount" label with a large numeric input field (64 dp height). The field is auto-focused. A currency symbol prefix (configured symbol) is shown as a non-editable prefix inside the field.
- "Common Amounts" chips: rows of denomination chips for quick entry.
- A summary card below the field showing: "Session will start at [current time]" and "Branch: [branch name]."
- "Open Session" button (full width, primary action, 56 dp).

**Key interactions:**

- The opening float may be zero if the business has no opening cash. A float of zero is valid.
- Tapping "Open Session" creates the session record, records the opening float, and navigates to the POS Main Screen.
- The session is locked to the opening user. Other cashiers cannot process sales under this session.

**Offline behaviour:** Session can be opened offline. The session record is stored locally and synced when connectivity is restored.

**Error states:**

- Non-numeric float entry: Field prevents non-numeric input.
- An existing open session for the same user and branch: The system automatically continues the existing session; this screen is not shown.

**Android vs Web differences:** None. Functionally identical.

---

## Screen 11: POS Session — Close Session

**Primary user:** Agnes (Cashier) or Robert (Business Owner)

**Entry point:** Tapping "Close Session" from the POS More menu or the session status indicator.

**Layout description:**

A full-screen view with header "Close POS Session." The screen is divided into a reconciliation summary:

**Summary section:**

| Item | Amount |
|---|---|
| Opening Float | [amount] |
| + Cash Sales | [amount] |
| − Cash Refunds | [amount] |
| = Expected Cash | [calculated] |
| Counted Cash | [input field] |
| Variance | [calculated — coloured green if zero, amber if within tolerance, red if above tolerance] |

The "Counted Cash" row is the only editable field. It is a large numeric input. The Variance row updates in real time as the user enters the counted amount.

Below the summary: a session statistics card showing:
- Total Transactions: [count]
- Total Revenue: [amount]
- MoMo Payments: [amount]
- Airtel Payments: [amount]
- Credit Sales: [amount]
- Voids: [count]

Below the statistics: a "Session Notes" field (multi-line, optional, 4 lines visible).

At the bottom: "Close Session" button (primary action, full width). A confirmation dialog appears before closing (destructive action per Section 2.7 of Principles document).

**Key interactions:**

- Entering the counted cash amount updates the Variance row in real time.
- Tapping "Close Session" triggers the confirmation dialog: "Close this session? This cannot be undone." The dialog shows the variance as a warning if non-zero.
- After confirmation, the session is closed. The user is redirected to the POS Main Screen which now shows the Open Session screen for the next session.
- A closing summary PDF is generated automatically and available in Reports.

**Offline behaviour:** Session can be closed offline. The close event and reconciliation data are stored locally and synced.

**Error states:**

- Counted cash field left empty: "Close Session" button disabled with tooltip "Enter your counted cash amount to continue."
- Variance exceeds configurable threshold: The Variance row shows an amber warning: "Variance of [amount] exceeds the allowed threshold. A manager will be notified."

**Android vs Web differences:**

Web shows the reconciliation as a structured data table with column headers. Android shows it as a card with row-label pairs.

---

## Screen 12: Void and Refund Screen

**Primary user:** Agnes (Cashier) for same-session voids; Robert (Business Owner) for cross-session refunds

**Entry point:**

- Same-session void: Tapping "Void Sale" from the receipt or from the session's transaction list.
- Historical refund: Navigating to Reports → Sales → Transaction Detail → "Refund."

**Layout description:**

Header: "Void Sale" or "Process Refund" depending on entry path.

Top section: Sale summary card showing:
- Receipt number
- Date and time
- Cashier name
- Item count and total

Below: a list of sale line items with checkboxes. For a full void, all items are pre-checked. For a partial refund, the user unchecks items they are NOT refunding.

Below the item list:
- "Refund Method" selection (same options as payment, limited to the original payment method for cash and MoMo; credit refunds go to customer credit account).
- "Reason Code" required dropdown: Customer Return, Pricing Error, Duplicate Sale, Damaged Item, Other.
- "Notes" field (optional, single line).
- Refund total (auto-calculated from checked items): "[currency symbol] [amount]", 18 sp, bold.
- "Confirm Void" or "Confirm Refund" button (primary action, red fill #D32F2F).

**Key interactions:**

- Checking/unchecking item checkboxes updates the refund total in real time.
- Reason Code is mandatory. The confirm button is disabled until a reason is selected.
- Tapping the confirm button shows the standard confirmation dialog (destructive action).
- On confirmation: the sale record is flagged as voided/partially refunded. A counter-movement stock entry is created. The void is recorded in the audit log (BR-003). A new void/refund receipt is issued with a separate receipt number.

**Offline behaviour:**

Void/refund operations are permitted offline for same-session sales (the data is local). Cross-session refunds that require server-side balance lookups show a warning: "Full refund history requires connectivity. Showing local session data only."

**Error states:**

- No reason code selected: Confirm button disabled. Dropdown label turns red.
- Attempting to refund more than the original sale amount: The refund total is capped at the original total. Checkboxes for items already refunded are disabled.
- Attempting a void on a session that has already been closed: A manager PIN is required. Inline prompt: "Enter manager PIN to void a closed-session sale."

**Android vs Web differences:**

- Web displays the item list as a data table with checkboxes in the first column.
- Android uses a scrollable list with trailing checkboxes.
- Web shows an inline receipt preview on the right panel after confirmation.
