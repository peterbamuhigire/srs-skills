# Feature: Citizen Portal

## Description
Public-facing self-service gateway — citizen identity proofing, account
management, service applications, status inquiries, document upload,
and notifications — with mandatory Section 508 accessibility and IAL2
identity assurance.

## Standard Capabilities
- Citizen account creation with IAL2 identity proofing (Login.gov or national IdP integration)
- Multi-Factor Authentication (MFA) — phishing-resistant (FIDO2/WebAuthn)
- Service catalog and eligibility screening
- Online application submission for government services (benefits, permits, licenses)
- Application status tracking and notification (email, SMS, in-portal)
- Secure document upload with virus scanning and format validation
- Secure messaging between citizen and case worker
- Downloadable correspondence and decision letters (accessible PDF)
- Account activity log (accessible to citizen per Privacy Act rights)
- FOIA request intake and tracking

## Regulatory Hooks
- Section 508 / WCAG 2.1 AA: all portal interfaces must be accessible; VPAT required at procurement
- NIST SP 800-63 IAL2: identity proofing required before accessing personal records or submitting applications
- Privacy Act (5 U.S.C. §552a): citizens have the right to access and amend their own records held by the agency
- FOIA (5 U.S.C. §552): portal must support FOIA request submission, tracking, and response delivery

## Linked NFRs
- GOV-NFR-001 (FISMA Compliance — citizen portal is a federal information system)
- GOV-NFR-002 (Accessibility — Section 508 / WCAG 2.1 AA mandatory)
- GOV-NFR-003 (Data Sovereignty — citizen PII must remain in national jurisdiction)
- GOV-NFR-004 (Identity Assurance Level IAL2 minimum for service access)
- GOV-NFR-005 (Audit Trail Retention — all citizen record access logged)
