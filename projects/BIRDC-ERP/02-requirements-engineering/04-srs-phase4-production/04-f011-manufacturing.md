# 3. Specific Requirements — F-011: Manufacturing & Production

## 3.1 Recipe and Bill of Materials Management

### 3.1.1 Recipe Definition

**FR-MFG-001**
*When* a Production Manager creates a new recipe, *the system shall* record the finished product item code (linked to inventory catalogue), recipe name, recipe type (Primary or Circular Economy), unit of measure, and the target batch size quantity, and assign a sequential Recipe ID in the format `RCP-YYYY-NNNN`.

*Test oracle:* A new recipe record is retrievable by Recipe ID with all fields populated and the Recipe ID matches the sequential format.

---

**FR-MFG-002**
*When* a recipe ingredient line is added, *the system shall* record the raw material item code, quantity per target batch size, unit of measure, and a loss percentage allowance; and *the system shall* calculate and display the expected net quantity consumed after loss allowance: $Q_{net} = Q_{gross} \times (1 - \text{Loss\%})$.

*Test oracle:* For a line with 100 kg gross and 5% loss, the displayed net quantity equals 95 kg.

---

**FR-MFG-003**
*When* a recipe output line is added, *the system shall* record the output item code (primary product or by-product), expected output quantity per batch, unit of measure, and output type (Primary, By-product, or Scrap/Waste); and *the system shall* validate that the sum of all output quantities converted to the base unit (kg) does not exceed the total input quantity in kg, and display a warning if it does.

*Test oracle:* A recipe where outputs sum to 110 kg against 100 kg inputs triggers a validation warning before save.

---

**FR-MFG-004**
*When* a recipe is saved in draft state, *the system shall* calculate and display the theoretical yield percentage: $\text{Yield\%} = \frac{\text{Primary Product Output (kg)}}{\text{Total Input (kg)}} \times 100$.

*Test oracle:* With 100 kg input and 72 kg primary product output, the displayed yield equals 72.00%.

---

**FR-MFG-005**
*When* a Production Manager activates a recipe draft by clicking **Activate**, *the system shall* assign it Version 1.0, record the activation timestamp and the activating user ID, set the status to "Active", and prevent any further edits to ingredient or output lines in that version.

*Test oracle:* After activation, any attempt to edit ingredient lines via the API returns HTTP 403; the record shows activating user and timestamp.

---

**FR-MFG-006**
*When* a Production Manager creates a revised version of an existing active recipe, *the system shall* create a new version record (incrementing the minor version number, e.g., 1.0 → 1.1) linked to the same Recipe ID, carry forward all existing ingredient and output lines as editable defaults, and retain the previous version as "Superseded" with its activation date and deactivation date recorded.

*Test oracle:* After revision, version 1.0 status equals "Superseded" with a deactivation date; version 1.1 status equals "Draft"; both are retrievable by Recipe ID.

---

**FR-MFG-007**
*When* a production order is created, *the system shall* record the recipe version in effect at that moment on the production order header, and *the system shall* prevent any change to the linked recipe version after the production order status advances beyond "Plan".

*Test oracle:* Attempting to change the recipe version on a "Materials Reserved" production order returns a validation error; the recipe version recorded on the order matches the version that was active at order creation time.

---

### 3.1.2 Circular Economy Recipes

**FR-MFG-008**
*When* a recipe is created with type "Circular Economy — Banana Peel → Biogas", *the system shall* require the following additional fields: peel input weight (kg per batch), expected biogas output (kWh per batch), and calorific conversion factor (kWh/kg of peel); and *the system shall* compute and display: $\text{Biogas (kWh)} = \text{Peel Weight (kg)} \times \text{Calorific Factor (kWh/kg)}$.

*Test oracle:* With 500 kg peel input and a calorific factor of 0.15 kWh/kg, the displayed biogas output equals 75.00 kWh.

---

**FR-MFG-009**
*When* a production order completes under a Banana Peel → Biogas circular economy recipe, *the system shall* record the actual peel weight consumed (kg) and the actual biogas generated (kWh) as separate completion fields distinct from primary product output, and post these values to the circular economy by-product register.

