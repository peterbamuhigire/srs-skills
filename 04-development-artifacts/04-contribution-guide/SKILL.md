---
name: "contribution-guide"
description: "Generate a contribution guide with branching strategy, PR process, commit conventions, review checklist, and code of conduct per IEEE 1074."
metadata:
  use_when: "Use when the task matches contribution guide skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Contribution Guide Skill

## Overview

This is the fourth skill in Phase 04 (Development Artifacts). It generates a contribution guide that establishes the team's branching strategy, commit message conventions, pull request process, code review checklist, and CI/CD expectations. The output standardizes the development workflow so that every contribution follows a predictable, auditable process conforming to IEEE 1074 (Software Life Cycle Processes).

## When to Use

- After `tech_stack.md` exists in `../project_context/` with VCS and CI/CD tooling details.
- After `02-coding-guidelines` and `03-dev-environment-setup` have completed, since the contribution guide references coding standards and environment setup.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../project_context/tech_stack.md` |
| **Output**  | `../output/Contribution_Guide.md` |
| **Tone**    | Prescriptive, process-oriented, team-facing |
| **Standard** | IEEE 1074 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| tech_stack.md | `../project_context/tech_stack.md` | Yes | VCS platform, CI/CD tooling, deployment targets |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Contribution_Guide.md | `../output/Contribution_Guide.md` | Complete contribution workflow guide with branching, commits, PRs, and review standards |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `tech_stack.md` from `../project_context/`. Log the absolute path of each file read. If `tech_stack.md` is missing, halt execution and report the gap. Identify the VCS platform (GitHub, GitLab, Bitbucket), CI/CD tooling, and deployment targets.

### Step 2: Define Branching Strategy

Define the branching model based on the project's scale and deployment strategy:
- **Strategy selection**: GitFlow, trunk-based, or feature-branch with rationale
- **Branch naming conventions**: prefixes (feature/, bugfix/, hotfix/, release/) with examples
- **Protected branches**: main/master and develop with merge restrictions
- **Branch lifecycle**: creation, updates via rebase or merge, deletion after merge

### Step 3: Define Commit Message Conventions

Establish commit message standards using Conventional Commits format:
- **Format**: `type(scope): description` (e.g., `feat(auth): add JWT token refresh`)
- **Allowed types**: feat, fix, docs, style, refactor, test, chore, perf, ci, build
- **Scope rules**: module or component name from the project structure
- **Body and footer**: when to include breaking change notes and issue references

### Step 4: Define Pull Request Process

Document the complete PR lifecycle:
- **PR template**: title format, description sections (Summary, Changes, Testing, Screenshots)
- **Review requirements**: minimum reviewer count, required approvals, CODEOWNERS rules
- **Merge strategy**: squash-and-merge, rebase-and-merge, or merge commit with rationale
- **Size guidelines**: maximum lines changed per PR with escalation path for large changes

### Step 5: Define Code Review Checklist

Produce a structured checklist for code reviewers:
- Functional correctness: does the code implement the stated requirement
- Naming and style compliance: does the code follow the Coding Guidelines
- Error handling: are edge cases and failure paths handled
- Security: are inputs validated, secrets externalized, and injection risks mitigated
- Test coverage: are new or modified functions covered by tests
- Documentation: are public interfaces documented with parameter descriptions

### Step 6: Define CI/CD Pipeline Expectations

Document what the CI/CD pipeline shall enforce:
- Automated checks that must pass before merge (lint, type-check, unit tests, build)
- Code coverage thresholds with specific percentage targets
- Security scanning requirements (dependency audit, SAST)
- Deployment stages (staging, production) and approval gates

### Step 7: Write Output

Write the completed document to `../output/Contribution_Guide.md`. Include a Getting Started section that references `Dev_Environment_Setup.md` for initial setup and `Coding_Guidelines.md` for code standards. Include an Issue Reporting section with templates for bug reports and feature requests. Log the total count of process rules defined.

## Output Format

The generated `Contribution_Guide.md` shall contain these sections in order: Document Header (project name, date, version, standard), 1. Getting Started, 2. Branching Strategy, 3. Commit Conventions, 4. Pull Request Process, 5. Code Review Checklist, 6. CI/CD Pipeline, 7. Issue Reporting.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Branching strategy without naming conventions | Every branch type shall have a naming pattern with examples |
| Commit conventions without concrete examples | Every commit type shall include a real-world example message |
| PR process without size guidelines | Define maximum PR size to prevent unreviewable changes |
| CI/CD expectations without specific thresholds | Coverage and quality thresholds shall use specific percentages |

## Verification Checklist

- [ ] `Contribution_Guide.md` exists in `../output/` with all seven sections populated.
- [ ] Branching strategy defines branch naming conventions with examples.
- [ ] Commit conventions follow Conventional Commits format with allowed types and scope rules.
- [ ] PR process defines template, review requirements, and merge strategy.
- [ ] Code review checklist covers correctness, style, error handling, security, and testing.
- [ ] CI/CD expectations define specific coverage thresholds and automated checks.
- [ ] Getting Started section references Dev_Environment_Setup.md and Coding_Guidelines.md.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 02-coding-guidelines | References coding standards for review checklist items |
| Upstream | 03-dev-environment-setup | References environment setup in Getting Started section |
| Upstream | `../project_context/tech_stack.md` | Reads VCS and CI/CD tooling details |
| Downstream | Development teams | Primary workflow reference for all contributors |

## Standards

- **IEEE 1074** -- Software Life Cycle Processes. Governs the documentation of development workflows, process definitions, and lifecycle management.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step contribution guide generation logic.
- `README.md` -- Quick-start guide for this skill.
