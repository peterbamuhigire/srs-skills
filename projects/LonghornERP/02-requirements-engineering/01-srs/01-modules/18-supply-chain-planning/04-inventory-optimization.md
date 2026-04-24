# Inventory Optimization

**FR-SCP-017** - The system shall allow an authorised user to define service classes and inventory-policy segments by item, location, product family, or channel, and each planning segment shall carry a target service objective and default replenishment policy.

**FR-SCP-018** - The system shall calculate safety stock, target stock, and reorder policy outputs for each planned item-location using tenant-configured logic and the current planning-policy version.

**FR-SCP-019** - When the `ADV_INVENTORY` module is active, the system shall support multi-echelon inventory-policy logic across upstream and downstream stocking points; when `ADV_INVENTORY` is not active, the system shall fall back to single-echelon policy calculations.

**FR-SCP-020** - The system shall provide inventory-health dashboards showing at minimum projected inventory coverage, projected stockouts, excess inventory, slow-moving inventory exposure, and working-capital impact by item, location, and segment.

**FR-SCP-021** - The system shall version every inventory-policy set with effective date, owner, and approval status, and historical planning runs shall remain linked to the policy version that was active when the run was generated.

**FR-SCP-022** - When an authorised user applies a manual inventory-policy override to an item-location, the system shall require reason code, approval note when above the tenant-defined threshold, and an expiry date for the override.
