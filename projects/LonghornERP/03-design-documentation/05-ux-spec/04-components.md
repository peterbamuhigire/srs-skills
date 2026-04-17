# Standard UI Component Patterns

## 1. List Views — DataTables (Server-Side)

All list views in Longhorn ERP use DataTables configured for server-side processing. Client-side DataTables are prohibited for any dataset that may exceed 500 rows.

### 1.1 Standard Configuration

| Setting | Value |
|---|---|
| Default page size | 25 rows |
| Page size options | 10, 25, 50, 100 |
| Pagination style | Full numbers with first/last controls |
| Column sorting | Enabled on all non-action columns; default sort on primary identifier descending |
| Global search | Input field, top-right of table header bar; debounced at 400 ms |
| Processing indicator | Spinner overlay on table body during AJAX calls |
| Responsive mode | Column priority collapse on viewports < 768 px |

### 1.2 Table Header Bar Layout

```
[+ Add Button]  [Export: CSV | Excel | PDF]          [Search: ____________]
```

- **+ Add** button: Primary Navy, left-aligned.
- Export button group: outlined secondary buttons, left of centre.
- Search input: right-aligned, width 240 px, placeholder "Search…".
- Additional filters (date range, status dropdown) appear between the export group and the search input when the module requires them.

### 1.3 Column Layout Standard

- Column 1: Primary identifier (e.g., Invoice No., Employee Code). Always sortable. Renders as a clickable link to the detail view.
- Column 2: Primary descriptor (e.g., Customer Name, Item Name). Sortable.
- Columns 3–N: Supporting data columns. Sortable where meaningful.
- Final column: **Actions** — right-aligned, fixed width 140 px, not sortable. Contains: `View | Edit | [contextual]`.
  - Contextual action examples: `Post`, `Void`, `Print`, `Approve`.
  - Actions beyond 3 collapse into a kebab menu (⋮).

### 1.4 Empty State

When a list view returns 0 records, the table body is replaced with:

```
[Illustration: empty document stack]
No records found.
Click + Add to create your first record.
[+ Add Button — Primary Navy]
```

The illustration is decorative (alt=""). The message text is 16 px, colour #6B7280. The embedded **+ Add** button duplicates the header button for convenience.

### 1.5 Row Selection

Bulk actions (bulk approve, bulk export, bulk delete) display a checkbox in column 1. When ≥ 1 row is selected, a contextual bulk-action bar appears above the table:

```
[N rows selected]  [Bulk Action Dropdown ▾]  [Clear Selection ×]
```

---

## 2. Forms

### 2.1 Field Layout