*Test oracle:* The circular economy register shows an entry with peel weight, biogas kWh, and the linked production order ID; the values are independent of primary product output fields.

---

**FR-MFG-010**
*When* a recipe is created with type "Circular Economy — Waste Water → Bio-Slurry", *the system shall* require: waste water input volume (litres per batch), expected bio-slurry output (kg per batch), and conversion ratio (kg bio-slurry per litre waste water); and *the system shall* compute: $\text{Bio-Slurry (kg)} = \text{Waste Water (L)} \times \text{Conversion Ratio (kg/L)}$.

*Test oracle:* With 2,000 L waste water input and a conversion ratio of 0.08 kg/L, the displayed bio-slurry output equals 160.00 kg.

---

**FR-MFG-011**
*When* a production order completes under a Waste Water → Bio-Slurry circular economy recipe, *the system shall* record the actual waste water volume processed (litres), the actual bio-slurry produced (kg), and the disposal method (Sold to Farmers or Internal Input), and create an inventory receipt for bio-slurry as a sellable or transferable item in the finished goods register.

*Test oracle:* Completing such an order creates a by-product inventory receipt record; the record includes waste water volume, bio-slurry kg, disposal method, and is linked to the production order ID.

---

**FR-MFG-012**
*When* a user views the circular economy dashboard, *the system shall* display for the selected date range: total peel weight processed (kg), total biogas generated (kWh), total waste water processed (litres), total bio-slurry produced (kg), and the cumulative mass balance for all primary production orders in that period, refreshed on every page load.

*Test oracle:* Dashboard values match the sum of individual circular economy by-product records for the selected period within ±0.01 kg/kWh rounding.

---

## 3.2 Production Order Management

### 3.2.1 Production Order Lifecycle

**FR-MFG-013**
*When* a Production Manager creates a new production order, *the system shall* record the target finished product, recipe version, planned quantity, planned start date, planned completion date, and target production location; assign a sequential Production Order ID in the format `PO-YYYY-NNNN`; and set the initial status to "Plan".

*Test oracle:* A new production order is retrievable by PO ID with all fields populated; status equals "Plan".

---

**FR-MFG-014**
*When* a Production Manager submits a production order in "Plan" status for materials reservation, *the system shall* check whether sufficient raw material stock exists in the warehouse inventory (F-003) for all recipe ingredient quantities at the planned production quantity, and *the system shall* display a line-by-line material availability report before the user confirms reservation.

*Test oracle:* For a recipe requiring 500 kg matooke, if warehouse stock is 420 kg, the availability report shows a shortfall of 80 kg on the matooke line; the manager must confirm or cancel before proceeding.

---

**FR-MFG-015**
*When* a Production Manager confirms materials reservation on a production order, *the system shall* create soft reservations against the raw material stock (reducing available-for-sale and available-for-production quantities without reducing physical stock), advance the order status to "Materials Reserved", and record the reservation timestamp and user ID.

*Test oracle:* After reservation, the raw material available quantity in F-003 is reduced by the reserved amount; the physical stock quantity is unchanged; the production order status equals "Materials Reserved".

---

**FR-MFG-016**
*When* a Production Supervisor starts a production order by clicking **Start Production**, *the system shall* advance the status from "Materials Reserved" to "In Progress", record the actual start timestamp, and activate the associated job card.

*Test oracle:* After start, production order status equals "In Progress"; actual start timestamp is recorded; job card status equals "Active".

---

**FR-MFG-017**
*When* a production order is in "In Progress" status and the final job card operation is completed, *the system shall* automatically advance the status to "QC Check" and notify the QC Manager (STK-010) via an in-application alert that the batch is ready for final inspection.

*Test oracle:* On completion of the final job card operation, order status transitions to "QC Check"; the QC Manager alert record is created with the batch ID and production order ID.

---

**FR-MFG-018**
*When* the QC module sets a batch quality status to "Approved" and issues a CoA, *the system shall* advance the linked production order status from "QC Check" to "Completed" and allow the Production Manager to initiate finished goods transfer to saleable inventory.

*Test oracle:* Production order status changes to "Completed" only after QC approval; attempting to advance status before QC approval via direct API call returns HTTP 400 with error code QC_GATE_BLOCKED.

