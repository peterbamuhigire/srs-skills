---
title: "SRS Phase 2b — Pharmacy/Drug Store Add-on Module (F-012)"
subtitle: "Section 3: Functional Requirements"
project: Maduuka
version: 0.1-draft
date: 2026-04-05
status: Draft — Pending Human Review
---

# Section 3: Functional Requirements for the Pharmacy/Drug Store Module

All requirements in this section follow the stimulus-response pattern mandated by the IEEE 830-1998 verifiability criterion. The format is: *When [stimulus/condition], the system shall [deterministic response].*

Requirements are uniquely identified with the prefix **FR-PHR-** followed by a 3-digit sequence number. Each identifier maps to the business feature (F-012) and the applicable business rules (BR-006, BR-013, BR-014) stated in the requirement.

---

## 3.1 Patient Management (FR-PHR-001 to FR-PHR-010)

**FR-PHR-001** — When a Pharmacist or Pharmacy Technician initiates the "New Patient" action, the system shall create a patient profile record containing the following mandatory fields: first name, last name, date of birth, sex, and phone number. The following fields are optional: National Identification Number (NIN), email address, district/sub-county, insurance provider name, and insurance member ID.

**FR-PHR-002** — When a patient profile is saved with at least one allergen entry, the system shall store each allergen as a structured record containing: allergen name, associated drug class (selectable from the drug reference database drug class list), and severity (mild / moderate / severe). Multiple allergen entries are permitted per patient.

**FR-PHR-003** — When a Pharmacist or Pharmacy Technician adds an allergen to a patient's allergy register, the system shall validate that the drug class field references a class present in the drug reference database. If the class does not exist, the system shall reject the entry and display: "Drug class not recognised. Select a class from the reference list or add it via drug reference settings."

**FR-PHR-004** — When a user enters a search term of 2 or more characters in the patient search field, the system shall return all patient records where the search term matches the beginning of the patient's first name, last name, or NIN, or exactly matches the registered phone number. Results shall be displayed within 500 ms.

**FR-PHR-005** — When a search returns no matching patient records, the system shall display: "No patient found. Create a new patient profile?" with an action link to FR-PHR-001.

**FR-PHR-006** — When a patient profile is opened, the system shall display: demographics summary, allergy register, insurance details, active prescriptions count, and dispensing history count, each as a navigable section.

**FR-PHR-007** — When a Pharmacist or Pharmacy Technician edits a patient profile field (excluding allergy register entries), the system shall save the change and record the previous value, new value, user, and timestamp in the audit log (BR-003).

**FR-PHR-008** — When a Pharmacist or Pharmacy Technician edits an existing allergy register entry, the system shall treat the edit as a new entry appended to the allergy history. The prior entry shall remain visible and marked "superseded" with date and user. Allergy entries shall never be permanently deleted.

**FR-PHR-009** — When the pharmacy POS is opened and a patient is selected, the system shall display a summary badge showing the count of active allergens. If the count is 1 or greater, the badge shall be displayed in amber.

**FR-PHR-010** — When a patient profile is accessed by an NDA Inspector role, the system shall display only the data fields required for the controlled drugs register (name, NIN). The full demographic profile, allergy register, and prescription history shall not be visible to the NDA Inspector role.

---

## 3.2 Prescription Management (FR-PHR-011 to FR-PHR-025)

**FR-PHR-011** — When a Pharmacist or Pharmacy Technician initiates "New Prescription" for a selected patient, the system shall create a prescription record containing: prescribing doctor name (free text), prescribing facility name (free text), prescription date, and at least 1 prescription line item.

**FR-PHR-012** — When a prescription line item is added, the system shall capture: drug name (searchable against the drug reference database generic and brand names), prescribed dosage (free text), prescribed quantity, duration (number of days), and administration instructions (free text). All 5 fields are mandatory per line item.

**FR-PHR-013** — When a prescription is saved, the system shall assign a unique prescription number following the format `RX-{TENANT_ID}-{YYYYMMDD}-{SEQ}` where SEQ is a zero-padded 4-digit sequence that resets daily per tenant.

