# Healthcare: Regulations & Standards Reference

## HIPAA (Health Insurance Portability and Accountability Act)

| Rule | Citation | Requirement |
|---|---|---|
| Privacy Rule | 45 CFR §164.500–534 | Governs use and disclosure of PHI |
| Security Rule | 45 CFR §164.300–318 | Safeguards for electronic PHI (ePHI) |
| Breach Notification | 45 CFR §164.400–414 | 60-day breach notification requirement |
| Minimum Necessary | 45 CFR §164.502(b) | Limit PHI access to minimum necessary |

### Key HIPAA Technical Safeguards (§164.312)

- **Access Control (§164.312(a)):** Unique user identification, automatic logoff, encryption/decryption
- **Audit Controls (§164.312(b)):** Hardware/software activity recording on systems containing ePHI
- **Integrity (§164.312(c)):** Protect ePHI from improper alteration or destruction
- **Transmission Security (§164.312(e)):** Encryption of ePHI in transit

## HL7 FHIR R4 (Fast Healthcare Interoperability Resources)

- **Standard:** HL7 FHIR Release 4 (4.0.1)
- **Use:** RESTful API for healthcare data exchange
- **Key Resources:** Patient, Practitioner, Encounter, Observation, Condition, MedicationRequest
- **Auth:** SMART on FHIR (OAuth 2.0 + OpenID Connect)
- **Reference:** https://hl7.org/fhir/R4/

## FDA 21 CFR Part 11

- Applies to electronic records and electronic signatures
- Requires audit trails, user authentication, system validation
- Relevant for clinical trial software, FDA-regulated medical devices

## ICD-10 / CPT Coding

- **ICD-10-CM:** Diagnosis codes (68,000+ codes)
- **CPT:** Procedure codes (American Medical Association)
- Must support annual code updates (effective October 1 each year for ICD-10)

## CMS Requirements

- **Medicare/Medicaid:** Must support CMS billing formats (ANSI X12 837)
- **CLIA:** Clinical Laboratory Improvement Amendments for lab result handling
