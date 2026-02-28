---
name: acceptance-criteria
description: Formalize Gherkin-format acceptance criteria (Given-When-Then) for each user story, ensuring deterministic pass/fail testability per IEEE 29148 Sec 6.4.5.
---

# Acceptance Criteria Skill Guidance

## Overview

Run this skill after user stories are generated. It transforms each user story produced by `01-user-story-generation` into formal acceptance criteria using the Gherkin (Given-When-Then) format. Every criterion shall be deterministic and independently verifiable, ensuring that test engineers can derive binary pass/fail outcomes without ambiguity. The skill enforces IEEE 29148-2018 Section 6.4.5 traceability between stakeholder intent and testable conditions.

## When to Use

Execute this skill after `01-user-story-generation` has produced `../output/user_stories.md`. Each user story in that file shall already follow the "As a / I want / So that" format. This skill shall not run until the upstream file exists and contains at least one valid story identifier (US-XXX).

## Quick Reference

- **Inputs:** `../output/user_stories.md` (required), `../project_context/quality_standards.md` (optional, for NFR criteria)
- **Output:** `../output/acceptance_criteria.md`
- **Tone:** Precise, testable, deterministic -- no subjective adjectives

## Input Files

| File | Source | Purpose | Required? |
|------|--------|---------|-----------|
| `user_stories.md` | `../output/` | User stories with "As a / I want / So that" triads | Yes |
| `quality_standards.md` | `../project_context/` | NFR targets for performance, security, and reliability thresholds | No |

## Output Files

| File | Destination | Contents |
|------|-------------|----------|
| `acceptance_criteria.md` | `../output/` | Gherkin-format acceptance criteria cross-referenced to story IDs |

## Core Instructions

1. **Read upstream output.** Open `../output/user_stories.md` and log the file path to confirm the read succeeded.
2. **Extract story triads.** For each user story identified by US-XXX, parse the "As a [role]", "I want to [action]", and "So that [value]" triad. Record the story ID, title, and epic association.
3. **Generate Gherkin criteria.** Produce 3--5 acceptance criteria per story using the format: `Given [precondition], When [action], Then [expected result]`. Criteria shall cover:
   - The happy-path scenario (normal successful flow)
   - At least one error or edge-case scenario
   - At least one boundary-condition scenario
4. **Append NFR criteria.** If `../project_context/quality_standards.md` exists, read it and append non-functional acceptance criteria with measurable thresholds (response time, throughput, encryption standard, etc.) to each relevant story.
5. **Flag untestable stories.** If a story cannot yield deterministic, binary pass/fail criteria, tag it with `[AC-FAIL]` and append a remediation note identifying the missing or ambiguous element.
6. **Write output.** Write `../output/acceptance_criteria.md` with each story's criteria grouped under its US-XXX identifier, including cross-references back to the originating story and epic.

## Output Format Specification

The generated `acceptance_criteria.md` shall follow this structure:

```markdown
# Acceptance Criteria: [Project Name]

**Generated:** [Date]
**Source:** user_stories.md
**Standard:** IEEE 29148-2018 Sec 6.4.5, Gherkin/BDD Format

---

## US-001: [Story Title]

**Epic:** [Epic Name]
**Story:** As a [role], I want to [action], So that [value]

### Functional Criteria

- [ ] **AC-001.1:** Given [precondition], When [action], Then [expected result]
- [ ] **AC-001.2:** Given [error condition], When [action], Then [error handling result]
- [ ] **AC-001.3:** Given [boundary condition], When [action], Then [boundary result]

### NFR Criteria (if applicable)

- [ ] **AC-001.NFR-1:** Given [load condition], When [action], Then [measurable threshold]

---

## US-002: [Story Title]

[... repeat per story ...]

---

## Summary

| Metric | Value |
|--------|-------|
| Stories Processed | N |
| Total Criteria Generated | N |
| NFR Criteria | N |
| Failures Flagged ([AC-FAIL]) | N |
```

## Common Pitfalls

- **Vague criteria:** Avoid language such as "the system handles it correctly." Each criterion shall state a concrete, observable outcome.
- **Missing negative cases:** Every story shall include at least one error-path criterion. Omitting negative cases leaves validation gaps.
- **Subjective language:** Words like "fast," "intuitive," or "user-friendly" violate IEEE 29148 verifiability. Replace with measurable thresholds.
- **Orphaned criteria:** Every criterion shall trace back to exactly one US-XXX identifier. Criteria without story references shall be flagged.

## Verification Checklist

Before finalizing the output:

- [ ] Every user story in `user_stories.md` has a corresponding criteria section in `acceptance_criteria.md`
- [ ] Each story has 3--5 acceptance criteria in Gherkin format
- [ ] At least one error/edge-case criterion exists per story
- [ ] At least one boundary-condition criterion exists per story
- [ ] All NFR criteria include measurable, numeric thresholds
- [ ] Stories that lack testable criteria are tagged with `[AC-FAIL]` and include remediation notes

## Integration

- **Upstream:** `01-user-story-generation` -- provides `user_stories.md`
- **Downstream:** `05-testing-documentation/` -- acceptance criteria become test cases; `03-story-mapping` -- maps criteria coverage across the backlog

## Standards Compliance

This skill implements:

- **IEEE Std 29148-2018** Section 6.4.5: Requirements specification and verifiability
- **Gherkin/BDD Format:** Given-When-Then structure for behavioral specifications
- **IEEE Std 610.12-1990:** Terminology alignment via project glossary

## Resources

- `logic.prompt` -- Direct AI execution instructions for this skill
- `README.md` -- Objective summary and quick-start guide

---

**Last Updated:** 2026-02-28
**Skill Version:** 1.0.0
