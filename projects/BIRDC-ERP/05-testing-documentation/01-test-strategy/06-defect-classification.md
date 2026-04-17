## 5. Defect Classification

All defects are classified by severity at the time of discovery. The defect severity determines the mandatory resolution timeline and Phase Gate impact.

| Severity | Definition | Phase Gate Impact | Resolution SLA |
|---|---|---|---|
| **Critical** | System is unusable; financial data is lost or corrupted; audit trail has a gap; a business rule (BR-001 to BR-018) is violated; data is written to the wrong ledger; PAYE/NSSF calculation is wrong by any amount. | Phase Gate is blocked until the defect is resolved, verified, and a regression test added. | Fix before next working day. |
| **High** | A complete module is unusable; a primary user journey cannot be completed; a PPDA document is missing; EFRIS submission fails without retry; an agent cash balance is incorrect; QC gate can be bypassed by any user. | Phase Gate is blocked until resolved. | Fix within 3 working days. |
| **Medium** | A feature is partially broken; a workaround exists; a secondary user journey fails; a report shows incorrect data in edge cases; a non-critical API integration returns an unexpected response. | Phase Gate proceeds with defect acknowledged and a remediation date agreed in writing. | Fix before the subsequent Phase Gate. |
| **Low** | Cosmetic issue; UI alignment; label spelling error; non-impacting formatting issue in a report; help text inaccurate; tooltip missing. | Phase Gate not affected. | Fix before go-live (Phase 7). |

### 5.1 Defect Lifecycle

1. Defect raised in project issue tracker with: severity, module, test case ID, steps to reproduce, expected result, actual result, and screenshot or log excerpt.
2. Developer acknowledges within 1 working day.
3. Developer resolves and marks "Ready for Retest."
4. Peter Bamuhigire or assigned tester retests using the original test case. If pass, defect closed. If fail, defect re-opened with additional notes.
5. All Critical and High defects require a root cause note and a new regression test case added to the suite before closure.

### 5.2 Defect Density Target

At Phase 7 go-live, the open defect counts must not exceed: Critical = 0, High = 0, Medium ≤ 5 (all acknowledged and scheduled), Low = no limit.
