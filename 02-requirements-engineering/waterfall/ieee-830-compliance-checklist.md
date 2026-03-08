# IEEE 830-1998 Compliance Checklist

> **Authoritative Reference for All Waterfall SRS Skills**
> Every skill in the `02-requirements-engineering/waterfall/` pipeline SHALL reference this checklist to ensure generated requirements meet IEEE Std 830-1998.

---

## Part 1: Eight Quality Attributes (IEEE 830 §4.3)

### IEEE830-4.3.1 Correct

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| Every requirement reflects stakeholder intent | Requirement traces to `vision.md` goal or `features.md` entry | Requirement exists with no source document reference |
| Agrees with higher-level specifications | No contradiction between SRS sections and `vision.md` | Section 3.2 states "offline-only" but vision says "cloud-first" |

### IEEE830-4.3.2 Unambiguous

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| Single interpretation per requirement | No weak words: should, might, could, may, possibly, preferably, ideally, somewhat, user-friendly, highly, intelligent, optimized | "The system should handle large datasets" |
| Terms defined in glossary | Every domain term appears in Section 1.3 or `glossary.md` | "The system shall update the ledger" without defining "ledger" |
| Natural language reviewed | Active voice, one "shall" per clause | "The system shall validate and process and store the input" |

### IEEE830-4.3.3 Complete

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| All features have requirements | Every `features.md` entry maps to at least one Section 3.2 requirement | Feature "Inventory Alerts" has no requirements |
| Valid and invalid inputs addressed | Each stimulus has both success and error responses | Only happy-path described, no error handling |
| All figures/tables labeled | Every table and diagram has a caption and reference | Unlabeled block diagram in Section 2.1 |
| TBD protocol followed | Every TBD includes: (a) condition/reason, (b) resolution action, (c) responsible party, (d) deadline | "Response time: TBD" with no resolution plan |

### IEEE830-4.3.4 Consistent

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| No conflicting requirements | No two requirements specify contradictory behavior | R-REQ-005 says "tabular output," R-REQ-012 says "textual output" for same report |
| Uniform terminology | Same real-world object uses same term throughout | "prompt" in Section 3.2.1, "cue" in Section 3.2.4 for identical concept |
| No duplicate requirements | Each requirement appears exactly once | Same "shall" statement in Section 3.2.3 and Section 3.2.7 |

### IEEE830-4.3.5 Ranked for Importance and/or Stability

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| Every requirement has a ranking | Labeled Essential, Conditional, or Optional | Requirement with no priority indicator |
| Stability noted where applicable | Volatile requirements flagged with expected change frequency | Core pricing algorithm marked stable; seasonal discount rules flagged as volatile — but neither is labeled |

**Definitions (IEEE 830 §4.3.5.2):**
- **Essential:** Software unacceptable without this requirement.
- **Conditional:** Enhances the product but absence does not make it unacceptable.
- **Optional:** May or may not be worthwhile; supplier may propose alternatives.

### IEEE830-4.3.6 Verifiable

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| Finite, cost-effective test exists | Requirement contains measurable quantity or deterministic criterion | "The system shall work well" |
| No subjective terms | No "good," "easy," "fast," "usually" without quantification | "The system shall usually respond quickly" |
| Measurable target present | Contains numeric threshold: ms, s, %, count, or defined pass/fail | "The system shall be responsive" |

**Compliant Example:** "The system shall produce output within 20 s of event X 60% of the time and within 30 s 100% of the time."

### IEEE830-4.3.7 Modifiable

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| Coherent organization | TOC present, sections numbered, cross-references explicit | Flat list of requirements with no grouping |
| No redundancy | Each requirement stated once; if repeated, explicit cross-reference provided | Same requirement in Section 3.2.1 and 3.2.5 without cross-ref |
| Single requirement per clause | One "shall" per numbered requirement | Compound requirement with three "shall" statements |

### IEEE830-4.3.8 Traceable

| Criterion | Pass Condition | Fail Example |
|-----------|---------------|--------------|
| Backward traceability | Each requirement references its source (vision goal, feature, stakeholder need) | R-REQ-015 has no source reference |
| Forward traceability | Each requirement has a unique ID (R-REQ-NNN format) | Requirements without identifiers |
| RTM exists | Traceability matrix links requirements to business goals, design, and test cases | No traceability matrix produced |

---

## Part 2: SRS Structure Checklist (IEEE 830 §5)

### Section 1 — Introduction (§5.1) → Generated by Phase 02

