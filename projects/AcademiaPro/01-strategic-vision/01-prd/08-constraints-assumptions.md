# Product Requirements Document — Academia Pro

## Constraints and Assumptions

### Design Constraints

**DC-001 — Uganda-First Calendar:** The system shall support exactly 3 terms per academic year. Monthly billing cycles are not supported. All fee structures, attendance summaries, report cards, and EMIS data are term-based. This constraint is derived from the Uganda academic calendar mandated by MoES and applies to all Uganda-profile schools; it does not apply to schools under country profiles with different calendar models.

**DC-002 — Design Covenant:** Every module must be operable by a single administrator who has watched that module's training video. No module may require an IT professional for day-to-day operation. This constraint is binding and overrides any design decision that introduces complexity visible to the daily operator.

**DC-003 — UNEB Grade Computation Accuracy:** The UNEB grading engine shall produce results that match UNEB published grade boundary tables with 100% accuracy. Any deviation — however small — is a critical defect, not a product limitation. This accuracy is non-negotiable because erroneous grades affect student progression and UNEB candidate registration.

**DC-004 — Multi-Tenant Isolation:** Row-level tenant isolation (`tenant_id` enforced at the Repository layer) is non-negotiable. Under no circumstances may code be written that accesses tenant data without the `tenant_id` filter, except for global identity tables (`global_students`, `student_identifiers`) which are subject to service-layer access control. Violation of this constraint is a critical security defect.

**DC-005 — SchoolPay Webhook Reliability:** SchoolPay webhooks are fire-and-forget with no retry mechanism. The nightly polling fallback job (`SyncSchoolTransactions` + `SchoolRangeTransactions`) is not optional — it is a mandatory component of the reconciliation architecture. The system cannot rely on webhook delivery alone.

**DC-006 — BoU Licensing for Direct Mobile Money:** Direct MTN MoMo and Airtel Money collection (Phase 3) requires a Bank of Uganda Payment Systems Operator licence. Phase 3 development shall not proceed until the BoU pre-application process is engaged and the licensing timeline is confirmed. Phase 1 and 2 payments operate exclusively under SchoolPay's BoU licence.

**DC-007 — PDPO Health Data Classification:** Student health records are special category data under the Uganda Data Protection and Privacy Act 2019. The Phase 7 health module shall implement access controls such that no user other than the treating nurse/doctor, the student, and the linked parent can access individual health records without an explicit emergency override logged with user, timestamp, and reason. This constraint cannot be relaxed by school configuration.

**DC-008 — No Cardholder Data Storage:** All card payment processing for Visa/Mastercard (Phase 4) shall be delegated entirely to Flutterwave. Academia Pro servers shall store tokenised references only. Storing cardholder data would bring Academia Pro into PCI-DSS scope for card data storage, which is explicitly out of scope.

**DC-009 — Android-First Mobile Priority:** The Android mobile applications (Phases 3–6) take priority over iOS (Phases 9–10). The dominant smartphone category among Uganda teachers and parents is Android budget devices (2GB RAM, Android 10+, 360 × 800 px screen). All mobile features must be fully validated on this hardware profile before iOS development begins.

**DC-010 — Offline PWA Requirement:** The web frontend must support offline operation for attendance entry and mark entry via Workbox service workers. Schools with intermittent connectivity shall not lose data when the connection drops. Data written offline shall sync automatically on reconnect.

**DC-011 — Single Active Enrolment Rule:** A student cannot hold two active enrolments at two different Academia Pro schools simultaneously. This constraint is enforced at the global identity service layer. It prevents duplicate payment records and EMIS data anomalies.

**DC-012 — Receipt Immutability:** Fee receipts shall be sequentially numbered per school and cannot be deleted by any user role, including Super Admin. A voided payment is recorded as a separate reversal transaction referencing the original receipt number. This constraint is required for financial audit trail integrity.

---

### Technical Constraints

**TC-001 — PHP 8.2+ / Laravel 11:** The backend is constrained to PHP 8.2 or higher and Laravel 11. No other backend language or framework is within scope. The Service/Repository pattern is mandatory; direct Eloquent model access in business logic is prohibited.

**TC-002 — MySQL 8.x Strict Mode:** The database engine is MySQL 8.x InnoDB in strict mode with utf8mb4 charset. Any data type shortcut that would be silently permitted in non-strict mode shall cause a validation error in production. This eliminates a class of data integrity bugs.

