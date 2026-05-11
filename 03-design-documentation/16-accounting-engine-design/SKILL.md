---
name: accounting-engine-design
description: Generate the SDS/HLD/LLD design for an embedded accounting engine: canonical data model, append-only journal tables, chart of accounts, mapping tables, accounting periods, LedgerPostingService interface, idempotency, reversal workflow, subledger tagging, materialized balance rebuilds, audit trail, and IFRS/IFRS for SMEs reporting projections.
metadata:
  portable: true
---

# Accounting Engine Design

## Use When

- The approved SRS includes money-handling or embedded accounting requirements.
- A design document must specify the accounting write path, schema, services, reports, and invariants.

## Hard Rules

- NEVER design a direct write path from sales, inventory, payroll, payments, or assets into ledger tables.
- NEVER design mutable posted journals.
- MUST show how materialized balances rebuild from journal lines.
- MUST include `tenant_id` on accounting tables unless explicitly single-tenant.

## Canonical Data Model

Required tables:

- `chart_of_accounts`
- `account_mappings`
- `posting_rule_versions`
- `journal_entries`
- `journal_lines`
- `accounting_periods`
- `accounting_integrity_runs`
- `accounting_audit_log`

Recommended supporting tables:

- `tax_rates`
- `exchange_rates`
- `inventory_cost_layers`
- `fixed_assets`
- `payroll_runs`
- `bank_accounts`
- `funds` for NGOs and donor-funded projects

## LedgerPostingService Interface

```php
interface LedgerPostingService
{
    public function post(JournalEntry $entry): PostedJournal;
}
```

The design shall document validations for debit-credit equality, tenant scope, open period, active accounts, idempotency key, source document state, mapping completeness, currency policy, and database transaction boundaries.

## Design Sections To Produce

1. Accounting context and standard profile.
2. Service boundaries and event producers.
3. Account resolver and mapping tables.
4. Posting service contract.
5. Database schema and constraints.
6. Reversal and correction workflow.
7. Period close and lock workflow.
8. Subledger and control-account reconciliation.
9. Report projection and cache rebuild strategy.
10. Audit trail and tamper-evidence strategy.
11. Operational jobs: nightly integrity, report rebuild, FX revaluation, depreciation, payroll remittance checks.

## Outputs

- SDS/HLD/LLD accounting-engine section.
- ERD/table specification.
- Service interface and sequence diagram text.
- Reconciliation and report rebuild design.
