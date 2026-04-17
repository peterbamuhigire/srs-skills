# Introduction to the Point of Sale Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Point of Sale (POS) module of Longhorn ERP. It is addressed to Chwezi Core Systems developers, QA engineers, and business stakeholders who require a verifiable, auditable specification prior to implementation.

## 1.2 Business Goals

| ID | Goal |
|---|---|
| BG-001 | Revenue capture: maximise transaction speed, support split payments and credit sales to reduce queue abandonment. |
| BG-002 | Cash control: enforce till discipline through opening floats, cash-in/out records, end-of-shift reconciliation, and variance accountability. |
| BG-003 | Regulatory compliance: generate VAT-compliant fiscal receipts and submit transaction data to the Uganda Revenue Authority Electronic Fiscal Receipting and Invoicing System (EFRIS). |
| BG-004 | Operational resilience: maintain transaction processing capability during internet outages for up to 8 hours without data loss. |

## 1.3 Scope

The POS module covers terminal lifecycle management, sales transaction processing, multi-method payment handling, till management, offline operation, and fiscal receipt generation. It integrates with the Inventory, Accounts Receivable, and General Ledger modules of Longhorn ERP.

This SRS does not cover hardware procurement, physical terminal installation, or point-of-sale hardware driver development. Payment card hardware integration (card reader firmware) is out of scope for version 1.0; card payments are captured via manual entry only.

## 1.4 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|---|---|
| EFRIS | Electronic Fiscal Receipting and Invoicing System — Uganda Revenue Authority's mandatory fiscal receipt platform. |
| Float | The opening cash amount placed in a till at the start of a cashier shift. |
| GS1 | Global Standards 1 — international organisation that administers barcode standards including EAN-13 and UPC-A used for retail item scanning. |
| MTN MoMo | MTN Mobile Money — mobile payment service operated by MTN Uganda. |
| POS | Point of Sale — the physical or virtual terminal at which a retail transaction is completed. |
| Super Admin | A system user role with authority to activate, deactivate, and configure POS terminals. |
| Terminal Session | The period between a cashier opening a terminal (shift start) and closing it (shift end); all transactions are recorded against the session. |
| Till | The cash drawer and its associated accounting record for a terminal session. |
| URA | Uganda Revenue Authority — the government body responsible for tax administration. |
| VAT | Value Added Tax — tax levied on retail transactions at the rate defined in the Uganda VAT Act. |
| X-Report | An intra-shift summary report of running till totals; does not close the shift. |
| Z-Report | An end-of-shift summary report of all till totals; triggers till closure. |

## 1.5 Applicable Standards and References

- IEEE Std 830-1998 — *Recommended Practice for Software Requirements Specifications*
- IEEE Std 1233-1998 — *Guide for Developing System Requirements Specifications*
- IEEE Std 610.12-1990 — *Standard Glossary of Software Engineering Terminology*
- ASTM E1340-96 — *Standard Guide for Rapid Prototyping of Computerized Systems*
- Uganda VAT Act (Cap. 349) — VAT obligations on retail sales transactions
- Uganda Revenue Authority EFRIS Technical Integration Guide — fiscal receipt submission requirements
- GS1 General Specifications — barcode symbology and data structure standards for retail scanning

## 1.6 Document Overview

| Section | Content |
|---|---|
| 02 | Terminal Management requirements (FR-POS-001 to FR-POS-012) |
| 03 | Sales Transaction requirements (FR-POS-013 to FR-POS-032) |
| 04 | Payment Handling requirements (FR-POS-033 to FR-POS-047) |
| 05 | Till Management requirements (FR-POS-048 to FR-POS-057) |
| 06 | Offline Mode requirements (FR-POS-058 to FR-POS-067) |
| 07 | Non-Functional Requirements (NFR-POS-001 to NFR-POS-005) |
| 08 | Traceability Matrix |
