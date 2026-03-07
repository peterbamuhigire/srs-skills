---
name: ux-specification
description: Generate a comprehensive UX specification document covering information architecture, wireframing standards, design system documentation, usability testing protocols, and design handoff specs per ISO 9241-210 and ISO 25010.
---

# UX Specification Skill

## Overview

Produces a complete UX specification document that bridges user research insights and engineering implementation. The output includes information architecture diagrams (Mermaid flowcharts), wireframing standards across three fidelity levels, design system token definitions, usability testing protocols with quantitative metrics, and developer-ready design handoff specifications. This skill draws on ISO 9241-210 (Human-centred design for interactive systems), ISO 25010 (Systems and software quality models), and principles from "The Effective Product Designer" and "Design for How People Think" (John Whalen).

## When to Use

- After `HLD.md` exists in `../output/` and identifies user-facing components.
- SRS or user stories define user interactions and interface expectations.
- `vision.md` and `features.md` in `../project_context/` provide product scope and feature inventory.
- `stakeholder_register.md` in `../project_context/` identifies user personas and audience segments.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../output/SRS_Draft.md` or `../project_context/user_stories.md`, `../output/HLD.md`, `../project_context/vision.md`, `../project_context/features.md`, `../project_context/stakeholder_register.md` |
| **Outputs** | `../output/UX_Specification.md` |
| **Tone**    | Precise, user-centred, standards-grounded |
| **Standard** | ISO 9241-210:2019, ISO 25010:2011, WCAG 2.1 AA |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| SRS_Draft.md | `../output/SRS_Draft.md` | Preferred | Functional requirements, user interaction flows, data objects |
| user_stories.md | `../project_context/user_stories.md` | Alternate | User stories when SRS is not yet available |
| HLD.md | `../output/HLD.md` | Yes | Architectural context, component hierarchy, data flow paths |
| vision.md | `../project_context/vision.md` | Yes | Product scope, target audience, business goals |
| features.md | `../project_context/features.md` | Recommended | Feature inventory for information architecture mapping |
| stakeholder_register.md | `../project_context/stakeholder_register.md` | Recommended | User personas, audience segments, accessibility needs |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| UX_Specification.md | `../output/UX_Specification.md` | Complete UX specification with all sections |

## Core Instructions

Follow these eight steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `SRS_Draft.md` and `HLD.md` from `../output/`. Read `vision.md`, `features.md`, `stakeholder_register.md`, and `user_stories.md` from `../project_context/`. Log the absolute path of each file read. If `SRS_Draft.md` is missing, fall back to `user_stories.md`. If both are missing, halt execution and report the gap. If `HLD.md` or `vision.md` is missing, halt execution and report the gap. If `features.md` or `stakeholder_register.md` is missing, log a warning and proceed with available data.

### Step 2: Generate Information Architecture

The system shall produce the following information architecture artifacts:

1. **Site Map** -- Generate a Mermaid flowchart (`graph TD`) representing the full page/screen hierarchy. Each node shall represent a distinct screen or content group. Use top-down decomposition: start from the application shell, then primary navigation targets, then secondary views.

2. **Content Inventory Table** -- Enumerate every content element:

   | Page/Screen | Content Type | Owner | Status | Priority |
   |-------------|-------------|-------|--------|----------|

3. **Navigation Model** -- Define navigation types present in the application:
   - **Global Navigation:** Persistent across all screens (e.g., top bar, sidebar).
   - **Local Navigation:** Context-specific within a section.
   - **Contextual Navigation:** In-content links and related items.
   - **Utility Navigation:** Account, settings, help, logout.
   - **Breadcrumb Navigation:** Hierarchical path indicator.

4. **Card Sorting Results Template** -- Provide a template for recording card sorting sessions (open or closed) with columns for Card Label, User-Assigned Category, Frequency, and Confidence Score.

See `references/information-architecture.md` for construction techniques and methodology.

### Step 3: Define Wireframe Standards

The system shall define three fidelity levels with explicit scope boundaries:

| Level | Purpose | Content | Tools |
|-------|---------|---------|-------|
| **Low Fidelity** | Structure and layout exploration | Boxes, labels, placeholder text, no color | Paper, whiteboard, Balsamiq |
| **Mid Fidelity** | Layout validation and content placement | Actual content, grayscale, basic interactions | Figma (wireframe mode), Axure |
| **High Fidelity** | Visual design and interaction validation | Full color, real assets, micro-interactions | Figma (design mode), Sketch |

**Required Annotations per Level:**
- Low: Screen name, primary user flow, content blocks, navigation targets.
- Mid: All low-fidelity annotations plus spacing values, content hierarchy, interaction triggers, form field types.
- High: All mid-fidelity annotations plus color tokens, typography tokens, exact spacing (in design tokens), animation timing, accessibility notes.

**Responsive Breakpoints:**
- Mobile: 320px -- 767px (single column, stacked layout, touch targets >= 44px).
- Tablet: 768px -- 1023px (adaptive columns, collapsible navigation).
- Desktop: 1024px+ (multi-column, expanded navigation, hover states).

See `references/wireframing-standards.md` for patterns and examples.

### Step 4: Generate Design System Foundation

The system shall produce design system documentation with three layers:

**4.1 Design Tokens**

- **Color Tokens:** Primitives (palette values) -> Semantic (e.g., `color-action-primary`, `color-feedback-error`) -> Component-level (e.g., `button-primary-bg`).
- **Typography Scale:** Font families, size scale (using a modular scale ratio), line heights, font weights, and letter spacing per usage context (heading, body, caption, code).
- **Spacing Scale:** Base unit of 4px. Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96px. Each value shall have a named token (e.g., `space-xs`, `space-sm`, `space-md`).
- **Elevation/Shadow Levels:** Define shadow levels (0-5) with CSS box-shadow values and usage context (e.g., level-1 for cards, level-3 for modals).

**4.2 Component Library Catalog**

For each UI component, document:

| Property | Description |
|----------|-------------|
| Name | Component identifier (PascalCase) |
| Description | One-sentence purpose statement |
| Variants | Visual/behavioral variations (e.g., primary, secondary, destructive) |
| States | Interactive states (default, hover, focus, active, disabled, loading, error) |
| Props | Configurable properties with types and defaults |
| Usage Guidelines | When to use and when not to use |
| Accessibility | ARIA roles, keyboard behavior, screen reader announcements |

**4.3 Pattern Library**

- **Layout Patterns:** Dashboard, list-detail, master-detail, split view, full-screen modal.
- **Form Patterns:** Single-page form, multi-step wizard, inline editing, search with filters.
- **Navigation Patterns:** Sidebar, top bar, tab bar, breadcrumb, mega menu.
- **Data Display Patterns:** Data table, card grid, timeline, tree view, chart dashboard.

See `references/design-system-guide.md` for token taxonomy and documentation templates.

### Step 5: Define Interaction Specifications

The system shall define interaction behaviors for:

1. **Micro-interactions:** Button press feedback, toggle animations, form field focus transitions, notification entry/exit.
2. **Page Transitions:** Navigation transitions (slide, fade, none), modal open/close, drawer expand/collapse.
3. **Loading States:** Skeleton screens (preferred over spinners for content areas), progress indicators (determinate for uploads, indeterminate for fetches), optimistic UI updates.
4. **Error States:** Inline field validation (on blur), form-level error summary, toast notifications (auto-dismiss after 5s for info, persist for errors), empty states with actionable guidance, offline/connectivity loss handling.

Each interaction shall specify: trigger, animation duration (in ms), easing function, and fallback for reduced-motion preferences per `prefers-reduced-motion` media query.

### Step 6: Define Accessibility Requirements

The system shall enforce WCAG 2.1 Level AA compliance:

| Criterion | Requirement | Verification Method |
|-----------|-------------|---------------------|
| Color Contrast | Text contrast ratio >= 4.5:1 (normal text), >= 3:1 (large text) | Automated contrast checker |
| Keyboard Navigation | All interactive elements shall be reachable via Tab, operable via Enter/Space, dismissible via Escape | Manual keyboard walkthrough |
| Screen Reader | All images shall have alt text, all form fields shall have associated labels, dynamic content shall use ARIA live regions | Screen reader testing (NVDA, VoiceOver) |
| Focus Management | Visible focus indicator on all interactive elements, logical tab order, focus trap in modals | Manual inspection |
| Touch Targets | Minimum 44x44px touch target size on mobile | Design review |
| Motion | The system shall respect `prefers-reduced-motion` and provide static alternatives | CSS media query audit |

### Step 7: Create Usability Testing Protocol

The system shall define a usability testing framework:

**7.1 Test Planning Template**
- Objectives: What hypotheses does this test validate?
- Participants: Minimum 5 per user segment (per Nielsen Norman Group recommendation).
- Environment: Moderated remote, unmoderated remote, or in-person lab.

**7.2 Task Scenario Template**
- Task scenarios shall be realistic, goal-oriented, and free of leading language.
- Format: "You are [context]. You want to [goal]. Using the application, [action]."

**7.3 Success Metrics**

| Metric | Target | Measurement |
|--------|--------|-------------|
| Task Completion Rate | >= 85% | Binary pass/fail per task per participant |
| Time on Task | Varies by complexity | Stopwatch from task start to completion |
| Error Rate | <= 2 errors per task | Count of incorrect actions or missteps |
| SUS Score | >= 68 (above average) | Post-test System Usability Scale questionnaire |

**7.4 Observation Recording Format**

| Task | Participant | Time (s) | Errors | Path Taken | Quotes | Severity |
|------|-------------|----------|--------|------------|--------|----------|

**7.5 Findings-to-Requirements Feedback Loop**
- Each finding shall be classified by severity (Critical, Major, Minor, Cosmetic).
- Critical and Major findings shall generate new or revised requirements traceable to SRS Section 3.2.
- The system shall maintain a findings register mapping each observation to a requirement ID.

See `references/usability-testing.md` for the SUS questionnaire and scoring methodology.

### Step 8: Generate Design Handoff Checklist

The system shall produce developer-ready handoff specifications:

**8.1 Annotation Standards**
- Spacing values shall reference design tokens, not raw pixel values.
- Colors shall reference semantic tokens (e.g., `color-action-primary`), not hex codes.
- Interaction states shall be documented for every interactive component (default, hover, focus, active, disabled).
- Responsive behavior shall specify layout changes at each breakpoint.

**8.2 Asset Delivery Checklist**

| Asset Type | Format | Naming Convention | Resolution |
|------------|--------|-------------------|------------|
| Icons | SVG | `icon-{name}-{size}.svg` | Vector |
| Illustrations | SVG + PNG fallback | `illustration-{name}.svg` | 1x, 2x |
| Photos | WebP + JPEG fallback | `photo-{context}-{id}.webp` | 1x, 2x, 3x |
| Logos | SVG | `logo-{variant}.svg` | Vector |

**8.3 Implementation Acceptance Criteria**
- The implemented component shall match the design specification within 2px tolerance.
- All design tokens shall be consumed from the shared token system, not hard-coded.
- Responsive layouts shall function correctly at all three breakpoint ranges.
- All WCAG 2.1 AA criteria defined in Step 6 shall pass automated and manual testing.
- Interaction timing shall match specification within 50ms tolerance.

## Output Format

The generated `UX_Specification.md` shall use this section structure with a Document Header (Date, Version, Authors, Standard), followed by eight sections:

1. **Information Architecture** -- Site map (Mermaid flowchart), content inventory, navigation model, card sorting template
2. **Wireframe Standards** -- Fidelity levels, annotation requirements, responsive breakpoints
3. **Design System** -- Design tokens (color, typography, spacing, elevation), component catalog, pattern library
4. **Interaction Specifications** -- Micro-interactions, transitions, loading states, error states
5. **Accessibility Requirements** -- WCAG 2.1 AA criteria with verification methods
6. **Usability Testing Protocol** -- Task scenarios, success metrics, observation format, feedback loop
7. **Design Handoff** -- Annotation standards, asset delivery, acceptance criteria
8. **Traceability Matrix** -- Screen/Component mapped to SRS Section/Requirement IDs

## Cross-References

For cognitive evaluation of designs (mental models, attention patterns, emotional response, memory load), reference `skills/cognitive-ux-framework/`.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Using raw pixel values instead of tokens | The system shall reference named design tokens for all spacing, color, and typography values |
| Missing accessibility annotations | Every interactive component shall include ARIA roles, keyboard behavior, and contrast verification |
| Wireframes without responsive variants | Each wireframe shall show mobile, tablet, and desktop adaptations |
| Usability test tasks with leading language | Task scenarios shall describe goals without hinting at the solution path |
| Design handoff without interaction states | Every component shall document default, hover, focus, active, and disabled states |
| No feedback loop from testing to requirements | Usability findings rated Critical or Major shall generate traceable requirement updates |

## Verification Checklist

- [ ] `UX_Specification.md` exists in `../output/`.
- [ ] Site map renders correctly in Mermaid flowchart syntax.
- [ ] All three wireframe fidelity levels are defined with annotation requirements.
- [ ] Design tokens cover color, typography, spacing, and elevation.
- [ ] Component catalog entries include all required properties (name, variants, states, props, accessibility).
- [ ] WCAG 2.1 AA criteria are specified with verification methods.
- [ ] Usability testing protocol defines quantitative success metrics.
- [ ] Design handoff uses token references, not raw values.
- [ ] Traceability matrix links every screen/component to SRS requirements.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 01-high-level-design | Consumes `HLD.md` for component hierarchy and data flow |
| Upstream | Phase 02 (Requirements) | Consumes SRS or user stories for functional context |
| Downstream | Phase 04 (Development) | Provides component specs, tokens, and acceptance criteria for front-end implementation |
| Downstream | Phase 05 (Testing) | Provides usability test protocols and accessibility verification criteria |
| Cross-Ref | `skills/cognitive-ux-framework/` | Cognitive evaluation methodology for design decisions |

## Standards

- **ISO 9241-210:2019** -- Human-centred design for interactive systems: iterative design process, user research, usability evaluation
- **ISO 25010:2011** -- Systems and software quality models: usability characteristics (learnability, operability, error protection, accessibility, user interface aesthetics)
- **WCAG 2.1 Level AA** -- Web Content Accessibility Guidelines: perceivable, operable, understandable, robust
- **IEEE 830-1998** -- Requirement traceability for UX-to-requirement mapping

## Resources

- `references/information-architecture.md` -- Site map construction and navigation model reference.
- `references/wireframing-standards.md` -- Fidelity levels, annotation rules, and common patterns.
- `references/design-system-guide.md` -- Token taxonomy, component documentation template, pattern library.
- `references/usability-testing.md` -- Test planning, SUS questionnaire, observation format.
- `references/design-handoff.md` -- Annotation standards, asset delivery, acceptance criteria.
- `README.md` -- Quick-start guide for this skill.
