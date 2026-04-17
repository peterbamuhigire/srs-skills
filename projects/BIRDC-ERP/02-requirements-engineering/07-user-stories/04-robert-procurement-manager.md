# Persona 4: Robert — Procurement Manager

**Profile:** Age 39, BSc Procurement and Supply Chain, proficient. Raises purchase requests, issues LPOs, manages the 5-stage cooperative farmer procurement workflow, tracks goods receipts, ensures PPDA compliance on all purchases.

**Critical requirement:** PPDA approval workflow with full document checklist; individual farmer contribution breakdown per cooperative batch.

---

## US-037: Raise a Purchase Request with PPDA Category Classification

**US-037:** As Robert, I want to raise a purchase request and have the system automatically classify it by PPDA procurement category, so that the correct approval workflow is triggered without me having to look up the thresholds.

**Acceptance criteria:**

- When Robert creates a purchase request, the system evaluates the estimated total value against the configured PPDA procurement thresholds and automatically assigns the category: Micro, Small, Large, or Restricted.
- The assigned category determines the approval workflow: Micro → Department Head; Small → Finance Manager + Procurement Officer; Large → Director + Finance Manager + Solicitor General clearance flag; Restricted → Board approval flag (per BR-005).
- Robert cannot modify the system-assigned category; he can only override it with a reason logged in the audit trail, and the override requires Finance Manager countersignature.
- The purchase request form pre-fills the required PPDA document checklist based on the assigned category so Robert knows exactly which documents must be uploaded before the LPO can be issued.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-001

---

## US-038: Issue a Request for Quotation to Multiple Suppliers

**US-038:** As Robert, I want to issue an RFQ to 3 or more suppliers simultaneously and compare their responses side by side, so that I can document competitive pricing and comply with PPDA requirements.

**Acceptance criteria:**

- Robert selects an approved purchase request, selects 3 or more vendors from the vendor register, and sends the RFQ; the system records the RFQ number, date sent, and recipient vendor list.
- When vendor quotes are entered, the system displays a side-by-side comparison table showing each vendor's unit price, delivery lead time, and total price.
- The system highlights the lowest-priced qualifying quote; Robert can select any quote with a documented justification if not selecting the lowest.
- The completed RFQ with all vendor responses is stored as a PDF attachment linked to the procurement record for PPDA audit purposes.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-002

---

## US-039: Generate a Local Purchase Order in Uganda LPO Format

**US-039:** As Robert, I want to generate an LPO from an approved purchase request, so that the supplier receives a formally approved procurement document in the standard Uganda format.

**Acceptance criteria:**

- Once a purchase request has completed the required approval workflow, Robert can generate an LPO; the system populates the LPO with: LPO number, date, vendor details, item descriptions, quantities, unit prices, delivery date, and authorising signatures (BIRDC Director or delegate per PPDA category).
- The LPO number is sequential and gap-free (per BR-009).
- The LPO is generated as a PDF with the BIRDC/PIBID letterhead and is available for printing and email delivery to the supplier.
- The LPO status is set to "Issued" and the committed amount is posted to the relevant budget vote in the Budget module (F-008).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-003

---

## US-040: Receive Goods Against an LPO (Three-Way Match)

**US-040:** As Robert, I want to record a goods receipt and have the system automatically match it to the LPO, so that no vendor invoice can be paid until receipt is confirmed and quantities reconciled.

**Acceptance criteria:**

- When recording a GRN, Robert selects the originating LPO; the system pre-fills the expected items and quantities from the LPO.
- Robert enters the actual quantities received; the system flags any quantity variance > 2% from the LPO quantity for Finance Manager review (per BR-012).
- When the vendor invoice is registered, the system performs three-way matching: LPO quantities and prices vs. GRN quantities vs. invoice quantities and prices. A price variance > 5% triggers a Finance Manager review flag before payment can be authorised (per BR-012).
- The GRN is linked to the LPO and invoice in a single traceability chain; the auditor can navigate from payment back to GRN back to LPO in a single click.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-004

---

## US-041: Initiate Stage 1 Cooperative Farmer Bulk Purchase Order

**US-041:** As Robert, I want to raise a bulk matooke Purchase Order per cooperative for a delivery season, so that the procurement plan is formally documented before farmers begin delivering.

**Acceptance criteria:**

- Robert creates a Farmer Bulk PO by selecting the cooperative, season, estimated total quantity (kg), and target price per grade (A, B, C).
- The system assigns a Bulk PO number, sets the status to "Stage 1 — Open," and makes the PO visible to the Farmer Delivery App as the active procurement order for that cooperative.
- The Bulk PO's committed value is posted to the Cooperative Payable account in the Budget module.
- Robert can track the PO's fulfilment: total ordered (kg) vs. total received to date (kg) vs. outstanding (kg), updated in real time as deliveries are recorded.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-005

