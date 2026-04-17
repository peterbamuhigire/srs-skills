# Module Wireframe Specifications

This section defines the layout, key UI elements, and interaction behaviour for the 6 primary screens of Longhorn ERP. These are wireframe-level specifications — they define structure and interaction, not visual polish.

---

## 1. Dashboard (Home)

### 1.1 Layout

```
┌──────────────────────────────────────────────────────────────────────────┐
│ TOP BAR: Breadcrumb | Tenant Name + Branch | Bell | Avatar               │
├──────────────────────────────────────────────────────────────────────────┤
│ [KPI: Revenue MTD]  [KPI: Outstanding Invoices]  [KPI: Stock Value]  [KPI: Payroll MTD] │
├────────────────────────────────────────┬─────────────────────────────────┤
│ Revenue Chart (last 12 months)         │ Recent Activity Feed            │
│ [ApexCharts bar chart — full width]    │ ─────────────────────────────── │
│                                        │ [Timestamped event list]        │
├────────────────────────────────────────│─────────────────────────────────┤
│ Top Customers Table                    │ Quick Actions                   │
│ [DataTable — 5 rows, no pagination]    │ [+ New Invoice]                 │
│                                        │ [+ New Purchase Order]          │
│                                        │ [+ New Employee]                │
└────────────────────────────────────────┴─────────────────────────────────┘
```

### 1.2 KPI Card Specification

