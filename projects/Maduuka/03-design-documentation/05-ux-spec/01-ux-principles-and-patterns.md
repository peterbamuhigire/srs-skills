---
project: Maduuka
document: UX Specification — Principles and Global Patterns
version: 1.0
date: 2026-04-05
author: Peter Bamuhigire · Chwezi Core Systems
status: Draft
---

# UX Specification: Principles and Global Patterns

## 1. UX Philosophy

Maduuka's interface is designed for Agnes — a shopkeeper who can use WhatsApp but has never opened accounting software. Every screen is evaluated against one question: can a new user complete this task in under 3 minutes without reading a manual? DC-002 (zero mandatory training) eliminates instructional text, wizards, and jargon; the interface teaches itself through placement, affordance, and immediate feedback. DC-004 (cheapest phone) enforces hard constraints: no animations that require GPU compositing, no list rendering that causes jank on 2 GB RAM devices, and no screen that requires a display wider than 360 dp to be usable. These two constraints together produce an interface that is simple not by accident but by discipline — every added element must justify its presence against the cost it imposes on the least capable user and device.

## 2. Global Design Patterns

### 2.1 Navigation

**Android — Bottom Tab Bar**

The bottom navigation bar contains exactly 5 tabs, fixed and always visible:

1. Dashboard
2. POS
3. Inventory
4. Reports
5. More (overflow: Customers, Suppliers, HR, Settings, Help)

