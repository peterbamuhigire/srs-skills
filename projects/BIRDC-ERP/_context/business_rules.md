# Business Rules — BIRDC ERP

These rules are immutable. They encode BIRDC's operational, legal, and financial constraints.
No requirement, design, or implementation may violate these rules without explicit written
sign-off from the Finance Director and BIRDC Director.

---

## BR-001: Dual-Track Inventory Separation
Warehouse stock (table: tbl_stock_balance) and agent field stock (table: tbl_agent_stock_balance)
are permanently separate ledgers with no shared records. A report on warehouse stock NEVER
includes agent-held inventory. A report on total company stock includes both, clearly labelled.
Cross-contamination between the two ledgers is architecturally impossible.

## BR-002: FIFO Remittance Allocation
When an agent submits a cash remittance, the system allocates the remittance to the agent's
outstanding invoices in FIFO order (oldest invoice cleared first). This is enforced by stored
procedure `sp_apply_remittance_to_invoices`. No manual invoice selection is permitted.
Partial allocation is allowed when the remittance amount is less than the oldest invoice balance.

## BR-003: Segregation of Duties
The person who creates a transaction cannot be the same person who approves or verifies it.
This applies to: journal entries, purchase orders, stock adjustments, remittance verification,
payroll approval, and agent stock issuance. Enforced at API layer — not just UI. A user cannot
bypass this rule by constructing a direct API request.

## BR-004: QC Gate on Production Output
Finished goods from a production order CANNOT be transferred to saleable inventory until the
Quality Control module has completed inspection and set the batch quality status to "Approved"
and issued a Certificate of Analysis. The stock transfer API endpoint for production output
returns an error if the QC status is not "Approved".

## BR-005: PPDA Procurement Approval Matrix
All procurement transactions are classified by Uganda PPDA Act procurement category. The
approval authority depends on the category:
- Micro procurement: Department Head approval
- Small procurement: Finance Manager approval + Procurement Officer sign-off
- Large procurement: Director approval + Finance Manager + Solicitor General clearance where required
- Restricted procurement: Board approval + all PPDA documentation complete
No payment is processed for a procurement transaction missing any required PPDA document.

## BR-006: Agent Stock Float Limit
Each agent has a configured stock float limit — the maximum monetary value of inventory they
may hold at any time. A stock transfer to an agent that would cause the agent's stock balance
value to exceed their float limit is BLOCKED by the system. The Sales Manager must increase
the float limit or recover existing stock before new issuance.

## BR-007: FEFO Enforcement
For all products with expiry dates (all processed food products), the system automatically
selects the batch with the earliest expiry date when allocating stock for a sale, transfer,
or production input. Manual batch selection that would violate FEFO is not permitted at POS
or at the warehouse dispatch screen.

## BR-008: Circular Economy Mass Balance
For every production order, the following equation must be satisfied:
  Total Input (kg) = Primary Product Output (kg) + By-product Output (kg) + Scrap/Waste (kg)
If the recorded outputs do not balance to the recorded input (within a configurable tolerance
of ±2%), the production order CANNOT be closed. A mass balance variance report is generated
and must be reviewed by the Production Supervisor.

## BR-009: Sequential Numbering and Gap Detection
Invoice numbers, receipt numbers, and journal entry numbers are assigned sequentially and
must be gap-free within each series. If a gap is detected (e.g., invoice 1045 followed by
1047 with no 1046), an automatic alert is generated to the Finance Manager and logged in
the audit trail. Voided documents retain their numbers and are marked VOID — numbers are
never recycled.

## BR-010: Payroll Immutability
Once the Finance Manager approves and locks a payroll run, no modification to that run is
permitted. If an error is discovered, a correction is processed as a separate adjustment run
in the next payroll period (a counter-entry). The approved payroll run is permanently locked
in the database with the approver's identity and timestamp.

## BR-011: Individual Farmer Contribution Tracking
Every cooperative batch goods receipt must be broken down to individual farmer contributions
before the batch can be posted to the GL (Stage 3 of the 5-stage procurement workflow). A
cooperative batch receipt CANNOT be moved to Stage 4 (Stock Receipt) until every kilogramme
in the batch is allocated to a specific registered farmer with a quality grade and unit price.

## BR-012: Three-Way Matching
No vendor payment may be processed unless the vendor invoice has been matched to both a
Purchase Order and a Goods Receipt Note. Price variance > 5% between PO and invoice, or
quantity variance > 2%, is flagged for Finance Manager review before payment can be authorised.
This applies to all standard supplier payments. Farmer payments use the individual contribution
records instead of a traditional PO/GRN/invoice match.

## BR-013: GL Hash Chain Integrity
Every entry in the general ledger references the cryptographic hash of the previous entry in
the same account. Any tampering with a historical record breaks the hash chain. The system
performs a hash chain integrity check on demand (triggered by the Finance Director or auditor)
and reports any broken links. This satisfies the Uganda Companies Act and Income Tax Act
requirements for tamper-evident financial records.

## BR-014: Parliamentary Budget Vote Alert
When cumulative expenditure against any parliamentary budget vote reaches 80% of the
allocated vote amount, an automatic alert is sent to the Finance Director and Director.
When it reaches 95%, an additional alert is sent. Expenditure that would exceed 100% of a
vote requires Director-level override with a written justification logged in the audit trail.

## BR-015: Commission on Verified Sales Only
Agent commission accrues when a remittance is verified by a supervisor (not when cash is
collected and not when an invoice is issued). Commission is calculated as a percentage of
the invoice value of the specific invoices cleared by the verified remittance. Unverified
remittances generate no commission.

## BR-016: Biometric Attendance Authority
Attendance records imported from ZKTeco biometric devices are treated as authoritative.
Manual overrides to biometric attendance records require Finance Manager approval and are
logged in the audit trail with the reason. Manual attendance records are acceptable only when
the biometric device is offline, and must be reconciled with biometric data once the device
reconnects.

## BR-017: Export CoA Requirements
Finished product batches destined for export markets (South Korea, Saudi Arabia, Qatar,
Italy, United States) require a Certificate of Analysis referencing the specific QC test
results for all parameters specified by the destination market's import requirements. A
batch with "Approved for Domestic" status cannot be dispatched on an export order without
generating an export-grade CoA with the appropriate market-specific parameters.

## BR-018: Imprest Account Control
Imprest accounts (petty cash floats) are cash-limited. A disbursement from an imprest
account that would reduce the imprest balance below zero is blocked. Imprest replenishment
requires Finance Manager approval. All imprest transactions are individually receipted and
posted to the GL.
