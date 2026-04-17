# 8. Non-Functional Requirements

## 8.1 Performance

**NFR-COOP-001** — Intake entry submission (FR-COOP-026) shall complete — from the officer tapping "Save" to the system displaying the confirmed gross payment — within 3 seconds at the 95th percentile (P95) under normal operating load, defined as ≤ 50 concurrent intake sessions per tenant.

*Measurement:* Load test with 50 concurrent virtual users each submitting one intake entry per 10 seconds; P95 response time ≤ 3,000 ms.

**NFR-COOP-002** — Farmer statement generation for a single farmer (FR-COOP-049) shall complete within 5 seconds at P95 for a season containing ≤ 500 intake entries for that farmer.

*Measurement:* Automated test generating a statement for a farmer with 500 entries; P95 ≤ 5,000 ms over 20 test runs.

**NFR-COOP-003** — Bulk farmer statement generation (FR-COOP-051) shall complete within 60 seconds for up to 500 farmers in a society, measured from request initiation to the file download being available.

*Measurement:* Test with a society of 500 farmers; generation completes and the download link appears within 60 seconds.

**NFR-COOP-004** — The hierarchy tree view (FR-COOP-021) shall render within 3 seconds at P95 for a hierarchy containing up to 10,000 farmer records.

*Measurement:* Performance test with a seeded hierarchy of 10,000 farmers; P95 first meaningful paint ≤ 3,000 ms.

**NFR-COOP-005** — Mobile money bulk payment API calls (FR-COOP-045) shall be submitted to the provider at a rate of ≥ 10 payment requests per second to avoid provider rate-limit throttling, with the full batch of 500 payments submitted within 50 seconds.

*Measurement:* Batch of 500 payments: all API calls submitted within 50 seconds (500 ÷ 10 = 50 s).

## 8.2 Reliability and Availability

**NFR-COOP-006** — The Cooperative Procurement module shall achieve a monthly uptime of ≥ 99.5% (scheduled maintenance windows excluded), equivalent to a maximum of 3.65 hours of unplanned downtime per month.

*Measurement:* Uptime monitoring via synthetic health check at 60-second intervals; SLA reported monthly.

**NFR-COOP-007** — The offline sync engine (Section 7) shall achieve zero data loss for any intake entry recorded while offline, validated by comparing the count of entries in the device's local queue at sync-start with the count of entries confirmed on the server at sync-end.

*Measurement:* End-to-end sync test with 200 offline entries across 3 simulated connectivity interruptions; server receives exactly 200 unique entries.

**NFR-COOP-008** — The weighbridge RS-232 integration (Section 4.4) shall recover from a serial port disconnect and reconnect (cable pull-and-re-insert) within 10 seconds without requiring the collection officer to restart the application.

*Measurement:* Physical RS-232 disconnect and reconnect during an active intake session; the capture button resumes functioning within 10 seconds.

## 8.3 Security

**NFR-COOP-009** — All farmer PII (personally identifiable information) stored in the database — including NIN, phone number, bank account number, and GPS coordinates — shall be encrypted at rest using AES-256 with tenant-specific encryption keys managed by the platform's key management service.

*Measurement:* Database column-level encryption audit; raw database dump shall contain no plaintext NIN or phone number values. Verified by extracting a raw row and confirming the NIN field is ciphertext.

**NFR-COOP-010** — All API endpoints for the Cooperative Procurement module shall require a valid JSON Web Token (JWT) bearing the authenticated user's tenant ID and role claims; requests without a valid JWT shall return HTTP 401 within 200 ms.

*Measurement:* Automated security test sending requests without a token, with an expired token, and with a token from a different tenant; all three cases return HTTP 401.

**NFR-COOP-011** — Role-based access control shall enforce the following minimum permission boundaries:

| **Role** | **Permitted Actions** |
| --- | --- |
| Collection Officer | Record intake, view own entries |
| Society Manager | View all society entries, approve batches, generate statements |
| Payment Officer | Initiate and manage payment batches |
| Administrator | Full configuration, user management, price management |
| Auditor | Read-only access to all records and audit logs |

*Measurement:* RBAC penetration test: each role attempts an action outside its boundary; all out-of-boundary attempts return HTTP 403.

**NFR-COOP-012** — The mobile application's local offline database shall be encrypted with AES-256 (FR-COOP-065); the encryption key shall never be stored in plaintext on the device file system or in application logs.

*Measurement:* Static analysis of the mobile app binary and log output; no plaintext key material is found.

## 8.4 Compliance and Regulatory

**NFR-COOP-013** — Farmer NIN data handling shall comply with Uganda's Data Protection and Privacy Act, 2019, including: purpose limitation (NIN used only for farmer identity verification), data minimisation (only NIN and not the full NIRA record is stored), and the right of access (a farmer may request a printout of their stored personal data within 72 hours of the request).

*Measurement:* Compliance checklist audit against the Act; the data access request feature is demonstrated to retrieve and print a farmer's stored data.

**NFR-COOP-014** — Payment records, intake entries, and farmer ledger entries shall be retained for a minimum of 7 years from the close of the season in which they were created, in compliance with Uganda's Income Tax Act retention requirements.

*Measurement:* Data retention policy configuration verified in the platform's data lifecycle settings; records aged > 7 years are the only records eligible for archival deletion.

**NFR-COOP-015** — For Kenya tenants, the module shall generate KTDA-compatible payment advice reports in the format required by the KTDA Factory Management System for monthly submission. [CONTEXT-GAP: KTDA Factory Management System report format specification — obtain the field layout and file format (CSV/PDF/XML) required for submission.]

## 8.5 Scalability

**NFR-COOP-016** — The module shall support up to 100,000 registered farmers per tenant without degradation of intake entry P95 response time below the threshold defined in NFR-COOP-001.

*Measurement:* Load test with a seeded database of 100,000 farmers; intake entry P95 ≤ 3,000 ms.

**NFR-COOP-017** — A single payment batch shall support up to 5,000 farmer payment records without exceeding the submission time defined in NFR-COOP-005 (scaled proportionally: 5,000 payments ≤ 500 seconds).

*Measurement:* Batch of 5,000 payments submitted; all API calls dispatched within 500 seconds.

## 8.6 Usability

**NFR-COOP-018** — A collection officer with no prior system training shall be able to record a complete intake entry (select farmer, select commodity/grade, capture weight, save) within 90 seconds after a 30-minute onboarding session on the mobile application.

*Measurement:* Usability test with 5 representative collection officers; median task completion time ≤ 90 seconds on the third attempt.

**NFR-COOP-019** — All user-facing error messages in the mobile application shall be available in English and Luganda; the language is set per user profile. [CONTEXT-GAP: Luganda translation strings — confirm whether Chwezi Core provides translations or the cooperative society supplies them.]

## 8.7 Maintainability

**NFR-COOP-020** — The RS-232 weighbridge integration driver (Section 4.4) shall be implemented as a configurable plugin; adding support for a new weighbridge model shall require only a new parse-pattern configuration entry and shall not require code changes to the core intake recording flow.

*Measurement:* A new weighbridge model is integrated by adding a parse pattern to the configuration screen; no source code deployment is required; the new device captures weight correctly.
