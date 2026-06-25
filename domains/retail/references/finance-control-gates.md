# Retail Finance and Control Gates for SRS

Retail software commonly changes inventory value, margin, cash/POS settlement, refund liabilities, vendor funding, and management reporting. When any of the triggers below appear, the SRS must route to the Chwezi accounting and finance doctrine engine before release.

## Finance Trigger Matrix

| Trigger | Required finance/control coverage |
|---|---|
| Inventory receipt, transfer, adjustment, stock count, shrink, damage, quarantine, disposal | Inventory costing method, stock movement audit trail, count variance approval, write-down/reversal path, GL handoff. |
| Price change, promotion, coupon, manual discount, markdown | Price approval, margin floor, offer stack control, effective date, reason code, source event, markdown reporting. |
| Sale, payment, refund, exchange, credit note, split tender, mobile money, card settlement, cash drawer | POS/payment reconciliation, settlement matching, refund approval, tender variance, exception queue. |
| Return, restock, repair, dispose, vendor return | Disposition status, inventory valuation impact, refund liability, customer communication, reverse logistics cost. |
| Loyalty points, vouchers, gift cards, store credit, wallet balance | Issuance and redemption evidence, liability or deferred income route, expiry policy, fraud controls. |
| Vendor allowances, rebates, co-op funding, scanbacks, trade spend recovery | Agreement evidence, accrual logic, claim workflow, dispute status, recovery reconciliation. |
| Private label landed cost, supplier quality hold, packaging approval | Cost build-up, duty/freight allocation, quality release, write-off or rework evidence. |
| Retail dashboard, WBR, management pack | Metric definition, source lineage, reconciliation to subledger/GL where financial. |

## Mandatory SRS Sections

If any trigger is in scope, the SRS must include:

1. Source event catalogue for each retail finance event.
2. Posting or reporting handoff contract: event ID, source system, timestamp, actor, amount, currency, tax, account/dimension hint, evidence pointer, idempotency key.
3. Approval and segregation-of-duties rules for manual discounts, refunds, stock adjustments, markdown overrides, and vendor claims.
4. Reconciliation workflow for POS, payment gateway, card settlement, mobile money, cash drawer, refunds, and inventory subledger.
5. Exception queue with owner, severity, evidence missing, due date, and reviewer role.
6. Audit log retention requirements for pricing, promotion, stock, payment, refund, and supplier-funding events.
7. Dashboard lineage from KPI to source transaction or reconciled management-accounting dataset.

## Requirement Templates

### Retail Event Idempotency

The system shall assign a globally unique, immutable event ID and idempotency key to every retail source event that can affect inventory, customer balance, payment settlement, revenue, discount, refund, vendor funding, or management reporting.

**Verifiability:** Replay the same event payload 3 times. The system shall create 1 accepted source event, reject or mark the duplicates as idempotent replays, and preserve the original audit trail.

### Manual Discount Approval

The system shall require approval for any manual discount above the configured threshold or below the configured margin floor before the discount can be applied to a sale.

**Verifiability:** Attempt a manual discount above threshold using a cashier role. The system shall block checkout completion until an authorised approver records approval, reason code, effective transaction, and audit note.

### Inventory Variance Control

The system shall route stock count variances above the configured tolerance to an exception queue before posting an inventory adjustment.

**Verifiability:** Close a stock count with a variance above tolerance. The system shall hold the adjustment, show exception status, require controller approval, and create an audit record linking count sheet, variance reason, approver, and posting event.

### Dashboard Lineage

The system shall expose source lineage for each financial KPI in the retail dashboard, including source system, refresh timestamp, transformation rule, and reconciliation status.

**Verifiability:** Select gross margin, markdown rate, return rate, shrink rate, and vendor funding recovery in the dashboard. Each KPI shall show source lineage and the latest reconciliation status without manual spreadsheet lookup.

## Finance Engine Route

Use these finance-engine skills when the SRS touches their topic:

- `skills/11-sector-and-fund-accounting/retail-and-pos-accounting-pack/SKILL.md`
- `skills/04-subledgers-and-operations/inventory-costing-and-stock-accounting/SKILL.md`
- `skills/04-subledgers-and-operations/pos-and-cash-drawer-management/SKILL.md`
- `skills/09-budgeting-fpa-and-costing/pricing-discounts-rebates-and-refunds/SKILL.md`
- `skills/10-controls-governance-and-fraud/internal-controls-library/SKILL.md`
- `skills/06-close-consolidation-and-reporting/audit-ready-reporting-pack/SKILL.md`
