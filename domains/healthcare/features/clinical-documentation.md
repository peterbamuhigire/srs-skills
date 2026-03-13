# Feature: Clinical Documentation

## Description
Structured and free-text clinical note capture — SOAP notes, problem lists,
medication management, allergy tracking, and order management.

## Standard Capabilities
- SOAP note creation and templating
- Problem list management (active, inactive, resolved)
- Medication list with e-prescribing (NCPDP SCRIPT standard)
- Allergy and adverse reaction recording
- Vital signs capture and trending
- Clinical order entry (labs, imaging, referrals)
- Document scanning and attachment
- Clinical decision support alerts

## Regulatory Hooks
- FDA: e-prescribing for controlled substances requires DEA certification
- Meaningful Use / MIPS: structured data capture for quality reporting
- ONC 21st Century Cures: no information blocking in clinical data exchange

## Linked NFRs
- NFR-HC-001 (Audit Trail)
- NFR-HC-002 (Encryption at Rest)
- NFR-HC-005 (MFA — required for prescribing)
