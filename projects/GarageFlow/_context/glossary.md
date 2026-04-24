# Glossary — GarageFlow

Every domain- or project-specific term used in generated artifacts MUST resolve to an entry here. Missing terms are flagged `[GLOSSARY-GAP: <term>]` at audit.

## Platform and organisational

- **Chwezi Core Systems** — publisher and sole owner of GarageFlow. chwezicore.com.
- **GarageFlow** — the multi-tenant SaaS automotive service management platform that is the subject of this SRS.
- **Garage Manager App** — staff-facing application family (Android, iOS, web).
- **Garage Customer App** — customer-facing application family (Android, iOS, web secondary).
- **Super Admin Panel** — Chwezi-operated platform administration surface.
- **Tenant** — a subscribing garage business. Owns branches, users, and all operational records.
- **Branch** — a physical location of a tenant. Owns bays and local stock.

## Workshop operations

- **Job card** — the unit of work representing one vehicle's service visit.
- **Bay** — a physical workshop position (lift, flat, alignment, paint, valet, etc.).
- **Bay board** — live tablet-mounted overview of all bays at a branch.
- **Service advisor** — staff role facing the customer; composes estimates, captures approvals.
- **Workshop controller** — staff role assigning jobs to bays and technicians.
- **Technician** — staff role executing work and capturing inspections.
- **Storekeeper** — staff role managing parts inventory.
- **Appointment** — planned pre-arrival entity for a job card.
- **QC** — Quality Control, post-execution review before invoicing.

## Vehicle and inspection

- **VIN** — Vehicle Identification Number; 17-character identifier per ISO 3779.
- **Plate** — vehicle registration plate number.
- **Odometer** — cumulative distance reading.
- **DTC** — Diagnostic Trouble Code, per SAE J1979 / ISO 15031.
- **OBD-II** — On-Board Diagnostics standard used to retrieve DTCs.
- **ELM327** — consumer OBD-II interpreter chip; the common Bluetooth OBD adapter class.
- **Inspection template** — tenant-authored list of checkpoints for a service type.
- **Checkpoint** — single inspection item with label, measurement unit, thresholds, photo rule.
- **Traffic-light severity** — green / amber / red mapping of a checkpoint's measurement to urgency.
- **Recommendation** — derived suggested service or part arising from an amber or red checkpoint.

## Parts and inventory

- **Reservation** — quantity of a part held against an approved estimate but not yet consumed.
- **Issue** — consumption of a reserved part at the workshop bay; decrements stock-on-hand.
- **Cycle count** — periodic physical count of stock against the ledger.
- **FIFO** — First-In-First-Out inventory valuation method.
- **COGS** — Cost of Goods Sold.
- **Core charge** — returnable deposit on a remanufactured part.

## Accounting and finance

- **GL** — General Ledger.
- **Chart of accounts** — tenant-configured ledger account structure.
- **Journal entry** — a debit/credit pair (or set) posted to the GL.
- **Real-time-async GL posting** — GL entry emitted to a durable queue at event commit and posted by a worker within 60 s at P95.
- **Period close** — finalising a financial period so prior-period entries are locked.
- **Bank reconciliation** — matching bank statement lines to journal entries.

## Payment and tax

- **PCI-DSS** — Payment Card Industry Data Security Standard v4.0.
- **PAN** — Primary Account Number (credit card number).
- **Token** — opaque reference to a stored card held by a PCI-certified gateway.
- **3DS / 3D Secure** — cardholder authentication standard for card-not-present transactions.
- **Mobile money** — phone-based electronic wallet (MTN MoMo, Airtel Money, M-PESA, etc.).
- **STK push** — SIM Toolkit-initiated payment prompt on the customer's phone.
- **EFRIS** — Electronic Fiscal Receipting and Invoicing System (Uganda, URA).
- **KRA eTIMS** — Kenya Revenue Authority electronic Tax Invoice Management System.
- **RRA EBM** — Rwanda Revenue Authority Electronic Billing Machine.
- **ZATCA** — Zakat, Tax and Customs Authority (Saudi Arabia); Phase 2 e-invoicing.
- **CFDI** — Comprobante Fiscal Digital por Internet (Mexico / LATAM).

## Data protection

- **PII** — Personally Identifiable Information.
- **CHD** — Cardholder Data.
- **GDPR** — EU General Data Protection Regulation.
- **Uganda DPPA 2019** — Data Protection and Privacy Act of Uganda.
- **PDPO** — Personal Data Protection Office (Uganda).
- **DPIA** — Data Protection Impact Assessment.
- **Subject access / erasure / portability** — standard data-subject rights under GDPR and equivalents.

## Methodology and engineering

- **Hybrid methodology** — Water-Scrum-Fall: Waterfall SRS phase, Agile build phase.
- **SRS** — Software Requirements Specification (IEEE 830).
- **SDD** — Software Design Description.
- **V&V** — Verification and Validation (IEEE 1012).
- **NFR** — Non-Functional Requirement.
- **FR** — Functional Requirement.
- **ADR** — Architecture Decision Record.
- **CIA** — Change Impact Analysis.
- **Baseline** — a sealed snapshot of artifacts at a phase boundary.
- **P95 / P99** — 95th / 99th percentile latency measures.

## Mobile engineering

- **Room** — Android local database (AndroidX Room).
- **SwiftData / Core Data** — iOS local persistence.
- **ML Kit** — Google ML library used for barcode scanning on Android.
- **Vision** — Apple framework used for barcode scanning on iOS.
- **Keychain plus Secure Enclave** — iOS secure credential store.
- **Android Keystore plus StrongBox** — Android secure credential store.
- **Play Integrity** — Google device attestation API.
- **App Attest** — Apple device attestation API.

## Customer experience

- **Customer digital approval** — authoritative record that the customer approved the estimate (channel: in-app, email-click, signed image, recorded verbal).
- **Live status timeline** — chronological, customer-visible view of job transitions.
- **White-label Customer App** — tenant-branded build of the Customer App distributed under the tenant's own App Store / Play Store listing.
- **Multi-tenant Customer App** — the default single app whose tenant theme is applied after the user authenticates and selects a garage.
