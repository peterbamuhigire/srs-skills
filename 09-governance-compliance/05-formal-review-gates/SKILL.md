---
name: formal-review-gates
phase: "09-governance-compliance"
description: Generate PSR, CSR, and FSAR formal customer review gate documents per Royce (1970) Step 5
standard: IEEE 1028-2008 (Software Reviews), IEEE 15288 (System Life Cycle)
---

# Skill: Formal Review Gates (PSR / CSR / FSAR)

## Source
Royce, W.W. (1970). Managing the Development of Large Software Systems. IEEE WESCON, p. 335-337. Step 5: Involve the Customer.

## Purpose
Generate formal customer review gate documentation for three mandatory review points in the waterfall lifecycle. These reviews commit the customer at earlier points, preventing the "contractor free rein" failure mode Royce identified.

## Trigger
User says: "generate review gates", "create PSR document", "generate CSR", "prepare FSAR", "customer review documentation"

## Three Review Gates

### PSR — Preliminary Software Review
**Timing:** After Preliminary Program Design (Phase 03 HLD complete)
**Purpose:** Customer commits to the architecture before detailed design begins
**Attendees:** Customer representative, project manager, lead architect, systems analyst
**Outputs:** PSR minutes, action items, customer sign-off on HLD

**PSR Document Template:**
Generate to: `projects/<ProjectName>/09-governance-compliance/05-formal-review-gates/PSR.md`

```markdown
# Preliminary Software Review (PSR)

**Project:** <ProjectName>
**Date:** <date>
**Location/Platform:** <location>
**Royce Reference:** IEEE WESCON 1970, Step 5

## Attendees
| Name | Role | Organization |
|------|------|-------------|

## Review Scope
- Software Requirements (Doc 1): ☐ Reviewed ☐ Approved ☐ Conditional ☐ Rejected
- Preliminary Design Spec (Doc 2): ☐ Reviewed ☐ Approved ☐ Conditional ☐ Rejected

## Architecture Decisions Confirmed
[List each major architectural decision agreed at this review]

## Open Items / Action Items
| ID | Item | Owner | Due Date |
|----|------|-------|----------|

## Customer Commitment
By attending this PSR and not formally objecting in writing within 5 business days, the customer commits to the Preliminary Design as the basis for detailed design.

**Customer Representative Signature:** _________________ Date: _________
**Project Manager Signature:** _________________ Date: _________
```

---

### CSR — Critical Software Review
**Timing:** During/after Program Design (Phase 03 complete, multiple rounds permitted)
**Purpose:** Customer reviews detailed design decisions before coding begins; catches requirement misinterpretations
**Attendees:** Customer representative, full design team
**Outputs:** CSR minutes, design issue log, customer approval to proceed to coding

**CSR Document Template:**
Generate to: `projects/<ProjectName>/09-governance-compliance/05-formal-review-gates/CSR-<n>.md`
(Multiple CSRs permitted — number them CSR-1, CSR-2, etc.)

Key sections: Design compliance matrix (each requirement → design element), open design issues, customer approval statement.

---

### FSAR — Final Software Acceptance Review
**Timing:** After testing complete, before operations handover
**Purpose:** Final customer acceptance; commits customer to operational deployment
**Attendees:** Customer, project manager, test lead, operations lead
**Outputs:** FSAR report, acceptance certificate, known issues register

**FSAR Document Template:**
Generate to: `projects/<ProjectName>/09-governance-compliance/05-formal-review-gates/FSAR.md`

Key sections: Test results summary, all-requirements coverage statement, known defects with severity/disposition, formal acceptance statement, operations readiness confirmation.

---

## Execution Instructions

When generating any review gate document:
1. Read `projects/<ProjectName>/_context/vision.md` for project context
2. Read `projects/<ProjectName>/_context/stakeholders.md` for attendee roles
3. Read the relevant completed documents (HLD for PSR, LLD/API spec for CSR, Test Report for FSAR)
4. Generate the document with all sections populated from available context
5. Flag with `<!-- TODO: CUSTOMER SIGNATURE REQUIRED -->` any field requiring physical signature

## Standards References
- IEEE 1028-2008: Software Reviews and Audits
- IEEE 15288-2015: System Life Cycle Processes (Section 6.4.7 Verification Process)
- Royce (1970): Step 5, Figure 9, p.337