---

**FR-MFG-019**
*When* a Production Manager closes a completed production order, *the system shall* perform the mass balance verification (per FR-MFG-038 through FR-MFG-040), and *the system shall* block order closure if the mass balance variance exceeds the configured tolerance (default ±2%), displaying the variance figure and requiring the Production Supervisor to acknowledge a variance report before closure is permitted.

*Test oracle:* With 1,000 kg input and 950 kg total recorded outputs (5% variance), the system blocks closure; the variance report is generated showing 50 kg unaccounted; closure is blocked until supervisory acknowledgement.

---

**FR-MFG-020**
*When* a production order is closed, *the system shall* set the status to "Closed", record the close timestamp and closing user ID, finalise all costing calculations, and post the production completion GL entries per FR-MFG-056 through FR-MFG-060.

*Test oracle:* Closed production order is immutable — no field edits are accepted via the API; GL entries appear in F-005 with the production order ID as the source reference.

---

### 3.2.2 Material Requisition

**FR-MFG-021**
*When* a Production Supervisor clicks **Issue Materials** on a production order in "In Progress" status, *the system shall* generate a Material Requisition Note listing all recipe ingredients and their required quantities at the planned production quantity, and require the Supervisor to confirm actual quantities to be issued before processing.

*Test oracle:* The material requisition note lists every ingredient with recipe-computed quantity; the supervisor can adjust individual lines downward but not upward beyond the recipe quantity without a warning.

---

**FR-MFG-022**
*When* a material requisition is confirmed, *the system shall* reduce the physical stock balance of each raw material in F-003 by the issued quantity (eliminating the soft reservation created at materials reservation stage), create a WIP inventory record for the issued materials, and post the GL entry: DR WIP Inventory / CR Raw Material Inventory, using the FIFO cost of the issued stock.

*Test oracle:* After issue, raw material stock balance decreases by issued quantity; WIP balance increases by the FIFO cost of issued materials; the GL entry is retrievable in F-005 with the production order ID as reference.

---

**FR-MFG-023**
*When* the system selects raw material batches for a production material issue, *the system shall* apply FEFO (First Expiry First Out) logic (BR-007), selecting the batch with the earliest expiry date first, and log the selected batch numbers on the material requisition note for full traceability.

*Test oracle:* Given 2 batches of matooke flour (Batch A expiring 2026-06-01, Batch B expiring 2026-08-01), the system issues from Batch A first; the requisition note records Batch A's lot number.

---

**FR-MFG-024**
*When* actual raw material consumption differs from the requisitioned quantity (material return or additional issue), *the system shall* allow the Production Supervisor to record a consumption adjustment, re-post the GL entry for the difference (DR WIP / CR Raw Material or DR Raw Material / CR WIP), and log the adjustment with reason, user, and timestamp.

*Test oracle:* A 10 kg return posts a reversal GL entry (DR Raw Material / CR WIP) for the FIFO cost of 10 kg; the adjustment record shows user, reason, and timestamp.

---

## 3.3 Job Card Management

**FR-MFG-025**
*When* a production order transitions to "In Progress" status, *the system shall* generate a job card containing all operations defined in the recipe's operation sequence, each with: operation name, assigned workstation, work instructions text, estimated duration (minutes), quality checkpoint indicators, and a worker assignment field.

*Test oracle:* The job card contains the same number of operation lines as defined in the recipe operation sequence; each line shows workstation, instructions, and checkpoint flag.

---

**FR-MFG-026**
*When* a Production Supervisor assigns a worker to a job card operation, *the system shall* record the employee ID from the HR worker registry (F-013), the operation ID, the assigned date, and the assignment user ID; and *the system shall* prevent assignment of an employee not in the HR active worker registry.

*Test oracle:* Assigning a deactivated employee ID returns a validation error; assigning an active employee creates an assignment record with all required fields.

---

**FR-MFG-027**
*When* a worker starts an operation, *the system shall* record the start timestamp; *when* the worker completes the operation, *the system shall* record the stop timestamp and compute the elapsed labour time: $\text{Labour Hours} = \frac{\text{Stop Timestamp} - \text{Start Timestamp}}{3{,}600}$.

