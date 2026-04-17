---
project: Maduuka
document: UX Specification — F-005 through F-010 (Finance, HR, Dashboard, Settings)
version: 1.0
date: 2026-04-05
author: Peter Bamuhigire · Chwezi Core Systems
status: Draft
---

# UX Specification: Finance, HR, Dashboard, and Settings

---

## F-005: Expenses and Petty Cash

### Screen E-01: Expense Entry Screen

**Primary user:** Agnes (Cashier) for petty cash; Grace (Accountant) for review

**Entry point:** Expenses → New Expense (FAB on Android, "Add Expense" button on Web).

**Layout description:**

A single-column form. Fields in order:

1. Amount: a large numeric input field (64 dp height on Android, 48 px on Web). Auto-focused on screen open. Currency symbol shown as a non-editable prefix. An "Extract from photo" icon button on the trailing edge triggers the OCR flow (see below).
2. Date: date picker, defaults to today.
3. Category: a searchable dropdown of custom expense categories. A "+" link at the bottom of the dropdown list opens an inline "Add Category" field for new categories without leaving the screen.
4. Payment Method: a segmented control — Cash (Petty Cash) / MTN MoMo / Airtel Money / Bank.
5. Paid To: text field for vendor/payee name.
6. Description: multi-line text field (3 lines visible, expandable).
7. Tax Deductible: a toggle switch (off by default).
8. Receipt Photo: a tap area showing either a placeholder ("Tap to attach receipt photo") or a thumbnail of the attached photo. Tapping opens the camera (Android) or file picker (Web).

**OCR Flow:**

When the user taps "Extract from photo," the camera opens. After capture, the image is processed locally (Android ML Kit). The OCR result populates the Amount field and the Paid To field if extracted with sufficient confidence (≥ 80%). Extracted values are shown with an amber "OCR — please verify" label. The user must confirm or correct them. The original photo is attached automatically.

Below the form: "Save Expense" button (primary, full width).

**If expense amount exceeds the approval threshold (configurable):** The button label changes to "Submit for Approval." A blue info banner below the amount field reads: "This expense requires manager approval."

**Key interactions:**

- Saving a below-threshold expense posts immediately to the GL and updates the petty cash float.
- Saving an above-threshold expense creates a pending record visible in the Expense Approval Queue.

**Offline behaviour:** Expenses can be entered offline. OCR works offline (on-device). Receipt photos are stored locally and uploaded on connectivity restore.

**Error states:**

- Amount field empty: "Save Expense" disabled. Inline error: "Enter an amount."
- Category not selected: Inline error: "Select or add a category."
- Amount exceeds petty cash float: Amber warning inline: "This amount exceeds the available petty cash float of [amount]. You can still record this expense, but the float will go negative."

**Android vs Web differences:**

- Camera capture for receipt photo is native on Android.
- Web uses file upload (drag-and-drop or file picker). OCR is server-side for Web (uploaded image processed by the backend).

---

### Screen E-02: Expense Approval Queue

**Primary user:** Robert (Business Owner), Grace (Accountant) with approval permission

**Entry point:** Dashboard → Pending Approvals → Expenses, or Expenses → Approval Queue.

**Layout description:**

A list of pending expense records. Each row shows: submitter name, date, amount (in bold), category, and a "View" button. Rows are sorted by submission date, oldest first.

Above the list: a summary strip — "Pending: [count] expenses totalling [amount]."

Tapping a row or "View" expands the row (Android) or opens a side panel (Web) showing the full expense detail including the receipt photo thumbnail.

Row action buttons (shown on expansion): "Approve" (green) and "Reject" (red). Both require a comment field (optional for approval, mandatory for rejection). After action, the row is removed from the list with a slide-out animation.

**Offline behaviour:** The approval queue requires connectivity to load server-pending items. A banner informs the user if offline.

---

### Screen E-03: Petty Cash Float Screen

**Primary user:** Agnes (Cashier), Robert (Business Owner)

