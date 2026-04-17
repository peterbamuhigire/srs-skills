# Section 2: Risk Register

## Risk R-001: EFRIS API Sandbox Unavailable

| Field | Detail |
|---|---|
| **Risk ID** | R-001 |
| **Description** | URA EFRIS API sandbox credentials are not yet provisioned [GAP-001]. Phase 1 invoice and POS receipt testing cannot be completed without sandbox access. If sandbox access is delayed beyond the Phase 1 testing sprint, the Phase 1 milestone delivery will slip, triggering a milestone payment delay. |
| **Category** | External (E) |
| **Probability** | Medium — URA's EFRIS developer portal exists; registration is a procedural step, not a technical barrier. Delays are common. |
| **Impact** | Critical — EFRIS compliance is a legal requirement for every commercial invoice; Phase 1 cannot go live without it. |
| **Risk Level** | High (2 × 4 = 8) |
| **Mitigation Strategy** | 1. Peter to initiate URA EFRIS developer portal registration in Week 1 of Phase 1 development, before the first invoice sprint begins. 2. BIRDC IT to provide all required business registration documents for the registration. 3. Begin EFRIS integration module development against the EFRIS API documentation without live sandbox; use mocked API responses for unit tests. 4. Reserve the last 2 weeks of Phase 1 for live sandbox integration testing once credentials arrive. |
| **Residual Risk** | Low — if mock-based development is completed first, sandbox integration is a 2-week activity. If sandbox is delayed beyond Phase 1 timeline, Phase 1 is extended; it does not fail. |
| **Owner** | Peter Bamuhigire / BIRDC IT |

---

## Risk R-002: Uganda DPPA Legal Review Not Completed Before Go-Live

| Field | Detail |
|---|---|
| **Risk ID** | R-002 |
| **Description** | The Uganda Data Protection and Privacy Act 2019 review of BIRDC's farmer PII collection (NIN, GPS, photo, mobile money number) has not been completed [GAP-004]. If the system goes live with farmer registration before lawful basis is confirmed and a privacy notice is in place, BIRDC faces legal liability under DPPA 2019, including fines and enforcement action by the National Data Protection Office (NDPO). |
| **Category** | Legal (L) |
| **Probability** | Medium — legal review can be completed; the risk is that it is overlooked or deprioritised. |
| **Impact** | Critical — regulatory enforcement, potential data collection suspension, and reputational damage to a government entity. |
| **Risk Level** | Critical (2 × 4 = 8) — classified Critical due to legal exposure severity |
| **Mitigation Strategy** | 1. BIRDC Director to commission a legal opinion from counsel familiar with DPPA 2019 before Phase 3 farmer registration module enters development (not at go-live). 2. Legal opinion to confirm: lawful basis, retention period, farmer consent form text, and subject rights procedure. 3. The system's privacy controls (encryption, access restriction, audit trail) are already built in; the legal review confirms the procedural layer. 4. Farmer registration module go-live is gated on receipt of the legal opinion. |
| **Residual Risk** | Low — technical privacy controls are already specified; legal review is a procedural gate. |
| **Owner** | BIRDC Director / Legal Counsel |

---

## Risk R-003: MTN MoMo API Sandbox Unavailable

| Field | Detail |
|---|---|
| **Risk ID** | R-003 |
| **Description** | MTN MoMo Business API sandbox credentials are not yet provisioned [GAP-002]. Agent remittance reconciliation and farmer bulk payment testing cannot be completed without sandbox access. Affects Phase 2 AR module and Phase 3 farmer payment testing. |
| **Category** | External (E) |
| **Probability** | Medium — MTN MoMo developer portal is open for registration; credential issuance typically takes 2–4 weeks after business verification. |
| **Impact** | High — farmer payment and agent remittance modules cannot go live without a tested mobile money integration. |
| **Risk Level** | High (2 × 3 = 6) |
| **Mitigation Strategy** | 1. Peter to initiate MTN MoMo Business API registration during Phase 1 development (not Phase 2). 2. BIRDC Finance to provide business registration certificate for MTN verification. 3. Develop mobile money integration module against MTN API documentation with mock responses. 4. Schedule live sandbox testing in the Phase 2 sprint after credentials are received. |
| **Residual Risk** | Low — MTN MoMo Business API is a documented API with an active developer programme. Registration is procedural. |
| **Owner** | Peter Bamuhigire / BIRDC Finance |

