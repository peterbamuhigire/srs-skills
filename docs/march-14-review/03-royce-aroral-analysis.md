# Analysis: Royce (1970) and Aroral (2021) — Implications for SDLC-Docs-Engine

**Date:** 2026-03-15
**Source 1:** Royce, W.W. (1970). Managing the Development of Large Software Systems. *IEEE WESCON Proceedings*, pp. 328–338.
**Source 2:** Aroral, H.K. (2021). Waterfall Process Operations in the Fast-paced World. *International Journal of Applied Business and Management Studies*, 6(1), 91–99.

---

## 1. The Most Important Misreading in Software History

Every reproduction of the "waterfall model" in textbooks, certification curricula, and project management frameworks traces back to Royce's Figure 2 (p. 329). That diagram shows a linear sequence: System Requirements → Software Requirements → Analysis → Program Design → Coding → Testing → Operations. For fifty years it has been cited as Royce's recommendation.

It is not. Royce presents Figure 2 as the failure mode.

His exact framing (p. 329): the basic sequential model "is risky and invites failure." He introduces it only to dismantle it. The paper's entire contribution — five corrective steps — is devoted to explaining why pure sequential development fails and what must replace it.

The misreading has consequences that Aroral (2021) confirms empirically: waterfall projects fail most frequently because integration is deferred to the end, because requirements are locked before design is understood, and because the customer is absent until delivery. All three failures are explicitly anticipated and addressed by Royce. The industry adopted his diagram and discarded his fixes.

This analysis corrects that record and identifies structural gaps in the SDLC-Docs-Engine resulting from the same misreading.

---

## 2. Royce's True Model: The 5 Corrective Steps

### Step 1: Program Design Comes First (p. 330)

Preliminary program design must precede analysis. Design must allocate database structures, subroutine storage, execution time budgets, inter-module interfaces, and operating procedures. The output is a written **Overview Document** comprehensible to every team member — not just architects.

**Purpose:** Surface storage and timing failures before requirements analysis commits the project to an infeasible specification. Once analysis is complete, redesign is expensive. If discovered during design, it is cheap.

**Engine implication:** Our pipeline begins with `01-initialize-srs` and proceeds directly to requirements elicitation. No preliminary design gate exists before `05-feature-decomposition`. This is the exact inversion Royce identifies as risky.

### Step 2: Document the Design (p. 331)

Royce states: "During the early phase of software development the documentation IS the specification and IS the design. If the documentation does not yet exist there is as yet no design."

He quantifies the documentation burden: a $5M software project requires approximately 1,000 pages of specification, compared to 30 pages for a $5M hardware project. The ratio is not bureaucracy — it is the only medium through which software design exists prior to code.

**Engine implication:** Our skills produce documentation, but the skills themselves lack enforcement mechanisms. There is no skill that validates document completeness before the next phase is permitted to begin. Ruthless enforcement, in Royce's terms, requires a gate — not a checklist.

### Step 3: Do It Twice (p. 332)

The version delivered to the customer should be the second version. A pilot — a miniature of the full process — must be built first. For a 30-month project, Royce prescribes a 10-month pilot. The pilot eliminates reliance on human judgment for storage and timing estimates; actual measurements replace projections.

This is a direct precursor to modern iterative and agile practice. Royce proposed it in 1970. Its absence from the industry's adopted model is the source of most large-project cost overruns attributable to late-phase estimation failure.

**Engine implication:** We have no Proof-of-Concept or Pilot Model document skill. This is the second-highest risk-reduction mechanism Royce identifies.

### Step 4: Plan, Control, and Monitor Testing (pp. 332–333)

Testing consumes the largest share of project resources and carries the highest risk concentration. Royce's prescriptions:

- Test specialists must be autonomous from the original designers. The same person who built a module cannot reliably verify it.
- Visual code inspection precedes computer-based testing. Inspection is cheaper per defect found.
- Every logic path must be exercised at least once with a numerical check.
- Without adequate documentation, every defect is analyzed exclusively by its author — the person least likely to identify the class of error.

