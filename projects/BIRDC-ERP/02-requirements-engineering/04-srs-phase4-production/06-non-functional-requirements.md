# 5. Non-Functional Requirements — Phase 4

## 5.1 Performance Requirements

**NFR-P-001**
*When* a user submits a production order confirmation, *the system shall* complete all validation checks (material availability, recipe version lock) and return a success or failure response within 2 seconds at P95 under normal load (defined as fewer than 50 concurrent web users).

*Test oracle:* Load test with 50 concurrent users submitting production order confirmations shows P95 response time ≤ 2,000 ms; measured using JMeter or equivalent.

---

**NFR-P-002**
*When* the Factory Floor App performs a background sync of offline records after reconnection, *the system shall* complete the sync of up to 200 queued records within 60 seconds on a mobile connection with bandwidth ≥ 1 Mbps.

*Test oracle:* 200 queued records (operations, completions, attendance) transmitted over a simulated 1 Mbps connection complete sync within 60 seconds; confirmed by WorkManager completion callback timestamp.

---

**NFR-P-003**
*When* the SPC chart for a parameter is requested, *the system shall* render the X-bar and R-charts with up to 250 data points within 3 seconds at P95, with calculations performed server-side.

*Test oracle:* SPC chart request with 250 data points returns a fully rendered ApexCharts configuration (including UCL, LCL, centre line values) within 3 seconds; tested under normal load.

---

**NFR-P-004**
*When* a CoA PDF is generated, *the system shall* complete PDF generation using mPDF within 5 seconds per document under normal load (fewer than 10 concurrent CoA generation requests).

*Test oracle:* 10 simultaneous CoA generation requests each complete within 5 seconds; validated via timed HTTP response measurement.

---

## 5.2 Reliability Requirements

**NFR-R-001**
The manufacturing and QC modules shall maintain a minimum availability of 99% during the factory operating hours of 06:00 to 22:00 EAT (East Africa Time), Monday to Saturday, measured monthly; planned maintenance windows outside these hours are excluded from availability calculation.

*Test oracle:* Monthly uptime log for operating hours shows ≥ 99% availability (maximum 72 minutes downtime per month during operating hours).

---

**NFR-R-002**
*When* the Factory Floor App's WorkManager sync fails due to a network error, *the system shall* retry the sync up to 5 times with exponential backoff (30 seconds, 1 minute, 2 minutes, 4 minutes, 8 minutes) before notifying the IT Administrator of a persistent sync failure.

*Test oracle:* Simulating a network failure after the first sync attempt triggers 5 retry attempts at the specified intervals before the IT Administrator alert is generated.

---

## 5.3 Security Requirements

**NFR-S-001**
All QC inspection results, CoA documents, and NCR records shall be stored in immutable audit tables (as defined in the tech stack security architecture); any modification to a committed inspection result shall require a correction entry with the original value, new value, user ID, and justification text — direct row update is prohibited.

*Test oracle:* Attempting a direct `UPDATE` on the inspection results table via the application DB user returns a database permission error; corrections create a new correction record linked to the original.

---

**NFR-S-002**
Access to CoA generation, QC template management, and batch quality status changes shall be restricted to users with the QC Manager or QC Analyst roles, enforced at the API endpoint level (not only at the UI level), as specified in the 8-layer RBAC architecture.

*Test oracle:* An authenticated user with role "Warehouse Staff" submitting a POST request to the CoA generation endpoint receives HTTP 403; a user with role "QC Analyst" receives HTTP 200.

---

**NFR-S-003**
*When* a batch quality status is changed, the system shall enforce segregation of duties (BR-003): the user who submitted the inspection result shall not be the same user who approves the batch to "Approved" status; the API shall reject self-approval attempts.

*Test oracle:* An API request for batch approval where the submitting user ID equals the approving user ID returns HTTP 400 with error code SOD_VIOLATION.

---

## 5.4 Usability Requirements

**NFR-U-001**
The production order creation workflow shall require no more than 5 screen interactions (clicks, form submissions) from the time a Production Manager selects "New Production Order" to the time the order is in "Plan" status, in compliance with DC-001.

*Test oracle:* Usability walkthrough by a newly trained Production Manager completes order creation in ≤ 5 interactions; tested with a first-time user who has received only a 30-minute orientation.

---

**NFR-U-002**
The Factory Floor App shall operate without mandatory training for supervisors performing routine daily tasks (start order, record completion, submit attendance), in compliance with DC-001. All primary actions shall be reachable within 3 taps from the app home screen.

*Test oracle:* A usability test with a first-time user finds that starting a production order, entering completion quantities, and recording attendance are each completed within 3 taps without assistance.

---

## 5.5 Maintainability Requirements

**NFR-M-001**
All production and QC business rules configurable under DC-002 (overhead rate, mass balance tolerance, SPC subgroup size, grading rules, CoA template formats) shall be maintainable via the web ERP administration interface by the Finance Director or IT Administrator without source code changes or developer involvement.

*Test oracle:* The Finance Director can update the overhead absorption rate and the mass balance tolerance via the UI; the new values take effect on the next production order close without a deployment; confirmed by unit test of the configuration-reading service.

---

**NFR-M-002**
The manufacturing and QC modules shall achieve a minimum of 80% test coverage for all service classes handling production costing, mass balance calculation, QC gate enforcement, and CoA generation, measured by PHPUnit code coverage report.

*Test oracle:* PHPUnit coverage report for Phase 4 service classes shows ≥ 80% line coverage; the coverage report is generated as part of the CI/CD pipeline.

---

## 5.6 Portability and Replicability

**NFR-PR-001**
All BIRDC-specific production configuration (processing station names, by-product categories, overhead categories, CoA format parameters) shall reside in database configuration tables, not in application code, in compliance with DC-007. Redeploying the system for a different agro-processor shall require only configuration table updates.

*Test oracle:* A code review confirms that no processing station name or by-product label is hardcoded in PHP files; all such values are read from configuration tables; verified by static code analysis.

---
