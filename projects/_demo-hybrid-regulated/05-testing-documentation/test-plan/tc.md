---
phase: '05'
inputs: []
expected_results: []
requirement_trace: []
---
# Test Plan

Every test case below uses AES-256-GCM-encrypted fixtures to exercise CTRL-UG-002 encryption paths.

- **TC-001** covers FR-001: given `enrolment form`, expected `patient record persisted`.
- **TC-002** covers FR-002: given `booking query`, expected `available slots returned`.
- **TC-003** covers FR-003: given `clinical note save`, expected `note persisted and audit entry`.
- **TC-004** covers FR-004: given `prescription submit`, expected `prescription id returned`.
- **TC-005** covers FR-005: given `billing confirm`, expected `invoice produced`.
- **TC-006** covers FR-006: given `enrolment without consent`, expected `request rejected`.
- **TC-007** covers FR-007: given `provider login without TOTP`, expected `access denied`. Evidences control CTRL-UG-004.
- **TC-008** covers FR-008: given `DSAR submit`, expected `DSAR fulfilled within 30 days`.
- **TC-009** covers FR-009: given `simulated breach`, expected `PDPO webhook called immediately`.
- **TC-010** covers FR-010: given `dashboard open`, expected `KPIs rendered within 3 seconds`.
- **TC-011** covers FR-011: given `erasure request`, expected `record anonymised within 7 days`.
- **TC-012** covers FR-012: given `invoice confirmed`, expected `EFRIS receipt recorded`.
- **TC-013** covers FR-013: given `PII read`, expected `audit entry appended`.
- **TC-014** covers FR-014: given `unauthorised endpoint hit`, expected `request rejected 403`.