**Engine implication:** Our `05-testing-documentation/` phase (`01-test-strategy`, `02-test-plan`, `03-test-report`) exists as a phase-level deliverable but is not initiated at design time. This violates Royce's structural requirement (see Section 4 below).

### Step 5: Involve the Customer (pp. 333–334)

Royce defines three formal customer review points:

| Gate | Timing | Purpose |
|------|--------|---------|
| **PSR** — Preliminary Software Review | After preliminary design | Validate design approach before analysis locks scope |
| **CSR** — Critical Software Review | During/after program design (multiple rounds) | Validate design decisions; may recycle to earlier phase |
| **FSAR** — Final Software Acceptance Review | After testing, before operations | Formal acceptance; authorizes transition to operations |

His statement (p. 334): "To give the contractor free rein between requirement definition and operation is inviting trouble." The reviews are not optional milestones. They are risk-reduction mechanisms with defined recycling paths back to earlier phases.

**Engine implication:** We have `08-semantic-auditing` (V&V) but no formal customer review gate documents. Auditing is an internal quality function. Customer review gates are a contractual and communication function — distinct artifacts with distinct owners.

---

## 3. Royce's 6 Canonical Documents

Royce's Figure 6 (p. 331) defines the document set and its timing relative to the development phases:

| Doc | Title | Initiated At | Delivered At |
|-----|-------|-------------|-------------|
| Doc 1 | Software Requirements | System Requirements phase | Before Analysis |
| Doc 2 | Preliminary Design Spec | Preliminary Program Design | Before Analysis |
| Doc 3 | Interface Design Spec | Preliminary Program Design | Before Analysis |
| Doc 4 | Final Design Spec (→ As-Built) | Program Design | Updated through Coding |
| Doc 5 | Test Plan Spec → Test Results | **Program Design** | Completed after Testing |
| Doc 6 | Operating Instructions | Program Design | Before Operations |

**Mapping to our current phase structure:**

| Royce Document | Closest Engine Skill | Gap |
|---------------|---------------------|-----|
| Doc 1: Software Requirements | `02-requirements-engineering/waterfall/` (skills 01–08) | Covered |
| Doc 2: Preliminary Design Spec | `03-design-documentation/` | Partial — no explicit "preliminary" design gate |
| Doc 3: Interface Design Spec | `02-requirements-engineering/waterfall/04-interface-specification` | Partial — interface spec is in requirements phase, not design phase |
| Doc 4: Final Design Spec | `03-design-documentation/` | Partial — no As-Built variant |
| Doc 5: Test Plan | `05-testing-documentation/02-test-plan` | **Structural gap** — see Section 4 |
| Doc 6: Operating Instructions | `06-deployment-operations/` | Partial — exists but not formally linked to Doc 4 |

---

## 4. Critical Insight: Test Plan Starts at Design Phase

Royce's Figure 6 is explicit: Doc 5 (Test Plan Spec) is **initiated at the Program Design phase**, not at the Testing phase. By the time coding begins, the test plan must already exist.

This is not a minor scheduling detail. It reflects Royce's principle that testing cannot be planned after the system is built — the test criteria must be derived from the design specifications, not reverse-engineered from the code.

**Current engine gap:** `05-testing-documentation/02-test-plan` is a Phase 05 skill. It is executed after development artifacts (Phase 04). A consultant using the engine in strict phase order will produce a test plan after implementation is complete — the precise failure mode Royce identifies.

**Recommended correction:** Add a stub or formal link in `03-design-documentation/` that initiates the test plan artifact. The Phase 05 skill then completes and validates what was started in Phase 03. This mirrors Royce's "initiated at design, completed at testing" structure.

---

## 5. The "Overview Document" — Missing from Our Engine

Royce's Step 1 mandates a system-level Overview Document produced at preliminary design time. Its defining characteristic: it must be comprehensible to every team member, regardless of specialization. It is not an SRS (which is audience-specific and requirements-focused) and not an HLD (which is architecture-focused). It is the shared mental model of the system that coordinates all subsequent work.

Royce's rationale: storage and timing allocations made at preliminary design affect every subsequent artifact. Without a shared overview, different team members operate from incompatible system models, and integration failures are guaranteed.