*Test oracle:* Start at 08:00:00, stop at 10:30:00 — recorded labour hours equal 2.50; the value is used in production cost calculation.

---

**FR-MFG-028**
*When* a job card operation is marked as a critical quality checkpoint and the inspection result entered by the QC analyst is outside the defined specification limits, *the system shall* set the operation status to "Halted", prevent progression to the next operation, and trigger an NCR creation prompt in F-012.

*Test oracle:* A critical checkpoint with moisture content USL 14% where the entered result is 16% sets operation status to "Halted"; the next operation cannot be started; the NCR creation screen is presented automatically.

---

**FR-MFG-029**
*When* a non-critical quality checkpoint result is outside specification, *the system shall* record the out-of-specification result, display a warning to the supervisor, and allow the operation to proceed; the out-of-specification event is logged in the batch quality record in F-012.

*Test oracle:* A non-critical checkpoint with an out-of-specification result does not block operation progression; the out-of-specification event appears in the batch quality record accessible from F-012.

---

**FR-MFG-030**
*When* all operations on a job card are completed (including all quality checkpoint results entered), *the system shall* set the job card status to "Completed" and prompt the Production Supervisor to enter actual production output quantities.

*Test oracle:* After the last operation is completed, job card status equals "Completed"; the output entry form is presented immediately on the same screen.

---

## 3.4 WIP Location Tracking

**FR-MFG-031**
*When* a production order is in "In Progress" status, *the system shall* maintain a WIP location record for each processing station in the factory, updated each time a job card operation at that station starts or completes. The 6 tracked stations are: Peeling Station, Washing Station, Slicing Station, Drying Station, Milling Station, and Packaging Station.

*Test oracle:* The WIP location dashboard shows a non-null current station for every active production order; the station updates within 1 page refresh after an operation is started.

---

**FR-MFG-032**
*When* a user views the WIP location dashboard, *the system shall* display, for each processing station, the list of active production orders currently at that station, the product being processed, the quantity in process (kg), and the elapsed time at that station, refreshed on each page load without requiring a manual refresh.

*Test oracle:* For a production order at the Drying Station started 2 hours ago, the dashboard shows the station name, product name, quantity, and elapsed time of approximately 2 hours.

---

**FR-MFG-033**
*When* WIP moves between stations, *the system shall* record the station-to-station transfer timestamp, the transferring user ID, and the quantity transferred in the WIP movement log, creating an auditable trail of in-process material movement.

*Test oracle:* A WIP transfer from Peeling Station to Washing Station creates a log record with both station IDs, the transfer timestamp, user ID, and quantity; the log is retrievable by production order ID.

---

## 3.5 Production Completion Recording

**FR-MFG-034**
*When* a Production Supervisor submits production completion quantities, *the system shall* record: finished product actual output quantity (kg), by-product quantities per by-product type (kg for bio-slurry, kWh for biogas), and scrap/waste quantity (kg), linked to the production order ID.

*Test oracle:* The completion record contains all required output fields; missing any mandatory field (including scrap) returns a validation error.

---

**FR-MFG-035**
*When* production completion quantities are submitted, *the system shall* calculate the actual yield percentage: $\text{Actual Yield\%} = \frac{\text{Actual Primary Product Output (kg)}}{\text{Total Raw Material Input (kg)}} \times 100$, and compare it to the recipe theoretical yield, calculating: $\text{Yield Variance\%} = \text{Actual Yield\%} - \text{Recipe Yield\%}$.

*Test oracle:* Recipe yield is 72%; actual primary output is 68 kg from 100 kg input (68% actual yield); yield variance equals −4.00 percentage points; both values are displayed on the production order summary.

---

**FR-MFG-036**
*When* the yield variance for a production order exceeds ±5 percentage points from the recipe yield, *the system shall* flag the production order with a yield variance alert and require the Production Manager to enter a variance explanation before the order can advance to "Completed" status.

*Test oracle:* A variance of −6 percentage points blocks status advancement until a text explanation is recorded; a variance of −4 percentage points requires no explanation.

---

