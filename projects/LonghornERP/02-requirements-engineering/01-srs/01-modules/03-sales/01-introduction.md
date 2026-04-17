# Sales Module — Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Sales module of Longhorn ERP, a multi-tenant Software-as-a-Service (SaaS) enterprise resource planning platform developed by Chwezi Core Systems. This document governs the design, implementation, and verification of all sales-cycle capabilities from customer management through cash collection.

All requirements are prospective. Every requirement uses the keyword "shall" to denote a binding obligation, per IEEE Std 830-1998.

## 1.2 Scope

The Sales module covers the full order-to-cash cycle:

- Customer master data and credit management
- Price lists and discount structures
- Quotations and sales orders
- Invoicing (standard, pro-forma, and recurring)
- Delivery notes and proof of delivery
- Sales returns and credit notes
- Payment receipts and debtors aging

The Sales module integrates with the Inventory module (stock reservation and delivery posting), the Accounting module (revenue recognition, accounts receivable), the Platform Integration Layer (EFRIS submission for Uganda-profile tenants), and the Notifications sub-system (overdue alerts, recurring invoice dispatch).

The module does not define point-of-sale (POS) terminal flows. POS requirements are specified in a separate module SRS.

## 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|---|---|
| Credit Note (CN) | A document reducing the amount owed by a customer, issued following a return or billing adjustment. |
| Debtors Aging | A report classifying outstanding customer balances by the number of days elapsed since the invoice due date. |
| Delivery Note (DN) | A document accompanying dispatched goods, confirming items and quantities shipped. |
| EFRIS | Electronic Fiscal Receipting and Invoicing System — Uganda Revenue Authority's mandatory e-invoicing platform. |
| FR | Functional Requirement |
| IFRS | International Financial Reporting Standards |
| NFR | Non-Functional Requirement |
| P95 | 95th percentile response time under normal operating load. |
| Pro-Forma Invoice | A preliminary invoice sent to a customer before goods or services are delivered; does not constitute a financial posting. |
| Sales Order (SO) | A confirmed request from a customer to supply goods or services at agreed terms. |
| SRS | Software Requirements Specification |
| TIN | Taxpayer Identification Number |
| UOM | Unit of Measure |
| VAT | Value Added Tax |

## 1.4 Applicable Standards and References

- IEEE Std 830-1998 — *Recommended Practice for Software Requirements Specifications*
- IEEE Std 1233-1998 — *Guide for Developing System Requirements Specifications*
- IEEE Std 610.12-1990 — *Standard Glossary of Software Engineering Terminology*
- ASTM E1340 — *Standard Guide for Rapid Prototyping of Computerized Systems*
- IFRS 15 — *Revenue from Contracts with Customers*
- Uganda VAT Act (Cap. 349) — VAT obligations on taxable supplies
- Uganda Revenue Authority EFRIS Technical Guide — defers to Platform Integration Layer (FR-INTG series)

## 1.5 Overview of This Document

| Section | Content |
|---|---|
| 02 | Customer Management |
| 03 | Price Lists |
| 04 | Quotations and Sales Orders |
| 05 | Invoicing |
| 06 | Delivery |
| 07 | Returns and Credit Notes |
| 08 | Receipts and Debtors Aging |
| 09 | Non-Functional Requirements |
| 10 | Traceability Matrix |
