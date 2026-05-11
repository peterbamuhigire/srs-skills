# AI Agent Responsible-AI Addendum Template

## 1. Action Accountability per Feature

| Feature | Accountable role | Responsible party | Named approver | Audit path |
|---------|--------------------|--------------------|------------------|--------------|
| Inbox Triage | Workspace admin | <Company> AI Lead | Inbox owner (per-run plan approval) | `audit/inbox-triage/<tenant>/...` |
| Daily Reconciliation | Workspace admin | <Company> AI Lead | Finance admin (per-day digest review) | `audit/reconciliation/<tenant>/...` |
| Support Triage | Workspace admin | <Company> AI Lead | Support team lead (per-call) | `audit/support-triage/<tenant>/...` |

## 2. Audit-Log Retention by Event Class

| Event class | Hot | Cold | Regulatory justification |
|--------------|-----|------|----------------------------|
| Tool call — read | 90 d | 13 mo | operational |
| Tool call — write-internal | 13 mo | 3 yr | tenant audit, dispute |
| Tool call — write-external | 13 mo | 7 yr | regulatory, dispute |
| Tool call — billing | 13 mo | 7 yr | financial regulation |
| Tool call — irreversible | 13 mo | 7 yr | regulatory, contestability |
| Plan + approval events | 13 mo | 7 yr | Art. 14 evidence |
| Kill-switch events | 13 mo | 7 yr | safety audit |
| Human-approval events | 13 mo | 7 yr | Art. 14 evidence |

Retention thresholds meet the most stringent applicable regulation per region; documented per-tenant in the DPA.

## 3. Contestability Mechanism

| Step | Detail |
|------|--------|
| User path | `Report` button on any agent audit row; in-product flag + form. |
| Internal review SLA | 2 working days (1 working day Enterprise + irreversible side-effect). |
| Evidence assembly | full audit excerpt for the run; planner transcript; sanitised tool inputs and outputs. |
| Escalation | senior reviewer; legal review for regulated decisions; DPO if data-protection involved. |
| Postmortem trigger | every confirmed wrong action goes to the postmortem queue and produces a regression case in the agent eval rig. |

## 4. Human-Final-Decision Principle

| Tool class | Human role | Moment | Information shown | Bypass |
|-------------|-------------|--------|---------------------|--------|
| `email.send` | Inbox owner | per-call (before send) | recipient, subject, full body, justification | none; documented waiver with ADR only |
| `payments.charge.execute` | Finance admin | per-call (before charge) | amount, account, reason, agent rationale | none |
| `payments.refund.issue` above $200 | Finance admin | per-call | amount, account, reason, agent rationale | threshold lowered, never raised, without ADR |
| `file.delete-permanent` | Workspace admin | per-call | path, owner, agent rationale, restore window | none |

This is the operationalisation of EU AI Act Art. 14 for the product.

## 5. Bias and Harm Reviews

For features affecting protected-class outcomes (declared per-feature on first PRD pass):

| Feature | Cadence | Reviewers | Metrics tracked | Remediation path |
|---------|---------|-----------|-------------------|--------------------|
| Support Triage (if used for priority assignment) | quarterly | AI Lead + external auditor | priority assignment by demographic proxy if measurable | re-train / re-prompt + red-team |
| (None at present where applicable) | — | — | — | — |

If a feature is later applied to hiring, lending, housing, healthcare, or education, this table is updated **before** the feature ships in the new context, not after.

## 6. Public-Declaration Cross-link Table

| Public paragraph | Internal evidence row | Refresh trigger |
|--------------------|------------------------|-------------------|
| "Our agents act under your workspace's authority and within the limits we publish." | Sections 1, 4 above | quarterly |
| "We retain a full audit of every agent action for at least 13 months." | Section 2 | quarterly |
| "You can flag any agent action and a human will respond within 2 working days." | Section 3 | quarterly |
| "Irreversible actions always require a human decision." | Section 4 | quarterly |
| "We review agents that affect protected-class outcomes on a documented cadence." | Section 5 | quarterly |

## 7. Review Cadence

- Quarterly: full addendum review by AI Lead + DPO + Security + Legal.
- After any SEV1 or SEV2: re-review of the affected feature's row.
- After any change to the action catalogue: re-review the affected human-final-decision rows.