**FR-MFG-037**
*When* production completion is recorded for an order using a Primary recipe type, *the system shall* create a provisional finished goods inventory receipt in F-003 with status "Pending QC" and quantity equal to the actual primary product output; this receipt is visible in inventory reports as "Pending QC" and is not available for sales order allocation until QC approval.

*Test oracle:* A provisional receipt with status "Pending QC" appears in F-003; it does not appear in available-to-sell quantity calculations; it appears in total stock reports with a "Pending QC" label.

---

## 3.6 Mass Balance Verification

**FR-MFG-038**
*When* a Production Manager initiates production order closure, *the system shall* compute the mass balance equation for the order: $\text{Balance} = \text{Total Input (kg)} - [\text{Primary Output (kg)} + \text{By-product Output (kg)} + \text{Scrap (kg)}]$.

*Test oracle:* With 1,000 kg input, 720 kg primary output, 150 kg by-product, and 120 kg scrap, Balance = 10 kg; the system displays Balance = 10 kg and Variance% = 1.00%.

---

**FR-MFG-039**
*When* the mass balance variance percentage is within the configured tolerance (default ±2%, configurable by IT Administrator per DC-002), *the system shall* display a "Mass Balance: PASS" indicator and permit production order closure.

*Test oracle:* With variance = 1.00% and tolerance = 2%, the system displays "Mass Balance: PASS"; closure proceeds.

---

**FR-MFG-040**
*When* the mass balance variance percentage exceeds the configured tolerance, *the system shall* display a "Mass Balance: FAIL" indicator, block production order closure (BR-008), generate a Mass Balance Variance Report for the order, and require the Production Supervisor to acknowledge the report before any further action.

*Test oracle:* With variance = 3.50% and tolerance = 2%, closure is blocked; the variance report is generated listing total input, each output category, and the unaccounted quantity; the API endpoint for closure returns HTTP 400 with error code MASS_BALANCE_FAIL.

---

**FR-MFG-041**
*When* the mass balance variance tolerance is changed by the IT Administrator, *the system shall* log the old value, new value, user ID, and timestamp in the audit trail, and apply the new tolerance to all future production order closures without affecting already-closed orders.

*Test oracle:* The audit trail shows the old and new tolerance values with the changing user ID and timestamp; existing closed orders retain their recorded variance values.

---

## 3.7 Equipment and Capacity Management

**FR-MFG-042**
*When* equipment is registered in the equipment register, *the system shall* record: equipment name, equipment code, category (processing, packaging, laboratory, utility), location (processing station), rated capacity per hour (kg or units), acquisition date, and initial book value in UGX.

*Test oracle:* A new equipment record is retrievable with all fields; the rated capacity field is numeric and linked to a UOM.

---

**FR-MFG-043**
*When* a production order is scheduled and the planned quantity exceeds the rated capacity of the assigned equipment for the planned duration, *the system shall* display a capacity warning to the Production Manager showing the excess load, and *the system shall* permit the manager to override the warning with a documented justification.

*Test oracle:* A Drying Station with 100 kg/hour capacity scheduled for 4 hours (400 kg capacity) against a planned order of 500 kg shows a capacity warning of 100 kg excess; the manager can override with a text justification.

---

**FR-MFG-044**
*When* a maintenance event is recorded against equipment, *the system shall* capture: maintenance type (Preventive, Corrective), start date, end date, description, cost in UGX, and the technician or vendor responsible; and *the system shall* automatically flag the equipment as "Under Maintenance" during the recorded maintenance period.

*Test oracle:* Equipment under maintenance cannot be assigned as the workstation for a new production order operation for dates within the maintenance period; attempting assignment displays a "Equipment under maintenance" error.

---

**FR-MFG-045**
*When* maintenance costs are recorded, *the system shall* aggregate total maintenance cost per equipment item for the current financial year and display it in the equipment cost summary report as a production overhead component.

*Test oracle:* Maintenance cost summary report total for a given equipment equals the sum of all maintenance event costs for that equipment in the selected period.

---

## 3.8 Production Costing

**FR-MFG-046**
*When* a production order is closed, *the system shall* calculate the total actual production cost:

$$\text{Actual Cost} = \text{Raw Materials Cost} + \text{Direct Labour Cost} + \text{Absorbed Overhead}$$

