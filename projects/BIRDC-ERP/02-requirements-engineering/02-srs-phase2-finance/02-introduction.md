# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for Phase 2 — Financial Core of the BIRDC ERP system. Phase 2 delivers four tightly integrated financial modules: Financial Accounting and General Ledger (F-005), Accounts Receivable (F-006), Accounts Payable (F-007), and Budget Management (F-008).

This document is the authoritative requirements baseline for the Phase 2 development team. All functional requirements are expressed as stimulus-response pairs per IEEE Std 830-1998 Section 3.2. Every requirement must satisfy the verification criteria defined in IEEE Std 1012.

## 1.2 Document Scope

This SRS governs the design, implementation, and acceptance testing of the four financial modules that form the Financial Core of the BIRDC ERP. Together these modules provide:

- A dual-mode accounting engine satisfying both Parliamentary vote accountability (PIBID) and commercial International Financial Reporting Standards for SMEs (BIRDC IFRS)
- An immutable, hash-chained General Ledger (GL) with cryptographic tamper detection
- Fully automated GL posting from all operational modules — no manual journal entries for operational transactions
- Real-time Accounts Receivable (AR) tracking for customers and 1,071 field agents
- Full Accounts Payable (AP) lifecycle including three-way matching, farmer bulk payment, and Withholding Tax (WHT) management
- Parliamentary and commercial Budget Management with variance tracking, threshold alerts, and Director-override controls

Phase 2 depends on Phase 1 modules (F-001 through F-004) as GL posting sources. Phase 2 outputs feed Phase 3 (procurement AP), Phase 4 (production costing), and Phase 5 (payroll GL posting).

## 1.3 Definitions, Acronyms, and Abbreviations

All terms are defined in `_context/glossary.md`. The following are cited most frequently in this document:

| Term | Definition |
|---|---|
| AR | Accounts Receivable |
| AP | Accounts Payable |
| BR | Business Rule (see `_context/business_rules.md`) |
| CoA | Chart of Accounts |
| DC | Design Covenant (see `_context/vision.md`) |
| FEFO | First Expiry First Out |
| FDN | Fiscal Document Number |
| GL | General Ledger |
| IFRS | International Financial Reporting Standards |
| JE | Journal Entry |
| PAYE | Pay As You Earn |
| PPDA | Public Procurement and Disposal of Public Assets Authority |
| SRS | Software Requirements Specification |
| URA | Uganda Revenue Authority |
| Vote | Parliamentary budget allocation category |
| WHT | Withholding Tax |
| WIP | Work In Progress |

## 1.4 References

| Reference | Title |
|---|---|
| IEEE Std 830-1998 | Recommended Practice for Software Requirements Specifications |
| IEEE Std 1233-1998 | Guide for Developing System Requirements Specifications |
| IEEE Std 610.12-1990 | Standard Glossary of Software Engineering Terminology |
| IEEE Std 1012-2016 | Standard for System, Software, and Hardware Verification and Validation |
| ASTM E1340 | Standard Guide for Rapid Prototyping of Computerized Systems |
| IAS 7 | Statement of Cash Flows (IFRS Foundation) |
| IFRS for SMEs | International Financial Reporting Standard for Small and Medium-sized Entities |
| Uganda Companies Act Cap 110 | Financial records retention and audit obligations |
| Uganda Income Tax Act Cap 340 | WHT obligations, 7-year retention |
| Uganda PPDA Act | Public procurement compliance |
| BIRDC ERP Vision | `_context/vision.md` |
| BIRDC Business Rules | `_context/business_rules.md` |
| BIRDC Gap Analysis | `_context/gap-analysis.md` |

## 1.5 Overview

Section 2 provides the overall system description and design covenants applicable to Phase 2. Sections 3 through 6 define the functional requirements for modules F-005, F-006, F-007, and F-008 respectively. Section 7 defines non-functional requirements applicable across all Phase 2 modules. Section 8 defines the verification and traceability matrix.
