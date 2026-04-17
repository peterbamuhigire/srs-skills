# UX Specification — Academia Pro Phase 1

**Document ID:** DD-05-01
**Project:** Academia Pro
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review

---

## 1. Design System

### 1.1 Framework

The web application uses the **Tabler** admin template (Bootstrap 5 derivative) as the base component library. All screens are built from Tabler components with a custom colour theme applied via CSS custom properties. No custom CSS framework is created — Tabler provides all layout, form, table, card, and navigation components.

The Android app (Phase 3+) uses **Material 3** (Jetpack Compose) with custom colour mapping to match the web palette. The iOS app (Phase 9+) uses **SwiftUI** with a custom colour asset catalogue.

### 1.2 Colour Palette

| Token | Hex | Usage |
|---|---|---|
| `--primary` | `#206bc4` | Primary actions, active navigation, links |
| `--primary-dark` | `#1a56a0` | Hover/pressed state for primary |
| `--secondary` | `#656d77` | Secondary text, muted icons |
| `--success` | `#2fb344` | Positive status (present, paid, promoted) |
| `--warning` | `#f76707` | Warnings (arrears, low attendance) |
| `--danger` | `#d63939` | Destructive actions, errors, absent status |
| `--info` | `#4299e1` | Informational badges, tooltips |
| `--bg-surface` | `#f4f6fa` | Page background |
| `--bg-card` | `#ffffff` | Card and modal background |
| `--text-primary` | `#1e293b` | Headings, primary body text |
| `--text-secondary` | `#64748b` | Captions, helper text |
| `--border` | `#e2e8f0` | Card borders, dividers, table rows |

All colour combinations meet **WCAG 2.1 AA** contrast ratio of 4.5:1 for normal text and 3:1 for large text.

### 1.3 Typography

| Element | Font | Size | Weight | Line Height |
|---|---|---|---|---|
| Page title (h1) | Inter | 24px / 1.5rem | 600 | 1.3 |
| Section heading (h2) | Inter | 20px / 1.25rem | 600 | 1.3 |
| Card title (h3) | Inter | 16px / 1rem | 600 | 1.4 |
| Body text | Inter | 14px / 0.875rem | 400 | 1.5 |
| Small / caption | Inter | 12px / 0.75rem | 400 | 1.5 |
| Monospace (codes, IDs) | JetBrains Mono | 13px | 400 | 1.4 |

### 1.4 Spacing Scale

Based on a 4px base unit: `4, 8, 12, 16, 24, 32, 48, 64`.

| Token | Value | Usage |
|---|---|---|
| `--space-xs` | 4px | Icon-to-text gap |
| `--space-sm` | 8px | Between related elements |
| `--space-md` | 16px | Card padding, form field gap |
| `--space-lg` | 24px | Section separation |
| `--space-xl` | 32px | Page section margin |

### 1.5 Component Library

All components are standard Tabler widgets. Custom components specific to Academia Pro:

| Component | Description |
|---|---|
| `StudentCard` | Compact student summary: photo, name, admission number, class, status badge |
| `FeeBalanceWidget` | Colour-coded balance display: green (cleared), amber (partial), red (outstanding) |
| `AttendanceGrid` | Daily calendar grid with status-coloured cells (present/absent/late/excused) |
| `GradeChip` | Inline badge displaying grade (D1, B+, HC, etc.) with curriculum-appropriate colour |
| `PromotionWizardStepper` | Multi-step wizard with class-by-class progression and summary counts |
| `ReportCardPreview` | In-page preview of report card layout before PDF generation |

---

## 2. Information Architecture

### 2.1 Navigation Structure

The primary navigation is a **left sidebar** (collapsible on mobile) with role-filtered menu items. The sidebar is persistent across all pages.

#### School Admin Workspace (School Owner / Head Teacher / Bursar)

