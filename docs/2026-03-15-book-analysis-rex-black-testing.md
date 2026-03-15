# Book Analysis: Managing the Testing Process — Rex Black (3rd Ed.)
**Analyzed:** 2026-03-15
**Feeds:** W-09, B-02, B-03, B-05, B-08

---

## W-09: Seven-Step Defect Resolution Protocol

Black's protocol is 7 steps (not 6). Steps 1–3 = tester-owned isolation; 4–6 = developer-owned debugging; 7 = tester-owned confirmation + regression.

| Step | Owner | Action |
|------|-------|--------|
| 1 | Tester | Reproduce: exact minimal sequence; check for intermittence |
| 2 | Tester | Discriminate: test bug or system bug? |
| 3 | Tester | Isolate: external factors influencing symptoms (configs, data, workflows) |
| 4 | Developer | Root cause: identify cause in code, hardware, network, or environment |
| 5 | Developer | Repair: fix without introducing new problems |
| 6 | Developer | Debug: verify the fix is clean |
| 7 | Tester | Confirm + Regression: does it pass the failing test? Does everything else still work? |

The handoff boundary at 3→4 is the critical management line. The Bug Report is the artifact that crosses this boundary.

---

## Bug Report Fields (Complete)

**Static fields (set at open):**
- Bug ID (auto-number)
- Project Name
- Tester (reporter)
- Date Opened
- Summary (one-to-two sentence customer-impact statement)
- Steps to Reproduce (precise, minimal sequence)
- Isolation (variables tested; bounding box around the bug)

**Importance fields:**
- Severity (1–5 scale; 1 = data loss/hardware damage/safety, 5 = cosmetic)
- Priority (1–5 scale; 1 = complete loss of system value, 5 = negligible)
- RPN = Severity × Priority (range 1–25; 1 = most dangerous)

**Dynamic/tracking fields:**
- State (Review → Open → Assigned → Test → Closed/Deferred/Cancelled/Reopened)
- Owner
- Estimated Fix Date
- Log/Status (audit trail of state changes)

**Analysis fields:**
- Subsystem
- Configuration (test release + environment identifier)
- Quality Risk (traceability to risk item)
- Resolution / Root Cause (from taxonomy)
- Close Date
- Phase Injected / Detected / Removed

---

## Defect Lifecycle States

```
Review → Open → Assigned → Test → Closed
Review → Rejected (back to tester)
Open/Assigned/Test → Deferred (terminal)
Open/Assigned/Test → Cancelled (terminal)
Test → Reopened → Assigned
```

Terminal states: Closed, Deferred, Cancelled.
Rule: If fix fails confirmation → Reopen. If fix passes confirmation but fails regression → Open NEW bug.

---

## Severity Scale (1–5)

| Level | Definition |
|-------|------------|
| 1 | Data loss, hardware damage, or safety issue |
| 2 | Loss of functionality, no workaround |
| 3 | Loss of functionality with workaround |
| 4 | Partial loss of functionality |
| 5 | Cosmetic or trivial |

## Priority Scale (1–5)

| Level | Definition |
|-------|------------|
| 1 | Complete loss of system value |
| 2 | Unacceptable loss of system value |
| 3 | Possibly acceptable reduction |
| 4 | Acceptable reduction |
| 5 | Negligible reduction |

Priority ≠ severity. Example: Severity 5 (cosmetic) bug blocking Windows certification = Priority 1.

---

## Root Cause Taxonomy

**Functional:** Specification error | Function (impl wrong) | Test (false positive)
**System:** Internal interface | Hardware devices | OS | Software architecture | Resource management
**Process:** Arithmetic | Initialization | Control/sequence | Static logic | Other
**Data:** Type | Structure | Initial value | Other
**Code:** Typo/stylistic error causing failure
**Documentation:** Docs say X, system does valid Z
**Standards:** Failure to meet industry/code standards
**Bookkeeping:** Duplicate | NAP (Not A Problem) | Bad Unit | RCN (Root Cause Needed) | Unknown

---

## Test Plan Structure (All Sections)

