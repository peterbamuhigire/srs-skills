# Retail: Security Baseline

## PCI Scope Minimization

- Reduce the Cardholder Data Environment (CDE) to the smallest possible footprint
- Use hosted payment fields or redirect to payment service provider to prevent PAN from touching application servers
- Network segmentation must isolate the CDE from all out-of-scope retail systems
- Scope reduction via tokenization must be validated by a Qualified Security Assessor (QSA) or SAQ attestation

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| At Rest (customer PII) | AES-256-GCM | 256-bit |
| In Transit | TLS 1.2+ (TLS 1.3 preferred) | — |
| Payment tokens at rest | AES-256 | 256-bit |
| Backups | AES-256 | 256-bit |

## Card Tokenization

- All payment card numbers must be tokenized prior to storage; raw PANs must not be logged or persisted
- CVV/CVC must not be stored at any point, even temporarily, after the transaction authorization request
- Displayed card numbers must be truncated to last 4 digits in all UI and printed receipts
- Payment tokens must be network-specific and non-reversible without the token vault

## 3D Secure for Card-Not-Present Transactions

- 3D Secure 2.x must be implemented for all card-not-present (CNP) transactions on e-commerce channels
- Exemption thresholds (e.g., SCA exemptions under EU PSD2) must be configurable per market
- 3DS authentication results must be stored and associated with the order record for chargeback defense

## Fraud Scoring

- All online orders must receive a fraud risk score before payment authorization
- Signals: device fingerprint, IP geolocation, email age, billing-shipping address mismatch, velocity
- High-risk orders must be routed to manual review queue; fulfillment must be held pending disposition
- Fraud rules must be configurable without code deployment (rules engine with admin UI)

## GDPR Consent Management

- Cookie consent banner must be displayed on first visit for EU/EEA visitors before any non-essential cookies are set
- Consent must be recorded with timestamp, IP (truncated), and consent version
- Withdrawing consent must immediately disable associated cookies and tracking
- Consent records must be retained for the lifetime of the user account plus 1 year

## Authentication Requirements

- Staff and admin accounts: MFA mandatory
- Customer accounts: MFA optional (strongly encouraged for accounts with stored payment methods)
- Session timeout: 15 minutes inactivity for admin interfaces; 30 minutes for customer-facing
- Account lockout: 10 failed attempts → 30-minute lockout with email notification to account owner

## Vulnerability Management

| Severity | Remediation SLA |
|---|---|
| Critical | 48 hours |
| High | 14 days |
| Medium | 60 days |

- Annual penetration test of the CDE and e-commerce platform
- OWASP Top 10 compliance required for all customer-facing web applications