**Entry point:** Expenses → Petty Cash.

**Layout description:**

A summary card at the top: "Current Float: [amount]" in large text (24 sp), with the last-updated timestamp below.

Below the card: a list of recent petty cash movements (disbursements and top-ups). Each row: date, description, amount (signed), and balance after.

Two action buttons below the summary card:
- "Top Up Float" (primary): opens a modal — amount input, payment method (Cash / Bank Transfer), notes. On confirm, adds a positive movement to the float.
- "Disburse" (secondary): opens the Expense Entry screen pre-populated with Payment Method = Cash (Petty Cash).

**Offline behaviour:** Float balance shown from local cache. Top-up and disburse operations are queued offline.

---

## F-006: Financial Accounts and Cash Flow

### Screen FA-01: Account Dashboard

**Primary user:** Robert (Business Owner), Grace (Accountant)

**Entry point:** Finance → Accounts from the sidebar (Web) or More tab (Android).

**Layout description:**

A card-based layout. Each payment account (Cash Till, MTN MoMo, Airtel Money, Bank, SACCO) is shown as a card:

- Account name (bold, 16 sp)
- Account type label (secondary, 12 sp)
- Current balance (24 sp, bold, colour-coded: green if positive, red if negative)
- Last transaction: "[description] — [time ago]" in 12 sp secondary text
- "View Transactions" link at the bottom of the card

Cards are arranged in a vertically scrollable list on Android. On Web, they are arranged in a 3-column grid (2-column on medium viewports).

Below the cards: a "Cash Flow Summary" card showing a 2-row comparison:
- Total Inflows (today): [amount] in green
- Total Outflows (today): [amount] in red
- Net Position: [amount], colour-coded

A date range selector allows switching the summary between Today, This Week, and This Month.

"Transfer Between Accounts" button (secondary, bottom of screen) navigates to the Cash Transfer screen.

**Offline behaviour:** Account balances loaded from local cache with last-sync timestamp. Transfer initiation requires connectivity.

---

### Screen FA-02: Account Transaction Log

**Primary user:** Grace (Accountant)

**Entry point:** Account Dashboard → "View Transactions" on any account card.

**Layout description:**

Header: account name. Date range picker (defaults to last 30 days).

A chronological list of transactions. Each row:
- Date and time (12 sp, secondary)
- Description (14 sp, bold, 2 lines max)
- Reference number (12 sp, monospace, secondary)
- Amount: right-aligned, green for credits, red for debits
- Running balance: right-aligned, 12 sp, secondary

A summary strip at the top: "Opening Balance: [amount] | Closing Balance: [amount] | Net: [amount]."

Export button (Web): exports the filtered log as CSV.

**Offline behaviour:** Loads from local cache for recent transactions (last 30 days). Older transactions require connectivity.

---

### Screen FA-03: Bank Reconciliation Workflow

**Primary user:** Grace (Accountant)

**Entry point:** Finance → Bank Reconciliation → New Reconciliation.

**Layout description:**

A multi-step process presented as a single scrollable screen with clear step dividers.

**Step 1: Import Bank Statement**

A file upload area (Web): "Drop your bank statement CSV here or click to browse." Accepted format: CSV. A format guide link shows the expected column structure. Android: file picker for CSV.

On upload, the system parses the CSV and shows a preview of detected transactions (date, description, amount).

**Step 2: Auto-Match**

The system automatically matches bank statement lines to Maduuka transactions using date, amount, and description similarity. Matched pairs are shown in a two-column table:
- Left column: Bank statement line
- Right column: Maduuka transaction

Each row has a match confidence badge: "Auto-matched" (green) or "Review Required" (amber). The user can unmatch any row by tapping an unlink icon.

**Step 3: Manual Match**

Unmatched bank lines and unmatched Maduuka transactions are shown in two side-by-side lists. The user drags a bank line onto a Maduuka transaction to create a manual match (Web). On Android, the user selects a bank line, then selects the matching Maduuka transaction from a list.

