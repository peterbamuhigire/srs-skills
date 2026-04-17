---
title: "SRS Phase 2a — Restaurant/Bar Add-on Module (F-011)"
subtitle: "Section 3: Functional Requirements"
project: Maduuka
version: "0.1-draft"
date: 2026-04-05
---

# Section 3: Functional Requirements for the Restaurant/Bar Add-on Module

All requirements in this section are scoped to F-011 on the Web and iOS platforms (Phase 2a). Requirements follow stimulus-response format per the IEEE Std 1233-1998 "Verifiable" criterion. "The system" refers to the Maduuka platform with F-011 active. Every data operation is implicitly scoped to the authenticated tenant's `franchise_id` (BR-001).

---

## 3.1 Table Management (FR-RES-001 to FR-RES-015)

### 3.1.1 Area and Table Definition

**FR-RES-001:** When a Branch Manager or Business Owner creates a serving area (e.g., "Main Hall," "Rooftop," "Bar Counter"), the system shall store the area name, maximum capacity (covers), and an optional display colour used on the floor plan. The area shall become available for table assignment immediately on save.

**FR-RES-002:** When a Branch Manager or Business Owner creates a table within an area, the system shall require: table name or number, area assignment, seating capacity (covers), and table shape (round, square, or rectangle). The table shall default to *Available* status on creation.

**FR-RES-003:** When a Branch Manager or Business Owner edits a table's properties (name, capacity, area, or shape), the system shall apply the changes immediately. If the table is currently *Occupied* or *Reserved*, the system shall display a warning before saving but shall not block the edit.

**FR-RES-004:** When a Branch Manager or Business Owner deletes a table, the system shall block deletion if the table has any open orders, active reservations, or an *Occupied* or *Reserved* status. The system shall display the blocking reason. Deletion of a table with no open records shall be permitted and shall retain the table in archived state for historical reporting.

**FR-RES-005:** When a Branch Manager or Business Owner sets a table's seating capacity, the system shall use the capacity value as the default cover count when an order is opened on that table. The waiter shall be able to override the cover count at order creation.

### 3.1.2 Real-Time Status Board

**FR-RES-006:** When any user with the Waiter, Cashier, Bar Staff, Branch Manager, or Business Owner role opens the table status board, the system shall display all tables grouped by area, each showing: table name/number, current status (*Available*, *Occupied*, *Reserved*, or *Cleaning*), cover count (if occupied), assigned waiter (if occupied), and elapsed time since last status change. The status board shall reflect the current state within 2 seconds of any status change across all connected clients.

**FR-RES-007:** When a table's status is *Available*, the system shall render the table tile in green on the status board. When the status is *Occupied*, the tile shall be rendered in red. When the status is *Reserved*, the tile shall be rendered in amber. When the status is *Cleaning*, the tile shall be rendered in grey.

### 3.1.3 Status Transitions

**FR-RES-008:** When a waiter opens a new Dine-In order on a table with *Available* status, the system shall automatically change the table status to *Occupied* and record the transition timestamp. The system shall reject order creation on a table with *Occupied* or *Reserved* status unless a Branch Manager or Business Owner overrides.

**FR-RES-009:** When a Branch Manager or Business Owner overrides the status of an *Occupied* or *Reserved* table to allow a new order, the system shall record the override event in the audit log with the overriding user's name, reason code, timestamp, and the original table status (BR-003).

**FR-RES-010:** When a bill is fully paid and the payment is confirmed, the system shall automatically change the table status from *Occupied* to *Cleaning*. The table shall not revert to *Available* until a staff member with Waiter, Branch Manager, or Business Owner role manually marks it as *Available*.

**FR-RES-011:** When a staff member marks a table as *Available* from *Cleaning* status, the system shall update the status, clear the assigned waiter and cover count fields, and record the transition timestamp.

**FR-RES-012:** When a reservation is cancelled, the system shall change the table status from *Reserved* to *Available* if no other active reservation exists for that table in the current time window.

### 3.1.4 Table Reservations

**FR-RES-013:** When a Branch Manager, Business Owner, or Waiter creates a table reservation, the system shall require: table selection, reservation date and time, cover count, and a customer name or phone number. The system shall block creation of a reservation that overlaps an existing confirmed reservation for the same table in the same date-time window, displaying the conflict.

**FR-RES-014:** When a reservation's scheduled arrival time is reached, the system shall change the table status from *Available* to *Reserved* and display the reservation details on the table tile.

