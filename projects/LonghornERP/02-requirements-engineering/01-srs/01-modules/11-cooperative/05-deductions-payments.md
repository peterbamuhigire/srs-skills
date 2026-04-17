# 5. Deductions and Mobile Money Payment Requirements

## 5.1 Overview

This section specifies requirements for calculating and applying all deductions against a farmer's gross intake payment — including outstanding input loan balances and society or union levies — and for disbursing net payments to farmers via mobile money bulk transfer.

## 5.2 Payment Calculation Formula

The net farmer payment is computed as:

$FarmerPayment = (Weight \times GradePrice) - \sum Deductions$

where $\sum Deductions$ includes all active input loan instalments and all applicable levies for the intake entry's season and commodity.

## 5.3 Input Loan Deductions

**FR-COOP-036** — When an intake entry is saved for a farmer who has an outstanding input loan balance, the system shall retrieve all active loan records for that farmer, compute the instalment amount per the loan's repayment schedule, and apply the deduction automatically on the intake entry.

*Acceptance criterion:* Farmer with outstanding loan UGX 120,000 on a 4-instalment schedule; single intake entry deducts UGX 30,000 (UGX 120,000 ÷ 4); net payment reflects the deduction.

**FR-COOP-037** — When a loan deduction would result in a negative net payment (i.e., $\sum Deductions > GrossPayment$), the system shall cap the deduction at the gross payment amount, set the net payment to UGX 0, and carry forward the unrecovered balance to the farmer's next intake entry.

*Acceptance criterion:* GrossPayment = UGX 18,000; loan instalment = UGX 25,000 → deduction capped at UGX 18,000; net = UGX 0; loan balance reduced by UGX 18,000 with UGX 7,000 carried forward.

**FR-COOP-038** — When a loan is fully repaid (outstanding balance reaches UGX 0), the system shall mark the loan as "Closed", stop generating deductions for that loan on subsequent intake entries, and record the closure date and final repayment intake reference.

*Acceptance criterion:* After the final instalment deduction, the loan record status changes to "Closed" and no further deductions are applied on the next intake entry for that farmer.

**FR-COOP-039** — When an administrator registers a new input loan for a farmer, the system shall require: loan amount, disbursement date, repayment method (equal instalments per intake / fixed amount per intake / full deduction on first intake), number of instalments (if applicable), and linked commodity season, and persist the loan record with status "Active".

*Acceptance criterion:* A loan of UGX 200,000 over 5 equal instalments for "2025 Coffee Season" is saved; the system computes instalment = UGX 40,000 and applies it correctly on the next 5 intake entries.

## 5.4 Levy Deductions

**FR-COOP-040** — When an intake entry is saved, the system shall compute and apply all levy deductions configured for the intake's commodity, society, and season, using:

$LevyAmount = GrossPayment \times LevyRate$

for percentage-based levies, or the configured fixed amount per kilogram for per-kg levies.

*Acceptance criterion:* Society levy 2% of gross on Tea entry GrossPayment UGX 54,000 → LevyAmount = UGX 1,080; this appears as a line item on the deductions breakdown.

**FR-COOP-041** — When a union levy is configured for a commodity season, the system shall apply the union levy as a separate deduction line from the society levy, remit the union levy amount to the union's ledger account, and display both levies as distinct line items on the farmer's payment breakdown.

*Acceptance criterion:* Society levy = UGX 1,080 (2%) and union levy = UGX 540 (1%) both appear as separate lines on the payment breakdown; total deductions = UGX 1,620 (assuming no loan).

**FR-COOP-042** — When an administrator configures a levy, the system shall require: levy name, levy type (percentage of gross / fixed amount per kg), rate or amount, applicable commodity, applicable society or union, and effective season, and persist the levy record as active.

*Acceptance criterion:* A "NAEB Export Levy" at 1.5% of gross for Rwanda Arabica coffee in the 2025 season is saved and applied on the next intake entry for a Rwanda tenant.

**FR-COOP-043** — When a levy is deactivated mid-season, the system shall stop applying that levy to intake entries created after the deactivation date and retain it on all entries created before that date.

*Acceptance criterion:* Levy deactivated 2025-04-15 → entries dated 2025-04-14 retain the levy; entries dated 2025-04-16 do not include it.

## 5.5 Mobile Money Bulk Payment

**FR-COOP-044** — When a payment officer initiates a bulk payment run for a season and collection centre, the system shall:

1. Aggregate all approved, unpaid intake entries.
2. Compute the net payment per farmer (gross minus all deductions).
3. Generate a payment batch record with a unique batch reference, total payout amount, farmer count, and status "Pending".
4. Present the payment batch for supervisor approval before disbursement.

*Acceptance criterion:* A bulk run for 200 farmers produces a batch record with the correct total (independently verified) and status "Pending"; no disbursement is initiated without approval.

**FR-COOP-045** — When a supervisor approves the payment batch, the system shall submit individual payment instructions to the configured Mobile Money API (MTN Mobile Money Uganda / Airtel Money Uganda / M-Pesa Kenya) for each farmer using the farmer's registered default MoMo number and net payment amount.

*Acceptance criterion:* Batch approval triggers API calls to the configured provider; each call includes the correct farmer phone number, amount, and batch reference as the transaction reference.

**FR-COOP-046** — When the Mobile Money API returns a success callback for a farmer payment, the system shall mark that farmer's payment record as "Paid", record the provider transaction ID, and update the batch completion counter.

When the API returns a failure callback (insufficient float, invalid number, or provider error), the system shall mark the specific farmer's payment as "Failed", log the provider error code and description, and allow the payment officer to retry the failed payment separately without re-initiating the entire batch.

*Acceptance criterion:* A batch of 10 where 8 succeed and 2 fail produces 8 "Paid" records and 2 "Failed" records with logged error codes; the retry function re-submits only the 2 failed records.

**FR-COOP-047** — When the system has submitted payment instructions and not received a callback within the provider timeout window (configurable, default 120 seconds), the system shall mark the payment status as "Pending — Awaiting Confirmation" and alert the payment officer: "Payment to [Farmer Name] ([phone]) is awaiting confirmation after [timeout] seconds."

*Acceptance criterion:* A simulated API timeout of 130 seconds (10 seconds past the 120-second threshold) triggers the alert; the record is marked "Pending — Awaiting Confirmation".

**FR-COOP-048** — When the payment batch is fully reconciled (all entries are "Paid", "Failed", or "Cancelled"), the system shall update the batch status to "Completed", post the disbursement journal entry to the Accounting module (Module 01), and mark the corresponding intake entries as "Payment Processed".

*Acceptance criterion:* A batch with 198 "Paid" and 2 "Cancelled" entries transitions to "Completed", a journal debit to Farmer Payables and credit to Cash/MoMo Float is posted in Module 01, and all 200 intake entries are marked "Payment Processed".

[CONTEXT-GAP: MTN Mobile Money Uganda API version and authentication method (API key vs. OAuth 2.0) — confirm to specify the integration contract.]

[CONTEXT-GAP: Airtel Money Uganda API sandbox availability for testing bulk disbursement.]

[CONTEXT-GAP: Float management — confirm whether float balance checking is a pre-disbursement gate or handled by the provider API response only.]
