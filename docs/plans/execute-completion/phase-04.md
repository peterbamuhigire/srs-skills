# Phase 4: Web Application Stack

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Complete the web application development capability by writing a comprehensive
`webapp-gui-design` skill — the only remaining gap in a strong modern web stack.

**Architecture:** The web stack is already expert-grade across React, Next.js, TypeScript,
Tailwind, Node.js, and PHP. The single gap is `webapp-gui-design` (currently 27 lines),
which needs to become a comprehensive SaaS UI component architecture reference.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Build production SaaS web applications end-to-end using the React/Next.js/TypeScript stack
- Reference a complete component architecture guide for SaaS dashboards, forms, and data tables
- Apply consistent UI patterns across all Chwezi Core Systems products
- Implement secure, performant full-stack web applications with Node.js or PHP backends
- Design and build REST and GraphQL APIs with proper auth, pagination, and error handling
- Deliver web applications that perform at P95 ≤ 200 ms for server-rendered pages
- Apply RBAC with dual-mode auth (session + JWT) across multi-tenant applications

---

## Current Strengths — Skills Already Built

### React / Next.js Frontend
- `react-development` — React 19 fundamentals, hooks, component patterns, React Query
- `react-patterns` — Advanced patterns: compound components, render props, HOCs, portals
- `nextjs-app-router` — Next.js 15 App Router: RSC, server actions, streaming, metadata
- `typescript-mastery` — TypeScript 5: generics, utility types, template literals, narrowing
- `typescript-design-patterns` — Design patterns in TypeScript: Factory, Strategy, Observer, DI
- `tailwind-css` — Tailwind CSS 4: utility classes, design tokens, dark mode, responsive
- `frontend-performance` — Core Web Vitals, code splitting, lazy loading, image optimisation
- `responsive-design` — Mobile-first layout, breakpoints, container queries
- `webapp-gui-design` — **STUB — 27 lines, must complete this phase**

### Backend
- `nodejs-development` — Node.js: Fastify, Prisma ORM, BullMQ, async patterns, streams, security
- `php-modern-standards` — PHP 8.2: named arguments, fibers, enums, match, attributes
- `php-security` — PHP security: prepared statements, output escaping, CSRF, session hardening
- `php-vs-nextjs` — When to use PHP vs Next.js — technology selection framework
- `javascript-advanced` — ES2024: generators, proxies, Symbol, WeakRef, async iterators
- `javascript-modern` — Modern JS: optional chaining, nullish coalescing, logical assignment
- `javascript-patterns` — Module pattern, observer, command, mediator, strategy
- `javascript-php-integration` — JS + PHP integration: AJAX, Fetch API, CORS, shared auth

### Auth, Security & APIs
- `dual-auth-rbac` — Session + JWT dual auth, role-based access control, permission gates
- `web-app-security-audit` — OWASP Top 10, XSS, CSRF, SQL injection, security headers
- `graphql-security` — GraphQL-specific attacks, depth limiting, rate limiting, field masking
- `api-design-first` — OpenAPI 3.1 schema-first design, versioning, contract testing
- `api-error-handling` — RFC 7807 Problem Details, error taxonomy, client-side retry
- `api-pagination` — Cursor, offset, keyset pagination — when to use which
- `api-testing-verification` — Contract testing, Postman/Newman, API test strategy

### Data Visualization & UI Utilities
- `data-visualization` — Chart patterns, dashboard layout, aggregation for charts
- `report-print-pdf` — PDF generation from web, print stylesheets, report design

---

## Build Tasks

### Task 1: Complete `webapp-gui-design` stub

**File to modify:** `C:\Users\Peter\.claude\skills\webapp-gui-design\SKILL.md`

**Current state:** 27 lines — effectively empty.

**Read first:**
- `react-development`, `nextjs-app-router`, `tailwind-css` skills (already built)
- *Atomic Design* (Brad Frost — free at atomicdesign.bradfrost.com)
- Shadcn/ui documentation — `ui.shadcn.com` (component patterns reference)
- TanStack Table documentation — `tanstack.com/table`

