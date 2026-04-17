# 3. Functional Requirements — F-009: Procurement & Purchasing

All functional requirements in this section follow the IEEE 830-1998 stimulus-response pattern: *when [stimulus], the system shall [response]*. Requirement identifiers are permanent and non-recyclable. All requirements are subject to BR-003 (Segregation of Duties) and DC-003 (Audit readiness) unless explicitly noted.

---

## 3.1 Purchase Request Management

**FR-PRO-001** — When any authenticated BIRDC/PIBID staff member with the "Raise PR" permission submits a Purchase Request form with a description, quantity, estimated unit cost, required-by date, and budget account code, the system shall create a PR record in status "Draft" and assign a sequential PR number in the format `PR-YYYY-NNNN`.

**FR-PRO-002** — When a PR is in "Draft" status and the originator clicks Submit, the system shall validate that all mandatory fields (item description, quantity, estimated unit cost, required-by date, budget account code, and justification) are populated; if any field is empty, the system shall display an inline validation error identifying each missing field and shall not advance the PR status.

**FR-PRO-003** — When a PR is submitted and passes validation, the system shall automatically classify the PR into a PPDA procurement category (micro, small, large, or restricted) based on the estimated total value against the configurable threshold table; the assigned category shall be displayed on the PR form and shall determine the approval path. [CONTEXT-GAP: GAP-007 — exact UGX threshold values pending BIRDC Administration confirmation]

**FR-PRO-004** — When the system classifies a PR as micro procurement, the system shall route the PR to the submitter's Department Head for approval and shall send an email notification to the Department Head containing the PR number, item description, estimated value, and a direct approval link.

**FR-PRO-005** — When the system classifies a PR as small procurement, the system shall route the PR sequentially to the Procurement Officer for sign-off and then to the Finance Manager for approval; each approver receives an email notification; the PR cannot advance to the next approver until the current approver acts.

**FR-PRO-006** — When the system classifies a PR as large procurement, the system shall route the PR for sequential approval by the Finance Manager, followed by the Procurement Manager, followed by the Director; the system shall block advancement to each subsequent approver until the preceding approver has acted.

**FR-PRO-007** — When the system classifies a PR as restricted procurement, the system shall route the PR for Board approval and shall require confirmation that Solicitor General clearance documentation has been uploaded before the PR can be marked approved; no LPO can be generated from a restricted PR that lacks Board approval and Solicitor General clearance document attachment.

**FR-PRO-008** — When any approver in the PR workflow rejects a PR, the system shall record the rejection reason, change the PR status to "Rejected", notify the originator by email, and prevent any further procurement action on that PR number.

**FR-PRO-009** — When a PR is fully approved per its PPDA category approval path, the system shall change the PR status to "Approved — Pending RFQ" and make the PR available for selection when creating a Request for Quotation.

**FR-PRO-010** — When a user views the PR list, the system shall display PR number, originator, department, PPDA category, estimated value, current status, current approver, and days outstanding; the list shall be filterable by department, status, and PPDA category.

**FR-PRO-011** — When an IT Administrator accesses the PPDA threshold configuration screen, the system shall allow updating of all PPDA procurement threshold values (UGX amounts for micro, small, large, and restricted categories) without developer involvement, per DC-002; every threshold change shall be logged in the audit trail with the previous value, new value, actor, and timestamp.

---

## 3.2 Request for Quotation

**FR-PRO-012** — When a Procurement Officer creates an RFQ from an approved PR, the system shall allow selection of 3 or more vendors from the vendor directory; if fewer than 3 vendors are selected, the system shall display a warning stating that PPDA guidelines require a minimum of 3 quotations for competitive procurement and shall require an override justification to be recorded before allowing fewer vendors.

**FR-PRO-013** — When an RFQ is created, the system shall assign a sequential RFQ number in the format `RFQ-YYYY-NNNN`, record the RFQ issue date, required response date, item descriptions, quantities, and specifications; the system shall generate a PDF RFQ document in Uganda standard format using mPDF and shall email it to all selected vendors.

**FR-PRO-014** — When a Procurement Officer records a supplier's quotation response, the system shall capture the supplier name, quoted unit price, quoted total, currency, delivery lead time, payment terms, validity period, and any conditions; the system shall link the response to the originating RFQ.

