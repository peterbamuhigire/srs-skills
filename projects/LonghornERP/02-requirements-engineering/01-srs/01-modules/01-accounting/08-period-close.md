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