| ID | Section | Required Content | IEEE Clause |
|----|---------|-----------------|-------------|
| IEEE830-5.1.1 | 1.1 Purpose | Problem statement, intended audience | §5.1.1 |
| IEEE830-5.1.2 | 1.2 Scope | Product name, what it will/will not do, benefits/objectives/goals, consistency with higher-level specs | §5.1.2 |
| IEEE830-5.1.3 | 1.3 Definitions | All terms, acronyms, abbreviations (or reference to glossary appendix) | §5.1.3 |
| IEEE830-5.1.4 | 1.4 References | Complete list with title, report number, date, publisher, source | §5.1.4 |
| IEEE830-5.1.5 | 1.5 Overview | Description of SRS structure and organization | §5.1.5 |

### Section 2 — Overall Description (§5.2) → Generated by Phase 03

| ID | Section | Required Content | IEEE Clause |
|----|---------|-----------------|-------------|
| IEEE830-5.2.1 | 2.1 Product Perspective | System context, block diagram, plus all 8 sub-items below | §5.2.1 |
| IEEE830-5.2.1.1 | 2.1.1 System Interfaces | System interface list with functionality and interface description | §5.2.1.1 |
| IEEE830-5.2.1.2 | 2.1.2 User Interfaces | Logical characteristics, screen layouts, accessibility constraints | §5.2.1.2 |
| IEEE830-5.2.1.3 | 2.1.3 Hardware Interfaces | Logical characteristics, ports, instruction sets, protocols | §5.2.1.3 |
| IEEE830-5.2.1.4 | 2.1.4 Software Interfaces | Name, mnemonic, version, source for each dependency; interface purpose and message format | §5.2.1.4 |
| IEEE830-5.2.1.5 | 2.1.5 Communications Interfaces | Network protocols, local network requirements | §5.2.1.5 |
| IEEE830-5.2.1.6 | 2.1.6 Memory Constraints | Primary and secondary memory limits | §5.2.1.6 |
| IEEE830-5.2.1.7 | 2.1.7 Operations | Normal/special operations, interactive/unattended periods, backup/recovery | §5.2.1.7 |
| IEEE830-5.2.1.8 | 2.1.8 Site Adaptation | Site-specific data, initialization sequences, mission-related modifications | §5.2.1.8 |
| IEEE830-5.2.2 | 2.2 Product Functions | Summary of major functions with logical relationships | §5.2.2 |
| IEEE830-5.2.3 | 2.3 User Characteristics | Education, experience, technical expertise of intended users | §5.2.3 |
| IEEE830-5.2.4 | 2.4 Constraints | Regulatory, hardware, interface, parallel operation, audit, control, language, protocol, reliability, criticality, safety/security | §5.2.4 |
| IEEE830-5.2.5 | 2.5 Assumptions and Dependencies | Factors affecting requirements that are not design constraints | §5.2.5 |
| IEEE830-5.2.6 | 2.6 Apportioning of Requirements | Requirements deferred to future versions | §5.2.6 |

### Section 3 — Specific Requirements (§5.3) → Generated by Phases 04–07

| ID | Section | Required Content | IEEE Clause |
|----|---------|-----------------|-------------|
| IEEE830-5.3.1 | 3.1 External Interfaces | Detailed I/O: name, purpose, source/destination, range, units, timing, relationships, formats | §5.3.1 |
| IEEE830-5.3.2 | 3.2 Functions | Validity checks, operation sequences, abnormal responses (overflow, comms failure, error recovery), parameter effects, I/O relationships and formulas | §5.3.2 |
| IEEE830-5.3.3 | 3.3 Performance | Static (terminals, users, data volume) and dynamic (transactions/time) numerical requirements — all measurable | §5.3.3 |
| IEEE830-5.3.4 | 3.4 Logical Database | Information types, frequency, access, entities/relationships, integrity constraints, retention | §5.3.4 |
| IEEE830-5.3.5 | 3.5 Design Constraints | Standards compliance, hardware limitations | §5.3.5 |
| IEEE830-5.3.5.1 | 3.5.5 Standards Compliance | Report formats, data naming, accounting procedures, audit tracing derived from standards/regulations | §5.3.5.1 |
| IEEE830-5.3.6 | 3.6 Software System Attributes | Reliability, Availability, Security, Maintainability, Portability — each objectively verifiable | §5.3.6 |
| IEEE830-5.3.7 | 3.7 Other Requirements | Requirements not fitting Sections 3.1–3.6 (or explicit "None" statement) | §5.3.8 |

### Supporting Information (§5.4) → Generated by Phase 08

| ID | Section | Required Content | IEEE Clause |
|----|---------|-----------------|-------------|
| IEEE830-5.4.1 | TOC | Table of contents following general compositional practices | §5.4.1 |
| IEEE830-5.4.2 | Index | Keyword index for large SRS documents | §5.4.1 |
| IEEE830-5.4.3 | Appendixes | Sample I/O, background info, problem descriptions; explicitly state if appendixes are part of requirements | §5.4.2 |