**FR-PRO-015** — When at least 2 supplier quotation responses have been recorded for an RFQ, the system shall display a side-by-side quotation comparison table showing all supplier responses with columns for supplier name, unit price, total price, delivery lead time, payment terms, and a calculated "recommended" indicator highlighting the lowest-compliant price; the comparison shall be printable as a PDF evaluation report.

**FR-PRO-016** — When a Procurement Officer selects a winning supplier on the quotation comparison screen, the system shall require a recorded justification if the winning supplier is not the lowest-priced quote; this justification is stored as a mandatory PPDA evaluation record linked to the RFQ.

**FR-PRO-017** — When a winning supplier is confirmed, the system shall change the RFQ status to "Evaluated — LPO Pending" and make the RFQ available for LPO generation.

---

## 3.3 Local Purchase Order Management

**FR-PRO-018** — When a Procurement Officer creates an LPO from an evaluated RFQ, the system shall pre-populate the LPO with the winning supplier's details, line items, quantities, unit prices, and totals from the quotation; the system shall assign a sequential LPO number in the format `LPO-YYYY-NNNN`.

**FR-PRO-019** — When an LPO is generated, the system shall produce a PDF document in Uganda standard Local Purchase Order format using mPDF, including: LPO number, date, BIRDC/PIBID letterhead with TIN, supplier name and address, item descriptions, quantities, unit prices, total price, delivery address (Nyaruzinga), payment terms, authorised signatory line, and PPDA category classification.

**FR-PRO-020** — When an LPO is submitted for approval, the system shall apply the same PPDA approval matrix as the originating PR (BR-005); the LPO cannot be sent to the supplier until it reaches "Approved" status.

**FR-PRO-021** — When an LPO is approved, the system shall change its status to "Issued" and shall email the PDF LPO to the supplier's registered email address; the sent timestamp and delivery confirmation (if SMTP delivery receipt is available) shall be recorded in the audit trail.

**FR-PRO-022** — When a user views an LPO, the system shall display the full LPO lifecycle: draft → pending approval → approved → issued → partially received → fully received → invoiced → paid; each status transition shall display the actor and timestamp.

**FR-PRO-023** — When a Procurement Officer cancels an LPO before any goods are received, the system shall require a cancellation reason, change the LPO status to "Cancelled", and notify the supplier by email; the LPO number is retained with "CANCELLED" status and is never recycled (BR-009).

---

## 3.4 Goods Receipt Note and Three-Way Matching

**FR-PRO-024** — When a Store Manager creates a GRN against an issued LPO, the system shall display the LPO line items with ordered quantities; the Store Manager shall enter the quantity actually received per line item; the system shall not permit a received quantity to exceed the ordered quantity without an override authorisation from the Procurement Manager.

**FR-PRO-025** — When a GRN is saved, the system shall assign a sequential GRN number in the format `GRN-YYYY-NNNN`, record the receipt date, vehicle registration number, driver name (optional), delivery note number, and receiving officer's name; the system shall automatically increment the relevant stock balance in tbl_stock_balance per F-003 (Inventory & Warehouse Management).

**FR-PRO-026** — When a vendor invoice is registered against a GRN, the system shall automatically perform three-way matching (BR-012): comparing the LPO unit price, GRN received quantity, and invoice unit price and quantity; if the invoice unit price deviates from the LPO unit price by more than 5%, or if the invoiced quantity exceeds the GRN received quantity by more than 2%, the system shall flag the invoice as "Match Exception" and send an alert to the Finance Manager; no payment may be processed against an invoice in "Match Exception" status until the Finance Manager explicitly approves it with a recorded justification.

**FR-PRO-027** — When a three-way match is confirmed (all variances within tolerance or Finance Manager has approved exceptions), the system shall change the invoice status to "Matched — Ready for Payment" and make it available in the Accounts Payable payment run.

