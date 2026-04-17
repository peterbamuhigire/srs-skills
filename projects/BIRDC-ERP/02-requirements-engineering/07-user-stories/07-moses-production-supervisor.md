# Persona 7: Moses — Production Supervisor

**Profile:** Age 34, HND Mechanical Engineering, basic smartphone user. Manages factory floor operations. Creates production orders, assigns workers, records actual yields, submits daily production reports. Uses the Factory Floor Android app on the production floor (no desktop computer at processing stations).

**Critical requirement:** Factory Floor App — offline-capable, barcode scanning, simple data entry for mass balance verification.

---

## US-063: Create a Production Order from a Recipe

**US-063:** As Moses, I want to create a production order from a configured Bill of Materials recipe, so that the required materials are reserved and production is tracked from plan to completion.

**Acceptance criteria:**

- Moses selects the product to be produced, the recipe version (Bill of Materials), and the planned output quantity; the system calculates the required input materials based on the recipe ratios.
- The system checks that sufficient raw material stock is available in the raw materials warehouse before confirming the production order; if any material is insufficient, the system displays: "Insufficient stock: [material name] — required [x] kg, available [y] kg."
- Upon confirmation, materials are reserved (status: "committed") in `tbl_stock_balance` and the production order status is set to "Materials Reserved."
- The production order is assigned a sequential production order number and appears in the Factory Floor App job queue within 60 seconds of creation.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-011-001

---

## US-064: Issue Materials to Production (WIP Posting)

**US-064:** As Moses, I want to record materials issued from the warehouse to production, so that the WIP account is updated and raw material inventory is reduced.

**Acceptance criteria:**

- Moses raises a material requisition from the Factory Floor App, specifying the production order, materials, and quantities required.
- The system applies FEFO batch selection automatically: the earliest-expiry batch of each material is selected for issue; Moses cannot manually override batch selection to violate FEFO (per BR-007).
- Upon Store Manager confirmation in the Warehouse App, the system posts the GL entries: DR Work In Progress (WIP) / CR Raw Material Inventory — with no manual journal entry required.
- The production order's "Actual Materials Used" is updated; any variance from the recipe standard is displayed to Moses in real time.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-011-002

---

## US-065: Record Production Output and Verify Mass Balance

**US-065:** As Moses, I want to enter the actual quantities of primary products, by-products (biogas, bio-slurry), and waste produced in a production run, so that the circular economy mass balance equation is verified before the order is closed.

**Acceptance criteria:**

- The Factory Floor App prompts Moses to enter: primary product output (kg), by-product 1 output (biogas — calorific value units), by-product 2 output (bio-slurry — kg), and scrap/waste (kg).
- The system calculates: Total Input (kg) minus [Primary Output + By-product equivalents + Scrap] and displays the mass balance variance.
- If the variance is within the configured tolerance (±2%, per BR-008), the mass balance is marked "Balanced" and Moses can proceed to submit the production completion.
- If the variance exceeds ±2%, the system displays: "Mass balance out of tolerance. Variance: [x]%. Review inputs and outputs before closing." and blocks production order closure until Moses corrects the entries or submits a variance justification (per BR-008).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-011-003

---

## US-066: Assign Workers to a Production Order and Record Attendance

**US-066:** As Moses, I want to assign factory workers to a production order and record their daily attendance, so that labour costs are tracked per production order and worker productivity is measurable.

**Acceptance criteria:**

- Moses assigns workers from the registered factory worker registry to a production order on the Factory Floor App, specifying the date and their role (processing, packaging, quality check, cleaning).
- Worker assignment generates a direct labour record linked to the production order for production costing.
- When ZKTeco biometric attendance records are imported, the system cross-references them against Moses's manual assignment records for the same day; discrepancies are flagged for Finance Manager review (per BR-016).
- Moses can view the cumulative labour hours per production order, which feed into the production costing calculation (raw materials + direct labour + absorbed overhead).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-011-004

---

## US-067: Monitor Active Production Orders on the Factory Floor App

**US-067:** As Moses, I want to see all active production orders on my Android phone while walking the factory floor, so that I can monitor multiple production lines simultaneously without returning to an office.

**Acceptance criteria:**

- The Factory Floor App home screen displays all "In Progress" production orders with: order number, product name, planned output quantity, actual output recorded to date, and progress percentage.
- Moses can tap any production order to view its job card: step-by-step instructions, assigned workers, materials issued, output recorded so far, and QC status.
- The Factory Floor App works fully offline; Moses's entries are synced to the server when connectivity is restored.
- The production order status changes displayed in the app match the status visible in the web ERP within 5 minutes of a sync event.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-011-005

---

## US-068: Submit a Daily Production Report

**US-068:** As Moses, I want to submit a daily production report from the Factory Floor App, so that management receives a structured summary of the day's output, input consumption, and yield variance.

**Acceptance criteria:**

- The daily production report is auto-populated from the day's production order records; Moses reviews and confirms with any additional notes.
- The report includes: production orders started, production orders completed, total input matooke (kg), total primary product output (kg), total by-products, total scrap, and aggregate mass balance for the day.
- Upon submission, the report is sent automatically to Moses's supervisor (Factory/Production Manager) and the Director via push notification and email.
- Moses can view his historical daily production reports from the app for the last 30 days.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-011-006

---

## US-069: Record Actual Yield Variance Against Recipe Standard

**US-069:** As Moses, I want to see the yield variance between actual output and the recipe standard after each production run, so that I can investigate unexplained losses and improve process efficiency.

**Acceptance criteria:**

- After production completion is submitted, the system calculates yield variance: actual output (kg) minus recipe standard output (kg based on input quantity) divided by recipe standard output, expressed as a percentage.
- The yield variance is displayed on the completed production order record with a traffic-light indicator: green (within ±5%), amber (±5% to ±10%), red (> ±10%).
- Red-variance production orders require Moses to enter a variance explanation before the order can be closed.
- The system maintains a yield variance trend report per product showing average variance over the last 12 months, accessible to the Production Manager.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 4

**FR Reference:** FR-011-007
