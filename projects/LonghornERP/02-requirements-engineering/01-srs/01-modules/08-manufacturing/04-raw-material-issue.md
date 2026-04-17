# Raw Material Issue

## 4.1 Issue to Production

**FR-MFG-017** — When a production order moves to "In Progress" status, the system shall generate a raw material issue (RMI) document listing each BOM component, the gross required quantity (including wastage), the reserved stock balance, and the available bin locations.

**FR-MFG-018** — When the user confirms the RMI, the system shall post stock deductions for each component from the source warehouse to the "WIP" virtual stock location and shall credit the GL stock account, debiting the WIP account.

**FR-MFG-019** — When FEFO is enabled for a raw material component (`FR-ADVINV-022`), the system shall apply FEFO batch selection automatically at the time of RMI generation.

## 4.2 Partial Issues and Back-Flush

**FR-MFG-020** — The system shall support partial raw material issue: a production order may receive multiple issues across its duration; the system shall track the cumulative issued quantity per component and flag over-issues (issued quantity > BOM requirement).

**FR-MFG-021** — The system shall support a back-flush mode for items where physical counting at issue is impractical: when the production order is completed, the system shall automatically compute and post the theoretical raw material consumption based on actual output quantity and BOM quantities, rather than requiring manual issue.

## 4.3 Issue Substitutions

**FR-MFG-022** — When a required component is unavailable, the system shall allow a production supervisor to substitute an alternate component (if configured in the BOM as a substitute); the substitution shall be recorded in the production order with the original component, substitute component, quantities, and the approving supervisor's identity.
