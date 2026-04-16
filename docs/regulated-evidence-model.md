# Regulated Evidence Model

This repository can draft compliance-oriented artifacts, but audit-grade work requires an evidence model stronger than narrative guidance alone. This document defines the minimum evidence chain the engine expects for regulated delivery.

## Purpose

Use this model when the project touches healthcare, finance, education, government, privacy-regulated data, or any environment where "we documented it" is not enough.

## Evidence Principle

Do not treat a compliance document as proof by itself. Proof comes from linked evidence across the lifecycle.

The minimum chain is:

`Regulation/Control -> Policy or obligation -> Requirement -> Design decision -> Test evidence -> Operational control -> Audit record`

## Required Evidence Layers

1. **Regulatory source layer**
   - Capture the governing law, regulation, framework, customer control catalog, or internal policy.
   - Break it into identifiable obligations or controls.

2. **Requirements layer**
   - Map each obligation to one or more requirement IDs.
   - If no requirement exists, record a `[CONTROL-GAP]`.

3. **Design layer**
   - Show where the control is implemented architecturally: API contract, workflow constraint, encryption boundary, audit log, retention mechanism, segregation-of-duties point, and so on.

4. **Verification layer**
   - Map each requirement or control to one or more deterministic tests, inspections, or review checks.
   - A control without verification is a claim, not evidence.

5. **Operational layer**
   - Identify runtime controls such as alerting, access review, backup verification, retention enforcement, incident response, or key rotation.

6. **Audit layer**
   - Record who reviewed what, on what date, using which artifacts, with which unresolved findings.

## Required Artifacts

At minimum, regulated projects should maintain:

- control or obligation register
- requirements traceability matrix
- design artifacts with control references
- deterministic test evidence
- deployment and runbook controls
- risk assessment and audit report

## Minimum Review Questions

Before describing a project as compliance-ready, answer all of these:

1. Which exact obligations apply?
2. Which requirement IDs implement them?
3. Which design elements enforce them?
4. Which tests prove them?
5. Which runtime controls sustain them?
6. Which findings remain open?

## Relationship to Repository Phases

- Phase 01 identifies regulated scope and stakeholders.
- Phase 02 converts obligations into traceable requirements.
- Phase 03 translates them into architecture and control points.
- Phase 05 proves them through deterministic verification.
- Phase 06 shows operational enforcement.
- Phase 09 assembles the audit trail.

## Claim Discipline

Do not claim:

- "compliant"
- "audit-ready"
- "full traceability"
- "control coverage complete"

unless the evidence chain is assembled and the missing links are either zero or explicitly logged.
