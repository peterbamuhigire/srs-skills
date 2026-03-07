---
name: elicitation-toolkit
description: Multi-technique requirements gathering skill that guides the AI through choosing and executing the right elicitation techniques per IEEE 29148 Section 6.3 and Wiegers Practices 4-6.
---

# Elicitation Toolkit Skill

## Overview

This skill provides a structured, multi-technique approach to requirements elicitation. It guides the AI through selecting the most appropriate elicitation technique based on stakeholder availability, domain complexity, and requirements maturity, then executes the chosen technique to produce a grounded elicitation log. The skill supports interviews, Joint Application Development (JAD) workshops, prototyping, observation, and questionnaires, with domain-specific checklist hooks for specialized industries.

## When to Use This Skill

- After the stakeholder register has been produced by `01-stakeholder-analysis`
- When requirements need to be gathered from diverse stakeholder groups
- When the elicitation technique is unclear and a decision framework is needed
- When domain-specific requirements (healthcare, SaaS, POS, GIS) require specialized checklists
- When previous elicitation rounds produced incomplete or ambiguous requirements

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `../output/stakeholder_register.md`, `../project_context/vision.md`, `../project_context/features.md` |
| **Output** | `../output/elicitation_log.md` |
| **Tone** | Investigative, methodical, source-attributed |
| **Standards** | IEEE 29148-2018 Section 6.3, Laplante Ch.4, Wiegers Practices 4-6 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| stakeholder_register.md | `../output/stakeholder_register.md` | Yes | Stakeholder roles, communication preferences, engagement levels |
| vision.md | `../project_context/vision.md` | Yes | Business goals, problem statement, domain context |
| features.md | `../project_context/features.md` | Yes | Feature list for elicitation scoping |
| glossary.md | `../project_context/glossary.md` | No | Domain terminology for consistent language |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| elicitation_log.md | `../output/elicitation_log.md` | Structured findings with source attribution, technique used, and confidence levels |

## Core Instructions

Follow these six steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `stakeholder_register.md` from `../output/`, and `vision.md` and `features.md` from `../project_context/`. Optionally read `glossary.md`. Log every file path read. If any required file is missing, halt execution and report the gap.

### Step 2: Assess Elicitation Context

Evaluate three dimensions to determine the appropriate elicitation technique:

**Dimension 1 -- Stakeholder Availability**

| Level | Description | Indicator |
|-------|-------------|-----------|
| High | Stakeholders are accessible for extended, interactive sessions | On-site team, dedicated availability windows |
| Medium | Stakeholders are available for scheduled sessions with limited duration | Remote team, shared across projects |
| Low | Stakeholders are difficult to reach or available only asynchronously | External clients, regulators, distributed globally |

**Dimension 2 -- Domain Complexity**

| Level | Description | Indicator |
|-------|-------------|-----------|
| High | Domain requires specialized knowledge, regulatory compliance, or complex workflows | Healthcare, finance, aerospace, legal |
| Medium | Domain has moderate complexity with some specialized terminology | E-commerce, SaaS, logistics |
| Low | Domain is well-understood with common patterns | CRUD applications, content management |

**Dimension 3 -- Requirements Maturity**

| Level | Description | Indicator |
|-------|-------------|-----------|
| Greenfield | No existing requirements; starting from scratch | New product, new market |
| Evolving | Partial requirements exist but need refinement | MVP iteration, feature expansion |
| Mature | Well-documented existing requirements needing validation | System migration, modernization |

### Step 3: Select Elicitation Technique

Use the following decision matrix to recommend one or more techniques:

| Context | Primary Technique | Secondary Technique |
|---------|-------------------|---------------------|
| High availability + High complexity + Greenfield | JAD Workshop | Interview |
| High availability + Low complexity + Greenfield | Interview | Prototyping |
| Medium availability + High complexity + Evolving | Interview | Observation |
| Medium availability + Medium complexity + Evolving | Prototyping | Questionnaire |
| Low availability + Any complexity + Any maturity | Questionnaire | Document Analysis |
| Any availability + High complexity + Mature | Observation | Interview |
| Any availability + Low complexity + Mature | Questionnaire | Document Analysis |

