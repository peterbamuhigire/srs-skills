# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for Phase 4 of the BIRDC ERP system: the Manufacturing & Production module (F-011) and the Quality Control & Laboratory module (F-012). This document is the authoritative requirements baseline for the Phase 4 development effort. It is written for the software development team, the BIRDC Factory Manager (STK-009), the QC Manager (STK-010), and the project consultant.

Every requirement in this document is verifiable per IEEE Std 830-1998 criteria: correct, unambiguous, complete, consistent, ranked, modifiable, and traceable.

## 1.2 Scope

Phase 4 covers 2 modules:

- **F-011 — Manufacturing & Production:** Recipe and Bill of Materials management with version control; circular economy recipes for by-products (biogas, bio-slurry); production order lifecycle management; material requisition and Work In Progress (WIP) accounting; job cards with worker assignment; mass balance verification; production costing; equipment and capacity management; and the Factory Floor Android application.
- **F-012 — Quality Control & Laboratory:** Configurable inspection templates; incoming material inspection with quality grading; in-process QC checkpoints; finished product certification; Certificate of Analysis (CoA) generation for domestic and export markets; Statistical Process Control (SPC); Non-Conformance Reports (NCR); batch quality status management; laboratory equipment calibration tracking; and incubation/maturation tracking for fermented products.

These 2 modules interface directly with Phase 1 (Inventory — F-003), Phase 2 (Financial Accounting — F-005), Phase 3 (Procurement — F-009, Farmer Management — F-010), and Phase 5 (HR — F-013). All GL auto-posting from manufacturing events follows the chart of accounts established in F-005.

This SRS does not cover modules outside Phase 4. Cross-phase interfaces are specified at the API boundary level only.

## 1.3 Definitions, Acronyms, and Abbreviations

The following terms supplement the master glossary in `_context/glossary.md`. All IEEE Std 610.12-1990 software engineering terms apply.

| Term | Definition |
|---|---|
| Bill of Materials (BOM) | The structured list of raw material inputs, quantities, and expected output yield that defines a recipe for a finished product. Also called Recipe in BIRDC operational terminology. |
| Circular Economy Recipe | A specialised BOM type that models by-product production processes: banana peel to biogas, or waste water to bio-slurry fertiliser. |
| CoA | Certificate of Analysis — a formal laboratory document certifying that a finished product batch meets all specified quality parameters, including test results and specification limits. |
| Cp | Process capability index — the ratio of specification width to process spread: $C_p = \frac{USL - LSL}{6\sigma}$. |
| Cpk | Process capability index adjusted for centering: $C_{pk} = \min\left(\frac{USL - \bar{x}}{3\sigma}, \frac{\bar{x} - LSL}{3\sigma}\right)$. |
| FIFO Cost | The cost of raw material consumed, calculated using the First In First Out inventory valuation method, as maintained by F-003. |
| Job Card | A production document specifying step-by-step work instructions for a production order, with worker assignments and quality checkpoints. |
| LSL | Lower Specification Limit — the minimum acceptable value for a quality parameter. |
| Mass Balance | The physical accounting equation: Total Input (kg) = Primary Product Output (kg) + By-product Output (kg) + Scrap/Waste (kg). Enforced by BR-008. |
| NCR | Non-Conformance Report — a QC document raised when a quality failure is detected, with root cause analysis and corrective action tracking. |
| Production Order | A manufacturing instruction document authorising production of a specified quantity of a finished product against a specific recipe version. |
| QC Gate | The system control point at which finished goods transfer to saleable inventory is blocked until QC status equals "Approved" and a CoA is issued. Enforced by BR-004. |
| Recipe Version | An immutable snapshot of a BOM at a specific point in time, referenced by all production orders processed under it. |
| SPC | Statistical Process Control — quality management technique using control charts (X-bar, R-chart) and process capability indices (Cp, Cpk) to detect process instability before product goes out of specification. |
| USL | Upper Specification Limit — the maximum acceptable value for a quality parameter. |
| WIP | Work In Progress — the value of materials issued to the production floor but not yet converted to finished goods. Posted as DR WIP / CR Raw Material Inventory. |

## 1.4 References

| Reference | Standard / Document |
|---|---|
| IEEE Std 830-1998 | IEEE Recommended Practice for Software Requirements Specifications |
| IEEE Std 1233-1998 | IEEE Guide for Developing System Requirements Specifications |
| IEEE Std 610.12-1990 | IEEE Standard Glossary of Software Engineering Terminology |
| ASTM E1340 | Standard Guide for Rapid Identification of Microorganisms and Allergy-Causing Proteins |
| ISO 9001:2015 | Quality Management Systems — Requirements |
| Codex Alimentarius | International food standards referenced for export CoA parameters |
| UNBS EAS 2 | Uganda National Bureau of Standards — labelling and food safety standards |
| BR-004 | QC Gate on Production Output (BIRDC Business Rules) |
| BR-008 | Circular Economy Mass Balance (BIRDC Business Rules) |
| BR-017 | Export CoA Requirements (BIRDC Business Rules) |
| DC-002 | Configuration over code (BIRDC Design Covenant) |
| DC-005 | Offline-first where it matters (BIRDC Design Covenant) |
| DC-007 | Replicable by design (BIRDC Design Covenant) |
| `_context/gap-analysis.md` | BIRDC ERP known information gaps |

## 1.5 Overview

Section 2 describes the overall context of Phase 4 within the BIRDC ERP system. Section 3 specifies all functional requirements for F-011 (Manufacturing & Production) and F-012 (Quality Control & Laboratory). Section 4 specifies non-functional requirements applicable to both modules. Section 5 lists all open context gaps and verification annotations.
