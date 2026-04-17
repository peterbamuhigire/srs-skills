# Section 1: Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for Maduuka Phase 1 -- the Android mobile application and web interface covering all 10 core business management modules. This document is the authoritative reference for the Phase 1 development team at Chwezi Core Systems. It constitutes the formal requirements gate that must be signed off before Phase 1 development begins, per the Water-Scrum-Fall hybrid methodology adopted for this project.

The intended audience is:

- The Phase 1 development team (2-5 engineers at Chwezi Core Systems)
- The project owner (Peter Bamuhigire)
- Quality assurance reviewers performing V&V against this specification
- Future maintainers who inherit this system

This SRS covers **Phase 1 only**. Phase 2 (iOS parity, Restaurant/Bar module, Pharmacy module) and Phase 3 (Hotel/Accommodation, Advanced Inventory, EFRIS) are documented in separate SRS documents produced after Phase 1 sign-off.

## 1.2 Scope

**Product name:** Maduuka

**Vendor:** Chwezi Core Systems (chwezicore.com) -- Peter Bamuhigire, owner and developer

**What Maduuka does:** Maduuka is a mobile-first, multi-tenant SaaS business management platform serving small and medium businesses in Uganda and across Africa. It provides point of sale, inventory management, customer and supplier management, expense tracking, financial account management, sales reporting, HR and payroll, and business health monitoring -- all from a single Android application or web browser, with full offline capability.

**What Phase 1 delivers:**
- Android application (Kotlin/Jetpack Compose) covering all 10 core modules
- Web application (PHP 8.3+, Bootstrap 5/Tabler) covering all 10 core modules
- Single REST API backend serving both clients
- Offline-first operation: all core POS and inventory functions work without internet connectivity
- Multi-tenant architecture: complete data isolation between business accounts

**What this SRS explicitly excludes:**
- iOS application (Phase 2)
- Restaurant/Bar add-on module (Phase 2)
- Pharmacy add-on module (Phase 2)
- Hotel/Accommodation add-on module (Phase 3)
- Advanced Inventory add-on module (Phase 3)
- EFRIS compliance add-on module (Phase 3)
- Any MLM or distributor network functionality -- permanently excluded from all phases
- Any Byoosi.com branding or association -- Maduuka is exclusively a Chwezi Core Systems product

**Business goals this SRS serves** (from _context/vision.md):
1. Acquire 1,000 paying Ugandan business accounts within 12 months of Phase 1 launch.
2. Provide real-time business health visibility on any Android phone.
3. Achieve EFRIS compliance coverage via the Phase 3 add-on (foundation built in Phase 1).
4. Expand to all African markets with configurable currency, language, and mobile money gateways.
5. Displace pirated POS software as the dominant solution in Kampala's downtown business district.

## 1.3 Definitions, Acronyms, and Abbreviations

All terms below follow IEEE Std 610.12-1990 format. The complete glossary is maintained in `_context/glossary.md`.

| Term | Definition |
|---|---|
| EFRIS | Electronic Fiscal Receipting and Invoicing Solution -- URA's real-time digital invoicing system |
| FEFO | First Expiry, First Out -- stock rotation by nearest expiry date |
| FIFO | First In, First Out -- stock rotation by oldest stock first |
| Franchise ID | Unique tenant identifier. Every database record is scoped to franchise_id |
| KDS | Kitchen Display System -- kitchen-facing order display screen |
| KOT | Kitchen Order Ticket -- digital order sent from server to kitchen |
| LST | Local Service Tax -- Ugandan local government employment tax |
| MTN MoMo | MTN Mobile Money -- dominant mobile payment in Uganda |
| NDA | National Drug Authority Uganda |
| NSSF | National Social Security Fund Uganda |
| Offline-First | Full operation without internet; sync when connectivity restores |
| PAYE | Pay As You Earn -- Uganda income tax withheld at source |
| PIF | Project Input Folder -- the _context/ directory |
| POS | Point of Sale -- the transaction processing module |
| PWA | Progressive Web Application -- installable web app with offline capability |
| RBAC | Role-Based Access Control |
| Receipt Gap | Missing receipt number in a POS session sequence |
| RevPAR | Revenue Per Available Room -- hotel occupancy metric |
| SKU | Stock Keeping Unit |
| Tenant | A business account on the Maduuka SaaS platform |
| TIN | Taxpayer Identification Number (Uganda) |
| UOM | Unit of Measure |
| URA | Uganda Revenue Authority |
| Void | Cancellation of a completed POS transaction, with audit record |
| Warehouse | A named storage location within a branch |
| Water-Scrum-Fall | Hybrid methodology: formal requirements gate + iterative sprints |

## 1.4 References

| Reference | Description |
|---|---|
| IEEE Std 830-1998 | IEEE Recommended Practice for Software Requirements Specifications |
| IEEE Std 1233-1998 | IEEE Guide for Developing System Requirements Specifications |
| IEEE Std 610.12-1990 | IEEE Standard Glossary of Software Engineering Terminology |
| IEEE Std 1012-2016 | IEEE Standard for System, Software, and Hardware Verification and Validation |
| ASTM E1340-96 | Standard Guide for Rapid Prototyping of Computerized Systems |
| Uganda DPA 2019 | Data Protection and Privacy Act 2019 (Uganda) |
| EFRIS API Docs | URA EFRIS system-to-system integration specification (Phase 3) |
| maduuka_spec.docx | Maduuka product specification, Peter Bamuhigire, 2026-04-05 |
| docs/plans/2026-04-05-maduuka-design.md | Approved design document, Chwezi Core Systems |
| _context/vision.md | Project vision and business goals |
| _context/features.md | Feature register F-001 through F-015 |
| _context/business_rules.md | Business rules BR-001 through BR-015 |
| _context/tech_stack.md | Technology stack specification |

## 1.5 Document Structure

This SRS is organised as follows:

- **Section 1 (this section):** Purpose, scope, definitions, and references.
- **Section 2:** Overall product description -- product perspective, user characteristics, constraints, and assumptions.
- **Section 3:** External interface requirements -- user interfaces, hardware interfaces, software interfaces, and communications interfaces.
- **Section 4:** Functional requirements -- one subsection per core module (F-001 through F-010), written in stimulus-response format.
- **Section 5:** System constraints -- regulatory, hardware, design, and software attribute constraints.
- **Section 6:** Non-functional requirements -- performance, availability, security, usability, and scalability requirements with measurable thresholds.

Each functional requirement (Section 4) carries a unique identifier in the format **FR-[module]-[sequence]** (e.g., FR-POS-001). Each non-functional requirement (Section 6) carries an identifier in the format **NFR-[category]-[sequence]** (e.g., NFR-PERF-001). These identifiers are used in the Traceability Matrix (Phase 09).
