# Agent Self-Service Portal

## 6.1 Overview

The Agent Self-Service Portal provides each agent with a secure, read-only view of their own sales performance, commission earnings, targets, and payment statements. It is accessible via any modern web browser with a mobile-responsive layout. Agents do not have access to other agents' data or to the administrative back-end.

## 6.2 Portal Authentication and Access

**FR-AGENT-043** — When an agent navigates to the portal URL and submits their credentials (**Phone Number** or **Email Address** and **Password**), the system shall authenticate the agent using the tenant's Identity Provider integration and, on success, display the agent's personalised dashboard within 3 seconds. Failed authentication attempts shall increment a counter; after 5 consecutive failed attempts within 10 minutes, the system shall lock the account for 15 minutes and notify the tenant administrator via in-app notification.

**Test oracle:** After 5 consecutive failed logins within 10 minutes, the sixth attempt returns error `ACCOUNT_TEMPORARILY_LOCKED` and an in-app notification is sent to the administrator.

---

**FR-AGENT-044** — When an agent is authenticated, the system shall enforce data isolation: all queries on the portal shall be scoped to the authenticated agent's **Agent ID** and the tenant's **Tenant ID**. No cross-agent or cross-tenant data shall be accessible via any portal endpoint.

**Test oracle:** Manually crafting a request with a different `agentId` parameter while authenticated returns a 403 Forbidden response and logs an access violation audit entry.

## 6.3 Sales View

**FR-AGENT-045** — When an authenticated agent selects the **My Sales** section, the system shall display a paginated list of all invoices attributed to that agent, sorted by **Invoice Date** descending, with columns for **Invoice ID**, **Customer Name**, **Invoice Date**, **Invoice Amount**, **Attributed Amount**, and **Attribution Source**. The list shall load within 2 seconds for agents with up to 1,000 attributed invoices.

**Test oracle:** An agent with 1,000 attributed invoices sees the first page of results within 2 seconds of navigating to **My Sales**.

---

**FR-AGENT-046** — When an authenticated agent applies a date range filter on the **My Sales** view, the system shall return matching results within 2 seconds and display the filtered total attributed amount at the top of the results panel.

**Test oracle:** Filtering by a 30-day range returns the correct invoices and the correct sum of attributed amounts within 2 seconds.

## 6.4 Commission Statements

**FR-AGENT-047** — When an authenticated agent navigates to the **My Commissions** section, the system shall display a list of all commission run ledger rows for that agent, showing **Run Name**, **Period**, **Attributed Sales**, **Computed Commission**, **Status** (`Pending`, `Approved`, `Paid`, `Failed`), and **Payment Date** (if paid). The list shall cover all runs from the agent's join date to the current date.

**Test oracle:** An agent whose first commission run was in January 2026 sees all subsequent runs listed with correct statuses when accessing **My Commissions** in April 2026.

---

**FR-AGENT-048** — When an authenticated agent selects a specific commission run row, the system shall display a detailed statement showing the commission calculation breakdown: rule type applied, rate(s), attributed sales by product (if `ProductSpecific` rule), total computed commission, any adjustments, and the net commission paid.

**Test oracle:** Selecting a run with a tiered rule displays each tier threshold, the applicable rate, and the computed amount for that tier, summing to the correct total.

---

**FR-AGENT-049** — When an authenticated agent requests a PDF statement for a specific commission run by selecting **Download Statement**, the system shall generate and serve a PDF within 10 seconds containing the agent's name, **Agent ID**, run period, commission breakdown table, and payment confirmation (if paid), formatted using the Longhorn ERP document template.

**Test oracle:** The generated PDF contains all required fields and is served within 10 seconds.

## 6.5 Target Progress

**FR-AGENT-050** — When an authenticated agent views the **My Targets** section, the system shall display each active target with a visual progress indicator showing the **Target Amount**, **Current Attributed Sales**, and **Target Achievement Percentage** computed as:

$$TargetAchievement = \frac{AttributedSales}{TargetAmount} \times 100$$

The progress value shall reflect sales attributed as of no later than 5 minutes before the page load.

**Test oracle:** An agent with UGX 1,500,000 attributed against a UGX 2,000,000 monthly target sees 75% displayed. After a new UGX 200,000 invoice is attributed, the value updates to 85% within 5 minutes.

---

**FR-AGENT-051** — When an agent's **Target Achievement Percentage** reaches 80%, 100%, and 120% of the target, the system shall send a congratulatory in-app notification to the agent within 5 minutes of the threshold being crossed.

**Test oracle:** Attributing an invoice that pushes an agent's achievement from 79% to 82% triggers a notification to the agent within 5 minutes.

## 6.6 Notifications and Alerts

**FR-AGENT-052** — When a commission run that includes the authenticated agent transitions to `Approved` or `Paid`, the system shall send the agent an in-app notification and, if an email address is on record, an email notification containing the **Run Period**, **Commission Amount**, and (for `Paid` status) the **Payment Reference Number** from the mobile money gateway. Both notifications shall be delivered within 5 minutes of the status transition.

**Test oracle:** Within 5 minutes of a run transitioning to `Paid`, the agent has an in-app notification and an email with a non-null payment reference number.
