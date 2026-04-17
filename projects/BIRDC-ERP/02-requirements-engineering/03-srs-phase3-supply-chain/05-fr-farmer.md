# 4. Functional Requirements — F-010: Farmer & Cooperative Management

All functional requirements in this section follow the IEEE 830-1998 stimulus-response pattern. All farmer personal data requirements are subject to the Uganda Data Protection and Privacy Act 2019. Pending legal review: [CONTEXT-GAP: GAP-004].

---

## 4.1 Farmer Registration

**FR-FAR-001** — When a Field Collection Officer opens the Farmer Registration screen in the Farmer Delivery App (online or offline), the system shall present a form capturing: first name, last name, other names, sex, date of birth, NIN (16-character alphanumeric), primary phone number (MTN or Airtel mobile money number), secondary phone number (optional), cooperative name, district, sub-county, parish, village, and GPS coordinates (auto-captured via device GPS at the time of registration).

**FR-FAR-002** — When a Field Collection Officer captures the farmer's NIN, the system shall, when online, submit a lookup request to the National Identification and Registration Authority (NIRA) API to verify the NIN and return the registered name for confirmation; if the NIRA API is unavailable or the device is offline, the system shall accept the NIN as entered and flag the record as "NIN Unverified — Pending NIRA Lookup" for resolution on next sync. [CONTEXT-GAP: GAP-004 — NIRA API integration scope and data sharing agreement required]

**FR-FAR-003** — When a Field Collection Officer registers a new farmer, the system shall capture a farmer photo using the device camera; the photo shall be stored at a minimum resolution of 480 × 640 pixels and shall be displayed on the farmer profile and on the farmer receipt; if photo capture fails (camera unavailable), the system shall allow registration to proceed and flag the record as "Photo Missing".

**FR-FAR-004** — When a new farmer registration is submitted offline, the system shall store the complete record in the local Room (SQLite) database with a temporary local ID prefixed `LOC-`; when connectivity returns and the record syncs to the server, the server shall assign a permanent farmer registration number in the format `FMR-NNNNNN` and the app shall replace the local ID with the permanent number in all local records referencing that farmer.

**FR-FAR-005** — When a farmer registration is synced to the server, the system shall encrypt the following fields at rest using AES-256 encryption: NIN, primary phone number, secondary phone number, and GPS coordinates; these fields shall be decryptable only by authenticated users with "View Sensitive Farmer Data" permission, per DC-006 and the Uganda Data Protection and Privacy Act 2019. [CONTEXT-GAP: GAP-004 — confirm which fields require encryption under DPPА legal review]

**FR-FAR-006** — When a duplicate NIN is detected during farmer registration (either online or on sync), the system shall reject the duplicate record and display: "A farmer with this NIN is already registered as [Farmer Name], Registration No. [FMR-NNNNNN]. Do you want to update the existing record instead?" The system shall not create two farmer records with the same NIN.

**FR-FAR-007** — When a farmer record is created or updated, the system shall record the mobile money number and network (MTN or Airtel) for that farmer; this number is the destination for all farmer bulk payment submissions; the system shall maintain a history of all phone number changes, recording the old number, new number, change date, and the officer who made the change.

**FR-FAR-008** — When a Procurement Manager views a farmer profile, the system shall display: farmer's full name, registration number, NIN (masked by default, full NIN visible on explicit "View NIN" action with permission check), photo, cooperative, district/sub-county/parish/village, GPS coordinates (with map link), mobile money number, registration date, and current account status (active / suspended / deceased).

**FR-FAR-009** — When a farmer is registered, the system shall generate and print a Farmer Registration Card via the Bluetooth thermal printer connected to the Field Collection Officer's device; the card shall include: farmer name, registration number, cooperative, barcode (encoding the farmer registration number), QR code, and photo.

---

## 4.2 Farmer Bulk Import

**FR-FAR-010** — When an IT Administrator uploads a CSV or Excel file to the farmer bulk import function, the system shall validate each row against the mandatory field schema (first name, last name, NIN, phone, cooperative, district, sub-county, parish, village); rows failing validation shall be reported in an error log with row number and specific error; valid rows shall be imported and assigned permanent farmer registration numbers.

**FR-FAR-011** — When a bulk import is completed, the system shall display an import summary: total rows submitted, rows successfully imported, rows rejected (with error count), and a downloadable error report in Excel format; no partial row shall be imported — each row either fully succeeds or is fully rejected.