**FR-PHR-014** — When a Pharmacist or Pharmacy Technician attaches a prescription photo or scan, the system shall accept image files (JPEG, PNG, HEIC) up to 10 MB and PDF files up to 20 MB. The attachment shall be stored against the prescription record and retrievable from the prescription detail view.

**FR-PHR-015** — When a prescription is created, the system shall set its status to "New" and record the creation timestamp and creating user.

**FR-PHR-016** — When a dispensing event is completed against a prescription and at least 1 but fewer than all prescription line items are fully dispensed, the system shall update the prescription status to "Partially Filled" and record the remaining quantity per unfilled line item.

**FR-PHR-017** — When a dispensing event is completed against a prescription and all prescription line items reach their prescribed quantity, the system shall update the prescription status to "Fully Filled" and record the completion timestamp.

**FR-PHR-018** — When the current date exceeds the prescription date plus the configurable expiry period (default: 30 days), the system shall update the prescription status to "Expired" via a scheduled background job running at 00:00 tenant local time. An "Expired" prescription shall not be fillable.

**FR-PHR-019** — When a Pharmacist or Pharmacy Technician attempts to dispense against a prescription with status "Expired", the system shall block the dispensing action and display: "Prescription RX-{number} expired on {date}. A new prescription is required."

**FR-PHR-020** — When the prescription expiry period is configured by a Business Owner, the system shall accept any whole-number value from 1 to 365 days. The default value at pharmacy activation is 30 days.

**FR-PHR-021** — When a Pharmacist or Pharmacy Technician searches for a prescription at the POS, the system shall accept search input by patient name (FR-PHR-004 matching rules) or by prescription number. Results shall display: prescription number, patient name, prescribing doctor, prescription date, status, and item count.

**FR-PHR-022** — When a prescription search returns results, the system shall display only prescriptions with status "New" or "Partially Filled" in the default view. "Fully Filled" and "Expired" prescriptions shall be accessible via an explicit "Show all" toggle.

**FR-PHR-023** — When a prescription-only product is added to the pharmacy POS dispensing cart without a linked prescription, the system shall apply the enforcement rule configured per BR-013: (a) if set to "hard block", the system shall prevent the item from being added and display a blocking message; (b) if set to "warning-only", the system shall display a warning and require the user to acknowledge before the item is added.

**FR-PHR-024** — When a partial fill is completed against a prescription line item, the system shall record: the quantity dispensed in this event, the remaining quantity, the dispensing pharmacist, the batch number selected, and the timestamp. This record is appended to the prescription dispensing history and is immutable (BR-004).

**FR-PHR-025** — When a prescription's last remaining quantity across all line items is dispensed, the system shall automatically transition the prescription status from "Partially Filled" to "Fully Filled" as part of the same dispensing transaction commit.

---

## 3.3 Pharmacy POS — Dispensing (FR-PHR-026 to FR-PHR-045)

**FR-PHR-026** — When the Pharmacy POS is opened, the system shall display a patient selection step before any product can be added to the dispensing cart. A dispensing cart without a linked patient shall not be committable.

**FR-PHR-027** — When a user enters a search term of 2 or more characters in the pharmacy product search field, the system shall search simultaneously against the product's generic name field and all brand name entries in the drug reference database and return ranked results within 500 ms. Results shall display generic name, brand names, drug class, and current stock level.

**FR-PHR-028** — When a controlled substance product appears in pharmacy product search results, the system shall display a visual controlled substance indicator (a distinct colour-coded badge labelled with the schedule classification, e.g., "S3") adjacent to the product name in all search result rows.

**FR-PHR-029** — When a product is added to the pharmacy dispensing cart, the system shall apply FEFO batch selection (BR-006) by automatically pre-selecting the batch with the earliest expiry date that has available stock greater than 0. The selected batch number, expiry date, and available quantity shall be displayed to the user.

**FR-PHR-030** — When a Pharmacist with manager-level override permission manually selects a batch other than the FEFO-selected batch, the system shall record the override: user, overridden batch, selected batch, reason (free text, mandatory), and timestamp. This override record is appended to the audit log (BR-003) and is immutable.

**FR-PHR-031** — When a Pharmacy Technician attempts to override the FEFO batch selection, the system shall block the action and display: "FEFO override requires Pharmacist authorisation."

