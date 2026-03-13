# Healthcare: Security Baseline

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| At Rest | AES-256-GCM | 256-bit |
| In Transit | TLS 1.2+ | — |
| Database fields (PHI) | AES-256 field-level | 256-bit |
| Backups | AES-256 | 256-bit |

## Authentication Requirements

- Multi-Factor Authentication (MFA) mandatory for all clinical staff
- Session timeout: 15 minutes inactivity for clinical workstations
- Password policy: minimum 12 characters, complexity requirements
- Account lockout: 5 failed attempts → 30-minute lockout
- Privileged accounts require hardware token (FIDO2/WebAuthn)

## Access Control Baseline

- Principle of least privilege on all roles
- Access reviews every 90 days
- Immediate access revocation on staff termination (< 1 hour SLA)
- Shared accounts prohibited
- Service accounts must have minimal scoped permissions

## Network Security

- PHI systems must reside in private subnets
- No direct internet access to database tier
- WAF required on all public-facing endpoints
- Network segmentation between clinical and administrative systems
- VPN required for remote administrative access

## Vulnerability Management

- Critical patches: 72 hours
- High patches: 30 days
- Penetration testing: annually minimum
- OWASP Top 10 compliance required

## Business Continuity

- RTO (Recovery Time Objective): ≤ 4 hours for clinical systems
- RPO (Recovery Point Objective): ≤ 1 hour for PHI data
- Backup testing: quarterly
- DR failover testing: annually