For bank lines with no corresponding Maduuka transaction: a "Create Missing Transaction" option allows the user to record the transaction directly from this screen.

**Step 4: Reconciliation Summary**

A summary showing: Matched items, Unmatched bank items, Unmatched Maduuka items, Net difference. An "Approve Reconciliation" button is available when the net difference is zero (or within a configurable tolerance). If a difference remains, a "Mark as Reconciled with Difference" option is available with a mandatory notes field.

---

### Screen FA-04: Cash Transfer Screen

**Primary user:** Robert (Business Owner), Grace (Accountant)

**Entry point:** Finance → Accounts → Transfer Between Accounts.

**Layout description:**

A simple form:
1. From Account: dropdown of configured accounts.
2. To Account: dropdown (excludes From Account selection).
3. Amount: numeric input.
4. Date: date picker.
5. Notes: optional text field.
6. "Transfer" button (primary, full width).

After confirmation, both account balances update immediately. The transfer is recorded as two movements (one debit, one credit) in the transaction log.

---

## F-007: Sales Reports

### Screen R-01: Report Hub

**Primary user:** Robert (Business Owner), Grace (Accountant)

**Entry point:** "Reports" in the bottom tab bar (Android) or sidebar (Web).

**Layout description:**

A categorised list of available reports. Categories:

- **Sales:** Daily Sales, Sales by Product, Sales by Category, Sales by Cashier, Sales by Branch, Top Sellers, Gross Margin.
- **Stock:** Stock Levels, Stock Movement, Expiry Alerts, Stock Valuation.
- **Finance:** Cash Flow Summary, Account Statement, Debtors Ageing, Creditors Ageing.
- **HR:** Payroll Summary, Leave Summary, Attendance Summary.
- **Audit:** Voids and Refunds, Receipt Gap Report, Expense Audit.

Each report is shown as a row (Android) or card (Web) with the report name and a short description (1 line). Tapping navigates to the Report View screen (Screen R-02) for that report.

A search field at the top allows filtering the report list by name.

---

### Screen R-02: Report View

**Primary user:** Robert (Business Owner), Grace (Accountant)

**Entry point:** Tapping any report in the Report Hub.

**Layout description:**

Header: report name. A filter bar below the header contains (report-dependent controls):
- Date range picker (presets: Today, Yesterday, This Week, Last Week, This Month, Last Month, Custom)
- Branch selector (if multi-branch)
- Category filter (for product reports)
- Cashier filter (for sales-by-cashier reports)

A "Apply Filters" button (or auto-apply with 500 ms debounce on Web).

The report body is divided into two zones:
- **Chart zone** (top, approximately 200 dp / px height): a bar chart or line chart appropriate to the report type. Charts are rendered using MPAndroidChart (Android) or Chart.js (Web). On low-end devices (DC-004), charts are rendered as static SVG images if animation causes frame drops.
- **Table zone** (below chart): a data table of the report's detail rows. Sortable columns. On Android, the table is horizontally scrollable if it exceeds the screen width.

Action bar above the table: Export CSV, Export PDF, Print, Schedule Report (navigates to Screen R-04), Share (Android share intent).

**Offline behaviour:** Reports load from local cache for the last 30 days. A banner indicates "Report data is as of last sync. Current data requires connectivity."

---

### Screen R-03: Custom Report Builder (Web Only)

**Primary user:** Grace (Accountant)

**Entry point:** Reports → Custom Report Builder.

**Layout description:**

A two-panel interface on wide viewports:

- **Left panel (filter builder, 320 px):** A list of available filter dimensions (Date Range, Branch, Product, Category, Customer, Cashier, Payment Method, Transaction Type). The user adds filters by clicking a "+" button beside each dimension. Added filters appear as filter chips above the dimension list with configured values.
- **Right panel (preview):** A live preview of the report data table as filters are applied (data refreshes on each filter change, debounced 800 ms). A "Run Report" button forces a full refresh.

