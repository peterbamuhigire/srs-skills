---
title: "SRS Phase 3c -- EFRIS Compliance: Design Constraints"
project: "Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 4: Design Constraints -- EFRIS Compliance (F-015)

## 4.1 Regulatory Constraint: URA Accreditation (GAP-005)

**DC-EFR-001:** All EFRIS API integration components -- including fiscal invoice submission, FDN retrieval, credit note submission, debit note submission, and offline queue processing -- are **[BLOCKED: GAP-005]** and shall not be deployed to a production environment until the following conditions are all met:

1. Maduuka is registered and approved by URA as a system-to-system EFRIS integration partner.
2. URA has issued production API credentials (client ID, client secret, and device serial number range).
3. End-to-end integration testing against the URA sandbox environment is complete with a zero-defect result on all mandatory EFRIS transaction types (B2C, B2B, B2G, credit note, debit note).
4. URA has issued a written accreditation confirmation.

Design, data modelling, UI wireframing, and offline-simulation testing using the mock FDN generator may proceed before GAP-005 is resolved.

## 4.2 Opt-In Constraint: Not Mandatory for All Subscribers

**DC-EFR-002:** The EFRIS Compliance module (F-015) shall be available exclusively as an opt-in add-on. No Maduuka subscriber shall have EFRIS submission logic activated without explicitly enabling the module and providing valid URA credentials (FR-EFR-001). Subscribers who do not activate F-015 shall experience no change to their POS or invoicing behaviour.

**DC-EFR-003:** The EFRIS module shall be available only to tenants whose configured functional currency is Uganda Shillings (UGX) or who are explicitly flagged as Uganda-jurisdiction tenants by the platform administrator. Tenants in other jurisdictions shall not be offered EFRIS activation, as the module is specific to URA Uganda.

## 4.3 URA API Dependency Constraint

**DC-EFR-004:** The Maduuka system shall not implement a client-side workaround that issues self-generated FDNs or fabricates URA QR codes. All FDNs and QR codes displayed on receipts and invoices must be sourced from a genuine URA EFRIS API response or from the offline queue confirmed upon successful URA submission after connectivity restoration.

**DC-EFR-005:** The EFRIS integration shall support only the URA EFRIS API. Integration with any third-party EFRIS middleware or proxy service that is not directly accredited by URA is prohibited unless URA explicitly authorises such proxies in its accreditation terms.

## 4.4 Data Residency Constraint

**DC-EFR-006:** All EFRIS submission records, FDNs, QR code payloads, and URA API credentials shall be stored on infrastructure located within Uganda or in a jurisdiction approved by the Uganda Data Protection Office under the Data Protection and Privacy Act 2019 (GAP-002). No EFRIS fiscal data shall be stored on infrastructure outside an approved jurisdiction without written DPO authorisation.

## 4.5 Receipt Constraint

**DC-EFR-007:** When EFRIS is active for a tenant, every receipt and invoice template -- including 80mm thermal print, A4 PDF invoice, WhatsApp PDF, and SMS summary -- shall include the FDN as a mandatory field. Receipts without an FDN shall be issued only when the transaction is in `PENDING_EFRIS` or `EFRIS_FAILED` status, and in those cases the receipt shall carry a clearly visible status label (e.g., `EFRIS STATUS: PENDING`) that distinguishes it from a confirmed fiscal receipt.
