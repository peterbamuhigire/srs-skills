# Accounting ERP Implementation Patterns

Use this reference for ERP, POS, school-fee, healthcare-billing, retail, manufacturing, grants, payroll, inventory, and finance systems that need bookkeeping or accounting correctness.

## Functional Requirement Themes

- The system shall maintain a configurable chart of accounts with account type, normal balance, parent account, reporting line, tax relevance, active status, and tenant/legal-entity scope.
- The system shall generate balanced journal entries from source transactions and reject unbalanced postings.
- The system shall separate GL from subledgers for AR, AP, inventory, fixed assets, payroll, tax, bank/cash, and grants/funds where relevant.
- The system shall reconcile subledger schedules to GL control accounts and expose unreconciled differences.
- The system shall support fiscal periods, closed-period locks, controlled reopening, recurring journals, reversing journals, accruals, prepayments, depreciation, provisions, and write-offs.
- The system shall support source-document linkage for invoices, receipts, bills, POs, delivery notes, stock movements, payroll, bank/mobile money statements, tax evidence, and contracts.
- The system shall support cost centres, profit centres, branches, departments, projects, funds, products/services, and locations as posting dimensions where the domain requires management reporting.
- The system shall support maker-checker controls for high-risk finance actions: payments, supplier bank changes, write-offs, stock adjustments, manual journals, payroll approval, tax filing, and closed-period changes.

## Posting and Reconciliation Rules

- AR aging total must reconcile to the AR control account.
- AP aging total must reconcile to the AP control account.
- Inventory valuation must reconcile to inventory control accounts by item, location, category, or valuation class.
- Fixed asset register net book value must reconcile to fixed asset cost less accumulated depreciation.
- Bank and mobile money reconciliation must explain every difference between statement and book balance.
- Payroll reports must reconcile gross pay, deductions, employer contributions, net pay, and payroll liabilities.
- Tax schedules must reconcile VAT/sales tax, WHT, PAYE, import duties, or other statutory liabilities to returns and payment evidence.

## Management and Cost Accounting Requirements

- The system shall classify costs as fixed/variable, direct/indirect, controllable/non-controllable, and one-time/recurring where management reporting requires it.
- The system shall support budgets and flexible-budget variance reporting by cost centre, profit centre, branch, project, product, service, or department.
- Manufacturing, processing, construction, and repeatable-service systems shall support standard cost, actual cost, variance, yield/scrap, overhead allocation, and contribution margin reporting where in scope.
- Dashboards shall distinguish financial accounting reports from management accounting reports so statutory truth and operational decisions are not mixed.

## Non-Functional and Control Requirements

- Monetary values shall use fixed precision decimal types, never floating point.
- Posted ledger entries shall be immutable; corrections shall use reversal, adjustment, debit note, credit note, write-off, or controlled reopening.
- Every finance event shall include actor, timestamp, source document, workflow status, approval chain, IP/device where available, and audit reference.
- Finance reports shall be reproducible from source postings and shall disclose data freshness, period, currency, and entity scope.
- Spreadsheet exports shall include control totals and should preserve account codes and source IDs for re-import or audit testing.

## Project-Specific Application Prompts

- LonghornERP: strengthen finance core with GL, subledgers, close, treasury, fixed assets, tax, cost centres, profit centres, consolidation-ready dimensions, and management packs.
- Maduuka: make POS sales, stock, cashup, mobile money, receivables, payables, expenses, and owner-friendly reports post into clean bookkeeping without exposing debit/credit complexity to micro users.
- BIRDC-ERP: link farmer purchases, production batches, inventory, export sales, grants, assets, and cost centres to auditable finance and cost accounting.
- Medic8: link patient billing, insurance claims, pharmacy inventory, lab billing, receipts, refunds, debtors, facility cost centres, and statutory reports to controlled accounting.
- AcademiaPro: link fees, scholarships, bursaries, payments, arrears, payroll, procurement, grants, campuses, and school funds to subledger and GL controls.
