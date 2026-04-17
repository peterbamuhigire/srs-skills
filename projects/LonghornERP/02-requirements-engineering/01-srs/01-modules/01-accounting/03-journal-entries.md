# Journal Entry Requirements

## 3.1 Overview

Journal entries are the atomic unit of the General Ledger (GL). Every financial event — whether originated manually or auto-posted from a sub-ledger module — is recorded as a journal entry consisting of one or more debit lines and one or more credit lines that sum to equality. This section specifies requirements for manual entry, double-entry enforcement, auto-generation, reversal, immutability, and audit trail.

## 3.2 Manual Journal Entry

**FR-ACCT-018:** The system shall allow an authorised user to create a manual journal entry by providing the following header fields: journal date, reference number (auto-generated or user-supplied), description (free text, max 255 characters), and at least 1 debit line and 1 credit line, each specifying GL account, amount, and optional narration.

**FR-ACCT-019:** The system shall allow a journal entry to contain an unlimited number of debit and credit lines, subject to the constraint that the sum of all debit amounts equals the sum of all credit amounts before posting is permitted.

**FR-ACCT-020:** The system shall allow an authorised user to save a journal entry in *Draft* status without posting, enabling retrieval, editing, and deletion prior to posting.

**FR-ACCT-021:** The system shall validate that the journal date falls within an open accounting period when the user submits a journal for posting; if the date falls in a closed period, the system shall apply the soft-close or hard-close rule as defined in FR-ACCT-093 and FR-ACCT-094.

**FR-ACCT-022:** The system shall auto-generate a unique, sequential journal reference number per tenant in the format `JNL-{YYYY}-{NNNNNN}` when the user does not supply a reference number, where `{YYYY}` is the journal year and `{NNNNNN}` is a zero-padded integer incrementing from 000001.

## 3.3 Double-Entry Enforcement

**FR-ACCT-023:** The system shall reject a journal posting request and return HTTP 422 with the error message "Debit total [{amount}] does not equal credit total [{amount}]. Journal cannot be posted." when the sum of debit lines does not equal the sum of credit lines.

**FR-ACCT-024:** The system shall display a running debit total, credit total, and difference indicator on the journal entry form, updated in real time as the user adds or modifies lines, so that the user can correct imbalances before submitting.

**FR-ACCT-025:** The system shall reject a journal posting request when any line references a deactivated GL account and shall return a validation error identifying the offending line number and account code.

**FR-ACCT-026:** The system shall reject a journal posting request when any line references a GL account that belongs to a different tenant than the authenticated user's tenant.

## 3.4 Auto-Generated Journals from Sub-ledger Posting

**FR-ACCT-027:** The system shall auto-create and post a GL journal entry when a Sales module invoice is confirmed, mapping revenue lines to the configured Revenue account, tax lines to the VAT Control (Output) account, and the total to the Accounts Receivable account.

**FR-ACCT-028:** The system shall auto-create and post a GL journal entry when a Purchases module invoice is confirmed, mapping expense/asset lines to the configured expense or asset accounts, tax lines to the VAT Control (Input) account, and the total to the Accounts Payable account.

**FR-ACCT-029:** The system shall auto-create and post a GL journal entry when a payment is recorded in the Payments module, debiting or crediting the bank/cash account and the corresponding payable or receivable account.

**FR-ACCT-030:** The system shall auto-create and post a GL journal entry when a payroll run is confirmed in the HR module, mapping gross pay to the configured Salaries Expense account, PAYE deductions to the PAYE Payable account, and net pay to the Bank/Cash account.

**FR-ACCT-031:** The system shall tag every auto-generated journal with the `source_module` field set to the originating module name (e.g., `sales`, `purchases`, `payments`, `payroll`) and the `source_document_id` field set to the originating document's primary key.

**FR-ACCT-032:** The system shall prevent manual editing of any auto-generated journal entry; the edit controls shall be hidden and an informational message shall indicate that the entry was auto-posted from the source module.

## 3.5 Journal Reversal

**FR-ACCT-033:** The system shall create a reversal journal entry when an authorised user selects the *Reverse* action on a posted journal; the reversal entry shall contain the same lines as the original but with debit and credit amounts swapped, dated on the first calendar day of the accounting period immediately following the original journal's period.

**FR-ACCT-034:** The system shall link the reversal journal to the original journal via a `reversal_of` foreign key, and shall display a cross-reference link in the UI on both the original and reversal journal detail screens.

**FR-ACCT-035:** The system shall set the status of a reversed journal to *Reversed* and shall prevent a second reversal from being initiated on a journal that already has status *Reversed*.

**FR-ACCT-036:** The system shall require the user to enter a reversal reason (free text, max 255 characters) before the reversal journal is created.

## 3.6 Immutability and Corrections

**FR-ACCT-037:** The system shall set a posted journal's status to *Posted* and shall prevent any UPDATE or DELETE operation on the `journals` or `journal_lines` tables for that record by any user role, including Super Admin; the only permitted corrective action is reversal per FR-ACCT-033.

**FR-ACCT-038:** The system shall hide the *Edit* and *Delete* controls on all posted journals in the UI; only the *Reverse* and *View* actions shall be available.

## 3.7 Audit Trail

**FR-ACCT-039:** The system shall record the following audit fields on every journal entry at the point of posting: `created_by` (user ID), `created_at` (UTC timestamp), `posted_by` (user ID), `posted_at` (UTC timestamp), `source_module`, and `ip_address` of the posting request.

**FR-ACCT-040:** The system shall display the audit trail fields defined in FR-ACCT-039 on the journal detail screen in a read-only section labelled *Posting History*.

**FR-ACCT-041:** The system shall record a timestamped audit log entry when a reversal is initiated, capturing `initiated_by`, `initiated_at`, `reversal_reason`, and the `journal_id` of both the original and reversal journals.

**FR-ACCT-042:** The system shall provide a searchable *Journal Audit Log* report accessible to Super Admin and Finance Manager roles, filterable by date range, user, source module, and journal status.
