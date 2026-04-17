# 3. F-005: Financial Accounting and General Ledger

## 3.1 Module Overview

Module F-005 is the accounting engine of the BIRDC ERP. It implements IFRS for SMEs double-entry accounting with dual-mode operation: simultaneous tracking of PIBID parliamentary budget votes as cost-centre segments and BIRDC commercial IFRS accounts. Every operational transaction across all 17 modules posts to the GL automatically. The GL maintains a cryptographic hash chain (BR-013) that makes tampering mathematically detectable by any auditor.

## 3.2 Chart of Accounts Management

### FR-GL-001

**Stimulus:** The Finance Director submits a new account record specifying account code, name, account type (Asset, Liability, Equity, Revenue, or Expense), parent account, department, and control-account flag.

**Response:** The system validates that the account code is unique, the parent account exists in the hierarchy, and the account type is one of the 5 permitted types. On validation success, the system creates the account, adds it to the hierarchical Chart of Accounts tree, and returns confirmation with the new account code. If the control-account flag is set to true, the system records the account as a control account and blocks direct manual posting to it from all journal entry screens (enforced at API layer).

**Verification:** Create a control account; attempt a manual journal entry to it; confirm the API returns HTTP 422 with error code `ERR_CONTROL_ACCOUNT`.

---

### FR-GL-002

**Stimulus:** The Finance Director submits an account edit request (name or description only — code and type are immutable after creation).

**Response:** The system updates the account name and description, records the change in the audit trail with the editor's identity, old value, new value, and timestamp. The system does not permit changes to account code, account type, or parent after the account has received any posted transaction.

**Verification:** Attempt to change the account type of an account with a posted transaction; confirm the API returns HTTP 422 with error code `ERR_ACCOUNT_IMMUTABLE_AFTER_POST`.

---

### FR-GL-003

**Stimulus:** A user requests the Chart of Accounts list view with optional filters for account type, department, or active status.

**Response:** The system returns the hierarchical account list displaying account code, name, type, parent, department, balance (current period), and control-account flag. Indentation in the UI reflects parent-child depth. Response time ≤ 800 ms at P95 for the full 1,307-account list on standard BIRDC server hardware.

[CONTEXT-GAP: GAP-012] — The Finance Director must confirm whether the existing 1,307-account structure is to be imported from a legacy system or designed from scratch. The database design and GL module cannot be finalised until this is resolved.

---

### FR-GL-004

**Stimulus:** The Finance Director submits a request to deactivate an account.

**Response:** The system checks that the account has a zero balance in all open periods and has no child accounts. If both conditions are satisfied, the system sets the account status to inactive, preventing any future posting. If either condition fails, the system returns HTTP 422 with the specific blocking condition. Deactivated accounts remain visible in historical reports.

---

### FR-GL-005

**Stimulus:** The system receives a dual-mode account configuration request assigning a PIBID parliamentary vote code and department segment to an existing GL account.

**Response:** The system records the vote code and cost-centre segment against the account. Any transaction posted to this account thereafter is reportable both as a parliamentary vote expenditure under the assigned vote code and as an IFRS expense under the account's standard classification. Both views draw from the same posted journal entry — no data is duplicated.

**Verification:** Post a transaction to a dual-mapped account; run the parliamentary vote report and the IFRS P&L report; confirm the same amount appears in both with correct classification labels.

## 3.3 Journal Entry Management

### FR-GL-006

**Stimulus:** An Accounts Assistant submits a manual journal entry with one or more debit lines and one or more credit lines, each specifying account, amount, currency, cost centre, description, and supporting document reference.

**Response:** The system validates: (a) $\sum Debits = \sum Credits$ — if debits ≠ credits, the system rejects the entry with error code `ERR_UNBALANCED_JE` and returns the imbalance amount; (b) no line posts to a control account; (c) the accounting period is open; (d) no line posts to an inactive account. On full validation success, the system saves the entry in `draft` status, assigns a sequential draft reference number, and timestamps the creation with the submitter's identity.

**Verification:** Submit a JE where $\sum Debits \neq \sum Credits$; confirm rejection with `ERR_UNBALANCED_JE` and zero records written to the GL table.

---

### FR-GL-007

**Stimulus:** A Finance Manager submits approval for a journal entry currently in `draft` status.