**FR-RES-015:** When a user cancels a reservation, the system shall record the cancellation with the cancelling user's name and timestamp. The table status shall revert per FR-RES-012.

---

## 3.2 Order Management (FR-RES-016 to FR-RES-030)

### 3.2.1 Order Creation

**FR-RES-016:** When a waiter selects an *Available* table and creates a new order, the system shall prompt for: order type (Dine-In, Takeaway, or Delivery), cover count, and waiter assignment (defaulting to the logged-in user). For Takeaway and Delivery orders, no table assignment is required.

**FR-RES-017:** When a waiter selects "Delivery" as the order type, the system shall additionally prompt for a customer name and delivery address. The table status board shall not be affected by Delivery or Takeaway orders.

**FR-RES-018:** When a Branch Manager or Business Owner assigns a waiter to a table order, the system shall record the assigned waiter's name and staff ID against the order. The assignment shall be changeable until the order is settled.

### 3.2.2 KOT Creation and Dispatch

**FR-RES-019:** When a waiter adds items to an order, the system shall display the full menu product catalogue filtered to F&B items. For each item added, the system shall accept: quantity, per-item modifiers (e.g., "extra sauce," "no onions," "well done"), and a free-text special instructions field (max 200 characters).

**FR-RES-020:** When a waiter selects "Send to Kitchen" on a populated order, the system shall create a Kitchen Order Ticket (KOT) containing: KOT sequence number (auto-incremented per order), table number or order reference, waiter name, all items with modifiers and special instructions, and the timestamp of dispatch. The KOT shall appear on the KDS within 500 ms of dispatch.

**FR-RES-021:** When a KOT is sent, the system shall immediately trigger raw material stock deduction per the BOM for each dispatched item (see Section 3.6). If the KOT send and BOM deduction succeed, the items move from the order staging area to the active KOT list. If BOM deduction fails due to a system error (not a shortfall warning), the KOT send shall be rolled back and the waiter notified.

**FR-RES-022:** When a waiter adds further items to an order after the first KOT has been sent, the system shall allow creation of a new KOT for the additional items on the same order. Multiple KOTs may exist against a single order, each with its own dispatch timestamp and item list. The bill shall aggregate items across all KOTs for the order.

**FR-RES-023:** When a waiter selects "Hold" on an order in progress, the system shall save the current item selection without dispatching a KOT. Held items shall be clearly labelled as "staged — not sent to kitchen" in the order view. The waiter may add further items or fire the held KOT at any point.

**FR-RES-024:** When a waiter selects "Fire" on a held KOT, the system shall dispatch the KOT to the KDS following the same process as FR-RES-020 and FR-RES-021.

### 3.2.3 Order Modification

**FR-RES-025:** When a waiter adds items to an existing order that has at least one sent KOT, the system shall add the new items to a new staged KOT rather than modifying the previously sent KOT. Previously sent KOTs are immutable after dispatch.

**FR-RES-026:** When a Branch Manager or Business Owner voids an item from a sent KOT, the system shall record the void in the audit log (BR-003), reverse the BOM stock deduction for the voided item, and mark the item as voided on the bill. The system shall not permit a waiter-role user to void items from a sent KOT without manager authorisation.

**FR-RES-027:** When a waiter changes the modifier or special instruction on an item in a staged (unsent) KOT, the system shall update the item in place. No audit log entry is required for modifications to staged, unsent items.

---

## 3.3 Kitchen Display System (FR-RES-031 to FR-RES-040)

### 3.3.1 Display and Refresh

**FR-RES-031:** When the KDS screen is open in a browser on a kitchen display device, the system shall automatically refresh the KOT list every 30 seconds by default. The auto-refresh interval shall be configurable per station by a Branch Manager or Business Owner (minimum: 10 seconds, maximum: 120 seconds). Refresh shall not require a manual page reload.

**FR-RES-032:** When a new KOT is dispatched by any waiter, the system shall display the KOT on all KDS screens associated with the order's station within 500 ms of dispatch, without waiting for the next scheduled refresh cycle. This near-real-time push shall use a server-sent events or WebSocket mechanism.

**FR-RES-033:** When the KDS displays a KOT, the system shall render the elapsed time since KOT dispatch using the following colour-coding scheme: green background when elapsed time is less than 10 minutes, amber background when elapsed time is 10 to 15 minutes (inclusive), and red background when elapsed time exceeds 15 minutes. The urgency thresholds (10 minutes and 15 minutes) shall be configurable per station by a Branch Manager or Business Owner.

