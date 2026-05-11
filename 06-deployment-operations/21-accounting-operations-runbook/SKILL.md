---
name: accounting-operations-runbook
description: Generate operations runbooks for embedded accounting systems: go-live opening balances, period close, ledger integrity jobs, reconciliation failures, duplicate/missing postings, report rebuilds, materialized balance rebuilds, FX revaluation, depreciation, payroll remittance checks, locked-period exceptions, audit evidence packs, and first-close support.
metadata:
  portable: true
---

# Accounting Operations Runbook

## Use When

- Deploying, operating, migrating, or supporting a system with an embedded ledger.
- Planning go-live, month-end close, audit support, or incident response for accounting data.

## Required Runbook Sections

1. Opening balance migration and sign-off.
2. Posting queue monitoring and retry policy.
3. Nightly per-tenant integrity job and alert routing.
4. Period close checklist.
5. Locked-period exception workflow.
6. Duplicate posting incident procedure.
7. Missing posting incident procedure.
8. Subledger reconciliation failure procedure.
9. Inventory, payroll, fixed asset, tax, and bank/mobile-money reconciliation procedures.
10. Materialized balance and report rebuild command.
11. Audit evidence export pack.
12. First month-end close support plan.

## Safety Rules

- NEVER fix accounting incidents by editing journal lines.
- NEVER unlock a period without named approval, reason, timestamp, and post-close recheck.
- MUST take a backup before migration, opening-balance import, report-cache rebuild, or bulk mapping change.
- MUST preserve source documents and posting-rule versions used at the time of posting.

## Outputs

- Accounting operations runbook.
- Close checklist.
- Incident playbooks.
- Audit evidence checklist.