**TC-003 — PHPStan Level 8:** All PHP code shall pass PHPStan level 8 static analysis with zero errors before any pull request is merged. This constraint is enforced in CI and is not waivable for deadline reasons.

**TC-004 — TLS 1.3 Minimum:** All data in transit shall use TLS 1.3. TLS 1.2 is permitted only for the USSD integration (Phase 11) where the Africa's Talking USSD API requires it. TLS 1.0 and 1.1 are prohibited.

**TC-005 — AES-256 at Rest:** All PII fields and database volumes shall be encrypted using AES-256. This applies to all environments including staging.

**TC-006 — SchoolPay MD5 Hash Constraint:** SchoolPay's API uses MD5 hash-based request signing. MD5 is computationally weak by modern cryptographic standards but is SchoolPay's mandated scheme. To compensate, all outbound calls to SchoolPay shall enforce TLS 1.3. The MD5 implementation shall be server-side only; the `apiPassword` shall never appear in source code or client-side code.

---

### Regulatory Constraints

**RC-001 — PDPO 2019:** All processing of student personal data shall comply with the Uganda Data Protection and Privacy Act 2019. Lawful basis is contractual necessity for enrolled students and parental consent for students under 18. A full compliance specification is maintained in `_context/gap-analysis.md` (HIGH-008).

**RC-002 — Uganda Copyright Act 2006:** Academia Pro is registered with URSB. All developers engaged on the platform shall sign IP assignment agreements before commencing work.

**RC-003 — UNEB Format Compliance:** Candidate registration data exports shall conform to UNEB-specified formats. Any change to the UNEB format by UNEB requires an update to the export module before the next exam registration cycle.

**RC-004 — MoES EMIS Format Compliance:** EMIS exports shall conform to MoES-specified formats. Format changes by MoES require an update before the next EMIS submission deadline.

---

### Assumptions

**A-001:** SchoolPay will provide sandbox credentials and a signed merchant agreement before Phase 1 development begins. If sandbox access is not available before development starts, the SchoolPay integration will be built against the documented API specification with mocked responses, pending certification in Phase 8.

**A-002:** UNEB will provide sample mark sheets with verified correct grade outputs for PLE, UCE, and UACE cohorts before Phase 8 grading validation begins. If UNEB-supplied samples are not available, validation will use historical mark sheets verified by a qualified Uganda examinations specialist.

**A-003:** MoES will validate the EMIS export format before Phase 8 launch. If MoES does not provide a validator, validation will be performed by cross-referencing the current MoES EMIS data collection guide and verified by a field officer contact.

**A-004:** The Bank of Uganda Payment Systems Operator licence application process for direct mobile money (Phase 3) will be initiated no later than the start of Phase 2. If the licence is not granted before Phase 3 development completes, direct MoMo integration will be deferred to Phase 4 and the Phase 3 scope will be limited to SchoolPay + Flutterwave card payments.

**A-005:** Africa's Talking will maintain their Uganda SMS sender ID registration throughout the product lifecycle. SMS delivery rates to Uganda mobile numbers will be ≥ 90% as advertised by Africa's Talking SLA.

**A-006:** Uganda schools using SchoolPay assign each student a permanent `studentPaymentCode` before paying any fees. This assumption underlies the SchoolPay reconciliation architecture. Schools that have not assigned payment codes require a one-time setup step before SchoolPay integration is functional.

**A-007:** The minimum supported Android version for the native apps is Android 10 (API level 29). This covers the dominant budget phone segment in Uganda (Tecno, Samsung Galaxy A-series entry models, Itel). Devices below Android 10 will be served by the PWA web portal only.

**A-008:** School internet connectivity is intermittent but present for at least 50% of the school day. The offline PWA covers the gap for attendance and mark entry. Fee payment confirmation and report card PDF generation require connectivity and are not expected to function fully offline.

**A-009:** Chwezi Core Systems will engage at least 3 pilot schools before Phase 9 live trials to validate onboarding flow and training video effectiveness. Pilot schools will provide structured feedback that informs Phase 9 live trial preparation.

**A-010:** The pricing model (subscription tiers, per-school fees, optional module add-on pricing) will be defined and validated in `_context/pricing.md` before Phase 9 begins. The PRD does not specify pricing — this is a commercial decision for the product owner.
