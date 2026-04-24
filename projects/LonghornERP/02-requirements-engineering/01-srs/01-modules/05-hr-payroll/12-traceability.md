# Traceability Matrix — HR and Payroll

## 12.1 Functional Requirements to Business Goals

| Requirement ID | Requirement Summary | Business Goal |
|---|---|---|
| FR-HR-001–009 | Employee master, org structure, grade/scale | BG-001, BG-004 |
| FR-HR-010–018 | Leave types, balances, requests, calendar | BG-003 |
| FR-HR-019–025 | Attendance capture, shifts, overtime | BG-001 |
| FR-HR-026–032 | Payroll elements, assignments, pay periods | BG-001 |
| FR-HR-033–041 | Payroll run, PAYE, NSSF, GL posting | BG-001, BG-002 |
| FR-HR-042–049 | Payslips, statutory schedules, disbursement | BG-001, BG-002 |
| FR-HR-050–056 | Loans, advances, deductions | BG-001 |
| FR-HR-057–062 | Exit management, terminal benefits | BG-001, BG-004 |
| FR-HR-063–069 | Employee self-service portal | BG-003 |
| FR-HR-070–076 | Position and workforce governance | BG-005, BG-004 |
| FR-HR-077–083 | Payroll governance and controls | BG-006, BG-001, BG-002 |
| FR-HR-084–088 | Manager self-service and workforce analytics | BG-003, BG-005, BG-006 |

## 12.2 Context Gaps

| Gap ID | Topic | Impact |
|---|---|---|
| GAP-002 | URA PAYE e-return format and current tax band thresholds | FR-HR-036, FR-HR-046 |
| GAP-003 | NSSF employer schedule upload format | FR-HR-045 |
| GAP-007 | Uganda Data Protection Act compliance specification | NFR-HR-008 |
| GAP-009 | Biometric device API specification | FR-HR-020 |

## 12.3 Open Verification Notes

- FR-HR-036 (PAYE bands) and FR-HR-037 (Kenya, Tanzania, Rwanda equivalents) require confirmation of current statutory rates before coding the payroll engine.
- FR-HR-034 (net pay formula) must be regression-tested against at least 20 real employee profiles covering all edge cases: zero basic, loans exceeding net, multi-country bands.
- NFR-HR-001 (payroll run ≤ 60 s for 500 employees) must be verified during load testing using a seeded dataset of 500 employees with diverse element configurations.
- NFR-HR-006 (AES-256 encryption) must be validated in a penetration test confirming no plain-text salary data is retrievable via API without correct permissions.
- FR-HR-080 (shadow payroll mode) must be verified by computing a full shadow run and proving that no GL journals, employee payslips, or payment files are created.
- FR-HR-081 (segregation of duties) must be verified with at least 2 roles: payroll preparer and payroll approver, including the emergency-override path.
