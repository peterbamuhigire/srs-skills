# 3. Key Screen Specifications

## 3.1 POS Main Screen — S-001 (Prossy's Daily Screen)

**Screen ID:** S-001

**Panel:** Main ERP

**Primary Persona:** Prossy — Factory Gate Cashier (S4 education, basic smartphone user)

**DC-001 Requirement:** A cash sale from product search to printed receipt in ≤ 90 seconds on first attempt with no training.

### Layout

The screen is divided into two permanent panels:

- **Left panel (60% width):** Product catalogue — searchable, filterable, visual.
- **Right panel (40% width):** Active cart — items added, quantities, payment, totals.

The two panels are always visible simultaneously on screen. The cashier never navigates away from this screen during a transaction.

### Left Panel — Product Catalogue

- A prominently positioned search bar at the top (auto-focused on page load). Supports text search by product name and barcode scan (USB barcode reader input treated as keyboard input).
- Product results displayed as a grid of product cards (default view). Each card shows: product photo (80×80 px), product name, pack size, price in bold UGX format. Cards are large enough for touch interaction (minimum 100×120 px tap target).
- A list/grid toggle button is available for cashiers who prefer list view.
- Clicking a product card adds it immediately to the cart (no intermediate dialog for standard quantities). For weight-based items, a quantity entry modal appears.

### Right Panel — Cart

- Cart line items: product name, quantity (editable — tap to edit inline), unit price, line total.
- Quantity controls: plus/minus buttons beside each line item. Minimum tap target: 44×44 px.
- Remove item button (red X icon with label "Remove") on each cart row.
- Cart total (subtotal, any discount, grand total) displayed in large font at the bottom of the cart panel.
- Payment section below the total:
  - Payment type buttons: **Cash**, **MTN MoMo**, **Airtel Money**, **Cheque**, **Bank Deposit** — displayed as large toggle buttons. Multiple types can be selected for split payment.
  - For each selected payment type, an amount input field appears.
  - Change calculated and displayed automatically when cash amount exceeds total.
- **Complete Sale** button: full-width, green, `.btn-primary` style, 48px height, at the bottom of the cart panel. Disabled until payment amount ≥ total.

### Post-Sale Receipt Screen

- Immediately after sale is posted, receipt preview appears in a modal.
- Three action buttons: **Print Receipt** (80mm thermal — primary), **Send SMS**, **Send WhatsApp**.
- A **New Sale** button is prominently displayed to reset the screen for the next customer.
- The modal can be dismissed to start the next sale without printing.

### DC-001 90-Second Test Sequence

