# Gap Analysis -- Medic8 Healthcare Management System

All 7 HIGH-priority gaps must be resolved before clinical module development begins. MEDIUM gaps must be resolved before Phase 2. External resources and internal decisions are listed at the end.

---

## HIGH Priority Gaps (Resolve Before Clinical Development)

### HIGH-001: Clinical Safety -- Medication Errors

**Gap:** Drug interaction database source not specified. Allergy-prescription conflict check logic not defined. Weight-based dosing for paediatrics not specified.

**Resolution Required:**
1. Licence a drug interaction database (DrugBank, RxNorm/NLM, or Uganda NDA formulary)
2. Define interaction severity levels and alert behaviour (warning vs hard stop)
3. Define paediatric dosing formula (mg/kg with min/max cap)
4. Specify allergy-prescription conflict detection logic and pharmacist override workflow

**Owner:** Peter (clinical safety architecture decision)
**Status:** [ ] Unresolved

---

### HIGH-002: Data Protection Act 2019 -- Healthcare Data

**Gap:** Patient consent for data collection/sharing, right of access, breach notification, cross-border sharing (FHIR/DHIS2), and lawful basis for HIV/mental health/reproductive health records are not documented.

**Resolution Required:**
1. Engage a Uganda data protection lawyer for health data legal review
2. Document consent categories per data type (routine clinical, HIV, mental health, reproductive health, substance abuse)
3. Define data retention periods aligned with WHO/MoH guidelines
4. Define lawful basis for processing each category under the Uganda Data Protection and Privacy Act 2019
5. Establish breach notification procedure (72 hours to PDPO, immediate to affected patients)
6. Define cross-border data sharing rules for FHIR/DHIS2 integrations

**Owner:** Peter (legal review required)
**Status:** [ ] Unresolved

---

### HIGH-003: Uganda Medical Licensing -- Software Regulation

**Gap:** Whether Medic8 requires registration with UMDPC or NDA if it supports prescribing, dispensing, and clinical decision support is unknown.

**Resolution Required:**
1. Contact Uganda Medical and Dental Practitioners Council (UMDPC) for software registration enquiry
2. Contact National Drug Authority (NDA) for guidance on software that supports prescribing and dispensing
3. Determine if Medic8 classifies as a medical device under Uganda regulations

**Blocker:** This is a blocker before commercial sale to licensed health facilities.

**Owner:** Peter (regulatory enquiry)
**Status:** [ ] Unresolved

---

### HIGH-004: Clinical Decision Support Specificity

**Gap:** What CDS rules are implemented, who configures them, how clinicians override alerts, how overrides are logged, and what liability Medic8 assumes if CDS is wrong are not defined.

**Resolution Required:**
1. Define CDS as data-driven (configuration table, not hardcoded rules)
2. Define alert types: informational, warning (overridable with reason), hard stop (not overridable)
3. Audit every alert fired and every override action (clinician ID, timestamp, reason text, patient ID, alert ID)
4. Define in Terms of Service that Medic8 is decision support, not decision maker -- clinical liability remains with the prescribing clinician
5. Consult a practising clinician to validate alert categories and thresholds

**Owner:** Peter (architecture and legal decision)
**Status:** [ ] Unresolved

---

### HIGH-005: HIV and Confidential Record Access

**Gap:** Not all clinical staff should see HIV status. Mental health, reproductive health, and substance abuse records need additional access controls beyond standard RBAC.

**Resolution Required:**
1. Define a sensitive record access tier using Attribute-Based Access Control (ABAC) for: HIV, mental health, substance abuse, reproductive health
2. Restrict cross-facility access more strictly for sensitive categories
3. Allow patients to request their own records but not alter clinical entries
4. Log all access to sensitive records with viewer identity, timestamp, and justification
5. Implement "break the glass" emergency access with mandatory post-access audit

**Owner:** Peter (security architecture decision)
**Status:** [ ] Unresolved

---

### HIGH-006: Emergency Access to Cross-Facility Records

