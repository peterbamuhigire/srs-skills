---
name: embedded-accounting-engine-srs
description: Generate the SRS subsection for any system that handles money, inventory value, payroll, tax, grants, fees, payments, receivables, payables, fixed assets, or financial reporting. Specifies embedded accounting engine requirements: chart of accounts, mapping layer, LedgerPostingService, append-only journals, subledgers, accounting periods, reversals, reports, audit trail, IFRS/IFRS for SMEs/local tax context, and integrity invariants.
metadata:
  portable: true
---

# Embedded Accounting Engine SRS

## Use When

- The system records sales, expenses, inventory, payroll, school fees, clinic billing, grants, donations, payments, loans, assets, wallets, or tax.
- The SRS must prove the product can replace routine external bookkeeping software for the operating entity.

## Do Not Use When

- The product only exports data to an external accounting system and never owns the books.
- Accounting treatment depends on a current law, tax rate, or professional judgement not provided in the brief; write a verification requirement instead of inventing the answer.

## Required SRS Subsections

Add these to functional requirements for every money-handling system:

1. Accounting standard and compliance profile: IFRS for SMEs by default, full IFRS where required, or project-specific local GAAP.
2. Chart of accounts: tenant-specific CoA cloned from an industry template, account types, control accounts, status, currency, and report rollups.
3. Mapping layer: product categories, expense categories, payment methods, tax rates, payroll components, asset categories, donor funds, and inventory categories mapped to accounts.
4. Posting engine: one `LedgerPostingService` write path, idempotency key, period validation, account validation, debit-credit validation, and atomic database transaction.
5. Journal model: append-only `journal_entries` and `journal_lines`; no edits or soft deletes; reversing journals only.
6. Subledgers: AR, AP, inventory, fixed assets, payroll, tax, bank/mobile money, grants/funds implemented through tagged journal lines or reconciled registers.
7. Accounting periods: open, closed, locked states; no posting to locked periods except approved reopening workflow.
8. Reports: trial balance, income statement, statement of financial position, cash flow statement, statement of changes in equity/net assets, GL detail, ageing, tax schedules, inventory valuation, payroll liabilities, fixed asset register, donor/fund reports where relevant.
9. Integrity invariants: balanced entries, control-account reconciliation, inventory tie-out, period enforcement, idempotency enforcement, tenant isolation, rebuildable balances.
10. Audit trail: actor, timestamp, source document, posting rule version, mapping changes, CoA changes, reversals, exports, and close approvals.

## Requirement Wording Pattern

Use testable requirements:

```text
FR-ACC-001 The system shall post every accounting entry through a single LedgerPostingService.
FR-ACC-002 The system shall reject any journal entry whose total debits do not equal total credits.
FR-ACC-003 The system shall prevent updates, deletes, or soft deletes of posted journal lines.
FR-ACC-004 The system shall correct posted accounting errors only by posting reversing journals linked to the original journal.
FR-ACC-005 The system shall run a nightly per-tenant accounting integrity check and alert operators on failure.
```

## Compliance And Standards Template

```text
Accounting standard: IFRS for SMEs / full IFRS / local GAAP: [fill in]
Functional currency: [fill in]
Presentation currency, if different: [fill in]
Tax regime: [fill in]
VAT/sales tax regime: [fill in]
Payroll statutory regime: [fill in]
External sign-off required: statutory audit / tax filing / donor audit / board approval: [fill in]
Current-rate verification owner: [role/person]
```

## Outputs

- SRS accounting-engine functional requirements.
- Compliance and standards section.
- Requirements traceability entries for accounting invariants.
- Open verification items for current tax/regulatory rates.