**FR-RES-034:** When the KDS is displayed, the system shall show for each KOT: KOT number, table number or order reference, waiter name, dispatch timestamp, elapsed time, and each item with its modifiers and special instructions.

### 3.3.2 Authentication

**FR-RES-035:** When a kitchen display device completes initial session login by a user with Kitchen Staff or Branch Manager role, the system shall maintain the KDS session active without requiring re-authentication for subsequent KDS page views on that device. The session shall remain active until explicitly logged out or until the device's session token expires (maximum 24 hours from last activity).

**FR-RES-036:** When a KDS session token expires, the system shall redirect to the login screen and require re-authentication. The KDS shall not display KOT data to an unauthenticated browser session.

### 3.3.3 KOT Completion

**FR-RES-037:** When a kitchen staff member marks an individual item on a KOT as "Done," the system shall visually strike through the item on the KDS for all users viewing that KDS station and record the item completion timestamp.

**FR-RES-038:** When a kitchen staff member marks an entire KOT as "Complete," the system shall remove the KOT from the active KDS view, record the KOT completion timestamp, and update the order's KOT status to "complete." The KOT shall remain visible in the order history.

### 3.3.4 Multi-Station Support

**FR-RES-039:** When a Branch Manager or Business Owner defines a kitchen station (e.g., "Grill," "Fryer," "Cold Section," "Bar"), the system shall allow assignment of menu item categories to that station. KOTs dispatched for items in a category shall appear on the KDS screen for the assigned station only.

**FR-RES-040:** When a KOT contains items assigned to multiple stations, the system shall split the KOT into station-specific sub-tickets for display on each relevant station's KDS, while maintaining the KOT as a single record for billing and reporting.

---

## 3.4 Bar Tabs (FR-RES-041 to FR-RES-050)

### 3.4.1 Tab Lifecycle

**FR-RES-041:** When a Bar Staff or Waiter user opens a bar tab, the system shall require: a customer name or a table reference (at least one). Optional fields: phone number and a tab credit limit. The tab shall be assigned a unique tab reference number and set to *Open* status.

**FR-RES-042:** When a Bar Staff or Waiter user adds a drink round to an open bar tab, the system shall create a KOT for the bar station with the ordered items and append the round to the tab's running total. Each round shall be recorded with a timestamp.

**FR-RES-043:** When a Bar Staff or Waiter user attempts to add a round to a bar tab and the resulting tab total would exceed the configured tab credit limit, the system shall block the addition and display the current tab balance and the credit limit (BR-002). A Branch Manager or Business Owner may override the block with a reason code; the override shall be recorded in the audit log (BR-003).

**FR-RES-044:** When a Bar Staff or Waiter user transfers an open bar tab to a table order, the system shall merge all tab items into a new KOT appended to the target table's order, close the bar tab, and display the merged items on the table bill.

**FR-RES-045:** When a Bar Staff, Waiter, or Cashier user settles a bar tab, the system shall present an itemised tab summary and accept any payment method available in F-001 (FR-POS-011 through FR-POS-015). On full payment confirmation, the system shall close the tab and record it as settled with the payment method, amount, and timestamp.

**FR-RES-046:** When a bar tab is settled with partial payment, the system shall record the partial payment against the tab, reduce the outstanding tab balance, and keep the tab in *Open* status until the balance reaches zero.

### 3.4.2 Tab Reporting

**FR-RES-047:** When a Branch Manager or Business Owner views open bar tabs, the system shall list all tabs with *Open* status, showing: tab reference, customer name or table, running total, elapsed time since opening, and assigned staff member.

---

## 3.5 Billing and Payments (FR-RES-051 to FR-RES-060)

### 3.5.1 Bill Generation

**FR-RES-051:** When a Cashier or Waiter requests a bill for a Dine-In order, the system shall generate an itemised bill aggregating all items across all KOTs for that order. The bill shall show: each item with quantity, unit price, and line total; subtotal; service charge (if configured); cover charge (if configured); tax (per configured tax rules); and total due.

**FR-RES-052:** When a service charge is configured for the branch, the system shall calculate the service charge as: *Service Charge = Subtotal × Service Charge Rate*, where *Service Charge Rate* is a percentage configurable by the Business Owner (0%–30%). The calculated service charge shall be displayed as a separate line on the bill before tax.

