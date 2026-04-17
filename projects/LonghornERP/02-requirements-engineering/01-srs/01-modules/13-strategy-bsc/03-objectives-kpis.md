# Strategic Objectives and KPI Definition

## 3.1 Overview

Strategic objectives translate the tenant's strategy into measurable commitments within each BSC perspective. KPIs operationalise those objectives by defining the specific measure, formula, unit, target, and collection frequency. The requirement hierarchy is: Perspective → Strategic Objective → KPI.

## 3.2 Strategic Objective Definition

**FR-BSC-011:** The system shall allow a `strategy.admin` user to create a strategic objective by supplying the following mandatory fields: objective title (free text, max 160 characters), parent perspective (selected from active perspectives), strategic theme (selected from active themes), objective owner (selected from active tenant user accounts), and target period (fiscal year or custom date range); the system shall assign a unique system-generated identifier in the format `OBJ-{NNNN}` upon creation.

**FR-BSC-012:** The system shall allow a `strategy.admin` user to edit any field of a strategic objective, and shall require a change reason (free text, max 300 characters) when editing the objective title or target period of an objective that already has at least 1 actual KPI data point recorded against it.

**FR-BSC-013:** The system shall allow a `strategy.admin` user to set the status of a strategic objective to one of four states: Active, On Hold, Achieved, or Cancelled; the system shall prevent deletion of any objective that has linked KPIs or linked initiatives, returning an error listing the linked item counts.

**FR-BSC-014:** The system shall display the list of strategic objectives grouped by perspective on the BSC configuration screen, sortable by objective identifier, owner, status, or display order, and filterable by strategic theme and status.

## 3.3 KPI Definition

**FR-BSC-015:** The system shall allow a `strategy.admin` user to create a KPI by supplying the following mandatory fields: KPI name (free text, max 160 characters), parent strategic objective (selected from active objectives), unit of measure (free text, max 40 characters — e.g., "%", "UGX", "count", "days"), data source type (Manual or Auto-Pull), measurement frequency (Daily, Weekly, Monthly, Quarterly, or Annual), and the data collection owner (active user account); the system shall assign a unique identifier in the format `KPI-{NNNN}` upon creation.

**FR-BSC-016:** The system shall allow a `strategy.admin` user to define a KPI formula as a free-text expression (max 500 characters) using operand tokens referencing other KPIs or ERP data fields (e.g., `[GL:Revenue] / [GL:Headcount]`); the system shall validate that all referenced tokens resolve to defined data sources at save time, and shall return a validation error identifying any unresolvable token.

**FR-BSC-017:** The system shall allow a `strategy.admin` user to set a numeric target value and a baseline value for each KPI, both typed as decimal numbers with up to 4 decimal places; target and baseline values shall be period-specific, allowing different targets per fiscal year or quarter.

**FR-BSC-018:** The system shall allow a `strategy.admin` user to configure RAG threshold boundaries for each KPI as two percentage values — `amber_threshold` and `red_threshold` — where:

- Green: $Score \geq amber\_threshold$
- Amber: $red\_threshold \leq Score < amber\_threshold$
- Red: $Score < red\_threshold$

and the system shall enforce that `red_threshold < amber_threshold ≤ 100`; submission violating this constraint shall be rejected with a validation error.

**FR-BSC-019:** The system shall display a KPI detail panel showing: KPI identifier, name, objective link, formula, unit, current actual, target, score, RAG status, last updated timestamp, and data collection owner, when an authorised user selects any KPI from the scorecard or KPI list screen.

**FR-BSC-020:** The system shall allow a `strategy.admin` user to mark a KPI as *inverse polarity* (lower actual is better — e.g., cost or defect rate), in which case the scoring formula shall be inverted: $Score = (Target \div Actual) \times 100$; the system shall display an inverse-polarity indicator beside the KPI name throughout the UI.

## 3.4 KPI-to-Objective Linkage Validation

**FR-BSC-021:** The system shall enforce that every KPI is linked to exactly 1 active strategic objective; the system shall prevent saving a KPI record without a valid `objective_id` foreign key reference.

**FR-BSC-022:** The system shall display an aggregate objective score on each strategic objective card, calculated as the unweighted arithmetic mean of the current scores of all active KPIs linked to that objective:

$$ObjectiveScore = \frac{\sum_{i=1}^{n} KPIScore_i}{n}$$

where $n$ is the count of active KPIs linked to the objective; when $n = 0$, the objective score shall display as "No data."
