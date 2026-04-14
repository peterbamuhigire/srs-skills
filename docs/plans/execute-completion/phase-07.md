# Phase 7: Quality Engineering & Test Automation

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Close the two remaining testing gaps — end-to-end browser automation (Playwright)
and offline-first Progressive Web Apps — completing a full-spectrum quality engineering
capability that covers unit, integration, E2E, and offline scenarios.

**Architecture:** Two new skills built from free documentation. The existing testing skills
already cover unit and integration testing across all platforms. This phase adds the
outer ring of the testing pyramid: E2E browser tests and PWA offline resilience testing.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Write end-to-end browser tests with Playwright using the Page Object Model
- Integrate E2E tests into CI/CD pipelines (GitHub Actions) with parallel execution
- Run visual regression tests to detect unintended UI changes between deployments
- Test authentication flows, multi-step forms, and API interactions end-to-end
- Build Progressive Web Apps that work offline in East Africa's variable connectivity
- Implement Service Worker caching strategies (NetworkFirst, CacheFirst, StaleWhileRevalidate)
- Persist structured data offline with IndexedDB (Dexie.js) and sync when reconnected
- Test PWAs with Lighthouse for performance, accessibility, and installability scores
- Deliver software with measurable quality gates: coverage thresholds, E2E pass rate ≥ 99%

---

## Current Strengths — Testing Skills Already Built

### Test Strategy & Architecture
- `advanced-testing-strategy` — Testing pyramid, test taxonomy, quality gates, coverage strategy
- `sdlc-testing` — Test plan authoring, UAT coordination, defect lifecycle, sign-off process

### Platform-Specific Testing
- `ios-tdd` — XCTest, snapshot testing, async test patterns, Xcode test navigator
- `android-tdd` — JUnit5, MockK, Robolectric, Espresso, Hilt testing, Flow testing
- `kmp-tdd` — Shared test code, platform-specific mocks, coroutines test dispatcher
- `api-testing-verification` — Contract testing, Postman/Newman automation, API test strategy

---

## Build Tasks

### Task 1: Create `e2e-testing` skill

**File to create:** `C:\Users\Peter\.claude\skills\e2e-testing\SKILL.md`

**Read first:**
- Playwright documentation — `playwright.dev/docs/intro`
- *Testing JavaScript Applications* — Lucas da Costa (Manning)
- Playwright GitHub Actions guide — `playwright.dev/docs/ci-github`

**Content outline for SKILL.md (target: 380–460 lines):**

1. **When E2E Tests Are Worth It** — the test pyramid, what E2E catches that unit tests miss
2. **Playwright Setup** — `npm init playwright@latest`, project structure, config options
3. **Page Object Model (POM)** — class-per-page pattern, locator encapsulation, action methods
4. **Locator Strategy** — `getByRole`, `getByLabel`, `getByTestId` priority order; avoid CSS selectors
5. **Test Fixtures** — test isolation, shared browser context, fixture composition
6. **Authentication in E2E Tests** — `storageState` for persisting auth session across tests
7. **Network Interception** — `page.route()` to mock API responses, simulate errors, slow network
8. **Form Submission Testing** — multi-step forms, validation error assertions, file upload
9. **Visual Regression Testing** — `expect(page).toHaveScreenshot()`, baseline management
10. **Accessibility Testing** — `@axe-core/playwright` integration, WCAG 2.2 AA assertions
11. **Mobile Viewport Testing** — device emulation, touch events, responsive breakpoint verification
12. **API + UI Combined Tests** — use `request` fixture for API setup before UI assertions
13. **Parallel Execution** — `workers`, shard configuration for fast CI runs
14. **CI Integration (GitHub Actions)** — full workflow: install → build → test → upload report
15. **Debugging** — `--debug` flag, trace viewer (`npx playwright show-trace`), screenshots on failure
16. **Reporting** — HTML report, Allure integration, flaky test detection

**Step 1:** Read all three source materials above.
**Step 2:** Create `SKILL.md` following the content outline.
**Step 3:** Every section must include a TypeScript code snippet.
**Step 4:** Include a complete `playwright.config.ts` example in the Setup section.
**Step 5:** Include a full GitHub Actions workflow YAML in the CI Integration section.
**Step 6:** Run `wc -l SKILL.md` — confirm 350–500 lines.
**Step 7:** Commit: `feat(skills): add e2e-testing skill — Playwright + POM + CI`

---

### Task 2: Create `pwa-offline-first` skill

**File to create:** `C:\Users\Peter\.claude\skills\pwa-offline-first\SKILL.md`

**Read first:**
- Workbox documentation — `developer.chrome.com/docs/workbox`
- Dexie.js documentation — `dexie.org/docs`
- MDN Service Worker API — `developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API`
- Web Push API guide — `web.dev/notifications` (free)

