# Feature: Patient Management

## Description
Core patient record management — demographics, identifiers, contact info,
insurance, emergency contacts, and consent records.

## Standard Capabilities
- Patient registration and demographic capture
- MRN (Medical Record Number) generation
- Insurance eligibility verification
- Patient consent management (HIPAA authorizations)
- Duplicate patient detection and merge
- Patient search (name, DOB, MRN, SSN last-4)
- Patient portal access management

## Regulatory Hooks
- HIPAA Right of Access: patients must be able to export their records
- HIPAA Minimum Necessary: search results must not expose unnecessary PHI
- ONC 21st Century Cures: prohibits information blocking

## Linked NFRs
- NFR-HC-001 (Audit Trail)
- NFR-HC-002 (Encryption at Rest)
- NFR-HC-005 (MFA)
