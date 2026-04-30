# Finance: Architecture Patterns

## Financial Data Isolation

- Cardholder data environment (CDE) must be network-segmented from all other systems
- Never store raw PANs, CVV2/CVC2, or magnetic stripe data post-authorization
- Financial account balances must reside in a dedicated, encrypted schema
- Non-production environments must use tokenized or synthetic data — never real account numbers

## Double-Entry Ledger Pattern

Every financial transaction must produce balanced journal entries:

```
DEBIT  account_id=1001  amount=500.00  currency=USD
CREDIT account_id=2001  amount=500.00  currency=USD
```

- The sum of all debits must always equal the sum of all credits ($\sum Debits = \sum Credits$)
- Ledger entries are immutable; corrections are made via offsetting entries, never by modifying existing records
- Each entry must reference the originating transaction ID, timestamp, and authorizing user
- General ledger and subledgers must stay distinct. AR, AP, inventory, fixed assets, payroll, tax, and bank/cash subledgers reconcile to GL control accounts.
- Users must not post directly to control accounts except through controlled adjustment workflows with reason, approval, and audit trail.
- Posted entries should carry management dimensions where required: legal entity, branch, cost centre, profit centre, project, fund, product/service, location, and tax code.

## Transaction Atomicity (ACID Guarantee)

Financial transactions must satisfy all four ACID properties:

| Property | Implementation |
|---|---|
| **Atomicity** | All ledger entries in a transaction commit together or roll back entirely |
| **Consistency** | Account balance constraints (e.g., no negative balance without overdraft) enforced at commit |
| **Isolation** | Serializable isolation level for balance updates; no dirty reads on account balances |
| **Durability** | Committed transactions persisted to write-ahead log before acknowledging success |

- Use database transactions with explicit BEGIN/COMMIT/ROLLBACK
- Implement idempotency keys on all payment API endpoints to prevent double-posting

## Record-to-Report and Close Pattern

- Fiscal periods must be explicit records with open, closing, closed, and reopened states.
- Period close must include reconciliation checkpoints for bank/cash, AR, AP, inventory, fixed assets, payroll, tax, suspense, and intercompany where applicable.
- Accruals, prepayments, depreciation, provisions, revaluations, foreign-exchange remeasurement, and correction journals must be posted before close.
- Reopening a closed period requires permission, reason, approval, audit trail, and downstream report refresh.
- Financial statements must regenerate from ledger source data and expose period, entity, currency, and consolidation scope.

## Management and Cost Accounting Pattern

- Cost centres and profit centres are reporting dimensions, not substitutes for GL accounts.
- Standard costing systems must retain standard version/effective date and calculate price/rate, usage/efficiency, volume, yield/mix, and overhead variances where data exists.
- Flexible budget reports must compare actual cost against the budget adjusted for actual activity level.
- Contribution margin reports must separate variable costs from fixed costs for pricing, break-even, and capacity decisions.

## Audit Trail for Financial Events

Every financial event must produce an immutable audit log entry:

```json
{
  "audit_id": "uuid",
  "timestamp": "ISO-8601",
  "transaction_id": "string",
  "user_id": "string",
  "user_role": "string",
  "action": "INITIATE | APPROVE | REJECT | REVERSE | EXPORT",
  "account_id": "string",
  "amount": "decimal",
  "currency": "ISO-4217",
  "ip_address": "string",
  "outcome": "SUCCESS | FAILURE | PENDING"
}
```

Audit logs must be:
- Write-once (no UPDATE/DELETE permitted)
- Retained for minimum 7 years (SOX requirement)
- Queryable by account ID, user ID, transaction ID, and date range

## Fraud Detection Pipeline

```
Transaction Event → Feature Extraction → Risk Scoring Engine → Decision (APPROVE / REVIEW / DECLINE)
                                                ↓
                                        Alert Queue → Fraud Analyst
```

- Risk scoring must complete within 200ms for real-time payment authorization
- Model inputs: transaction amount, merchant category, geographic velocity, device fingerprint, behavioral baseline
- Declined transactions must not reveal fraud scoring rationale to the cardholder (security through obscurity)

## Segregation of Duties (Maker-Checker)

- **Maker:** User who initiates a transaction or configuration change
- **Checker:** Separate user who reviews and approves; must not be the same person as the maker
- High-value transactions (above configurable threshold) require dual approval
- System must enforce maker-checker at the data layer, not solely at the UI layer
