---
name: coding-guidelines
description: Generate language-specific coding standards with naming conventions, patterns, anti-patterns, and code quality metrics per IEEE 730.
---

# Coding Guidelines Skill

## Overview

This is the second skill in Phase 04 (Development Artifacts). It generates language-specific coding standards that establish naming conventions, code structure patterns, anti-patterns to avoid, error handling conventions, and code quality metrics. The output ensures consistent, maintainable code across the development team and conforms to IEEE 730 (Software Quality Assurance Plans).

## When to Use

- After `tech_stack.md` exists in `../project_context/` with language and framework details.
- Optionally after `HLD.md` exists in `../output/` to align coding patterns with architectural decisions.
- Can run in parallel with `03-dev-environment-setup` since they address independent concerns.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../project_context/tech_stack.md`; optionally `../output/HLD.md` |
| **Output**  | `../output/Coding_Guidelines.md` |
| **Tone**    | Prescriptive, example-driven, enforceable |
| **Standard** | IEEE 730 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| tech_stack.md | `../project_context/tech_stack.md` | Yes | Languages, frameworks, and tooling to derive conventions from |
| HLD.md | `../output/HLD.md` | No | Architectural patterns to align coding conventions with |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Coding_Guidelines.md | `../output/Coding_Guidelines.md` | Complete coding standards document with conventions, patterns, and quality metrics |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `tech_stack.md` from `../project_context/`. Optionally read `HLD.md` from `../output/`. Log the absolute path of each file read. If `tech_stack.md` is missing, halt execution and report the gap.

### Step 2: Define Naming Conventions

For each language and framework detected in `tech_stack.md`, define naming conventions:
- **Files**: naming pattern, casing (kebab-case, PascalCase, snake_case), suffix rules
- **Classes/Components**: casing, prefix/suffix conventions (e.g., `Service`, `Controller`, `Repository`)
- **Functions/Methods**: casing, verb-first naming (e.g., `getUser`, `calculateTotal`)
- **Variables**: casing, descriptive naming rules, abbreviation policy
- **Database Columns**: casing (snake_case), naming patterns for foreign keys, timestamps, and flags
- **Constants**: UPPER_SNAKE_CASE with grouping conventions

### Step 3: Define Code Structure Patterns

Define the project directory layout and module organization:
- Top-level directory structure with purpose annotations
- Module boundary rules (what belongs in each layer)
- File length and function length guidelines with specific thresholds
- Import ordering conventions

### Step 4: Define Anti-Patterns to Avoid

Document specific anti-patterns with explanations:
- Code smells to reject in code review (e.g., God classes, deep nesting, magic numbers)
- Framework-specific anti-patterns (e.g., direct DOM manipulation in React, N+1 queries in ORMs)
- Security anti-patterns (e.g., string concatenation for SQL, hardcoded credentials)

### Step 5: Define Error Handling Conventions

Establish error handling standards:
- Exception hierarchy aligned with the LLD error handling design
- Try-catch scope rules (narrow catches, no empty catch blocks)
- Error message format standards (structured, loggable, user-safe)
- Async error handling patterns (Promise rejection, callback error-first)

### Step 6: Define Logging and Debugging Standards

Establish logging conventions:
- Log levels (DEBUG, INFO, WARN, ERROR, FATAL) with usage criteria
- Structured log format (JSON with timestamp, level, correlation ID, message)
- Sensitive data redaction rules (mask PII, credentials, tokens)
- Debug tooling recommendations aligned with tech stack

### Step 7: Write Output

Write the completed document to `../output/Coding_Guidelines.md`. The document shall include a Code Review Checklist section that summarizes all conventions as a reviewable checklist. Log the total count of conventions defined.

## Output Format

The generated `Coding_Guidelines.md` shall contain these sections in order: Document Header (project name, date, version, standard), 1. Naming Conventions, 2. Code Structure, 3. Design Patterns to Use, 4. Anti-Patterns to Avoid, 5. Error Handling, 6. Logging, 7. Security Practices, 8. Code Review Checklist.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Generic conventions not tied to tech stack | Every convention shall reference the specific language or framework it applies to |
| No concrete examples | Every naming convention shall include a compliant and non-compliant example |
| Anti-patterns without alternatives | Every anti-pattern shall include the recommended alternative approach |
| Missing security practices | Security conventions shall address injection prevention, authentication handling, and data sanitization |

## Verification Checklist

- [ ] `Coding_Guidelines.md` exists in `../output/` with all eight sections populated.
- [ ] Naming conventions cover files, classes, functions, variables, database columns, and constants.
- [ ] Anti-patterns include framework-specific items derived from `tech_stack.md`.
- [ ] Error handling conventions define an exception hierarchy and message format.
- [ ] Logging standards define structured format with redaction rules for sensitive data.
- [ ] Code Review Checklist summarizes all conventions as reviewable items.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `../project_context/tech_stack.md` | Reads language and framework details |
| Parallel | 03-dev-environment-setup | Independent concern; can run simultaneously |
| Downstream | 04-contribution-guide | Informs code review checklist and PR standards |
| Downstream | Phase 05 (Testing) | Informs test naming and test structure conventions |

## Standards

- **IEEE 730** -- Software Quality Assurance Plans. Governs the definition of coding standards and quality practices.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step coding guidelines generation logic.
- `README.md` -- Quick-start guide for this skill.
