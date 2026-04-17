# 2. Overall Description

## 2.1 Product Perspective

Phase 4 operates as an integrated sub-system within the BIRDC ERP. It is not a standalone product. The Manufacturing & Production module (F-011) and the Quality Control & Laboratory module (F-012) share data with the following existing modules:

| Interface Direction | Consuming Module | Providing Module | Data Exchanged |
|---|---|---|---|
| F-011 reads | F-003 (Inventory) | F-011 | Raw material stock balance and FIFO cost layers for material requisition |
| F-011 writes | F-003 (Inventory) | F-011 | Finished goods and by-product receipt into saleable inventory (QC-gated) |
| F-011 writes | F-005 (GL) | F-011 | WIP journal entries, production completion COGS posting, overhead absorption |
| F-011 reads | F-013 (HR) | F-011 | Worker registry for job card assignment and labour cost capture |
| F-012 reads | F-011 | F-012 | Production order batch IDs for QC inspection scheduling |
| F-012 writes | F-011 | F-012 | QC approval status that releases or blocks finished goods transfer |
| F-012 writes | F-009 (Procurement) | F-012 | Incoming raw material quality grade driving farmer payment price tier |

The Factory Floor App (Android) communicates with the ERP via the mobile REST API documented in the tech stack. All offline data is stored in Room (SQLite) and synchronised via WorkManager.

## 2.2 Product Functions — Summary

**F-011 Manufacturing & Production** provides:

- Recipe (BOM) definition and version control
- Circular economy recipe modelling for banana peel → biogas and waste water → bio-slurry
- Production order management across the full lifecycle: Plan → Materials Reserved → In Progress → QC Check → Completed → Closed
- Material requisition with WIP accounting
- Job cards with step-by-step instructions, worker assignment, and quality checkpoints
- WIP location tracking across 6 processing stations
- Mass balance verification with ±2% tolerance enforcement (BR-008)
- Production costing: FIFO raw materials + direct labour + absorbed overhead
- Equipment register and capacity management
- Factory Floor Android application with offline capability

**F-012 Quality Control & Laboratory** provides:

- Configurable inspection templates with multiple parameter types
- Incoming material inspection linked to procurement quality grading
- In-process QC checkpoints within job cards
- Finished product QC and Certificate of Analysis generation
- Export-grade CoA for 5 destination markets [CONTEXT-GAP: GAP-010]
- Statistical Process Control with X-bar and R-charts, Cp and Cpk
- Non-Conformance Reports with corrective action tracking
- Batch quality status management integrated with inventory dispatch controls
- Laboratory equipment calibration tracking
- Incubation and maturation tracking for fermented products (banana wine)

## 2.3 User Classes and Characteristics

| User Class | Count | Technical Skill | Primary Phase 4 Touch |
|---|---|---|---|
| Factory / Production Manager (STK-009) | 1 | Moderate — ERP-trained | Production order management, scheduling, costing reports |
| Production Supervisors | ~5 | Low-moderate | Factory Floor App — job card execution, attendance, completion quantities |
| Factory Floor Workers | ~80 | Low | Job card view, time recording on Factory Floor App |
| QC Manager / Lab Manager (STK-010) | 1 | High — laboratory trained | Inspection templates, SPC, CoA issuance, NCR management |
| QC Analysts / Lab Technicians | ~5 | Moderate | Inspection result entry, CoA review, equipment records |
| Finance Director (STK-002) | 1 | High — financial | Production costing reports, WIP balance, variance review |
| IT Administrator (STK-003) | 1 | Very high | Overhead rate configuration, system integration maintenance |

DC-001 applies: every screen used daily by production supervisors and QC analysts must be self-discoverable without reading a manual.

## 2.4 Operating Environment

| Dimension | Specification |
|---|---|
| Web application server | Apache / Nginx on BIRDC on-premise hardware, Nyaruzinga, Bushenyi |
| Database | MySQL 9.1 InnoDB |
| Backend | PHP 8.3+ with strict types, PSR-4/PSR-12 |
| Factory Floor App | Android 8.0 (API 26) minimum; Kotlin, Jetpack Compose, Room, WorkManager |
| Connectivity | Intermittent at Bushenyi — Factory Floor App must operate fully offline (DC-005) |
| Network | LAN for web application; Factory Floor App syncs over LAN Wi-Fi or mobile data |

## 2.5 Design and Implementation Constraints

All 7 Design Covenants (DC-001 through DC-007) apply to every requirement in this document. Specific constraints most relevant to Phase 4:

- **DC-002 (Configuration over code):** Overhead absorption rates, recipe ingredient quantities, SPC specification limits, inspection template parameters, and CoA format configurations must all be maintained via the UI without developer involvement.
- **DC-003 (Audit readiness):** Every production event — material issue, operation completion, QC result entry, CoA issuance — creates an immutable audit record.
- **DC-005 (Offline-first):** The Factory Floor App stores production order data, job card instructions, and completion entry forms in Room (SQLite). All offline actions sync when connectivity is restored.
- **DC-007 (Replicable):** All BIRDC-specific production parameters (processing stations, by-product types, overhead categories) must reside in configuration tables, not in application code.

## 2.6 Assumptions and Dependencies

1. Phase 1 Inventory (F-003) is live and maintaining raw material stock balances with FIFO cost layers before any production order can be confirmed.
2. Phase 2 GL (F-005) is live with the full chart of accounts before WIP journal entries can be posted.
3. Phase 3 Procurement (F-009) provides incoming batch IDs with farmer quality grades before incoming material inspection can be linked to payment pricing.
4. Export CoA parameter sets for all 5 destination markets (South Korea, EU/Italy, Saudi Arabia, Qatar, USA) must be provided by the BIRDC QC Manager before export CoA templates can be built [CONTEXT-GAP: GAP-010].
5. The production overhead absorption rate is a configurable value; the Finance Director sets the initial rate before Phase 4 go-live.
