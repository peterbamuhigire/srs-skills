# Domain: Healthcare

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | HHS, FDA, CMS, ONC |
| **Key Standards** | HIPAA Privacy Rule, HIPAA Security Rule, HL7 FHIR R4, ICD-10, CPT, FDA 21 CFR Part 11 |
| **Risk Level** | High — PHI/PII data, patient safety implications |
| **Audit Requirement** | Mandatory — all PHI access must be logged |
| **Data Classification** | Protected Health Information (PHI), Personally Identifiable Information (PII) |

## Default Feature Modules

- Patient Management
- Appointment Scheduling
- Clinical Documentation
- Billing & Claims
- Reporting & Analytics

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new healthcare projects at scaffold time.

Key injected areas:
- **NFR:** HIPAA audit logging, data encryption at rest/transit, access control
- **FR:** Patient consent management, data export (Right of Access)
- **Interfaces:** HL7/FHIR API endpoints, EHR integration hooks

## References

- [regulations.md](references/regulations.md) — HIPAA, HL7/FHIR, FDA, CMS
- [architecture-patterns.md](references/architecture-patterns.md) — PHI isolation, audit logging, multi-tenant
- [security-baseline.md](references/security-baseline.md) — encryption, access control, PHI handling
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection

## Feature Reference

- [patient-management.md](features/patient-management.md)
- [appointment-scheduling.md](features/appointment-scheduling.md)
- [billing-claims.md](features/billing-claims.md)
- [clinical-documentation.md](features/clinical-documentation.md)
- [reporting-analytics.md](features/reporting-analytics.md)
