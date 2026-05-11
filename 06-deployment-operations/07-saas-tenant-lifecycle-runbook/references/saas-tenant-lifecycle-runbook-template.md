# SaaS Tenant Lifecycle Runbook — Master Template

## 1. Event catalogue

| Event | Trigger | Source service | Downstream consumers | SLA |
|-------|---------|----------------|----------------------|-----|
| `tenant.created` | | | | |
| `tenant.tier_changed` | | | | |
| `tenant.suspended` | | | | |
| `tenant.reactivated` | | | | |
| `tenant.offboarded` | | | | |
| `tenant.export_requested` | | | | |
| `tenant.hard_deleted` | | | | |

## 2. Playbook structure (reused per stage)

```
### <Stage name>

- Trigger: <who/what initiates>
- Pre-conditions: <state required>
- Actor: <automated | on-call | privacy officer | CS>
- Automated steps:
  1.
  2.
- Manual gates: <approver, criteria>
- Per-service propagation:
  | Service | Action |
  |---------|--------|
- Verification:
  - Post-condition assertion(s):
  - Test query / smoke test:
- Rollback / abort: <state on failure, paging>
- Audit-trail entry: <event name, destination, retention>
- Customer-comms:
  - Subject:
  - Body:
  - In-app banner:
- Retention-policy reference: <link>
```

## 3. Hard-delete verification

After hard delete the on-call MUST execute the verification across every data store and attach the result to the destruction certificate:

```sql
-- Primary DB
SELECT COUNT(*) FROM <every tenant-scoped table> WHERE tenant_id = '<TID>'; -- expect 0

-- Search index
GET /index/_count?q=tenant_id:<TID>  -- expect 0

-- Object storage
aws s3 ls s3://<bucket>/tenants/<TID>/  -- expect empty

-- Cache
redis-cli --scan --pattern "tenant:<TID>:*" | wc -l  -- expect 0

-- Backups still in retention: list explicitly with planned expiry date
```

## 4. Destruction certificate (signed by privacy officer)

| Field | Value |
|-------|-------|
| Tenant ID | |
| Tenant name | |
| Offboarding requested | |
| Grace period ended | |
| Hard delete executed | |
| Verification results | (attach above output) |
| Backups still retaining tenant data and their expiry dates | |
| Legal-hold check | NO HOLD CONFIRMED |
| Privacy officer signature | |
| Retention of certificate | 7 years |

## 5. Legal-hold procedure

A tenant may be placed under legal hold by Legal/Compliance. While the hold is active:

- Hard-delete is blocked.
- Soft-delete is reversible.
- Audit-trail and metering data must be preserved beyond regular retention.
- The hold expiry must be tracked; on release, hard-delete may be scheduled.

## 6. Customer-comms templates

Templates for every customer-facing transition: pending suspension, suspended, reactivated, offboarding confirmation, data-export ready, account-deleted confirmation. Keep tone factual, name the date, and provide the contact path for disputes.
