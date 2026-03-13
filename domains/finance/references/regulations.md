# Finance: Regulations & Standards Reference

## PCI-DSS v4.0 (Payment Card Industry Data Security Standard)

| Requirement | Citation | Scope |
|---|---|---|
| Protect Cardholder Data | PCI-DSS v4.0 Req. 3 | Encryption and storage restrictions on PANs, CVV, track data |
| Control Access | PCI-DSS v4.0 Req. 7–8 | Least-privilege access, unique IDs, MFA for cardholder data environment |
| Monitor and Test | PCI-DSS v4.0 Req. 10–11 | Audit log retention (12 months), vulnerability scanning, pen testing |
| Secure Transmission | PCI-DSS v4.0 Req. 4 | TLS 1.2+ for all cardholder data in transit |
| Network Segmentation | PCI-DSS v4.0 Req. 1 | CDE must be isolated from out-of-scope networks |

### Key PCI-DSS Technical Controls

- **Tokenization:** Replace PAN with a non-sensitive token; raw PAN must never be stored post-authorization
- **Truncation:** Display only last 4 digits of PAN in UI and logs
- **Key Management:** Cryptographic keys must be managed per PCI-DSS Req. 3.7 (rotation, split knowledge, dual control)

## SOX (Sarbanes-Oxley Act)

| Section | Requirement |
|---|---|
| Section 302 | CEO/CFO personal certification of financial report accuracy |
| Section 404 | Annual assessment of internal controls over financial reporting (ICFR) |
| Section 802 | Criminal penalties for alteration or destruction of audit records |

### SOX Technical Controls

- Immutable audit trail for all financial transactions and system access
- Segregation of duties: no single user may initiate and approve a financial transaction
- Change management controls: all system changes must be logged with approver
- Quarterly access reviews for all personnel with access to financial systems

## BSA/AML (Bank Secrecy Act / Anti-Money Laundering)

- **Currency Transaction Reports (CTR):** Mandatory filing for cash transactions exceeding $10,000 (31 U.S.C. §5313)
- **Suspicious Activity Reports (SAR):** Filing required within 30 days of suspicious activity detection (31 CFR 1020.320)
- **Customer Due Diligence (CDD):** Verify beneficial ownership for legal entity customers (31 CFR 1010.230)
- **Transaction Monitoring:** Automated monitoring systems required to detect structuring and layering patterns

## KYC (Know Your Customer — FinCEN)

- **Customer Identification Program (CIP):** Verify name, DOB, address, and ID number at account opening (31 CFR 1020.220)
- **Beneficial Ownership Rule:** Identify and verify individuals owning 25%+ of legal entity customers
- **Enhanced Due Diligence (EDD):** Required for high-risk customers, politically exposed persons (PEPs), and correspondent banks
- **Ongoing Monitoring:** Periodic re-verification of customer identity based on risk rating

## GDPR / CCPA (Data Privacy)

| Regulation | Jurisdiction | Key Rights |
|---|---|---|
| GDPR | EU/EEA residents | Right to access, rectification, erasure (with financial record exceptions), portability |
| CCPA | California residents | Right to know, delete, opt-out of sale |

- Financial institutions must balance privacy rights against mandatory record retention obligations
- Data minimization: collect only data necessary for the stated financial service purpose
- Privacy notices must be provided at account opening and updated annually