The active tab uses the brand primary colour fill on its icon. Inactive tabs use a mid-grey icon (#9E9E9E). Labels are always visible below icons — no icon-only tabs. The tab bar height is 56 dp. The POS tab carries a distinct action-button visual treatment (filled circle, brand colour) to signal its primacy.

**Web — Sidebar Drawer**

The web application uses the Tabler admin sidebar layout. On viewports wider than 992 px, the sidebar is fixed and 240 px wide. On viewports narrower than 992 px, the sidebar collapses to a hamburger-triggered full-screen overlay. The sidebar groups navigation items under labelled sections: POS, Inventory, Customers, Suppliers, Finance, HR, Reports, Settings. Active items use a left-border accent (4 px, brand primary colour) and a light-fill background.

### 2.2 Typography and Touch Targets

All interactive elements on Android shall have a minimum tap target of 48 x 48 dp regardless of the visual size of the element. Padding is added around small icons to meet this minimum. On web, the minimum click target is 44 x 44 px.

Type hierarchy:

- Screen title: 20 sp, medium weight, single line
- Section header: 16 sp, medium weight
- Body / list item primary text: 14 sp, regular weight
- Secondary / caption: 12 sp, regular weight, secondary colour
- Input labels: 12 sp, medium weight, placed above the field (not as floating labels — floating labels are prohibited due to context-loss on low-literacy users)

All body text shall achieve a contrast ratio of at least 4.5:1 against its background (WCAG AA). Secondary text shall achieve at minimum 3:1 contrast.

### 2.3 Error States

Error communication rules:

- Errors are inline — displayed directly beneath the field or action that caused them.
- Error messages are specific and actionable: "Phone number must be 10 digits starting with 07" not "Invalid input."
- Modal dialogs are never used for recoverable errors.
- Error text colour: #D32F2F (red 700). An error icon (filled circle with exclamation, 16 dp) precedes the message.
- Form submission is blocked and the first erroneous field is scrolled into view and focused automatically.
- Network errors (API failure) display a non-blocking snackbar (Android) or toast notification (Web) with a Retry action button.

### 2.4 Empty States

Every list or data view that can be empty shall display:

- A centred icon (48 dp on mobile, 64 px on web) representing the empty entity (e.g., shopping cart outline for an empty cart).
- A single sentence explaining why the view is empty: "No products found. Try a different search term."
- A primary action button that resolves the emptiness: "Add First Product" or "Clear Filter."

Empty state text never says "No data available." That phrase is prohibited.

### 2.5 Offline Indicator

A persistent amber banner (height: 28 dp / px) shall appear at the top of every screen when the device has no internet connectivity. Banner text: "Offline — changes will sync when reconnected." The banner does not block any interaction. POS operations, stock viewing, and basic reports continue to function in offline mode. The banner is dismissed automatically when connectivity is restored — no user action required.

### 2.6 Loading States

- Lists and data-heavy screens use skeleton screens (animated shimmer placeholders matching the shape of the content rows) while data loads.
- Individual actions (saving a form, processing a payment) use a centred circular spinner overlaid on the triggered button. The button is disabled and shows a spinner in place of its label.
- Spinner-only loading is used only for actions expected to complete in under 2 seconds. Actions expected to take longer use a progress indicator with a status label: "Processing payment…"
- The maximum acceptable wait before showing a loading indicator is 200 ms.

### 2.7 Confirmation Dialogs

Confirmation dialogs are shown only for destructive or irreversible actions. Criteria:

- Voiding a completed sale
- Deleting a product record
- Closing a POS session (reconciliation trigger)
- Approving payroll (locked after approval)
- Revoking a connected device

Confirmation dialog structure: title (imperative statement of the action: "Void This Sale?"), a single sentence of consequence ("This cannot be undone. The receipt gap will be flagged."), a Cancel button (secondary style), and a Confirm button (destructive red fill: #D32F2F).

All other actions — including editing, soft-filtering, and navigating away from unsaved forms — do not trigger a confirmation dialog. Instead, unsaved-form navigation shows a bottom sheet (Android) or browser-native "Leave page?" prompt (Web).

### 2.8 Colour Convention

Colour is used consistently as a semantic signal across all screens:

| Colour | Hex | Semantic Meaning |
|---|---|---|
| Green | #388E3C | Completed, paid, in stock, positive variance |
| Amber | #F57C00 | Pending, low stock, warning, partial |
| Red | #D32F2F | Error, void, critical alert, out of stock |
| Blue | #1976D2 | Brand primary, interactive elements, links |
| Grey | #757575 | Disabled, inactive, secondary text |

Status badges (pills) use a light-fill variant: 10% opacity background of the semantic colour, full-opacity text of the same colour. Example: a "Pending" badge has an amber background at 10% and amber text.

## 3. Android-Specific Patterns

### 3.1 Jetpack Compose Conventions

- All screens are composed as stateless composables receiving state via `ViewModel` and `StateFlow`.
- `LazyColumn` is used for all scrollable lists. `RecyclerView` is not used in new screens.
- Recomposition scope is minimised by lifting state to the narrowest common ancestor.
- `remember` and `derivedStateOf` are used to prevent unnecessary recomposition on high-frequency state (e.g., cart total updating on quantity change).

### 3.2 Back Gesture

The Android predictive back gesture is supported. Screens that have unsaved changes intercept the back gesture and show a bottom sheet with: "Discard Changes?" / "Keep Editing" / "Discard." Screens with no unsaved changes allow back navigation immediately without interception.

### 3.3 Bottom Sheet for Secondary Actions

Secondary actions on list items are exposed via a `ModalBottomSheet` triggered by a long-press or a trailing vertical-dots icon. The bottom sheet lists actions as full-width rows with an icon and label. This pattern replaces context menus and right-click menus on Android.

### 3.4 Full-Screen POS Mode

In POS mode, the status bar is hidden and the navigation bar (Android system) is hidden using `WindowInsetsController`. The bottom tab bar is also hidden. The POS UI occupies the full display area edge-to-edge.

### 3.5 Adaptive Layout

On phones (< 600 dp width): single-column layout. On tablets (≥ 600 dp): two-pane layout where applicable (e.g., product list on left, product detail on right in Inventory). The POS module uses a 3-column product grid on phones and a 5-column grid on 7-inch tablets.

## 4. Web-Specific Patterns

### 4.1 Tabler Admin Layout

The web application uses Tabler UI as its component library on top of Bootstrap 5. The root layout consists of:

- Fixed sidebar (240 px) on desktop.
- Top navbar (60 px) with: business name, branch switcher, notifications bell, user avatar menu.
- Content area filling the remaining viewport with 24 px padding on desktop, 16 px on mobile.
- Footer (32 px) showing version, support link, and EFRIS status indicator.

### 4.2 Data Tables

All list views on web use `DataTables`-compatible tabular layout with:

- Column-level sort (click column header; toggle ascending/descending; sort indicator arrow).
- Inline search/filter bar above the table.
- Pagination: 25 rows per page default; configurable to 50 or 100.
- Row-level action buttons: View (eye icon), Edit (pencil icon), Delete/Void (trash/x icon in red).
- Bulk-action checkbox column for multi-row operations (export, delete, approve).
- Responsive collapse: on narrow viewports, rightmost columns collapse into a row-detail toggle.

### 4.3 Modal Dialogs for Forms

Short forms (≤ 6 fields) are presented in a modal dialog rather than a full page navigation. The modal has a fixed header (title + close icon), a scrollable body, and a sticky footer (Cancel + primary action buttons). The modal is dismissed by the close icon, the Cancel button, or the Escape key. Clicking the backdrop does not dismiss the modal (prevents accidental data loss).

### 4.4 Keyboard Shortcuts (POS Mode)

| Shortcut | Action |
|---|---|
| `F2` | Focus product search field |
| `F4` | Open payment screen |
| `F6` | Hold current cart |
| `F8` | Open resume cart list |
| `Esc` | Cancel current modal or bottom sheet |
| `Enter` (on cart item) | Increment quantity by 1 |
| `Delete` (on cart item) | Remove item from cart |

Keyboard shortcuts are documented in a persistent tooltip accessible from the POS screen help icon.

### 4.5 Report and Export Actions

Every data table and report view includes an action bar above the table with:

- Export CSV button.
- Export PDF button.
- Print button (triggers browser print dialog with print-optimised CSS).
- Date range picker (presets: Today, This Week, This Month, Last Month, Custom).

## 5. Accessibility Baseline

- **Contrast ratio:** All body text shall achieve a minimum 4.5:1 contrast ratio against its background. Large text (≥ 18 sp / 24 px) shall achieve a minimum 3:1 contrast ratio. UI components and graphical elements shall achieve a minimum 3:1 contrast ratio.
- **Tap target size:** Minimum 48 x 48 dp on Android. Minimum 44 x 44 px on web.
- **Text scaling:** All layouts shall remain usable at Android system font scale 1.3x. Text shall not be clipped or overlap other elements at 1.3x scale. Font sizes are defined in `sp` (not `dp`) to respect system font scale.
- **Screen reader labels:** Every icon-only button shall have a `contentDescription` (Android) or `aria-label` (web) describing its action.
- **Focus indicators:** Web interactive elements shall have a visible focus ring (2 px, brand blue, 2 px offset) when focused via keyboard. The default browser focus ring is not suppressed without a replacement.
- **Error identification:** Form errors shall be associated with their field via `aria-describedby` (web) or `semantics(error = true)` (Compose) so screen readers announce the error when the field is focused.
