# Healthcare: Architecture Patterns

## PHI Data Isolation

- Store PHI in dedicated, encrypted database schema or separate DB
- Never log PHI in application logs — log record IDs only
- Implement field-level encryption for SSN, DOB, diagnosis codes
- Use data masking in non-production environments

## Audit Logging Architecture

Every PHI access event must produce an immutable log entry:

```json
{
  "event_id": "uuid",
  "timestamp": "ISO-8601",
  "user_id": "string",
  "user_role": "string",
  "action": "READ | WRITE | DELETE | EXPORT",
  "resource_type": "Patient | Encounter | ...",
  "resource_id": "string",
  "ip_address": "string",
  "session_id": "string",
  "outcome": "SUCCESS | FAILURE"
}
```

Audit logs must be:
- Write-once (no UPDATE/DELETE operations permitted)
- Retained for minimum 6 years (HIPAA)
- Queryable by patient ID, user ID, date range

## Multi-Tenant PHI Isolation

- Each tenant (hospital/clinic) must have strictly isolated PHI
- Row-level security or schema-per-tenant depending on scale
- Cross-tenant queries must be architecturally impossible
- Tenant ID must be validated on every query, not just at login

## Role-Based Access Control (RBAC)

Minimum roles required:
- **Patient:** Own records only
- **Clinician:** Assigned patients + emergency override
- **Admin:** Administrative data, no clinical notes
- **Billing:** Billing data only, masked clinical info
- **Auditor:** Read-only audit logs
- **Super Admin:** System config, no PHI access

## Emergency Access ("Break-Glass")

- Clinicians must be able to access any patient record in emergencies
- All break-glass accesses must trigger immediate notification to Privacy Officer
- Require post-access justification within 24 hours

## API Design

- All FHIR endpoints must support OAuth 2.0 / SMART on FHIR
- Rate limiting on all patient data endpoints
- Response must never include PHI in error messages
- Support `_elements` parameter to limit PHI in responses