```
Dashboard
├── Overview (KPI cards: students, fees collected, attendance %)
├── Quick Actions (admit student, record payment, take attendance)
│
Students
├── Student List (searchable, filterable by class/status)
├── Admit Student (wizard form)
├── Student Profile (tabbed: details, fees, attendance, marks)
│
Academics
├── Academic Years (list + create)
├── Classes (list + create + assign teacher)
├── Subjects (list + create)
├── Timetable (visual grid editor per class)
├── Promotion Wizard (year-end — conditional visibility)
│
Fees
├── Fee Structures (per class/term configuration)
├── Record Payment (search student → enter amount)
├── Receipts (searchable receipt list)
├── Refund Requests (list + approve/reject)
├── Fee Reports
│   ├── Collection Summary
│   └── Defaulters List
│
Attendance
├── Take Attendance (class selector → student checklist)
├── Attendance Reports
│   ├── Monthly Report
│   └── Termly Summary
│
Examinations
├── Exam Setup (create exams, configure subjects/weights)
├── Enter Marks (class → exam → subject → mark grid)
├── Grading Results (computed grades per class)
├── UNEB Export (P7, S4, S6 classes only)
│
Reports
├── Report Cards (single student or bulk class)
├── School Performance (aggregate dashboard)
│
Users
├── User List (searchable by role)
├── Invite User
├── Role Management
│
Settings
├── School Profile
├── Data Import (student import wizard)
├── Audit Log
├── EMIS Export
```

#### Role-Based Menu Filtering

| Menu Section | Owner | HT | CT | Bursar | Receptionist | Parent | Student |
|---|---|---|---|---|---|---|---|
| Dashboard | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Students | ✓ | ✓ | ✓* | — | ✓ | — | — |
| Academics | ✓ | ✓ | ✓* | — | — | — | — |
| Fees | ✓ | ✓ | — | ✓ | — | ✓* | ✓* |
| Attendance | ✓ | ✓ | ✓ | — | — | ✓* | ✓* |
| Examinations | ✓ | ✓ | ✓ | — | — | — | — |
| Reports | ✓ | ✓ | ✓* | ✓* | — | ✓* | ✓* |
| Users | ✓ | ✓ | — | — | — | — | — |
| Settings | ✓ | ✓ | — | — | — | — | — |

`*` = limited view (own class only, own child only, own record only).

---

## 3. Key Screen Specifications

### 3.1 Dashboard

**Layout:** 3-column responsive grid (stacks to 1 column on mobile).

**Row 1 — KPI Cards (4 cards):**
- Total Students (active count)
- Fee Collection Rate (% of billed collected this term)
- Today's Attendance (% present)
- Pending Actions (count of unresolved items: pending refunds, unlocked exams, retention locks)

**Row 2 — Charts (2 cards):**
- Fee Collection Trend (bar chart: monthly collection vs billed, current term)
- Attendance Trend (line chart: daily attendance % over last 30 school days)

**Row 3 — Action Lists (2 cards):**
- Recent Payments (last 10 payments with student name, amount, date)
- Alerts (students with 3+ consecutive absences, pending refund approvals)

### 3.2 Student List

**Layout:** Full-width data table with toolbar.

**Toolbar:** Search input (name, admission number, NIN, LIN) | Class filter dropdown | Status filter dropdown | "Admit Student" primary button.

**Table Columns:** Photo (avatar), Full Name, Admission No., Class, Status (badge), Guardian Phone, Actions (view, edit).

**Pagination:** 25 per page, standard page navigation.

**Empty State:** Illustration + "No students enrolled yet. Click Admit Student to begin."

### 3.3 Admit Student Form

**Layout:** Single-page form with fieldsets, not a multi-step wizard (student admission is a single-action operation).

**Fieldsets:**
1. **Student Identity:** First name*, Last name*, Middle name, Date of birth* (date picker), Gender* (radio: male/female)
2. **Enrollment:** Class* (dropdown of active classes), Admission date* (date picker, defaults to today), Local admission number (optional, auto-generated if blank)
3. **Identifiers:** NIN (optional, shown only if DOB indicates age 16+), LIN (optional)
4. **Guardian:** Guardian name, Phone (with +256 prefix helper), Relationship (dropdown: father/mother/guardian/other)

**NIN/LIN Lookup:** When NIN or LIN is entered and the field loses focus, the system calls `GET /students/lookup` in the background. If a match is found, a card appears showing the existing global student's name, DOB, and current enrollment status. If the student is already enrolled at another school, a warning is displayed: "This student has an active enrollment at [school name]. They must be transferred out before admitting here."

**Submit:** "Admit Student" primary button. On success → redirect to the new student's profile page.

