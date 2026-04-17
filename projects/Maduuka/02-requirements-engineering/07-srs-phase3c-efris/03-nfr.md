---
title: "SRS Phase 3c -- EFRIS Compliance: Non-Functional Requirements"
project: "Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft -- BLOCKED pending GAP-005"
---

# Section 3: Non-Functional Requirements -- EFRIS Compliance (F-015)

All performance thresholds below apply under normal load, defined as: up to 500 concurrent active POS sessions per tenant, standard cloud infrastructure (minimum 4 vCPU, 8 GB RAM application tier), and a stable internet connection with latency to URA EFRIS servers ≤ 150 ms.

---

## 3.1 Performance

**NFR-EFR-P-001:** The URA EFRIS API call timeout shall be 10 seconds. If the URA EFRIS API does not respond within 10 seconds, the system shall treat the transaction as an offline event and place it in the offline queue per FR-EFR-018. No sale shall be held open awaiting a URA response beyond this 10-second limit.

**NFR-EFR-P-002:** When the URA EFRIS API responds successfully within the 10-second timeout, the FDN and QR code shall be stored and the receipt generation process shall complete within 5 seconds of the successful API response, measured from FDN receipt to receipt availability for print or digital delivery.

**NFR-EFR-P-003:** The offline queue processing engine (FR-EFR-019) shall begin processing queued transactions within 5 seconds of connectivity restoration detection and shall complete the submission of a queue of up to 500 transactions within 30 seconds, assuming each URA API call completes within the 10-second timeout.

**NFR-EFR-P-004:** The EFRIS Status Dashboard counters (FR-EFR-026) shall reflect data that is at most 2 minutes stale under normal conditions. On-demand refresh shall update counters within 5 seconds.

**NFR-EFR-P-005:** The monthly reconciliation calculation (FR-EFR-031) shall complete within 15 seconds at P95 for months containing up to 100,000 transactions.

---

## 3.2 Security

**NFR-EFR-S-001:** All data transmitted between Maduuka and the URA EFRIS API shall be encrypted using TLS 1.2 or higher per URA EFRIS API specifications. Plaintext transmission of transaction data or credentials is prohibited.

**NFR-EFR-S-002:** EFRIS API credentials (client ID and client secret) shall be stored encrypted at rest using AES-256 encryption. They shall never be transmitted to the client (Android or web browser) and shall only be accessed server-side for API call signing.

**NFR-EFR-S-003:** The EFRIS device serial number and TIN shall be stored in the tenant configuration table with field-level encryption. Access to these fields shall require a server-side authorisation check confirming the requesting user belongs to the correct tenant.

**NFR-EFR-S-004:** EFRIS API credentials shall be rotatable by the Business Owner at any time without service interruption. On credential rotation, the system shall immediately use the new credentials for all subsequent API calls and invalidate any cached tokens derived from the old credentials.

---

## 3.3 Data Integrity

**NFR-EFR-DI-001:** Every EFRIS submission record (successful or failed) shall be written to an immutable audit log. No update or delete operation shall be permitted on a confirmed EFRIS submission record. Corrections require new credit note or debit note records referencing the original FDN.

**NFR-EFR-DI-002:** The offline queue shall be stored in a persistent, crash-safe local store (server-side database, not in-memory cache) so that a server restart or power interruption does not result in loss of queued transactions. All queued transactions shall survive a server restart and be submitted on the next connectivity restoration.

**NFR-EFR-DI-003:** Each FDN received from URA shall be stored exactly as received, without truncation or transformation. The QR code payload shall be stored in full to enable exact reproduction on reprinted receipts.

---

## 3.4 Availability

**NFR-EFR-AV-001:** The offline queuing capability shall ensure that the Maduuka POS remains fully operational (sales processing, receipt issuance) regardless of URA EFRIS server availability. A URA server outage shall not block a sale from completing.

**NFR-EFR-AV-002:** The EFRIS module shall share the Maduuka platform availability SLA of 99.5% uptime per calendar month for all non-URA-API-dependent functions (local queue, dashboard, reporting). URA EFRIS API availability is outside Maduuka's control and is not included in this SLA.

---

## 3.5 Compliance

**NFR-EFR-C-001:** All EFRIS submissions shall conform to the URA EFRIS API data format, field lengths, and encoding requirements as documented in the URA EFRIS Integration Guide (version current at accreditation date). Deviations from the URA specification shall be treated as defects of severity Critical.

**NFR-EFR-C-002:** EFRIS submission records and FDN logs shall be retained for a minimum of 10 years to satisfy Uganda Revenue Authority audit requirements under the Income Tax Act and the Tax Procedures Code Act.

**NFR-EFR-C-003:** The system shall support URA EFRIS API version updates without requiring a full platform release, subject to the updated API remaining backward-compatible. Breaking API changes shall be treated as a planned maintenance event with 30 days' notice to subscribers.