Below the panels: "Save as Named Report" (saves to the Report Hub under a "Custom" category) and "Export" buttons.

This screen is Web-only per DC-001 compatibility scope (the feature is available on Web; Android provides the standard Report View with its filter bar for the same outputs).

---

### Screen R-04: Scheduled Report Setup

**Primary user:** Robert (Business Owner), Grace (Accountant)

**Entry point:** Report View → "Schedule Report."

**Layout description:**

A form modal (Web) or full screen (Android):

1. Report: pre-filled from the current report context.
2. Frequency: Daily / Weekly / Monthly (segmented control).
3. Day of Week (shown only for Weekly): day picker chips.
4. Day of Month (shown only for Monthly): numeric input 1–28.
5. Delivery Time: time picker.
6. Format: PDF / CSV / Both.
7. Recipients: a multi-value email input field. The user adds email addresses one at a time.
8. "Save Schedule" button.

Saved schedules appear in a list accessible from Reports → Scheduled Reports. Each scheduled report row shows the report name, frequency, next run time, and a toggle to enable/disable.

---

## F-008: HR and Payroll

### Screen H-01: Staff List

**Primary user:** Amara (HR Manager)

**Entry point:** HR from the sidebar (Web) or More tab (Android).

**Layout description:**

Search field at top. Filter chips: All / Active / On Leave / Resigned.

Each staff row shows: staff photo avatar (40 dp circle), full name, job title, department, and an employment type badge (Full-time, Part-time, Contract). Tapping a row navigates to the Staff Profile screen.

FAB (Android) / "Add Staff" button (Web) opens the staff creation form.

---

### Screen H-02: Staff Profile Screen

**Primary user:** Amara (HR Manager)

**Entry point:** Tapping a staff row in the Staff List.

**Layout description:**

A tabbed profile screen. Header card (always visible): staff photo (64 dp circle), full name, job title, department, branch, employment type badge, and hire date.

Tabs:

- **Personal:** Name, date of birth, NIN, phone, email, emergency contact, physical address.
- **Contract:** Employment type, department, job title, branch, start date, end date (for contract staff), renewal reminder date.
- **Salary:** Salary structure — earnings (basic salary, allowances) and deductions (NSSF employee, PAYE, LST, staff loan deduction). Monthly net pay shown as a summary line. "Edit Salary Structure" is restricted to Amara (HR Manager) and above.
- **Leave:** Leave entitlements per type (Annual, Sick, Maternity, etc.), days used, days remaining. A list of leave requests with status badges.
- **Attendance:** A calendar heatmap showing attendance for the current month. Below: a list of daily attendance records (clock-in time, clock-out time, hours worked).
- **Disciplinary:** A list of disciplinary records (date, category, description, resolution). "Add Record" restricted to HR Manager.

---

### Screen H-03: Leave Request Flow

**Step 1: Staff Leave Application (Android)**

**Primary user:** Staff member applying for leave

**Entry point:** HR → My Leave → Request Leave.

**Layout description:**

A form with:
1. Leave Type: dropdown of configured leave types.
2. From Date: date picker.
3. To Date: date picker. Duration (working days) is auto-calculated and shown below: "Duration: 5 working days."
4. Reason: multi-line text field (optional for most types; mandatory for sick leave).
5. Handover Note: text field (optional).
6. "Submit Request" button (primary).

After submission, the staff member sees a pending status badge and receives a push notification when the request is approved or rejected.

**Step 2: Manager Approval**

**Entry point:** Dashboard → Pending Approvals → Leave Requests (manager view).

**Layout description:**

A list of pending leave requests. Each row: staff name, leave type, dates, duration, and reason summary. Row actions: "Approve" (green check) and "Reject" (red X). Both trigger a comment modal (comment optional for approval, mandatory for rejection). Approved requests send a push notification and WhatsApp message to the staff member.

---

### Screen H-04: Payroll Run Screen

**Primary user:** Amara (HR Manager)

**Entry point:** HR → Payroll → Run Payroll.

