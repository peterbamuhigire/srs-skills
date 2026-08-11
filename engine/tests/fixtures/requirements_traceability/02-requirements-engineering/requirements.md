---
phase: "02"
document: "requirements"
---
# Requirements

- **FR-001** The system shall reject duplicate claim IDs; traces to **BG-001** and **TC-001**.

Ambiguity status: resolved. A duplicate claim is a second submission with the same claim ID within the same tenant.

Acceptance criterion **AC-001**: Given an existing claim ID, when the same claim ID is submitted again, then the system rejects the submission with `DUPLICATE_CLAIM_ID`.