1. Cashier opens browser — POS screen loads directly (default landing page for Prossy's role). *(0 seconds)*
2. Cashier types "maize" in the search bar — results appear in ≤ 500 ms. *(5 seconds)*
3. Cashier clicks the product card — item added to cart. *(10 seconds)*
4. Cashier selects **Cash** payment type. *(15 seconds)*
5. Cashier enters cash amount received. *(20 seconds)*
6. Cashier clicks **Complete Sale**. *(25 seconds)*
7. Receipt modal appears — cashier clicks **Print Receipt**. *(30 seconds)*
8. 80mm receipt prints. *(≤ 90 seconds total — **PASS**)*

### EFRIS Integration Indicator

A small status indicator in the header of the POS screen shows the EFRIS submission status of the last transaction:

- Green dot: "EFRIS: Submitted" — FDN received.
- Orange dot: "EFRIS: Queued" — submission pending (offline or retry queue).
- Red dot: "EFRIS: Failed — retry queued" — alert visible; Finance Manager notified separately.

The cashier's workflow is never blocked by EFRIS status. The sale is always completed locally first.

---

## 3.2 Agent Dashboard — S-010 (Samuel's Main Screen)

**Screen ID:** S-010

**Panel:** Agent Portal

**Primary Persona:** Samuel — Field Sales Agent (Diploma, confident smartphone user)

**Critical requirement:** Samuel must see his cash balance, outstanding invoices, and submit a remittance without calling the office for figures.

### Layout

Three primary KPI cards at the top of the dashboard, always visible:

| Card | Content | Design |
|---|---|---|
| Cash Balance | Total cash collected but not yet remitted (UGX, large bold number) | Blue card with white text — large font (28px). Colour-codes to red when balance exceeds a defined threshold. |
| Outstanding Invoices | Count and total value of invoices not yet cleared by remittances | White card with orange accent — count in large font. |
| Last Remittance | Date and amount of last verified remittance | White card with green accent. Shows "No remittances yet" for new agents. |

**Quick Action Row** (immediately below KPI cards):

- **Submit Remittance** button — large, primary, always visible. This is the most frequent action after viewing the dashboard.
- **New Sale** button — links to S-011 Agent POS.
- **My Stock** button — links to S-014 Agent Stock View.

**Recent Sales List** (below the quick actions):

- Last 10 sales with: date, customer name, amount, payment method, status badge.
- "View All Sales" link at the bottom.

**Offline Banner:**

- When the Agent Portal detects no internet connection, a persistent orange banner appears at the top: "You are offline — sales will sync when you reconnect. Cash balance shown is from your last sync."

---

## 3.3 Finance Dashboard — S-022 (Grace's Screen)

**Screen ID:** S-022

**Panel:** Main ERP

**Primary Persona:** Grace — Finance Director (CPA, MBA, proficient Excel user)

**Critical requirement:** Full financial visibility at any moment — parliamentary and commercial simultaneously — without month-end closing.

### Layout

**Period Selector:** Date range pickers (Flatpickr) at the top right. Defaults to current financial year. A **Mode Toggle** (PIBID / BIRDC / Consolidated) determines which accounts are shown.

**KPI Cards Row 1 — Parliamentary Mode (PIBID):**

| Card | Metric | Alert Threshold |
|---|---|---|
| Development Vote Balance | Approved vote − expenditure to date | Orange at 80% spent; red at 95% |
| Recurrent Vote Balance | Approved vote − expenditure to date | Same thresholds |
| Uncommitted Budget | Total votes − committed expenditure − posted expenditure | N/A |

**KPI Cards Row 2 — Commercial Mode (BIRDC):**

| Card | Metric |
|---|---|
| Revenue MTD | Month-to-date sales revenue |
| Gross Profit MTD | Revenue − COGS |
| Cash Position | Bank + petty cash − outstanding AP due today |
| AR Overdue | Total AR > 30 days |

**Charts Section:**

- Budget vs. Actual bar chart (ApexCharts) — one bar per vote/department; actual in blue, budget in grey; variance shown as %. Filter by mode.
- Cash flow trend line chart — 12-month rolling, BIRDC commercial only.

**GL Hash Chain Status:**

- A status indicator card at the bottom of the dashboard: "Hash chain integrity: VERIFIED — last checked [timestamp]". A manual "Run Integrity Check" button triggers the check on demand (takes ≤ 5 seconds). If the chain is broken, the card turns red and shows the first broken link: "Break detected at JE-2026-0089 — contact IT Administrator immediately."

**Dual-Mode Navigation:**

- The mode toggle persists across all Finance module screens in the current session. Grace does not need to re-select the mode on each screen.

---

## 3.4 Farmer Contribution Breakdown — S-030 (Patrick's Screen)

**Screen ID:** S-030

**Panel:** Main ERP

**Primary Persona:** Patrick — Collections Officer (Certificate in Agriculture, basic smartphone user)

**Business rule enforced:** BR-011 — every kilogramme in a cooperative batch must be allocated to a specific farmer before the batch can advance to Stage 4.

### Layout

**Batch Header (read-only):**

- Cooperative name, batch number, total batch weight (kg), date received, quality grade distribution from Stage 2.

**Progress Indicator:**

- A horizontal step indicator showing the 5 stages: `Bulk PO → [2] Batch Receipt → [3] Farmer Breakdown → Stock Receipt → GL Post`. Stage 3 is active.

**Allocation Balance Bar:**

- A prominent progress bar showing: "Allocated: 320 kg of 500 kg — 180 kg remaining."
- The bar turns green and shows a checkmark when all 500 kg are allocated.
- The **Proceed to Stage 4** button remains disabled until remaining = 0 kg.

**Farmer Contribution DataTable:**

Each row in the table represents one farmer's contribution in this batch:

| Column | Control | Rule |
|---|---|---|
| Farmer | Select2 (searchable, 6,440+ names) | Required. NIN auto-fills on selection |
| NIN | Auto-filled from farmer record | Read-only |
| Weight (kg) | Number input | Required. Running total updates the balance bar. |
| Quality Grade | Dropdown: A / B / C | Required. Determines unit price |
| Unit Price (UGX/kg) | Auto-filled from grade | Read-only (configurable by Finance Director) |
| Net Payable (UGX) | Calculated: weight × unit price | Read-only |
| Action | Delete row button | Removes allocation |

**Add Farmer Row** button at the bottom of the table.

**Batch Total Summary:**

- Batch weight: 500 kg
- Allocated: [running total]
- Remaining: [running total]
- Total payable: [sum of all net payable]

**Submit and Print:**

- When the balance reaches zero, the **Proceed to Stage 4** button enables.
- The system auto-generates a farmer receipt PDF for each farmer in the batch (printable via Bluetooth printer on the Farmer Delivery App).

---

## 3.5 Production Order Detail — S-033 (Moses's Screen)

**Screen ID:** S-033

**Panel:** Main ERP and Factory Floor App

**Primary Persona:** Moses — Production Supervisor (HND Mechanical Engineering, basic smartphone user)

**Design principle:** This screen is used on a mobile device on the factory floor where Moses has no desk. The layout must be mobile-first.

### Mobile-First Layout

**Order Header Card:**

- Recipe name, production order number, planned quantity, status badge (PLANNED / IN PROGRESS / PENDING QC / COMPLETED).
- Start date, target completion date.

**Input Materials Card:**

- Table: Material name, recipe qty (kg), issued qty (kg), remaining to issue (kg).
- "Issue Materials" button triggers a material requisition — DR WIP / CR Raw Material Inventory auto-posted on confirmation.

**Mass Balance Live Calculator:**

- A card showing:
  - Input issued: [kg]
  - Primary product recorded: [kg]
  - By-product (biogas): [kWh, converted to kg equivalent]
  - By-product (bio-slurry): [kg]
  - Scrap/waste: [kg]
  - Balance: [input − outputs] in kg, target = 0 ±2% tolerance
- Colour codes: green when within tolerance, red when outside.

**Worker Assignment:**

- Tap to assign workers from a searchable list. Each worker shown with their skill matrix tags.

**Job Card Steps:**

- Numbered checklist of production steps from the recipe. Moses taps each step to mark complete. Completed steps are crossed out.

**QC Status:**

- A status card at the bottom: "QC Inspection: PENDING". When QC submits results, this updates to "APPROVED" (green) or "REJECTED — see NCR [NCR-2026-0012]" (red).
- Until status = APPROVED, the "Transfer to Finished Goods" button remains disabled (BR-004 enforcement).

---

## 3.6 Executive Dashboard — S-044 (Director's Screen)

**Screen ID:** S-044

**Panel:** Main ERP (also mirrored in Executive Dashboard Android App)

**Primary Persona:** The Director (PhD, basic smartphone user — primary access is via the Android app)

**Design principle:** The Director reviews this dashboard for ≤ 5 minutes each morning. Every key figure must be visible without scrolling on a standard smartphone screen.

### Layout — Android App View

**Revenue Today** — large number card at the top. UGX formatted with comma separators. Subtitle shows "vs. yesterday" with a green/red arrow indicator.

**Cash Position** — total liquid cash (bank + petty cash). Subtitle: "AP due today: [amount]".

**Agent Outstanding** — total agent cash balance across all 1,071 agents. Subtitle: "Top overdue: [agent name] — [amount]".

**Production Status** — "Active orders: [count] — On target: [count] — Behind: [count]".

**P&L Snapshot** — a 3-line mini statement: Revenue / Gross Profit / Net Profit for the current month. Each line shows MTD figure and % of annual plan.

**Push Notification History** — last 5 system alerts received (budget threshold breaches, EFRIS failures, agent balance anomalies).

All figures refresh automatically when the app is opened (pull-to-refresh also available). The Director does not interact with input controls on this screen — it is view-only.
