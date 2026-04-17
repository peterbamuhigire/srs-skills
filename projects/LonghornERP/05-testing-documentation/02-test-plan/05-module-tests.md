# Add-On Module Test Cases

This section covers the Point of Sale (POS), Sales Agent Commission, Cooperative Intake, and Asset Depreciation modules.

## Point of Sale (POS)

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-POS-001 | `PosSessionTest` | `test_open_session_records_float_and_sets_status` | Cashier opens a POS session with an opening float | `cashier_id`; `till_id`; `opening_float` = UGX 50,000 | Session record created; `status` = `OPEN`; `opening_float` = 50,000 stored as integer |
| TC-POS-002 | `PosTransactionTest` | `test_transaction_decrements_stock_and_posts_gl` | Record a sale of 3 line items paid by cash | 3 product lines with quantities and unit prices; `payment_method` = `CASH`; open session | Receipt record created; `stock_ledger` gains 1 row per line item (quantity OUT); GL posted: DR Cash, CR Revenue per line, CR VAT Output where applicable |
| TC-POS-003 | `PosSessionTest` | `test_close_session_flags_cash_discrepancy` | Close a session where declared cash differs from expected | `session_id`; `declared_cash` differs from system-calculated expected by any amount > 0 | Session `status` = `CLOSED`; `cash_discrepancy` field = declared − expected (signed integer); discrepancy flagged in session record; Z-report generated |

## Sales Agent Commission

Commission amounts are calculated in UGX using integer arithmetic.

### Flat Rate

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-AGENT-001 | `CommissionCalculationTest` | `test_flat_rate_commission_calculated_correctly` | Flat 5% commission rule on attributed sales | `attributed_sales` = 10,000,000 UGX; `rate` = 5% | Commission = 10,000,000 × 5 / 100 = 500,000 UGX (integer arithmetic) |

### Tiered Rate

The tiered formula is: $Commission = \sum_{t=1}^{n} (min(Sales, Tier_t^{upper}) - Tier_t^{lower}) \times Rate_t$

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-AGENT-002 | `CommissionCalculationTest` | `test_tiered_commission_calculated_correctly` | Tiered rule: UGX 0–5,000,000 = 3%; UGX 5,000,001–10,000,000 = 5%; total sales = UGX 7,000,000 | `attributed_sales` = 7,000,000; tiered rate config as described | Tier 1: 5,000,000 × 3% = 150,000; Tier 2: 2,000,000 × 5% = 100,000; Total commission = 250,000 UGX (integer match) |

### Commission Run Approval and Payout

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-AGENT-003 | `CommissionRunTest` | `test_approve_commission_run_queues_momo_bulk_payment` | Approve commission run for multiple agents | `commission_run_id` with calculated totals; session with `commissions.approve` | MoMo bulk payment request enqueued; each agent's record in the queue contains the correct UGX integer amount; run `status` = `APPROVED` |

## Cooperative Intake

Cooperative intake net pay formula: $NetPay = (Quantity \times UnitPrice) - LoanDeduction - (Quantity \times UnitPrice \times LevyRate)$

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-COOP-001 | `CoopIntakeTest` | `test_intake_net_pay_calculated_correctly` | Record 500 kg Grade A at UGX 2,000/kg; loan deduction UGX 50,000; levy rate 2% | `quantity` = 500; `unit_price` = 2000; `loan_deduction` = 50,000; `levy_rate` = 2 | Gross = 500 × 2,000 = 1,000,000; levy = 1,000,000 × 2% = 20,000; net = 1,000,000 − 50,000 − 20,000 = 930,000 UGX (integer match) |
| TC-COOP-002 | `CoopIntakeOfflineTest` | `test_offline_intake_syncs_on_reconnect` | Record intake while device has no network; restore network connection | Intake record created offline; network restored | Record persisted in local store within 5 s of creation; sync completed within 30 s of network restoration; server record matches local record exactly |

## Asset Depreciation

### Straight-Line Depreciation

The monthly straight-line depreciation formula is: $MonthlyDepreciation = \frac{Cost - ResidualValue}{UsefulLifeMonths}$

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-ASSET-001 | `DepreciationTest` | `test_straight_line_monthly_depreciation_correct` | Asset cost UGX 12,000,000; residual value UGX 0; useful life 5 years (60 months) | `cost` = 12,000,000; `residual` = 0; `life_months` = 60 | Monthly depreciation = 12,000,000 / 60 = 200,000 UGX (integer); total depreciation over 60 months = 12,000,000 UGX |

### Reducing Balance Depreciation

The annual reducing balance depreciation formula is: $AnnualDepreciation = NBV \times Rate$

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-ASSET-002 | `DepreciationTest` | `test_reducing_balance_annual_depreciation_correct` | Net Book Value (NBV) = UGX 10,000,000; annual depreciation rate = 20% | `nbv` = 10,000,000; `rate` = 20 | Annual depreciation = 10,000,000 × 20 / 100 = 2,000,000 UGX (integer); remaining NBV after Year 1 = 8,000,000 UGX |
