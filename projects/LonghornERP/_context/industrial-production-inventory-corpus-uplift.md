# Industrial Production and Inventory Corpus Uplift

## Purpose

This note captures implementable LonghornERP and BIRDC-ERP enhancement decisions derived from the supplied EPUB corpus without copying source text:

- `CLTD 2022-Module 7.epub`
- `module 4 - Internal Operations and inventory (APICS).epub`
- `Modeling and Optimization in Manufacturing Toward Greener Production by Integrating Computer Simulation.epub`
- `Manufacturing Facilities Design & Material Handling.epub`
- `Orlicky's Material Requirements Planning.epub`
- `Production Planning and Industrial Scheduling: Examples, Case Studies and Applications.epub`

## Derived Capability Themes

The corpus reinforces that inventory, production planning, scheduling, warehousing, material handling, and green manufacturing are separate but connected disciplines. The ERP should therefore improve its manufacturing and inventory modules around these capability themes:

| Theme | ERP implication |
|---|---|
| MRP discipline | Planning must net gross requirements against stock, reservations, scheduled receipts, lot-sizing rules, lead times, and BOM effectivity before proposing buy or make actions. |
| Master scheduling | Finished-goods and major component plans need frozen, slushy, and liquid time fences so planners can control short-term disruption. |
| Capacity and scheduling | Production orders must be checked against work-centre capacity, calendars, setup time, run time, sequence-dependent changeovers, and due-date penalties. |
| Warehouse execution | Inventory accuracy depends on location, slotting, storage medium, picking method, replenishment, staging, and congestion controls, not only item balances. |
| Facility and material flow | Factory layouts should preserve explicit from-to flows, aisle constraints, transfer distances, equipment constraints, and future expansion allowances. |
| Green manufacturing | Production records should capture energy, water, material yield, scrap, emissions proxy, rework, and circular-economy recovery metrics. |
| Simulation and optimization | Planning should support scenario runs before commitment, with objective functions and constraints stored as decision evidence. |

## Enhancement Decisions

1. LonghornERP Supply Chain Planning should gain a clear MRP and finite-capacity planning layer rather than relying only on reorder alerts.
2. LonghornERP Manufacturing should add finite scheduling, setup/changeover logic, and green production measurement beside the existing MES execution requirements.
3. LonghornERP Inventory should add warehouse slotting, pick-path, replenishment, and storage-capacity requirements to make warehouse operations auditable.
4. BIRDC-ERP should keep its current recipe, mass-balance, QC, and circular-economy strengths, but add material availability time-phasing, factory flow/layout constraints, energy and water intensity, and operation-level dispatch priority.
5. Database and service designs should retain calculation lineage: every recommendation, schedule, policy, and simulation result must be linked to source demand, inventory, BOM, routing, capacity, and rule versions.

## Acceptance Bar

The enhanced specifications should allow a reviewer to verify:

- planned orders explain why they exist and what demand they cover;
- production schedules explain why a sequence was chosen;
- warehouse tasks explain where stock should be stored, picked, replenished, or staged;
- production cost and sustainability metrics reconcile to source events;
- scenario decisions remain auditable after execution changes.
