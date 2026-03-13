# Education: Security Baseline

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| At Rest (student PII) | AES-256-GCM | 256-bit |
| In Transit | TLS 1.2+ | — |
| Database fields (SSN, ID numbers) | AES-256 field-level | 256-bit |
| Backups | AES-256 | 256-bit |

## Parental Consent Workflows (COPPA)

- Systems serving users under 13 must implement a verifiable parental consent (VPC) gate before account activation
- Acceptable VPC methods: signed consent form, credit card verification, toll-free phone confirmation, or government ID verification
- Consent records must be retained for the lifetime of the child's account plus the data retention period
- Schools acting as consent intermediaries (COPPA school exception) must maintain records of the institutional consent authorization
- Consent must be re-obtained if the data collection purpose changes materially

## Student PII Data Sharing Restrictions

- Student education records may not be shared with third parties without written consent or a FERPA exception
- All third-party vendors receiving student PII must execute a Data Processing Agreement (DPA) prior to data access
- Vendor DPAs must prohibit use of student data for advertising, re-identification, or sale
- State student privacy laws (e.g., NY Education Law §2-d, SOPIPA) may impose additional restrictions beyond FERPA

## Age-Gating for Under-13

- Date of birth must be collected at account creation
- Users determined to be under 13 must be routed to the parental consent workflow before any data is collected
- Neutral age-screen questions must be used; systems must not encourage users to provide a higher age
- Under-13 accounts must have restricted feature sets disabling any social or public-sharing features

## Authentication Requirements

- Multi-Factor Authentication (MFA) required for all staff and administrator accounts
- Student accounts: MFA encouraged but may be optional at institution discretion
- Session timeout: 30 minutes inactivity for staff; 60 minutes for student learning sessions
- Password policy: minimum 10 characters for staff; institution-configurable for students
- Shared student login credentials are prohibited; each student must have a unique identifier

## Access Control Baseline

- Principle of least privilege on all roles
- Access reviews every 180 days for staff accounts
- Immediate access revocation for staff on termination (< 4 hour SLA)
- Parent access rights automatically expire when student reaches age 18

## Vulnerability Management

| Severity | Remediation SLA |
|---|---|
| Critical | 72 hours |
| High | 30 days |
| Medium | 90 days |

- OWASP Top 10 compliance required for all student-facing web applications
- Annual penetration testing minimum
