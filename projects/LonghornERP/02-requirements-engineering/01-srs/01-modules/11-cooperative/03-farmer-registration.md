# 3. Farmer Registration and Society Hierarchy Requirements

## 3.1 Overview

This section specifies requirements for registering individual farmers and outgrowers, validating their national identity, recording geographic and financial data, and organising them within a multi-level cooperative hierarchy. The hierarchy model supports Uganda's standard four-level structure as well as KTDA and NAEB configurations.

## 3.2 Farmer Record and NIN Validation

**FR-COOP-011** — When a registration officer submits a farmer record containing first name, last name, date of birth, sex, NIN, phone number, and primary commodity, the system shall validate the NIN format (14 alphanumeric characters matching the pattern `[A-Z]{2}[0-9]{7}[A-Z]{5}` for Uganda), persist the record, and return the assigned farmer ID within 2 seconds.

*Acceptance criterion:* NIN "CM12345678ABCDE" passes format validation and the record is saved; NIN "CM123" is rejected with: "NIN must be 14 alphanumeric characters in the correct format."

[CONTEXT-GAP: NIRA real-time NIN verification API availability — confirm whether Longhorn ERP will call the NIRA API for live NIN validation or perform format-only validation.]

**FR-COOP-012** — When a registration officer submits a farmer record with a NIN that already exists in the tenant, the system shall reject the submission and display: "A farmer with NIN [value] is already registered as [Farmer Name] (ID: [ID])."

*Acceptance criterion:* Duplicate NIN submission returns the existing farmer's name and ID; no duplicate record is created.

**FR-COOP-013** — When a registration officer edits a field on an existing farmer record, the system shall record the previous value, the new value, the editing user, and the timestamp in an immutable audit log entry for that farmer.

*Acceptance criterion:* Changing a farmer's phone number creates an audit log entry with old value, new value, user ID, and UTC timestamp retrievable via the audit trail screen.

## 3.3 GPS Coordinates

**FR-COOP-014** — When a registration officer enters or captures GPS coordinates for a farmer's farm plot, the system shall validate that the latitude is in the range −90.000000 to 90.000000 and the longitude is in the range −180.000000 to 180.000000, store the coordinates to 6 decimal places, and display the location on a map preview.

*Acceptance criterion:* Coordinates (0.347596, 32.582520) are accepted and displayed on the map; coordinates (91.0, 32.5) are rejected with: "Latitude must be between −90 and 90."

**FR-COOP-015** — When the mobile application has GPS hardware access and the registration officer taps "Capture GPS", the system shall read the device location and auto-populate the latitude and longitude fields with a positional accuracy of ≤ 10 metres (CEP-50).

*Acceptance criterion:* Auto-capture populates coordinates within 10 metres of the actual farm location as verified by a reference GPS device.

## 3.4 Payment Details (Bank and Mobile Money)

**FR-COOP-016** — When a registration officer saves payment details for a farmer, the system shall store one or more of the following payment methods: bank account (bank name, branch, account number, account name) or mobile money (provider: MTN/Airtel/M-Pesa, phone number), and designate one method as the default disbursement channel.

*Acceptance criterion:* A farmer record with MTN MoMo number 0771234567 as default and a Centenary Bank account as secondary is saved; the disbursement engine uses the MTN number by default.

**FR-COOP-017** — When a registration officer enters a mobile money phone number, the system shall validate the number against the provider's prefix rules (MTN Uganda: 077x/078x; Airtel Uganda: 070x/075x; M-Pesa Kenya: 07xx/01xx) and reject non-matching numbers with: "Phone number [value] does not match the prefix rules for [provider]."

*Acceptance criterion:* Number "0701234567" submitted as MTN is rejected; submitted as Airtel is accepted.

## 3.5 Society Hierarchy

**FR-COOP-018** — When an administrator creates a group record with a name, location, and parent primary society, the system shall persist the group and make it selectable as the organisational unit when registering individual farmers.

*Acceptance criterion:* Group "Butebo Farmers Group" under society "Butebo Primary Cooperative Society" is created; a farmer can be assigned to it during registration.

**FR-COOP-019** — When an administrator creates a primary society record with a name, registration number, district, and parent union (optional), the system shall persist the record and display it as a selectable node in the hierarchy tree.

*Acceptance criterion:* Society "Butebo Primary Cooperative Society" (reg. no. CS-2021-0045) is created and visible in the hierarchy.

**FR-COOP-020** — When an administrator creates a union record with a name and registration number, the system shall persist the record as the top-level node in the hierarchy; primary societies may be linked to this union.

*Acceptance criterion:* Union "Eastern Uganda Cooperative Union" is created; societies are linked to it and the hierarchy renders correctly.

**FR-COOP-021** — When a user requests the hierarchy view for a cooperative union, the system shall render the complete tree (union → societies → groups → farmers) with record counts at each node, and the response shall load within 3 seconds for a hierarchy of up to 10,000 farmer records.

*Acceptance criterion:* A union with 3 societies, 12 groups, and 2,500 farmers renders its full hierarchy within 3 seconds as measured from request submission to first meaningful paint.

## 3.6 Kenya KTDA and Rwanda NAEB Structure Support

**FR-COOP-022** — When a tenant is configured for the Kenya (KTDA) jurisdiction, the system shall:

1. Replace the Uganda NIN field with the Kenya National ID field (8-digit numeric).
2. Relabel the primary society tier as "Factory" to align with KTDA nomenclature.
3. Apply the KTDA two-payment-cycle model (green leaf payment + bonus payment) in the payment configuration for that tenant.

When a tenant is configured for the Rwanda (NAEB) jurisdiction, the system shall:

1. Replace the Uganda NIN field with the Rwanda National ID field (16-digit numeric).
2. Relabel the union tier as "NAEB Cooperative" and the primary society tier as "Washing Station" for coffee cooperatives.
3. Apply NAEB export levy deduction rules as the default levy schedule.

*Acceptance criterion:* A Kenya-configured tenant shows "Factory" in the hierarchy and "Kenya National ID" on the farmer form; the Uganda NIN label does not appear. A Rwanda-configured tenant shows "Washing Station" and "NAEB Cooperative" labels.

[CONTEXT-GAP: KTDA green leaf and bonus payment cycle dates and calculation rules — confirm whether these are configurable per tenant or hardcoded to KTDA seasonal norms.]

[CONTEXT-GAP: NAEB export levy current rate schedule — confirm applicable levy percentages for coffee and tea to populate the default Rwanda levy configuration.]
