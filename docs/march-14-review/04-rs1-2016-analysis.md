# RS1_2016 Literature Review: Analysis & Applied Improvements
**Source:** RS1_2016_1_59_Bab2.pdf — Chapter 2 (Literature Review), undergraduate thesis, 2016
**Subject:** Building a "Love String" Android app (Five Love Languages domain)
**Analyst:** Claude Sonnet 4.6
**Date:** 2026-03-15

---

## Document Overview

This is the literature review chapter of a 2016 undergraduate thesis for an Android mobile application. Unlike Royce (1970) which directly critiques waterfall methodology, or Aroral (2021) which provides a SWOT analysis of SDLC models, this document is a textbook survey covering:

1. **Waterfall Model** (Pressman, 2010 — 5 phase version: Communication, Planning, Modeling, Construction, Deployment)
2. **Object-Oriented Concepts** (classes, objects, attributes, methods, inheritance, polymorphism, messages)
3. **Java** (platform independence, JVM, bytecode, JDK/API)
4. **Android** (Linux kernel, open source, API-driven versioning)
5. **UML** (Use Case, Activity, Sequence, Class Diagrams, ERD)
6. **Software Testing** (Black-box testing, Eight Golden Rules, Five Measurable Human Factors)
7. **Android Studio, SQLite, Five Love Languages domain**

The document's academic value to the SRS-Skills project is **targeted but real**: sections 2.5 (UML) and 2.6 (Testing/Evaluation) contain specific frameworks that are either absent from or less precisely specified in our current skills.

---

## Applicable Findings

### Finding 1: Whitten & Bentley 4-Actor Taxonomy (Section 2.5.1)

The current use-case-modeling skill uses a 3-class actor taxonomy (Primary / Supporting / Offstage) from Cockburn's "Writing Effective Use Cases." RS1 documents Whitten & Bentley's alternative 4-class taxonomy, which is more common in enterprise business systems analysis:

| Actor Type | Definition |
|------------|------------|
| **Primary Business Actor** | Receives measurable value from the use case **without initiating it** |
| **Primary System Actor** | **Directly initiates or triggers** the use case event |
| **External Server Actor** | Responds to a request from a use case (service provider) |
| **External Receiver Actor** | Not a primary actor; receives output/value from the use case |

**Gap identified:** The distinction between "who benefits" vs "who initiates" is collapsed in the 3-class model. In enterprise systems (e.g., an approval workflow where the Approver initiates but the Requester benefits), this distinction is necessary for correct actor assignment.

**Applied to:** `09-use-case-modeling/SKILL.md` — Step 2 now offers both taxonomies with guidance on when to apply each.

---

### Finding 2: Temporal Actor / Temporal Events (Section 2.5.1)

RS1 explicitly notes: *"there are events which triggered by the calendar or the time on a clock... The events which triggered automatically in that way are called as temporal events, and the actor of such temporal event is the time."*

**Gap identified:** Our use-case-modeling skill does not mention temporal actors. Scheduled processes (nightly batch jobs, billing cycles, reminder notifications, session expiry) are common in enterprise systems but currently have no modeling guidance in our skill.

**Applied to:** `09-use-case-modeling/SKILL.md` — Step 2 actor classification adds Temporal Actor guidance.

---

### Finding 3: "Depends On" Use Case Relationship (Section 2.5.1)

RS1 documents a fourth use case relationship type absent from our skill:

> *"Depends on relationship in use case diagram provides a model that helps in planning and scheduling purposes. Depends on relationship is shown as an arrow-headed line labeled with `<<depends on>>`."*

Our skill currently covers only: Association, `<<include>>`, `<<extend>>`, and Actor Generalization. The `<<depends on>>` relationship communicates development sequencing (UC-B cannot be built before UC-A is complete) and is particularly valuable for the project planning context of our consultants.

**Applied to:** `09-use-case-modeling/SKILL.md` — Step 4 Use Case Diagram adds `<<depends on>>` as a relationship type.

---

### Finding 4: Expanded Use Case Narrative Fields (Section 2.5.1)

RS1 documents an "expanded use case narrative" that includes two fields not present in our current template:

- **Assumptions** — assumptions made by the author that affect the use case
- **Implementation Constraints and Specifications** — technical constraints that bound implementation choices

Our current template has: UC-ID, Name, Primary Actor, Stakeholders, Preconditions, Success Guarantee, Minimal Guarantee, Priority, Frequency, Trigger, Main Success Scenario, Alternative Flows, Exception Flows, Business Rules, Data Requirements, Open Issues.

**Missing:** Assumptions and Implementation Constraints — both are standard in Whitten & Bentley fully-dressed format and prevent ambiguity that surfaces during implementation.