**Response:** The system validates: (a) the approver is not the same user who created the entry (BR-003 segregation of duties — enforced at API layer); (b) the entry remains balanced; (c) the period is still open. On success, the system transitions the entry status from `draft` to `approved` and records the approver's identity and timestamp. If the approver is the creator, the system returns HTTP 403 with error code `ERR_SOD_VIOLATION`.

**Verification:** Log in as User A, create a JE; log in as User A and attempt to approve the same JE; confirm HTTP 403.

---

### FR-GL-008

**Stimulus:** The Finance Manager triggers posting of an approved journal entry.

**Response:** The system: (a) assigns a permanent sequential Journal Entry number in format `JE-YYYY-NNNN` where YYYY is the fiscal year and NNNN is a zero-padded sequential integer with no gaps (BR-009); (b) writes each line to the GL detail table with the JE number, account, debit/credit amount, currency, cost centre, period, and timestamp; (c) updates the running balance of each affected account; (d) computes and stores the SHA-256 hash of the new GL entry concatenated with the hash of the immediately preceding entry in the chain (BR-013); (e) transitions entry status to `posted`. The entire operation executes within a single database transaction — if any step fails, all steps are rolled back.

**Verification:** Post a JE; confirm JE number is sequential with no gaps; query the GL hash field; verify it equals SHA-256(current entry data + previous entry hash).

---

### FR-GL-009

**Stimulus:** A Finance Manager submits a reversal request for a posted journal entry, specifying the reversal date and reason.

**Response:** The system creates a new journal entry that is the exact mirror of the original (debits become credits, credits become debits), assigns a new `JE-YYYY-NNNN` number, records a reference to the original JE number in the reversal description, and posts it to the specified reversal date's period (which must be open). The original entry is flagged `reversed` with a pointer to the reversal JE number. The original entry is never deleted or modified.

**Verification:** Post a JE; request reversal; confirm reversal JE has inverted debit/credit lines and references the original JE number; confirm original JE shows `reversed` status with reversal pointer.

---

### FR-GL-010

**Stimulus:** An Accounts Assistant requests the Journal Entry list with filters for date range, account, cost centre, JE number, or status.

**Response:** The system returns a paginated list of JEs matching the filters, displaying JE number, date, description, total debit, status, creator, and approver. Each row is expandable to show all line items. Filters are applied server-side. Response time ≤ 1,000 ms at P95 for a 12-month date range on standard server hardware.

---

### FR-GL-011

**Stimulus:** The Finance Director requests the GL detail for a specific account for a date range.

**Response:** The system returns all posted journal entry lines affecting the account within the date range, displaying date, JE number, description, debit amount, credit amount, and running balance after each entry. The running balance column is calculated as a real-time accumulation from the account's inception balance. Export to Excel (PhpSpreadsheet) and PDF (mPDF) available.

## 3.4 GL Auto-Posting from Operational Modules

### FR-GL-012

**Stimulus:** A sales invoice is confirmed in F-001 (Sales and Distribution).

**Response:** The system automatically creates and posts a balanced journal entry: DR Accounts Receivable (customer account) / CR Revenue (product revenue account) for the invoice net amount, and DR Cost of Goods Sold / CR Inventory for the standard cost of the items sold. The JE description references the invoice number. No manual entry is required or permitted for this transaction.

---

### FR-GL-013

**Stimulus:** A payment receipt is recorded in F-006 (Accounts Receivable) and allocated to one or more invoices.

**Response:** The system automatically posts: DR Bank or Cash (appropriate account per payment method) / CR Accounts Receivable (customer account) for the receipt amount. The JE description references the receipt number and allocated invoice numbers.

---

### FR-GL-014

**Stimulus:** A stock adjustment is approved in F-003 (Inventory and Warehouse Management).

**Response:** The system automatically posts: DR Inventory Adjustment Expense / CR Inventory (for negative adjustments) or DR Inventory / CR Inventory Gain (for positive adjustments) for the FIFO or moving-average value of the adjusted quantity. The JE references the stock adjustment approval number.

---

### FR-GL-015

**Stimulus:** A vendor payment is authorised and processed in F-007 (Accounts Payable).

**Response:** The system automatically posts: DR Accounts Payable (vendor account) / CR Bank or Cash (appropriate account per payment method). If WHT applies, the posting is: DR Accounts Payable / CR Bank or Cash (net amount) and CR WHT Payable (WHT amount). The JE references the payment voucher number.