---

## 4.3 Farm Profiling

**FR-FAR-012** — When a Field Collection Officer opens the Farm Profile screen for a registered farmer, the system shall allow creating multiple farm records under that farmer; each farm record shall capture: farm name/local identifier, size in acres, GPS polygon boundary (minimum 3 GPS coordinate vertices captured by walking the boundary or tapping on a map), primary banana cultivar (selectable from the banana variety catalogue from F-015), secondary cultivars, other crops grown, livestock count by type, on-farm irrigation (yes/no), on-farm storage capacity (tonnes), drying surface area (m²), and access road condition (murram / tarmac / footpath / none).

**FR-FAR-013** — When GPS polygon boundary points are captured offline, the system shall store all polygon vertices in the local Room database and sync them to the server on reconnection; the server shall calculate and store the polygon area in hectares as a cross-check against the officer-entered acreage.

**FR-FAR-014** — When a farm record is saved, the system shall link the banana varieties recorded on that farm to the banana variety catalogue (F-015 Research module); if a cultivar name entered by the officer does not match any entry in the variety catalogue, the system shall flag it as "[GLOSSARY-GAP: cultivar name]" and add it to a pending variety catalogue review list for the Research Coordinator.

---

## 4.4 Banana Variety Tracking

**FR-FAR-015** — When a Research Coordinator adds a banana variety to the variety catalogue, the system shall capture: cultivar name, variety code (unique alphanumeric), *Musa* species group (AAA / AAB / ABB), processing characteristics (flour yield %, chips suitability rating, juice yield %), and regional suitability notes; this catalogue is shared between F-010 (farmer profiling) and F-015 (Research & Development).

**FR-FAR-016** — When a Procurement Manager requests a variety distribution report, the system shall display the count of farms and farmers growing each registered banana cultivar, aggregated by district and cooperative; this report supports procurement planning for specific-cultivar processing runs.

---

## 4.5 Cooperative Organisation and Hierarchy

**FR-FAR-017** — When an IT Administrator or Procurement Manager configures the cooperative hierarchy, the system shall support exactly 4 levels: individual farmer → primary cooperative → zone → BIRDC network; each level shall have a name, geographic coverage description, and at least one registered leader contact; a farmer cannot be registered without assignment to a primary cooperative.

**FR-FAR-018** — When a Procurement Manager views a cooperative profile, the system shall display: cooperative name, zone, registered leader name and contact, total registered farmers, total area (sum of all member farm acreages), current season's total weight delivered (kg), current season's total gross payable (UGX), and average quality grade mix (% Grade A, B, C) for the current season.

**FR-FAR-019** — When a zone or BIRDC-level report is requested, the system shall aggregate cooperative-level data to the requested hierarchy level; all aggregated reports shall clearly label the reporting level (cooperative / zone / network) and the reporting period.

**FR-FAR-020** — When a cooperative leader's contact details change, the system shall require the change to be approved by the Procurement Manager; the previous contact details shall be retained in history and shall not be deleted.

---

## 4.6 Farmer Contribution History and Account Statement

**FR-FAR-021** — When a Finance Manager or Procurement Manager views a farmer's delivery history, the system shall display a chronological list of all delivery records for that farmer including: batch number, delivery date, cooperative, weight delivered (kg), quality grade, gross payable (UGX), deductions (itemised by type), net payable (UGX), and payment status (Pending / Paid / Failed); the list shall be filterable by date range, season, and payment status.

**FR-FAR-022** — When a Finance Manager or the farmer (via farmer portal, future phase) requests an account statement for a specified period, the system shall generate a PDF farmer account statement (mPDF) showing: farmer name, registration number, cooperative, period covered, opening balance, all delivery transactions with debits (gross payable), all deductions by type, net payments made with mobile money transaction references, and closing balance.

**FR-FAR-023** — When a Procurement Manager needs to export the full delivery history for a cooperative or season, the system shall export the data in Excel format (PhpSpreadsheet) with one row per farmer contribution record; the export shall include all fields shown in FR-FAR-021.

---

## 4.7 Extension Services Tracking

**FR-FAR-024** — When an Extension Officer records a training session, the system shall capture: training date, topic, facilitator name and organisation, location, and a list of attending farmers (selected from the farmer register by name or registration number); each attending farmer's record shall be updated with the session reference, creating a training attendance log per farmer.

