# LonghornERP Human Capital Management Enhancement Roadmap

## Purpose

This document translates the source book `C:\Users\Peter\Downloads\ERP Playbook\The Human Capital Management System Playbook.epub` into concrete enhancement decisions for LonghornERP.

The goal is to make LonghornERP's HR capability a disciplined human capital operating system, not only a payroll-processing screen set.

## Executive Decision

LonghornERP should strengthen `HR_PAYROLL` along 3 lines:

1. Keep `HR_PAYROLL` as the tenant-facing commercial module, but deepen it beyond employee records and payroll execution.
2. Add stronger workforce-governance capabilities: job architecture, position control, manager self-service, payroll operating rhythm, and privacy controls.
3. Treat recruiting, learning, performance, succession, and broader talent-suite depth as future bounded capabilities rather than forcing all HCM ambition into the first release of `HR_PAYROLL`.

The playbook makes one point very clearly: HCM value comes from process, data discipline, decision rights, and controlled self-service. LonghornERP should reflect that operating model.

## Critical Findings from the Playbook

### 1. HCM is a system of record, workflow, and experience layer

The HCM playbook frames HCM as the governed source of workforce truth:

- effective-dated worker history
- organizational and manager hierarchies
- job and position frameworks
- payroll, time, attendance, and leave controls
- employee and manager self-service
- people reporting and analytics

Critical implication for LonghornERP:

- employee master data alone is not enough
- payroll correctness depends on upstream workforce governance
- manager self-service is not a UI extra; it is part of the operating model

### 2. Payroll quality is an operating rhythm, not only a calculation engine

The playbook repeatedly emphasizes:

- payroll calendars and cutoffs
- pre-payroll validation
- variance review
- off-cycle and retro controls
- parallel payroll governance
- segregation of duties

Critical implication for LonghornERP:

- a correct payroll formula is necessary, but it is not sufficient
- LonghornERP needs explicit payroll-governance workflows, not just run buttons

### 3. Data discipline and privacy are core HCM requirements

The playbook treats people data as sensitive and governance-heavy. Effective-dated truth, role-based visibility, auditability, and controlled data export are first-class requirements.

Critical implication for LonghornERP:

- people-data security must be modeled as product behavior, not only infrastructure policy
- HR workflow design must preserve audit trails and historical truth

## Current LonghornERP Position

## Strengths already present

LonghornERP already has solid HR and payroll foundations:

- employee master data
- leave management
- attendance capture
- payroll configuration and payroll runs
- payslips and salary disbursement
- loans, advances, and exit processing
- employee self-service basics
- statutory integration hooks through localisation and integration layers

## Critical gaps

### Gap A: Workforce operating model is too light

Current scope is strong on payroll administration but lighter on:

- job architecture
- position management
- budgeted headcount control
- manager-initiated workforce transactions
- effective-dated organizational change governance

### Gap B: Payroll governance is too implicit

Current documentation does not yet model enough depth for:

- payroll calendars and cutoffs
- readiness checks before payroll release
- variance review against prior payroll
- shadow or parallel payroll runs
- dual-control approval and release evidence

### Gap C: People analytics and privacy controls need stronger expression

Current documentation mentions self-service and statutory compliance, but it needs stronger productized support for:

- headcount and workforce dashboards
- manager oversight of team events
- export governance for sensitive employee data
- clearer separation between operational visibility and highly restricted compensation data

## Recommended Module Boundary

`HR_PAYROLL` should own:

- worker record and effective-dated employment history
- organizational, position, and manager workflow context
- leave, attendance, payroll, and statutory control
- employee and manager self-service
- payroll-governance workbench
- operational workforce analytics

It should not own:

- identity and authentication policy, which remains under `USER_MGMT` and platform IAM
- final accounting-book governance, which remains under `ACCOUNTING`
- full recruiting, learning, and succession depth unless Chwezi later chooses to introduce dedicated talent capabilities

## Required HCM Uplifts

LonghornERP should explicitly add or strengthen:

- job architecture and position management
- manager self-service workbench
- onboarding, probation, and controlled employee change workflows
- payroll calendar, cutoff, and readiness controls
- payroll variance and parallel-run capability
- people-data export controls and stronger privacy guardrails
- people analytics for headcount, absenteeism, overtime, and payroll quality

## Recommended Delivery Steps

1. Upgrade the module inventory and architecture language so `HR_PAYROLL` is positioned as governed workforce operations, not only payroll processing.
2. Extend the HR & Payroll SRS for position management, payroll-governance controls, manager self-service, and analytics.
3. Extend design documentation for new services, endpoints, and data structures supporting those capabilities.
4. Update test documentation and end-user guidance so the operating model is verifiable and teachable.

## Output Standard

A stronger LonghornERP HCM capability must support:

- accurate and controlled payroll
- workforce data integrity over time
- accountable manager participation
- privacy-aware employee-data operations
- audit-ready statutory and payroll evidence
- SME-friendly usability without consultant-dependent workflow design
