---
name: "deployment-guide"
description: "Generate a step-by-step deployment procedure with pre-checks, deployment steps, rollback procedures, and post-deployment verification per IEEE 1062."
metadata:
  use_when: "Use when the task matches deployment guide skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Deployment Guide Skill

## Overview

This is the first skill in Phase 06 (Deployment & Operations). It produces a comprehensive deployment guide that defines pre-deployment checklists, numbered deployment steps with exact commands, database migration procedures, environment-specific configuration, rollback procedures, and post-deployment verification. The output conforms to IEEE 1062 (Software Acquisition) and serves as the authoritative deployment reference for operations teams.

## When to Use

- After Phase 03 completes and `HLD.md` exists in `projects/<ProjectName>/<phase>/<document>/` with system architecture and component topology.
- When `tech_stack.md` is present in `projects/<ProjectName>/_context/` with technology choices and runtime versions.
- Optionally when `Database_Design.md` exists in `projects/<ProjectName>/<phase>/<document>/` for database migration steps.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/_context/tech_stack.md`, `projects/<ProjectName>/<phase>/<document>/Database_Design.md` (optional) |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md` |
| **Tone**    | Procedural, precise, operations-facing |
| **Standard** | IEEE 1062 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `projects/<ProjectName>/<phase>/<document>/HLD.md` | Yes | System architecture, component topology, deployment targets |
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | Yes | Technology choices, runtime versions, package managers |
| Database_Design.md | `projects/<ProjectName>/<phase>/<document>/Database_Design.md` | No | Database schema for migration step generation |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Deployment_Guide.md | `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md` | Complete deployment procedure with pre-checks, steps, rollback, and verification |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `HLD.md` from `projects/<ProjectName>/<phase>/<document>/` and `tech_stack.md` from `projects/<ProjectName>/_context/`. Optionally read `Database_Design.md` from `projects/<ProjectName>/<phase>/<document>/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Define Pre-Deployment Checklist

Document every action that shall occur before deployment begins:
- Database backup verification (method, location, retention)
- Stakeholder notification (who, channel, timing)
- Maintenance window scheduling (duration estimate, approval)
- Dependency verification (external services, third-party APIs)
- Artifact readiness (build artifacts, container images, checksums)

### Step 3: Define Deployment Steps

Produce numbered deployment steps with exact commands where the tech stack permits:
- Service shutdown or traffic drain sequence
- Artifact deployment (copy, pull, install)
- Service startup sequence with dependency ordering
- Each step shall include expected duration and success criteria

### Step 4: Define Database Migration Steps

If `Database_Design.md` is present, define migration steps:
- Migration script execution order
- Data transformation steps
- Schema validation after migration
- If no database design exists, state that this section is not applicable

### Step 5: Define Configuration Changes per Environment

Document configuration differences across environments:
- Dev, Staging, and Production environment variables
- Feature flags and toggles per environment
- External service endpoints per environment (API URLs, credentials references)

### Step 6: Define Rollback Procedure

Provide step-by-step reversal instructions:
- Decision criteria for triggering rollback
- Service rollback sequence (reverse of deployment order)
- Database rollback (restore from backup or reverse migration)
- Configuration rollback
- Verification that rollback restored previous state

### Step 7: Define Post-Deployment Verification

Document verification procedures after deployment completes:
- Health check endpoints and expected responses
- Smoke test scenarios (critical user paths)
- Performance baseline comparison
- Log review checklist (error rates, warnings)

### Step 8: Define Environment Matrix and Write Output

Produce an environment matrix summarizing resource differences across dev/staging/prod. Write the completed document to `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md`. Log the total count of deployment steps and rollback steps.

## Output Format

The generated `Deployment_Guide.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Pre-Deployment Checklist, 2. Deployment Steps, 3. Database Migrations, 4. Configuration, 5. Rollback Procedure, 6. Post-Deployment Verification, 7. Environment Matrix.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Deployment steps without exact commands | Every step shall include the literal command or action to execute |
| Missing rollback procedure | Every deployment guide shall include a complete reversal procedure |
| No environment differentiation | Configuration shall distinguish dev, staging, and prod explicitly |
| Post-deployment verification omitted | Every guide shall define health checks and smoke tests |

## Verification Checklist

- [ ] `Deployment_Guide.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all seven sections populated.
- [ ] Pre-deployment checklist includes backup verification and stakeholder notification.
- [ ] Deployment steps are numbered with exact commands and expected durations.
- [ ] Rollback procedure reverses every deployment step.
- [ ] Post-deployment verification defines health checks and smoke tests.
- [ ] Environment matrix covers dev, staging, and production.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | Phase 03 (01-high-level-design) | Consumes `HLD.md` for system architecture and component topology |
| Upstream | Phase 04 (01-technical-specification) | Consumes tech specs for deployment context |
| Downstream | 02-runbook | Informs incident response with deployment context |
| Downstream | 04-infrastructure-docs | Feeds deployment topology into infrastructure documentation |

## Standards

- **IEEE 1062** -- Recommended Practice for Software Acquisition. Governs deployment procedure structure and acceptance criteria.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step deployment guide generation logic.
- `README.md` -- Quick-start guide for this skill.
