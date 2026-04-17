# 9. Traceability Matrix and Context Gap Register

## 9.1 FR-to-Business-Goal Traceability Matrix

| **Requirement ID** | **Requirement Summary** | **Business Goal** | **Section** |
| --- | --- | --- | --- |
| FR-COOP-001 | Create commodity type record | BG-COOP-01 | 2.2 |
| FR-COOP-002 | Reject duplicate commodity name | BG-COOP-01 | 2.2 |
| FR-COOP-003 | Deactivate commodity without data loss | BG-COOP-01 | 2.2 |
| FR-COOP-004 | Add grade to commodity | BG-COOP-01 | 2.3 |
| FR-COOP-005 | Deactivate grade with batch warning | BG-COOP-01 | 2.3 |
| FR-COOP-006 | Assign grade price to season | BG-COOP-02 | 2.3 |
| FR-COOP-007 | Enforce floor price on intake | BG-COOP-02 | 2.4 |
| FR-COOP-008 | Apply price change prospectively | BG-COOP-02 | 2.4 |
| FR-COOP-009 | Premium price calculation | BG-COOP-02 | 2.4 |
| FR-COOP-010 | Seasonal intake window auto-open/close | BG-COOP-01 | 2.5 |
| FR-COOP-011 | Farmer record creation with NIN validation | BG-COOP-01 | 3.2 |
| FR-COOP-012 | Reject duplicate NIN | BG-COOP-01 | 3.2 |
| FR-COOP-013 | Farmer record audit log | BG-COOP-05 | 3.2 |
| FR-COOP-014 | GPS coordinate validation and storage | BG-COOP-01 | 3.3 |
| FR-COOP-015 | Mobile GPS auto-capture | BG-COOP-01 | 3.3 |
| FR-COOP-016 | Farmer payment method registration | BG-COOP-03 | 3.4 |
| FR-COOP-017 | MoMo phone number prefix validation | BG-COOP-03 | 3.4 |
| FR-COOP-018 | Group creation in hierarchy | BG-COOP-01 | 3.5 |
| FR-COOP-019 | Primary society creation | BG-COOP-01 | 3.5 |
| FR-COOP-020 | Union creation | BG-COOP-01 | 3.5 |
| FR-COOP-021 | Hierarchy tree view with record counts | BG-COOP-01 | 3.5 |
| FR-COOP-022 | KTDA and NAEB jurisdiction configuration | BG-COOP-05 | 3.6 |
| FR-COOP-023 | Activate intake session for season | BG-COOP-01 | 4.2 |
| FR-COOP-024 | Close intake period with supervisor PIN | BG-COOP-02 | 4.2 |
| FR-COOP-025 | Period closure summary generation | BG-COOP-05 | 4.2 |
| FR-COOP-026 | Intake entry recording with gross payment | BG-COOP-01, BG-COOP-02 | 4.3 |
| FR-COOP-027 | Reject zero or negative weight | BG-COOP-01 | 4.3 |
| FR-COOP-028 | Reject intake for unregistered farmer | BG-COOP-01 | 4.3 |
| FR-COOP-029 | Multiple-intake-per-day warning | BG-COOP-02 | 4.3 |
| FR-COOP-030 | RS-232 weighbridge weight capture | BG-COOP-01 | 4.4 |
| FR-COOP-031 | Weighbridge timeout fallback | BG-COOP-01 | 4.4 |
| FR-COOP-032 | Unstable weight rejection | BG-COOP-01 | 4.4 |
| FR-COOP-033 | Weighbridge configuration settings | BG-COOP-01 | 4.4 |
| FR-COOP-034 | Batch posting to Inventory and Accounting | BG-COOP-02 | 4.5 |
| FR-COOP-035 | Block posting of flagged batch entries | BG-COOP-02 | 4.5 |
| FR-COOP-036 | Auto-apply input loan deductions | BG-COOP-02 | 5.3 |
| FR-COOP-037 | Cap deduction at gross payment; carry forward | BG-COOP-02 | 5.3 |
| FR-COOP-038 | Close loan on full repayment | BG-COOP-02 | 5.3 |
| FR-COOP-039 | Register new input loan | BG-COOP-02 | 5.3 |
| FR-COOP-040 | Compute and apply levy deductions | BG-COOP-02 | 5.4 |
| FR-COOP-041 | Separate society and union levy lines | BG-COOP-02 | 5.4 |
| FR-COOP-042 | Levy configuration | BG-COOP-02 | 5.4 |
| FR-COOP-043 | Levy deactivation prospective effect | BG-COOP-02 | 5.4 |
| FR-COOP-044 | Bulk payment batch generation | BG-COOP-03 | 5.5 |
| FR-COOP-045 | Submit payment instructions to MoMo API | BG-COOP-03 | 5.5 |
| FR-COOP-046 | Handle MoMo success and failure callbacks | BG-COOP-03 | 5.5 |
| FR-COOP-047 | MoMo API timeout handling | BG-COOP-03 | 5.5 |
| FR-COOP-048 | Batch reconciliation and journal posting | BG-COOP-03 | 5.5 |
| FR-COOP-049 | Individual farmer statement generation | BG-COOP-05 | 6.2 |
| FR-COOP-050 | PDF farmer statement with cooperative branding | BG-COOP-05 | 6.2 |
| FR-COOP-051 | Bulk statement generation (up to 500 farmers) | BG-COOP-05 | 6.2 |
| FR-COOP-052 | Seasonal summary report | BG-COOP-05 | 6.3 |
| FR-COOP-053 | Seasonal summary Excel export | BG-COOP-05 | 6.3 |
| FR-COOP-054 | Society performance report | BG-COOP-05 | 6.4 |
| FR-COOP-055 | Levy collection report | BG-COOP-05 | 6.4 |
| FR-COOP-056 | Market price with floor price enforcement | BG-COOP-02 | 6.5 |
| FR-COOP-057 | Price history audit trail | BG-COOP-05 | 6.5 |
| FR-COOP-058 | Minimum support price override warning | BG-COOP-02 | 6.5 |
| FR-COOP-059 | Offline mode auto-activation | BG-COOP-04 | 7.2 |
| FR-COOP-060 | 72-hour offline limit warning and lock | BG-COOP-04 | 7.2 |
| FR-COOP-061 | Encrypted local offline entry storage | BG-COOP-04 | 7.3 |
| FR-COOP-062 | Auto-sync on connectivity restoration | BG-COOP-04 | 7.4 |
| FR-COOP-063 | Conflict resolution for duplicate offline entries | BG-COOP-04 | 7.4 |
| FR-COOP-064 | Interrupted sync resumption without duplicates | BG-COOP-04 | 7.4 |
| FR-COOP-065 | Offline database encryption and remote wipe | BG-COOP-04 | 7.5 |