**FR-RES-053:** When a cover charge is configured for the branch, the system shall calculate the cover charge as: *Cover Charge = Cover Count × Cover Charge Amount per Cover*, where cover count is the number recorded on the order and cover charge per cover is a fixed amount configurable by the Business Owner. The calculated cover charge shall be displayed as a separate line on the bill.

**FR-RES-054:** When a bill is generated, the system shall print a KOT-style bill ticket on the kitchen thermal printer if a "print on bill request" option is enabled for the branch. The bill ticket shall include the table number, all items, subtotal, charges, and total due.

### 3.5.2 Split Billing

**FR-RES-055:** When a Cashier or Waiter selects "Split Bill by Item," the system shall display all items on the order and allow the user to assign each item to one of N named splits (e.g., "Split 1," "Split 2"). Each split shall display its own subtotal, applicable charges, and total. The user shall settle each split independently using any payment method from F-001.

**FR-RES-056:** When a Cashier or Waiter selects "Split Bill Equally," the system shall divide the order total (including service charge and cover charge) by a user-specified number of covers (N), display the per-cover amount, and allow each share to be settled independently. If the total is not divisible without remainder, the remainder shall be added to the last split.

**FR-RES-057:** When all splits of a split bill are fully settled, the system shall mark the order as paid and trigger table release per FR-RES-010.

### 3.5.3 Payment Processing

**FR-RES-058:** When a Cashier settles a bill, the system shall accept all payment methods configured in F-001 (cash, MTN MoMo, Airtel Money, credit). Multi-payment settlement (FR-POS-015) shall apply. Each payment component shall be recorded against its payment account.

**FR-RES-059:** When a bill is fully paid, the system shall generate a receipt per the F-001 receipt format (FR-POS-017) augmented with restaurant-specific lines: table number, cover count, waiter name, service charge, and cover charge. The receipt shall be printable on the thermal printer or shareable via WhatsApp/SMS.

**FR-RES-060:** When a bill is fully paid and the payment confirmed, the system shall automatically change the table status to *Cleaning* per FR-RES-010. This transition shall occur within 2 seconds of payment confirmation.

---

## 3.6 Bill of Materials and Stock Integration (FR-RES-061 to FR-RES-070)

### 3.6.1 BOM Definition

**FR-RES-061:** When a Business Owner or Branch Manager creates a BOM for a menu item, the system shall allow linking of one or more raw material SKUs (from the F-002 product catalogue) to the finished menu item. For each raw material, the system shall record: SKU, quantity per unit of the menu item, and unit of measure (UOM). A menu item with no BOM record shall not trigger any stock deduction on KOT send.

**FR-RES-062:** When a Business Owner or Branch Manager edits an existing BOM, the system shall apply the updated recipe to all future KOT sends. Previously completed KOT stock deductions are not retroactively adjusted.

**FR-RES-063:** When a Business Owner or Branch Manager deletes a BOM for a menu item, the system shall deactivate the BOM and log the deletion event with the user and timestamp. Future KOT sends for that item shall not trigger stock deduction until a new BOM is created.

### 3.6.2 Automatic Stock Deduction

**FR-RES-064:** When a KOT is sent (FR-RES-020), the system shall, for each item with a BOM, calculate the raw material quantities to deduct as: *Deduction = Item Quantity × BOM Raw Material Quantity per Unit*. The system shall create an immutable stock movement record of type `kot_deduction` for each raw material deducted, per BR-004.

**FR-RES-065:** When a KOT is sent and a raw material's current stock level is insufficient to cover the BOM deduction for any item in the KOT, the system shall display a warning to the waiter showing the item name, the shortfall quantity, and the raw material name. The waiter shall be able to proceed and send the KOT despite the shortfall (allowing the stock level to go negative), or cancel the KOT send. The shortfall event shall be recorded in the audit log.

**FR-RES-066:** When a KOT item is voided by a manager (FR-RES-026), the system shall reverse the BOM raw material deductions for the voided item by creating a compensating stock movement record of type `kot_deduction_reversal`. The original `kot_deduction` record is not modified (BR-004).

### 3.6.3 Yield Management

