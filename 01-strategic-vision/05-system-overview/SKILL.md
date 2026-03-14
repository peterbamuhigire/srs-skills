---
name: system-overview
phase: "01-strategic-vision"
description: Generate a system overview document understandable by every project stakeholder — required by Royce Step 1
standard: IEEE 29148-2018 (Requirements Engineering), Royce (1970) Step 1
---

# Skill: System Overview Document

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
- Where does this system fit in the organisation's landscape?
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
