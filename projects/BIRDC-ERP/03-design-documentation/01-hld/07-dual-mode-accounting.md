# 7. Dual-Mode Accounting Design

## 7.1 Requirement

Design Covenant DC-004 requires that PIBID parliamentary budget votes and BIRDC commercial IFRS accounts are tracked simultaneously in the same system, with consolidated and separated reporting always available.

## 7.2 Chart of Accounts Structure

The single chart of accounts (1,307 accounts) serves both modes simultaneously.

[CONTEXT-GAP: GAP-012] — BIRDC Finance Director must confirm whether an existing Chart of Accounts is to be imported or whether the 1,307-account structure is to be designed from scratch. The design below assumes a unified CoA is designed as part of Phase 2.

Each account in `tbl_coa_accounts` carries the following classifying columns:

| Column | Type | Purpose |
|---|---|---|
| `account_code` | VARCHAR(20) | Hierarchical account code (parent-child via `parent_id`) |
| `account_type` | TINYINT | Asset, Liability, Equity, Revenue, Expense |
| `entity_mode` | TINYINT | 0 = BIRDC Commercial only; 1 = PIBID Parliamentary only; 2 = Both modes |
| `segment_code` | VARCHAR(10) | Parliamentary segment / vote code (NULL for commercial-only accounts) |
| `cost_centre` | VARCHAR(20) | Department or cost centre code (applies to both modes) |
| `budget_vote_id` | INT NULL | FK to `tbl_budget_votes` (for PIBID accounts); NULL for commercial-only |
| `ifrs_classification` | VARCHAR(30) | IFRS for SMEs line item mapping (P&L or Balance Sheet) |

## 7.3 Segment and Cost Centre Approach

Parliamentary accountability is achieved via **segment coding** on the chart of accounts and **vote codes** on expenditure transactions:

- Each PIBID-applicable account is tagged with a `segment_code` corresponding to the parliamentary vote (e.g., `DEV-001` for Development Vote, `REC-001` for Recurrent Vote).
- Each journal line can additionally carry a `cost_centre` code for departmental breakdowns shared across both modes.
- A single journal entry (e.g., payment to a supplier) carries both the IFRS account code (for commercial P&L) and the parliamentary segment/vote code (for budget tracking) on the same journal lines.

## 7.4 How a Transaction Appears in Both Reports

**Example:** Payment of UGX 5,000,000 for fertiliser under PIBID Development Vote DEV-001.

```
GL Journal Entry:
  DR  5100-Fertiliser-Expense   5,000,000   [segment: DEV-001, cost_centre: AGR]
  CR  1010-Bank-Account         5,000,000   [segment: DEV-001, cost_centre: AGR]
```

- In the **BIRDC Commercial P&L:** this entry appears as an Operating Expense under "Agricultural Inputs" (account 5100), reducing commercial profit.
- In the **PIBID Parliamentary Budget vs. Actual:** this entry is captured as expenditure against Development Vote DEV-001, reducing the remaining vote balance.
- In the **Consolidated Report:** both views are present side by side.

## 7.5 Financial Statement Generation

| Statement | Mode | Source |
|---|---|---|
| Trial Balance | Both (filtered by `entity_mode`) | `vw_trial_balance` with mode filter |
| Profit & Loss (IFRS) | BIRDC Commercial | Journal lines where `entity_mode IN (0, 2)` |
| Balance Sheet | BIRDC Commercial | Journal lines where `entity_mode IN (0, 2)` |
| Cash Flow Statement (IAS 7) | BIRDC Commercial | Derived from GL journals |
| Budget vs. Actual | PIBID Parliamentary | `vw_budget_vs_actual` joining `tbl_budget_votes` |
| Vote Expenditure Report | PIBID Parliamentary | Journal lines filtered by `segment_code` |
| Consolidated Report | Both | Union of both modes with clear labelling |

All financial statements are available on demand without period-closing (living reports from live journal data). Period closing is an optional process for year-end archiving only.

## 7.6 Accounting Period Management

Two fiscal years coexist:

- **PIBID Parliamentary:** July 1 – June 30 (aligned to Uganda government financial year)
- **BIRDC Commercial:** January 1 – December 31 (or aligned to PIBID fiscal year — [CONTEXT-GAP: GAP-012] confirm with Finance Director)

Both fiscal year configurations are managed in `tbl_accounting_periods`. Reports accept a date range input rather than a period code, enabling cross-year analysis.
