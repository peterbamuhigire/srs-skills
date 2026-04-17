# Strategic Initiative Management and Executive Reporting

## 6.1 Overview

Strategic initiatives are discrete, time-bound projects and programmes that drive progress against one or more strategic objectives. The initiative register provides a lightweight tracking mechanism — not a full project management system — recording status, budget, owner, timeline, and objective linkage. The executive report engine generates a board-ready PDF snapshot of the scorecard state at any point in time.

## 6.2 Strategic Initiative Register

**FR-BSC-045:** The system shall allow a user with the `strategy.admin` role to create a strategic initiative by supplying the following mandatory fields: initiative title (free text, max 200 characters), description (free text, max 1,000 characters), initiative owner (active user account), start date, planned end date, and at least 1 linked strategic objective (selected from active objectives); the system shall assign a unique identifier in the format `INIT-{NNNN}` upon creation.

**FR-BSC-046:** The system shall allow an initiative owner or `strategy.admin` user to set the initiative status to one of 5 states: Planned, In Progress, On Hold, Completed, or Cancelled; status transitions shall be unrestricted except that a Completed or Cancelled initiative shall not be set back to In Progress without first providing a reactivation reason (free text, max 300 characters).

**FR-BSC-047:** The system shall allow an initiative owner or `strategy.admin` user to record a planned budget amount and an actual spend-to-date amount for each initiative, both stored as decimal values in the tenant's functional currency; the system shall calculate and display budget variance as:

$$BudgetVariance = PlannedBudget - ActualSpend$$

## 6.3 Initiative-to-Objective Linkage

**FR-BSC-048:** The system shall allow each initiative to be linked to 1 or more strategic objectives from the same tenant; the system shall display all initiatives linked to a given objective in the objective detail screen (see FR-BSC-044 drill-down level 2), showing initiative identifier, title, status, owner, and planned end date.

**FR-BSC-049:** The system shall display a **Strategic Initiatives** section on the executive scorecard dashboard listing all active (Planned or In Progress) initiatives, sorted by planned end date ascending, with RAG-style status indicators: Green (In Progress, end date > 14 days away), Amber (In Progress, end date ≤ 14 days away), Red (In Progress, end date passed without Completed status), or Grey (Planned).

## 6.4 Initiative Status Updates

**FR-BSC-050:** The system shall allow the initiative owner to post a status update — comprising a progress note (free text, max 500 characters), percentage completion (integer 0–100), and updated actual spend — at any time; the system shall store each update as an immutable record in the `initiative_updates` table with `posted_by`, `posted_at`, and all supplied fields.

**FR-BSC-051:** The system shall display the full chronological status update history for each initiative in the initiative detail screen, most-recent update shown first.

## 6.5 Executive Report Generation

**FR-BSC-052:** The system shall generate a PDF executive scorecard report when a user with the `executive` or `strategy.admin` role selects **Generate Report** and specifies a reporting period; the report shall include:

- Tenant name, logo (if configured), report title, and reporting period on the cover page.
- Mission and vision statements.
- Scorecard summary (total objectives, RAG counts, period).
- One section per active BSC perspective, each showing: perspective name, aggregate RAG status, all objective cards (objective title, owner, aggregate score, RAG indicator), and for each objective, all linked KPIs with actual, target, score, and RAG status.
- Strategic initiatives summary table (identifier, title, owner, status, planned end date, budget variance).
- Report generation timestamp and generating user name in the footer.

**FR-BSC-053:** The system shall generate the executive PDF report within ≤ 15 seconds at P95 for a tenant with up to 8 perspectives, 40 objectives, 120 KPIs, and 30 initiatives; the resulting file shall be made available for immediate download and shall be retained in the tenant's report archive for 90 days.
