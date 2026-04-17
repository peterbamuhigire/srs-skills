# Commission Run, Approval Workflow, and Mobile Money Payout

## 5.1 Overview

The monthly commission run is a batch process that calculates commission amounts for all eligible agents for a specified period, routes the results through a configurable approval workflow, and initiates bulk disbursement via MTN Mobile Money or Airtel Money. This section covers requirements from run initiation through payment confirmation.

## 5.2 Commission Run Initiation

**FR-AGENT-031** — When an authorised user initiates a commission run via the **New Commission Run** action, the system shall require the following inputs: **Run Name**, **Period Start Date**, **Period End Date**, **Commission Rule ID** (or "Use Agent Overrides"), and **Currency**. The system shall reject the run if an active or pending run already exists for an overlapping period, returning error `DUPLICATE_RUN_PERIOD`.

**Test oracle:** Initiating a second April 2026 run when one is in `Pending Approval` status returns `DUPLICATE_RUN_PERIOD`.

---

**FR-AGENT-032** — When a commission run is initiated, the system shall execute the batch calculation asynchronously, processing all active agents with at least one attribution record in the period. The system shall complete the calculation for up to 500 agents within 120 seconds and update the run status from `Calculating` to `Pending Approval` upon completion.

**Test oracle:** A run initiated for 500 agents transitions from `Calculating` to `Pending Approval` within 120 seconds.

---

**FR-AGENT-033** — When the commission run calculation completes, the system shall generate a run summary record containing: **Run ID**, **Period**, **Total Agents Processed**, **Total Agents With Zero Commission**, **Total Commission Amount**, **Total Exceptions Count**, and a line-by-line agent commission ledger with columns for **Agent ID**, **Agent Name**, **Attributed Sales**, **Rule Applied**, **Computed Commission**, **Override Applied** flag, and **Exception Flags**.

**Test oracle:** The run summary is accessible within 5 seconds of the run transitioning to `Pending Approval` and contains one ledger row per processed agent.

---

**FR-AGENT-034** — When an authorised user downloads the commission run exception report, the system shall produce a CSV file listing all exception-flagged ledger rows with their **Agent ID**, **Agent Name**, **Exception Code**, and **Exception Detail**. The file shall be available for download within 10 seconds of the request.

**Test oracle:** A run with 15 exception rows produces a CSV with 15 data rows (plus header) within 10 seconds.

## 5.3 Approval Workflow

**FR-AGENT-035** — When a commission run transitions to `Pending Approval`, the system shall send an in-app notification and an email notification to all users assigned the `CommissionApprover` role within the tenant, containing the **Run ID**, **Period**, **Total Commission Amount**, and a direct link to the approval screen. The notification shall be delivered within 5 minutes of the status transition.

**Test oracle:** Within 5 minutes of a run entering `Pending Approval`, every `CommissionApprover` user has an in-app notification and an email with the correct run details.

---

**FR-AGENT-036** — When an authorised approver reviews the commission run and selects **Approve**, the system shall record the approver's user ID, timestamp, and optional approval comment, transition the run status to `Approved`, and unlock the **Initiate Payment** action. The approval action shall be irreversible.

**Test oracle:** After approval, the run status is `Approved`, the approver's name and timestamp are displayed on the run detail page, and the run cannot be returned to `Pending Approval`.

---

**FR-AGENT-037** — When an authorised approver selects **Reject**, the system shall require a rejection reason (minimum 10 characters), record the rejector's user ID and timestamp, transition the run status to `Rejected`, and send notifications to the run initiator and all `CommissionApprover` users. A rejected run shall not be restartable; a new run must be initiated.

**Test oracle:** Entering a rejection reason of fewer than 10 characters is blocked by client-side and server-side validation. A valid rejection transitions the run to `Rejected` and notifies the initiator within 5 minutes.

## 5.4 Mobile Money Bulk Payment

**FR-AGENT-038** — When an authorised user initiates payment on an `Approved` commission run by selecting **Initiate Payment**, the system shall validate that every agent in the run has a verified **Mobile Money Number** (**MTN** or **Airtel**, formatted as a valid 10-digit Uganda mobile number) before submitting the bulk payment request. Agents with missing or unverified mobile numbers shall be excluded from the batch and listed in a pre-payment exception report.

**Test oracle:** A run with 3 agents lacking verified mobile numbers produces a pre-payment exception report listing those 3 agents; the payment batch contains the remaining agents only.

---

**FR-AGENT-039** — When the pre-payment validation passes (or is acknowledged by the user), the system shall submit a bulk payment request to the configured Mobile Money gateway (MTN Mobile Money API or Airtel Money API) containing for each agent: **Phone Number**, **Amount**, **Currency** (`UGX`), **Narrative** (format: `Commission - {Run Name} - {Agent ID}`), and **External Reference** (the **Agent Commission Ledger Row ID**). The system shall store the gateway batch reference number and transition the run status to `Payment Initiated`.

**Test oracle:** After submission, the run record stores a non-null gateway batch reference number and displays status `Payment Initiated`.

---

**FR-AGENT-040** — When the Mobile Money gateway sends payment callback notifications (success or failure per agent), the system shall update each agent's payment status in the commission run ledger to `Paid`, `Failed`, or `Reversed` within 60 seconds of receiving the callback. The system shall send in-app notifications to the run initiator for each agent payment event.

**Test oracle:** A simulated gateway callback for 10 agents is processed within 60 seconds, and each of the 10 ledger rows reflects the correct status.

---

**FR-AGENT-041** — When an agent payment status is `Failed`, the system shall expose a **Retry Payment** action for that individual agent that re-submits the payment to the gateway with a new external reference suffixed `-R{N}` where `N` is the retry count. The system shall allow a maximum of 3 retries per agent per run.

**Test oracle:** After 3 failed retries for a single agent, the **Retry Payment** action is disabled and the agent's status is `Payment Failed — Max Retries Reached`.

---

**FR-AGENT-042** — When a commission run reaches a terminal state (`All Paid`, `Partially Paid`, or `Payment Failed`), the system shall generate a run closure report containing: **Run ID**, **Approved Amount**, **Total Paid**, **Total Failed**, **Total Excluded (No MoMo Number)**, and a per-agent payment status table. The report shall be available for PDF download within 10 seconds of the terminal state being reached.

**Test oracle:** A completed run generates a downloadable PDF closure report within 10 seconds of all agent statuses being resolved.