---

## Risk R-004: PPDA Threshold Values Not Confirmed

| Field | Detail |
|---|---|
| **Risk ID** | R-004 |
| **Description** | The current PPDA procurement threshold values (UGX amounts for micro, small, large, restricted categories) applicable to BIRDC/PIBID as a government entity have not been confirmed [GAP-007]. If placeholder values are used in the procurement approval matrix and the system goes live with incorrect thresholds, procurement transactions may be approved at the wrong authority level — a PPDA Act violation. |
| **Category** | Legal (L) |
| **Probability** | Low — threshold values are publicly available from PPDA Uganda; this is a research task. |
| **Impact** | High — incorrect PPDA classification exposes BIRDC to procurement non-compliance findings in the annual OAG audit. |
| **Risk Level** | Medium (1 × 3 = 3) |
| **Mitigation Strategy** | 1. Peter to retrieve current PPDA threshold schedule from PPDA Uganda website (ppda.go.ug) during Phase 3 design. 2. BIRDC Administration to confirm the entity classification (central government, statutory body) to determine applicable threshold tier. 3. Finance Director to review and sign off configuration values before Phase 3 procurement module goes live. |
| **Residual Risk** | Very Low — once values are confirmed and configured, the system enforces them deterministically. Configuration update by Finance Director or IT Administrator if PPDA revises thresholds. |
| **Owner** | BIRDC Administration / Peter |

---

## Risk R-005: Intermittent Power and Internet at Nyaruzinga Bushenyi

| Field | Detail |
|---|---|
| **Risk ID** | R-005 |
| **Description** | BIRDC's operations are at Nyaruzinga hill, Bushenyi District, Western Uganda, where power supply and internet connectivity are intermittent. Production and development activities may be interrupted, slowing development timelines. At go-live, operational disruptions during connectivity outages could result in data loss or synchronisation failures if offline-first design is not correctly implemented. |
| **Category** | Operational (O) |
| **Probability** | High — power and connectivity interruptions in rural Uganda are frequent. |
| **Impact** | Medium — development slowdown; no data loss risk if offline-first is correctly implemented. |
| **Risk Level** | High (3 × 2 = 6) |
| **Mitigation Strategy** | 1. System design enforces offline-first for all field-facing modules (DC-005): Factory Gate POS, Farmer Delivery App, Warehouse App, Sales Agent App all persist transactions locally and sync on reconnect. 2. BIRDC IT to maintain a UPS (Uninterruptible Power Supply) for the primary server rack. 3. Peter to conduct development primarily remotely; deploy and test on-site in sprint review sessions only. 4. Offline sync time requirement of ≤ 60 seconds ensures data loss is zero for typical day's transactions. |
| **Residual Risk** | Low for data integrity. Medium for development timeline — budget an additional 10% development time buffer for connectivity-related interruptions. |
| **Owner** | Peter Bamuhigire / BIRDC IT |

---

## Risk R-006: Developer Skill Availability in Uganda

| Field | Detail |
|---|---|
| **Risk ID** | R-006 |
| **Description** | The BIRDC ERP requires PHP/MySQL web backend developers and Kotlin Android developers. The Ugandan developer market has limited supply of developers with experience in enterprise ERP systems. If key developers cannot be sourced, delivery timelines will slip. |
| **Category** | Operational (O) |
| **Probability** | Medium — Uganda has a growing developer community, but enterprise ERP experience is scarce. |
| **Impact** | High — developer shortage directly delays phase delivery milestones and milestone payment triggers. |
| **Risk Level** | High (2 × 3 = 6) |
| **Mitigation Strategy** | 1. Peter to begin developer recruitment in parallel with Phase 1 documentation, not after. 2. Prioritise developers with PHP/Laravel or PHP/CodeIgniter background over ERP-specific experience — ERP domain knowledge can be provided by Peter. 3. Consider remote East African developers (Kenya, Rwanda, Tanzania) for the Kotlin Android components where local market is thin. 4. Structure onboarding with the BIRDC Technical Specification and Coding Guidelines documents (Phase 4 artefacts) to reduce ramp-up time. 5. Retain a backup developer contact before Phase 1 development begins. |
| **Residual Risk** | Medium — developer availability is the project's most significant operational risk. Mitigation reduces but does not eliminate the risk. |
| **Owner** | Peter Bamuhigire |

