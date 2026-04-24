# Demand Planning

**FR-SCP-001** - The system shall ingest demand signals from sales history, open sales orders, approved promotion inputs, and authorised manual-import files, and it shall retain the source reference for each imported planning signal.

**FR-SCP-002** - The system shall generate a statistical baseline forecast by item, location, and time bucket for an authorised planning horizon using historical demand and tenant-configured forecasting rules.

**FR-SCP-003** - The system shall allow an authorised planner to classify items into planning segments and assign a default forecasting method, review cadence, and override threshold per segment.

**FR-SCP-004** - When a user overrides a baseline forecast, the system shall require reason code, owner, effective horizon, and override note, and it shall preserve the baseline value and overridden value for audit and bias analysis.

**FR-SCP-005** - The system shall support new-product and end-of-life forecast handling using designated lifecycle flags, manual seeding rules, and end-of-life demand taper assumptions without requiring historical data for every new item.

**FR-SCP-006** - The system shall provide a consensus-demand review workflow in which authorised users can review, comment on, and approve a demand-plan version before it becomes the active demand input for downstream planning.

**FR-SCP-007** - The system shall support a frozen horizon by preventing forecast edits inside the tenant-defined near-term window unless the acting user has override permission and records an override reason.

**FR-SCP-008** - The system shall provide forecast-performance views showing at minimum forecast accuracy, forecast bias, override frequency, and high-variance items for a selected horizon, item scope, and location scope.
