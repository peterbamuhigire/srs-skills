---
title: "SRS Phase 3c -- EFRIS Compliance Module (F-015)"
project: "Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft -- BLOCKED pending GAP-005"
---

# Section 1: Introduction to the EFRIS Compliance Module (F-015)

## 1.1 Purpose

This document specifies the Software Requirements Specification (SRS) for the Electronic Fiscal Receipting and Invoicing System (EFRIS) Compliance module (F-015) of the Maduuka SaaS platform. It is written per IEEE Std 830-1998 and covers the full scope of Phase 3c. The intended audience is the Maduuka development team, quality assurance engineers, the product owner, and the Uganda Revenue Authority (URA) integration partner review team.

## 1.2 Background: URA EFRIS

The Uganda Revenue Authority (URA) Electronic Fiscal Receipting and Invoicing System (EFRIS) is a mandatory fiscal receipting infrastructure for registered taxpayers in Uganda. Under URA's expansion mandate effective July 2025, EFRIS compliance is required for all businesses with annual turnover exceeding UGX 150,000,000 (one hundred fifty million Uganda Shillings). The mandate requires every invoice and receipt to carry a Fiscal Document Number (FDN) issued by the URA EFRIS system and a URA-generated QR code verifiable by URA-approved scanners.

EFRIS operates as a system-to-system Application Programming Interface (API) integration between the business's Point of Sale or invoicing software and the URA EFRIS server. The integration transmits transaction data to URA in real time at the point of sale and receives an FDN in return, which is printed on the customer's receipt.

Integration with the URA EFRIS API requires URA accreditation as a system-to-system integration partner. Maduuka has not yet obtained this accreditation (see GAP-005 in Section 1.6). All functional requirements that depend on the live EFRIS API are tagged **[BLOCKED: GAP-005]** and shall not be implemented until accreditation is confirmed and sandbox integration testing is complete.

## 1.3 Scope

The EFRIS Compliance module (F-015) provides Maduuka subscribers in Uganda with full URA EFRIS compliance for their Point of Sale (F-001) and invoicing operations. The module covers:

- EFRIS tenant configuration and URA credential management
- Real-time fiscal invoice submission to URA at point of sale
- FDN and QR code printing on all receipts and invoices
- B2B, B2C, and B2G transaction type handling
- Offline queuing when the URA server is unavailable
- EFRIS-compliant credit notes and debit notes
- EFRIS status dashboard and reconciliation reporting

F-015 is an opt-in add-on priced at +UGX 40,000 per month. It is not mandatory for all Maduuka subscribers. Subscribers outside Uganda, or Ugandan subscribers whose annual turnover is below the URA mandate threshold, may subscribe voluntarily to prepare for future compliance.

F-015 integrates with F-001 (Point of Sale) at the receipt generation stage and with the invoicing functions in F-002 (Inventory -- purchase invoices) and F-006 (Financial Accounts). All Phase 1 functional requirements in those modules remain in force.

## 1.4 Definitions

**B2B Transaction** -- A business-to-business EFRIS transaction where the purchasing entity is a registered business identified by its URA Tax Identification Number (TIN). EFRIS requires the buyer's TIN to be transmitted to URA for B2B transactions.

**B2C Transaction** -- A business-to-consumer EFRIS transaction where the purchasing entity is an individual consumer not identified by TIN. No buyer TIN is required for B2C transactions.

**B2G Transaction** -- A business-to-government EFRIS transaction where the purchasing entity is a government body identified by a procurement reference number. EFRIS requires the procurement reference to be transmitted to URA for B2G transactions.

**Credit Note** -- An EFRIS-compliant document issued when a sale is voided or a partial refund is granted, referencing the original FDN and transmitted to URA to reverse or reduce the fiscal record of the original transaction.

**Debit Note** -- An EFRIS-compliant document issued when the price of an invoiced item is adjusted upward after the original invoice, referencing the original FDN and transmitted to URA to record the additional amount.

**EFRIS** -- Electronic Fiscal Receipting and Invoicing System. The URA system that issues Fiscal Document Numbers and records all fiscal transactions for registered taxpayers in Uganda.

**EFRIS API** -- The system-to-system Application Programming Interface provided by URA for accredited integration partners to submit fiscal transactions and receive Fiscal Document Numbers programmatically.

**FDN (Fiscal Document Number)** -- A unique identifier issued by the URA EFRIS system for every submitted fiscal transaction. The FDN is mandatory on all receipts and invoices issued to customers.

**Fiscal Receipt** -- A receipt or invoice that carries a URA-issued FDN and QR code, confirming that the transaction has been registered in the URA EFRIS system.

**Offline Queue** -- A local store of fiscal transactions that have been completed in Maduuka but not yet submitted to URA, accumulated during periods when the URA EFRIS server is unavailable. Transactions in the offline queue are assigned a `PENDING` status and updated to `CONFIRMED` once the FDN is received after connectivity is restored.

**Product Catalogue Synchronisation** -- The process of mapping Maduuka's internal product catalogue entries to the corresponding items in the URA EFRIS standard commodity catalogue, required before fiscal invoices can be submitted to URA.

**QR Code** -- A machine-readable two-dimensional barcode generated by URA and embedded in the FDN response, printed on every fiscal receipt. The QR code allows customers and auditors to verify the receipt's authenticity via the URA EFRIS portal or any URA-approved scanner.

**TIN (Tax Identification Number)** -- The unique identifier assigned to a registered taxpayer by URA, used to identify the seller and (for B2B transactions) the buyer in EFRIS submissions.

**URA** -- Uganda Revenue Authority. The government body responsible for tax administration in Uganda and the operator of the EFRIS system.

## 1.5 References

- IEEE Std 830-1998, *Recommended Practice for Software Requirements Specifications*
- IEEE Std 610.12-1990, *Standard Glossary of Software Engineering Terminology*
- URA EFRIS Integration Guide (version current at accreditation date -- obtain from URA upon GAP-005 resolution)
- URA EFRIS API Technical Specification (obtain from `efris@ura.go.ug` upon GAP-005 resolution)
- Maduuka Phase 1 SRS, Section 4.1 (F-001: Point of Sale)
- Maduuka `_context/features.md`, F-015 entry
- Maduuka `_context/gap-analysis.md`, GAP-005

## 1.6 GAP-005 Status and Impact

**GAP-005: EFRIS API Accreditation -- Not Started**

Maduuka must register as a URA system-to-system integration partner before any EFRIS API call can be made. The registration process involves: submitting an application to `efris@ura.go.ug`, URA review and approval (multi-week timeline), issuance of sandbox credentials, completion of integration testing against the URA sandbox, and final production accreditation.

Until GAP-005 is resolved, the following impacts apply:

- All functional requirements tagged **[BLOCKED: GAP-005]** are approved for design and data model work only. No implementation of live API calls may proceed.
- The EFRIS module may be built with a full offline-simulation mode for testing purposes, using a mock FDN generator that mimics URA API responses.
- The product owner (Peter) is responsible for initiating the URA registration process and tracking accreditation progress.
- The Phase 3c implementation schedule shall not commit to a go-live date until sandbox integration testing is confirmed complete.

[CONTEXT-GAP: URA API version] -- The specific URA EFRIS API version number and endpoint base URL are not available in `_context/`. These must be obtained from URA upon GAP-005 resolution and documented in `_context/integrations.md` before detailed API implementation design begins.

## 1.7 Overview of This Document

Section 2 contains all functional requirements for F-015, organised by capability area. Section 3 specifies non-functional requirements. Section 4 documents design constraints. Requirements follow stimulus-response format per IEEE 830 Section 4.3.
