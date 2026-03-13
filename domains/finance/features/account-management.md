# Feature: Account Management

## Description
Core financial account lifecycle management — account opening, customer identity
verification (KYC), account configuration, balance inquiries, statements, and
account closure with regulatory holds.

## Standard Capabilities
- New account application and onboarding workflow
- KYC identity verification (name, DOB, address, government ID)
- Beneficial ownership collection for legal entity accounts
- Account type configuration (checking, savings, money market, credit)
- Balance inquiry and transaction history retrieval
- Statement generation (monthly, on-demand, PDF/CSV export)
- Account alerts and notification preferences
- Account closure workflow with regulatory hold validation
- Dormant account detection and escheatment processing

## Regulatory Hooks
- FinCEN CIP Rule (31 CFR 1020.220): identity verification mandatory at account opening
- BSA Beneficial Ownership Rule (31 CFR 1010.230): collect UBO for legal entities
- CFPB: account disclosures (fee schedules, terms) must be provided at opening
- State escheatment laws: dormant accounts must be reported and remitted to the state

## Linked NFRs
- FIN-NFR-001 (Financial Audit Trail)
- FIN-NFR-003 (Card Data Security — for debit card issuance)
- FIN-NFR-004 (Availability — account inquiry is customer-facing)
