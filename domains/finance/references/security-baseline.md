# Finance: Security Baseline

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| At Rest (account data) | AES-256-GCM | 256-bit |
| In Transit | TLS 1.2+ (TLS 1.3 preferred) | — |
| Card PAN (stored token map) | AES-256 | 256-bit |
| Backups | AES-256 | 256-bit |
| Key Encryption Keys (KEK) | RSA-4096 or AES-256 | 256-bit / 4096-bit |

## Card Data Tokenization (PCI-DSS)

- Raw PAN must be replaced with a payment token within the authorization response
- Token vault must reside in a separate, hardened system outside the primary application
- Card Verification Values (CVV2/CVC2) must never be stored after authorization, even encrypted
- Hardware Security Modules (HSM) must be used for all cryptographic key operations in the CDE
- Key custodians must operate under split knowledge and dual control (no single person holds a complete key)

## Authentication Requirements

- Multi-Factor Authentication (MFA) mandatory for all users accessing financial account data
- Privileged access (admin, maker-checker approver) requires hardware token (FIDO2/WebAuthn)
- Session timeout: 10 minutes inactivity for financial transaction interfaces
- Password policy: minimum 14 characters with complexity requirements
- Account lockout: 5 failed attempts → 30-minute lockout with security alert
- Service accounts must use certificate-based authentication, not passwords

## SOX Access Controls

- Principle of least privilege enforced on all roles
- Access provisioning requires documented business justification
- Quarterly access certification reviews for all personnel with financial system access
- Immediate revocation upon role change or termination (< 1 hour SLA)
- Shared accounts prohibited; each user must have a unique identifier
- All privileged actions (schema changes, batch overrides) require dual approval

## Role Separation (Maker-Checker)

| Role | Permitted Actions |
|---|---|
| Maker | Initiate transactions, create payment instructions |
| Checker | Approve or reject maker submissions |
| Auditor | Read-only access to transaction and audit logs |
| Compliance Officer | Access to SAR/CTR reporting, read-only account data |
| System Admin | Infrastructure configuration, no access to financial account data |

## Network Security

- CDE must be isolated in a dedicated network segment with firewall rules explicitly permitting only required traffic
- No direct internet access to database or ledger tier
- WAF required on all public payment-facing endpoints
- All CDE-to-CDE communications must use mutual TLS
- Penetration testing of the CDE: annually minimum (PCI-DSS Req. 11.4)

## Vulnerability Management

| Severity | Remediation SLA |
|---|---|
| Critical | 24 hours |
| High | 7 days |
| Medium | 30 days |

- OWASP Top 10 compliance required for all web-facing payment interfaces
- Static Application Security Testing (SAST) in CI/CD pipeline

## Business Continuity

- RTO (Recovery Time Objective): ≤ 2 hours for transaction processing systems
- RPO (Recovery Point Objective): ≤ 15 minutes for account balance data
- Backup testing: monthly
- DR failover testing: bi-annually