**FR-PHR-032** — When a product is dispensed, the system shall apply the dispensing unit configured for that product (tablet, capsule, ml, sachet, or other). If the dispensing unit differs from the purchase unit (e.g., purchase unit = box of 100 tablets, dispensing unit = tablet), the system shall calculate and deduct the correct stock quantity using the configured unit conversion factor.

**FR-PHR-033** — When a product is added to the pharmacy dispensing cart and the selected patient has 1 or more allergen entries in their allergy register, the system shall check whether the product's drug class matches any allergen drug class in the patient's register within 300 ms of the add action. If a match is found, the system shall display an allergy alert before the item is confirmed into the cart.

**FR-PHR-034** — When an allergy alert is displayed (FR-PHR-033), the alert shall include: the matched allergen name, the patient's recorded severity for that allergen, the matching drug class, and an "Override with reason" action. The override is available to the Pharmacist role only. The Pharmacy Technician role shall see a hard block with the message: "Allergy block: consult the pharmacist." [CONTEXT-GAP: drug interaction database source not defined — the category-level check specified in FR-PHR-035 depends on a drug-class-to-interaction mapping table whose source has not been determined.]

**FR-PHR-035** — When a product is added to the pharmacy dispensing cart, the system shall perform a category-level drug interaction check against all products currently in the cart and against the patient's active prescription medications (if a prescription is linked). If a potential interaction is detected between drug classes, the system shall display an interaction warning message that includes: the two interacting drug classes, a plain-language category description of the interaction type, and the mandatory disclaimer: *"This system provides basic category-level drug interaction warnings as a decision-support aid only. It does not replace clinical pharmacist judgement. Maduuka is not certified as a clinical decision support system."* [CONTEXT-GAP: drug interaction database source not defined — interaction mapping rules required before FR-PHR-035 can be implemented.]

**FR-PHR-036** — When a drug interaction warning is displayed (FR-PHR-035), the pharmacist shall be required to either: (a) acknowledge the warning and proceed, or (b) remove the flagged product from the cart. Acknowledgement is logged against the dispensing session with user and timestamp.

**FR-PHR-037** — When the allergy alert severity configuration is set to "Hard Block" for a given drug class by a Business Owner, the system shall prevent the add-to-cart action entirely for that class match and shall not provide an override option to any user role.

**FR-PHR-038** — When a dispensing transaction is completed, the system shall generate a dispensing label record for each product dispensed. The label record shall contain: patient name, drug name (generic), dosage, administration instructions, pharmacist name, dispensing date, batch number, and expiry date.

**FR-PHR-039** — When a Pharmacist or Pharmacy Technician requests label printing for a completed dispensing event, the system shall render the dispensing label as: (a) a printable PDF formatted for 57 mm × 32 mm label stock, or (b) an A4 PDF with up to 8 labels per page. The user shall select format before printing.

**FR-PHR-040** — When a dispensing cart is committed as a sale, the system shall record the sale against the linked prescription (if present), update the prescription line item remaining quantities, and update the prescription status per FR-PHR-016, FR-PHR-017, and FR-PHR-025 within the same database transaction.

**FR-PHR-041** — When a controlled substance is included in the pharmacy dispensing cart, the system shall require the linked prescription to be present before the cart is committable, regardless of the BR-013 enforcement setting configured for the business. The hard block for controlled substances is not configurable.

**FR-PHR-042** — When a void or refund is processed against a pharmacy dispensing transaction, the system shall reverse the stock movement and update the prescription dispensing history with a reversal record containing: original dispensing event reference, reversal reason, user, and timestamp (BR-004).

**FR-PHR-043** — When a Pharmacy Technician attempts to commit a dispensing cart containing a controlled substance, the system shall block the commit and display: "Controlled substance dispensing requires a Pharmacist to complete this transaction."

**FR-PHR-044** — When the dispensing unit quantity entered for a product exceeds the available stock in the FEFO-selected batch, the system shall display: "Insufficient stock: {available quantity} {dispensing unit} available in batch {batch number} (expiry {date}). Select a different batch or reduce quantity."

