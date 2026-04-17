# Production Costing and Overhead Absorption

## 7.1 Production Cost Components

**FR-MFG-035** — The system shall accumulate the following cost components for each production order: (a) raw material cost (from RMI transactions), (b) direct labour cost (from timesheets linked to the production order), (c) machine/overhead cost (from overhead absorption rules), and (d) scrap cost (from scrap recording).

**FR-MFG-036** — The total finished goods cost shall be computed as:

$Cost_{FG} = Cost_{RM} + Cost_{Labour} + Cost_{Overhead} - Value_{ByProduct}$

where each component is the sum of actual costs recorded against the production order during its lifecycle.

## 7.2 Labour Costing

**FR-MFG-037** — The system shall support employee timesheet entries linked to a production order; each timesheet line shall record: employee, production order, task description, hours worked, and the labour rate (sourced from the employee's configured production labour rate or grade rate).

**FR-MFG-038** — When a timesheet entry is approved, the system shall post the labour cost to the WIP account using the formula: $LabourCost = HoursWorked \times LabourRate$ and shall debit the WIP account, crediting the Labour Absorbed account.

## 7.3 Overhead Absorption

**FR-MFG-039** — The system shall support machine-based overhead absorption: each work centre shall carry a configured overhead rate (UGX per machine hour); when a production order uses a work centre, the user records machine hours, and the system posts: $OverheadCost = MachineHours \times OverheadRate$.

**FR-MFG-040** — The system shall support percentage-based overhead absorption as an alternative: overhead is computed as a percentage of direct material cost: $OverheadCost = Cost_{RM} \times OverheadRate_{pct}$.

## 7.4 Yield and Variance Analysis

**FR-MFG-041** — When a production order is completed, the system shall compute:

$YieldVariance = (ActualOutput - PlannedOutput) \times StandardCost$

A positive variance (higher actual than planned output) reduces unit cost; a negative variance increases it. Both variances shall be posted to a configurable Yield Variance GL account.

**FR-MFG-042** — The system shall generate a production variance report per period showing: production order, standard cost, actual cost, material variance, labour variance, overhead variance, yield variance, and total cost variance; this report shall be the primary input for monthly production performance review.
