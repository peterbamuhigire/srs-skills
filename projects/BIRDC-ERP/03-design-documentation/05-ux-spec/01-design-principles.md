# 1. Design Principles

## 1.1 DC-001: Zero Mandatory Training

*DC-001 is the primary design constraint.* Every screen a staff member uses daily must be self-discoverable. A newly hired accounts assistant must post a journal entry correctly; a newly deployed field agent must process a cash sale — both without reading a manual.

**DC-001 Validation Standard:** Prossy (Factory Gate Cashier, S4 education, basic smartphone user) is the benchmark. If Prossy cannot complete a POS transaction from product search to printed receipt in ≤ 90 seconds on first attempt with no coaching, the screen fails DC-001.

### DC-001 Validation Checklist for Screen Design

Each screen submitted for review must be checked against all items before it is accepted:

1. The primary action is accessible in ≤ 3 taps or clicks from the panel home screen.
2. All interactive elements (buttons, inputs, dropdowns) have visible, descriptive labels — no icon-only controls without adjacent text labels.
3. Error messages identify the specific field in error and state the corrective action: "Agent name is required — enter the agent's full name."
4. Confirmation dialogs for destructive or financial actions state the exact consequence: "This will post Journal Entry JE-2026-0047 to the GL. This action cannot be undone."
5. Status indicators (loading, saving, syncing, offline) are always visible and use plain language, not technical codes.
6. Field labels appear above input fields (not as placeholder text that disappears on entry).
7. Required fields are marked with a red asterisk (*) before the label.
8. The primary action button is the largest, highest-contrast element on the screen.
9. Navigation breadcrumb is visible on every non-home screen: `Sales > Invoices > INV-2026-0123`.
10. The screen functions correctly when the font size is increased to 125% (accessibility).

## 1.2 Tabler UI + Bootstrap 5 Component Standards

The BIRDC ERP web application uses Tabler admin UI built on Bootstrap 5. The following component standards are mandatory across all screens.

### Colour Palette

| Token | Hex | Usage |
|---|---|---|
| Primary | `#206bc4` | Primary action buttons, active nav items, links |
| Success | `#2fb344` | Approved status badges, success alerts, positive variance |
| Warning | `#f76707` | Pending status badges, threshold alerts (80% budget used) |
| Danger | `#d63939` | Error messages, blocked actions, negative variance, VOID status |
| Secondary | `#667382` | Secondary labels, helper text, inactive nav items |
| Background | `#f4f6fa` | Page background (not white — reduces eye strain for all-day users) |

### Typography

| Element | Specification |
|---|---|
| Body text | 14px, `font-weight: 400`, colour `#1d273b` |
| Table cell text | 13px — maximises data density on standard monitors |
| Labels | 12px, `font-weight: 500`, `text-transform: uppercase`, `letter-spacing: 0.05em` |
| Page headings (H1) | 20px, `font-weight: 600` |
| Card headings (H3) | 15px, `font-weight: 600` |
| Monetary values | Monospace font (`font-family: 'JetBrains Mono', monospace`) — ensures column alignment in financial tables |

### Component Usage Rules

- **Cards:** All screen content sections are wrapped in Tabler `.card` components. Cards have a white background, 4px border radius, 1px `#e6e7e9` border.
- **Buttons:** Use Tabler button classes exclusively. Primary action = `.btn-primary`. Destructive action = `.btn-danger`. Cancel/back = `.btn-outline-secondary`. Never use custom colours for buttons.
- **Tables:** All data tables use DataTables with server-side pagination. Column headers are sortable by default. Monetary columns are right-aligned. Action columns are fixed-width on the right.
- **Status Badges:** All status fields use `.badge` with the colour mapping in Section 1.2. Status text is always capitalised: `DRAFT`, `APPROVED`, `POSTED`, `VOID`.
- **Form Layout:** All forms use a 2-column Bootstrap grid on desktop (col-md-6 per field). Financial entry forms (journal entries, invoices) use a full-width layout to maximise the line-item table.
- **Modals:** Confirmation dialogs and quick-entry forms use Tabler `.modal`. Maximum modal width is 800px. Modals never nest.
- **Alerts:** System alerts use `.alert-*` with a dismiss button. Validation errors appear inline below the relevant field, not in a top-level alert.
- **Select2:** All dropdown inputs with > 10 options use Select2 with search enabled. Agent names (1,071), farmer names (6,440+), and chart of accounts (1,307 accounts) always use Select2.
- **Flatpickr:** All date and date-time inputs use Flatpickr. Date format: `DD/MM/YYYY`. Date-time format: `DD/MM/YYYY HH:mm`.
- **SweetAlert2:** All confirmation dialogs before financial posting, deletion, or approval use SweetAlert2. Never use the browser's native `confirm()`.

## 1.3 Information Hierarchy

Every screen must present information in this priority order:

1. **What am I looking at?** — Page title, breadcrumb, entity identifier (e.g., `Invoice INV-2026-0123 — Kampala Supermarket`).
2. **What is its current status?** — Status badge, prominent and colour-coded, immediately below the title.
3. **What are the key figures?** — Summary KPI cards at the top: totals, balances, quantities. Never bury the headline number in a table.
4. **What actions can I take?** — Action buttons in a fixed button bar at the top right of the content area. Buttons are ordered: primary action first, secondary actions, then destructive action last with a visual separator.
5. **Detail data** — Full data tables, line items, audit history — below the summary, collapsible where appropriate.

## 1.4 Error Messaging Standards

All error messages must comply with the following pattern:

**Format:** `[What happened] — [Why it happened] — [What to do]`

**Examples:**

| Scenario | Correct Error Message | Prohibited Message |
|---|---|---|
| Agent float limit exceeded | "Stock issuance blocked — this transfer would exceed Samuel Okello's float limit of UGX 2,500,000. Reduce the quantity or increase the float limit in Agent Settings." | "Error: Float limit exceeded." |
| Mass balance fails | "Production order cannot be closed — outputs total 485 kg but input was 500 kg. The 15 kg gap exceeds the 2% tolerance (10 kg). Record the missing by-product or scrap allocation." | "Mass balance error." |
| Required field missing | "Agent name is required — enter the agent's full name before saving." | "Please fill in all required fields." |
| Duplicate invoice number | "Invoice number INV-2026-0122 is already used — the system has assigned INV-2026-0147 as the next available number." | "Duplicate record." |
| Session expired | "Your session has expired after 30 minutes of inactivity. Your unsaved changes have been stored as a draft — click 'Restore Draft' to continue." | "Session expired. Please log in again." |
