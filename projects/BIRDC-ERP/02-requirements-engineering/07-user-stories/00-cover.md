---
title: "User Stories — BIRDC ERP"
subtitle: "Requirements Engineering | Document 07"
author: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
---

# User Stories — BIRDC ERP

**Project:** BIRDC Enterprise Resource Planning System

**Client:** PIBID / BIRDC, Nyaruzinga Hill, Bushenyi District, Western Uganda

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

**Document Version:** 1.0

**Date:** 2026-04-05

**Classification:** Requirements Engineering — Document 07

---

## Purpose

This document captures the complete user story register for the BIRDC ERP system. Each user story expresses a stakeholder need from the perspective of a named persona, with testable acceptance criteria, MoSCoW priority classification, delivery phase assignment, and traceability to a functional requirement identifier.

User stories are grouped by persona. The 8 primary personas are: Prossy (Cashier), Samuel (Sales Agent), Grace (Finance Director), Robert (Procurement Manager), David (Store Manager), Dr. Amara (QC Manager), Moses (Production Supervisor), Patrick (Collections Officer), and The Director. All 17 operational modules and 6 Android applications are covered.

Stories conform to the IEEE 830 verifiability criterion: each acceptance criterion describes a deterministic, pass/fail test condition.

---

## Persona Index

| Persona | Role | Module Focus | Stories |
|---|---|---|---|
| Prossy | Factory Gate Cashier | POS (F-002), Inventory (F-003) | US-001 – US-009 |
| Samuel | Field Sales Agent | Sales Agent App, Agent Distribution (F-004), AR (F-006) | US-010 – US-022 |
| Grace | Finance Director | GL (F-005), AR (F-006), AP (F-007), Budget (F-008), Payroll (F-014) | US-023 – US-036 |
| Robert | Procurement Manager | Procurement (F-009), Farmer Management (F-010), AP (F-007) | US-037 – US-047 |
| David | Store Manager | Inventory (F-003), Agent Distribution (F-004) | US-048 – US-055 |
| Dr. Amara | QC / Lab Manager | QC (F-012), Manufacturing (F-011) | US-056 – US-062 |
| Moses | Production Supervisor | Manufacturing (F-011), Factory Floor App | US-063 – US-069 |
| Patrick | Collections Officer | Farmer Delivery App, Farmer Management (F-010), Procurement (F-009) | US-070 – US-077 |
| The Director | BIRDC Director | Executive Dashboard App, Reporting across all modules | US-078 – US-084 |

---

## Conventions

- Acceptance criteria are written as deterministic test oracles (pass/fail, not judgment calls).
- MoSCoW priorities: *Must Have* = system cannot go live without it; *Should Have* = high value, required within phase; *Could Have* = valuable enhancement.
- Delivery phase references align with the 7-phase feature register (Phase 1 = Commerce Foundation through Phase 7 = Integration, Hardening, and Go-Live).
- FR references follow the pattern FR-[module]-[sequence].
