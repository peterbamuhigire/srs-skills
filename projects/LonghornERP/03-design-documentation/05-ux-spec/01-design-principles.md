# Design Principles for Longhorn ERP

## 1. The Golden Rule: Zero Mandatory Training (NFR-USAB-001)

**NFR-USAB-001** defines the primary usability contract for Longhorn ERP: any user who holds the correct role and permissions must complete their first task unassisted within 10 minutes of logging in, with no prior product training.

Operationally, this means:

- Every screen must communicate its purpose within 3 seconds of load — the page title, primary action button, and key data must be immediately visible without scrolling.
- Navigation labels use common business language ("Invoices", "Purchase Orders", "Payroll Run") — never system-internal identifiers or developer terminology.
- Primary actions appear in consistent locations across all modules: the **+ Add** / **+ New** button is always top-right of every list view; the **Save** button is always bottom-right of every form.
- Empty states on list views display an explicit instruction: "No records found. Click **+ Add** to create your first record." — eliminating dead-end screens.
- Contextual help text (≤ 20 words) appears directly below complex or risk-bearing fields — no help icon hunting required.
- Destructive and irreversible actions (post, void, reverse) are visually distinct from non-destructive actions and require a confirmation dialog before execution.

Compliance with NFR-USAB-001 is verified by the usability benchmarks in Section 1.3.

## 2. The Five Design Principles

### 2.1 Clarity Over Cleverness

Every interaction pattern must be immediately recognisable to a user trained in basic ERP concepts. Innovative UI patterns are adopted only when they reduce cognitive load by a measurable degree; otherwise, the conventional pattern is used. Form labels are always explicit nouns ("Invoice Date", not "Date"). Abbreviations in the interface are prohibited unless the full term exceeds 30 characters and the abbreviation is a universally known business term (e.g., "VAT", "PAYE", "PO").

### 2.2 Progressive Disclosure

Advanced options, secondary fields, and configuration controls are hidden by default and revealed on demand via clearly labelled expand controls ("Advanced Options ▾", "Add Deduction +"). List views show the 6–8 columns most critical to the user's primary task; additional columns are accessible via a column-chooser control. Wizard flows (payroll run, period close, bulk import) break complex multi-step processes into discrete, labelled steps with visible progress indicators.

### 2.3 Error Prevention Before Error Recovery

The system prevents invalid states rather than correcting them after the fact:

- Numeric inputs enforce type constraints client-side (no letters in amount fields).
- Date pickers enforce valid range constraints (e.g., invoice date cannot exceed today + 365 days; payroll period must be an open period).
- The **Post** button on journal entries and invoices is disabled until all validation rules pass — the user never reaches a server-side rejection for a preventable input error.
- Duplicate detection (duplicate invoice number, duplicate employee code) runs on blur of the relevant field, not on form submission.

### 2.4 Consistency Within and Across Modules

All modules share the same structural template: list view → detail/form view → sub-list views. The same component handles the same task everywhere: Select2 for all searchable dropdowns, Flatpickr for all date inputs, DataTables for all list views. Colour semantics are fixed across the entire application (see Section 3 — Colour Palette): green always means approved/active, amber always means pending/draft, red always means error/rejected. No module may override these conventions.

### 2.5 Accessibility as Baseline, Not Afterthought

WCAG 2.1 AA compliance is a build-time requirement, not a post-launch audit item. Accessibility requirements are enforced at the component level so all modules inherit compliance automatically. No feature is considered complete until it passes the accessibility requirements listed in Section 1.4.

## 3. Usability Benchmarks

| Metric | Target | Measurement Method |
|---|---|---|
| First-task completion time (new user, trained role) | ≤ 10 min | Moderated usability test, Task 1 scenario per module |
| Error rate after 2 sessions | < 5% of task steps | Error log analysis during usability testing |
| Navigation to target screen | ≤ 3 clicks from dashboard | Click-path audit per user story |
| Form submission success on first attempt | ≥ 90% | Form analytics, server-side validation rejection rate |
| Page load time (list view, 100-row result) | ≤ 2 s at P95 | Browser performance profile, simulated 10 Mbps connection |
| Mobile task completion rate (primary flows) | ≥ 85% | Usability test on Android/iOS reference devices |

## 4. WCAG 2.1 AA Accessibility Requirements

| Requirement | Standard | Specification |
|---|---|---|
| Colour contrast — body text | WCAG 1.4.3 | ≥ 4.5:1 contrast ratio against background |
| Colour contrast — large text (≥ 18 px or ≥ 14 px bold) | WCAG 1.4.3 | ≥ 3:1 contrast ratio |
| Colour contrast — interactive component boundaries | WCAG 1.4.11 | ≥ 3:1 against adjacent background |
| Keyboard navigation | WCAG 2.1.1 | All interactive elements reachable via Tab / Shift+Tab; logical tab order matches visual order |
| Focus indicator | WCAG 2.4.7 | Visible focus ring on all focusable elements; minimum 2 px outline |
| Form field labels | WCAG 1.3.1 | Every input has an associated `<label>` element or `aria-label`; placeholder text alone is not acceptable as a label |
| Error identification | WCAG 3.3.1 | Error messages identify the field and describe the required correction in plain language |
| Skip navigation | WCAG 2.4.1 | "Skip to main content" link present as first focusable element on every page |
| Image alt text | WCAG 1.1.1 | All non-decorative images carry descriptive `alt` attributes; decorative images use `alt=""` |
| Session timeout warning | WCAG 2.2.1 | User receives a 2-minute warning before session expiry with option to extend |
| Reflow | WCAG 1.4.10 | Content reflows at 320 px viewport width without horizontal scrolling (except data tables) |