where:

- $\text{Raw Materials Cost}$ = sum of FIFO costs of all materials issued (from FR-MFG-022)
- $\text{Direct Labour Cost} = \sum_{i} (\text{Labour Hours}_i \times \text{Hourly Rate}_i)$, with hourly rates from the HR module (F-013)
- $\text{Absorbed Overhead} = \text{Total Machine Hours (or Labour Hours)} \times \text{Configured Overhead Rate}$

*Test oracle:* For an order with UGX 500,000 materials, UGX 120,000 direct labour, and UGX 80,000 absorbed overhead, actual cost equals UGX 700,000; all three component values are displayed separately on the costing report.

---

**FR-MFG-047**
*When* a production order is closed, *the system shall* calculate the standard cost from the recipe: $\text{Standard Cost} = \text{Recipe Ingredient Quantities} \times \text{Standard Costs}$ (using the recipe ingredient standard costs configured per DC-002), and compute the cost variance: $\text{Cost Variance} = \text{Actual Cost} - \text{Standard Cost}$.

*Test oracle:* With actual cost UGX 700,000 and standard cost UGX 650,000, the cost variance equals UGX 50,000 adverse; the sign convention (favourable/adverse) is displayed beside the variance.

---

**FR-MFG-048**
*When* a cost variance exceeds a configurable threshold (default UGX 100,000, configurable by Finance Director), *the system shall* flag the production order in the cost variance report and send an in-application alert to the Finance Director (STK-002).

*Test oracle:* A cost variance of UGX 120,000 triggers the alert to the Finance Director; the production order appears in the flagged cost variance report; a variance of UGX 80,000 does not trigger the alert.

---

**FR-MFG-049**
*When* the Finance Director or Production Manager requests the production cost report, *the system shall* display, for each closed production order in the selected period: actual cost breakdown (materials, labour, overhead), standard cost, cost variance (UGX and percentage), and actual cost per kg of finished product.

*Test oracle:* Cost per kg = Actual Cost ÷ Actual Primary Output kg; for UGX 700,000 actual cost and 700 kg output, cost per kg equals UGX 1,000.00; the report value matches this calculation.

---

**FR-MFG-050**
*When* a production order for a circular economy by-product is closed, *the system shall* calculate the by-product production cost using the same formula as FR-MFG-046, record the cost per kWh of biogas or cost per kg of bio-slurry, and create a separate line in the production cost register for the by-product batch.

*Test oracle:* A biogas production run with UGX 50,000 total cost and 75 kWh output shows cost per kWh = UGX 667; this value appears in the circular economy cost register.

---

## 3.9 GL Posting from Production Events

**FR-MFG-051**
*When* materials are issued to a production order (FR-MFG-022), *the system shall* post the GL entry:
- DR: WIP Inventory (asset account, configured in CoA)
- CR: Raw Material Inventory (asset account, FIFO cost)

*Test oracle:* The GL entry is retrievable in F-005 with DR and CR equal (balanced); source reference equals the production order ID; account codes match the configured WIP and Raw Material accounts.

---

**FR-MFG-052**
*When* finished goods are transferred from production to saleable inventory after QC approval, *the system shall* post:
- DR: Finished Goods Inventory (asset account)
- CR: WIP Inventory (asset account)

at the actual production cost computed in FR-MFG-046.

*Test oracle:* Finished goods inventory increases by actual production cost; WIP inventory decreases by the same amount; the GL entry is balanced and references the production order ID.

---

**FR-MFG-053**
*When* direct labour costs are absorbed into a production order on closure, *the system shall* post:
- DR: WIP Inventory (labour component)
- CR: Accrued Labour Cost (liability account)

using the actual labour hours and hourly rates from F-013.

*Test oracle:* The posted labour GL entry amount equals the sum of (labour hours × hourly rate) for all operations on the production order; the entry is balanced and traceable to the production order.

---

**FR-MFG-054**
*When* overhead is absorbed into a production order on closure, *the system shall* post:
- DR: WIP Inventory (overhead component)
- CR: Manufacturing Overhead Applied (income statement account)

using the configured overhead absorption rate per DC-002.