**FR-RES-067:** When a Business Owner or Branch Manager records the actual raw material consumption for a period (via a stock count reconciliation), the system shall calculate the BOM yield percentage as: *Yield % = (Theoretical Consumption ÷ Actual Consumption) × 100*, where theoretical consumption is the sum of BOM deductions for all KOTs in the period and actual consumption is the physical stock movement. The yield percentage shall be displayed per raw material on the BOM yield report.

**FR-RES-068:** When the BOM yield percentage for any raw material falls below a configurable threshold (default: 80%) in a reporting period, the system shall flag the material in the yield report and display it on the Branch Manager's dashboard alerts panel.

---

## 3.7 Floor Plan Designer — Web Only (FR-RES-071 to FR-RES-075)

**FR-RES-071:** When a Business Owner or Branch Manager opens the floor plan designer on the web interface, the system shall display a canvas representing the serving area. The user shall be able to drag table objects onto the canvas and position them freely. Table objects shall display the table name, shape (round, square, or rectangle), and seating capacity.

**FR-RES-072:** When a user selects a table object on the floor plan canvas, the system shall display a properties panel allowing update of: table name, shape, seating capacity, and area assignment. Changes shall be reflected on the canvas immediately.

**FR-RES-073:** When a user defines a room section on the canvas by drawing a boundary zone, the system shall allow the zone to be labelled with an area name (e.g., "Outdoor Terrace"). Tables placed inside the zone boundary shall be automatically associated with that area.

**FR-RES-074:** When a user publishes the floor plan, the system shall save the layout and make it immediately available as the table status board view for all users (Waiter, Cashier, Bar Staff, Branch Manager, Business Owner) on web and iOS. The published floor plan shall show each table's current status colour per FR-RES-007.

**FR-RES-075:** When a user saves an unpublished draft of the floor plan, the system shall preserve the draft layout without overwriting the currently published floor plan. The currently published floor plan remains active until the draft is explicitly published.

---

## 3.8 Reporting (FR-RES-076 to FR-RES-085)

### 3.8.1 Server Performance Report

**FR-RES-076:** When a Business Owner or Branch Manager requests the server performance report for a date range, the system shall display for each waiter: total covers served, total revenue on orders they were assigned to, average order value, and average covers per order. Results shall be sortable by any column.

**FR-RES-077:** When a Business Owner or Branch Manager requests the server performance report, the system shall also display a tip total per waiter if tip recording is enabled on the tenant's account. [CONTEXT-GAP: GAP-011 — confirm whether tip recording is in scope for Phase 2a or deferred to a later phase.]

### 3.8.2 KOT Timing Report

**FR-RES-078:** When a Business Owner or Branch Manager requests the KOT timing report for a date range, the system shall display: average time from KOT dispatch to KOT marked complete, per kitchen station, per day. The report shall flag stations where the average exceeds the urgency thresholds configured in FR-RES-033.

**FR-RES-079:** When a Business Owner or Branch Manager requests the KOT timing report, the system shall list the slowest 10 KOTs by completion time within the selected period, showing: KOT number, table, waiter, station, dispatch time, completion time, and elapsed duration.

### 3.8.3 Menu Item Performance Report

**FR-RES-080:** When a Business Owner or Branch Manager requests the menu item performance report for a date range, the system shall display for each menu item: quantity sold (in covers), total revenue, cost of goods sold (based on BOM raw material cost), and gross margin per item in both UGX and percentage. Items with no BOM shall show cost as "N/A."

**FR-RES-081:** When a Business Owner or Branch Manager requests the top sellers report within the menu item performance report, the system shall list the top 20 items by revenue and the top 20 items by quantity sold for the selected period.

### 3.8.4 Cover and Revenue Report

**FR-RES-082:** When a Business Owner or Branch Manager requests the cover and revenue report, the system shall display for the selected period: total covers served, total revenue, revenue per cover, and average party size (covers per order). Results shall be groupable by day, week, or month.

**FR-RES-083:** When a user requests any F-011 report, the system shall provide export options: CSV download, PDF download, and print. Exports shall complete within 30 seconds for periods up to 12 months of data.

### 3.8.5 BOM Yield Report

**FR-RES-084:** When a Business Owner or Branch Manager requests the BOM yield report, the system shall display for each raw material in the selected period: theoretical consumption (sum of BOM deductions), actual consumption (from stock movements), yield percentage, and variance in UGX at cost price.

**FR-RES-085:** When a Business Owner or Branch Manager exports the BOM yield report, the system shall include all columns displayed in FR-RES-084 in the CSV and PDF export formats, with period start and end date in the export header.
