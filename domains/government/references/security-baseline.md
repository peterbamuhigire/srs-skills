# Government: Security Baseline

## FIPS 140-2 Cryptographic Modules

- All cryptographic operations must use FIPS 140-2 validated modules (Level 1 minimum; Level 2+ for sensitive data)
- FIPS-approved algorithms only: AES-256, SHA-256/SHA-384, RSA-3072+, ECDSA P-256+
- Non-FIPS algorithms (MD5, SHA-1, DES, 3DES) are prohibited on federal systems
- Cryptographic module validation certificates must be current (CMVP certificate not expired)

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| At Rest (citizen PII, CUI) | AES-256-GCM (FIPS 140-2) | 256-bit |
| In Transit | TLS 1.2+ with FIPS-approved cipher suites | — |
| Database fields (SSN, biometrics) | AES-256 field-level | 256-bit |
| Backups | AES-256 | 256-bit |
| Key Management | NIST SP 800-57 | Key rotation annually minimum |

## PIV / CAC Card Support

- Personal Identity Verification (PIV) cards (FIPS 201) required for all federal employees and contractors
- Common Access Cards (CAC) required for Department of Defense systems
- Systems must support PIV/CAC authentication via PKIX certificate validation
- PIV/CAC must be the primary authentication mechanism for all internal staff; passwords alone are prohibited
- Derived PIV credentials required for mobile device access to government systems

## Continuous Monitoring (ISCM — Information Security Continuous Monitoring)

- Per NIST SP 800-137 and OMB M-14-03: ongoing monitoring of security controls, not annual-only assessment
- Automated vulnerability scanning: monthly at minimum; critical systems weekly
- Configuration compliance scanning: weekly against approved baselines (DISA STIGs or CIS Benchmarks)
- Security metrics must be reported to agency CISO dashboard in near-real-time
- Plan of Action and Milestones (POA&M) required for all identified weaknesses; tracked to closure

## Supply Chain Risk Management (C-SCRM)

- Per NIST SP 800-161: agencies must assess and manage risks from the ICT supply chain
- Software Bill of Materials (SBOM) required for all procured software (OMB M-22-18)
- Third-party components must be assessed for known vulnerabilities before deployment
- Contracts must include security requirements and right-to-audit clauses for vendors

## Insider Threat Controls

- User and Entity Behavior Analytics (UEBA) required for high-impact systems
- Privileged access management (PAM): just-in-time access for admin accounts; sessions recorded
- Separation of duties: no single individual may have unrestricted access to production data and audit logs
- Background investigations: Tier 2 investigation minimum for personnel with access to moderate-impact systems

## Authentication Requirements

- All government system users: phishing-resistant MFA mandatory (PIV/CAC or FIDO2)
- Session timeout: 15 minutes inactivity for classified and CUI systems; 30 minutes for public-facing portals
- Password policy: minimum 15 characters; no complexity requirements (per NIST SP 800-63B); no 90-day forced rotation
- Account lockout: 3 failed attempts → immediate lockout pending administrator review for high-impact systems

## Vulnerability Management

| Severity | Remediation SLA |
|---|---|
| Critical | 15 days (OMB M-22-01 / CISA BOD 22-01) |
| High | 30 days |
| Medium | 180 days |

- Known Exploited Vulnerabilities (KEV) catalog (CISA): mandatory patching within BOD 22-01 deadlines
- Annual penetration test with Rules of Engagement approved by the authorizing official