**Layout description:**

A three-step process.

**Step 1: Compute**

Select payroll period (year + month selector). Branch / All Branches selector. "Compute Payroll" button. After computation, a summary table shows one row per staff member: Name, Gross Pay, Deductions (NSSF, PAYE, LST, Loan), Net Pay. Each row is expandable to show the full salary structure breakdown.

Rows with computation warnings (e.g., missing NIN, incomplete salary structure) are shown with an amber warning icon. These must be resolved before approval.

**Step 2: Review**

All computed payslips are shown. The user can edit individual payslip lines at this stage (manager-level permission required). Edits are tracked with a "Modified" badge on that row.

Below the table: aggregate totals — Total Gross, Total Deductions, Total Net, Total Employer NSSF.

**Step 3: Approve**

"Approve Payroll" button (primary, full width, brand colour). A confirmation dialog: "Approve payroll for [period]? Payslips will be locked after approval." (BR-012).

After approval: "Generate Bank File" button appears. The user selects the bank from a dropdown (Centenary, Stanbic, ABSA, KCB, Equity, Dfcu) and downloads a bank-format CSV file. A "Send Payslips" button sends payslips via WhatsApp and/or email to all staff.

---

### Screen H-05: Payslip View

**Primary user:** Staff member (view own), Amara (HR Manager) for all

**Entry point:** HR → Payroll → [Month] → [Staff Name] or notification tap.

**Layout description:**

A read-only formatted payslip view:

- Header: business logo, business name, "PAYSLIP" title, period.
- Employee section: name, NIN, job title, department, branch.
- Earnings table: each earning type with its amount.
- Deductions table: each deduction type with its amount.
- Summary: Gross Pay, Total Deductions, Net Pay in bold.
- EFRIS fiscal indicator (DC-006) below the summary (shown even if EFRIS is not active — greyed placeholder).

Action buttons at the bottom:
- "Send via WhatsApp" (primary)
- "Send via Email" (secondary)
- "Download PDF" (secondary)

**Offline behaviour:** Previously loaded payslips are cached for offline viewing. Sending requires connectivity.

---

## F-009: Dashboard

### Screen D-01: Dashboard Layout

**Primary user:** Robert (Business Owner), Agnes (Cashier — limited view)

**Entry point:** "Dashboard" in the bottom tab bar (Android) or the root URL on Web.

**Layout description (Android):**

A vertically scrollable screen. Sections from top to bottom:

1. **Top bar:** Business name, branch indicator, and a notification bell icon (with unread count badge).
2. **KPI Cards row:** A horizontal scrollable row of cards (each 140 dp wide, 80 dp tall). Cards: Today's Revenue, Transaction Count, Outstanding Credit, Cash Position. Each card shows the KPI label (12 sp), the value (20 sp, bold), and a trend indicator (up/down arrow with a percentage change vs yesterday, in green or red).
3. **Business Health Score widget:** A card showing the health score (see Screen D-03).
4. **Revenue Comparison chart:** A bar chart showing today vs yesterday and this week vs last week. Two grouped bar pairs. Rendered as a static bar chart — no hover tooltips on Android (hover requires mouse).
5. **Recent Transactions list:** Last 5 transactions. Each row: time, description, amount. "View All" link navigates to the full sales report.
6. **Low Stock Alerts:** A card listing up to 3 low-stock products with a "View All" link. If no low-stock items: "All stock levels are healthy" in green.
7. **Pending Approvals:** A card listing counts of pending items (Expenses: 2, Leave Requests: 1, Stock Adjustments: 0). Tapping each navigates to the respective approval queue.
8. **Quick Action Shortcuts:** A 2-column grid of action buttons: New Sale, Add Expense, Add Product, Transfer Stock, Request Leave, Record Payment. Each is a card with an icon and label.

**Layout description (Web):**

A widget grid (CSS Grid, 3-column on wide viewports, 2-column on medium). Widgets are repositionable by drag-and-drop (logged-in user preference saved server-side). Widgets auto-refresh every 2 minutes.