**FR-FAR-025** — When an Extension Officer issues an input loan to a farmer, the system shall capture: loan type (seeds / fertiliser / crop management tools / other), item description, quantity issued, unit cost, total loan value (UGX), issue date, repayment schedule (number of instalments, amount per instalment, first deduction season), and the authorising officer; the loan record shall be linked to the farmer's record and shall be accessible to the payment calculation module for deduction application (FR-PRO-061).

**FR-FAR-026** — When a loan repayment instalment is due (based on the repayment schedule), the system shall automatically include the instalment amount in the farmer's deductions for the next payment calculation run; the system shall display the outstanding loan balance on the farmer's profile and shall notify the Procurement Manager of any farmer whose outstanding loan balance exceeds UGX 500,000 or 60% of their last 3-season average earnings.

**FR-FAR-027** — When an Extension Officer logs a farm visit, the system shall capture: visit date, officer name, farmer visited, farm visited, purpose of visit (advisory / inspection / problem investigation / data collection), observations recorded (free text), recommendations made (free text), and follow-up actions with due dates; each visit record is appended to the farmer's extension log.

**FR-FAR-028** — When a Procurement Manager requests an extension services summary report, the system shall display: total training sessions conducted (by period), total farmers trained, total input loans issued (UGX), total input loans outstanding (UGX), total farm visits conducted, and top 10 farmers by outstanding loan balance.

---

## 4.8 Farmer Performance Analysis

**FR-FAR-029** — When a Procurement Manager opens the farmer performance dashboard, the system shall display: top 20 farmers by total weight delivered (current season), top 20 farmers by Grade A percentage, bottom 20 farmers by Grade A percentage, farmers with zero deliveries in the current season, and farmers whose current-season deliveries are below 50% of their prior-season deliveries; each list shall be exportable to Excel.

**FR-FAR-030** — When the system identifies a farmer with zero deliveries in a season where the farmer's cooperative has active deliveries, the system shall add the farmer to a "Below Target" list visible to the Extension Officer assigned to that cooperative; the Extension Officer shall be prompted to log a follow-up visit.

**FR-FAR-031** — When a Procurement Manager requests a quality grade trend report for a cooperative, the system shall display a time-series chart showing the proportion of Grade A, B, and C deliveries per month for the selected cooperative over the selected period; the chart shall be rendered using ApexCharts and shall be exportable as a PNG image or PDF.

---

## 4.9 Farmer Payment Processing

**FR-FAR-032** — When a farmer payment schedule is generated (per FR-PRO-062), the system shall display each farmer's mobile money number and network operator alongside their net payable amount; the Procurement Manager or Finance Manager may flag an individual farmer's payment as "Hold — Pending Verification" before submission; held payments are excluded from the bulk submission but remain on the schedule as "Held".

**FR-FAR-033** — When a bulk mobile money payment batch is submitted to MTN MoMo Business API, the system shall include: the farmer's mobile money number, payment amount (UGX), a narration string in the format "BIRDC Payment [Season] Batch [BPO-YYYY-NNNN]", and the BIRDC merchant wallet identifier; each API call shall be made over HTTPS/TLS 1.3 using the credentials stored in the system integration configuration (not in code). [CONTEXT-GAP: GAP-002 — MTN MoMo Business API credentials]

**FR-FAR-034** — When a bulk mobile money payment batch is submitted to Airtel Money API for Airtel number holders, the system shall follow the equivalent process to FR-FAR-033 using the Airtel Money API endpoint and credentials. [CONTEXT-GAP: GAP-003 — Airtel Money API credentials]

**FR-FAR-035** — When a mobile money payment confirmation is received from MTN MoMo or Airtel Money API for an individual farmer payment, the system shall: (1) update the farmer's payment record status to "Paid", (2) record the mobile money transaction reference, (3) record the payment timestamp, (4) trigger an SMS notification to the farmer (see FR-FAR-049), and (5) update the farmer's Cooperative Payable balance in the GL (DR Cooperative Payable / CR Bank Account via the bulk payment).

**FR-FAR-036** — When a mobile money payment fails for an individual farmer (API returns a failure response), the system shall: set the farmer's payment record to "Payment Failed", record the error code and description from the API response, alert the Finance Manager by email with the farmer name, registration number, mobile money number, amount, and failure reason; the failed payment shall be eligible for retry in the next payment run or via manual bank transfer.

**FR-FAR-037** — When a farmer's mobile money number is changed (FR-FAR-007), the system shall require Finance Manager approval for any payment submitted to the new number for the first 2 payment runs after the change; this approval requirement is an anti-fraud control.