**Content outline for SKILL.md (target: 380–460 lines):**

1. **SaaS Application Shell** — sidebar navigation, topbar, breadcrumbs, content area layout
2. **Navigation Patterns** — collapsible sidebar, mobile hamburger, active state, nested menus
3. **Dashboard Layout** — KPI card grid, chart area, recent activity feed, responsive breakpoints
4. **Data Table Architecture** — TanStack Table setup, column definition, sorting, filtering, pagination
5. **Form Architecture** — React Hook Form + Zod validation, field components, error display, async submit
6. **Modal & Drawer Patterns** — controlled modals, confirmation dialogs, slide-over drawers
7. **Loading States** — skeleton screens, spinner placement, optimistic updates, suspense boundaries
8. **Error Boundaries** — React error boundary, fallback UI, error reporting to Sentry
9. **Toast Notifications** — Sonner / react-hot-toast setup, success/error/loading variants
10. **Authentication Flow UI** — login page, register page, forgot password, 2FA input, redirect logic
11. **Multi-Tenant Switcher** — workspace/tenant selector, context persistence, URL namespacing
12. **Dark Mode** — Tailwind dark class strategy, CSS variables for theme, persistence in localStorage
13. **File Upload Patterns** — drag-and-drop upload zone, progress indicator, preview, cancellation
14. **Empty State Design** — empty list, first-use onboarding, zero-data dashboard patterns
15. **Accessibility** — keyboard navigation, ARIA attributes, focus management, colour contrast ≥ 4.5:1

**Step 1:** Read the four source materials listed above.
**Step 2:** Rewrite `webapp-gui-design/SKILL.md` using the content outline above.
**Step 3:** Include at least one concrete Tailwind + React code snippet per section.
**Step 4:** Run `wc -l SKILL.md` — confirm 350–500 lines.
**Step 5:** Commit: `feat(skills): complete webapp-gui-design stub — SaaS component architecture`

---

## Phase Completion Checklist

- [ ] `webapp-gui-design` has been completely rewritten — minimum 350 lines
- [ ] All 15 sections in the content outline are present
- [ ] Every section has at least one code example (Tailwind + React/TypeScript)
- [ ] `webapp-gui-design` cross-references `react-development`, `nextjs-app-router`, `tailwind-css`
- [ ] No skill file exceeds 500 lines
- [ ] Git commit made: `feat(skills): complete phase-4 — web application stack`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Node.js Design Patterns* (3rd ed.) | Casciaro & Mammino | Packt | ~$45 | Advanced Node.js patterns: streams, design patterns, scaling — deepens `nodejs-development` skill |
| 2 | *You Don't Know JS* series | Kyle Simpson | O'Reilly | ~$40 | JavaScript internals: scope, closures, async, prototypes — foundational for all web work |
| 3 | *Full Stack React, TypeScript, and Node* | David Choi | Packt | ~$40 | End-to-end TypeScript full-stack — React + Node.js integration patterns |
| 4 | *Learning PHP, MySQL & JavaScript* (6th ed.) | Robin Nixon | O'Reilly | ~$55 | PHP + MySQL + JS integration — deepens `javascript-php-integration` skill |

### Free Resources

- TypeScript Handbook — `typescriptlang.org/docs/handbook` — authoritative TypeScript reference
- Next.js documentation — `nextjs.org/docs` — App Router patterns, server actions, caching
- TanStack Table documentation — `tanstack.com/table/latest` — data table implementation
- React Hook Form documentation — `react-hook-form.com` — form management
- Zod documentation — `zod.dev` — TypeScript schema validation
- Shadcn/ui — `ui.shadcn.com` — copy-paste React component patterns for SaaS
- Atomic Design — `atomicdesign.bradfrost.com` — free book on component hierarchy
- Tailwind CSS documentation — `tailwindcss.com/docs` — utility class reference

---

*Next phase: [Phase 5 — Mobile Application Stack](phase-05.md)*
