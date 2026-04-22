# Period-Close Processing Requirements

## 8.1 Overview

Period-close processing controls which accounting periods are open for transaction posting. The module provides soft-close and hard-close states, year-end retained earnings automation, and a Super Admin override to re-open closed periods with full audit trail coverage.

<!-- [CONTEXT-GAP: GAP-008 — accounting period close rules (soft vs. hard) not fully defined] -->

The requirements below represent the most common industry pattern for period-close behaviour. The consultant must review and confirm or amend the soft-close and hard-close thresholds (e.g., number of days after period end that soft-close activates, override permission name) before this section is considered finalised.

## 8.2 Accounting Period Management

**FR-ACCT-108:** The system shall automatically create 12 accounting periods per financial year for each tenant at tenant onboarding, aligning period start and end dates to the tenant's configured financial year start month; each period shall be initialised with status *Open*.

**FR-ACCT-109:** The system shall allow an authorised user with the Finance Manager role to manually set any *Open* period to *Soft Closed* status.

**FR-ACCT-110:** The system shall allow an authorised user with the Finance Manager role to manually set any *Soft Closed* period to *Hard Closed* status.

**FR-ACCT-111:** The system shall display the status of each accounting period (Open, Soft Closed, Hard Closed) on the Period Management screen, with the current period highlighted.

## 8.3 Soft-Close Behaviour

**FR-ACCT-112:** The system shall display a modal warning message "Period [{period name}] is soft-closed. Do you want to proceed with this posting? This action will be logged." when a user attempts to post a transaction with a date in a *Soft Closed* period; the user shall be able to confirm or cancel.

**FR-ACCT-113:** The system shall allow the posting to proceed after the user confirms the soft-close override (FR-ACCT-112), provided the user's role includes the `accounting.override_soft_close` permission.

**FR-ACCT-114:** The system shall reject the posting and return an error "Insufficient permissions to post to a soft-closed period." when the user confirms the soft-close override but their role does not include the `accounting.override_soft_close` permission.

**FR-ACCT-115:** The system shall record a soft-close override audit event capturing `user_id`, `period_id`, `document_type`, `document_id`, and `timestamp` for every posting that proceeds under a soft-close override.

## 8.4 Hard-Close Behaviour

**FR-ACCT-116:** The system shall reject any transaction posting — from any module, by any user role, including Super Admin — when the transaction date falls within a *Hard Closed* period, and shall return HTTP 422 with the error message "Period [{period name}] is hard-closed. No postings are permitted."

**FR-ACCT-117:** The system shall reject bank reconciliation imports and matching operations that reference a *Hard Closed* period and shall return the same error as FR-ACCT-116.

## 8.5 Year-End Close

**FR-ACCT-118:** The system shall auto-post a year-end retained earnings journal when an authorised user with the Finance Manager role initiates the *Year-End Close* action for a financial year in which all 12 periods are *Hard Closed*; the journal shall debit all Revenue accounts and credit all Expense accounts with their year-end balances, and post the net profit (or net loss) to the Retained Earnings system account.

**FR-ACCT-119:** The system shall set all Revenue and Expense GL account balances to zero after the year-end close journal is posted, carrying only Balance Sheet account balances forward as opening balances for the new financial year.

**FR-ACCT-120:** The system shall prevent the year-end close action from executing when any of the 12 periods in the financial year has a status other than *Hard Closed*, and shall display a list of non-closed periods to the user.

## 8.6 Re-opening a Closed Period

**FR-ACCT-121:** The system shall allow a user with Super Admin role to re-open a *Hard Closed* or *Soft Closed* period by selecting the *Re-open Period* action and providing a mandatory re-open reason (free text, max 500 characters).

**FR-ACCT-122:** The system shall record a re-open audit event capturing `super_admin_user_id`, `period_id`, `re_open_reason`, and `timestamp` for every period re-open action; this event shall be visible in the global Audit Log and shall trigger an in-app notification to all Finance Manager role users within the tenant.

## 8.7 Close Orchestration and Task Management

**FR-ACCT-123:** The system shall allow an authorised user with the Finance Manager role to define period-close templates per entity and close type (`month_end`, `quarter_end`, `year_end`) with task name, sequence, due-date offset, dependency, required evidence flag, approval-required flag, and default owner role.

**FR-ACCT-124:** The system shall instantiate a close run from a selected close template for a target entity and accounting period, creating task instances with inherited metadata and initial status *Not Started*.

**FR-ACCT-125:** The system shall support the close task statuses *Not Started*, *In Progress*, *Blocked*, *Completed*, *Approved*, and *Waived*; any transition to *Blocked* or *Waived* shall require a mandatory explanatory comment.

