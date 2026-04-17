# Escalation Matrix and Contact Directory for Longhorn ERP

Use this matrix to determine the correct response time and escalation path for any incident. Assign the priority level based on the highest impact criterion that applies.

---

## Priority Levels and Response Targets

| Severity | Description | First Response | Escalation |
|---|---|---|---|
| P1 Critical | Complete outage; data loss risk; security breach; backup gap > 48 hours | On-call engineer immediately | CTO within 30 minutes |
| P2 High | Partial outage; major feature broken for all tenants; backup gap > 24 hours | Engineer within 1 hour | Team lead within 4 hours |
| P3 Medium | Single-tenant issue; degraded performance; non-critical integration failure | Engineer within 4 hours | Team lead if unresolved within 24 hours |
| P4 Low | Cosmetic defect; minor usability issue; documentation error | Next business day | Not applicable |

---

## Escalation Rules

- Escalate immediately when the first response time target cannot be met.
- Escalate immediately when a diagnosis step reveals a more severe condition than the initial priority assessment (e.g., what appeared to be a P3 single-tenant issue reveals a data isolation breach affecting multiple tenants — reclassify to P1 immediately).
- Never downgrade a P1 to a lower priority without senior engineer sign-off.
- For financial data integrity concerns (duplicate payments, EFRIS submission errors, payroll miscalculations): treat as P1 regardless of user impact count.

---

## Contact Directory

| Role | Contact | Channel |
|---|---|---|
| General support | support@chwezi.com | Email |
| On-call engineer | Assigned per weekly rota — see internal rota document | Phone / Signal |
| Team lead | Assigned per project — see internal directory | Phone / Signal |
| CTO | See internal directory | Phone |

*Note: Do not publish personal phone numbers in this document. Maintain personal contact details in the internal private directory, which is not committed to the repository.*

---

## Integration Provider Contacts

| Integration | Support Channel |
|---|---|
| MTN MoMo (Uganda) | MTN Developer Portal — developer.mtn.com |
| Airtel Money (Uganda) | Airtel Africa developer support — airtelAfrica developer portal |
| Africa's Talking (SMS / USSD) | support@africastalking.com |
| URA EFRIS | URA Taxpayer Services — efris@ura.go.ug |