*Test oracle:* Overhead posted equals machine hours (or labour hours) multiplied by the configured rate; the applied overhead account in F-005 shows the cumulative absorption balance.

---

**FR-MFG-055**
*When* scrap or waste is recorded in production completion, *the system shall* post:
- DR: Manufacturing Scrap Expense (expense account)
- CR: WIP Inventory

at the FIFO cost of the material allocated to scrap.

*Test oracle:* The scrap expense account in F-005 increases by the FIFO cost of scrap materials; WIP inventory decreases by the same amount; the entry references the production order ID.

---

## 3.10 Factory Floor Android Application

**FR-MFG-056**
*When* a Production Supervisor opens the Factory Floor App, *the system shall* display a dashboard showing all active production orders assigned to the supervisor's factory location, with status, product name, planned completion date, and a real-time progress indicator based on completed job card operations.

*Test oracle:* The dashboard lists only production orders in "In Progress" or "QC Check" status assigned to the supervisor's configured location; the progress indicator shows the percentage of completed operations.

---

**FR-MFG-057**
*When* the Factory Floor App has no network connectivity, *the system shall* continue to display the production orders and job cards that were last synchronised, allow the supervisor to record operation start/stop times, enter completion quantities, and record quality checkpoint results in the local Room (SQLite) database, without requiring a server connection.

*Test oracle:* With network disabled on the device, all offline actions (operation start, stop, result entry) are recorded locally; on reconnection, WorkManager syncs all offline records to the server within 60 seconds.

---

**FR-MFG-058**
*When* the Factory Floor App reconnects to the network after an offline period, *the system shall* transmit all locally queued records to the server, apply conflict resolution (last-write-wins with server timestamp per the tech stack specification), log any conflicts for IT Administrator review, and confirm synchronisation success to the supervisor with a notification.

*Test oracle:* After reconnection, the server production order reflects all locally recorded events; a sync confirmation notification appears in the app; any conflicts appear in the IT Administrator's conflict log.

---

**FR-MFG-059**
*When* a supervisor submits worker attendance records in the Factory Floor App, *the system shall* record the employee ID, date, production order, shift start time, and shift end time in the local database and sync to the HR attendance module (F-013) on reconnection.

*Test oracle:* Worker attendance records submitted offline appear in the F-013 attendance register after sync; the records show the production order and factory floor source.

---

**FR-MFG-060**
*When* a supervisor submits production completion quantities via the Factory Floor App, *the system shall* validate that all required output fields (primary product kg, by-product quantities, scrap kg) are non-negative and that at least one output quantity is greater than zero before accepting the submission.

*Test oracle:* Submitting a completion form with all output quantities equal to zero returns a validation error; submitting with primary output = 700 kg, by-product = 150 kg, scrap = 120 kg succeeds.

---

**FR-MFG-061**
*When* a production order status changes on the server (e.g., QC approves the batch), *the system shall* push a status update notification to the Factory Floor App within 30 seconds when the device is online, using Firebase Cloud Messaging or equivalent push notification service.

*Test oracle:* A QC approval event on the server results in the Factory Floor App displaying a "Batch Approved" notification within 30 seconds of the server-side status change.

---

**FR-MFG-062**
*When* a Production Supervisor views a job card operation in the Factory Floor App, *the system shall* display the work instruction text, assigned workstation, quality checkpoint type (Critical or Non-critical), and the specification limit (LSL, USL) for each checkpoint parameter.

*Test oracle:* Job card displayed in the app contains identical instruction text, workstation, and specification limits to the corresponding web ERP job card record.

---

**FR-MFG-063**
*When* the Production Manager views the production schedule on the web ERP, *the system shall* display a Gantt-style timeline of all active and planned production orders for the next 14 days, showing the product, planned start, planned end, and current status for each order, with a visual indicator for orders whose planned end date has passed but are not yet closed.

*Test oracle:* All production orders with planned end dates within the next 14 calendar days appear on the timeline; overdue orders are visually distinguished from on-schedule orders.

---

**FR-MFG-064**
*When* a Production Manager generates a yield variance report, *the system shall* list all production orders for the selected period with: product name, recipe version, recipe yield%, actual yield%, yield variance (percentage points), and variance classification (Favourable / Adverse); with totals and averages at the foot of the report, exportable to PDF or Excel.

