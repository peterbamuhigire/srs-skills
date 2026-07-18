---
name: 05-system-overview
description: Use when every stakeholder needs a plain-language, current view of system purpose, context, major functions, constraints and actors; use vision-statement for strategic intent, PRD generation for product requirements, and high-level-design for technical architecture.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# Skill: System Overview Document
<!-- dual-compat-start -->
## Use When

- A mixed technical and non-technical audience needs a shared system orientation document.

## Do Not Use When

- Do not use for detailed requirements, component design or a marketing overview.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Approved vision and scope | Phase 01 decisions | Required | Stop if system boundary or purpose is disputed. |
| Known actors, external systems and constraints | Project context and subject-matter owners | Required | Show unknown interfaces as open issues, not facts. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the System Overview through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the System Overview to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| System Overview | All project participants and onboarding readers | A new team member can explain purpose, boundary, actors, major functions and constraints, and every named interface is sourced or qualified. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified System Overview draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Audience includes non-technical readers | Use plain language and a context view | Overview remains accessible |
| Detail is needed to implement a component | Route to HLD or LLD | Overview becomes an unmaintainable design dump |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Copying the vision statement verbatim. Fix: explain the operating system boundary and functions.
- Using unexplained acronyms. Fix: expand them or add a glossary.
- Showing components before actors and context. Fix: lead with the system boundary.
- Inventing an integration endpoint. Fix: label the external dependency and verification owner.
- Letting the overview drift after scope change. Fix: version it with the approved scope baseline.

## References

- [Vision Statement neighbour](../03-vision-statement/SKILL.md)
- [High-Level Design neighbour](../../03-design-documentation/01-high-level-design/SKILL.md)
<!-- dual-compat-end -->




## Source
Royce, W.W. (1970). Managing the Development of Large Software Systems. IEEE WESCON, p.331. Step 1, requirement 3: "Write an overview document that is understandable, informative and current. Each and every worker must have an elemental understanding of the system. At least one person must have a deep understanding of the system which comes partially from having had to write an overview document."

## Purpose
Produce a plain-language system overview that every stakeholder — technical and non-technical — can read and understand. This is distinct from the SRS (too detailed), the HLD (too technical), and the Vision Statement (too high-level). It is the "one document that explains the whole thing."

## Trigger
User says: "generate system overview", "write overview document", "system description document"

## Required Inputs
- `_context/vision.md` — problem statement and goals
- `_context/features.md` — feature list
- `_context/tech_stack.md` — technology context
- `_context/stakeholders.md` — audience list

## Output
Generate to: `projects/<ProjectName>/01-strategic-vision/05-system-overview/`

Files:
- `01-purpose-and-scope.md`
- `02-system-context.md`
- `03-major-functions.md`
- `04-constraints-and-assumptions.md`
- `05-stakeholder-summary.md`

Final document: `projects/<ProjectName>/01-strategic-vision/SystemOverview.docx`

## Document Structure

### Section 1: Purpose and Scope (plain language)
- What problem does this system solve?
- Who uses it?
- What does it NOT do?
- Written at a level a non-technical executive can understand

### Section 2: System Context
- Where does this system fit in the organisation's operating environment?
- What systems does it interact with?
- Simple context diagram (Mermaid)

### Section 3: Major Functions
- List each major function in one paragraph of plain language
- No technical jargon
- Describe the OUTCOME not the implementation

### Section 4: Constraints and Assumptions
- Technical constraints (platform, integration, performance)
- Business constraints (budget, timeline, regulatory)
- Key assumptions being made

### Section 5: Stakeholder Summary
- Who does what with the system
- Plain language — no role codes or technical identifiers

## Quality Standard
The overview document passes quality review when:
- A non-technical business stakeholder can read it and accurately describe what the system does
- A new developer joining the project can understand the system's purpose and scope within 15 minutes
- Every major function in `_context/features.md` is represented
- Royce's test: "Each and every worker must have an elemental understanding of the system"