---

## Part 3: Annex A Template Selection Guide

The SRS Section 3 SHALL be organized using one of the IEEE 830 Annex A templates. The chosen template SHALL be documented in the SRS Overview (Section 1.5).

| Template | Annex | Best For | Organization Axis |
|----------|-------|----------|-------------------|
| By System Mode (V1) | A.1 | Systems with distinct operational modes (training, normal, emergency) | Mode → Functions |
| By System Mode (V2) | A.2 | Mode-dependent interfaces and performance | Mode → Interfaces → Functions → Performance |
| By User Class | A.3 | Systems serving distinct user groups (admin, operator, customer) | User Class → Functions |
| By Object | A.4 | Object-oriented systems with real-world entity modeling | Class/Object → Attributes → Functions → Messages |
| **By Feature** | **A.5** | **Feature-rich systems described as stimulus-response sequences** | **Feature → Stimulus/Response → Functions** |
| By Stimulus | A.6 | Event-driven or reactive systems | Stimulus → Functions |
| By Functional Hierarchy | A.7 | Data-flow-oriented systems with complex process chains | Information Flows → Processes → Data Constructs → Data Dictionary |
| Combined (User Class + Feature) | A.8 | Systems needing both user-class and feature decomposition | User Class → Feature → Stimulus/Response → Functions |

**Default for this pipeline:** Template A.5 (By Feature) — aligns with the stimulus-response pattern enforced by Phase 05 (Feature Decomposition).

---

## Part 4: TBD Protocol (IEEE 830 §4.3.3.1)

Every TBD entry in the SRS SHALL include all four fields:

```markdown
**[TBD-NNN]:** [Description of the undetermined requirement]
- **Condition:** [Why the answer is not yet known]
- **Resolution:** [What must be done to eliminate the TBD]
- **Owner:** [Person or role responsible]
- **Deadline:** [Date by which the TBD must be resolved]
```

**Anti-pattern:** `Response time: TBD` — fails completeness because it lacks condition, resolution plan, owner, and deadline.

---

## Part 5: Anti-Patterns and Fixes

| Anti-Pattern | IEEE Clause Violated | Fix |
|---|---|---|
| "The system shall be fast" | §4.3.6 Verifiable | "The system shall respond within 500 ms under 100 concurrent users" |
| "The system should validate input" | §4.3.2 Unambiguous | "The system shall reject input values outside the range 1–999" |
| "The system shall validate, transform, and store data" | §4.3.7 Modifiable | Split into three separate "shall" clauses |
| "See above" without section reference | §4.3.8 Traceable | "As specified in R-REQ-003 (Section 3.2.1)" |
| Feature X has no requirements | §4.3.3 Complete | Add functional requirements for Feature X or move to Section 2.6 |
| Priority not stated | §4.3.5 Ranked | Add "Priority: Essential" to every requirement |
| Same requirement in two sections | §4.3.7 Modifiable | Remove duplicate; add cross-reference if needed |
| "TBD" with no context | §4.3.3.1 TBD Protocol | Add condition, resolution, owner, deadline per Part 4 |
| No Section 2.6 | §5.2.6 | Add "2.6 Apportioning of Requirements" even if empty ("None deferred") |
| No Section 3.6 | §5.3.8 | Add "3.6 Other Requirements" even if empty ("None identified") |

---

## Part 6: Skill-to-Clause Mapping

| Skill Phase | IEEE 830 Clauses Covered | Checklist IDs |
|---|---|---|
| 02 Context Engineering | §5.1.1–§5.1.5 | IEEE830-5.1.1 through IEEE830-5.1.5 |
| 03 Descriptive Modeling | §5.2.1–§5.2.6 | IEEE830-5.2.1 through IEEE830-5.2.6 |
| 04 Interface Specification | §5.3.1 | IEEE830-5.3.1 |
| 05 Feature Decomposition | §5.3.2 | IEEE830-5.3.2 |
| 06 Logic Modeling | §5.3.4 | IEEE830-5.3.4 |
| 07 Attribute Mapping | §5.3.3, §5.3.5, §5.3.5.1, §5.3.6, §5.3.7 | IEEE830-5.3.3 through IEEE830-5.3.7 |
| 08 Semantic Auditing | §4.3.1–§4.3.8, §5.4 | IEEE830-4.3.1 through IEEE830-4.3.8, IEEE830-5.4.1–5.4.3 |

---

**Standard:** IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications
**Maintained by:** SDLC-Docs-Engine Waterfall Pipeline
**Last Updated:** 2026-03-08
