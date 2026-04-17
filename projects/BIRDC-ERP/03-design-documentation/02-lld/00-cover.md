---
title: "BIRDC ERP — Low-Level Design (LLD)"
subtitle: "Version 1.0 | 2026-04-05"
author: "Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
---

# BIRDC ERP — Low-Level Design

**Document type:** Low-Level Design (LLD)
**Version:** 1.0
**Date:** 2026-04-05
**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC
**Client:** BIRDC / PIBID, Nyaruzinga Hill, Bushenyi District, Western Uganda
**Classification:** Confidential — BIRDC Internal

---

## Document Purpose

This Low-Level Design document defines the service contracts, method signatures, error handling conventions, data exchange formats, and permission matrix for every key service class in the BIRDC ERP system. It is the primary reference for developers implementing each service class and for QA engineers writing unit and integration tests.

Every method signature in this document constitutes an implementer contract. Method names, parameter types, and return types are binding. Business rule references (BR-xxx) identify which business rules constrain the method's behaviour.

This document assumes familiarity with the High-Level Design (HLD). Architectural decisions not repeated here (layered architecture, database design, security model) are governed by the HLD.

---

## Revision History

| Version | Date | Author | Summary |
|---|---|---|---|
| 1.0 | 2026-04-05 | Peter Bamuhigire | Initial release |

---

## Type Conventions

The following type aliases are used throughout this document:

| Alias | PHP Type | Description |
|---|---|---|
| `Money` | `int` | All monetary amounts in Uganda Shillings (UGX) stored as integer shillings. No floating-point arithmetic on money. |
| `Uuid` | `string` | UUID v4 string identifier (used for idempotency keys) |
| `DateString` | `string` | ISO 8601 date: `YYYY-MM-DD` |
| `DateTimeString` | `string` | ISO 8601 datetime UTC: `YYYY-MM-DDTHH:MM:SSZ` |
| `AuthResult` | `array` | `{user: UserDTO, access_token: string, refresh_token: string, expires_in: int}` |
| `TokenPair` | `array` | `{access_token: string, refresh_token: string, expires_in: int}` |
| `PermissionMatrix` | `array` | `{role: string, pages: string[], endpoints: string[], elements: string[], conditions: array}` |
| `BatchAllocation` | `array` | `{batch_id: int, batch_number: string, quantity: float, expiry_date: DateString}` |
| `IntegrityReport` | `array` | `{account_id: int, lines_checked: int, broken_at: int|null, broken_journal_id: int|null, status: string}` |
| `MatchResult` | `array` | `{matched: bool, price_variance_pct: float, quantity_variance_pct: float, flags: string[]}` |
