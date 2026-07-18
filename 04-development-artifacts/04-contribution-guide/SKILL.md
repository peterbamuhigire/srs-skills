---
name: 04-contribution-guide
description: Use when producing or updating repository contribution guide for branching, commits, pull requests, review gates, CI expectations, and exception handling. Use coding-guidelines for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Contribution Guide Skill

<!-- dual-compat-start -->
## Use When

- Produce or update repository contribution guide from approved project evidence.
- Resolve decisions about branching, commits, pull requests, review gates, CI expectations, and exception handling.
- Prepare a reviewable handoff for Contributors and maintainers.

## Do Not Use When

- The task is primarily owned by coding-guidelines; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Repository Contribution Guide | Contributors and maintainers | A contributor can open a conforming change and reviewers can determine acceptance from the documented gates. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Inspection is read-only by default. Create or edit the named project document only when explicitly authorised. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose contribution controls that match repository protection and CI and produce the full artefact. | A process guide that contradicts actual controls. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring coding-guidelines concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when a contributor can open a conforming change and reviewers can determine acceptance from the documented gates.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

This is the fourth skill in Phase 04 (Development Artifacts). It generates a contribution guide that establishes the team's branching strategy, commit message conventions, pull request process, code review checklist, and CI/CD expectations. The output standardizes the development workflow so that every contribution follows a predictable, auditable process conforming to IEEE 1074 (Software Life Cycle Processes).

## When to Use

- After `tech_stack.md` exists in `projects/<ProjectName>/_context/` with VCS and CI/CD tooling details.
- After `02-coding-guidelines` and `03-dev-environment-setup` have completed, since the contribution guide references coding standards and environment setup.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/_context/tech_stack.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Contribution_Guide.md` |
| **Tone**    | Prescriptive, process-oriented, team-facing |
| **Standard** | IEEE 1074 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | Yes | VCS platform, CI/CD tooling, deployment targets |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Contribution_Guide.md | `projects/<ProjectName>/<phase>/<document>/Contribution_Guide.md` | Complete contribution workflow guide with branching, commits, PRs, and review standards |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `tech_stack.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. If `tech_stack.md` is missing, halt execution and report the gap. Identify the VCS platform (GitHub, GitLab, Bitbucket), CI/CD tooling, and deployment targets.

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

Write the completed document to `projects/<ProjectName>/<phase>/<document>/Contribution_Guide.md`. Include a Getting Started section that references `Dev_Environment_Setup.md` for initial setup and `Coding_Guidelines.md` for code standards. Include an Issue Reporting section with templates for bug reports and feature requests. Log the total count of process rules defined.

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

- [ ] `Contribution_Guide.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all seven sections populated.
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
| Upstream | `projects/<ProjectName>/_context/tech_stack.md` | Reads VCS and CI/CD tooling details |
| Downstream | Development teams | Primary workflow reference for all contributors |

## Standards

- **IEEE 1074** -- Software Life Cycle Processes. Governs the documentation of development workflows, process definitions, and lifecycle management.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step contribution guide generation logic.
- `README.md` -- Quick-start guide for this skill.