---

### FR-GL-016

**Stimulus:** A farmer bulk payment file is confirmed in F-007 (Accounts Payable).

**Response:** The system automatically posts: DR Cooperative Payable (aggregated per cooperative) / CR Bank or Mobile Money (net payment total) and DR Deductions Payable / CR relevant deduction accounts (loan repayments, levies, transport). All farmer-level individual records are traceable to this single bulk posting via the cooperative payable sub-ledger.

---

### FR-GL-017

**Stimulus:** A purchase order is received via GRN in F-009 (Procurement — Phase 3, future integration point).

**Response:** The system automatically posts: DR Raw Material Inventory / CR Goods Received Not Invoiced (GRNI) at PO price. On vendor invoice matching and approval: DR GRNI / CR Accounts Payable (vendor account). This requirement specifies the GL interface contract for Phase 3 integration; the Phase 3 procurement module must call the GL auto-post API endpoint with the standard payload format defined in the API integration specification.

---

### FR-GL-018

**Stimulus:** The Finance Director activates the GL auto-posting configuration for a new operational module.

**Response:** The system records the module-to-account mapping (debit account, credit account, journal description template, and triggering transaction type) in the configuration table `tbl_gl_posting_rules`. All subsequent transactions of the specified type from that module use the configured mapping without code changes (DC-002).

**Verification:** Add a new posting rule via UI; trigger the specified transaction type; confirm the GL receives the correct debit/credit entry per the rule without any code deployment.

## 3.5 Hash Chain Integrity

### FR-GL-019

**Stimulus:** The Finance Director or an authorised auditor triggers an on-demand GL hash chain integrity check, optionally scoped to a specific account or date range.

**Response:** The system recalculates the SHA-256 hash chain for every GL entry in the specified scope in sequential order. For each entry, it compares the stored hash against the recomputed hash of (entry data + previous entry hash). The system generates an integrity report displaying: total entries checked, entries passing verification (count and percentage), any broken links (entry ID, position in chain, expected hash prefix, actual stored hash prefix). If all entries pass, the report status is `INTEGRITY_VERIFIED`. If any entry fails, the report status is `INTEGRITY_BREACH_DETECTED` with the specific entry IDs flagged. The report is written to the audit log with the requestor's identity and timestamp.

**Verification (BR-013):** Directly update a GL entry in the database; trigger the integrity check; confirm the report status is `INTEGRITY_BREACH_DETECTED` and identifies the tampered entry ID.

---

### FR-GL-020

**Stimulus:** The system detects a hash chain breach during an automated nightly integrity scan (scheduled task).

**Response:** The system immediately sends an email and SMS alert to the Finance Director and IT Administrator, logs the breach event in the security audit log with the affected entry IDs, and sets a system-wide `GL_INTEGRITY_ALERT` flag that displays a banner on the Finance Director's dashboard until acknowledged. The system does not suspend GL operations — it continues recording while the breach is investigated.

## 3.6 Running Balances and Trial Balance

### FR-GL-021

**Stimulus:** A user requests the Trial Balance for a specific date (not restricted to month-end).

**Response:** The system computes the debit and credit balance for every active GL account as of the specified date by aggregating all posted journal entry lines up to and including that date. The Trial Balance is displayed with columns for account code, account name, debit balance, and credit balance. Total debits must equal total credits — the system validates this before rendering and flags any imbalance as a system error requiring IT investigation. Export to Excel and PDF available. Response time ≤ 3,000 ms at P95 for the full 1,307-account Trial Balance.

---

### FR-GL-022

**Stimulus:** Any GL posting event occurs (any journal entry is posted to any account).

**Response:** The system updates the running balance field (`current_balance`) of every affected account within the same database transaction as the posting. The running balance is always current to the last posted transaction and is never batch-recalculated at period-end.

**Verification:** Post a JE; immediately query `tbl_gl_accounts.current_balance` for the affected accounts; confirm the balance reflects the posted amounts without delay.

## 3.7 Accounting Period Management

### FR-GL-023

**Stimulus:** The Finance Director opens a new accounting period, specifying period name, start date, end date, and period type (monthly, quarterly, or annual) within a configured fiscal year.