---

## Risk R-007: Legacy Data Migration Complexity

| Field | Detail |
|---|---|
| **Risk ID** | R-007 |
| **Description** | The current state of BIRDC's accounting and operational data is unknown [GAP-014]. If BIRDC has existing financial records in Excel, accounting software, or paper registers that must be migrated into the ERP, the migration complexity could extend the go-live timeline significantly. Poor data quality or incomplete historical records could result in an inaccurate opening balance sheet. |
| **Category** | Technical (T) |
| **Probability** | Medium — BIRDC is an established organisation with 20+ years of operations; some historical records are certain to exist. |
| **Impact** | High — incorrect opening balances invalidate the first audited financial statements produced by the ERP. |
| **Risk Level** | High (2 × 3 = 6) |
| **Mitigation Strategy** | 1. Finance Director to confirm the current accounting tools in use and provide a sample data extract before Phase 2 design begins [GAP-014]. 2. Data migration plan to be a separate project artefact (not part of the core ERP development). 3. Agree a data migration cut-off date with the Finance Director (clean opening balances from a specific date). 4. Run parallel operation (old system + new ERP) for a minimum of one financial month before decommissioning the old system. 5. OAG audit of the opening balances in the first year to validate migration accuracy. |
| **Residual Risk** | Medium — data migration is inherently risky. The parallel operation period reduces the risk of undetected migration errors. |
| **Owner** | BIRDC Finance Director / Peter |

---

## Risk R-008: Payroll Calculation Error After Approval Lock

| Field | Detail |
|---|---|
| **Risk ID** | R-008 |
| **Description** | Once the Finance Manager approves and locks a payroll run (BR-010), no modification is possible. A calculation error discovered after lock results in employees receiving incorrect salary for that period, creating PAYE underpayment or overpayment liability to URA and potential employee relations issues. The correction mechanism (adjustment run in the next period) may not satisfy employees who received less than their correct salary. |
| **Category** | Operational (O) |
| **Probability** | Low — the payroll lock workflow requires Finance Manager review and approval before lock. |
| **Impact** | High — incorrect PAYE remittance creates URA liability; incorrect NSSF creates NSSF liability; incorrect net salary creates employee relations risk. |
| **Risk Level** | Medium (1 × 3 = 3) |
| **Mitigation Strategy** | 1. Implement a mandatory payroll preview report that the Finance Manager must review before approval. The preview shows gross-to-net calculations for every employee. 2. Include a comparison to the previous payroll run to flag unusually large variances (e.g., salary increase or new deduction). 3. Require the Finance Manager to confirm they have reviewed the preview before the approval button is active. 4. Test payroll calculations against manually verified figures for a representative sample of 10 employee profiles before go-live. |
| **Residual Risk** | Low — the preview and comparison controls reduce the probability of an undetected error to near zero. |
| **Owner** | BIRDC Payroll Officer / Finance Manager |

---

## Risk R-009: Agent Cash Accountability Gap During Transition

| Field | Detail |
|---|---|
| **Risk ID** | R-009 |
| **Description** | During the parallel operation period (paper registers and ERP running simultaneously), the 1,071 field agents will be operating partly on the old paper system and partly on the new Sales Agent App. Cash accountability gaps can occur if remittances are recorded in only one system, or if stock issuances from the old system are not entered into the ERP. |
| **Category** | Operational (O) |
| **Probability** | High — parallel operation is always high-risk for a field agent network of this size. |
| **Impact** | Medium — cash discrepancies that are not detected early accumulate and become difficult to reconcile. |
| **Risk Level** | High (3 × 2 = 6) |
| **Mitigation Strategy** | 1. Define a hard cut-over date for the field agent network — no parallel operation for agent activities. Agents move to the Sales Agent App fully on go-live day, not gradually. 2. Freeze all paper-based agent stock issuances one week before go-live and enter opening balances into the ERP from the final paper reconciliation. 3. The Sales Manager to conduct a 100% agent balance reconciliation in the first week of ERP operation. 4. Provide mandatory 2-hour Sales Agent App training to all agents in the 2 weeks before go-live. |
| **Residual Risk** | Low — a hard cut-over with confirmed opening balances eliminates the parallel operation risk. |
| **Owner** | BIRDC Sales Manager / Peter |