---

## US-042: Advance a Cooperative Batch from Stage 2 to Stage 3 (Farmer Contribution Breakdown)

**US-042:** As Robert, I want to confirm that every kilogramme in a cooperative batch receipt has been allocated to a specific farmer before advancing to the next stage, so that every farmer is paid accurately and BR-011 is satisfied.

**Acceptance criteria:**

- A cooperative batch goods receipt (Stage 2) cannot advance to Stage 3 until every kilogramme in the batch is assigned to a specific registered farmer with a quality grade, weight (kg), unit price, and net payable amount (per BR-011).
- If unallocated kilograms remain when Robert attempts to advance the batch, the system displays: "Stage 3 blocked: [n] kg unallocated. All kilograms must be assigned to farmers before proceeding."
- Upon successful Stage 3 completion, the system generates an individual farmer contribution report showing each farmer's delivery, grade, price, deductions (loan repayments, cooperative levies), and net payment.
- The Stage 3 data feeds the Farmer Payment batch in Accounts Payable (F-007) for the mobile money bulk payment.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-006

---

## US-043: View PPDA Document Compliance Status for Each Procurement

**US-043:** As Robert, I want to see which PPDA-required documents are present and which are missing for each active procurement transaction, so that I can resolve gaps before the audit and never receive a PPDA audit finding.

**Acceptance criteria:**

- Each procurement record displays a PPDA document checklist with traffic-light status: green (uploaded and dated), amber (required but missing), red (overdue — payment date passed with no document).
- Robert can upload a document against any checklist item directly from the procurement record screen.
- The system prevents payment processing for any procurement record with one or more red-status required documents, displaying: "Payment blocked: PPDA required documents missing. Upload [document name] to proceed." (per BR-005).
- Robert can export a PPDA Compliance Summary Report showing the status of all active procurements, for presentation at the monthly management meeting.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-007

---

## US-044: Register and Rate Vendor Performance

**US-044:** As Robert, I want to record vendor performance after each completed purchase, so that future procurement decisions are informed by delivery accuracy, quality, and price history.

**Acceptance criteria:**

- After a procurement cycle is completed (LPO issued, GRN received, invoice matched), Robert rates the vendor on: delivery punctuality (on-time / late / very late), quality conformance (acceptable / minor non-conformance / rejected), and price competitiveness (ranked against last 3 quotes).
- The vendor record displays a cumulative performance score and the trend over the last 12 months.
- Vendors with a performance score below a configurable threshold are flagged "Preferred — Caution" and require Finance Manager sign-off to receive a new LPO.
- The vendor performance data is available in the RFQ comparison view so Robert can see past performance before selecting vendors for new RFQs.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-008

---

## US-045: Track Landed Costs for Imported Inputs

**US-045:** As Robert, I want to allocate landing costs (freight, insurance, customs duty) to imported input items, so that the true landed cost is recorded in inventory and the COGS calculation is accurate.

**Acceptance criteria:**

- For imported purchase orders, Robert can add landed cost components (freight, insurance, customs duty, clearing fees) as line items on the GRN.
- The system distributes landed costs across received items proportionally by value or by weight (Robert selects the allocation method).
- The allocated landed cost per unit is added to the item's inventory valuation cost and is visible in the stock item's cost history.
- The landed cost allocation is auto-posted to the GL (DR Inventory / CR Landed Cost Payable) without a manual journal entry.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-009

---

## US-046: View the Procurement Register with PPDA Category Breakdown

**US-046:** As Robert, I want to view the complete procurement register filtered by PPDA category and period, so that I can prepare the procurement activity report required under the PPDA Act.

**Acceptance criteria:**

- The Procurement Register displays all procurement transactions with: LPO number, vendor, description, PPDA category, estimated value, actual value, and document status.
- Robert can filter by PPDA category, date range, department, and status (open, completed, cancelled).
- The register exports to Excel and PDF in a layout suitable for direct submission to PPDA in the annual procurement report.
- The register total values by category match the corresponding GL expenditure accounts for the same period to within UGX 0.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-016-001

---

## US-047: View Farmer Payment History and Outstanding Balances

**US-047:** As Robert, I want to view each cooperative farmer's complete delivery and payment history, so that I can resolve farmer disputes about payment amounts without manual spreadsheet checks.

**Acceptance criteria:**

- The Farmer Profile screen in the Farmer Management module (F-010) displays the full delivery history: date, cooperative, batch reference, weight (kg), quality grade, unit price, gross payable, deductions (itemised), and net paid.
- The screen shows the farmer's cumulative statistics: total matooke delivered (kg), total paid (UGX), and any outstanding balance.
- Robert can print or export an individual Farmer Payment Statement as a PDF for presentation to the farmer at the cooperative.
- The farmer's payment data matches the AP payment records for the same farmer ID to within UGX 0.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-001
