# Persona 9: The Director

**Profile:** Age 52, PhD, basic smartphone user. Reviews management reports, approves strategic decisions, presents to Parliament. Needs a 5-minute daily brief on revenue, cash, agent performance, and production status. Pain point: Finance Director currently takes 2 days to prepare a management report.

**Critical requirement:** Executive Dashboard App — real-time KPIs on phone, push alerts for budget over-runs and critical events.

---

## US-078: View Real-Time KPIs on the Executive Dashboard App

**US-078:** As the Director, I want to open the Executive Dashboard App and see BIRDC's critical KPIs within 10 seconds, so that I have a complete operational picture before any morning meeting without calling the Finance Director.

**Acceptance criteria:**

- The Executive Dashboard App home screen displays, in a single scrollable view: today's revenue (UGX), month-to-date revenue vs. budget (bar chart), current cash and bank balances (UGX), total agent outstanding balance (UGX), and today's production output (kg).
- All figures are live, refreshed every 5 minutes when the app has internet connectivity; the last-refresh timestamp is visible on screen.
- The Director can tap any KPI tile to see the underlying breakdown (e.g., tapping "Revenue" shows a split by product category; tapping "Cash" shows individual bank account balances).
- The dashboard loads within 10 seconds on a standard 4G connection.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-006-004

---

## US-079: Receive a Push Alert When a Budget Vote Approaches Its Limit

**US-079:** As the Director, I want to receive a push notification on my phone when any parliamentary budget vote reaches 80% or 95% utilisation, so that I am aware of budget pressures before they become overruns.

**Acceptance criteria:**

- When any budget vote reaches 80% of its approved amount, the system sends a push notification to the Executive Dashboard App on the Director's device within 5 minutes of the triggering transaction (per BR-014).
- The notification message reads: "Budget Alert: [Vote Name] has reached [X]% of its approved allocation. Remaining balance: UGX [amount]."
- When the vote reaches 95%, a second push notification is sent with a "Critical" priority flag, causing the notification to appear even if the Director's phone is on silent.
- The Director can tap the notification to open the Executive Dashboard App and view the full budget breakdown for the affected vote.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-008-002

---

## US-080: Approve a Budget Over-Run with a Logged Justification

**US-080:** As the Director, I want to be the only person who can authorise expenditure that exceeds a parliamentary budget vote's approved limit, so that over-runs require explicit accountability.

**Acceptance criteria:**

- Any transaction that would cause a vote balance to exceed 100% is blocked by the system until the Director approves it (per BR-014).
- The Director's approval interface (accessible from the Executive Dashboard App and web ERP) displays: vote name, approved budget, current expenditure, the transaction requesting approval, and the amount by which the vote would be exceeded.
- The Director must enter a written justification (minimum 20 characters) before the approval is accepted; the justification, Director's user ID, and timestamp are logged permanently in the audit trail.
- After Director approval, the transaction proceeds and the vote utilisation exceeds 100%; the Finance Director is notified of the authorised over-run.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-008-003

---

## US-081: View Agent Network Performance Summary

**US-081:** As the Director, I want to see the top-performing and underperforming agents and their aggregate outstanding cash balances, so that I can hold the Sales Manager accountable for the agent network.

**Acceptance criteria:**

- The Agent Performance section of the Executive Dashboard App displays: total active agents (count), total agent outstanding balance (UGX), top 5 agents by month-to-date sales, and bottom 5 agents by month-to-date sales.
- A "Cash at Risk" figure is displayed: the total outstanding balance of agents who have not remitted in the last 7 days.
- The Director can drill down to a territory-level view showing revenue and outstanding balance by territory.
- The data shown matches the agent performance report in the web ERP for the same period and filters.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 1

**FR Reference:** FR-004-009

---

## US-082: Receive a Daily Summary Push Notification

**US-082:** As the Director, I want to receive an automated daily summary notification at 07:00 every morning, so that I start each day informed without having to open the app.

**Acceptance criteria:**

- The system generates and sends a push notification to the Director's device at 07:00 each morning (configurable time) containing: yesterday's total revenue, yesterday's total production (kg), total agent network outstanding balance, and any critical alerts (budget votes at ≥ 95%, overdue remittances > UGX 10M).
- The notification is delivered even if the Executive Dashboard App is not open.
- If the Director's device is offline, the notification is delivered the next time the device connects.
- The Director can adjust the notification time and content preferences from the app settings.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-001-002

---

## US-083: View the P&L Summary Without Waiting for Month-End Closing

**US-083:** As the Director, I want to view the BIRDC Profit and Loss summary for the current period at any time without waiting for month-end closing, so that I can present current financial performance at Board meetings.

**Acceptance criteria:**

- The Executive Dashboard App provides a "P&L Summary" view showing: month-to-date revenue, month-to-date cost of goods sold, gross profit, and top-3 expense categories — for BIRDC commercial mode.
- The P&L summary reflects all posted transactions up to the current day; no period-closing procedure is required to generate a current-period view.
- The Director can toggle between the current month and the previous month for comparison.
- The P&L summary figures match the full P&L report generated in the web ERP for the same period and mode to within UGX 0.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 2

**FR Reference:** FR-005-008

---

## US-084: Authorise Large Procurement above PPDA Threshold

**US-084:** As the Director, I want to review and approve Large and Restricted category procurement requests, so that BIRDC's high-value expenditures are subject to Director-level oversight as required by the PPDA Act.

**Acceptance criteria:**

- Large and Restricted procurement approvals are routed to the Director's approval queue in the web ERP and are displayed as a push notification on the Executive Dashboard App.
- The approval screen shows: procurement description, vendor(s), total value, PPDA category, all required documents uploaded (checklist), Finance Manager's recommendation, and the LPO draft.
- The Director can approve, reject, or send back for revision; all actions are logged with the Director's user ID and timestamp.
- No LPO is generated and no payment is initiated for Large or Restricted procurement without the Director's approval record in the system (per BR-005).

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-011