**FR-PRO-028** — When a GRN is finalised, the system shall auto-post the GL entry: DR Purchases / Stock Account (per item's GL account mapping) and CR Goods Received Not Invoiced (GRNI) liability account; when the matching vendor invoice is posted, the system shall reverse the GRNI entry and post DR GRNI / CR Accounts Payable.

**FR-PRO-029** — When a GRN contains items that are subject to withholding tax (local service supplier payments), the system shall calculate WHT at the applicable rate (configurable, currently 6% per Uganda Income Tax Act) and display the WHT amount on the vendor invoice and payment voucher.

---

## 3.5 Purchase Returns

**FR-PRO-030** — When a Store Manager initiates a purchase return against a finalised GRN, the system shall require the return reason (defective, wrong item, over-delivery, quality failure), the quantity being returned per line, and a reference to the originating GRN number.

**FR-PRO-031** — When a purchase return is approved by the Procurement Manager, the system shall decrement the relevant stock balance in tbl_stock_balance for the returned quantity, create a supplier credit note record, and auto-post the GL reversal: DR Goods Returned to Supplier / CR Purchases Account; the debit to the supplier's AP balance shall be updated accordingly.

---

## 3.6 Vendor Directory Management

**FR-PRO-032** — When a Procurement Officer creates a new vendor record, the system shall capture: vendor name, trading name, TIN, physical address, district, primary contact name, primary contact phone, primary contact email, bank name, bank account number, bank branch, payment terms (days), vendor category (goods supplier, service provider, or both), and WHT applicability flag.

**FR-PRO-033** — When a vendor record is created or updated, the system shall enforce that vendor records and cooperative farmer records are stored in separate database tables with no shared identifiers; vendor search results shall never display cooperative farmers and farmer search results shall never display commercial vendors.

**FR-PRO-034** — When a Procurement Officer uploads a document attachment to a vendor record (contract, certificate, registration document), the system shall store the file in the server document store, record the document type, upload date, uploaded by, and expiry date (if applicable); documents with expiry dates shall generate an alert to the Procurement Manager 30 days before expiry.

**FR-PRO-035** — When a GRN for a vendor is finalised, the system shall update the vendor's performance record with: delivery date, on-time flag (actual delivery date vs. LPO required date), quantity accuracy (% of ordered quantity delivered), and quality acceptance rate (% of received goods that passed incoming inspection); these metrics shall be aggregated and displayed on the vendor profile as a performance rating.

**FR-PRO-036** — When a Procurement Manager views the vendor list, the system shall display vendor name, category, TIN, payment terms, performance rating, last order date, and total procurement value (current financial year); the list shall be sortable by performance rating and searchable by vendor name or TIN.

---

## 3.7 Landed Cost Allocation

**FR-PRO-037** — When a Procurement Officer records landed costs (freight, duty, insurance, clearing charges) against a GRN for imported goods, the system shall allocate the total landed cost proportionally across the GRN line items based on either item weight (kg) or item value (UGX), with the allocation basis selectable per GRN.

**FR-PRO-038** — When landed costs are allocated, the system shall update the unit cost of each received item to include the proportional landed cost; this updated cost shall be used for stock valuation and COGS calculation in downstream inventory and production modules.

**FR-PRO-039** — When landed costs are posted, the system shall auto-post the GL: DR Stock / Purchases Account (updated cost) and CR Landed Costs Payable; the landed cost payable shall be cleared when the freight and duty invoices are paid through Accounts Payable.

---

## 3.8 Five-Stage Cooperative Farmer Procurement

The cooperative farmer procurement workflow implements a 5-stage process that is architecturally distinct from standard vendor procurement. Each stage must be completed in sequence; the system shall block advancement to the next stage until all mandatory conditions of the current stage are satisfied.

### 3.8.1 Stage 1 — Bulk Purchase Order

**FR-PRO-040** — When a Procurement Manager creates a cooperative Bulk Purchase Order, the system shall capture: target cooperative(s), season identifier (e.g., Season 2026-A), expected total volume (kg), quality grade pricing schedule per grade (Grade A price per kg, Grade B price per kg, Grade C price per kg), collection point address, collection start date, and collection end date; the system shall assign a Bulk PO number in the format `BPO-YYYY-NNNN`.

**FR-PRO-041** — When a cooperative Bulk PO is created, the system shall require that quality grade prices (Grade A, B, C) are set from the configurable price schedule table; the system shall display the last season's prices for comparison; no Bulk PO may be saved with Grade B price exceeding Grade A price, or Grade C price exceeding Grade B price.

**FR-PRO-042** — When a cooperative Bulk PO is approved by the Procurement Manager, the system shall change its status to "Active" and make it available for batch goods receipt (Stage 2); the system shall notify the relevant cooperative leader(s) by SMS of the approved PO details including season, pricing schedule, and collection dates.

### 3.8.2 Stage 2 — Batch Goods Receipt at Factory Gate

**FR-PRO-043** — When a Procurement Officer records a batch goods receipt under an active cooperative Bulk PO, the system shall capture: batch number (auto-generated, format `BTH-YYYYMMDD-NNN`), gross weight (kg), tare weight of vehicle/packaging (kg), net weight (kg), vehicle registration number, driver name, driver phone number, cooperative name, collection point, delivery date and time, and receiving officer's name.

**FR-PRO-044** — When a batch goods receipt is saved, the system shall calculate the net weight as gross weight minus tare weight and display it prominently; if the net weight is zero or negative, the system shall reject the record with an error message "Net weight must be greater than zero."

**FR-PRO-045** — When a Stage 2 batch receipt is saved, the system shall set the batch status to "Pending Farmer Breakdown" and display the outstanding weight to be allocated to individual farmers; the batch shall not advance to Stage 4 until 100% of the net weight is allocated to named farmers (BR-011).

**FR-PRO-046** — When a batch receipt is saved, the system shall display a progress indicator showing: total batch net weight (kg), weight allocated to named farmers (kg), unallocated weight (kg), and percentage allocated; this indicator shall update in real time as farmer contributions are entered in Stage 3.

### 3.8.3 Stage 3 — Individual Farmer Contribution Breakdown

**FR-PRO-047** — When a Procurement Officer enters an individual farmer contribution for a pending batch, the system shall provide a searchable farmer lookup by farmer name, farmer registration number, or NIN; the system shall return the matched farmer's name, registration number, cooperative, and photo for visual confirmation before the entry is accepted.

**FR-PRO-048** — When a farmer contribution is entered, the system shall capture: farmer registration number (mandatory), cooperative (auto-populated from farmer record), weight delivered (kg, must be > 0), quality grade assigned (A, B, or C), and the net payable calculated automatically as weight × grade price from the Bulk PO pricing schedule; the officer may not override the calculated net payable without Finance Manager approval.

**FR-PRO-049** — When a farmer contribution record is saved, the system shall accumulate the recorded weight against the batch's total allocated weight; if the total allocated weight across all farmer contributions would exceed the batch net weight by more than 1%, the system shall reject the entry with the message "Allocated weight exceeds batch net weight. Verify scale readings before proceeding."

**FR-PRO-050** — When 100% of the batch net weight has been allocated to named farmers (i.e., unallocated weight = 0 kg within a configurable rounding tolerance of ±0.5 kg), the system shall automatically change the batch status from "Pending Farmer Breakdown" to "Ready for Stock Receipt" and enable the Stage 4 action button; the batch cannot advance if any weight remains unallocated (BR-011).

**FR-PRO-051** — When a Procurement Officer attempts to advance a batch to Stage 4 while unallocated weight remains > 0.5 kg, the system shall display the error: "This batch cannot proceed to stock receipt. [X] kg is not yet allocated to named farmers. All weight must be assigned before the batch advances." and shall not perform the stage transition.

**FR-PRO-052** — When quality-failed matooke is identified during farmer contribution breakdown (quality grade below minimum acceptable threshold), the system shall allow the officer to record the rejected weight with a rejection reason code (e.g., "under-ripe", "over-ripe", "damaged", "contaminated"); the rejected quantity shall reduce the net weight eligible for stock receipt and shall be excluded from farmer payment calculation; a rejection notice referencing the farmer record shall be generated.

### 3.8.4 Stage 4 — Stock Receipt into Factory Inventory

**FR-PRO-053** — When a batch in "Ready for Stock Receipt" status is advanced to Stage 4 by the Store Manager, the system shall create a raw material stock receipt record in tbl_stock_balance, assigning the batch number from Stage 2 as the lot number; the quantity received shall equal the net weight minus any weight rejected in Stage 3.

**FR-PRO-054** — When Stage 4 stock receipt is posted, the system shall record the stock item as "Raw Matooke", unit of measure "kg", storage location "Factory Receiving", lot number equal to the batch number, receipt date, and source cooperative; the batch status shall change to "Stock Received — Pending GL".

**FR-PRO-055** — When a batch is received into stock (Stage 4), the system shall enforce that the stock item classification "Raw Matooke — Cooperative Procurement" is used exclusively for cooperative farmer batches and is never used for standard vendor procurement; mixing of procurement sources in a single lot is prohibited.

### 3.8.5 Stage 5 — General Ledger Posting

**FR-PRO-056** — When a Stage 5 GL posting is initiated by an Accounts Assistant for a batch in "Stock Received — Pending GL" status, the system shall auto-post the following double-entry: DR Raw Material Inventory (at weighted average cost per kg based on grade mix in the batch) / CR Cooperative Payable — [Cooperative Name] (one credit line per cooperative represented in the batch); the system shall not allow partial GL posting — the entire batch is posted atomically.

**FR-PRO-057** — When Stage 5 GL posting is executed, the system shall change the batch status to "GL Posted", lock all farmer contribution records for that batch against modification, and create an immutable audit trail entry recording the GL journal entry number, batch number, cooperative names, total debit amount, and total credit per cooperative.

**FR-PRO-058** — When Stage 5 GL posting is complete, the system shall make all individual farmer contribution records available in the farmer payment calculation module as "Pending Payment" items; each record shall carry: farmer ID, farmer name, cooperative, batch number, weight, grade, gross payable, and payment status = "Pending".

**FR-PRO-059** — When a Finance Manager requests a batch audit trail report, the system shall produce a PDF document (mPDF) showing the complete lifecycle of the batch: Stage 1 Bulk PO details → Stage 2 batch receipt details → Stage 3 individual farmer contributions with weights, grades, and gross payables → Stage 4 stock receipt record → Stage 5 GL journal entry; this report serves as the primary PPDA procurement documentation record for cooperative batches.

---

## 3.9 Farmer Payment Calculation

**FR-PRO-060** — When a Finance Manager initiates a farmer payment calculation run for a specified period (date range or season), the system shall aggregate all "Pending Payment" farmer contribution records for that period, grouping by farmer; the aggregated record shall show: farmer ID, farmer name, cooperative, total weight delivered, total gross payable, total input loan deductions, total cooperative levy deductions, total transport charge deductions, and net payable.

**FR-PRO-061** — When the farmer payment calculation run is executed, the system shall apply deductions in the following order: (1) outstanding input loan repayment instalment (from F-010 input loan records), (2) cooperative levy (configurable percentage per cooperative), (3) transport charges (configurable per collection point and season); the net payable per farmer shall never be negative — if deductions exceed gross payable, the system shall set net payable to zero and carry the excess deduction forward to the next payment run, flagging it for Finance Manager review. [CONTEXT-GAP: GAP-002 — farmer payment deduction rules and priority order to be confirmed with BIRDC Finance]

**FR-PRO-062** — When the payment calculation is complete, the system shall generate a farmer payment schedule: a tabulated list of all farmers with their net payable amounts, mobile money numbers, and network (MTN/Airtel); this schedule shall be reviewed and approved by the Finance Manager before bulk payment submission.

**FR-PRO-063** — When the Finance Manager approves the payment schedule, the system shall format the payment data into the MTN MoMo Business API bulk payment request format for MTN numbers and the Airtel Money API format for Airtel numbers, and shall submit the bulk payment requests to the respective APIs; each API submission shall be logged with the request timestamp, batch ID, number of transactions, and total amount. [CONTEXT-GAP: GAP-002 — MTN MoMo API sandbox credentials required for integration testing]

**FR-PRO-064** — When a mobile money bulk payment batch receives a confirmation response from MTN MoMo or Airtel Money API, the system shall update each farmer's payment record status to "Paid", record the transaction reference number and payment timestamp, and trigger an SMS notification to each farmer (see FR-FAR-049); if the API returns a payment failure for any individual farmer, the system shall mark that farmer's record "Payment Failed — Retry" and alert the Finance Manager.
