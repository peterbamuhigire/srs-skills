---
phase: '05'
inputs:
  - FR-001
  - FR-002
expected_results:
  - "Session terminates after 15 minutes idle"
  - "PHI column ciphertext != plaintext in disk dump"
requirement_trace:
  - FR-001 -> TC-001
  - FR-002 -> TC-002
---

# Test Cases

- **TC-001** covers FR-001. Precondition: user is logged in. Steps: leave the
  session idle for 16 minutes. Expected: HTTP 401 on next request and an
  audit-log record with `event=session_timeout`.
- **TC-002** covers FR-002. Precondition: one PHI row inserted. Steps: dump
  the on-disk page. Expected: no plaintext PHI tokens are visible.