---

## Risk R-010: ZKTeco Biometric Device Incompatibility

| Field | Detail |
|---|---|
| **Risk ID** | R-010 |
| **Description** | The ZKTeco biometric attendance device model numbers and SDK/API version deployed at BIRDC Nyaruzinga are not confirmed [GAP-005]. Different ZKTeco models use different SDK versions and data export formats. If the integration is designed for a different SDK version than what is deployed, the biometric import will fail. |
| **Category** | Technical (T) |
| **Probability** | Low — ZKTeco devices are standardised with well-documented SDKs; API differences are manageable. |
| **Impact** | Medium — if incompatible, the HR module must fall back to manual attendance entry until the integration is fixed or the device is upgraded. No data loss; payroll can run with manual attendance. |
| **Risk Level** | Low (1 × 2 = 2) |
| **Mitigation Strategy** | 1. BIRDC IT to provide ZKTeco device model numbers in Week 1 of Phase 5 (HR module design). 2. Design the biometric integration against the ZKTeco Push SDK (most common for network-connected devices) as the default. 3. Build the integration with an abstraction layer so that the import format can be changed by configuration without code changes. 4. Budget 2 development days for device-specific testing on-site at Nyaruzinga before Phase 5 go-live. |
| **Residual Risk** | Very Low — biometric import is a non-critical path; manual attendance covers the gap if integration is delayed. |
| **Owner** | BIRDC IT / Peter |

---

## Risk R-011: Scope Creep — Client Requests Features Outside Agreed 17 Modules

| Field | Detail |
|---|---|
| **Risk ID** | R-011 |
| **Description** | As ERP usage grows during development and early phases, BIRDC management may request features beyond the 17 agreed modules (e.g., customer relationship management, e-commerce portal, logistics tracking). Each uncontrolled addition extends the delivery timeline and risks destabilising completed modules. |
| **Category** | Operational (O) |
| **Probability** | High — scope creep is a near-universal risk on ERP projects, especially where the client is seeing the system for the first time. |
| **Impact** | Medium — timeline extension; financial impact on milestone payments; risk of incomplete core modules. |
| **Risk Level** | High (3 × 2 = 6) |
| **Mitigation Strategy** | 1. The SRS suite (6 documents) constitutes the contractual scope boundary. Any feature not in the SRS is a change request requiring a written scope change order and a revised timeline and cost estimate. 2. Peter to present the scope boundary explicitly at the project kick-off meeting. 3. Each phase gate sign-off includes a scope confirmation statement from the BIRDC Director. 4. Proposed additions are queued for a future Phase 8 (Post-Go-Live Enhancements) to be scoped separately. |
| **Residual Risk** | Low — a contractual scope boundary with change request procedure is an industry-standard control for scope creep. |
| **Owner** | Peter Bamuhigire / BIRDC Director |

---

## Risk R-012: Parliament or Management Sign-off Delay

| Field | Detail |
|---|---|
| **Risk ID** | R-012 |
| **Description** | Each phase gate requires formal client sign-off (hybrid methodology). If the BIRDC Director or Finance Director is unavailable for review and sign-off at a phase gate, the next phase cannot begin and the milestone payment is delayed, creating cash flow pressure on the project. |
| **Category** | Operational (O) |
| **Probability** | Medium — government clients often have competing priorities; sign-off can take weeks when staff are unavailable. |
| **Impact** | Medium — milestone payment delay; development team idle time. |
| **Risk Level** | Medium (2 × 2 = 4) |
| **Mitigation Strategy** | 1. Each phase deliverable is submitted to the client 5 business days before the planned phase gate review meeting. 2. A written acknowledgement of receipt constitutes the start of the review period. 3. Phase gate review meetings are scheduled and confirmed in the project calendar at least 3 weeks in advance. 4. Designate a deputy sign-off authority (Finance Director as deputy for Director sign-off) in the engagement agreement. |
| **Residual Risk** | Low — pre-scheduling and deputy authority reduce the probability of indefinite delays. |
| **Owner** | Peter Bamuhigire / BIRDC Director |