## 9.2 NFR Traceability

| **NFR ID** | **Quality Attribute** | **Linked FR(s)** |
| --- | --- | --- |
| NFR-COOP-001 | Performance — intake entry ≤ 3 s P95 | FR-COOP-026 |
| NFR-COOP-002 | Performance — statement ≤ 5 s P95 | FR-COOP-049 |
| NFR-COOP-003 | Performance — bulk statements ≤ 60 s | FR-COOP-051 |
| NFR-COOP-004 | Performance — hierarchy tree ≤ 3 s | FR-COOP-021 |
| NFR-COOP-005 | Performance — MoMo batch ≥ 10 req/s | FR-COOP-045 |
| NFR-COOP-006 | Availability — ≥ 99.5% monthly uptime | All FRs |
| NFR-COOP-007 | Reliability — zero offline data loss | FR-COOP-061 to FR-COOP-064 |
| NFR-COOP-008 | Reliability — RS-232 recovery ≤ 10 s | FR-COOP-030, FR-COOP-031 |
| NFR-COOP-009 | Security — PII encryption at rest (AES-256) | FR-COOP-011, FR-COOP-016 |
| NFR-COOP-010 | Security — JWT authentication on all endpoints | All FRs |
| NFR-COOP-011 | Security — RBAC permission boundaries | All FRs |
| NFR-COOP-012 | Security — mobile offline DB encryption | FR-COOP-061, FR-COOP-065 |
| NFR-COOP-013 | Compliance — Uganda Data Protection Act, 2019 | FR-COOP-011 |
| NFR-COOP-014 | Compliance — 7-year data retention | FR-COOP-026, FR-COOP-048 |
| NFR-COOP-015 | Compliance — KTDA report format | FR-COOP-022 |
| NFR-COOP-016 | Scalability — 100,000 farmers per tenant | FR-COOP-011 to FR-COOP-022 |
| NFR-COOP-017 | Scalability — 5,000-record payment batch | FR-COOP-044, FR-COOP-045 |
| NFR-COOP-018 | Usability — 90-second intake task time | FR-COOP-026 |
| NFR-COOP-019 | Usability — English and Luganda UI | All mobile FRs |
| NFR-COOP-020 | Maintainability — pluggable weighbridge driver | FR-COOP-030, FR-COOP-033 |