### 3.4 Record Payment

**Layout:** Two-panel layout.

**Left Panel — Student Search:**
- Search by name, admission number, or class.
- Search results appear as a list of `StudentCard` components.
- Clicking a student card loads their fee account in the right panel.

**Right Panel — Payment Form:**
- **Fee Summary:** Current term billed, paid, balance. Arrears from prior terms (highlighted in amber if > 0).
- **Payment Fields:** Amount (UGX, number input with thousand-separator formatting), Payment date (date picker, defaults to today), Payment method (radio: cash/bank transfer), Reference (optional text), Note (optional textarea).
- **Submit:** "Record Payment" primary button.
- **On Success:** Receipt modal appears with receipt number, amount, and "Print Receipt" / "Close" buttons.

### 3.5 Take Attendance

**Layout:** Full-width student checklist.

**Header:** Class selector (dropdown) | Date selector (date picker, defaults to today).

**Student List:** Each row shows: student photo, name, admission number, and 4 radio buttons (Present, Absent, Late, Excused). Default selection: Present (pre-selected for all students). Teacher changes only the exceptions.

**Footer:** Student count summary (e.g., "35 students — 32 Present, 2 Absent, 1 Late") | "Submit Attendance" primary button.

**Post-Submit:** Success toast. If any students triggered the 3-consecutive-absence alert, an info banner appears: "SMS alerts sent to 2 guardians."

### 3.6 Enter Marks

**Layout:** Spreadsheet-style mark entry grid.

**Header:** Class selector | Exam selector | Subject selector.

**Grid:** Rows = students (sorted by admission number). Columns = student name, score input, absent checkbox. The `maximum_mark` is displayed in the column header (e.g., "Score / 100").

**Validation:** Client-side: score input max is set to `maximum_mark`. Server-side: BR-UNEB-005 rejection on out-of-range. For Thematic curriculum, the score input is replaced with a dropdown (HC / C / NYC).

**Footer:** "Save Marks" primary button. On locked exam: all inputs are disabled; a banner reads "Mark entry is locked. Contact the Head Teacher to request an unlock."

### 3.7 Report Card — Single Student

**Layout:** Preview + download.

**Preview Panel:** Rendered HTML preview of the report card layout showing: school header, student details, subject marks/grades, attendance summary, class position (if applicable), teacher comment, head teacher comment.

**Action Bar:** "Download PDF" primary button | "Regenerate" secondary button (visible if marks have changed since last generation).

**Comment Section:** Two textareas below the preview: "Class Teacher Comment" and "Head Teacher Comment". Each has a 500-character limit with live counter. "Save Comments" button saves comments and triggers PDF regeneration.

### 3.8 Promotion Wizard

**Layout:** Stepper + class panel.

**Stepper:** Shows all classes as steps. Each step has a status indicator: green (resolved), amber (in progress), grey (pending).

**Class Panel:** Shows the class name, student count, and destination class. A table lists all students with columns: name, admission number, action (radio: Promote / Repeat / Depart). Default: all set to Promote.

For final-year classes (P7, S4, S6) where `promotes_to = null`, the default action is Depart and the departure reason dropdown is visible.

**Footer:** Summary bar showing counts (e.g., "Promoting: 38, Repeating: 2, Departing: 0") | "Confirm Decisions" primary button.

**Completion:** When all classes are resolved, a success banner appears: "Promotion Wizard complete. You may now activate the new academic year."

---

## 4. Responsive Behaviour

### 4.1 Breakpoints

| Breakpoint | Width | Layout |
|---|---|---|
| Mobile | < 768px | Single column, sidebar collapses to hamburger menu, tables scroll horizontally |
| Tablet | 768–1024px | 2-column where applicable, sidebar collapses but remains accessible |
| Desktop | > 1024px | Full layout, sidebar always visible, 3-column dashboard grid |

### 4.2 Mobile-Specific Adaptations

- **Attendance entry:** Swipeable student cards instead of full table. Swipe right = Present, left = Absent. Tap for Late/Excused.
- **Mark entry:** Single-student-at-a-time view instead of grid. "Previous / Next" navigation buttons.
- **Fee recording:** Full-screen search, then full-screen payment form. No split panel.
- **Data tables:** Horizontal scroll with sticky first column (student name). Column visibility configurable via dropdown.

