# SRS skill contract test matrix

| Prompt or condition | Required specification behaviour |
|---|---|
| New non-production tenant needing demo and system-test coverage | Route here and produce the complete output set |
| Migration, reference catalogue installation, or template bootstrap only | Route elsewhere; do not classify global defaults as demo data |
| Ambiguous target or authority | Stop at discovery and record the gap |
| Production target or real regulated data | Refuse mutation and specify safe alternatives |
| Capability only in schema/menu | `NOT_ASSESSED`, with evidence needed |
| No supported application boundary | `BLOCKED_CAPABILITY`; prohibit SQL/DML/private persistence |
| Duplicate key, collision, or cross-tenant ID | Require preflight refusal |
| Replay or forced partial failure | Require idempotency, rollback/compensation, run-ledger, and retest evidence |
| Reset | Require preservation of global/reference data and unrelated tenants |
| Limited-capability product | Report supported modules and blockers without fake completion |
