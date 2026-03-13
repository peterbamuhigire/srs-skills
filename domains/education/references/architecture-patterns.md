# Education: Architecture Patterns

## Student Data Isolation Per Institution

- Each institution (district, school, university) must have strictly isolated student records
- Row-level security or schema-per-tenant depending on scale and data sensitivity
- Cross-institution queries must be architecturally prohibited without explicit data-sharing agreements
- Tenant ID must be validated on every query, not solely at authentication

## Role Hierarchy

Minimum roles required for educational systems:

| Role | Data Access |
|---|---|
| Student | Own records, enrolled course content, own grades |
| Parent/Guardian | Records of dependent students under 18 only |
| Teacher | Roster of assigned students, grades for own courses |
| Counselor | Academic records of assigned students |
| Administrator | All student and staff records within institution |
| District Admin | Aggregated data across all schools in the district |
| System Admin | System configuration; no access to student records |
| Auditor | Read-only access to audit logs and compliance reports |

- Rights automatically transfer from parent to student at age 18 (FERPA eligible student)
- Parent access must be revoked automatically when the student turns 18 unless re-authorized

## Accessibility-First UI Patterns

- All UI components must be keyboard-navigable; tab order must match visual reading order
- Form inputs must have programmatically associated labels (`<label for>` or `aria-labelledby`)
- Color must not be the sole means of conveying information (WCAG 1.4.1)
- Error messages must identify the field in error and describe the correction required
- Minimum touch target size: 44x44 CSS pixels for mobile interfaces
- Skip-to-main-content link must be the first focusable element on every page

## LTI Integration (Learning Tools Interoperability)

- All third-party educational tools must integrate via LTI 1.3 / Learning Tools Interoperability standard
- LTI launches must pass only the minimum required student data (role, course context, anonymized ID)
- Third-party tools that receive student PII must have signed Data Processing Agreements (DPAs)
- Single Sign-On (SSO) via LTI must not bypass institutional access controls

## Audit Logging for Student Records

Every access to an education record must produce a log entry:

```json
{
  "event_id": "uuid",
  "timestamp": "ISO-8601",
  "user_id": "string",
  "user_role": "string",
  "action": "READ | WRITE | EXPORT | SHARE",
  "record_type": "GradeRecord | AttendanceRecord | TranscriptRequest | ...",
  "student_id": "anonymized_id",
  "institution_id": "string",
  "outcome": "SUCCESS | FAILURE | DENIED"
}
```

- Logs must never contain raw student PII; use anonymized or internal identifiers
- Logs must be retained for the duration of the data retention policy plus 1 year
