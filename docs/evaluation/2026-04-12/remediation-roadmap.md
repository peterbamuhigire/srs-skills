# Remediation Roadmap

## Purpose

This roadmap turns the 2026-05-01 re-evaluation into an execution sequence. The goal is to move the repository from a strong internal SDLC engine to a reproducible, world-class software planning, design, development, and maintenance assurance system.

## Stage 1: Restore Reproducible Proof

Goal:

- make the current checkout prove its own claims from a fresh environment

Concrete work:

- restore or regenerate `projects/_demo-hybrid-regulated`
- ensure `engine/tests/test_cli_sabotage.py` passes
- document `python -m pip install -e ".[dev]"`
- run and document `python -X utf8 -m pytest engine\tests -q`
- update README proof claims to match actual commands and outputs

Success condition:

- engine contract passes
- engine test suite passes
- demo project validates cleanly
- coverage claim matches the actual report

## Stage 2: Normalize the Skill Catalog

Goal:

- make every portable skill entrypoint consistent and validator-clean

Concrete work:

- fix the 15 quick-validator failures
- resolve broken local links in SDLC skills
- add missing metadata and portable contract markers
- decide whether canonical skill paths are `skills/<name>` or `skills/skills/<name>`
- align `AGENTS.md`, `README.md`, `PROJECT_BRIEF.md`, and skill-local links to the chosen path
- reduce contract-gate warnings to zero or document accepted exemptions

Success condition:

- 240 of 240 skills pass quick validation, or exemptions are explicit
- contract gate is clean under strict mode or has documented accepted exceptions

## Stage 3: Establish Clean Project Proof

Goal:

- demonstrate that the engine can govern a realistic workspace, not only a tiny fixture

Concrete work:

- select a reference project such as `AcademiaPro`
- add missing canonical `_context` files
- add ADR, threat model, coding standards, environment setup, and contribution guide
- add 29119 testing evidence, completion report, deployment guide, runbook, monitoring/SLO, readiness, and change-window docs
- add agile artifacts, user docs, audit report, and risk register
- run `engine sync`
- run `engine validate`
- generate an evidence pack

Success condition:

- at least one realistic workspace validates cleanly
- evidence pack generation succeeds
- documentation links to this workspace as the realistic proof path

## Stage 4: Build Requirements-to-Code-to-Test Traceability

Goal:

- extend assurance beyond document-to-document linkage

Concrete work:

- define trace schemas for requirements to modules, APIs, schemas, jobs, UI flows, tests, and test results
- add validators for missing, stale, or weak implementation evidence
- require test-result artifacts for release-scoped requirements
- expose trace gaps in Markdown and JSON reports

Success condition:

- a reviewer can trace a requirement from business intent to design, implementation target, test case, and test result

## Stage 5: Add Release and Runtime Evidence

Goal:

- connect documented intent to observed operational reality

Concrete work:

- ingest release manifests
- ingest deployment and rollback evidence
- link smoke tests, SLO checks, incidents, and monitoring snapshots to requirements and controls
- add runtime-evidence gates for release readiness and maintenance review

Success condition:

- the engine can distinguish documented intent from deployed and observed behavior

## Stage 6: Deepen Semantic and Audit Assurance

Goal:

- move from structural governance to deeper correctness and compliance assurance

Concrete work:

- expand clause-level proof across more standards and artifacts
- add semantic sufficiency checks across requirement, design, test, and control chains
- add contradiction and false-completeness detection
- generate audit views by obligation, control, requirement, evidence, waiver, and sign-off

Success condition:

- external reviewers can inspect coherent clause-level and evidence-level proof without relying on narrative interpretation alone

## Recommended Order

1. Restore reproducible proof.
2. Normalize the skill catalog.
3. Establish clean project proof.
4. Build requirements-to-code-to-test traceability.
5. Add release and runtime evidence.
6. Deepen semantic and audit assurance.

## Why This Order

The current blocker is not conceptual design. It is reproducibility. A world-class engine must first keep its proof assets, tests, validators, and documentation in sync. Once that foundation is green, deeper assurance features will compound instead of adding more unverified claims.
