# Incident Severity Matrix

| Sev | Definition | Example | Response Time |
|---|---|---|---|
| Sev-1 | Production outage for all tenants OR S-tier PII breach OR cross-tenant data leak | Site 5xx > 50%; MySQL primary down; cross-tenant query in audit log | Page primary in 0 min; resolve <= 4 h |
| Sev-2 | Degradation for >= 20% of tenants OR critical feature broken | MoMo reconciliation failing; UNEB export timing out | Page primary in 0 min; resolve <= 1 business day |
| Sev-3 | Non-critical feature broken for a minority of tenants | PDF export layout broken on Android | Ticket; resolve in sprint |
| Sev-4 | Cosmetic / enhancement | Typo in error message | Backlog |