**Current engine gap:** No skill in the engine produces this artifact. The closest candidates are:
- `02-requirements-engineering/waterfall/03-descriptive-modeling` — produces a system description but not an executable design-level overview
- `03-design-documentation/` — produces architecture and design artifacts but not a cross-role orientation document

The Overview Document is a distinct skill that should precede both the full SRS and the detailed design phase.

---

## 6. Formal Customer Review Gates — Missing from Our Engine

The PSR, CSR, and FSAR are not reviews of documentation quality. They are contractual communication events in which the customer formally validates that the project trajectory matches the original intent. Each gate has defined inputs, defined outputs, and a defined recycling path if the review fails.

Regulated industries (DoD, FDA, aerospace) implement these gates as non-negotiable contract deliverables. They are enforced by standards such as MIL-STD-498, DO-178C, and 21 CFR Part 11.

**Current engine gap:** `08-semantic-auditing` (Skill 08 in the waterfall pipeline) performs V&V against IEEE 830 criteria. This is an internal quality function with the document as its subject. Customer review gates are external communication functions with the customer as the primary actor. They require separate artifacts: gate entry criteria, review minutes, action item logs, and formal approval signatures.

No skill in the current engine produces PSR, CSR, or FSAR documentation packages.

---

## 7. "Do It Twice" — The Pilot/Prototype Gap

Royce identifies the pilot/prototype as the highest-value risk reduction available to a software project, secondary only to documentation. His argument: no amount of human expert judgment produces reliable storage and timing estimates for a novel system. The only reliable source is measurement from a working implementation.

A 10-month pilot for a 30-month project absorbs 33% of the schedule. Royce treats this as a cost reduction, not a cost addition — because the alternative is late-phase discovery of fundamental design failures, which costs more than the pilot in rework alone.

**Current engine gap:** The engine has no Pilot Model, Proof-of-Concept Plan, or Prototype Evaluation skill. Agile methodologies address this through sprints and MVPs (`07-agile-artifacts/`), but the waterfall pipeline (`02-requirements-engineering/waterfall/`) has no equivalent mechanism. A consultant executing a waterfall engagement with the engine has no structured path to recommend or document a pilot.

---

## 8. Aroral's SWOT Applied to Our Engine

Aroral (2021) provides a structured SWOT and a PMBOK mapping that clarifies when the engine's waterfall skills are appropriate and when they are not.

**SWOT Summary:**

| Dimension | Finding | Engine Implication |
|-----------|---------|-------------------|
| Strength | Strong for stable, well-understood requirements | Engine's waterfall skills are correctly positioned for regulated, requirements-stable projects |
| Weakness | Integration deferred to end; large projects accumulate undetected interface failures | Confirms Royce's CSR gate gap; engine needs interface validation checkpoints |
| Opportunity | Waterfall remains valid for predictable environments (infrastructure, compliance-driven systems) | Engine's `09-governance-compliance/` skills complement waterfall skills correctly |
| Threat | Fast-paced, evolving requirements environments render waterfall ineffective | Engine correctly separates `07-agile-artifacts/` from `02-requirements-engineering/waterfall/`; consultant guidance on methodology selection is needed |

**PMBOK Stage Mapping to Engine Phases:**

| PMBOK Stage | Engine Phase | Alignment |
|-------------|-------------|-----------|
| Initiation | `00-meta-initialization/`, `01-strategic-vision/` | Aligned |
| Planning | `02-requirements-engineering/` | Aligned, but missing preliminary design gate |
| Execution | `03-design-documentation/`, `04-development-artifacts/` | Aligned |
| Monitoring | `08-semantic-auditing/` (V&V skill), `09-governance-compliance/` | Partial — no active monitoring skill; V&V is post-hoc |
| Closure | `05-testing-documentation/`, `06-deployment-operations/` | Aligned |

Aroral's key finding — that waterfall's core failure is end-of-project integration — maps directly to the absence of Royce's CSR gates in our pipeline. The engine currently has no mechanism for mid-project customer validation of design decisions.

---

## 9. Improvements to Apply to This Engine