Each KPI card is 25% width (minus gutters), 96 px tall, white background, 1 px border (#E2E8F0), border-radius 8 px.

| Zone | Content |
|---|---|
| Top-left | Metric label (13 px, muted #6B7280) |
| Centre-left | Metric value (28 px, 700 weight, Primary Navy) |
| Top-right | Icon (28 px, Steel Blue) |
| Bottom-left | Period-over-period delta (12 px; green if positive, red if negative) |

KPI cards link to their relevant list views on click (Revenue MTD → AR Invoice list filtered to current month; Outstanding Invoices → AR Invoice list filtered to unpaid; Stock Value → Inventory valuation report; Payroll MTD → Payroll run list for current month).

### 1.3 Revenue Chart

- Library: ApexCharts, chart type: bar.
- X-axis: 12 month labels (abbreviated: Jan, Feb, …).
- Y-axis: currency formatted in tenant's base currency (UGX by default, abbreviated: "1.2M", "850K").
- Tooltip: shows full month name + exact amount on hover.
- Current month bar rendered in Accent Blue (#4472C4); previous months in Steel Blue (#2E5D8A) at 70% opacity.
- Chart height: 240 px. Responsive: redraws on window resize.

### 1.4 Recent Activity Feed

- Displays the 10 most recent system events for the authenticated user's branch.
- Each entry: event icon (16 px) + description (13 px) + relative timestamp (12 px, muted).
- Examples: "Invoice INV-2026-00123 posted — 5 min ago", "Purchase Order PO-2026-00045 approved — 2 h ago".
- "View all activity" link at the bottom navigates to the full audit log filtered to the current user's branch.
- Feed refreshes every 60 seconds via AJAX poll.

### 1.5 Quick Actions

Three primary shortcut buttons (140 px wide, 44 px tall, Primary Navy) that navigate directly to the new-record form for Invoice, Purchase Order, and Employee respectively. Shortcut buttons respect module visibility: if the authenticated user does not have access to a module, its Quick Action button does not render.

---

## 2. GL Journal Entry

### 2.1 Layout

```
FORM HEADER (single row, 4 fields):
[Date*]  [Reference (auto)]  [Narration*]  [Accounting Period (locked)]

LINES TABLE:
┌───────────────┬────────────┬──────────────┬──────────┬──────────┬──────┐
│ Account*      │ Cost Centre│ Description  │ Debit    │ Credit   │ [×]  │
├───────────────┼────────────┼──────────────┼──────────┼──────────┼──────┤
│ [Select2]     │ [Select2]  │ [text input] │ [amount] │ [amount] │ [×]  │
│ [Select2]     │ [Select2]  │ [text input] │ [amount] │ [amount] │ [×]  │
│ [+ Add Line]  │            │              │          │          │      │
└───────────────┴────────────┴──────────────┴──────────┴──────────┴──────┘

FOOTER:
                                      Total Debit: [sum]
                                      Total Credit: [sum]
                                      Difference: [sum — red if ≠ 0]

[Cancel]                                           [Save Draft]  [Post ▶]
```

### 2.2 Form Header Fields

| Field | Component | Behaviour |
|---|---|---|
| Date | Flatpickr | Defaults to today; cannot be outside the active accounting period |
| Reference | Text input (read-only) | Auto-generated on page load: `JNL-YYYY-NNNNN`; user may override |
| Narration | Text input | Required; max 200 characters; character counter displayed |
| Accounting Period | Text input (read-only) | Shows current open period (e.g., "April 2026"); locked — user cannot edit; link to Period Management if wrong period |

### 2.3 Lines Table Interaction

- Minimum 2 lines required to post.
- Account field: Select2 bound to Chart of Accounts; grouped by account type; search by code or name.
- Debit and Credit are mutually exclusive per line: entering a value in Debit clears Credit and vice versa.
- Row deletion: clicking [×] removes the line immediately; if only 2 lines remain, a SweetAlert2 confirmation fires ("Removing this line will leave only 1 line. Journal entries require at least 2 lines.").
- **+ Add Line** appends a new empty row and focuses the Account field of the new row.
- Keyboard navigation: Tab moves through cells left-to-right; pressing Enter on the Credit cell of the last line calls **+ Add Line** automatically.

### 2.4 Footer Totals

- Total Debit and Total Credit recalculate on every `input` event in any amount field.
- Difference = Total Debit − Total Credit.
- When Difference ≠ 0: Difference cell background #FEE2E2, text #DC2626, bold.
- When Difference = 0: Difference cell text #16A34A, bold, "Balanced ✓".
- **Post** button: disabled (opacity 0.5, `cursor: not-allowed`) while Difference ≠ 0. Enabled only when Difference = 0 and all required fields are filled.

---

## 3. Sales Invoice

### 3.1 Layout

```
FORM HEADER (2-row grid):
Row 1: [Customer*]  [Invoice Date*]  [Due Date*]  [Reference]
Row 2: [Currency*]  [Exchange Rate]  [Sales Rep]  [Status: Draft badge]

LINES TABLE:
┌──────────────┬──────────────┬─────┬────────────┬──────────┬───────┬────────────┬──────┐
│ Item*        │ Description  │ Qty │ Unit Price │ Disc %   │ VAT % │ Line Total │ [×]  │
├──────────────┼──────────────┼─────┼────────────┼──────────┼───────┼────────────┼──────┤
│ [Select2]    │ [text]       │[num]│ [amount]   │ [0–100]  │ [sel] │ [calc]     │ [×]  │
│ [+ Add Line] │              │     │            │          │       │            │      │
└──────────────┴──────────────┴─────┴────────────┴──────────┴───────┴────────────┴──────┘

FOOTER SUMMARY:                     Subtotal:        [calc]
                                    VAT:             [calc]
                                    Total:           [calc — 20px bold]

[Cancel]   [Save Draft]   [Preview PDF]   [Submit to EFRIS]   [Post ▶]
```

### 3.2 Header Field Behaviour

| Field | Component | Behaviour |
|---|---|---|
| Customer | Select2 (remote) | Searches customer name or code; on select, auto-populates Currency, Exchange Rate, Sales Rep, and payment terms |
| Invoice Date | Flatpickr | Defaults to today; must be within the open AR period |
| Due Date | Flatpickr | Auto-calculated from Invoice Date + customer payment terms; user may override |
| Currency | Select2 | Defaults from customer record; changing currency clears all line prices |
| Exchange Rate | Numeric input | Visible only when Currency ≠ base currency; auto-populated from daily rate table; user may override |

### 3.3 Lines Table Calculation

Line Total = (Unit Price × Qty) × (1 − Disc% / 100)

VAT amount per line = Line Total × (VAT% / 100)

Footer Subtotal = sum of all Line Totals (pre-VAT)

Footer VAT = sum of all per-line VAT amounts

Footer Total = Subtotal + VAT

All calculations run on every `input` event. Currency values display 2 decimal places with thousand separators.

### 3.4 EFRIS Integration

The **Submit to EFRIS** button is visible only when the tenant has EFRIS (Uganda Revenue Authority e-invoicing) enabled in their configuration. It is disabled until the invoice status is Posted. Clicking it fires a confirmation dialog and then calls the EFRIS submission API endpoint. On success, the invoice gains an EFRIS verification code displayed in the invoice header.

---

## 4. POS Terminal (Tablet-Optimised)

### 4.1 Layout (Landscape, ≥ 768 px)

```
┌─────────────────────────────┬───────────────────────────────────┐
│ ITEM GRID (60% width)       │ CART PANEL (40% width)            │
│                             │                                    │
│ [Search bar top]            │ [Cart header: Customer / Walk-in] │
│                             │ ─────────────────────────────────  │
│ [Item Card]  [Item Card]    │ Item Name         Qty  [−][+]  [×] │
│ [Item Card]  [Item Card]    │ Item Name         Qty  [−][+]  [×] │
│ [Item Card]  [Item Card]    │ ─────────────────────────────────  │
│ [Category Tabs below grid]  │ Subtotal:          UGX XXXXXXXXX  │
│                             │ Discount:          UGX XXXXXXXXX  │
│                             │ Total:             UGX XXXXXXXXX  │
│                             │ ─────────────────────────────────  │
│                             │ [CASH]  [MoMo]  [Card]            │
│                             │ [CHARGE CUSTOMER]                  │
└─────────────────────────────┴───────────────────────────────────┘
```

### 4.2 Item Grid

- Each item card: 120 px × 140 px, border-radius 8 px, white background, 1 px border.
- Card contents: item image (60 px × 60 px, centred, object-fit: cover), item name (2-line max, 12 px), price (14 px, 600 weight, Primary Navy).
- Tapping a card adds 1 unit to the cart and applies a brief scale animation (transform: scale(0.95) for 100 ms) as tactile feedback.
- Items out of stock display a "Out of Stock" overlay (semi-transparent grey) and are non-tappable.
- Search bar: full-width text input at the top of the item grid; filters items in real time (client-side filter on currently loaded page).
- Category tabs below the grid: filters the item grid to the selected category. "All" tab is always first.

### 4.3 Cart Panel

- Quantity controls: [−] and [+] buttons, 36 px × 36 px touch targets (minimum WCAG touch target size). Tapping [−] when quantity = 1 removes the line after a 500 ms long-press confirmation (prevents accidental removal).
- Discount: flat amount or percentage, switchable via a toggle. Applied to the cart total, not per-line.
- Customer assignment: "Walk-in" by default. Tapping "Customer / Walk-in" opens a modal with a customer search (Select2). Assigning a customer enables the "Charge to Account" option.
- Payment buttons (Cash, MoMo, Card) are large (full-width, 52 px tall). Selecting a payment method highlights it in Accent Blue. Multiple payment methods may be selected for split payment.
- **Charge Customer** button is enabled only when a customer is assigned and payment method is "Account".
- On successful transaction: SweetAlert2 success dialog with transaction total and change due (if Cash). "Print Receipt" and "WhatsApp Receipt" buttons in the dialog footer.

### 4.4 Receipt Options

- Print: sends to the configured session receipt printer (ESC/POS thermal) via a local print agent.
- WhatsApp: opens `https://wa.me/<phone>?text=<receipt_url>` in a new tab; the receipt URL is a tenant-branded shareable receipt page.

---

## 5. HR Payroll Run

### 5.1 Wizard Structure

A 4-step wizard with a horizontal step indicator at the top of the page.

```
Step 1: Select Period & Branches  ──▶  Step 2: Preview  ──▶  Step 3: Approve  ──▶  Step 4: Post
```

The active step label is Bold, Primary Navy. Completed steps show a check icon. Future steps are muted grey and non-clickable (forward navigation is disabled; backward navigation is allowed via the **Back** button).

### 5.2 Step 1 — Select Period and Branches

Fields:

- Payroll Period (Select2 — month/year from open payroll periods)
- Branch(es) (multi-select Select2 — defaults to all branches the user has access to)
- Payroll Type (Select2 — Monthly, Bi-weekly, Supplementary)
- Run Description (text input — e.g., "April 2026 Regular Payroll")

**Next** button: validates all required fields; calls the payroll preview API; transitions to Step 2 with a loading overlay while the server calculates.

### 5.3 Step 2 — Preview

Summary cards above the table:

| Card | Value |
|---|---|
| Total Employees | Count of employees in this run |
| Total Gross Pay | Sum of all gross pay |
| Total Net Pay | Sum of all net pay |
| Total PAYE | Sum of all PAYE deductions |

Preview table columns:

| Column | Notes |
|---|---|
| Employee | Employee code + full name; clickable to expand a detail row |
| Basic Pay | |
| Allowances | Tooltip lists individual allowances on hover |
| Gross Pay | Basic + Allowances |
| PAYE | Calculated per tax band |
| NSSF | Employee + employer contributions |
| Other Deductions | Tooltip lists loan repayments, levies, etc. |
| Net Pay | Bold |
| Status | Badge: Calculated, Exception (amber if any deduction anomaly) |

Employees with an Exception status display an amber badge. The user must resolve or acknowledge all exceptions before proceeding to Step 3. An **Exceptions** tab above the table filters to exception rows only.

**Back** and **Proceed to Approve** buttons in the step footer.

### 5.4 Step 3 — Approve

Displays a read-only summary (same summary cards as Step 2 but non-editable). An approval notes text area (optional, max 500 characters) is available.

**Approve Payroll Run** button triggers a non-destructive SweetAlert2 confirmation dialog (Section 4.2 of Component Specs). On confirmation, the run status changes to "Approved".

### 5.5 Step 4 — Post to GL and Generate Payment File

Two parallel actions available after approval:

1. **Post to GL**: Creates the payroll GL journal entry (Dr: Payroll Expense accounts; Cr: Payroll Payable). On success, shows the generated journal reference.
2. **Generate Payment File**: Downloads a CSV/TXT file formatted for the tenant's configured payment bank. File format is selectable (ABSA, Stanbic, Centenary Bank, MTN MoMo Bulk). On success, shows the download link.

Both actions can be triggered independently. The step is complete when at least **Post to GL** has been executed. A completion banner replaces the action buttons once both actions are done.

---

## 6. Cooperative Intake (Offline-Capable)

### 6.1 Layout

```
TOP BAR (standard + offline badge):
[Breadcrumb]  [Intake Period: Select2]  [OFFLINE badge — amber, if no connectivity]

FARMER SEARCH:
[Scan NIN Barcode 📷]  |  [Type name or NIN ______________]  [Search]

FARMER CARD (appears after selection):
┌───────────────────────────────────────────────┐
│ Name: [Full Name]          ID: [NIN]           │
│ Group: [Group Name]        Balance: UGX [amt]  │
└───────────────────────────────────────────────┘

INTAKE FORM:
[Commodity*]  [Grade* — auto-loads unit price]  [Unit Price: UGX XXXXX (read-only)]

[Gross Weight (kg)*]   [Tare Weight (kg)*]   [Net Weight (kg): CALC — read-only, bold]

Gross Payment:  UGX [Net Weight × Unit Price — read-only, 20px bold]

DEDUCTIONS:
  Loan Balance Deduction:   UGX [auto-populated from farmer's loan balance]
  Cooperative Levy (%):     [% input — auto-calculates UGX amount]
  Total Deductions:         UGX [sum]

NET PAYMENT:
  ┌──────────────────────────────┐
  │  UGX  XXXXXXX  (28px, bold) │
  └──────────────────────────────┘

[Cancel]                            [Save Intake ▶]
```

### 6.2 Offline Mode

The Cooperative Intake screen is the only screen in Longhorn ERP with offline capability (Progressive Web App service worker + IndexedDB).

Offline behaviour rules:

- The offline indicator badge ("OFFLINE — Data will sync when connection is restored") appears in the top bar when `navigator.onLine === false`.
- Commodity, grade, and price data are pre-cached when the user opens the intake screen while online.
- Farmer records are pre-cached for the selected intake period on screen load.
- Saved intake records are written to IndexedDB and synchronised to the server automatically when connectivity is restored.
- Sync status is shown in the offline badge: "Syncing… (3 pending)" → "All synced ✓".
- If a conflict is detected during sync (same farmer-period record exists on server), the server record takes precedence and the user is notified via a warning toast.

### 6.3 Farmer Search

- Barcode scan: activates the device camera (mobile) or a USB barcode scanner input (desktop). Scanned NIN auto-populates the search field and triggers the lookup immediately.
- Text search: debounced at 400 ms; searches by NIN, farmer name, or group name; results appear in a dropdown below the field (Select2 remote mode when online; IndexedDB search when offline).
- Selecting a farmer loads the Farmer Card and clears any previous intake form data.

### 6.4 Weight and Payment Calculation

Net Weight = Gross Weight − Tare Weight (calculated on every `input` event; red text if result ≤ 0)

Gross Payment = Net Weight × Unit Price (calculated on every `input` event)

Net Payment = Gross Payment − Loan Balance Deduction − (Gross Payment × Cooperative Levy%)

All calculated fields are read-only inputs (visually distinct via a light grey background #F3F4F6). Net Payment is displayed in a prominent card (28 px, 700 weight, Primary Navy) immediately above the Save button so the farmer can see and verify the amount before the intake record is saved.