**Response:** The system validates: (a) the period does not overlap with any existing period in the same fiscal year; (b) the start date is the day after the previous period's end date (no gaps in the fiscal calendar). On success, the system creates the period with status `open` and makes it available as a posting target for all GL entries.

---

### FR-GL-024

**Stimulus:** The Finance Director closes an accounting period.

**Response:** The system sets the period status to `closed`. All subsequent attempts to post a journal entry dated within a closed period are rejected with error code `ERR_PERIOD_CLOSED`. A closed period can only receive entries via a reversal transaction dated in the current open period that references the original closed-period entry. The closing action is recorded in the audit trail with the Finance Director's identity and timestamp.

**Verification:** Close a period; attempt to post a backdated JE to it; confirm `ERR_PERIOD_CLOSED` rejection.

---

### FR-GL-025

**Stimulus:** The Finance Director configures a dual fiscal year: PIBID fiscal year (July 1 — June 30) and BIRDC commercial fiscal year (January 1 — December 31).

**Response:** The system supports both fiscal year calendars simultaneously. Each journal entry is tagged with the applicable fiscal period for both calendars (PIBID period and commercial period). Period-end reports can be generated for either calendar without creating duplicate entries. The Finance Director selects the reporting calendar when generating any period-based financial statement.

## 3.8 Multi-Currency

### FR-GL-026

**Stimulus:** An Accounts Assistant records a foreign-currency transaction (USD, EUR, or KES) specifying the transaction currency, transaction amount, and the exchange rate in effect on the transaction date.

**Response:** The system records the transaction in the source currency and immediately calculates and stores the UGX functional-currency equivalent using the provided exchange rate ($\text{UGX Amount} = \text{Foreign Amount} \times \text{Exchange Rate}$). All GL postings are made in UGX. The original foreign currency amount and exchange rate are stored in the transaction record for audit and reporting.

---

### FR-GL-027

**Stimulus:** The Finance Director triggers a period-end foreign currency revaluation for all open foreign-currency AR and AP balances.

**Response:** The system retrieves the closing exchange rate for the revaluation date from the configured exchange rate table, calculates the revalued UGX balance for each open foreign-currency item ($\text{Revalued Balance} = \text{Outstanding Foreign Amount} \times \text{Closing Rate}$), computes the unrealised FX gain or loss ($\text{FX Variance} = \text{Revalued Balance} - \text{Carrying Balance}$), and automatically posts a journal entry: DR/CR Unrealised FX Gain/Loss (P&L account) / CR/DR respective AR or AP account. The revaluation journal is reversible.

---

### FR-GL-028

**Stimulus:** A foreign-currency AR invoice is fully settled by a payment received at a different exchange rate than the invoice rate.

**Response:** The system calculates the realised FX gain or loss: $\text{Realised FX} = \text{Invoice UGX Value} - \text{Payment UGX Value}$. The system automatically posts the realised FX gain or loss to the configured FX Gain/Loss account. The AR balance for that invoice is cleared to zero.

## 3.9 Financial Statements

### FR-GL-029

**Stimulus:** A Finance Director or Finance Manager requests a Profit and Loss (P&L) statement for a specified period (monthly, quarterly, or annual) and reporting mode (BIRDC commercial or PIBID parliamentary).

**Response:** The system aggregates all posted revenue and expense account balances for the specified period and reporting mode. The P&L is structured as: Revenue less Cost of Goods Sold equals Gross Profit; Gross Profit less Operating Expenses equals Operating Profit; Operating Profit adjusted for non-operating items equals Net Profit Before Tax. All figures are presented in UGX. Comparative period column available (prior month or prior year same period). Export to Excel and PDF (mPDF) available. Response time ≤ 5,000 ms at P95 for a full-year P&L.

---

### FR-GL-030

**Stimulus:** A user requests a Balance Sheet as of a specified date and reporting mode.

**Response:** The system aggregates all posted asset, liability, and equity account balances as of the specified date. The Balance Sheet is structured per IFRS for SMEs: current assets, non-current assets, current liabilities, non-current liabilities, and equity. The system validates $\text{Total Assets} = \text{Total Liabilities} + \text{Equity}$ before rendering and flags any imbalance as a system integrity alert. Export to Excel and PDF available.

---

### FR-GL-031

**Stimulus:** A user requests a Cash Flow Statement for a specified period.