The following improvements are prioritized by risk-reduction impact, mapped to affected files.

**Priority 1 — Critical (addresses Royce's identified failure modes):**

1. **Add Preliminary Design Gate skill** before `02-requirements-engineering/waterfall/05-feature-decomposition`. New skill: `02-requirements-engineering/waterfall/00-preliminary-design-overview/`. Produces the Overview Document and allocates storage/timing/interface budgets before analysis locks scope.

2. **Initiate Test Plan at Design phase.** Add a Test Plan stub skill to `03-design-documentation/` that is formally completed by `05-testing-documentation/02-test-plan`. Update `02-requirements-engineering/waterfall/README.md` and `05-testing-documentation/README.md` to document this cross-phase dependency.

3. **Add Customer Review Gate documents.** New skills for PSR, CSR, and FSAR packages, located in a new `02-requirements-engineering/waterfall/review-gates/` directory. Each skill produces: entry criteria checklist, review agenda template, action item log, and formal approval stub.

**Priority 2 — High (addresses significant documentation gaps):**

4. **Add Pilot/Proof-of-Concept Plan skill.** New skill in `02-requirements-engineering/waterfall/` or as a cross-phase skill in `skills/`. Produces a scoped pilot definition: objectives, duration estimate, measurement criteria, and evaluation report template.

5. **Add phase-completion enforcement gates.** Extend `08-semantic-auditing/` to include a phase-gate checklist that must resolve before the next phase begins. Currently `08-semantic-auditing` is terminal (end of pipeline). It should also have per-phase variants.

**Priority 3 — Moderate (clarifies existing skills):**

6. **Revise `03-design-documentation/` README** to distinguish Preliminary Design Spec (Doc 2) from Final Design Spec (Doc 4) and add explicit As-Built update instructions.

7. **Add methodology selection guidance** to `00-meta-initialization/new-project/SKILL.md`. Based on Aroral's SWOT, consultants need decision criteria for waterfall vs. agile. Trigger: requirements stability assessment during project initialization.

8. **Add Interface Design Spec as a design-phase artifact** (`03-design-documentation/`). Currently `04-interface-specification` is in the requirements phase. Royce places it at preliminary design. Both phases need the artifact — requirements capture the need; design specifies the solution.

---

## 10. Royce's Phase Sequence vs. Our Current Pipeline

| Step | Royce's Intended Sequence (1970) | Our Current Pipeline | Deviation |
|------|----------------------------------|---------------------|-----------|
| 1 | System Requirements | `00-meta-initialization/` + `01-strategic-vision/` | Aligned |
| 2 | **Preliminary Program Design** (allocates storage, timing, interfaces) | **Not present** | **Missing phase** |
| 3 | Software Requirements (informed by design constraints) | `02-requirements-engineering/waterfall/01–08` | Sequenced before design constraints are known |
| 4 | Program Design (detailed; multiple CSR cycles with customer) | `03-design-documentation/` | Present; CSR gates absent |
| 5 | Coding | `04-development-artifacts/` | Aligned |
| 6 | Testing (test plan already exists from Step 4) | `05-testing-documentation/` | Test plan initiated too late |
| 7 | Operations | `06-deployment-operations/` | Aligned |
| — | Pilot/Prototype (Royce Step 3; runs parallel to Steps 2–5) | **Not present** | **Missing entirely** |
| — | PSR, CSR, FSAR (Royce Step 5; gates at Steps 2, 4, 6) | **Not present** | **Missing entirely** |
| — | V&V Audit | `02-requirements-engineering/waterfall/08-semantic-auditing` | Present; terminal only |

**Summary of deviations:** The engine's waterfall pipeline correctly covers requirements, design, development, testing, and operations. It is missing three structural elements Royce identifies as essential: the preliminary design gate, the pilot/prototype mechanism, and the formal customer review gates. The test plan timing is structurally inverted relative to Royce's model. These gaps represent the same failure modes that have caused waterfall projects to fail for fifty years — not because waterfall is wrong, but because the corrective steps were never adopted.

---

*This document is part of the March 14 engine review series. See also `01-` and `02-` documents in this directory for related analysis.*
