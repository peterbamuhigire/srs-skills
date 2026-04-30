# Maduuka Accounting and Bookkeeping Uplift

## Purpose

This note applies bookkeeping, accounting controls, POS accounting, and finance-dashboard guidance to Maduuka requirements and design work.

## Product Implications

- Keep the user experience owner-friendly: users enter sales, purchases, expenses, cashups, mobile money receipts, stock movements, and supplier/customer balances; the system posts clean accounting behind the scenes.
- Sales, returns, discounts, VAT/tax where enabled, cash/mobile money/card receipts, credit sales, and bad-debt write-offs should flow to AR/revenue/tax/cash accounts through posting rules.
- Stock purchases, stock sales, shrinkage, expiry, owner withdrawals, petty cash, supplier bills, and supplier payments should reconcile to inventory, COGS, AP, expenses, and cash/bank accounts.
- Provide simple but rigorous reports: daily cashup, sales summary, profit estimate, stock value, receivables, payables, expense categories, tax-ready summary, and owner dashboard.
- Add checks for unbalanced entries, unreconciled cash/mobile money, negative stock, duplicate supplier invoices, unpaid customer balances, and missing expense categories.

## Requirement Prompt

Every Maduuka transaction should have a friendly business label and a hidden accounting effect. The system should let micro-business users understand cash, profit, debtors, creditors, stock value, and tax exposure without requiring them to know debits and credits.