**Offline behaviour:** Dashboard loads from local cache. KPIs show last-synced values with a "Last updated [time ago]" subtitle. The dashboard is never blocked by offline status.

---

### Screen D-02: Business Health Score Widget

**Primary user:** Robert (Business Owner)

**Entry point:** Embedded in the Dashboard; also tappable to expand.

**Layout description:**

A card with:
- "Business Health Score" title
- A large RAG indicator: a coloured circular badge (green = healthy, amber = attention, red = critical) with a score value (e.g., "76 / 100") inside it
- Below the badge: a 4-row breakdown table

| Metric | Value | Status |
|---|---|---|
| Gross Margin % | 28% | Amber |
| Expense Ratio | 18% | Green |
| Stock Turnover | 4.2x | Green |
| Collection Rate | 72% | Red |

Each status cell uses the colour convention (Section 2.8 of Principles document). The collection rate cell has a red badge — this is the dragger pulling the overall score down.

Tapping the card expands it to a full-screen detail view showing the metric definitions, thresholds, and 30-day trend sparklines for each metric.

The score thresholds are:
- Green: score ≥ 70
- Amber: score 40–69
- Red: score < 40

The score is a weighted average: Gross Margin (30%), Expense Ratio (20%), Stock Turnover (25%), Collection Rate (25%).

---

### Screen D-03: Branch Switcher

**Primary user:** Robert (Business Owner — multi-branch)

**Entry point:** Tapping the branch indicator in the Dashboard top bar or POS top bar.

**Layout description:**

A bottom sheet (Android) or dropdown (Web). Lists all branches the user has access to. The current branch has a checkmark. Tapping a different branch switches the active context — all subsequent data (stock, sales, staff) is scoped to the selected branch. A confirmation step is shown only if there is an active POS session at the current branch: "You have an open POS session at [Branch]. Switch branch? Your session will remain open."

---

### Screen D-04: Android Home Screen Widget

**Primary user:** Robert (Business Owner)

**Entry point:** Android long-press on home screen → Widgets → Maduuka.

**Layout description:**

A 4 x 2 grid widget (standard Android widget dimensions). Contents:
- Business logo (small, top-left)
- "Today's Revenue" label and value (large, centre)
- "Transactions" count (smaller, below revenue)
- Last updated timestamp (bottom-right, 10 sp)

The widget refreshes every 30 minutes via WorkManager. Tapping the widget launches the Maduuka Dashboard screen. The widget does not require the app to be running in the background to display the last cached values.

---

## F-010: Settings and Configuration

### Screen ST-01: Business Profile Screen

**Primary user:** Robert (Business Owner)

**Entry point:** Settings → Business Profile.

**Layout description:**

A form screen with: Business Name, Logo (image upload with crop), Physical Address, TIN (Uganda Tax Identification Number), Phone, Email, Financial Year Start Month (dropdown, defaults to July for Uganda), Currency (searchable dropdown of world currencies — no hardcoded UGX per DC-005), Date Format, Number Format, Language (per user: English / Swahili).

"Save Changes" button at the bottom.

The currency selection updates the currency symbol displayed everywhere in the application immediately upon save.

---

### Screen ST-02: Receipt Customisation Screen

**Primary user:** Robert (Business Owner)

**Entry point:** Settings → Receipt Customisation.

**Layout description:**

A split-screen: left side (or top on Android) is the configuration form; right side (or bottom on Android) is a live receipt preview that updates in real time as settings change.

Configuration fields:
- Receipt Header (multi-line text, e.g., business name, slogan)
- Logo: toggle show/hide; logo is sourced from Business Profile.
- Business Address on receipt: toggle
- TIN on receipt: toggle
- Footer message (multi-line text, e.g., "Thank you for shopping with us!")
- Show itemised tax breakdown: toggle
- EFRIS fiscal indicator position: Top / Bottom (greyed out if EFRIS not active, but the indicator is shown in the preview per DC-006)
- Receipt number format: prefix field + numeric counter example shown inline

