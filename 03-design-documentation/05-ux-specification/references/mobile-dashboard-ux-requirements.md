# Mobile And Dashboard UX Requirements

This reference is self-contained. It distills the user's supplied Design Studio UI/UX
mobile navigation, onboarding, dashboard, and mobile app examples articles into SRS-ready
requirements.

Sources used:

- https://www.designstudiouiux.com/blog/mobile-navigation-ux/
- https://www.designstudiouiux.com/blog/mobile-app-onboarding-best-practices/
- https://www.designstudiouiux.com/blog/dashboard-ui-design-guide/
- https://www.designstudiouiux.com/blog/mobile-app-design-examples/

## When To Load

Load this reference for mobile apps, responsive web apps, dashboards, portals, admin
tools, SaaS products, field-worker workflows, finance/reporting modules, and onboarding
flows.

## Mobile Navigation Requirements

Add these when the product has a mobile or small-screen interface:

- Primary navigation shall expose 3-5 high-frequency destinations.
- Secondary destinations shall use a drawer, More menu, settings area, or contextual path
  rather than crowding the primary navigation.
- Core actions shall not rely on gestures alone.
- Navigation labels shall be clear, short, and consistent with the user's task language.
- iOS and Android implementations shall respect native back behavior, safe areas, touch
  targets, and accessibility announcements.

Verification: mobile prototype walkthrough, device test, TalkBack/VoiceOver smoke test,
and task-based usability test.

## Onboarding Requirements

- First-run UX shall demonstrate value before requiring optional permissions or extended
  profile completion.
- Required setup shall be limited to what is necessary for the first valuable task.
- Permissions shall be requested in context with clear benefit text.
- Progressive onboarding shall teach features at first use instead of relying on long
  static intro slides.
- The system shall track activation, onboarding completion, time-to-value, first-session
  task completion, and early retention where analytics is in scope.

Verification: onboarding prototype test, analytics event map, and acceptance test for
permission-denied and skip paths.

## Dashboard Requirements

- Each dashboard shall declare its decision owner, decision job, metric definitions,
  data freshness, thresholds, and drill-down paths.
- KPI cards shall include context such as target, threshold, trend, prior period,
  benchmark, or next action.
- Dashboards shall prioritize urgent exceptions and high-value decisions before general
  exploration.
- Tables and charts shall include labels, units, empty states, error states, loading
  states, and data-freshness messaging.
- Decorative gauges, 3D charts, unlabelled axes, and chart cards without decision paths
  shall be rejected unless an explicit exception is approved.

Verification: dashboard review, data fixture test, accessibility review, and stakeholder
walkthrough against decision jobs.

## Requirement Templates

`MOB-NAV-###: The system shall expose [3-5 primary destinations] in [bottom navigation /
tab bar / adaptive navigation] so that [user segment] can reach [core task] within
[tap/time threshold]. Verification: mobile usability test and accessibility smoke test.`

`ONB-###: The system shall allow a new user to experience [first value] before requiring
[registration/profile/permission], except where [security/compliance reason] requires
earlier setup. Verification: onboarding prototype test and analytics event map.`

`DASH-UX-###: The dashboard shall show [metric] with [context: target/trend/threshold],
[freshness], and [drill-down/action path] for [decision owner]. Verification: stakeholder
walkthrough and data fixture test.`