Present the recommendation to the user with rationale. The user may override the selection.

### Step 4: Execute Elicitation Technique

Execute the selected technique using the corresponding protocol. Each technique produces structured findings.

#### Technique A: Structured Interview

1. Select target stakeholders from the register (prioritize "Manage Closely" and "Keep Informed" quadrants)
2. Prepare interview questions using the three-tier approach:
   - **Context questions**: Establish the stakeholder's role and perspective
   - **Open-ended questions**: Explore needs, pain points, and workflows
   - **Closed questions**: Confirm specific requirements, constraints, and priorities
3. For each finding, record:
   - Source stakeholder (by ID from the register)
   - Verbatim statement or paraphrase
   - Requirement type: Functional, Non-Functional, Constraint, or Assumption
   - Confidence level: Confirmed, Likely, or Uncertain

Reference: `references/interview-guide.md`

#### Technique B: JAD Workshop

1. Define workshop scope and objectives from `features.md`
2. Identify participants from the stakeholder register (minimum: one sponsor, two users, one developer)
3. Structure the workshop agenda:
   - Opening: scope confirmation, ground rules
   - Discovery: facilitated discussion of features and workflows
   - Consensus: prioritization and conflict resolution
   - Closure: action items and next steps
4. Record consensus decisions, dissenting views, and open items

Reference: `references/jad-workshop.md`

#### Technique C: Prototyping

1. Identify features from `features.md` that benefit from visual exploration
2. Describe low-fidelity prototype elements (screens, workflows, data layouts)
3. Define feedback questions for each prototype element
4. Record stakeholder reactions, suggested changes, and confirmed requirements

Reference: `references/prototyping-for-elicitation.md`

#### Technique D: Observation

1. Identify processes or workflows relevant to the project scope
2. Define observation targets: tasks, sequences, decision points, pain points
3. Document observed workflows with:
   - Step-by-step task descriptions
   - Time estimates per task
   - Error-prone steps
   - Workarounds currently in use
4. Derive requirements from observed gaps and inefficiencies

Reference: `references/observation-ethnography.md`

#### Technique E: Questionnaire

1. Design the questionnaire with question types matched to information needs:
   - Multiple choice for categorical data
   - Likert scale (1-5) for satisfaction and priority ratings
   - Open-ended for qualitative insights
2. Target distribution to stakeholder groups from the register
3. Define minimum response thresholds for statistical validity
4. Summarize responses with aggregated metrics and notable outliers

Reference: `references/questionnaires-surveys.md`

### Step 5: Apply Domain-Specific Checklists

If the project domain matches one of the following, apply the corresponding checklist to ensure domain-critical requirements are not missed:

| Domain | Checklist Focus | Key Concerns |
|--------|----------------|--------------|
| **Healthcare** | HIPAA compliance, HL7/FHIR integration, patient data handling | Privacy, audit trails, interoperability |
| **SaaS** | Multi-tenancy, subscription billing, API rate limiting | Tenant isolation, usage metering, SLA |
| **POS** | Payment processing, inventory sync, offline mode | PCI-DSS, real-time updates, hardware integration |
| **GIS** | Spatial data handling, coordinate systems, map rendering | Projection accuracy, data volume, tile caching |

For each checklist item, record whether the item was addressed (Yes/No/Partial) and the source of the finding.

Reference: `references/domain-checklists.md`

### Step 6: Write Elicitation Log

Assemble all findings and write to `../output/elicitation_log.md`. Log the total finding count, technique(s) used, and the number of unresolved items.

## Output Format Specification

The generated `elicitation_log.md` shall follow this structure:

