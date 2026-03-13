# Domain: Finance

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | SEC, FINRA, OCC, CFPB, FinCEN |
| **Key Standards** | PCI-DSS v4.0, SOX Sections 302/404, AML (BSA), KYC (FinCEN), Basel III |
| **Risk Level** | High — financial data, fraud risk |
| **Audit Requirement** | Mandatory — SOX requires immutable audit trails |
| **Data Classification** | Financial Account Data, Cardholder Data (CHD), Personally Identifiable Information (PII) |

## Default Feature Modules

- Account Management
- Transaction Processing
- Reporting & Compliance
- Fraud Detection

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new finance projects at scaffold time.

Key injected areas:
- **NFR:** SOX audit logging, PCI-DSS encryption, transaction atomicity, fraud detection latency
- **FR:** KYC identity verification, AML transaction monitoring, suspicious activity reporting
- **Interfaces:** Core banking system integration, payment network APIs (Visa/Mastercard), regulatory reporting feeds

## References

- [regulations.md](references/regulations.md) — PCI-DSS, SOX, BSA/AML, KYC, GDPR/CCPA
- [architecture-patterns.md](references/architecture-patterns.md) — financial data isolation, double-entry ledger, ACID, audit trail
- [security-baseline.md](references/security-baseline.md) — AES-256, TLS 1.2+, tokenization, HSM, maker-checker
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection

## Feature Reference

- [account-management.md](features/account-management.md)
- [transaction-processing.md](features/transaction-processing.md)
- [reporting-compliance.md](features/reporting-compliance.md)
- [fraud-detection.md](features/fraud-detection.md)
