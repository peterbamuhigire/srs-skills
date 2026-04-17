---
title: "Requirements Traceability Matrix — BIRDC ERP"
subtitle: "Governance and Compliance Documentation Suite"
author: "Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
status: "Final Draft — Pending Human Review"
---

# Requirements Traceability Matrix — BIRDC ERP

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC
**Date:** 2026-04-05
**Version:** 1.0
**Document Status:** Final Draft — Pending Human Review
**Classification:** Governance and Compliance

---

## Purpose

This Requirements Traceability Matrix (RTM) establishes bidirectional traceability between all functional requirements (FRs) in the BIRDC ERP Software Requirements Specification suite and their corresponding business goals, business rules, design covenants, and test case identifiers. It satisfies the IEEE 1012-2012 traceability mandate and provides the audit artefact required by the Office of the Auditor General (OAG) Uganda for pre-development requirements review.

## Scope

This RTM covers all 17 BIRDC ERP modules across 7 delivery phases, as specified in the six SRS documents constituting the requirements documentation suite. Traceability chains run from business goals (BG) through functional requirements (FR) to test cases (TC). Reverse traceability from test cases back to business goals is derivable from this matrix.

## Business Goal Register

| ID | Business Goal |
|---|---|
| BG-001 | Operational Unity — replace fragmented spreadsheets with one system covering all 17 operational domains |
| BG-002 | Financial Integrity — dual-mode accounting, immutable hash-chained audit trail, 7-year retention |
| BG-003 | Agent Accountability — real-time agent cash balance tracking; automated FIFO remittance allocation for 1,071 agents |
| BG-004 | Circular Economy Visibility — mass balance for all input matooke across primary products, by-products, and scrap |
| BG-005 | Government Replicability — every BIRDC-specific rule in configuration tables, not code |

## Traceability Conventions

- **FR identifier format:** `FR-[MODULE]-[NNN]` where MODULE is the 3-letter module code.
- **Test case identifier format:** `TC-[MODULE]-[NNN]` — assigned in the Test Plan (Phase 5 documentation). Where a test case has not yet been written, the cell reads `[TC-PENDING]`.
- **Business Rule reference:** BR-001 through BR-018 as defined in `_context/business_rules.md`.
- **Design Covenant reference:** DC-001 through DC-007 as defined in `_context/vision.md`.
