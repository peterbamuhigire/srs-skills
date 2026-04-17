# Chart of Accounts Requirements

## 2.1 Overview

The Chart of Accounts (CoA) is the tenant-owned, hierarchical structure of General Ledger (GL) accounts used to classify every financial transaction. Each tenant maintains an independent CoA scoped to their organisation. The hierarchy consists of three levels: Groups, Sub-groups, and Accounts.

## 2.2 Account Structure Requirements

**FR-ACCT-001:** The system shall create a GL account when an authorised user submits a form containing the following mandatory fields: account code (alphanumeric, tenant-unique), account name (free text, max 120 characters), account type (one of: Asset, Liability, Equity, Revenue, Expense), sub-type (tenant-defined), and functional currency.

**FR-ACCT-002:** The system shall reject account creation and return a validation error when the submitted account code already exists within the same tenant's CoA.

**FR-ACCT-003:** The system shall allow an authorised user to edit the account name, sub-type, and currency fields of an existing GL account when the account has no posted transactions in the current open period.

**FR-ACCT-004:** The system shall prevent modification of the account code and account type fields on any GL account that has at least 1 posted journal line linked to it, and shall return a validation error message stating the reason.

**FR-ACCT-005:** The system shall deactivate a GL account when an authorised user submits a deactivation request, provided the account carries a zero balance and has no open transactions in any open period; the account shall be excluded from all transaction entry drop-downs upon deactivation.

**FR-ACCT-006:** The system shall prevent deactivation of a GL account when the account carries a non-zero balance or has unposted journal lines referencing it, and shall return a validation error listing the blocking condition.

## 2.3 Account Hierarchy Requirements

**FR-ACCT-007:** The system shall maintain a 3-level account hierarchy — Groups, Sub-groups, and Accounts — and shall enforce that every Account belongs to exactly 1 Sub-group, and every Sub-group belongs to exactly 1 Group.

**FR-ACCT-008:** The system shall display the CoA in hierarchical tree format, indented by level, when an authorised user navigates to the Chart of Accounts screen.

**FR-ACCT-009:** The system shall allow an authorised user to create, rename, and delete Groups and Sub-groups, provided that deletion is blocked when the Group or Sub-group contains at least 1 active Account.

## 2.4 Localisation Templates

**FR-ACCT-010:** The system shall present a CoA template selection prompt during tenant onboarding, offering at minimum the following localisation profiles: Uganda, Kenya, and Tanzania; the selected template shall pre-populate the tenant's CoA with standard account codes, names, types, and hierarchy appropriate to the selected jurisdiction.

**FR-ACCT-011:** The system shall allow an authorised user to modify, extend, or delete any account imported from a localisation template, subject to the constraints in FR-ACCT-003 through FR-ACCT-006.

## 2.5 System Account Auto-Creation

**FR-ACCT-012:** The system shall automatically create the following system accounts for every new tenant during onboarding, using the codes defined in the selected localisation template: Retained Earnings, VAT Control (Input), VAT Control (Output), PAYE Payable, and Withholding Tax Payable.

**FR-ACCT-013:** The system shall prevent deletion and deactivation of system accounts (accounts flagged `is_system = true`) by any user role, including Super Admin; the deactivation and delete controls shall be hidden for system accounts in the UI.

**FR-ACCT-014:** The system shall display a visual indicator (e.g., a lock icon) beside each system account in the CoA tree to distinguish it from user-created accounts.

## 2.6 Currency

**FR-ACCT-015:** The system shall associate each GL account with exactly 1 functional currency selected from the platform's configured currency list; accounts denominated in a foreign currency shall be revalued at period-end using the platform exchange rate in effect on the closing date.

## 2.7 Audit and Metadata

**FR-ACCT-016:** The system shall record a timestamped audit log entry — capturing `user_id`, `action` (create/edit/deactivate/reactivate), `changed_fields`, and `timestamp` — for every change to any GL account.

**FR-ACCT-017:** The system shall allow an authorised user to view the full audit history of any GL account from within the account detail screen.