**Response:** The system generates an IAS 7-compliant Cash Flow Statement using the indirect method, classifying cash movements into three sections: operating activities (net profit adjusted for non-cash items and working capital changes), investing activities (capital expenditure and disposals), and financing activities (loan proceeds, repayments, capital contributions). The account-to-section mapping is configurable by the Finance Director (DC-002). Export to Excel and PDF available.

[CONTEXT-GAP: GAP-012] — Accurate Cash Flow statement generation requires the Finance Director to confirm and map each GL account to its IAS 7 cash flow classification. This mapping cannot be defaulted without the confirmed Chart of Accounts.

---

### FR-GL-032

**Stimulus:** A user requests a GL Detail Report for a specific account, date range, and cost centre (optional).

**Response:** The system returns all posted journal entry lines for the specified account within the date range, showing opening balance, each transaction (date, JE number, description, debit, credit, running balance), and closing balance. Export to Excel and PDF available.

---

### FR-GL-033

**Stimulus:** A user requests a Dual-Mode Consolidated Report for a specified period.

**Response:** The system generates a side-by-side report showing: (a) BIRDC IFRS P&L or Balance Sheet, and (b) PIBID parliamentary vote expenditure by vote code for the same period. Both columns draw from the same posted journal entries, reclassified by the dual-mode account mapping. A consolidated view combining both entities is available as a third column, with intercompany eliminations applied if configured.

## 3.10 GL Audit Trail

### FR-GL-034

**Stimulus:** Any user performs any action on any GL record (create, approve, post, reverse, view integrity check result, period open/close).

**Response:** The system writes an immutable audit log entry to `tbl_audit_log` recording: actor user ID, actor name, IP address, action type, target record ID and table, timestamp (UTC), old values (JSON), and new values (JSON). Audit log entries cannot be updated or deleted by any application user, including IT Administrator. Retention period: 7 years (Uganda Companies Act Cap 110 and Income Tax Act Cap 340 compliance).

---

### FR-GL-035

**Stimulus:** The Finance Director or Auditor General (OAG) requests an audit trail report filtered by user, date range, action type, or GL account.

**Response:** The system returns a paginated, searchable audit trail report meeting the filter criteria. Each row shows: timestamp, user, action, record ID, description of change. Export to PDF and Excel available. The report includes a cover page confirming the filter parameters and the total record count so the auditor can verify completeness.

## 3.11 GL Configuration

### FR-GL-036

**Stimulus:** The Finance Director configures a new fiscal year specifying the year label, start date, end date, and applicable reporting mode (PIBID, BIRDC, or both).

**Response:** The system creates the fiscal year record, makes it available for period creation under FR-GL-023, and does not auto-create periods (each period within the fiscal year is created individually to accommodate irregular fiscal calendars).

---

### FR-GL-037

**Stimulus:** The IT Administrator configures the exchange rate table, specifying currency code, effective date, and UGX rate.

**Response:** The system stores the rate with its effective date. When a foreign-currency transaction is recorded, the system auto-selects the rate whose effective date is closest to and not after the transaction date. Manual rate override is permitted for individual transactions with Finance Manager approval, logged in the audit trail.

---

### FR-GL-038

**Stimulus:** The Finance Director configures the account mapping for a GL posting rule (module, transaction type, debit account, credit account, description template).

**Response:** The system saves the rule to `tbl_gl_posting_rules` and applies it immediately to all subsequent transactions of the specified type without requiring a system restart or code deployment (DC-002). The Finance Director can also update or deactivate a posting rule; deactivation requires a confirmation warning that affected transactions will not auto-post until a replacement rule is configured.

---

### FR-GL-039

**Stimulus:** An Accounts Assistant requests a lookup of GL accounts matching a partial account code or name during journal entry line entry.

**Response:** The system returns matching accounts via a Select2 searchable dropdown response within 300 ms, filtering out control accounts and inactive accounts from the selectable list.

---

### FR-GL-040

**Stimulus:** The Finance Director requests a Gap Detection report for journal entry numbering (BR-009).

**Response:** The system scans the JE number sequence for the specified fiscal year and reports any gaps (e.g., JE-2025-1045 followed by JE-2025-1047 with no JE-2025-1046). For each gap found, the report shows: the missing number, the preceding JE number and date, the subsequent JE number and date. Voided entries are shown as present (marked VOID) — they are not treated as gaps. The report is accessible by the Finance Director and IT Administrator only.