*Test oracle:* The report total average yield variance equals the arithmetic mean of all individual order variances; the export produces a valid PDF and valid Excel file.

---

**FR-MFG-065**
*When* a Production Manager searches for historical production orders for a specific product, *the system shall* return all closed production orders for that product sorted by completion date descending, showing recipe version, actual yield%, actual cost per kg, and batch numbers issued, with a maximum page load time of 2 seconds for result sets up to 500 orders.

*Test oracle:* A search for 500 historical orders returns results within 2 seconds; recipe version and actual cost per kg values match the values recorded at order close.

---

**FR-MFG-066**
*When* a system user with Production Manager role views an equipment maintenance history report, *the system shall* display, per equipment item, all maintenance events in the selected period with dates, types, costs, and cumulative maintenance cost for the year, enabling cost allocation review per DC-003.

*Test oracle:* Cumulative maintenance cost per equipment equals the sum of all maintenance event costs for that equipment in the selected year; the report is exportable to PDF.

---

## 3.11 MRP, Factory Flow, and Green Production Extensions

**FR-MFG-067**
*When* the Production Manager creates or reschedules a production order, *the system shall* calculate time-phased material requirements from the active recipe version and compare them against warehouse stock, reserved stock, expected procurement receipts, quarantine stock, and supplier lead time before the order can be released.

*Test oracle:* A production order requiring 500 kg of raw matooke for Day 5 shows available stock, reservations, open receipts, quarantine exclusion, and net shortage or surplus for that date.

---

**FR-MFG-068**
*When* the material availability check identifies a shortage, *the system shall* create an exception record showing item, required date, required quantity, available quantity, shortage quantity, suggested action (purchase, transfer, reschedule, or split batch), owner, and due date.

*Test oracle:* A 120 kg packaging-material shortage creates one exception assigned to the Store Manager or Procurement Manager with suggested action and due date.

---

**FR-MFG-069**
*When* a production order is scheduled, *the system shall* validate workstation capacity using station calendar, rated kg/hour or unit/hour capacity, standard setup time, standard run time, and planned maintenance blocks; overloads shall require documented Production Manager override.

*Test oracle:* A 1,000 kg drying order assigned to a station with only 800 kg available capacity is flagged as overload and cannot be released without override reason.

---

**FR-MFG-070**
*When* job card operations are sequenced for the same workstation, *the system shall* calculate expected changeover time using configurable product-family transition rules and show the effect of resequencing on planned completion time.

*Test oracle:* Resequencing from flour to wine and back to flour displays a different setup total than grouping flour operations together, and the projected completion time updates.

---

**FR-MFG-071**
*When* the Production Manager views the factory flow dashboard, *the system shall* display each active batch by current station, next station, queued time, transfer distance class, and congestion status for the 6 factory stations listed in FR-MFG-031.

*Test oracle:* If 4 batches are queued at the Drying Station beyond the configured queue threshold, the station is marked congested and the affected batches are listed.

---

**FR-MFG-072**
*When* production readings are captured manually or from equipment integrations, *the system shall* record energy use (kWh), water use (litres), machine time, labour time, scrap quantity, rework quantity, and recovered by-product quantity against the production order and operation.

*Test oracle:* A completed drying operation shows energy, water, machine time, labour time, scrap, rework, and by-product recovery values linked to the operation record.

---

**FR-MFG-073**
*When* a production order is closed, *the system shall* calculate sustainability KPIs including energy per kg, water per kg, yield percentage, scrap percentage, rework percentage, by-product recovery percentage, and avoidable waste cost.

*Test oracle:* For a 700 kg finished output using 140 kWh and 2,100 litres of water, the report shows 0.20 kWh/kg and 3.00 litres/kg.

---

**FR-MFG-074**
*When* actual yield, energy per kg, water per kg, or scrap percentage exceeds configured tolerance versus recipe or product standard, *the system shall* create a production variance record and alert the Production Manager and Finance Director.

*Test oracle:* A water-per-kg variance 15% above standard creates a variance record with affected order, metric, standard, actual value, percentage variance, and owners notified.

---
