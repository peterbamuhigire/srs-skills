# Feature: Reporting & Compliance

## Description
Regulatory reporting and internal financial controls reporting — SOX control
documentation, AML/BSA filing, KYC risk reporting, and management information
system (MIS) dashboards for compliance oversight.

## Standard Capabilities
- SOX control evidence collection and documentation portal
- Suspicious Activity Report (SAR) creation and FinCEN e-filing
- Currency Transaction Report (CTR) automated generation and filing
- AML transaction monitoring alert management and case disposition
- KYC risk rating reports and EDD case tracking
- Regulatory capital and Basel III reporting outputs
- General ledger trial balance and financial statement generation
- Income statement, balance sheet, cash flow, AR/AP aging, fixed asset register, inventory valuation, bank reconciliation, tax schedules, and management pack outputs
- Budget vs actual, flexible-budget variance, standard-cost variance, cost-centre, profit-centre, project, branch, and contribution-margin reporting where applicable
- Audit log search and export (by user, account, date range, transaction type)
- Immutable report archive with tamper-evident storage

## Regulatory Hooks
- SOX Section 302/404: internal controls documentation must be auditable by external auditors
- BSA/FinCEN: SAR filing within 30 days of suspicious activity detection
- BSA/FinCEN: CTR filing within 15 calendar days of triggering transaction
- OCC: national bank examination readiness — audit trail must be producible on demand

## Linked NFRs
- FIN-NFR-001 (Financial Audit Trail — reports must reference immutable source logs)
- FIN-NFR-003 (Card Data Security — reports must mask PANs per PCI-DSS Req. 3.3)
- FIN-NFR-004 (Availability — compliance dashboards must be accessible for regulators)
