# The Golden Rule — Zero Mandatory Training

## Statement of the Rule

> *If a user would need a manual or a consultant to complete a task, the interface is redesigned until they do not.*

This is not a usability aspiration. It is a non-negotiable product constraint that applies to every screen, every workflow, and every release of Longhorn ERP from Version 1.0 forward. No feature ships if completing it requires the user to consult documentation, contact support, or call a trainer.

## What This Rule Demands of Product Design

The Golden Rule carries four concrete design obligations:

1. **Terminology must match the user's domain, not the engineer's.** Every field label, button caption, and status message shall use the language that an accountant, warehouse clerk, or HR officer already uses in their daily work. No technical identifiers, no system jargon, no database-derived naming.
2. **Workflows must follow the user's mental model, not the data model.** A user creating an invoice shall follow the sequence: customer → items → amounts → save — not navigate a multi-tab form built around the underlying relational schema.
3. **Errors must prescribe the fix, not describe the fault.** Error messages shall tell the user exactly what to do next. "Amount cannot be negative" is insufficient. "Enter a positive amount in the **Amount** field — payments use the **Record Payment** button instead" is compliant.
4. **Progressive disclosure shall protect novice users.** Advanced configuration options shall be accessible but not surfaced in primary task flows. A first-time user creating a stock item shall not encounter depreciation settings, advanced costing methods, or inter-branch routing unless they navigate to those settings deliberately.

## Measurable Compliance Criterion

The Golden Rule is verified by a formal unassisted task success test conducted before each major release. The compliance threshold is:

**≥ 85% unassisted task success rate across 5 benchmark tasks, tested with representative users who have received zero product training.**

The 5 benchmark tasks are:

| # | Task | Module |
|---|---|---|
| 1 | Create a tax invoice for a customer | Sales |
| 2 | Record a payment received against an outstanding invoice | Accounting |
| 3 | Check the current stock quantity of a specific item | Inventory |
| 4 | Submit a leave request for annual leave | HR & Payroll |
| 5 | Run payroll for the current month | HR & Payroll |

A task is scored as a *success* only if the user completes it without: opening any help documentation, asking a question of the test facilitator, or taking more than 3 incorrect navigational steps. A task is scored as a *failure* if any of those conditions occur. The overall rate is calculated as: $\text{Success Rate} = \frac{\text{Tasks Completed Without Assistance}}{\text{Total Tasks Attempted}} \times 100$.

If the success rate falls below 85% for any benchmark task, the responsible interface is returned to design before the release proceeds. No release exception is permitted for a Golden Rule failure.

## Strategic Differentiation: Longhorn ERP versus Odoo and SAP

This rule directly addresses the primary adoption barrier that mid-sized African businesses face with incumbent ERP platforms.

**SAP Business One** requires a certified implementation partner for initial deployment, a formal training programme for end users, and ongoing administrator involvement for routine configuration changes. The minimum viable implementation engagement for a 30-user organisation in Uganda is estimated at UGX 110,000,000 to UGX 375,000,000 before a single transaction is recorded. The training obligation is structural — SAP's interface is built for trained ERP specialists, not first-time business software users.

**Odoo Enterprise** is modular and configurable but exposes a level of technical complexity — module installation, configuration menus, developer mode, and database-level settings — that creates a steep learning curve for non-technical users. A typical Odoo implementation for a 30-user organisation requires a consulting engagement estimated at UGX 75,000,000 to UGX 300,000,000. The usability burden does not disappear after implementation; it recurs every time a new employee joins or a new workflow is needed.

**Longhorn ERP** shall be designed so that a new employee can be given a login and complete their first productive task — creating an invoice, receiving a delivery, recording a payment — within 30 minutes of first access, with no training session and no consultant present. This is not a marketing claim; it is a contractual product design obligation enforced by the Golden Rule compliance test before every release.