- Labels are positioned above their input — never beside or as placeholder-only.
- Required fields display a red asterisk (*) immediately after the label text, with `aria-required="true"` on the input.
- Field helper text (≤ 20 words) appears below the input in 12 px muted text (#6B7280) at all times — it does not disappear when the field receives focus.
- Field groups (e.g., "Customer Details", "Payment Terms") are wrapped in Bootstrap cards with an H3 section heading.

### 2.2 Validation Behaviour

| Trigger | Behaviour |
|---|---|
| User leaves field (blur) | Inline validation runs immediately; error border and message appear below the field |
| Form submit with invalid fields | All invalid fields highlight; page scrolls to the first error; focus is set on the first invalid field |
| Error cleared | Error state clears as soon as the field value becomes valid (on `input` event, not on blur) |

Error message style: 12 px, Danger red #DC2626, appears directly below the field with a 4 px top margin. Prefix with the field name: "Invoice Date is required." / "Amount must be a positive number."

### 2.3 Input Component Assignments

| Scenario | Component |
|---|---|
| Dropdown with ≤ 5 static options | Native Bootstrap `<select>` |
| Dropdown with > 5 options or remote data | Select2 (with search enabled) |
| Date input (date only) | Flatpickr, format DD/MM/YYYY |
| Date-time input | Flatpickr with `enableTime: true`, format DD/MM/YYYY HH:mm |
| Date range input | Flatpickr range mode |
| File upload (single or multiple) | Dropzone.js; accepted types and max size displayed inside the drop zone |
| Rich text (notes, descriptions) | Plain `<textarea>` with character counter; rich text editor is not used in transactional forms |
| Currency amount | Numeric input; thousand-separator formatting applied on blur; 2 decimal places enforced |
| Percentage | Numeric input; range 0–100; displays % suffix |

### 2.4 Form Footer

The form footer is a fixed bar at the bottom of the main content area when the form is longer than the viewport.

```
[Cancel Button — outlined]                    [Save Draft]  [Save Button — Primary Navy]
```

- **Cancel**: Outlined secondary button. On click, triggers unsaved-changes guard if the form is dirty.
- **Save Draft** (where applicable): Steel Blue outlined button.
- **Save / Post**: Primary Navy filled button. Right-most position.
- Destructive irreversible action buttons (e.g., **Post**, **Void**) are Primary Navy and visually distinguished from Save with a lock icon prefix.

### 2.5 Unsaved-Changes Guard

When a user attempts to navigate away from a dirty form (via breadcrumb, sidebar, browser back, or page refresh), a SweetAlert2 confirmation dialog fires:

- **Title:** "Unsaved Changes"
- **Body:** "You have unsaved changes. Leaving this page will discard them."
- **Buttons:** "Leave Page" (Danger red) | "Stay" (Primary Navy)

The guard is implemented via the `beforeunload` event for browser navigation and via a navigation intercept wrapper for in-app routing.

---

## 3. Modals

### 3.1 Usage Rules

Modals are used for:

- Quick-add forms where the result immediately populates a parent form field (e.g., "Add New Customer" from within an invoice form).
- Confirmation dialogs for irreversible actions (see Section 4).
- Preview panes (PDF invoice preview, report preview) where the user reads content without editing.

Modals are not used for:

- Full CRUD forms that have more than 8 fields (use a dedicated form page instead).
- Nested modals. A modal must never open another modal.
- Displaying list views or DataTables.

### 3.2 Size Variants

| Variant | Max Width | Use |
|---|---|---|
| Standard | 600 px | Confirmation dialogs, quick-add forms (≤ 6 fields) |
| Wide | 900 px | Complex quick-add forms (7–12 fields), PDF preview |
| Full-screen | 100% viewport | Document editor, image viewer (triggered by explicit user action only) |

### 3.3 Structure

```
┌─────────────────────────────────────┐
│ [Title]                          [×] │
├─────────────────────────────────────┤
│                                      │
│   [Modal body content]               │
│                                      │
├─────────────────────────────────────┤
│ [Cancel — outlined]  [Action Button] │
└─────────────────────────────────────┘
```

- Header: modal title (H2, 18 px, Primary Navy) + close button (×) right-aligned.
- Footer: action buttons right-aligned. Cancel button always present.
- The modal closes on close button click, Cancel button click, and Escape key. Clicking the backdrop closes the modal only on non-destructive, non-form modals.

---

## 4. Confirmation Dialogs (SweetAlert2)

Every destructive or irreversible action must be confirmed before execution. "Destructive or irreversible" includes: delete, void, reverse, write-off, period close, payroll post, GL post.

### 4.1 Destructive Action Dialog

| Element | Content |
|---|---|
| Icon | Warning triangle (amber) |
| Title | "Are you sure?" |
| Body | Specific consequence in plain language — e.g., "This will permanently void Invoice INV-2026-00123. This action cannot be undone." |
| Confirm button | "Yes, Void" (or "Yes, Delete", "Yes, Reverse") — Danger red (#DC2626) |
| Cancel button | "Cancel" — grey outlined |

### 4.2 Non-Destructive Approval Dialog

Used for approve, submit, and post actions that are reversible by an administrator.

| Element | Content |
|---|---|
| Icon | Question circle (blue) |
| Title | "Confirm [Action]?" |
| Body | Summary of what will happen — e.g., "This will submit Payroll Run PR-2026-04 for approval. 47 employees will be included." |
| Confirm button | "Confirm" — Primary Navy |
| Cancel button | "Cancel" — grey outlined |

### 4.3 Behaviour

- The confirm button is disabled for 1 second after the dialog opens to prevent accidental double-click confirmation.
- The dialog is not dismissible by pressing Escape or clicking the backdrop — the user must explicitly click Confirm or Cancel.

---

## 5. Toast Notifications

Toast notifications provide non-blocking feedback for completed actions.

| Type | Background | Icon | Duration | Dismiss |
|---|---|---|---|---|
| Success | #16A34A | Check circle | 3 s auto-dismiss | Auto + manual × |
| Error | #DC2626 | X circle | Persists until dismissed | Manual × only |
| Warning | #D97706 | Warning triangle | 5 s auto-dismiss | Auto + manual × |
| Info | #1D4ED8 | Info circle | 4 s auto-dismiss | Auto + manual × |

- Position: top-right, 16 px from top and right edges, stacked with 8 px gap between toasts.
- Maximum 4 simultaneous toasts. If a 5th fires, the oldest auto-dismiss toast is removed immediately.
- Toast text: 14 px, white, max 2 lines. Long messages are truncated with a "See details" link that opens the relevant record or log.
- Screen readers: toasts are rendered in an `aria-live="polite"` region (success/info/warning) or `aria-live="assertive"` region (error).

---

## 6. Loading and Progress States

| Context | Pattern |
|---|---|
| Full page initial load | Skeleton screens (grey animated blocks matching the page layout) — not a spinner overlay |
| AJAX table reload | Spinner overlay on the table body only; rest of page remains interactive |
| Form submission in progress | Save button shows spinner and "Saving…" label; button is disabled; form fields are disabled |
| Wizard step transition | Step indicator updates; content area fades out (150 ms) and fades in (150 ms) |
| File upload progress | Dropzone progress bar per file; overall progress bar above the drop zone for multi-file batches |
| Background report generation | Progress bar in a toast notification with percentage; "View Report" link appears on completion |