### 4.3 Low-Bandwidth Support

- All pages must reach First Contentful Paint within 3 seconds on a 3G connection (1.6 Mbps).
- Images: student photos are cropped to 100x100px and served as WebP (fallback JPEG).
- Lazy loading: data tables load first page only; subsequent pages on scroll.
- Bundle size target: < 300 KB gzipped for initial JavaScript payload.

---

## 5. Accessibility Requirements (WCAG 2.1 AA)

| Requirement | Implementation |
|---|---|
| Keyboard navigation | All interactive elements reachable via Tab. Modals trap focus. Escape closes modals. |
| Screen reader support | All form inputs have associated `<label>` elements. Data tables use `<th scope="col">` and `<th scope="row">`. Status badges have `aria-label` (e.g., `aria-label="Status: Active"`). |
| Colour contrast | All text meets 4.5:1 ratio. Status colours always paired with text labels (never colour alone). |
| Focus indicators | Visible focus ring (`outline: 2px solid var(--primary)`) on all interactive elements. |
| Error identification | Form validation errors announced via `aria-live="polite"` region. Error messages reference the field by name. |
| Skip navigation | "Skip to main content" link as first focusable element on every page. |
| Reduced motion | `@media (prefers-reduced-motion: reduce)` disables all animations and transitions. |

---

## 6. Print Specifications

### 6.1 Report Card (PDF)

- **Page size:** A4 portrait (210 × 297 mm).
- **Margins:** 15mm top, 15mm bottom, 20mm left, 20mm right.
- **Header:** School logo (left), school name and address (centre), "TERMLY REPORT CARD" (right). Term and year below.
- **Student Info Block:** Name, admission number, class, DOB, gender — in a bordered box.
- **Marks Table:** Subject | Score | Grade | Remark. Alternating row shading. Bold column headers.
- **Summary Section:** Total marks, average, class position (where applicable), division (PLE/UCE/UACE).
- **Attendance Section:** Days present / total school days, attendance percentage.
- **Comments Section:** Class teacher comment, head teacher comment. Each in a bordered box with the commenter's role label.
- **Footer:** School stamp placeholder, date generated.

### 6.2 Fee Receipt (Printable)

- **Size:** Half A4 (A5 landscape).
- **Content:** School name, receipt number, student name, class, amount paid (UGX, formatted with thousand separators), payment method, date, recorded by.
- **Print trigger:** Browser `window.print()` from the receipt modal. CSS `@media print` hides non-receipt elements.

---

## AI Module UX Patterns

This section specifies the user interface patterns for all AI-powered features. Every AI UI component follows the standards in the `ai-ux-patterns` skill: progressive reveal loading, confidence indicators, human-in-the-loop gates, and transparent error recovery.

### AI Insights Panel (Owner and Head Teacher Dashboard)