---

## 4.10 SMS Notification to Farmers

**FR-FAR-038** — When a batch goods receipt is saved (Stage 2), the system shall send an SMS to the cooperative leader of the delivering cooperative confirming: batch number, cooperative name, gross weight, net weight, collection date, and the number of individual contributions expected to be entered.

**FR-FAR-039** — When a farmer's individual contribution record is finalised in Stage 3, the system shall send an SMS to the farmer's registered primary phone number containing: farmer name, batch number, delivery date, weight delivered (kg), quality grade, and gross payable (UGX before deductions); the SMS shall be sent using the system's configured SMS gateway.

**FR-FAR-040** — When a farmer payment is confirmed as paid, the system shall send an SMS to the farmer's registered primary phone number containing: "BIRDC PAYMENT: You have received UGX [amount] for [season] deliveries. Ref: [transaction reference]. Queries: [BIRDC contact number]."

**FR-FAR-041** — When a farmer payment fails, the system shall send an SMS to the farmer's registered primary phone number: "BIRDC PAYMENT: Your payment of UGX [amount] for [season] could not be processed to [masked phone number]. Contact BIRDC office on [contact number] to resolve."

---

## 4.11 Farmer Portal (Future Phase — Planned)

**FR-FAR-042** — When a farmer accesses the farmer portal web page using their registration number and registered phone number as credentials, the system shall display a read-only view of: their delivery history for the last 3 seasons, current payment status, next expected payment date, and any outstanding input loan balance; the portal shall not permit any data modification.

*Note: The Farmer Portal is planned for a future phase. This requirement is included for architectural awareness. It shall not be built in Phase 3.*

---

## 4.12 Farmer Data Management and Compliance

**FR-FAR-043** — When an IT Administrator runs the data audit for farmer records, the system shall report: total registered farmers, farmers with missing NIN verification, farmers with missing photos, farmers with unverified mobile money numbers, and farmers with no delivery in the last 2 seasons; this report supports data quality management under DC-003.

**FR-FAR-044** — When a farmer is marked "Deceased" or "Inactive", the system shall: retain all historical delivery and payment records indefinitely, prevent new delivery records from being created for that farmer, flag any pending payment to that farmer as "Held — Farmer Status Review" for Finance Manager action, and prevent the farmer registration number from being reassigned.

**FR-FAR-045** — When an auditor or Procurement Manager requests a data export of all farmer records, the system shall produce the export in encrypted ZIP format; the export shall include all fields except NIN and mobile money numbers (which require a separate "Sensitive Data Export" permission with Director-level approval), per DC-006 and the Uganda Data Protection and Privacy Act 2019.

**FR-FAR-046** — When a farmer requests erasure of their data (right to erasure under the Uganda Data Protection and Privacy Act 2019), the system shall flag the request for the Finance Director's review; the Finance Director shall determine whether erasure is legally permissible (it is not permissible if the farmer has outstanding financial obligations or if their records are within the 7-year audit retention period per DC-003); the outcome and justification shall be logged in the audit trail. [CONTEXT-GAP: GAP-004 — legal review of data erasure vs. financial retention obligations required]

---

## 4.13 Cooperative Reporting and Aggregation

**FR-FAR-047** — When a Finance Manager requests a cooperative payable ageing report, the system shall display for each cooperative: total GL balance in Cooperative Payable account, amount arising from GL-posted batches paid in the current run, amount from prior runs pending payment, and amount from GL-posted batches not yet included in any payment run; the ageing shall be expressed in days from batch GL posting date.

**FR-FAR-048** — When a Procurement Manager requests a season summary report for the BIRDC network, the system shall display: total weight received (kg) by cooperative, total gross payable (UGX) by cooperative, total deductions by type (UGX), total net paid (UGX), average Grade A % by cooperative, average price per kg by cooperative, and a comparison to the prior season's equivalent figures; the report shall be exportable to Excel (PhpSpreadsheet) and PDF (mPDF).

---

## 4.14 Farmer SMS Confirmation of Contribution (Additional)

**FR-FAR-049** — When a payment confirmation SMS is sent (FR-FAR-040), the system shall log: farmer ID, phone number, SMS content, sending timestamp, gateway response code, and delivery status; delivery failures shall be retried once after 10 minutes and, if still failing, shall be logged as "SMS Delivery Failed" for manual follow-up by the Procurement Manager.
