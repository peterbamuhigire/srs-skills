---
name: "installation-guide"
description: "Generate step-by-step installation instructions covering prerequisites, system requirements, installation procedures, configuration, and verification per ISO 26514."
metadata:
  use_when: "Use when the task matches installation guide skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Installation Guide Skill

## Overview

This is the second skill in Phase 08 (End-User Documentation). It produces a comprehensive installation guide that walks end users and system administrators through prerequisites, system requirements, step-by-step installation procedures, post-installation configuration, and verification. The output conforms to ISO 26514 (User Documentation) and serves as the authoritative installation reference for deploying the software in end-user environments.

## When to Use This Skill

- After `tech_stack.md` exists in `../project_context/` with technology choices, runtime versions, and platform requirements.
- When end users or system administrators require clear installation instructions.
- Optionally after Phase 06 when `Deployment_Guide.md` exists in `../output/` for infrastructure and deployment context.

## Quick Reference

| Attribute    | Value |
|--------------|-------|
| **Inputs**   | `../project_context/tech_stack.md`, `../output/Deployment_Guide.md` (optional) |
| **Output**   | `../output/Installation_Guide.md` |
| **Tone**     | Procedural, precise, user-facing |
| **Standard** | ISO 26514 |
| **Time**     | 10-20 minutes |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| tech_stack.md | `../project_context/tech_stack.md` | Yes | Technology choices, runtime versions, OS compatibility, dependencies |
| Deployment_Guide.md | `../output/Deployment_Guide.md` | No | Infrastructure context, environment configuration, deployment procedures |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Installation_Guide.md | `../output/Installation_Guide.md` | Complete installation guide with system requirements, prerequisites, steps, configuration, verification, and troubleshooting |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `tech_stack.md` from `../project_context/`. Optionally read `Deployment_Guide.md` from `../output/`. Log the absolute path of each file read. Halt if any required file is missing.

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
- Write the completed document to `../output/Installation_Guide.md`. Log the total count of installation steps.

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

1. `Installation_Guide.md` exists in `../output/` with all nine sections populated.
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