The AI Insights Panel appears in Zone 3 of the analytics dashboard — a fixed sidebar to the right of the trend charts. It is the primary surface for AI-generated alerts and recommendations.

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│ ✦ AI Insights                          [Refresh]    │
│ Updated 2 hours ago                                 │
├─────────────────────────────────────────────────────┤
│ 🔴 14 students at HIGH RISK this term               │
│    Top signal: attendance below 60%                 │
│    [View List]  [Contact Teachers]                  │
├─────────────────────────────────────────────────────┤
│ 🟡 23 parents may delay fees (from last term data)  │
│    Bursar has been notified                         │
│    [View Fee Risk Report]                           │
├─────────────────────────────────────────────────────┤
│ 🟢 Parent sentiment this term: 74% positive         │
│    Up from 62% last term                            │
│    [View Full Sentiment Report]                     │
└─────────────────────────────────────────────────────┘
```

**Rules:**
- Maximum 5 insights at a time, ranked by urgency (red first, then yellow, then green).
- Each insight has a reason line — never a bare number with no explanation.
- Each insight has one primary action button and one optional secondary.
- Timestamp: "Updated X hours ago." Insights older than 24 hours show a warning: "Data may be outdated — refresh to update."
- Skeleton loader visible within 500 ms of page load (AI-NFR-001). Full panel within 8 s.
- Traffic-light colours: 🔴 urgent (high risk, budget exhausted), 🟡 attention needed (medium risk, 80% budget), 🟢 positive signal.

### At-Risk Student List Screen

Accessible from "View List" on the AI Insights panel or from the Head Teacher navigation.

**Layout:** Full-width detail table (Zone 4 pattern).

| Student | Class | Risk | Attendance | Avg Mark | Last Login | Action |
|---|---|---|---|---|---|---|
| **Sandra Nakato** | S.4A | 🔴 High | 54% | 38% | 12 days ago | [Contact Teacher] |
| **Tom Okello** | S.3B | 🟡 Medium | 71% | 53% | 3 days ago | [Flag to Head Teacher] |

**Rules:**
- Default sort: risk level descending (high first).
- Exportable as CSV and PDF.
- "Contact Teacher" opens a pre-composed SMS/email draft to the class teacher — the teacher decides whether to send.
- No action is taken automatically. Every action is teacher-initiated.
- AI badge (✦) on the column header: "Risk level assessed by AI · Last updated Monday 06:00."

### Report Card Comment Review UI

Accessible from the class report card batch editing screen, after marks are finalised.

**Step 1 — Trigger:** Teacher clicks "✦ Generate AI Comments." A progress bar appears: "Generating comments for 40 students (0/40)..."

**Step 2 — Review:** Comments appear one by one as they are generated (streaming UX). Each comment card:
```
┌─────────────────────────────────────────────────────┐
│ Sandra Nakato — S.4A                                │
│ ─────────────────────────────────────────────────── │
│ Sandra has shown strong improvement in Mathematics  │
│ this term, achieving 78%. She should continue to    │
│ focus on her English composition skills.            │
│ ─────────────────────────────────────────────────── │
│ [✓ Accept]  [✎ Edit]  [✕ Reject]                   │
│ Confidence: High ●●●○○                              │
└─────────────────────────────────────────────────────┘
```

**Step 3 — Save:** "Save X Approved Comments" button appears only after the teacher has reviewed all comments. Unapproved comments are not saved.

**UX rules:**
- Teacher cannot click "Save All" without reviewing each comment individually (Hard Gate).
- Rejected comments do not disappear — they stay greyed out so the teacher can revisit.
- Confidence indicator: High (solid bar), Medium (half bar), Low (single bar + "Review carefully" note).
- If generation fails for a student: "AI could not generate a comment for this student. Write manually." The teacher is never blocked.

### AI Budget Display (School Owner Settings)

**Location:** Settings → AI Module → Usage and Budget.

```
AI Module — April 2026
─────────────────────────────────────────────────────
Plan: Growth     Budget: UGX 200,000/month

This month's usage:
████████████████░░░░  UGX 148,200 / 200,000  (74%)

[View per-feature breakdown]  [Increase Budget]

⚠ You will be notified when you reach 80% (UGX 160,000).
```

**Per-feature breakdown table:**

| Feature | Calls This Month | Cost (UGX) |
|---|---|---|
| At-risk student alert | 40 | 32,000 |
| Report card comments | 120 | 96,000 |
| Parent sentiment | 20 | 8,200 |
| Fee risk prediction | 17 | 12,000 |

**Rules:**
- Progress bar colour: green (< 60%), amber (60–80%), red (> 80%).
- At 80%: amber warning banner at top of the AI settings page.
- At 100%: red banner across the entire AI Module section: "AI features are paused for this month. Budget reset on 1 May."

### Loading States

Every AI-generated panel follows the progressive reveal pattern:

1. **Skeleton:** Grey placeholder boxes appear within 500 ms of page load.
2. **Streaming:** Content appears token by token as the LLM responds (where the feature supports it — report card comments).
3. **Complete:** Final content with action buttons.
4. **Error:** Friendly message with fallback action. Never expose technical error details to end users.

**Error messages by scenario:**

| Scenario | User-visible message |
|---|---|
| LLM API unavailable | "AI insights are temporarily unavailable. Check back in a few minutes." |
| Budget exhausted | "Your school's AI budget for this month has been reached. Contact your administrator." |
| AI module not activated | Feature is hidden entirely — no error shown. |
| Insufficient data | "Not enough data yet to generate this insight. Data will be available after 4 weeks of use." |