```
# Elicitation Log: [Project Name]

## Document Header
- Project: [Name]
- Version: 1.0
- Date: [Current Date]
- Technique(s) Used: [Interview / JAD / Prototyping / Observation / Questionnaire]
- Status: Draft

## 1. Elicitation Context
### 1.1 Stakeholder Availability Assessment
### 1.2 Domain Complexity Assessment
### 1.3 Requirements Maturity Assessment
### 1.4 Technique Selection Rationale

## 2. Elicitation Findings
### 2.1 Functional Requirements
### 2.2 Non-Functional Requirements
### 2.3 Constraints
### 2.4 Assumptions

## 3. Source Attribution Matrix

## 4. Domain Checklist Results (if applicable)

## 5. Open Items and Unresolved Questions

## 6. Confidence Summary

## 7. Standards Traceability

## Appendix A: Raw Interview/Workshop Notes
## Appendix B: Revision History
```

Each finding in Section 2 shall use this format:

```
#### EL-XXX: [Finding Title]

- **Type**: Functional | Non-Functional | Constraint | Assumption
- **Source**: [Stakeholder ID] -- [Role]
- **Technique**: [Interview | JAD | Prototyping | Observation | Questionnaire]
- **Statement**: "[Verbatim or paraphrased stakeholder statement]"
- **Derived Requirement**: The system shall [requirement statement].
- **Confidence**: Confirmed | Likely | Uncertain
- **Priority**: Critical | High | Medium | Low
- **Notes**: [Additional context or dependencies]
```

## Common Pitfalls

- Selecting a single technique without considering stakeholder availability, leading to low participation and incomplete findings
- Recording findings without source attribution, making downstream validation impossible
- Skipping domain-specific checklists, resulting in missed regulatory or integration requirements
- Treating elicitation as a one-pass activity rather than iterating when confidence levels are low
- Using leading questions that bias stakeholder responses toward a predetermined solution
- Failing to distinguish between requirements, constraints, and assumptions in the log

## Verification Checklist

- [ ] All required input files were read and logged
- [ ] Elicitation context was assessed across all three dimensions
- [ ] Technique selection rationale is documented and grounded in context assessment
- [ ] Every finding has a source stakeholder ID, technique, and confidence level
- [ ] Findings are classified by type (Functional, Non-Functional, Constraint, Assumption)
- [ ] Domain-specific checklists were applied if the domain matches a supported category
- [ ] Open items and unresolved questions are explicitly listed
- [ ] No requirement statement uses subjective language without a defined metric
- [ ] Standards Traceability section maps to IEEE 29148 Section 6.3

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `01-stakeholder-analysis` | Consumes stakeholder register |
| Downstream | `03-brd-generation` | Feeds elicitation findings for BRD generation |
| Downstream | `02-requirements-engineering/waterfall/05-feature-decomposition` | Feeds functional requirements |
| Downstream | `02-requirements-engineering/agile/01-user-story-generation` | Feeds user-facing requirements |

## Standards Compliance

| Standard | Governs |
|----------|---------|
| IEEE 29148-2018 Section 6.3 | Requirements elicitation process and techniques |
| Laplante Ch.4 | Elicitation technique selection and execution |
| Wiegers Practice 4 | Interview and workshop facilitation |
| Wiegers Practice 5 | Observation and contextual inquiry |
| Wiegers Practice 6 | Survey and questionnaire design |
| IEEE Std 610.12-1990 | Terminology definitions |

## Resources

- `references/interview-guide.md` -- Structured interview protocol
- `references/jad-workshop.md` -- JAD workshop facilitation guide
- `references/prototyping-for-elicitation.md` -- Low-fi prototyping workflow
- `references/observation-ethnography.md` -- Contextual inquiry checklist
- `references/questionnaires-surveys.md` -- Survey design templates
- `references/domain-checklists.md` -- Domain-specific elicitation checklists
