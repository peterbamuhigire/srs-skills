# SRS module coverage matrix

Create rows from discovered capabilities, not menus or schema. No row is
`SUPPORTED` until its application boundary and evidence are named.

| Module family | Required journey prompts | Evidence prompts |
|---|---|---|
| Identity, tenant, RBAC | onboarding, grants/denies, suspension, offboarding, facility scope | role matrix, audit, attribution, cross-tenant denial |
| Core business | create, edit, approve, cancel, complete, search, empty state | state machine, validation, duplicate/replay, report inclusion |
| People/service delivery | customers/patients/members/staff, appointments/queues, documents, communication | privacy/consent, role access, lineage, recovery |
| Purchasing/inventory | suppliers, requisitions, PO, receipt, batches/expiry, transfers, sale/dispense, adjustment | approval separation, quantity/valuation, variance, rollback |
| Billing/finance | invoice, payment, refund, claim, expense, asset, close, reconciliation | balanced source events, period lock, AR/AP, cash, drilldown |
| HR/payroll | employee, attendance, leave, payroll, approval, payslip, payment | preparer/approver, deductions/contributions, register-to-ledger |
| Reports/admin/integrations | dashboards, exports, audit, settings, support, webhooks, mobile/offline | filters, empty/large reports, export restriction, side-effect adapter |

For a hospital, add appointments, triage, encounters, diagnoses linked to the
default coding catalogue, orders, laboratory results, prescriptions, dispensing,
claims, billing, payments, stock, and clinical privacy. For another domain, replace
these with the product's discovered business journeys while retaining the same
coverage dimensions.
