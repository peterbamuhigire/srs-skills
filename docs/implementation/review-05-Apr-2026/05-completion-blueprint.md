# Completion Blueprint — Maduuka Documentation Suite

**Project:** Maduuka
**Date:** 2026-04-05
**Goal:** Complete all Phase 1 documentation required for the "SRS Phase 1 signed off" phase gate, and prepare the Phase 2 documentation pipeline.

---

## Phase Gate: "SRS Phase 1 Signed Off"

**Definition:** All _context/ files populated, no open V&V-FAIL tags, Traceability Matrix complete, UX Spec complete, Test Plan complete, and formal sign-off recorded.

**Current status:** 7 of 12 required documents complete. 5 remaining.

---

## Phase A: Resolve External Blockers (Peter — Parallel with documentation work)

| # | Task | Owner | Complexity | Blocked By |
|---|---|---|---|---|
| A-1 | Obtain MTN MoMo Business API sandbox credentials | Peter | S (process task) | None |
| A-2 | Engage Data Protection Act 2019 legal adviser | Peter | M (process task) | None |
| A-3 | Verify NSSF / PAYE computation with tax consultant | Peter | S (process task) | None |

*These are not documentation tasks but must run in parallel. Development cannot start until A-1 and A-2 are resolved.*

---

## Phase B: Complete Missing Phase 1 Documents (Priority order)

### B-1: Traceability Matrix

**Priority:** Critical — required for any audit or compliance sign-off.

| Step | Action | Skill |
|---|---|---|
| 1 | Create `09-governance-compliance/01-traceability-matrix/` section files | `doc-architect` |
| 2 | Map every FR-xxx identifier → business goal (from vision.md) → test case ID | `plan-implementation` |
| 3 | Build `TraceabilityMatrix_Maduuka.docx` | `build-doc.sh` |

**Complexity:** L
**Blocked by:** None (SRS FR identifiers already exist)

---

### B-2: UX Specification

**Priority:** High — developers need a UI contract before writing a single screen.

| Step | Action | Skill |
|---|---|---|
| 1 | Define interaction patterns for all 10 core modules | `cognitive-ux-framework`, `form-ux-design` |
| 2 | Produce wireframes for POS screen, inventory, HR/payroll, dashboard | `practical-ui-design`, `webapp-gui-design` |
| 3 | Validate against Design Covenant (zero mandatory training, cheapest phone) | `laws-of-ux` |
| 4 | Write `03-design-documentation/05-ux-spec/` section files | `doc-architect` |
| 5 | Build `UXSpec_Maduuka.docx` | `build-doc.sh` |

**Complexity:** XL
**Blocked by:** None

---

### B-3: Test Plan Phase 1

**Priority:** High — required before testing begins.

| Step | Action | Skill |
|---|---|---|
| 1 | Create test cases for each FR-xxx requirement (POS, INV, CUS, SUP, EXP, FIN, REP, HR, DASH, SET) | `sdlc-testing` |
| 2 | Map test cases to traceability matrix entries | `plan-implementation` |
| 3 | Define test data setup (multi-tenant sandbox, offline simulation) | `sdlc-testing` |
| 4 | Build `TestPlan_Maduuka_Phase1.docx` | `build-doc.sh` |

**Complexity:** L
**Blocked by:** None (FR identifiers exist; B-1 Traceability Matrix is parallel, not a hard dependency)

---

### B-4: Vision Statement

**Priority:** Medium — stakeholder alignment document.

| Step | Action | Skill |
|---|---|---|
| 1 | Draft from `_context/vision.md` (already populated) | `doc-architect` |
| 2 | Build `VisionStatement_Maduuka.docx` | `build-doc.sh` |

**Complexity:** S
**Blocked by:** None

---

### B-5: Business Case

**Priority:** Medium — investment justification document.

| Step | Action | Skill |
|---|---|---|
| 1 | Build from vision goals, pricing model (30K–180K UGX/month), competitor analysis | `saas-business-metrics`, `software-business-models` |
| 2 | Build `BusinessCase_Maduuka.docx` | `build-doc.sh` |

**Complexity:** M
**Blocked by:** None

---

## Phase C: Phase 2 Documentation Pipeline (After Phase 1 Sign-off)

| # | Document | Module | Dependency |
|---|---|---|---|
| C-1 | SRS Phase 2a (Restaurant / Bar) | F-011 | Phase 1 sign-off |
| C-2 | SRS Phase 2b (Pharmacy) | F-012 | Phase 1 sign-off + GAP-003 (NDA drug codes) |
| C-3 | iOS platform additions to HLD | iOS parity | Phase 1 sign-off |
| C-4 | Database Design Phase 2 amendments | F-011, F-012 | C-1, C-2 |
| C-5 | API Spec Phase 2 amendments | F-011, F-012 | C-1, C-2 |

---

## Phase D: Phase 3 Documentation Pipeline (After Phase 2 Sign-off)

| # | Document | Module | Dependency |
|---|---|---|---|
| D-1 | SRS Phase 3 (Hotel / Accommodation) | F-013 | Phase 2 sign-off |
| D-2 | SRS Phase 3 (Advanced Inventory) | F-014 | Phase 2 sign-off |
| D-3 | SRS Phase 3 (EFRIS Compliance) | F-015 | Phase 2 sign-off + GAP-005 (EFRIS accreditation) |

---

## Phase E: Deferred Documentation (Post-Launch)

These documents are not on the critical path for Phase 1 sign-off but should be planned:

| Document | Phase | Skill |
|---|---|---|
| User Manual | Phase 1 launch | `manual-guide`, `sdlc-user-deploy` |
| Installation Guide (Android + Web) | Phase 1 launch | `sdlc-user-deploy` |
| Deployment Guide | Phase 1 launch | `sdlc-user-deploy` |
| Runbook | Phase 1 launch | `sdlc-maintenance` |
| Agile Artifacts (Sprint Planning, DoD, DoR) | Phase 1 development | `sdlc-planning` |

---

## Recommended Next Session

Start with **B-1 (Traceability Matrix)** — it is the highest-priority missing artifact and can be produced immediately from existing FR identifiers without any external dependencies.

Then run **B-3 (Test Plan)** and **B-2 (UX Spec)** in parallel using dispatched sub-agents.
Skill: `superpowers:dispatching-parallel-agents`
