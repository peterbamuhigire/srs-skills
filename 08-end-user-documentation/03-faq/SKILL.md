---
name: 03-faq
description: Use when converting recurring, evidence-backed user questions into concise searchable answers with documentation links. Use user-manual for complete procedures and installation-guide for setup sequences.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# FAQ Skill

<!-- dual-compat-start -->

## Use When

- Use when converting recurring, evidence-backed user questions into concise searchable answers with documentation links. Use user-manual for complete procedures and installation-guide for setup sequences.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Support tickets and recurring-question evidence; search logs where available; current manuals; approved product behaviour; escalation policy | Support, product, and documentation owners | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A feature, screen, or answer is not confirmed in the product or approved source | Omit or mark it pending verification | Documenting nonexistent behaviour |
| A procedure lacks a success or recovery state | Add both before publication | Users stranded after errors |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| FAQ | Customer, support, success, sales, or implementation owner | Every answer resolves a real recurring question, links to the authoritative procedure, states applicable roles or versions, and names escalation when unresolved. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| FAQ evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing FAQ from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a feature, screen, or answer is not confirmed in the product or approved source, omit or mark it pending verification. Record the evidence and result in the validation record; this avoids documenting nonexistent behaviour.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

This is the third skill in Phase 08 (End-User Documentation). It produces a structured Frequently Asked Questions document organized by category with clear question-answer pairs, cross-references to the user manual and installation guide, and search-friendly formatting. The output conforms to ISO 26514 (User Documentation) and serves as a quick-reference resource that reduces support burden by addressing common user inquiries proactively.

## When to Use This Skill

- After `vision.md` and `features.md` exist in `projects/<ProjectName>/_context/` to derive questions from product scope and feature set.
- Optionally after `User_Manual.md` exists in `projects/<ProjectName>/<phase>/<document>/` for cross-referencing detailed procedures.
- When the project requires a self-service knowledge base for end users.

## Quick Reference

| Attribute    | Value |
|--------------|-------|
| **Inputs**   | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/<phase>/<document>/User_Manual.md` (optional) |
| **Output**   | `projects/<ProjectName>/<phase>/<document>/FAQ.md` |
| **Tone**     | Conversational yet precise, user-facing |
| **Standard** | ISO 26514 |
| **Time**     | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `projects/<ProjectName>/_context/vision.md` | Yes | Product purpose, target audience, positioning for general questions |
| features.md | `projects/<ProjectName>/_context/features.md` | Yes | Feature list for feature-specific question generation |
| User_Manual.md | `projects/<ProjectName>/<phase>/<document>/User_Manual.md` | No | Detailed procedures for cross-reference links in answers |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| FAQ.md | `projects/<ProjectName>/<phase>/<document>/FAQ.md` | Structured FAQ organized by category with question-answer pairs and cross-references |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` and `features.md` from `projects/<ProjectName>/_context/`. Optionally read `User_Manual.md` from `projects/<ProjectName>/<phase>/<document>/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Generate General Questions

Produce questions and answers about the product overall:
- What is the product and what problem does it solve?
- Who is the target audience?
- What are the key benefits compared to alternatives?
- What are the system requirements?
- How do users get started?

### Step 3: Generate Installation & Setup Questions

Produce questions and answers about installation and initial configuration:
- How do I install the product?
- What prerequisites are needed?
- How do I configure the product after installation?
- How do I verify the installation was successful?
- Cross-reference `Installation_Guide.md` if available

### Step 4: Generate Feature-Specific Questions

For each feature in `features.md`, produce at least two questions:
- How do I use [feature name]?
- What are the limitations of [feature name]?
- Additional questions based on feature complexity and common misunderstandings
- Every answer SHALL cross-reference the corresponding User Manual section if available

### Step 5: Generate Account & Access Questions

Produce questions about user accounts and access control:
- How do I create an account or log in?
- How do I reset my password?
- What permissions or roles are available?
- How do I manage user access?
- If the product has no user accounts, state that this category is not applicable

### Step 6: Generate Troubleshooting Questions

Produce questions about common problems and solutions:
- What do I do if the product will not start?
- How do I resolve common error messages?
- Where do I find logs for diagnosing issues?
- How do I contact support for unresolved problems?

### Step 7: Generate Data & Security Questions

Produce questions about data handling and security:
- How is my data stored and protected?
- Can I export or import my data?
- What is the backup and recovery process?
- What compliance standards does the product meet?

### Step 8: Assemble and Write Output

Assemble all categories into the final document with a table of contents and search-friendly anchor links. Every answer SHALL be concise (three to five sentences maximum) with a cross-reference link to detailed documentation where applicable. Write the completed document to `projects/<ProjectName>/<phase>/<document>/FAQ.md`. Log the total count of question-answer pairs generated.

## Output Format Specification

The generated `FAQ.md` SHALL contain these sections in order:

1. **Document Header** -- Product name, version, date, standards reference
2. **Table of Contents** -- Category links for quick navigation
3. **General Questions** -- Product overview and getting started
4. **Installation & Setup** -- Installation, prerequisites, configuration
5. **Feature-Specific Questions** -- Per-feature usage questions
6. **Account & Access** -- User accounts, permissions, roles
7. **Troubleshooting** -- Common problems and solutions
8. **Billing & Licensing** -- Licensing model, pricing (if applicable; omit if not)
9. **Data & Security** -- Data handling, privacy, compliance

## Common Pitfalls

- **Vague answers:** Every answer SHALL provide a concrete action or fact, not a generic statement.
- **Missing cross-references:** Answers that describe procedures SHALL link to the relevant User Manual or Installation Guide section.
- **Monolithic answers:** Answers exceeding five sentences SHALL be split or redirected to detailed documentation.
- **Missing categories:** Every category SHALL contain at least two question-answer pairs.
- **Fabricated questions:** Questions SHALL be derived from actual product features and documented scope, not invented.

## Verification Checklist

1. `FAQ.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all applicable categories populated.
2. General Questions section addresses product purpose, audience, and getting started.
3. Every feature in `features.md` has at least two corresponding FAQ entries.
4. Answers are concise (three to five sentences maximum) with cross-reference links.
5. Troubleshooting section addresses common errors and support escalation.
6. Table of contents links match actual section headings.
7. No category contains fewer than two question-answer pairs.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 02 (Requirements Engineering) | Consumes `vision.md` and `features.md` for question derivation |
| Upstream | 01-user-manual | Consumes `User_Manual.md` for cross-reference links |
| Upstream | 02-installation-guide | References installation procedures for setup questions |
| Downstream | Phase 09 (Compliance) | FAQ feeds compliance documentation for user-facing claims |

## Standards Compliance

- **ISO 26514** -- Systems and Software Engineering -- Requirements for Designers and Developers of User Documentation. Governs FAQ structure, completeness, and audience-appropriateness.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step FAQ generation logic.
- `README.md` -- Quick-start guide for this skill.
