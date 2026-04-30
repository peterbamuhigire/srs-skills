# LonghornERP Accounting, Bookkeeping, and Costing Uplift

## Purpose

This note applies accounting, bookkeeping, ERP finance, cost accounting, and finance-workbook guidance to LonghornERP requirements and design work.

## Product Implications

- Keep `ACCOUNTING` as the finance backbone: GL, AR, AP, inventory accounting, fixed assets, payroll postings, tax, bank/cash, period close, and management reporting.
- Require subledger control-account reconciliation for AR, AP, inventory, fixed assets, payroll, tax, and bank/mobile money.
- Extend finance dimensions for legal entity, branch, cost centre, profit centre, project, fund, product/service, location, and tax code.
- Strengthen close orchestration: reconciliation checklist, accruals, prepayments, depreciation, provisions, recurring/reversing journals, trial balance review, and controlled reopening.
- Add cost-accounting depth for manufacturing, services, projects, and branches: standard cost, actual cost, contribution margin, flexible budget, variance, cost centre, and profit centre reporting.
- Treat Excel exports as audit-friendly artefacts with account codes, source IDs, control totals, period/currency metadata, and check totals.

## Requirement Prompt

Any LonghornERP finance or operational module that creates financial impact should define its posting rule, source document, subledger effect, GL control account, approval rule, reversal path, period-close treatment, and management-reporting dimensions.
