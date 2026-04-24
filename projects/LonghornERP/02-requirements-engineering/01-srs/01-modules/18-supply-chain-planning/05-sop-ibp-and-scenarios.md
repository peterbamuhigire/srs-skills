# S&OP / IBP and Scenario Management

**FR-SCP-023** - The system shall support a monthly S&OP / IBP cycle with configured milestones for demand review, supply review, executive review, and final plan release.

**FR-SCP-024** - For each S&OP / IBP cycle, the system shall display completion status, owner, due date, and blocker summary for each required review step.

**FR-SCP-025** - The system shall translate an approved demand or supply plan into financial views showing at minimum projected revenue, projected inventory value, projected procurement exposure, and projected margin impact for the selected planning horizon.

**FR-SCP-026** - The system shall allow an authorised user to create a scenario by cloning an existing demand-plan or supply-plan version into an isolated sandbox that does not affect the live released plan.

**FR-SCP-027** - The system shall allow authorised users to compare scenarios against the current approved plan using service, inventory, shortage, and financial metrics, and it shall preserve the comparison result as part of the decision record.

**FR-SCP-028** - The system shall support decision-right and escalation-threshold rules such that unresolved planning exceptions above a tenant-defined service, revenue, or inventory-risk threshold are escalated into the executive review agenda.

**FR-SCP-029** - Every change to a released plan, scenario decision, or executive approval outcome shall be stored in an immutable plan-change log containing acting user, timestamp, changed object, old value, new value, and reason.

**FR-SCP-030** - When an approved operating plan is published, the system shall notify the relevant planning and execution owners and mark the plan version as the current released version for the planning horizon.