**Gap:** Process, safeguards, audit requirements, and what information is shared during emergency access are not fully specified.

**Resolution Required:**
1. Define two-factor confirmation before granting emergency access
2. Specify data revealed during emergency access: allergies, current medications, blood group, HIV status (if patient consented to emergency disclosure), last 3 diagnoses
3. Set 24-hour access expiry with automatic revocation
4. Send patient SMS notification when emergency access is exercised
5. Create full audit trail: accessing clinician, facility, reason for access, timestamp, data viewed, expiry timestamp

**Owner:** Peter (clinical workflow decision)
**Status:** [ ] Unresolved

---

### HIGH-007: HMIS Form Versions

**Gap:** What happens when MoH changes HMIS forms, who updates mappings, and the acceptable lag time are not specified.

**Resolution Required:**
1. Subscribe to hmis2.health.go.ug notices for form version changes
2. Version-control HMIS form mappings in configuration tables (not hardcoded)
3. Establish a 30-day maximum turnaround for updating mappings after MoH publishes a new form version
4. Define a fallback: if a new form version is not yet mapped, export data in the previous version with a warning flag

**Owner:** Peter (operational process)
**Status:** [ ] Unresolved

---

## MEDIUM Priority Gaps (Resolve Before Phase 2)

1. **Insurance pre-authorisation** -- specific insurer workflows per Uganda insurer (NHIS, AAR, Jubilee, etc.). Contact each insurer for claims format and pre-auth form.
2. **NHIS integration** -- claims format and API not yet publicly documented. Register with NHIS as licensed healthcare software.
3. **NMS commodity ordering system** -- how National Medical Stores receives facility orders. Obtain LMIS data submission format.
4. **CPHL interface** -- specimen submission format and result return process. Contact Central Public Health Laboratories, Butabika.
5. **Disaster recovery** -- RPO and RTO not defined. Recommend RPO < 1 hour, RTO < 4 hours for clinical systems.
6. **Multi-language clinical interface** -- beyond Luganda for patient-facing content. Swahili, Runyoro/Rutooro for regional facilities.
7. **Telemedicine regulatory compliance** -- verify against Uganda MoH telemedicine guidelines before launch.
8. **Prescribing authority rules** -- clinical officers and nurses have different prescribing scopes. Define per role per Uganda Medical and Dental Practitioners Act.

---

## External Resources Required (from Peter)

1. Uganda NDA drug interaction database or formulary -- contact NDA Kampala
2. NHIS claims format and provider API documentation -- contact NHIS Uganda secretariat
3. NMS LMIS data submission format -- contact National Medical Stores Uganda
4. CPHL specimen submission process -- contact Central Public Health Laboratories, Butabika
5. Uganda MoH HMIS tools (forms 105, 108, 033b) -- download from health.go.ug
6. Uganda Diagnostic Imaging standards -- contact Radiology Society of Uganda
7. WHO Essential Medicines List (Uganda adaptation) -- download from WHO and MoH
8. PEPFAR MER Indicator Reference Guide (current FY) -- download from datim.org
9. UBTS blood transfusion guidelines -- contact Uganda Blood Transfusion Service
10. UMDPC software registration enquiry -- contact Uganda Medical and Dental Practitioners Council
11. Data Protection Officer -- consult Uganda data protection lawyer before launching HIV/mental health records

---

## Internal Decisions Required (from Peter)

1. **Clinical decision support liability** -- will Terms of Service explicitly disclaim clinical liability? Legal review required.
2. **Drug interaction database** -- build own (expensive, high liability) or licence third-party (preferred)? Budget allocation needed.
3. **FHIR server** -- full HAPI FHIR server or FHIR-format exports only? Full server is more complex but enables richer integration.
4. **White-labelling** -- allow facilities to brand Medic8 as their own? Affects pricing model.
5. **Government facility pricing** -- heavily discounted edition for HC IIs/IIIs? Builds market share but delays revenue.
6. **Telemedicine launch timing** -- launch under existing practice or wait for formal MoH regulation?
