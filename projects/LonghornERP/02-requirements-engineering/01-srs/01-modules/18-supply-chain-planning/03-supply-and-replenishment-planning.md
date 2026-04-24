# Supply and Replenishment Planning

**FR-SCP-009** - The system shall generate a supply plan from the approved consensus-demand plan using current inventory positions, open supply, lead times, sourcing rules, and planning policies for the selected horizon.

**FR-SCP-010** - The supply-planning engine shall respect tenant-configured sourcing rules, minimum order quantities, lot sizes, replenishment frequencies, lead times, and preferred supply source by item-location.

**FR-SCP-011** - When available supply or capacity is insufficient to satisfy planned demand, the system shall surface constrained-supply exceptions showing item, location, shortage quantity, constrained resource or source, and first projected shortage date.

**FR-SCP-012** - The system shall generate replenishment recommendations in the form of planned purchase, planned production, or planned transfer proposals, with each recommendation linked to its originating demand-plan and policy version.

**FR-SCP-013** - During constrained-supply conditions, the system shall support allocation rules based on service class, customer priority, or tenant-defined segment priority, and it shall show the quantity allocated and quantity deferred by rule.

**FR-SCP-014** - The system shall provide a planner exception workbench through which authorised users can filter, prioritise, assign, comment on, and resolve shortage, capacity, late-supply, or policy-violation exceptions.

**FR-SCP-015** - When a supply-plan version is released, the system shall export or publish only the approved recommendations to downstream execution modules; it shall not auto-create execution transactions without a release action.

**FR-SCP-016** - The system shall preserve plan-version history such that each supply-plan run records its parent demand-plan version, policy version, planning horizon, and release status.