---

## Risk R-013: Circular Economy Mass Balance Discrepancy in Production

| Field | Detail |
|---|---|
| **Risk ID** | R-013 |
| **Description** | The circular economy mass balance requirement (BR-008) mandates that Total Input = Products + By-products + Scrap (±2%). If production workers record output quantities inaccurately (intentionally or by scale calibration error), production orders will fail to close, blocking finished goods from entering saleable inventory and halting export order fulfilment. |
| **Category** | Operational (O) |
| **Probability** | Medium — manual data entry errors and uncalibrated scales are common in factory environments. |
| **Impact** | High — production orders stuck in "unbalanced" state delay product delivery to customers and impact export schedule. |
| **Risk Level** | High (2 × 3 = 6) |
| **Mitigation Strategy** | 1. The mass balance variance report (FR-MFG-010) is generated automatically for Production Supervisor review whenever the ±2% tolerance is exceeded. 2. The ±2% tolerance itself provides a buffer for minor scale calibration variance. 3. The Factory Floor App includes prompts that display the expected output range for the current recipe, so workers can cross-check before submission. 4. Scale calibration records are tracked in the QC module (lab equipment management, FR-QC-010). 5. Production Manager receives a daily production summary that includes mass balance pass/fail status for all orders closed that day. |
| **Residual Risk** | Medium — human entry errors cannot be fully eliminated. The ±2% tolerance and supervisor review process are the primary controls. |
| **Owner** | BIRDC Production Manager |

---

## Risk R-014: Export Certificate of Analysis Format Non-Compliance

| Field | Detail |
|---|---|
| **Risk ID** | R-014 |
| **Description** | Export market regulators (South Korea MFDS, EU RASFF, Saudi SFDA, Qatar MOPH, US FDA) require CoA documentation with specific parameters and formats [GAP-010]. If the CoA template is designed with incorrect or incomplete parameters, export shipments may be rejected at the destination port, causing financial loss and reputational damage with buyers. |
| **Category** | External (E) |
| **Probability** | Medium — export CoA requirements are documented by each country's food safety authority; the risk is that BIRDC's QC team does not obtain the exact parameter lists before the CoA template is designed. |
| **Impact** | Critical — a rejected shipment represents lost revenue, return logistics costs, and potential loss of the export buyer relationship. |
| **Risk Level** | Critical (2 × 4 = 8) |
| **Mitigation Strategy** | 1. BIRDC QC Manager to obtain the import inspection parameter lists for each target market before Phase 4 CoA template design. 2. CoA templates are configurable (DC-002); the QC Manager can update parameter sets without developer involvement if requirements change. 3. Engage each export buyer to review and approve the CoA template before the first export shipment. 4. The first export shipment to each new market should be treated as a pilot — deliver the CoA to the buyer's quality team for pre-shipment review before the shipment departs. |
| **Residual Risk** | Low — configurable CoA templates with buyer pre-approval provide strong protection against format rejection. |
| **Owner** | BIRDC QC Manager |

---

## Risk R-015: Data Loss During Go-Live Cutover

| Field | Detail |
|---|---|
| **Risk ID** | R-015 |
| **Description** | The go-live cutover involves migrating opening balances, existing farmer and employee records, and potentially historical financial data into the production system [GAP-014]. A failed cutover (database corruption, incomplete migration, or incorrect opening balances) could leave the system in an unusable state with lost data. |
| **Category** | Technical (T) |
| **Probability** | Low — a well-tested cutover plan with rollback procedures minimises this risk. |
| **Impact** | Critical — data loss at go-live could require returning to the old system, significant rework, and loss of stakeholder confidence. |
| **Risk Level** | High (1 × 4 = 4) — classified High due to Critical impact even at Low probability |
| **Mitigation Strategy** | 1. The go-live cutover plan (FR-SEC-007) must include a verified rollback procedure: at a defined checkpoint, the team can revert to the previous system state within 4 hours. 2. Perform a full database backup immediately before cutover begins. 3. Execute the cutover in a staging environment first (a dry run) at least 2 weeks before production go-live. 4. Cutover is executed during a weekend or public holiday — not during a business day — to minimise operational disruption. 5. A minimum 2-week parallel operation period follows cutover for validation. |
| **Residual Risk** | Very Low — dry run, backup, and rollback procedure reduce data loss probability to near zero. |
| **Owner** | Peter Bamuhigire / BIRDC IT |