## 9.3 Context Gap Register

The following gaps were identified during requirement authoring. Each gap must be resolved by the consultant before the corresponding requirements are finalised and implementation begins.

| **Gap ID** | **Topic** | **Blocking Requirement(s)** | **Action Required** |
| --- | --- | --- | --- |
| CG-COOP-001 | Maximum overlapping active seasons per commodity per tenant | FR-COOP-010 | Confirm with product owner whether concurrent seasons per commodity are permitted. |
| CG-COOP-002 | NIRA real-time NIN verification API availability | FR-COOP-011 | Confirm API availability, authentication method, and SLA; update FR-COOP-011 accordingly. |
| CG-COOP-003 | Specific weighbridge hardware models at collection centres | FR-COOP-030, FR-COOP-032, FR-COOP-033 | Obtain make/model list from cooperative partners; validate RS-232 output format and stability flag. |
| CG-COOP-004 | MTN Mobile Money Uganda API version and authentication | FR-COOP-045, FR-COOP-046, FR-COOP-047 | Obtain MTN API documentation; confirm OAuth 2.0 or API key; update integration contract. |
| CG-COOP-005 | Airtel Money Uganda API sandbox availability | FR-COOP-045, FR-COOP-046 | Confirm sandbox access with Airtel for integration testing. |
| CG-COOP-006 | Float management pre-disbursement gate | FR-COOP-044 | Confirm whether the system checks float balance before initiating the batch or relies on provider error responses only. |
| CG-COOP-007 | UCDA minimum support price API or manual entry | FR-COOP-058 | Confirm whether UCDA publishes a machine-readable price schedule or the administrator enters it manually. |
| CG-COOP-008 | KTDA green leaf and bonus payment cycle rules | FR-COOP-022, NFR-COOP-015 | Obtain KTDA payment cycle specifications; confirm whether these are configurable per tenant. |
| CG-COOP-009 | NAEB export levy rate schedule | FR-COOP-022, FR-COOP-042 | Obtain current NAEB levy percentages for coffee and tea from the Rwanda tenant contact. |
| CG-COOP-010 | Target mobile platform(s) for offline mode | FR-COOP-059 to FR-COOP-065 | Confirm Android-only, iOS-only, or both; specify minimum OS versions and storage requirements. |
| CG-COOP-011 | Minimum device hardware specification for offline officers | FR-COOP-061 | Confirm minimum Android API level (or iOS version) and available device storage for 72-hour data footprint. |
| CG-COOP-012 | Luganda translation strings | NFR-COOP-019 | Confirm whether Chwezi Core provides translations or the cooperative society supplies them. |
| CG-COOP-013 | KTDA Factory Management System report field layout | NFR-COOP-015 | Obtain the KTDA FMS file format specification (CSV/PDF/XML) and field layout for the monthly payment advice report. |
