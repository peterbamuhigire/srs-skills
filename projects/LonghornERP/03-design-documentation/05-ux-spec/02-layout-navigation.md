# Layout and Navigation Architecture

## 1. Three-Panel Application Structure

Longhorn ERP exposes three independent front-end panels, each with its own navigation structure, routing base, and access control layer. A single browser session is scoped to exactly one panel; cross-panel links open in a new tab.

| Panel | Base URL | Primary Users |
|---|---|---|
| Tenant Workspace | `/public/` | Tenant staff (all roles) |
| Super Admin Panel | `/public/superadmin/` | Chwezi Core platform administrators |
| Self-Service Portal | `/public/portal/` | Employees, cooperative farmers, customer contacts |

## 2. Tenant Workspace Layout

### 2.1 Three-Column Grid

The Tenant Workspace uses a fixed three-column layout:

| Column | Width (expanded) | Width (collapsed) | Behaviour |
|---|---|---|---|
| Left sidebar | 240 px | 64 px (icon-only) | Fixed position; does not scroll with content |
| Main content area | Fluid (fills remaining width) | Fluid | Scrollable; contains page header, content, and form footer |
| Right contextual panel | 320 px | Hidden (0 px) | Appears only on detail and complex form pages; toggled by a help icon in the top bar |

The sidebar collapses to icon-only mode via a toggle button at the bottom of the sidebar. The collapsed state persists in `localStorage` across sessions.

### 2.2 Sidebar Structure

```
[Tenant Logo / Name]
──────────────────────
[Module Group Label]
  ▸ Module Icon + Label
  ▸ Module Icon + Label
[Module Group Label]
  ▸ Module Icon + Label
──────────────────────
[Settings Icon]
[Help Icon]
[Collapse Toggle ◀]
```

Sidebar rendering rules:

- Module groups and individual modules render only when the authenticated user's role includes at least one permission within that module (module gate).
- Within a visible module, sub-navigation items (e.g., "Chart of Accounts" under "General Ledger") render only when the user holds the specific permission for that sub-item (permission gate).
- The active module is highlighted with a left-border accent in Accent Blue (#4472C4) and a background fill of #EFF6FF.
- Hovering over a collapsed (icon-only) sidebar item shows a tooltip with the module name.
- Maximum sidebar nesting depth: 2 levels (module group → module → sub-page). A third level is never introduced; sub-pages that require further grouping use tabs within the main content area.

### 2.3 Top Bar

The top bar is 56 px tall, fixed to the viewport top, and spans the full width of the main content area (does not overlap the sidebar).

| Zone | Contents |
|---|---|
| Left | Breadcrumb navigation (see Section 2.4) |
| Centre | Tenant name (bold) + active branch selector dropdown |
| Right | Notification bell (badge count), user avatar, user display name, dropdown chevron |

User avatar dropdown items:

- My Profile
- Change Password
- Switch Branch (if multi-branch tenant)
- Logout

The branch selector is visible only to tenants with more than 1 active branch. Selecting a branch reloads the current page scoped to the new branch context.

### 2.4 Breadcrumb Navigation

Breadcrumbs appear on all pages except the dashboard. They occupy the left zone of the top bar.

Format: `Module > Section > Record Name (or "New")`

Examples:

- `Accounts Receivable > Invoices > INV-2026-00123`
- `Human Resources > Payroll > New Payroll Run`
- `Inventory > Items > Maize Flour 2kg`

Rules:

- Every ancestor segment is a clickable link.
- The final (current page) segment is plain text, not a link.
- Breadcrumb segments truncate at 24 characters with an ellipsis if the record name is longer; the full name appears in a tooltip.
- Breadcrumbs do not appear on modal content — modals inherit the context of the page that launched them.

## 3. Responsive Breakpoints

| Breakpoint | Viewport Width | Layout Behaviour |
|---|---|---|
| Desktop (full) | ≥ 1280 px | Full 3-column layout; sidebar 240 px expanded |
| Desktop (compact) | 1024–1279 px | Sidebar defaults to collapsed (64 px icon-only); main content area fills remaining width |
| Tablet | 768–1023 px | Sidebar hidden by default; hamburger menu button in top bar toggles sidebar as an overlay panel |
| Mobile | < 768 px | Sidebar hidden; hamburger toggle; top bar shows only logo, hamburger, and user avatar; breadcrumb hidden |

On tablet and mobile, the sidebar overlay closes when the user taps outside it or navigates to a new page.

DataTables on mobile: columns are prioritised. Columns 1 (identifier), 2 (primary descriptor), and the Actions column are always visible. All other columns collapse and are accessible via a row-expand control (+).

## 4. Super Admin Panel Layout

The Super Admin Panel (`/public/superadmin/`) uses the same 3-column grid with a distinct colour scheme (dark navy sidebar, white top bar) to visually differentiate it from tenant workspaces. Navigation groups:

- Platform Overview (dashboard, health metrics)
- Tenant Management (create, suspend, configure tenants)
- Module Management (enable/disable modules per tenant)
- Billing & Subscriptions
- System Configuration (global settings, email templates, integrations)
- Audit Logs

The Super Admin Panel does not display tenant-specific data. Accessing tenant data requires a supervised "impersonate" action that logs a full audit trail.

## 5. Self-Service Portal Layout

The Self-Service Portal (`/public/portal/`) uses a simplified two-column layout: a narrow left navigation bar (180 px) and a main content area. The navigation bar contains only the sections relevant to the authenticated portal user's role:

| Portal Role | Available Sections |
|---|---|
| Employee | My Payslips, My Leave, My Profile |
| Farmer (Cooperative) | My Intake History, My Balance, My Deductions |
| Customer Contact | My Invoices, My Statements, Pay Now |

The portal top bar shows the host tenant's logo and name, the portal user's name, and a Logout button. There is no branch selector, module gate, or admin control in the portal.