**Content outline for SKILL.md (target: 380–450 lines):**

1. **Why Offline-First for East Africa** — connectivity patterns, EDGE/2G fallback, MTN MoMo offline
2. **PWA Checklist** — HTTPS, Web App Manifest, Service Worker registration, Lighthouse score ≥ 90
3. **Web App Manifest** — `manifest.json` fields: name, icons, start_url, display, theme_color
4. **Service Worker Lifecycle** — install → activate → fetch events; update flow
5. **Workbox Setup** — `workbox-webpack-plugin` or `vite-plugin-pwa`, `generateSW` vs `injectManifest`
6. **Caching Strategies:**
   - `NetworkFirst` — for API calls where freshness matters
   - `CacheFirst` — for static assets (fonts, images, CSS)
   - `StaleWhileRevalidate` — for content that can be slightly stale
   - `NetworkOnly` — for payment and authentication calls (never cache)
7. **App Shell Architecture** — cache the HTML shell and critical JS on install; content loaded dynamically
8. **IndexedDB with Dexie.js** — schema definition, CRUD operations, compound queries
9. **Offline Form Submissions** — queue writes to IndexedDB; sync to server on reconnect
10. **Background Sync API** — `SyncManager.register()`, sync tag patterns, retry strategy
11. **Conflict Resolution** — last-write-wins, server-authoritative, timestamp-based merge
12. **Push Notifications** — VAPID keys, `PushSubscription`, payload encryption, notification UI
13. **Testing PWAs** — Lighthouse CI in GitHub Actions, offline simulation in DevTools, Workbox test utils
14. **Next.js PWA Integration** — `next-pwa` plugin configuration, runtime caching rules
15. **Performance Budget** — Time to Interactive ≤ 3s on 3G, offline load ≤ 1s from cache

**Step 1:** Read all four source materials above.
**Step 2:** Create `SKILL.md` following the content outline.
**Step 3:** Every section must have a JavaScript/TypeScript code snippet.
**Step 4:** Include a complete `workbox.config.js` example.
**Step 5:** Include a complete Dexie.js schema definition example.
**Step 6:** Run `wc -l SKILL.md` — confirm 350–500 lines.
**Step 7:** Commit: `feat(skills): add pwa-offline-first skill — Workbox + IndexedDB + Background Sync`

---

## Phase Completion Checklist

- [ ] `e2e-testing` SKILL.md created — 350–500 lines
- [ ] All 16 sections in e2e-testing content outline are present
- [ ] Complete `playwright.config.ts` example is in the skill
- [ ] Complete GitHub Actions CI workflow YAML is in the skill
- [ ] `pwa-offline-first` SKILL.md created — 350–500 lines
- [ ] All 15 sections in pwa-offline-first content outline are present
- [ ] Dexie.js schema and Workbox config examples are present
- [ ] `e2e-testing` cross-references `advanced-testing-strategy`
- [ ] `pwa-offline-first` cross-references `nextjs-app-router` and `frontend-performance`
- [ ] No skill file exceeds 500 lines
- [ ] Git commit made: `feat(skills): complete phase-7 — quality engineering & test automation`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Testing JavaScript Applications* | Lucas da Costa | Manning | ~$50 | The best JavaScript testing book: unit, integration, E2E with Playwright, CI integration. Directly feeds `e2e-testing` skill. |
| 2 | *Growing Object-Oriented Software, Guided by Tests* | Freeman & Pryce | Addison-Wesley | ~$45 | TDD discipline and design — teaches test-first thinking that improves all testing skills. |
| 3 | *The Art of Software Testing* (3rd ed.) | Glenford Myers | Wiley | ~$40 | Foundational testing theory — equivalence partitioning, boundary analysis, test oracle design. |
| 4 | *Building Progressive Web Apps* | Tal Ater | O'Reilly | ~$40 | PWA fundamentals: Service Workers, offline patterns, push notifications. Feeds `pwa-offline-first` skill. |

### Free Resources

- Playwright documentation — `playwright.dev/docs` — the authoritative Playwright reference; start here
- Playwright GitHub Actions guide — `playwright.dev/docs/ci-github` — CI/CD integration walkthrough
- Workbox documentation — `developer.chrome.com/docs/workbox` — caching strategies, Vite integration
- Dexie.js documentation — `dexie.org/docs` — IndexedDB wrapper; schema, queries, relationships
- MDN Service Worker cookbook — `serviceworke.rs` — offline patterns with code examples
- web.dev PWA guide — `web.dev/progressive-web-apps` — Google's PWA implementation guide
- Lighthouse CI GitHub Action — `github.com/GoogleChrome/lighthouse-ci` — automated PWA quality gate

---

*Next phase: [Phase 8 — Deployment Pipeline, CI/CD & Infrastructure](phase-08.md)*
