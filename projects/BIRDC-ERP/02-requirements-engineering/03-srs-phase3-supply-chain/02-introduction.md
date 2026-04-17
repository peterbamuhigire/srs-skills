# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional requirements, non-functional requirements, and design constraints for Phase 3 of the BIRDC ERP system: Supply Chain & Farmers. This document covers two modules:

- **F-009:** Procurement & Purchasing
- **F-010:** Farmer & Cooperative Management

This SRS is prepared in accordance with IEEE Std 830-1998 (*Recommended Practice for Software Requirements Specifications*) and IEEE Std 1233-1998 (*Guide for Developing System Requirements Specifications*). Terminology follows IEEE Std 610.12-1990 (*Standard Glossary of Software Engineering Terminology*). Verifiability criteria follow ASTM E1340-96.

The intended audience is the BIRDC Director, Finance Director, Procurement Manager, IT Administrator, and the development team. Approval of this document by the BIRDC Director and Finance Director constitutes authorisation to proceed with Phase 3 design and development.

## 1.2 Scope

The BIRDC ERP system is a purpose-built, single-tenant enterprise resource planning system for the Banana Industrial Research and Development Centre (BIRDC) and the Presidential Initiative on Banana Industrial Development (PIBID), located at Nyaruzinga hill, Bushenyi District, Western Uganda.

Phase 3 delivers the supply chain and farmer management capabilities required to:

1. Execute PPDA-compliant procurement from standard commercial suppliers.
2. Execute the 5-stage cooperative farmer procurement workflow from bulk Purchase Order through individual farmer contribution breakdown to General Ledger posting.
3. Maintain a comprehensive farmer and cooperative database serving 6,440+ registered farmers across BIRDC's cooperative network.
4. Enable offline-first field data collection via the Farmer Delivery Android application.

Phase 3 modules integrate directly with Phase 1 (F-003: Inventory & Warehouse Management) for stock receipt, Phase 2 (F-005: Financial Accounting & General Ledger, F-007: Accounts Payable) for financial posting, and Phase 4 (F-011: Manufacturing & Production) as the source of raw material inventory.

## 1.3 Definitions, Acronyms, and Abbreviations

The following terms are defined as used throughout this document. The complete project glossary is maintained in `_context/glossary.md`.

| Term | Definition |
|---|---|
| BIRDC | Banana Industrial Research and Development Centre |
| PIBID | Presidential Initiative on Banana Industrial Development |
| Cooperative | A group of smallholder farmers organised for collective matooke procurement |
| DC | Design Covenant — one of 7 binding design constraints |
| GL | General Ledger |
| GRN | Goods Receipt Note |
| LPO | Local Purchase Order |
| Matooke | Fresh green bananas (*Musa* spp., AAB group) — primary raw material input |
| NIN | National Identification Number — Uganda national ID |
| PPDA | Public Procurement and Disposal of Public Assets Authority |
| PR | Purchase Request |
| PO | Purchase Order |
| RFQ | Request for Quotation |
| SRS | Software Requirements Specification |
| WHT | Withholding Tax — 6% on applicable local service supplier payments |

Additional acronyms used in this document:

- **BR** — Business Rule (defined in `_context/business_rules.md`)
- **DC** — Design Covenant (defined in `_context/vision.md`)
- **FR-PRO** — Functional Requirement, Procurement module
- **FR-FAR** — Functional Requirement, Farmer & Cooperative module
- **NFR** — Non-Functional Requirement
- **[CONTEXT-GAP: GAP-xxx]** — unresolved information gap per `_context/gap-analysis.md`

## 1.4 References

| Standard / Document | Citation |
|---|---|
| IEEE Std 830-1998 | *Recommended Practice for Software Requirements Specifications* |
| IEEE Std 1233-1998 | *Guide for Developing System Requirements Specifications* |
| IEEE Std 610.12-1990 | *Standard Glossary of Software Engineering Terminology* |
| ASTM E1340-96 | *Standard Guide for Rapid Prototyping of Computerized Systems* |
| Uganda PPDA Act, Cap. 305 | Public Procurement and Disposal of Public Assets Act |
| Uganda Data Protection and Privacy Act 2019 | Governs collection and storage of personal data including farmer NIN, GPS, and mobile money details |
| Uganda Companies Act 2012 | 7-year financial record retention requirement |
| Uganda Income Tax Act, Cap. 340 | WHT obligations; PAYE |
| BIRDC ERP Vision (`_context/vision.md`) | Strategic goals and Design Covenants |
| BIRDC ERP Feature Register (`_context/features.md`) | Module-level feature descriptions |
| BIRDC ERP Business Rules (`_context/business_rules.md`) | Immutable operational constraints |
| BIRDC ERP Gap Analysis (`_context/gap-analysis.md`) | Open items and unresolved dependencies |

## 1.5 Overview

Section 2 provides a product overview including context, user classes, and constraints. Section 3 contains the detailed functional requirements for F-009 (Procurement & Purchasing) and F-010 (Farmer & Cooperative Management). Section 4 covers non-functional requirements. Section 5 defines the Android Farmer Delivery App requirements. Section 6 lists external interface requirements. Section 7 documents design constraints and open gaps.
