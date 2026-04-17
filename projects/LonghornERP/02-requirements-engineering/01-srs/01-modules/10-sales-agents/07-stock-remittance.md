# Agent Stock Management, Remittance Verification, and Daily Summaries

## 7.1 Overview

Some agents act as field distributors who hold physical inventory on behalf of the tenant. This section defines requirements for issuing stock to agents, tracking balances, processing returns, verifying cash remittances collected by agents, and generating daily activity summaries.

## 7.2 Agent Stock Management

**FR-AGENT-053** — When an authorised user issues stock to an agent via the **Issue Stock to Agent** form, the system shall require **Agent ID**, **Product ID**, **Quantity**, **Issue Date**, and an optional **Delivery Note Reference**. Upon saving, the system shall deduct the issued quantity from the tenant's main inventory ledger, credit the agent's stock account with the same quantity, and create a timestamped **Stock Issue Record**. The system shall reject the issuance if the available quantity in the main inventory ledger is less than the requested quantity, returning error `INSUFFICIENT_STOCK`.

**Test oracle:** Issuing 100 units of a product with 80 units available returns `INSUFFICIENT_STOCK`. Issuing 50 units with 80 available reduces the main ledger by 50 and adds 50 to the agent's stock balance.

---

**FR-AGENT-054** — When an authorised user records a stock return from an agent via the **Agent Stock Return** form, the system shall require **Agent ID**, **Product ID**, **Returned Quantity**, **Return Date**, and **Condition** (`Good`, `Damaged`). Good-condition returns shall credit the main inventory ledger; damaged returns shall post to the configured damage write-off account. The agent's stock balance shall be reduced by the returned quantity in both cases.

**Test oracle:** A return of 10 units in `Good` condition for agent `AGT-20260401-001` increases the main ledger by 10 and decreases the agent's balance by 10. A return of 5 `Damaged` units reduces the agent's balance by 5 and posts a write-off entry, not a ledger credit.

---

**FR-AGENT-055** — When an authorised user views an agent's **Stock Balance** panel, the system shall display the current balance for each product assigned to the agent, computed as:

$$StockBalance_{Agent} = \sum Issued - \sum Returned - \sum SoldAttributed$$

where $SoldAttributed$ represents quantities tied to attributed and invoiced sales. The balance shall be accurate as of no later than 5 minutes before the page load.

**Test oracle:** After issuing 100 units, attributing sales of 30 units, and returning 10 units (good condition), the agent's displayed balance for that product is 60 units.

---

**FR-AGENT-056** — When an agent's stock balance for any product falls below the tenant-configured **Reorder Alert Level** for that product, the system shall send an in-app notification to the tenant administrator and the agent's assigned territory manager within 5 minutes of the balance drop.

**Test oracle:** Setting reorder alert level to 20 units and attributing a sale that drops the agent's balance from 22 to 18 units triggers a notification within 5 minutes.

---

**FR-AGENT-057** — When an authorised user performs a **Stock Reconciliation** for an agent by submitting a physical count, the system shall compute the variance as:

$$Variance = PhysicalCount - SystemBalance$$

A positive variance shall generate a stock gain entry; a negative variance shall generate a stock loss entry. Both entries shall require an authorised user's approval before posting to the inventory ledger.

**Test oracle:** A physical count of 45 units against a system balance of 50 units produces a variance of −5, a pending stock loss entry of 5 units, and the loss is not posted until approved.

## 7.3 Remittance Verification

**FR-AGENT-058** — When an agent collects cash or mobile money on behalf of the tenant, an authorised user shall record the collection via the **Record Remittance** form, specifying **Agent ID**, **Collection Date**, **Amount Collected**, **Collection Method** (`Cash` or `Mobile Money`), and **Reference Number** (mandatory for mobile money). The system shall create a **Remittance Record** with status `Unverified`.

**Test oracle:** Submitting the form with `Collection Method = Mobile Money` and a null **Reference Number** is rejected with error `REFERENCE_REQUIRED_FOR_MOBILE_MONEY`.

---

**FR-AGENT-059** — When an authorised user verifies a remittance by matching it to attributed invoices and selecting **Verify Remittance**, the system shall compute the **Expected Remittance** as the sum of the attributed invoice amounts (net of any applicable credit notes) for the agent within the collection period and display the **Variance** as:

$$Variance_{Remittance} = AmountCollected - ExpectedRemittance$$

A variance outside the tenant-configured tolerance (default ±0%) shall prevent automatic verification and require a supervisor override with a mandatory justification note.

**Test oracle:** An agent with attributed invoices totalling UGX 500,000 who remits UGX 490,000 displays a variance of −UGX 10,000. With a 0% tolerance, automatic verification is blocked and a supervisor override is required.

---

**FR-AGENT-060** — When a remittance is verified (status transitions to `Verified`), the system shall post a receipt entry to the tenant's accounts receivable ledger and link the remittance record to the corresponding invoice records, reducing the outstanding balance on each linked invoice proportionally.

**Test oracle:** Verifying a remittance of UGX 300,000 against two invoices of UGX 200,000 and UGX 100,000 posts a receipt entry and reduces both invoice balances to zero.

---

**FR-AGENT-061** — When a remittance remains `Unverified` for more than the tenant-configured **Remittance Verification SLA** (default 3 business days), the system shall flag the record as `Overdue`, increment the agent's **Overdue Remittances Count**, and notify the tenant administrator and territory manager via in-app notification daily until the record is resolved.

**Test oracle:** A remittance recorded on a Monday with a 3-business-day SLA is flagged `Overdue` on Thursday morning (no later than 09:00 EAT) and generates a daily notification until verified or escalated.

## 7.4 Daily Activity Summaries

**FR-AGENT-062** — When the daily summary schedule triggers (configurable time, default 23:45 EAT), the system shall generate a **Daily Activity Summary** record for each active agent, capturing the following metrics for the current calendar day: **Invoices Attributed** (count and value), **Stock Issued** (quantity by product), **Stock Returned** (quantity by product), **Remittances Collected** (count and value), **Remittances Verified** (count and value), and **Target Achievement Percentage** as of end of day. The record shall be stored, made available in the administrative reporting dashboard, and accessible to the agent in the self-service portal under **My Activity**.

**Test oracle:** At 23:45 EAT, a summary record is created for every active agent. An agent with 3 attributed invoices, 1 stock issue of 20 units, and 1 remittance of UGX 150,000 shows all three events accurately in their summary.