**FR-PHR-045** — When a dispensing event is completed, the system shall record the dispensing pharmacist's name (the logged-in user) against the transaction record. This field is non-editable after commit.

---

## 3.4 Drug Reference Database (FR-PHR-046 to FR-PHR-055)

**FR-PHR-046** — When a drug record is created or imported, the system shall store the following fields: generic name (mandatory), brand names (1 or more; each stored as a separate linked record), drug class (mandatory; controlled vocabulary), standard dosage description (free text), controlled substance classification (S1 / S2 / S3 / S4 / Not Controlled), storage requirements (ambient / refrigerated 2–8°C / frozen ≤ -18°C), and NDA drug code. [CONTEXT-GAP: GAP-003 — NDA Uganda approved drug codes and formulary not yet obtained. The NDA drug code field shall be populated once GAP-003 is resolved.]

**FR-PHR-047** — When the Pharmacy add-on is first activated for a tenant, the system shall load the platform-level drug reference database into the tenant's drug catalogue. The platform admin manages updates to this database. Tenants cannot add new drug records directly; they may request additions via a flagging mechanism.

**FR-PHR-048** — When a user searches the drug reference database by generic name or brand name, the system shall return results using fuzzy matching that tolerates up to 2 character substitutions (Levenshtein distance ≤ 2) and returns results within 500 ms.

**FR-PHR-049** — When a drug search is executed and results contain controlled substance entries, the system shall visually distinguish each controlled substance entry with a schedule badge (e.g., "S3") in the search result list.

**FR-PHR-050** — When a drug record is viewed, the system shall display all associated brand names, drug class, standard dosage, controlled substance classification, storage requirements, and NDA drug code. If the NDA drug code field is empty, the system shall display: "[CONTEXT-GAP: GAP-003 — NDA drug code not yet loaded]" in place of the code.

**FR-PHR-051** — When the platform admin uploads a drug database update file, the system shall validate the file format and flag any records with missing mandatory fields before import. Records with validation errors shall not be imported. A validation report shall be generated listing accepted and rejected records.

**FR-PHR-052** — When a drug record's controlled substance classification is changed from "Not Controlled" to any schedule (S1–S4) by the platform admin, the system shall flag all active tenant product catalogue entries linked to that drug record for review and notify the Business Owner via in-app notification.

**FR-PHR-053** — When a Pharmacist searches for a drug at the POS using a partial brand name of 3 or more characters, the system shall include brand name matches ranked above generic name matches in the result set, on the assumption that dispensing staff more frequently search by commercial name.

**FR-PHR-054** — When a drug record's storage requirement is set to "refrigerated" or "frozen", the system shall flag the associated product in inventory with a cold chain indicator visible in all stock listing views.

**FR-PHR-055** — When the platform admin deactivates a drug record, the system shall retain all historical dispensing records linked to that drug record. The deactivated drug shall not appear in new dispensing searches but shall remain visible in historical records with a "deactivated" label.

---

## 3.5 Batch and Expiry Management (FR-PHR-056 to FR-PHR-065)

**FR-PHR-056** — When stock for a pharmacy product is received, the system shall require batch number and expiry date to be recorded on the Goods Receipt Note (GRN) before the receipt can be confirmed. Receipt of pharmacy products without a batch number or expiry date shall be blocked.

**FR-PHR-057** — When a dispensing event occurs for a product with multiple active batches, the system shall select the batch with the earliest expiry date as the default dispensing batch (FEFO, BR-006). If 2 batches share the same expiry date, the system shall select the batch with the lower stock quantity first.

**FR-PHR-058** — When the current date reaches the near-expiry threshold for a batch (configurable: 30, 60, or 90 days before expiry date), the system shall generate a near-expiry alert. The alert shall be delivered as: (a) an in-app notification to the Pharmacist and Business Owner roles, and (b) an entry in the near-expiry alerts dashboard widget.

**FR-PHR-059** — When a batch's expiry date is reached (current date ≥ expiry date), the system shall automatically move the batch to "Expired — Quarantined" status via the scheduled background job (00:00 tenant local time). Quarantined batches shall be excluded from available dispensable stock and from FEFO selection.

