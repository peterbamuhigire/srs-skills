---
name: dev-environment-setup
description: Generate development environment setup documentation with toolchain requirements, dependency installation, local configuration, and build instructions per IEEE 1074.
---

# Dev Environment Setup Skill

## Overview

This is the third skill in Phase 04 (Development Artifacts). It generates comprehensive development environment setup documentation that enables any developer to establish a working local environment from scratch. The output covers prerequisites, dependency installation, local configuration, build commands, IDE setup, and verification steps, conforming to IEEE 1074 (Software Life Cycle Processes).

## When to Use

- After `tech_stack.md` exists in `../project_context/` with toolchain and runtime details.
- Optionally after `HLD.md` exists in `../output/` to derive infrastructure dependencies (databases, caches, message queues).
- Can run in parallel with `02-coding-guidelines` since they address independent concerns.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../project_context/tech_stack.md`; optionally `../output/HLD.md` |
| **Output**  | `../output/Dev_Environment_Setup.md` |
| **Tone**    | Instructional, step-by-step, platform-aware |
| **Standard** | IEEE 1074 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| tech_stack.md | `../project_context/tech_stack.md` | Yes | Runtimes, package managers, databases, and infrastructure tools |
| HLD.md | `../output/HLD.md` | No | Deployment topology to derive local infrastructure dependencies |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Dev_Environment_Setup.md | `../output/Dev_Environment_Setup.md` | Complete environment setup guide with numbered steps and verification commands |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `tech_stack.md` from `../project_context/`. Optionally read `HLD.md` from `../output/` for infrastructure context. Log the absolute path of each file read. If `tech_stack.md` is missing, halt execution and report the gap.

### Step 2: Define Prerequisites

Document all prerequisites the developer must have before starting:
- Operating system requirements (supported OS versions)
- Runtime versions with exact version numbers (e.g., Node.js 20.x, Python 3.12, Java 21)
- Package managers with minimum versions (e.g., npm 10.x, pip 24.x)
- System-level dependencies (e.g., Git, Docker, Docker Compose)

### Step 3: Define Dependency Installation Steps

Provide numbered, copy-paste-ready installation commands:
- Platform-specific commands (macOS/Homebrew, Windows/winget, Linux/apt)
- Runtime installation via version managers (nvm, pyenv, sdkman)
- Project dependency installation (npm install, pip install -r, mvn install)
- Infrastructure dependencies (database, cache, message queue via Docker Compose)

### Step 4: Define Local Configuration

Document all local configuration required:
- Environment variables with descriptions and example values
- Configuration file templates (`.env.example`, `config.local.yaml`)
- Database setup commands (create database, run migrations, seed data)
- SSL/TLS certificates for local development if applicable

### Step 5: Define Build and Run Commands

Document the complete build and execution workflow:
- Build commands (compile, transpile, bundle)
- Run commands for development mode with hot-reload
- Run commands for production-like mode
- Database migration commands
- Common task runner commands (lint, format, type-check)

### Step 6: Define IDE Setup Recommendations

Provide IDE configuration guidance:
- Recommended IDE or editor with version
- Required extensions or plugins (linter, formatter, debugger)
- Workspace settings (tab size, line endings, encoding)
- Debug configuration templates (launch.json, run configurations)

### Step 7: Write Output with Verification Steps

Write the completed document to `../output/Dev_Environment_Setup.md`. Include a Verification Checklist section with commands that confirm each component is correctly installed and configured. Include a Troubleshooting section addressing common setup failures. Log the total count of installation steps and verification checks.

## Output Format

The generated `Dev_Environment_Setup.md` shall contain these sections in order: Document Header (project name, date, version, standard), 1. Prerequisites, 2. Installation Steps (numbered, platform-specific), 3. Configuration, 4. Build and Run, 5. IDE Setup, 6. Verification Checklist, 7. Troubleshooting.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Missing exact version numbers | Every runtime and tool shall specify an exact or minimum version number |
| Platform-specific commands without labels | Every command block shall state which OS it targets |
| Environment variables without examples | Every env var shall include an example value and description |
| No verification steps | Every major installation step shall have a verification command |

## Verification Checklist

- [ ] `Dev_Environment_Setup.md` exists in `../output/` with all seven sections populated.
- [ ] Prerequisites list exact version numbers for all runtimes and tools.
- [ ] Installation steps provide platform-specific commands for at least two operating systems.
- [ ] Configuration section documents all environment variables with example values.
- [ ] Build and Run section covers development mode, production-like mode, and common tasks.
- [ ] Verification Checklist provides runnable commands to confirm correct setup.
- [ ] Troubleshooting section addresses at least three common setup failures.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `../project_context/tech_stack.md` | Reads toolchain and infrastructure details |
| Parallel | 02-coding-guidelines | Independent concern; can run simultaneously |
| Downstream | 04-contribution-guide | Informs the "Getting Started" section of the contribution guide |
| Downstream | Development teams | Primary onboarding reference for new developers |

## Standards

- **IEEE 1074** -- Software Life Cycle Processes. Governs the documentation of development environment and toolchain requirements.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step environment setup generation logic.
- `README.md` -- Quick-start guide for this skill.
