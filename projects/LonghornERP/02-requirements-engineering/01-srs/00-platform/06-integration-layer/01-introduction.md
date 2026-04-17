# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Integration Layer of Longhorn ERP. The Integration Layer provides all outbound and inbound communication between Longhorn ERP and external regulatory authorities, payment networks, and consumer systems. This document is authoritative for the design, development, testing, and audit of the following integration domains:

- Uganda Revenue Authority Electronic Fiscal Receipting and Invoicing System (EFRIS)
- Mobile Money payment networks: MTN Mobile Money (MoMo), Airtel Money, and M-Pesa
- Kenya Revenue Authority electronic Tax Invoice Management System (KRA eTIMS)
- National Social Security Fund (NSSF) payroll contribution submission
- Outbound webhook and REST event notification framework

## 1.2 Scope

The Integration Layer is a platform-level subsystem of Longhorn ERP. It is not a standalone product. Requirements in this document govern the behaviour of the integration subsystem under all localisation profiles and across all tenant configurations.

The Integration Layer does not implement business logic belonging to the Sales, Procurement, HR & Payroll, or Accounting modules. It provides transport, authentication, queuing, retry, and callback services that those modules consume.

## 1.3 Definitions

The following terms are used throughout this document. All definitions conform to IEEE Std 610.12-1990 unless otherwise stated.

| Term | Definition |
|---|---|
| Callback | An inbound HTTP POST request delivered by a third-party service to a Longhorn ERP endpoint, carrying a transaction status update. |
| Dead-Letter Queue (DLQ) | A storage queue for payloads that have exhausted all retry attempts without successful delivery. |
| EFRIS | Electronic Fiscal Receipting and Invoicing System — Uganda Revenue Authority's mandatory e-invoicing platform. |
| Exponential Backoff | A retry timing strategy in which the wait interval between successive attempts increases geometrically (e.g., 30 s, 60 s, 120 s). |
| Fiscal Document Number | A unique identifier returned by EFRIS or KRA eTIMS upon successful invoice submission, used as proof of fiscal registration. |
| HMAC-SHA256 | Hash-based Message Authentication Code using the SHA-256 algorithm — used to sign outbound webhook payloads. |
| Integration Plugin | A self-contained software component that implements the interface contract for a single third-party provider (e.g., MTN MoMo plugin). |
| KRA eTIMS | Kenya Revenue Authority electronic Tax Invoice Management System — Kenya's mandatory fiscal invoicing API. |
| Localisation Profile | A tenant-level configuration flag (e.g., `UG`, `KE`) that activates or deactivates country-specific compliance integrations. |
| MoMo | MTN Mobile Money — a mobile payment service operated by MTN Group. |
| NSSF | National Social Security Fund — a statutory social insurance body operating in Uganda and Kenya. |
| Offline Queue | A durable, persistent queue used to store outbound integration payloads when the target external service is unavailable. |
| QR Code | A machine-readable optical label returned by EFRIS and embedded in a printed fiscal invoice. |
| Tenant | A single organisational customer of the Longhorn ERP SaaS platform, operating within an isolated multi-tenant environment. |
| Webhook | An outbound HTTP POST notification sent by Longhorn ERP to a tenant-registered URL upon occurrence of a defined system event. |

## 1.4 Acronyms

| Acronym | Expansion |
|---|---|
| AES | Advanced Encryption Standard |
| API | Application Programming Interface |
| DLQ | Dead-Letter Queue |
| EFRIS | Electronic Fiscal Receipting and Invoicing System |
| ERP | Enterprise Resource Planning |
| HMAC | Hash-based Message Authentication Code |
| HTTP | Hypertext Transfer Protocol |
| JSON | JavaScript Object Notation |
| KRA | Kenya Revenue Authority |
| MoMo | Mobile Money |
| NSSF | National Social Security Fund |
| P95 | 95th percentile of a latency distribution |
| REST | Representational State Transfer |
| SFTP | SSH File Transfer Protocol |
| SRS | Software Requirements Specification |
| TLS | Transport Layer Security |
| URA | Uganda Revenue Authority |
| UTC | Coordinated Universal Time |

## 1.5 Applicable Standards and References

- IEEE Std 830-1998 — *Recommended Practice for Software Requirements Specifications*
- IEEE Std 1233-1998 — *Guide for Developing System Requirements Specifications*
- IEEE Std 610.12-1990 — *Standard Glossary of Software Engineering Terminology*
- ASTM E1340-96 — *Standard Guide for Rapid Prototyping of Computerized Systems*
- PRIME Methodology (Kodukula & Vinueza, 2024) — skill execution workflow for AI-assisted SRS generation
- Uganda Revenue Authority EFRIS Integration Guide (version TBC) — `[CONTEXT-GAP: GAP-001 — EFRIS API endpoint and auth not confirmed]`
- Kenya Revenue Authority eTIMS API Documentation (version TBC) — `[CONTEXT-GAP: GAP-009 — KRA eTIMS API specifics not confirmed]`
- MTN MoMo Developer API Documentation — https://momodeveloper.mtn.com
- Airtel Money Africa API Documentation
- Safaricom M-Pesa Daraja API Documentation — https://developer.safaricom.co.ke
- NSSF Uganda / NSSF Kenya Contribution Submission Specification (version TBC) — `[CONTEXT-GAP: NSSF API format not confirmed]`

## 1.6 Document Organisation

This document is structured as follows:

- Section 2 covers EFRIS e-invoicing integration requirements.
- Section 3 covers Mobile Money payment integration requirements.
- Section 4 covers KRA eTIMS fiscal integration requirements.
- Section 5 covers NSSF payroll contribution submission requirements.
- Section 6 covers the outbound webhook and REST event notification framework.
- Section 7 defines non-functional requirements for the Integration Layer.
- Section 8 provides the traceability matrix.