**FR-PHR-060** — When a batch is quarantined (FR-PHR-059), the system shall notify the Pharmacist and Business Owner via in-app notification with the message: "Batch {batch number} of {product name} expired on {date}. {quantity} {unit} quarantined. Record disposal."

**FR-PHR-061** — When a Pharmacist records the destruction of an expired batch, the system shall capture: destruction date, method (incineration / return to supplier / NDA disposal scheme / other), quantity destroyed, witnessing officer name (optional), and a destruction certificate attachment (optional PDF). The destruction record is appended to the batch history and is immutable (BR-004).

**FR-PHR-062** — When a cold chain product (storage type = refrigerated or frozen) has a temperature log entry recorded, the system shall validate the entered temperature against the defined range for the storage type: 2–8°C for refrigerated, ≤ -18°C for frozen. If the value is outside the range, the system shall immediately display an out-of-range alert and record the breach in the temperature log with a "Breach" flag.

**FR-PHR-063** — When a Pharmacist records a cold chain temperature reading, the system shall capture: product name, storage location (free text), temperature value (°C), reading timestamp, and the recording user. Readings shall be stored in the temperature log chronologically.

**FR-PHR-064** — When a cold chain temperature breach is recorded (FR-PHR-062), the system shall notify the Pharmacist and Business Owner via in-app notification within 60 seconds of the breach entry being saved.

**FR-PHR-065** — When the near-expiry alert threshold is configured by a Business Owner, the system shall accept any one of the following values: 30 days, 60 days, or 90 days. Multiple thresholds may be active simultaneously (e.g., alerts at both 60 days and 30 days). The default at activation is 30 days.

---

## 3.6 Controlled Drugs Register (FR-PHR-066 to FR-PHR-075)

**FR-PHR-066** — When a dispensing transaction is completed for a controlled substance (schedule S1–S4), the system shall automatically write a controlled drugs register entry within 1 second of dispensing confirmation containing: dispensing date and time, dispensing pharmacist (name and system user ID), patient name, patient NIN (if recorded), prescribing doctor name, drug name (generic), schedule classification, batch number, quantity dispensed, unit, and running balance of that drug in stock after the dispensing event.

**FR-PHR-067** — When a controlled drugs register entry is written (FR-PHR-066), the system shall ensure the entry is appended to the immutable register log. No user interface action, API endpoint, or database-level operation accessible to any tenant user role shall permit editing or deletion of a register entry. Platform admin bulk corrections are subject to a separate documented process outside the application UI.

**FR-PHR-068** — When the running balance in FR-PHR-066 is calculated, the system shall derive it as: running balance = previous register entry balance for that drug − quantity dispensed in this event. If no prior entry exists for the drug, the running balance equals the current stock level after deduction.

**FR-PHR-069** — When an NDA Inspector or Business Owner requests the controlled drugs register for a specified date range, the system shall return all register entries within the range sorted ascending by entry timestamp. [CONTEXT-GAP: GAP-009 — NDA Uganda exact register format, required fields, and data retention period not yet confirmed. The output format specified here is provisional and subject to revision once GAP-009 is resolved.]

**FR-PHR-070** — When the controlled drugs register export is requested (FR-PHR-069), the system shall generate the export in both PDF and CSV format. The PDF format shall use the `templates/reference.docx` style reference via Pandoc. The CSV export shall include a header row with column names matching the field list in FR-PHR-066.

**FR-PHR-071** — When the NDA audit log export is generated, the system shall include: all controlled drugs register entries, all FEFO override records for controlled substances, all allergy override records for controlled substances, and all prescription-linked dispensing events for controlled substances within the requested date range.

**FR-PHR-072** — When a Pharmacy Technician views the controlled drugs register, the system shall display the register in read-only mode with no export action available. The export action is restricted to Pharmacist, Business Owner, and NDA Inspector roles.

**FR-PHR-073** — When a void or refund is processed against a dispensing transaction that included a controlled substance, the system shall append a reversal entry to the controlled drugs register. The reversal entry shall reference the original entry number, state the reversal reason, and recalculate the running balance. The original entry shall remain unchanged (BR-004).

