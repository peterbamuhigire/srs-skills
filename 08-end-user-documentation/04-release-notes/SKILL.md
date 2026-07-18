---
name: 04-release-notes
description: Use when communicating a verified version delta, including features, fixes, breaking changes, migration steps, compatibility, and known issues. Use user-manual for durable product operation and baseline-delta for controlled document changes.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Release Notes Skill

<!-- dual-compat-start -->

## Use When

- Use when communicating a verified version delta, including features, fixes, breaking changes, migration steps, compatibility, and known issues. Use user-manual for durable product operation and baseline-delta for controlled document changes.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Approved change log; issue and commit identifiers; test and deployment evidence; breaking-change assessment; migration and rollback instructions; known-issue register | Release manager, engineering, QA, and product owner | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A change cannot be traced to an approved source | Exclude it or label it unverified | Invented release claims |
| A breaking change lacks migration and rollback guidance | Block publication | Customer outage caused by incomplete notes |

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
| Release Notes | Customer, support, success, sales, or implementation owner | Every claim traces to an approved change; breaking changes include migration and rollback; known issues state impact, workaround, and owner. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Release Notes evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Release Notes from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as `adequate`, `secure`, or `user-friendly`.** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a change cannot be traced to an approved source, exclude it or label it unverified. Record the evidence and result in the validation record; this avoids invented release claims.

## References

- [Generation logic](logic.prompt): load when creating the complete artefact.
- [Skill notes](README.md): consult for local examples and invocation context.
- [Repository operating rules](../../AGENTS.md): apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Overview

This is the fourth skill in Phase 08 (End-User Documentation). It produces a release notes template that standardizes how version changes are communicated to end users, including release highlights, new features, improvements, bug fixes, breaking changes, migration instructions, and known issues. The output conforms to IEEE 830 and provides a reusable template that the development team can populate for each release cycle.

## When to Use This Skill

- After `vision.md` exists in `projects/<ProjectName>/_context/` to establish the product identity and versioning context.
- When the project requires a standardized format for communicating changes to end users.
- Optionally after `SRS_Draft.md` exists in `projects/<ProjectName>/<phase>/<document>/` for tracing features to requirements.

## Quick Reference

| Attribute    | Value |
|--------------|-------|
| **Inputs**   | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` (optional) |
| **Output**   | `projects/<ProjectName>/<phase>/<document>/Release_Notes_Template.md` |
| **Tone**     | Professional, concise, user-facing |
| **Standard** | IEEE 830 |
| **Time**     | 10-15 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| vision.md | `projects/<ProjectName>/_context/vision.md` | Yes | Product name, versioning scheme, release cadence context |
| SRS_Draft.md | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | No | Functional requirements for tracing features to specifications |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Release_Notes_Template.md | `projects/<ProjectName>/<phase>/<document>/Release_Notes_Template.md` | Reusable release notes template with all standard sections and placeholder guidance |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `vision.md` from `projects/<ProjectName>/_context/`. Optionally read `SRS_Draft.md` from `projects/<ProjectName>/<phase>/<document>/`. Log the absolute path of each file read. Halt if the required file is missing.

### Step 2: Define Version and Date Header

Produce a header template with:
- Product name and version number placeholder (e.g., `v[MAJOR].[MINOR].[PATCH]`)
- Release date placeholder
- Release type classification (Major, Minor, Patch, Hotfix)
- Semantic versioning guidance for the development team

### Step 3: Generate Release Highlights Section

Define a template section for release highlights:
- Two to three sentence executive summary of the release
- Guidance that highlights SHALL focus on user-facing impact, not implementation details
- Placeholder format for highlight bullet points

### Step 4: Generate New Features Section

Define a template section for new features:
- Per-feature entry format: feature name, description, user benefit, related requirement ID (if SRS exists)
- Screenshot or demo link placeholder per feature
- Guidance that each feature entry SHALL describe what the user can now do, not how it was implemented

### Step 5: Generate Improvements and Bug Fixes Sections

Define template sections for improvements and bug fixes:
- Improvement entry format: area of improvement, description of change, user impact
- Bug fix entry format: issue ID (if applicable), description of the bug, resolution, affected versions
- Guidance that bug fix descriptions SHALL describe the symptom the user experienced, not the code change

### Step 6: Generate Breaking Changes and Migration Guide Sections

Define template sections for breaking changes and migration:
- Breaking change entry format: what changed, why, migration action required
- Migration guide format: numbered steps to transition from previous version
- Guidance that every breaking change SHALL include a concrete migration action
- Deprecation notices with timeline for removal

### Step 7: Generate Known Issues and Compatibility Matrix

Define template sections for known issues and compatibility:
- Known issue entry format: description, severity, workaround (if available), expected fix version
- Compatibility matrix template: OS versions, browser versions, dependency versions tested
- Guidance that known issues SHALL include severity classification (Critical, High, Medium, Low)

### Step 8: Assemble Template and Write Output

Assemble all sections into the final template with authoring instructions embedded as comments. Include a checklist at the end for release managers to verify completeness before publishing. Write the completed template to `projects/<ProjectName>/<phase>/<document>/Release_Notes_Template.md`. Log completion.

## Output Format Specification

The generated `Release_Notes_Template.md` SHALL contain these sections in order:

1. **Version & Date** -- Product name, version, release date, release type
2. **Release Highlights** -- Executive summary of the release
3. **New Features** -- Per-feature entries with descriptions and user benefit
4. **Improvements** -- Enhancements to existing functionality
5. **Bug Fixes** -- Resolved issues with symptom descriptions
6. **Breaking Changes** -- Changes that require user action
7. **Migration Guide** -- Step-by-step transition instructions
8. **Known Issues** -- Unresolved issues with severity and workarounds
9. **Deprecation Notices** -- Features scheduled for future removal
10. **Compatibility Matrix** -- Tested platform and dependency versions

## Common Pitfalls

- **Implementation-focused language:** Entries SHALL describe user-facing impact, not code changes or internal refactoring.
- **Missing migration actions:** Every breaking change SHALL include a concrete step the user must take.
- **No severity on known issues:** Every known issue SHALL include a severity classification.
- **Missing version context:** The template SHALL include semantic versioning guidance for consistent version numbering.
- **No completeness checklist:** The template SHALL include a pre-publish checklist for release managers.

## Verification Checklist

1. `Release_Notes_Template.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all ten sections.
2. Version header includes semantic versioning guidance and release type classification.
3. New Features section template includes user benefit and requirement traceability fields.
4. Breaking Changes section template requires a migration action for each entry.
5. Known Issues section template includes severity classification.
6. Compatibility matrix template covers OS, browser, and dependency versions.
7. Pre-publish checklist is present at the end of the template.
8. Authoring guidance comments are embedded in each section.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 02 (Requirements Engineering) | Consumes `vision.md` for product identity and versioning context |
| Upstream | Phase 02 (SRS Draft) | Optionally consumes `SRS_Draft.md` for requirement traceability |
| Downstream | Phase 09 (Compliance) | Release notes feed compliance documentation for change tracking |

## Standards Compliance

- **IEEE 830** -- Recommended Practice for Software Requirements Specifications. Governs traceability of features to requirements and structured documentation of changes.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step release notes template generation logic.
- `README.md` -- Quick-start guide for this skill.
