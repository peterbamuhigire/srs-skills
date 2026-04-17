# Business Rules -- Maduuka

## BR-001: Tenant Data Isolation
Every database query MUST be scoped to the authenticated user's franchise_id. A user from Business A can never retrieve, modify, or detect the existence of data belonging to Business B, even if both tenants share the same database server.

## BR-002: Credit Limit Enforcement
The system shall prevent a cashier from completing a credit sale that would cause a customer's outstanding balance to exceed their configured credit limit. A manager-level user may override the block with a reason code; the override is recorded in the audit log.

## BR-003: Immutable Audit Trail
All create, edit, delete, void, stock adjustment, and payment events shall be recorded in an append-only audit log. No user interface action or API endpoint shall permit deletion or modification of an audit log entry.

## BR-004: Stock Movement Immutability
Every stock movement record (purchase receipt, sale, transfer, adjustment) is immutable once confirmed. Corrections require a counter-entry (a new adjustment record) rather than editing the original movement.

## BR-005: Stock Adjustment Approval Threshold
Stock adjustments above a business-configurable monetary value threshold shall require manager-level approval before the stock level is updated. Adjustments below the threshold are applied immediately with a reason code.

## BR-006: FIFO / FEFO Enforcement
For products with batch/expiry tracking enabled, the system shall enforce First Expiry, First Out (FEFO) stock selection at the point of sale and dispensing. The oldest expiry date batch shall be selected automatically unless the user holds a manager-level override permission.

## BR-007: POS Session Reconciliation
A cashier session MUST be opened with an opening cash count before any sale can be processed. The session cannot be closed until all sales in the session are either completed or voided. The closing reconciliation report shows: opening float + cash sales - cash refunds = expected closing cash. Any variance is flagged.

## BR-008: Receipt Gap Detection
The system shall compare issued receipt numbers within each session against the expected sequential range. Any gap (e.g., receipt 1014 issued after 1012 with no 1013) shall be flagged in the receipt gap report for manager review.

## BR-009: Offline Sale Queue
When a sale is completed without internet connectivity, the system shall record the complete transaction locally and mark it as pending_sync. On connectivity restoration, all pending transactions shall be uploaded in chronological order. The system shall never prevent a sale from being recorded due to connectivity loss.

## BR-010: Multi-Payment Tracking
When a single sale is settled using multiple payment methods (e.g., partial cash + partial Mobile Money + partial credit), each payment component is recorded separately against its respective payment account. The sum of all payment components must equal the total sale amount.

## BR-011: Three-Way Purchase Matching
The system shall flag discrepancies between a Purchase Order, the Goods Receipt Note, and the Supplier Invoice when they differ in quantity or unit price by more than UGX 0. Flagged discrepancies must be reviewed and resolved by a manager before the purchase is finalised.

## BR-012: Payroll Immutability After Approval
Once a monthly payroll run has been approved by the authorised user, individual payslip amounts shall be locked. Any correction requires a reversal entry in the following payroll period, not modification of the approved payroll.

## BR-013: Pharmacy Prescription-Linked Dispensing (Phase 2)
For products classified as prescription-only, the system shall require a recorded prescription to be linked to the sale before dispensing is permitted. The enforcement level is configurable per business: warning-only or hard block.

## BR-014: Controlled Drugs Register (Phase 2)
Every dispensing of a controlled substance (narcotic or psychotropic) shall be recorded in the controlled drugs register with: dispensing pharmacist, batch number, patient name, prescribing doctor, quantity dispensed, and running balance. This register is read-only for all users except the dispensing pharmacist and platform admin.

## BR-015: Hotel Room Double-Booking Prevention (Phase 3)
The system shall prevent the assignment of a specific room to more than one active reservation or check-in for any overlapping date range. A warning shall appear when attempting to create a reservation that conflicts with an existing confirmed reservation.

## BR-016: Hourly and Nightly Room Billing (Phase 3)
Accommodation properties in Uganda (guesthouses, lodges, budget hotels) operate dual pricing: a nightly rate for overnight stays and an hourly rate for short-stay bookings. The system shall support both billing modes per room type. When a guest checks in under hourly billing, the system shall record the check-in time and calculate the charge as: Charge = Hours Occupied x Hourly Rate, rounded up to the next whole hour. When a guest checks in under nightly billing, the system shall calculate the charge as: Charge = Nights x Nightly Rate. The billing mode (hourly vs nightly) shall be selectable at check-in and shall not be changeable after check-out has been processed. Both billing modes shall support posting of additional charges (F&B, laundry, conference room) to the room account.
