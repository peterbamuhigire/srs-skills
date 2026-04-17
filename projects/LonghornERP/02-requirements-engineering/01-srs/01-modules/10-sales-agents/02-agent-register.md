# Agent Register

## 2.1 Overview

The Agent Register is the master data repository for all sales agents within a tenant. Every agent record must be created and approved before the agent can be attributed sales, assigned targets, or included in a commission run. This section defines requirements for agent record creation, territory assignment, and product assignment.

## 2.2 Agent Record Management

**FR-AGENT-001** — When an authorised user submits the **Create Agent** form with all mandatory fields populated, the system shall create an agent record with status `Active` and return a system-generated **Agent ID** in the format `AGT-{YYYYMMDD}-{NNN}`, where `NNN` is a zero-padded sequence unique within the tenant.

**Mandatory fields:** **Full Name**, **National ID / Passport Number**, **Date of Birth**, **Gender**, **Primary Phone Number** (validated as a valid Uganda or registered African country mobile number), **Email Address**, **Residential Address**, **Region**, and **Join Date**.

**Test oracle:** Given a valid form submission, the system creates the record within 3 seconds, assigns a unique **Agent ID**, and the record is immediately retrievable via the agent list filtered by status `Active`.

---

**FR-AGENT-002** — When an authorised user deactivates an agent record by setting status to `Inactive`, the system shall prevent new sales attributions and target assignments for that agent while retaining all historical records and commission history intact.

**Test oracle:** After deactivation, any attempt to attribute an invoice to that agent returns error `AGENT_INACTIVE` and the agent does not appear in active attribution dropdowns.

---

**FR-AGENT-003** — When an authorised user updates any field on an existing agent record, the system shall record a timestamped audit entry capturing the field name, previous value, new value, the user who made the change, and the change timestamp.

**Test oracle:** After an update, the audit log for the agent record contains exactly one new entry with all five captured data points.

---

**FR-AGENT-004** — When an authorised user uploads an agent profile photo (JPEG or PNG, maximum 2 MB), the system shall store the image, resize it to 256 × 256 pixels, and display it on the agent record and the agent portal header.

**Test oracle:** After upload, the stored image dimensions are 256 × 256 px and the image is visible on both the admin agent record page and the agent portal within 5 seconds.

---

**FR-AGENT-005** — When an authorised user searches the agent register using the **Search Agents** field, the system shall return all matching agents within 1 second, filtering by partial match on **Full Name**, **Agent ID**, or **Primary Phone Number**.

**Test oracle:** A search query of 3 or more characters returns results within 1 second for a tenant with up to 1,000 agent records.

## 2.3 Territory Assignment

**FR-AGENT-006** — When an authorised user assigns a territory to an agent via the **Assign Territory** action, the system shall link the agent to exactly one territory at a time, record the effective start date, and display the territory name on the agent record summary card.

**Test oracle:** After assignment, the agent record reflects the territory name and start date, and the territory appears in all attribution and reporting filters associated with that agent.

---

**FR-AGENT-007** — When an authorised user reassigns an agent to a new territory, the system shall close the previous territory assignment with an end date of the day before the new assignment's effective date, preserving the full territory history for audit and reporting.

**Test oracle:** The agent's territory history list shows the closed previous assignment with a non-null end date and the new active assignment with a null end date.

---

**FR-AGENT-008** — When an authorised user views the **Territory Map** screen, the system shall display all active agents grouped by their assigned territory, with a count of agents per territory and a list of unassigned agents flagged in a distinct colour.

**Test oracle:** The territory map renders within 3 seconds and the sum of agents shown across all territories plus unassigned agents equals the total active agent count.

## 2.4 Product Assignment

**FR-AGENT-009** — When an authorised user assigns one or more products to an agent via the **Manage Active Products** panel, the system shall restrict sales attribution for that agent to only the assigned products unless the tenant configuration flag `AttributionRestrictToActiveProducts` is set to `false`.

**Test oracle:** With `AttributionRestrictToActiveProducts = true`, an attempt to attribute an invoice containing a non-assigned product to the agent returns error `PRODUCT_NOT_ASSIGNED_TO_AGENT`.

---

**FR-AGENT-010** — When an authorised user removes a product from an agent's active product list, the system shall retain all historical attribution records for that product and agent pair without modification, and shall prevent new attributions of that product to the agent from the removal date forward.

**Test oracle:** Post-removal, existing attributed invoices remain visible in agent history; new attribution attempts for the removed product return error `PRODUCT_NOT_ASSIGNED_TO_AGENT`.
