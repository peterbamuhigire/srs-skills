# Domain: Education

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | U.S. Department of Education, FTC, State education boards |
| **Key Standards** | FERPA (20 U.S.C. §1232g), COPPA (15 U.S.C. §6501), WCAG 2.1 AA, Section 508 |
| **Risk Level** | Medium — student PII, minor data protection |
| **Audit Requirement** | Required for FERPA compliance |
| **Data Classification** | Education Records (FERPA), Personally Identifiable Information (PII), Child Online Data (COPPA) |

## Default Feature Modules

- Student Information System
- Learning Management
- Gradebook & Assessment
- Attendance Tracking

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new education projects at scaffold time.

Key injected areas:
- **NFR:** Student record confidentiality, WCAG 2.1 AA accessibility, parental consent for under-13
- **FR:** Parental consent management, student data export, directory information opt-out
- **Interfaces:** LTI 1.3 for third-party tool integration, SIS import/export, state reporting feeds

## References

- [regulations.md](references/regulations.md) — FERPA, COPPA, WCAG 2.1 AA, Section 508, CIPA
- [architecture-patterns.md](references/architecture-patterns.md) — student data isolation, role hierarchy, accessibility-first UI, LTI
- [security-baseline.md](references/security-baseline.md) — student PII encryption, parental consent, age-gating, data sharing
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection

## Feature Reference

- [student-information.md](features/student-information.md)
- [learning-management.md](features/learning-management.md)
- [gradebook-assessment.md](features/gradebook-assessment.md)
- [attendance-tracking.md](features/attendance-tracking.md)
