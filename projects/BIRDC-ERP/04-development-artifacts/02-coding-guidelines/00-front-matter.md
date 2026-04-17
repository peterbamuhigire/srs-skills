---
title: "Coding Guidelines — BIRDC ERP"
subtitle: "Development Standards for PHP, Kotlin, Git, and Database Access"
author: "Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
status: "Draft"
---

# Coding Guidelines — BIRDC ERP

**Document Type:** Coding Guidelines and Development Standards

**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC

**Client:** PIBID / BIRDC, Nyaruzinga hill, Bushenyi District, Western Uganda

**Date:** 2026-04-05

**Version:** 1.0

**Status:** Draft — Pending Consultant Review

---

## Purpose

These guidelines define the coding standards, development practices, and review requirements that govern all BIRDC ERP development. They are mandatory for all developers — contractor, staff, or third-party — who contribute code to the BIRDC ERP repository.

Adherence to these guidelines is verified at two points:

1. **Automated gate:** CI linters (PHPStan, PHP_CodeSniffer, ktlint) reject non-compliant code before a pull request can be merged.
2. **Human gate:** Code reviewers use the checklists in Section 5 to verify compliance before approval.

A pull request that passes the automated gate but fails the human checklist is rejected.