The receipt preview shows a to-scale mockup of the 80mm thermal receipt format.

---

### Screen ST-03: Tax Settings Screen

**Primary user:** Robert (Business Owner), Grace (Accountant)

**Entry point:** Settings → Tax.

**Layout description:**

Two sections:

**General Tax Settings:**
- Tax mode: Tax Inclusive / Tax Exclusive (radio buttons). A brief explanation beneath: "Inclusive: prices shown in POS already include tax. Exclusive: tax is added at checkout."
- Default Tax Rate: numeric input (defaults to 18% for Uganda VAT).

**Product Tax Categories:**
A table listing tax categories: Standard Rate (18%), Zero-Rated (0%), Exempt. A "Add Custom Category" button allows adding jurisdiction-specific rates (e.g., hotel levy). Each category row shows its rate and an example product use case.

A link to official Uganda Revenue Authority VAT documentation is shown below the table.

---

### Screen ST-04: Subscription Management Screen

**Primary user:** Robert (Business Owner)

**Entry point:** Settings → Subscription.

**Layout description:**

Current Plan card at the top:
- Plan name (bold, 18 sp)
- Price and billing cycle
- Features included (bulleted list, 3 key features)
- Next billing date

Below: a "Compare Plans" section showing all available plans side by side (Web: 3-column card grid; Android: horizontally scrollable plan cards). Each plan card shows name, price, and a "Upgrade" or "Current Plan" button.

Below the plans: account management links:
- "Download Invoice" (for last payment receipt)
- "Update Payment Method"
- "Cancel Subscription" (destructive — opens a retention flow before cancellation)

---

### Screen ST-05: Connected Devices Screen

**Primary user:** Robert (Business Owner)

**Entry point:** Settings → Security → Connected Devices.

**Layout description:**

A list of all active sessions / connected devices. Each row shows:
- Device type icon (phone, tablet, desktop browser)
- Device name / browser (e.g., "Chrome on Windows 11")
- Location (city, country if available from IP)
- Last active: "[time ago]"
- "Current Device" badge on the current session row
- "Revoke" button (red text) on all non-current rows

A "Revoke All Other Devices" button at the bottom (destructive — requires password confirmation).

---

### Screen ST-06: 2FA Setup Flow

**Primary user:** Robert (Business Owner)

**Entry point:** Settings → Security → Two-Factor Authentication.

**Step 1: Introduction**

A full-screen explanation of 2FA: "Add an extra layer of security. Each login will require a code from your authenticator app." A primary "Enable 2FA" button proceeds to Step 2. A "Learn More" link is available.

**Step 2: QR Code**

A generated QR code (200 x 200 dp on Android, 200 x 200 px on Web) and a manual setup key below it (monospace, copyable). Instruction: "Scan this QR code with your authenticator app (e.g., Google Authenticator, Authy)."

A "Next" button proceeds to Step 3. The QR code is shown only once. The user cannot proceed to Step 3 without tapping "Next" — the QR code is not auto-advanced.

**Step 3: Verification**

A 6-digit TOTP entry field (6 individual character boxes, auto-advance on each digit entry). Instruction: "Enter the code from your authenticator app to confirm setup."

"Verify and Enable" button. If the TOTP code is valid, 2FA is enabled and the user is shown a success screen with backup codes (10 codes, displayed as a list, with a "Download Backup Codes" button). If invalid: inline error "Incorrect code. Try again." The field clears and refocuses.

**Step 4: Backup Codes**

10 one-time backup codes displayed in a 2-column grid (monospace, 5 codes per column). A "Download Codes" button generates a PDF. A mandatory checkbox: "I have saved my backup codes" must be checked before the "Finish" button activates.

After 2FA is enabled, the Settings → Security page shows: "2FA is active. Last used [date]." with a "Disable 2FA" option (requires current TOTP to confirm).
