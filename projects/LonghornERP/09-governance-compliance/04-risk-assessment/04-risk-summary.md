# Risk Summary and Prioritisation

## 4.1 Risk Distribution by Score

| Score | Count | Risk IDs |
|---|---|---|
| Critical (9) | 2 | RISK-001, RISK-011 |
| High (6) | 8 | RISK-002, RISK-004, RISK-007, RISK-008, RISK-019, RISK-020, RISK-021, RISK-024 |
| Medium (4) | 6 | RISK-003, RISK-005, RISK-009, RISK-012, RISK-017, RISK-022, RISK-023 |
| Low (2–3) | 7 | RISK-006, RISK-010, RISK-013, RISK-014, RISK-015, RISK-016, RISK-018 |
| Minimal (1) | 1 | RISK-016 |
| **Total** | **24** | RISK-001 through RISK-024 |

*Note: RISK-016 appears in both Low and Minimal rows because the score matrix yields 1 (Minimal) for L×L. The count above corrects this: RISK-016 is Minimal (1); total Low (2–3) count is 6 (RISK-006, RISK-010, RISK-013, RISK-014, RISK-015, RISK-018); total Medium (4) count is 6 (RISK-003, RISK-005, RISK-009, RISK-012, RISK-017, RISK-022, RISK-023).*

## 4.2 Corrected Distribution

| Score | Count | Risk IDs |
|---|---|---|
| Critical (9) | 2 | RISK-001, RISK-011 |
| High (6) | 8 | RISK-002, RISK-004, RISK-007, RISK-008, RISK-019, RISK-020, RISK-021, RISK-024 |
| Medium (4) | 7 | RISK-003, RISK-005, RISK-009, RISK-012, RISK-017, RISK-022, RISK-023 |
| Low (2–3) | 6 | RISK-006, RISK-010, RISK-013, RISK-014, RISK-015, RISK-018 |
| Minimal (1) | 1 | RISK-016 |
| **Total** | **24** | |

## 4.3 Top 10 Risks Requiring Immediate Attention

The following risks are rated Critical or High and are ordered by priority. All must have active mitigations in progress before Phase 1 development begins.

| Priority | Risk ID | Score | Description | Target Date |
|---|---|---|---|---|
| 1 | RISK-001 | Critical (9) | URA EFRIS API credentials not obtained — blocks Sales and Accounting SRS finalisation and Phase 1 go-live. | 2026-05-01 |
| 2 | RISK-011 | Critical (9) | MTN MoMo bulk payment API not obtained — blocks payroll disbursement, cooperative payment, and bulk transfer features. | 2026-05-15 |
| 3 | RISK-008 | High (6) | Accounting period close behaviour unspecified — no audit-grade GL close procedure defined; blocks Accounting module development. | 2026-06-01 |
| 4 | RISK-004 | High (6) | Multi-tenancy security review not commissioned — tenant data isolation unverified; blocks first tenant onboarding. | 2026-06-01 |
| 5 | RISK-024 | High (6) | Solo developer dependency — no continuity plan; any unavailability halts all development and support. | 2026-09-30 |
| 6 | RISK-007 | High (6) | Uganda Data Protection Act legal review not commissioned — HR & Payroll data handling legally unverified. | 2026-06-15 |
| 7 | RISK-019 | High (6) | EFRIS API downtime has no queue-and-retry mechanism — invoice submission can be blocked indefinitely. | 2026-06-01 |
| 8 | RISK-021 | High (6) | PII stored without confirmed consent recording or retention controls — Data Protection Act exposure. | 2026-07-01 |
| 9 | RISK-002 | High (6) | URA PAYE graduated band thresholds unconfirmed — statutory returns may use incorrect tax calculations. | 2026-05-15 |
| 10 | RISK-020 | High (6) | Mobile money API breaking changes have no abstraction layer — a single API change could break all disbursement workflows. | 2026-06-15 |

## 4.4 Risk Acceptance Statement

Risks rated Low (2–3) and Minimal (1) are accepted for the current planning horizon, subject to review at the next quarterly register update. Acceptance does not mean the risk is ignored; it means the cost of mitigation before its target date exceeds the cost of the risk materialising.

All Critical and High risks listed in Section 4.3 are **not accepted**. Active mitigation is required. Any Critical or High risk without an active mitigation task in the project backlog by 2026-05-01 must be escalated to the project owner for a formal acceptance decision.
