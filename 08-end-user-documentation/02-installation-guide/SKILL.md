---
name: 02-installation-guide
description: Use when documenting verified prerequisites, installation, configuration, validation, upgrade, and uninstall procedures. Use user-manual for post-install operation and release-notes for version-specific migration changes.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Installation Guide Skill

<!-- dual-compat-start -->

## Use When

- Use when documenting verified prerequisites, installation, configuration, validation, upgrade, and uninstall procedures. Use user-manual for post-install operation and release-notes for version-specific migration changes.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Signed release artefact and checksum; supported environment matrix; dependency versions; configuration schema; install, upgrade, rollback, and uninstall procedures | Release engineering and platform owners | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A command or procedure was not tested on the stated environment | Label it unverified and stop release | Destructive or unusable setup guidance |
| Verification fails | Run documented recovery or rollback before continuing | Partially installed systems |

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
| Installation Guide | Customer, support, success, sales, or implementation owner | A new operator can complete and verify installation on every stated environment and recover cleanly from each documented failure. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Installation Guide evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Installation Guide from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a command or procedure was not tested on the stated environment, label it unverified and stop release. Record the evidence and result in the validation record; this avoids destructive or unusable setup guidance.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

This is the second skill in Phase 08 (End-User Documentation). It produces a comprehensive installation guide that walks end users and system administrators through prerequisites, system requirements, step-by-step installation procedures, post-installation configuration, and verification. The output conforms to ISO 26514 (User Documentation) and serves as the authoritative installation reference for deploying the software in end-user environments.

## When to Use This Skill

- After `tech_stack.md` exists in `projects/<ProjectName>/_context/` with technology choices, runtime versions, and platform requirements.
- When end users or system administrators require clear installation instructions.
- Optionally after Phase 06 when `Deployment_Guide.md` exists in `projects/<ProjectName>/<phase>/<document>/` for infrastructure and deployment context.

## Quick Reference

| Attribute    | Value |
|--------------|-------|
| **Inputs**   | `projects/<ProjectName>/_context/tech_stack.md`, `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md` (optional) |
| **Output**   | `projects/<ProjectName>/<phase>/<document>/Installation_Guide.md` |
| **Tone**     | Procedural, precise, user-facing |
| **Standard** | ISO 26514 |
| **Time**     | 10-20 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | Yes | Technology choices, runtime versions, OS compatibility, dependencies |
| Deployment_Guide.md | `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md` | No | Infrastructure context, environment configuration, deployment procedures |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Installation_Guide.md | `projects/<ProjectName>/<phase>/<document>/Installation_Guide.md` | Complete installation guide with system requirements, prerequisites, steps, configuration, verification, and troubleshooting |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `tech_stack.md` from `projects/<ProjectName>/_context/`. Optionally read `Deployment_Guide.md` from `projects/<ProjectName>/<phase>/<document>/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Define System Requirements

Document minimum and recommended system requirements:
- Operating system versions with architecture (e.g., Windows 10 x64, Ubuntu 22.04 LTS)
- Hardware minimums (CPU, RAM, disk space) and recommended specifications
- Network requirements (ports, bandwidth, firewall rules)
- Browser requirements if the product is web-based (name, minimum version)

### Step 3: Define Prerequisites

List all software and configuration prerequisites:
- Runtime environments and versions (e.g., Node.js 18+, Python 3.10+, .NET 8)
- Package managers and build tools required
- Database servers or external services that must be running
- Required user permissions or access levels (admin, root, standard)
- Environment variables or credentials that must be prepared in advance

### Step 4: Generate Installation Steps

Produce numbered installation steps with exact commands where applicable:
- Download or acquisition instructions (URL, package registry, repository clone)
- Dependency installation commands per platform
- Application installation commands with expected console output
- Each step SHALL include the exact command, expected output, and estimated time
- Platform-specific variations SHALL be called out with conditional blocks

### Step 5: Define Configuration

Document post-installation configuration:
- Configuration file locations and format
- Required configuration parameters with descriptions and example values
- Optional configuration parameters with defaults
- Environment-specific configuration differences (development vs. production)

### Step 6: Define Post-Installation Verification

Provide verification procedures to confirm successful installation:
- Version check commands with expected output
- Health check or status endpoints
- A minimal functional test (e.g., run the application and confirm the landing page loads)
- Log file locations for diagnosing installation failures

### Step 7: Define Upgrading and Uninstallation

Document upgrade and removal procedures:
- Upgrade procedure with data backup steps and migration notes
- Uninstallation steps that cleanly remove the product
- Data preservation guidance during uninstallation

### Step 8: Generate Common Issues Section and Write Output

Document frequent installation problems and solutions:
- Permission errors and resolution (elevation, ownership changes)
- Port conflicts and resolution (identifying and freeing ports)
- Dependency version mismatches and resolution
- Platform-specific known issues
- Write the completed document to `projects/<ProjectName>/<phase>/<document>/Installation_Guide.md`. Log the total count of installation steps.

## Output Format Specification

The generated `Installation_Guide.md` SHALL contain these sections in order:

1. **Document Header** -- Product name, version, date, audience, standards reference
2. **System Requirements** -- Minimum and recommended hardware, OS, network
3. **Prerequisites** -- Software dependencies and pre-configuration
4. **Installation Steps** -- Numbered procedures with exact commands
5. **Configuration** -- Post-install configuration parameters and files
6. **Post-Installation Verification** -- Checks confirming successful installation
7. **Upgrading** -- Upgrade procedures and migration notes
8. **Uninstallation** -- Clean removal procedures
9. **Common Issues & Solutions** -- Error catalog with resolutions

## Common Pitfalls

- **Platform-agnostic commands:** Installation commands SHALL specify the target platform when commands differ across operating systems.
- **Missing version pinning:** Every dependency SHALL specify a minimum version number.
- **No verification step:** Every installation guide SHALL include a verification procedure that confirms the product is operational.
- **Assumed prerequisites:** The guide SHALL NOT assume any prerequisite is already installed; every dependency SHALL be listed explicitly.
- **Missing uninstallation:** Every guide SHALL include clean removal instructions.

## Verification Checklist

1. `Installation_Guide.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all nine sections populated.
2. System requirements specify minimum OS, hardware, and network requirements.
3. Prerequisites list every runtime, package manager, and external service with version numbers.
4. Installation steps are numbered with exact commands and expected output.
5. Configuration section documents all required and optional parameters.
6. Post-installation verification includes at least one functional test.
7. Upgrading section includes data backup guidance.
8. Common issues section addresses permission errors and dependency conflicts.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 06 (01-deployment-guide) | Consumes `Deployment_Guide.md` for infrastructure and environment context |
| Upstream | Project Context | Consumes `tech_stack.md` for technology and platform requirements |
| Downstream | 03-faq | FAQ generation references installation guide for setup questions |
| Downstream | 01-user-manual | User manual references installation guide for onboarding |

## Standards Compliance

- **ISO 26514** -- Systems and Software Engineering -- Requirements for Designers and Developers of User Documentation. Governs installation procedure structure, completeness, and audience-appropriateness.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step installation guide generation logic.
- `README.md` -- Quick-start guide for this skill.