---

## Risk R-016: Key Person Dependency — Peter Bamuhigire as Sole Architect

| Field | Detail |
|---|---|
| **Risk ID** | R-016 |
| **Description** | Peter Bamuhigire is the sole architect, consultant, and requirements author for the BIRDC ERP project. All 6 SRS documents, the Traceability Matrix, and the entire project knowledge base reside primarily with Peter. If Peter is unavailable for an extended period (illness, competing engagement), the project cannot progress. |
| **Category** | Operational (O) |
| **Probability** | Low — planned unavailability is manageable; unplanned unavailability is the risk. |
| **Impact** | High — project would effectively pause until Peter or a replacement consultant with equivalent knowledge is available. |
| **Risk Level** | Medium (1 × 3 = 3) |
| **Mitigation Strategy** | 1. All project artefacts are documented to a level where a replacement consultant with equivalent experience could continue the project with 1–2 weeks of onboarding. 2. The SRS suite, technical specification, and context files are the complete knowledge base — hosted in the project workspace at BIRDC's disposal. 3. Peter to complete a project handover document at each phase gate summarising the current state and next steps. 4. BIRDC IT Administrator to be included in all technical design reviews so internal knowledge is built progressively. |
| **Residual Risk** | Medium — no mitigation fully eliminates key person risk on a single-consultant engagement. |
| **Owner** | Peter Bamuhigire / BIRDC Director |

---

## Risk R-017: URA EFRIS Regulation Change During Development

| Field | Detail |
|---|---|
| **Risk ID** | R-017 |
| **Description** | The URA EFRIS API specification may be updated by URA during the development period. A regulatory change to EFRIS requirements (new mandatory fields, changed API version, updated FDN format) could invalidate completed EFRIS integration work and require rework. |
| **Category** | External (E) |
| **Probability** | Low — EFRIS is an established system; major API changes are infrequent but not impossible. |
| **Impact** | High — if the EFRIS integration module must be reworked after completion, Phase 7 go-live is delayed. |
| **Risk Level** | Medium (1 × 3 = 3) |
| **Mitigation Strategy** | 1. Design the EFRIS integration as a separate, isolated module with a defined API adapter interface. Changes to EFRIS API format require changes only in the adapter, not in the invoice or POS modules. 2. Peter to subscribe to URA EFRIS developer communications and tax circular notifications. 3. The EFRIS module is delivered in Phase 7 (last phase) — by which time the regulatory environment is known. |
| **Residual Risk** | Low — adapter isolation reduces rework scope to a bounded module. |
| **Owner** | Peter Bamuhigire |

---

## Risk R-018: NSSF or PAYE Rate Change During Development

| Field | Detail |
|---|---|
| **Risk ID** | R-018 |
| **Description** | Uganda Parliament may amend the NSSF Act or Income Tax Act during the development period (development spans approximately 18 months), changing NSSF contribution rates or PAYE tax bands. If these rates are hardcoded, the payroll module would be non-compliant from go-live. |
| **Category** | External (E) |
| **Probability** | Low — NSSF and PAYE rates are amended infrequently; typically tied to the annual national budget in June. |
| **Impact** | High — non-compliant payroll calculations create URA and NSSF liabilities for every payroll run after the rate change. |
| **Risk Level** | Medium (1 × 3 = 3) |
| **Mitigation Strategy** | 1. Design Covenant DC-002 mandates that PAYE tax bands and NSSF rates are configuration parameters, not hardcoded values. This is already specified in FR-PAY-002 and FR-PAY-003. 2. The Finance Director can update rates via the UI within minutes of a regulation change — no developer involvement required. 3. Peter to monitor the annual Uganda Budget Speech (typically June) for any announced changes and update the system configuration before the effective date. |
| **Residual Risk** | Very Low — configuration-driven rates are the primary mitigation; rate changes require a UI update only. |
| **Owner** | BIRDC Finance Director / Peter |