**FR-ACCT-126:** The system shall allow an authorised Finance Manager to assign or reassign each close task to a named user or role-qualified queue while preserving the original template owner in the audit history.

**FR-ACCT-127:** The system shall require upload or linkage of supporting evidence (`attachment`, `URL`, or `commentary`) before a task marked `evidence_required = true` can be moved to *Completed*.

**FR-ACCT-128:** The system shall prevent a period from being moved to *Hard Closed* while any mandatory close task for that entity and period remains in a status other than *Completed*, *Approved*, or *Waived by authorised approver*.

**FR-ACCT-129:** The system shall provide a Close Cockpit dashboard showing close completion percentage, overdue task count, blocked task count, and task status by entity, period, and owner.

**FR-ACCT-130:** The system shall send in-app notifications to task owners and Finance Managers when a close task is assigned, becomes overdue, is marked *Blocked*, or is rejected during approval.

## 8.8 Close Journals, Recurring Entries, and Control Approvals

**FR-ACCT-131:** The system shall allow an authorised user to create recurring journal templates with frequency (`monthly`, `quarterly`, `annual`), effective start date, optional end date, journal line definitions, narration pattern, and approval route.

**FR-ACCT-132:** The system shall automatically generate draft journals from active recurring journal templates for each eligible open period, preserving a reference to the originating template and target period.

**FR-ACCT-133:** The system shall allow a recurring or manual close journal to be flagged `auto_reverse_next_period = true`, in which case the system shall generate a reversal journal dated the first day of the next open period after the original journal is posted.

**FR-ACCT-134:** The system shall enforce preparer-versus-approver segregation on close journals and recurring journal templates; a user who creates or submits the item shall not be permitted to approve the same item.

**FR-ACCT-135:** The system shall require approval before posting any journal whose source classification is `Recurring`, `LocalAdjustment`, `TopsideAdjustment`, `Intercompany`, or `Elimination` and whose absolute amount exceeds the tenant's configured finance approval threshold.

**FR-ACCT-136:** The system shall maintain a mandatory source classification on every close journal using one of the values `Recurring`, `Reversal`, `LocalAdjustment`, `TopsideAdjustment`, `Intercompany`, or `Elimination`.

**FR-ACCT-137:** The system shall provide a Close Journal Register report filterable by entity, period, source classification, status, preparer, approver, and reversal flag.

## 8.9 Multi-Entity Close and Consolidation Foundations

**FR-ACCT-138:** The system shall track close readiness independently for each legal entity and reporting basis, so that 1 entity can be *Hard Closed* while another remains *Open* for the same nominal calendar period.

**FR-ACCT-139:** The system shall require every intercompany close journal to capture a mandatory counterparty entity and shall validate that debit and credit effects are attributable to both the originating entity and the counterparty entity.

**FR-ACCT-140:** The system shall provide an Intercompany Mismatch report showing unmatched or unbalanced intercompany positions by entity, counterparty entity, account, currency, and period.

**FR-ACCT-141:** The system shall preserve separate journal layers for `LocalStatutory`, `GroupAdjustment`, `TopsideAdjustment`, and `Elimination`, and group-reporting outputs shall be filterable by those layers without altering the underlying local statutory journals.

**FR-ACCT-142:** The system shall allow only users with a dedicated group-finance permission to create or approve journals in the `Elimination` layer.

**FR-ACCT-143:** The system shall generate a Consolidation Input Trial Balance by entity, currency, account, and journal layer for a selected period as a standard output to downstream group-reporting processes.

**FR-ACCT-144:** The system shall preserve traceable source references from `TopsideAdjustment` and `Elimination` journals back to the contributing balances, intercompany pair, or close issue record from which the journal originated.

## 8.10 Finance Reporting Discipline

**FR-ACCT-145:** The system shall maintain a Close Pack register for each entity and period listing the required finance outputs, including Trial Balance, Income Statement, Balance Sheet, Cash Flow Statement, tax reports, and any tenant-configured management reports.

**FR-ACCT-146:** The system shall stamp every generated finance report with `entity`, `period`, `report_basis`, `generated_by_user_id`, `generated_at`, and the applied parameter set.

**FR-ACCT-147:** The system shall freeze a reproducible snapshot of any report marked *Final* or generated after the period reaches *Hard Closed*; regenerating the same report with the same parameters shall produce identical values unless the period is formally re-opened.

**FR-ACCT-148:** The system shall require Finance Manager sign-off before a Close Pack can be marked *Final*, capturing `approver_user_id`, `approved_at`, and an optional close commentary note.

