---
name: accounting-engine-test-plan
description: Generate mandatory accounting-engine test plans for systems that handle money: debit-credit equality, trial balance, balance sheet equation, control-account-to-subledger reconciliation, inventory GL tie-out, period locks, idempotency keys, reversal-only correction, tenant isolation, report rebuilds, payroll/FX/fixed-asset/inventory posting tests, and no direct ledger writes.
metadata:
  portable: true
---

# Accounting Engine Test Plan

## Use When

- The system has an embedded ledger, billing, inventory valuation, payroll, tax, grants, or financial statements.
- A release can affect posted journals, balances, accounting periods, or reports.

## Mandatory Test Suites

1. Balanced journal tests: every journal entry has equal debits and credits.
2. Posting service tests: all writes pass through `LedgerPostingService`; direct table writes fail review/CI checks.
3. Idempotency tests: duplicate source event with same key does not double-post.
4. Period tests: open periods allow posting; closed/locked periods reject posting unless approved workflow exists.
5. Reversal tests: corrections create linked reversing journals; original lines remain unchanged.
6. Subledger tests: AR/AP/customer/supplier balances equal control accounts.
7. Inventory tests: GL inventory equals stock-on-hand value by item/location/cost layer; sale posts COGS.
8. Fixed asset tests: asset register equals GL cost and accumulated depreciation; disposal gain/loss is correct.
9. Payroll tests: gross pay, employer cost, employee deductions, liabilities, net pay, and remittances reconcile.
10. FX tests: transaction-date rates, settlement differences, and month-end revaluation post realised/unrealised gains/losses correctly.
11. Report tests: trial balance, income statement, statement of financial position, cash flow, and equity/net-asset reports regenerate from journal lines.
12. Tenant isolation tests: one tenant cannot read or post to another tenant's accounts, mappings, periods, or journals.

## Acceptance Criteria Pattern

```text
Given a locked accounting period
When a business module attempts to post a sale dated in that period
Then the posting service rejects the entry
And no journal header or line is inserted
And the rejection names the locked period and source document.
```

## Outputs

- Accounting test plan.
- Invariant matrix.
- Test data scenarios.
- Release-blocking acceptance criteria.
