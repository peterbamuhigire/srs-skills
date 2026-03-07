# Wireframing Standards Reference

## Three Fidelity Levels

### Low Fidelity (Sketch / Structure)

**Purpose:** Explore layout options and information hierarchy rapidly. Low-fidelity wireframes prioritize speed over precision.

**When to Use:**
- Early ideation and concept exploration.
- Stakeholder alignment on page structure before investing in detailed design.
- Rapid iteration during design workshops.

**Characteristics:**
- Black and white or grayscale boxes and lines.
- Placeholder text ("Lorem ipsum" or descriptive labels like "[Hero Image]").
- No real content, no color, no imagery.
- Hand-drawn or rough digital sketches.

**Required Annotations:**
- Screen name and unique identifier.
- Primary user flow arrows between screens.
- Content block labels (e.g., "Navigation", "Main Content", "Sidebar", "Footer").
- Navigation targets and entry/exit points.

### Mid Fidelity (Layout / Content)

**Purpose:** Validate layout decisions, content placement, and basic interaction flows. Mid-fidelity wireframes introduce real content and proportional sizing.

**When to Use:**
- After low-fidelity concepts are approved.
- For usability testing of navigation and task flows.
- Developer alignment on component structure and data requirements.

**Characteristics:**
- Grayscale with typographic hierarchy (headings, body, captions).
- Actual or representative content (real labels, realistic data).
- Basic interactive elements (buttons, form fields, dropdowns) with correct sizing.
- No brand colors, final imagery, or visual polish.

**Required Annotations:**
- All low-fidelity annotations.
- Spacing values between major content blocks (in design tokens).
- Content hierarchy indicators (H1, H2, body, caption).
- Interaction triggers (click, hover, swipe) with destination references.
- Form field types (text, email, password, select, date, file upload).
- Data source references (which API endpoint or data object populates each element).

### High Fidelity (Visual / Interactive)

**Purpose:** Validate visual design, micro-interactions, and accessibility compliance. High-fidelity wireframes represent the final design intent.

**When to Use:**
- After mid-fidelity usability testing confirms the layout.
- For final stakeholder sign-off before development.
- As the source of truth for design handoff to developers.

**Characteristics:**
- Full color using design tokens.
- Real imagery, icons, and brand assets.
- Complete micro-interactions and transitions.
- Pixel-accurate spacing and typography.

**Required Annotations:**
- All mid-fidelity annotations.
- Color tokens for every colored element (e.g., `color-action-primary`, not `#3B82F6`).
- Typography tokens (font family, size token, weight, line height).
- Exact spacing using token names (e.g., `space-md` = 16px, not "16px").
- Animation timing (duration in ms, easing function).
- Accessibility notes (contrast ratio verification, ARIA role, keyboard behavior).
- Responsive behavior notes for each breakpoint.

## Responsive Design Breakpoints

### Mobile (320px -- 767px)

**Layout Rules:**
- Single-column layout for all content.
- Stacked navigation (hamburger menu or bottom tab bar).
- Touch targets shall be >= 44x44px (per WCAG 2.5.5).
- Form fields shall span full width.
- Tables shall transform to card-based or stacked layouts.
- Horizontal scrolling shall not be required for any content.

### Tablet (768px -- 1023px)

**Layout Rules:**
- Two-column layout where appropriate (list + detail, sidebar + content).
- Navigation may collapse to a slide-out drawer or remain as a compact sidebar.
- Touch targets shall be >= 44x44px.
- Tables may use horizontal scroll if columns exceed viewport, with a visible scroll indicator.
- Modal dialogs may expand to 80% viewport width.

### Desktop (1024px+)

**Layout Rules:**
- Multi-column layouts (up to 12-column grid).
- Persistent sidebar navigation.
- Hover states enabled for all interactive elements.
- Tables display in full tabular format with sortable headers.
- Maximum content width shall be constrained (typically 1280px or 1440px) to maintain readability.
- Keyboard shortcuts may be exposed in tooltips.

## Common Wireframe Patterns

### Dashboard Pattern

The system shall structure dashboards with:
- Summary metrics row (KPI cards) at the top.
- Primary chart or visualization in the main content area.
- Activity feed or recent items in a sidebar or secondary panel.
- Quick-action buttons for the most common tasks.

### CRUD List/Detail Pattern

The system shall structure list-detail views with:
- Filterable, sortable data table with pagination controls.
- Search bar with advanced filter toggle.
- Bulk action toolbar (appears when items are selected).
- Row-click or dedicated button navigates to detail view.
- Detail view shows all fields with contextual actions (edit, delete, archive).

### Form Wizard Pattern

The system shall structure multi-step forms with:
- Step indicator showing current position and total steps.
- One logical group of fields per step.
- Back and Next navigation with validation gating (the system shall prevent advancement until current step validates).
- Summary/review step before final submission.
- Save-as-draft capability for long forms.

### Settings Pattern

The system shall structure settings pages with:
- Category navigation (sidebar or tabs).
- Grouped settings with section headers and descriptions.
- Inline editing or save-per-section (not a single global save for the entire page).
- Dangerous actions (delete account, reset data) visually separated with confirmation dialogs.
