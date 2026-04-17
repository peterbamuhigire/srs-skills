# Defect Management

## 5.1 Defect Lifecycle

All defects discovered during any test level follow the lifecycle below. Transitions are controlled by role: developers transition defects to Fixed; the QA lead transitions them to Closed, Rejected, or Deferred.

```
Open → In Progress → Fixed → Retest → Closed
                                    ↘ Rejected
                                    ↘ Deferred
```

| Status | Definition |
|---|---|
| **Open** | Defect logged, not yet assigned to a developer. |
| **In Progress** | Developer has accepted the defect and is working on a fix. |
| **Fixed** | Developer has committed a fix and a new automated regression test (for Critical and High defects). The fix is available on the test branch. |
| **Retest** | QA lead is verifying the fix against the original defect reproduction steps. |
| **Closed** | QA lead has confirmed the fix resolves the defect and the regression test passes. |
| **Rejected** | QA lead or developer has determined the reported behaviour is not a defect (working as designed or cannot be reproduced). Justification is mandatory. |
| **Deferred** | Product owner has approved deferral to a future sprint. Deferral is only valid for Medium and Low defects. Critical and High defects may not be deferred. |

## 5.2 Defect Record Fields

Every defect record must contain all of the following fields. Incomplete records are returned to the reporter before triage.

| Field | Description |
|---|---|
| **ID** | Unique defect identifier, format `DEF-<sequence>` (e.g., `DEF-0042`) |
| **Title** | One-sentence description of the observed failure (active voice, specific module named) |
| **Severity** | Critical / High / Medium / Low (see Section 1.5) |
| **Module** | The Longhorn ERP module where the defect was observed |
| **Steps to Reproduce** | Numbered ordered list of steps; reproducible from step 1 on a clean test environment |
| **Expected Result** | The deterministic output defined by the SRS requirement or NFR |
| **Actual Result** | The observed output that deviates from the expected result |
| **Environment** | Development / Staging / Production; include PHP version, browser/mobile OS version |
| **Build Version** | The application version tag under which the defect was observed |
| **Assignee** | Developer responsible for the fix |
| **Reporter** | Person who logged the defect |

## 5.3 Severity SLA

Resolution time is measured from the moment the defect status changes to In Progress.

| Severity | Fix SLA | Retest SLA |
|---|---|---|
| **Critical** | Fix committed within 4 hours of In Progress assignment | Retested within 2 hours of Fixed status |
| **High** | Fix committed within 24 hours of In Progress assignment | Retested within 4 hours of Fixed status |
| **Medium** | Fix committed within the current sprint | Retested within the current sprint |
| **Low** | Placed in backlog; prioritised at product owner's discretion | Retested at next available QA slot |

SLA breaches for Critical and High defects are escalated immediately to the project lead. A Critical SLA breach beyond 8 hours total triggers a project incident report.

## 5.4 Security Defect Protocol

Security defects require a restricted disclosure procedure regardless of functional severity.

1. Any defect that involves unauthorised data access, authentication bypass, tenant data leakage, or injection vulnerability is classified as Critical at the time of logging, even if the immediate functional impact appears minor.
2. Security defect records are visible only to the tech lead and product owner until the defect reaches Closed status. All other team members see only the defect ID and the status "Security — Restricted."
3. No security defect details are shared in public channels, commit messages, or pull request descriptions. The fix is committed with a generic message referencing the defect ID (e.g., `fix: resolve DEF-0042`).
4. After closure, the tech lead conducts a root-cause analysis and documents whether a systemic code pattern change is required to prevent recurrence.

## 5.5 Regression Test Requirement on Fix

Every Critical and High defect fix must be accompanied by a new automated test case that satisfies the following conditions:

1. The test case would have failed before the fix was applied (verified by reverting the fix and confirming the test fails).
2. The test case passes after the fix is applied.
3. The test case is added to the appropriate PHPUnit suite (unit or integration) and runs in the CI pipeline on every subsequent pull request.
4. The test case ID is recorded in the defect record's **Regression Test** field before the defect is transitioned to Closed.

Defects that lack a linked regression test case may not be transitioned to Closed by the QA lead.