**FR-PHR-074** — When the system is queried for the current running balance of a controlled substance, the system shall calculate it by summing all register entries for that drug (dispensed quantities subtract, reversal quantities add back) rather than reading from a pre-computed balance field, to ensure the register is self-consistent.

**FR-PHR-075** — When a controlled drugs register entry is viewed, the system shall display a cryptographic hash (SHA-256) of the entry content, computed at write time and stored immutably. Inspectors may use this hash to verify that the entry has not been modified outside the application.

---

## 3.7 Insurance Billing (FR-PHR-076 to FR-PHR-083)

**FR-PHR-076** — When a dispensing transaction is completed and the patient has an insurance provider and policy number recorded on their profile, the system shall prompt the Pharmacist to optionally create an insurance claim record for the transaction. The prompt shall be dismissible without creating a claim.

**FR-PHR-077** — When an insurance claim record is created, the system shall capture: patient name, insurance provider, policy number, list of items claimed (drug name, quantity, unit price, subtotal), total amount claimed, and claim submission date.

**FR-PHR-078** — When an insurance claim is created, the system shall set its initial status to "Submitted" and record the creating user and timestamp.

**FR-PHR-079** — When the status of an insurance claim is updated to "Approved", "Rejected", or "Paid", the system shall record the new status, the user making the update, the timestamp, and — for "Rejected" status — a mandatory rejection reason (free text).

**FR-PHR-080** — When a Pharmacist or Business Owner opens the outstanding claims report, the system shall display all claims with status "Submitted" or "Approved" (not yet paid), grouped by insurance provider, with columns: claim reference, patient name, amount claimed, status, submission date, and days outstanding (calculated as current date − submission date).

**FR-PHR-081** — When the outstanding claims report is exported, the system shall generate a PDF and CSV version. Both formats shall include the same columns listed in FR-PHR-080 plus the policy number.

**FR-PHR-082** — When an insurance claim status transitions to "Paid", the system shall record the payment amount, payment date, and payment method. If the payment amount differs from the claimed amount, the system shall display: "Partial payment: UGX {paid amount} received against claim of UGX {claimed amount}. Difference: UGX {variance}."

**FR-PHR-083** — When a claim is marked "Rejected" and the rejection reason is recorded (FR-PHR-079), the system shall offer a "Re-submit" action that creates a new claim record referencing the original claim number. The original rejected claim record is not modified.

---

## 3.8 Refill Reminders (FR-PHR-084 to FR-PHR-090)

**FR-PHR-084** — When a dispensing transaction is completed against a prescription that has a duration field set on at least 1 line item, the system shall calculate the estimated refill date for each dispensed item as: refill date = dispensing date + duration (days). The refill reminder shall be scheduled to fire on: refill date − reminder lead time (days, configurable per prescription, default: 3 days).

**FR-PHR-085** — When the scheduled refill reminder fires, the system shall send a message to the patient's registered phone number via SMS (Africa's Talking) containing: patient name, drug name(s) due for refill, estimated refill date, and the pharmacy business name and phone number.

**FR-PHR-086** — When Africa's Talking WhatsApp Business API access is configured for the tenant (per GAP-006 resolution), the system shall also send the refill reminder as a WhatsApp message to the same phone number in addition to SMS. If WhatsApp delivery fails, the SMS delivery shall not be affected.

**FR-PHR-087** — When a refill reminder lead time is configured per prescription, the system shall accept any whole-number value from 1 to 30 days. The default at prescription creation is 3 days.

**FR-PHR-088** — When a patient opts out of refill reminders, the system shall record the opt-out preference against the patient profile and suppress all future refill reminder sends for that patient. The opt-out shall be recordable by the Pharmacist on the patient profile screen or by the patient via a reply keyword (e.g., "STOP") to the SMS message.

**FR-PHR-089** — When a refill reminder SMS is sent, the system shall log the send event with: patient name, phone number, drug name(s), scheduled send time, actual send time, and Africa's Talking delivery status response. The log is viewable by the Pharmacist and Business Owner.

**FR-PHR-090** — When a prescription is marked "Fully Filled" (FR-PHR-017) or "Expired" (FR-PHR-018), the system shall cancel any pending scheduled refill reminders for that prescription. Cancelled reminders shall be logged with status "Cancelled — prescription closed."
