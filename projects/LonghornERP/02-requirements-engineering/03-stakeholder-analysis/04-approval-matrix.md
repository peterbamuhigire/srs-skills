## Approval Matrix for Longhorn ERP

This matrix defines the approval authority chain for each transaction type. All thresholds marked as *configurable system parameter* will be settable by the Tenant System Administrator without code changes. Thresholds marked `[CONTEXT-GAP: GAP-006]` require confirmation of current Public Procurement and Disposal of Public Assets Authority (PPDA) limits from the product owner before Phase 1 sign-off.

*The product owner (Peter Bamuhigire) must confirm all configurable default values before they are committed to the platform seed data.*

---

### Purchase Order Approval by Value Threshold

The platform will enforce 3 approval tiers for Local Purchase Orders (LPOs). Tier boundaries are configurable system parameters; the defaults below are indicative pending PPDA threshold confirmation.

| Tier | Label | Default Value Range | Approver Level | Notes |
|---|---|---|---|---|
| Tier 1 | Micro | UGX 0 – 500,000 | Procurement Officer | Self-approved; no additional sign-off required |
| Tier 2 | Small | UGX 500,001 – 5,000,000 | Operations / Procurement Manager | Single approver required |
| Tier 3 | Large | UGX 5,000,001 and above | Operations / Procurement Manager → CEO / MD | Sequential dual approval required |

`[CONTEXT-GAP: GAP-006]` — PPDA mandates specific open-tendering and restricted-bidding thresholds for public entities. The default tier boundaries above are provisional. The product owner will confirm compliant defaults before Phase 1 go-live.

*All tier boundary values are configurable system parameters. Tenant System Administrators may adjust thresholds to match their internal financial policy without requiring a platform upgrade.*

---

### Leave Request Approval Chain

| Step | Actor | Action | Trigger |
|---|---|---|---|
| 1 | Employee | Submits leave request via HR module | Employee initiates |
| 2 | Direct Supervisor | Reviews and approves or rejects | System notifies supervisor on submission |
| 3 | HR Officer | Records approved leave; updates leave balance | System notifies HR Officer on supervisor approval |

- If the Direct Supervisor does not act within a configurable escalation period (default: 48 hours), the system will escalate to the HR Officer automatically.
- Rejection at Step 2 terminates the chain; the employee receives an in-app and email notification with the reason.

---

### Payroll Approval Chain

| Step | Actor | Action | Trigger |
|---|---|---|---|
| 1 | HR Officer | Prepares and submits payroll run for review | HR Officer initiates at month-end |
| 2 | Finance Manager | Reviews payroll totals, statutory deductions, and variance report; approves or returns with comments | System notifies Finance Manager on submission |
| 3 | CEO / MD | Final approval before disbursement | System notifies CEO / MD on Finance Manager approval |
| 4 | System | Generates payslips and initiates mobile money / bank disbursement | Triggered on CEO / MD approval |

- No disbursement will occur until all 3 approval steps are complete.
- A payroll run returned at Step 2 or Step 3 reverts to Step 1 with comments attached.

---

### Journal Entry Approval

| Entry Value | Approver | Notes |
|---|---|---|
| At or below configurable threshold | Accountant (self-approved) | Entry posts immediately upon save |
| Above configurable threshold | Accountant submits → Finance Manager approves | Entry remains in *Pending* status until Finance Manager approval |

- The journal entry approval threshold is a configurable system parameter (default value: UGX 1,000,000).
- *The product owner must confirm the default threshold before it is seeded into the platform.*
- Reversal entries above the threshold follow the same approval chain as original entries.
- All journal entries, regardless of value, are written to the immutable audit log with creator identity, timestamp, and IP address.

---

### Sales Quotation Approval

| Condition | Approver | Notes |
|---|---|---|
| Discount ≤ 10% of list price | Sales Representative (self-approved) | Quotation may be sent to customer without additional sign-off |
| Discount > 10% of list price | Sales Representative submits → Sales Manager approves | Quotation is locked in *Pending Approval* status until Sales Manager acts |

- The discount threshold (10%) is a configurable system parameter.
- If the Sales Manager does not act within a configurable period (default: 24 hours), the system will escalate to the Operations / Procurement Manager.
- Approved quotations are converted to sales orders by the Sales Representative without further approval.

---

### Production Order Approval

| Step | Actor | Action | Trigger |
|---|---|---|---|
| 1 | Production Supervisor / Planner | Creates and submits production order | Planner initiates on receiving sales order or production schedule |
| 2 | Production Manager | Reviews resource availability and Bill of Materials (BOM); approves or revises | System notifies Production Manager on submission |
| 3 | Operations Manager | Final approval for orders above a configurable value or quantity threshold | System notifies Operations Manager when Production Manager approves a large order |

- Production orders below the quantity or value threshold (configurable system parameter) are approved at Step 2 only.
- *The product owner must confirm default quantity and value thresholds for Step 3 escalation before Phase 1 sign-off.*
- An approved production order triggers automatic raw material reservation in the Inventory module.
