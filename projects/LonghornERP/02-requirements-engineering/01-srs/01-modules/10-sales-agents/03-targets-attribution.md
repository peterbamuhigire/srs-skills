# Sales Targets and Attribution

## 3.1 Overview

This section defines requirements for setting sales targets per agent and for attributing posted sales invoices to agents. Accurate attribution is the foundation of commission calculation; every commission-eligible sale must be traceable to exactly one agent.

## 3.2 Sales Target Setting

**FR-AGENT-011** — When an authorised user creates a target for an agent by submitting the **Set Target** form, the system shall store a target record containing **Agent ID**, **Period Type** (`Monthly` or `Quarterly`), **Period Start Date**, **Period End Date**, **Target Amount** (currency: tenant base currency), and **Target Units** (optional). The system shall reject the form if a target for the same agent and overlapping period already exists, returning error `DUPLICATE_TARGET_PERIOD`.

**Test oracle:** Submitting two monthly targets for agent `AGT-20260401-001` for April 2026 results in the second submission being rejected with `DUPLICATE_TARGET_PERIOD`.

---

**FR-AGENT-012** — When an authorised user submits a bulk target upload via a CSV file conforming to the published template, the system shall validate each row, import all valid rows, and return a summary report showing the count of rows imported, the count of rows rejected, and the rejection reason for each failed row. The import shall complete within 60 seconds for files containing up to 500 rows.

**Test oracle:** A 500-row CSV with 10 deliberately invalid rows produces a summary showing 490 imported and 10 rejected with named reasons, within 60 seconds.

---

**FR-AGENT-013** — When a target period is active, the system shall calculate and display each agent's **Target Achievement Percentage** as:

$$TargetAchievement = \frac{AttributedSales}{TargetAmount} \times 100$$

The value shall update within 5 minutes of a new invoice being attributed to the agent.

**Test oracle:** After attributing a new invoice of UGX 500,000 to an agent with a monthly target of UGX 2,000,000, the displayed **Target Achievement Percentage** updates to at least 25% within 5 minutes.

---

**FR-AGENT-014** — When a target period closes (end date passes), the system shall automatically mark the target record status as `Closed`, calculate the final **Target Achievement Percentage**, and make the target available in historical target reports. No manual intervention shall be required to close a period.

**Test oracle:** On the day after a target's end date, a scheduled process runs (no later than 06:00 EAT) and sets the target status to `Closed` with a final achievement value.

## 3.3 Sales Attribution

**FR-AGENT-015** — When a sales invoice is posted in the Sales and Invoicing module and the invoice contains a populated **Agent** field, the system shall automatically create an attribution record linking the invoice to the specified agent, recording **Invoice ID**, **Agent ID**, **Attribution Date**, **Invoice Amount**, and **Attributed Amount** (which may differ from invoice amount when only specific line items are commissionable).

**Test oracle:** Posting an invoice with a valid **Agent** field causes an attribution record to appear in the attribution ledger within 30 seconds.

---

**FR-AGENT-016** — When an authorised user manually attributes a posted invoice to an agent via the **Manual Attribution** action, the system shall require a justification note, record the user performing the action, and flag the attribution record with source type `Manual` for audit purposes.

**Test oracle:** A manually attributed invoice displays source type `Manual`, the justification note, and the attributing user's name in the attribution detail view.

---

**FR-AGENT-017** — When an invoice is already attributed to one agent and an authorised user re-attributes it to a different agent, the system shall void the original attribution record with a timestamp, create a new attribution record for the new agent, and require a justification note. The system shall not allow re-attribution of an invoice that has been included in a finalised commission run.

**Test oracle:** Attempting to re-attribute an invoice included in a finalised commission run returns error `ATTRIBUTION_LOCKED_FINALISED_RUN`.

---

**FR-AGENT-018** — When the tenant configuration flag `RequireSplitAttribution` is set to `true`, the system shall allow an invoice to be attributed to up to 3 agents with individual percentage splits that must sum to exactly 100%. The system shall reject the split if the sum deviates from 100% by any non-zero amount.

**Test oracle:** Entering splits of 40%, 35%, and 26% (total 101%) returns error `SPLIT_SUM_NOT_100`. Entering 40%, 35%, and 25% is accepted.

---

**FR-AGENT-019** — When an authorised user views the **Attribution Report** for a date range, the system shall display all attributed invoices with columns for **Invoice ID**, **Customer Name**, **Invoice Date**, **Agent Name**, **Territory**, **Invoice Amount**, **Attributed Amount**, and **Attribution Source** (`Auto` or `Manual`). The report shall load within 3 seconds for date ranges spanning up to 90 days for tenants with up to 10,000 attributed invoices.

**Test oracle:** Requesting a 90-day attribution report for a tenant with 10,000 records renders within 3 seconds.

---

**FR-AGENT-020** — When a posted invoice with an **Agent** field contains a product not in the agent's active product list and `AttributionRestrictToActiveProducts = true`, the system shall skip attribution for that line item, log a warning entry in the attribution exceptions log, and notify the tenant administrator via the in-app notification channel within 5 minutes.

**Test oracle:** Posting such an invoice produces an exception log entry and an in-app notification to the administrator within 5 minutes; the invoice total excluding the non-assigned product line is attributed, not the full invoice amount.