| Section | Purpose |
|---------|---------|
| Overview | Goals, methodology, objectives; architecture diagram |
| Bounds | Scope (Is/Is-Not table), Definitions, Setting |
| Quality Risks | Risk analysis doc or table (risk → strategy mapping) |
| Proposed Schedule of Milestones | Key dates |
| Transitions | Entry criteria, Continuation criteria, Exit criteria |
| Test Development | How cases/tools/scripts will be created |
| Test Configurations and Environments | HW allocation plan, SW revisions, lab |
| Test Execution | Execution factors |
| Resources | Roles, contacts, escalation |
| Test Case and Bug Tracking | Tools for tracking |
| Bug Isolation and Classification | Degree of isolation; classification scheme |
| Test Release Management | Release format, revision policy |
| Test Cycles | Number, timing, arrangement |
| Risks and Contingencies | Testing-project risks |

---

## Entry / Exit Criteria Format

Three-section Transitions model: **Entry → Continuation → Exit**

Each is a numbered list. Each item rated **Green / Yellow / Red** at phase gate meeting.

Entry criteria (key items):
1. Bug/test tracking systems in place
2. All components under automated CM control
3. Test environment configured with access provided
4. All scheduled features/bug-fixes development-complete
5. Development has unit-tested all features
6. Open must-fix bug count below threshold N
7. Software delivered N business days prior to start
8. Smoke test completed by test team
9. Project Management approves in Phase Entry Meeting

Exit criteria (key items):
1. No code/feature changes except defect fixes for prior N weeks
2. No crashes/panics for prior N weeks
3. No client systems made inoperable
4. All planned tests executed against GA candidate
5. All must-fix bugs resolved
6. All issues closed or deferred, confirmation+regression complete
7. Metrics indicate stability, coverage of critical risks
8. PM agrees product will satisfy customer expectations
9. Phase Exit Meeting held with formal approval

---

## Test Case Fields (Mapping to BS 29119-3)

Black's 20+ field template maps to all 9 BS 29119-3 normative fields:

| 29119-3 Field | Black Field |
|---------------|-------------|
| Unique ID | Test ID (Dewey decimal: XX.YYY) |
| Objective/Purpose | Risk-derived Priority + Name |
| Priority | RPN from quality risk analysis |
| Traceability to requirement | Quality Risk / Tracing column |
| Preconditions | Setup section |
| Input | Step/Substep data |
| Expected Result | Step/Substep expected result |
| Actual Result | Result column (Pass/Fail/Warn/Block/Skip) |
| Test Result | Overall Status rollup |

Additional Black fields: Bug ID, Bug RPN, Effort, Duration, Config ID, Tester, Date.

**Result status codes:** Pass | Fail | Warn | Block | Skip | IP (In-Progress)
**Rollup rule:** IP > Block > Fail > Warn > Pass

---

## Test Dashboard (Balanced Scorecard — 4 Charts)

1. **Test Progress Chart** — daily test hours achieved vs. planned (~30 hrs/tester/week)
2. **Test Fulfillment Chart** — cumulative planned vs. fulfilled (pass/fail/skip breakdown)
3. **Test and Bug Coverage Chart** — % coverage per quality risk category + % bugs found there
4. **Opened/Closed Bug Chart** — cumulative opens vs. closes over calendar time; trend lines

Questions the dashboard answers: Is quality improving? Is testing progressing? Are all planned tests running? Were quality risks addressed? What trends are developing?

---

## B-08: Test Environment Readiness

Maps to entry criteria items 3, 7, 8 and the Hardware Allocation Plan table:

Hardware Allocation Plan fields:
| System (Test Usage) | [QTY] | Network | When | Where | Other [QTY] |

All components must be under formal, automated CM control before system test entry. Configuration coded identifier system (e.g., A.Y.0.2.33) used in every bug report.

---

## Go/No-Go Decision

Black deliberately does NOT recommend go/no-go — provides objective metrics data and lets PM decide in a formal Phase Exit Meeting. This is the correct model: test team informs, management decides.