**Applied to:** `09-use-case-modeling/SKILL.md` — Step 5 template expanded.

---

### Finding 5: Eight Golden Rules of UI Design (Section 2.6.2)

Shneiderman & Plaisant (2010, p.88-89) define Eight Golden Rules that are a classic, well-cited UI heuristic evaluation framework. Our UX specification skill currently cites ISO 9241-210, ISO 25010, and WCAG 2.1 AA — but not Shneiderman's Golden Rules, which are more actionable for rapid design review.

The Eight Golden Rules:
1. Strive for Consistency
2. Seek Universal Usability
3. Offer Informative Feedback
4. Design Dialogs to Yield Closure
5. Prevent Errors
6. Permit Easy Reversal of Actions
7. Keep Users in Control
8. Reduce Short-term Memory Load

**Gap identified:** Our skill has a detailed usability testing section but no heuristic evaluation framework. Heuristic evaluation (applying Golden Rules during design review, before a usability test is conducted) is a standard lower-cost alternative that consultants can apply without test participants.

**Applied to:** `05-ux-specification/SKILL.md` — Step 7 (Usability Testing Protocol) extended with a Heuristic Evaluation section using the Eight Golden Rules.

---

### Finding 6: Five Measurable Human Factors (Section 2.6.3)

Shneiderman & Plaisant (2010, p.162) define five measurable factors for UX evaluation:

1. **Time to Learn** — how long to learn the features
2. **Performance Speed** — how fast the system responds
3. **User's Level of Error** — how often users make errors
4. **User's Memory** — how long users retain knowledge of the application
5. **Subjective Satisfaction** — satisfaction felt by user

Our current metrics table covers: Task Completion Rate, Time on Task, Error Rate, and SUS Score. This maps to factors 2, 3, and 5 but omits:
- **Time to Learn** (learnability — critical for enterprise tools used by training-heavy client organizations)
- **User's Memory** (retention — important for infrequently used features like approval workflows)

**Applied to:** `05-ux-specification/SKILL.md` — Step 7 metrics table expanded to formally include all five factors.

---

### Finding 7: V&V Canonical Definitions (Section 2.6)

RS1 cites Pressman's canonical V&V distinction:
- **Verification:** "Are we building the product right?" (correct implementation of functions)
- **Validation:** "Are we building the right product?" (suitability to user requirements)

Our Phase 09 audit skill uses V&V language but does not anchor to these canonical definitions explicitly in the output document. Adding these definitions to the audit report header section would make the report self-contained and more defensible.

**Applied to:** `09-governance-compliance/02-audit-report/SKILL.md` — Section 1 of the output template adds canonical V&V definitions.

---

## Findings NOT Applied

The following content from RS1 was reviewed and deemed either already covered or not applicable:

- **Waterfall model description** (Pressman's 5-phase version) — already covered by Royce analysis; our engine uses a more rigorous waterfall model
- **OOP concepts** (classes, inheritance, polymorphism) — not relevant to documentation generation
- **Java, Android, Android Studio, SQLite** — technology-specific; not relevant
- **ERD / Sequence Diagram / Class Diagram** sections — our existing skills already handle these in LLD and database design; no new information
- **Black-box testing description** — already implied by our Test Plan skill's "every 'shall' statement becomes a test case" instruction
- **Love Languages domain** — not relevant

---

## Summary of Improvements Applied

| Finding | Skill Modified | Type |
|---------|----------------|------|
| F1: Whitten & Bentley 4-actor taxonomy | `09-use-case-modeling/SKILL.md` | Enhancement |
| F2: Temporal Actor / temporal events | `09-use-case-modeling/SKILL.md` | Addition |
| F3: `<<depends on>>` relationship | `09-use-case-modeling/SKILL.md` | Addition |
| F4: Assumptions + Implementation Constraints fields | `09-use-case-modeling/SKILL.md` | Enhancement |
| F5: Eight Golden Rules heuristic evaluation | `05-ux-specification/SKILL.md` | Addition |
| F6: Time to Learn + User's Memory metrics | `05-ux-specification/SKILL.md` | Enhancement |
| F7: Canonical V&V definitions | `09-governance-compliance/02-audit-report/SKILL.md` | Enhancement |

---

## Standards Added to Project

- **Shneiderman & Plaisant (2010)** — *Designing the User Interface: Strategies for Effective Human-Computer Interaction* — Eight Golden Rules (Section 2.6.2) and Five Measurable Human Factors (Section 2.6.3)
- **Whitten & Bentley (2007)** — *Systems Analysis and Design Methods* — 4-type actor taxonomy, use case relationship types including `<<depends on>>`
- **Pressman (2010)** — V&V canonical definitions (already implied in our CLAUDE.md; now formally anchored)
