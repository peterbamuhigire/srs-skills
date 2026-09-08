# UX friction and premium experience requirements

Parent skill: [Kaizen Engine and Product Improvement](../SKILL.md).

This reference converts targeted UX improvement ideas into requirements evidence. It is a bridge
between the client's job and design/implementation; it is not a visual style catalogue. A
requirement may demand clarity, hierarchy, accessibility, recovery, or measurable comprehension,
but it must not demand that a product imitate a recognisable competitor.

## Source boundary

The following practitioner sources were accessed on 2026-09-08 and are used as Tier 5 inspiration:

- [18 UX Improvements That Move Product Metrics](https://www.eleken.co/blog-posts/ux-improvements)
- [16 Best Dashboard Design Examples](https://www.eleken.co/blog-posts/dashboard-design-examples-that-catch-the-eye)
- [Compelling Design Takes More Than “Making It Like Stripe”](https://www.eleken.co/blog-posts/making-it-like-stripe)

They supply pattern prompts, not standards, performance claims, or acceptance proof. Current
accessibility and platform claims must be verified against the applicable primary source and
recorded with scope, access date, review date, and uncertainty. The Eleken pages' reported case
results are not copied into requirements.

## Experience slice contract

Every material UX improvement or premium design decision should be represented by a small,
traceable slice before it is expanded into a catalogue requirement.

| Field | Requirement |
|---|---|
| Context | Actor, role, device, locale, environment, and stakes |
| Job | Observable outcome the actor needs, not a screen or component |
| Friction | Observed failure, delay, confusion, error, or unnecessary decision |
| Design thesis | Purpose-fit hierarchy and emotional posture in one sentence |
| Authored choice | Distinctive choice, reason, rejected reference treatment, and owner |
| Main path | Trigger, preconditions, steps, system responses, and completion state |
| Failure/recovery | Validation, timeout, empty, permission, interruption, retry, undo, and escalation |
| Accessibility | Text alternatives, labels, focus, keyboard, touch, contrast, motion, and assistive tech method |
| Measure | Baseline, target, method, sample/segment, instrumentation, review date |
| Trace | Requirement IDs, design artefact IDs, implementation slice, test oracle, and evidence location |

If the job, actor, or test oracle is missing, stop the affected branch and return a qualified gap
record. Do not replace missing product evidence with an aesthetic preference.

## Pattern-to-requirement translation

### Reduce form and data-entry burden

Translate import, upload, grouping, progressive disclosure, and guided steps into requirements
about the user's effort and correction rights:

- The system shall allow an actor to supply an existing document or structured source when one is
  available, while retaining a manual fallback where the task permits it.
- Extracted values shall be presented for review and correction before they become authoritative.
- A long form shall identify sections, field purpose, validation timing, save/resume behaviour,
  and a visible completion path.
- The acceptance test shall measure completion, correction, abandonment, or error recovery rather
  than merely checking that fields exist.

Do not require a wizard simply because the form is long. Use a multi-step flow when the steps
have meaningful decision boundaries, and use a structured single page when the decisions are
independent and users benefit from seeing them together.

### Make navigation and context discoverable

Requirements should expose how actors find, scope, and return to work:

- Applied filters, scope, period, sort, and permissions shall be visible in the result context.
- A high-frequency action shall have a discoverable route from the relevant task surface and a
  stable label.
- A detail inspection shall preserve the current entity and a recoverable return path; if it uses
  a modal or side panel, focus and dismissal behaviour shall be testable.
- Search, sidebar, tabs, or chips shall be justified by task frequency and information structure,
  not copied from a reference product.

### Specify dashboards as decision systems

For each dashboard view, write a decision table rather than a list of widgets:

| Decision field | Required question |
|---|---|
| Audience and job | Who must decide what, and under what time or risk constraint? |
| Signal | Which measure answers “what needs attention?” with unit, period, and comparison? |
| Explanation | Which trend, driver, or segment answers “why?” |
| Action | What can the actor do next, and what is the recovery path? |
| Detail | Which records, definitions, or drill-down support verification? |
| State | What does no data, stale data, partial data, or failed data mean? |
| Evidence | How will comprehension, task time, error, or decision quality be assessed? |

Use an operational, analytical, strategic, or explicitly hybrid classification only to clarify the
job. Do not impose an arbitrary number of cards, charts, or a universal “five-second” pass rule.
Make the scan-time or metric-count idea a hypothesis that can be tested with the actual audience.

### Preserve context without hiding depth

Specify a modal, side panel, inline expansion, or new page using the content depth and navigation
need as the decision rule:

- Quick inspection or small edit: keep context and define close, Escape, focus, and return rules.
- Deep or linkable work: use a page with a stable URL, breadcrumb or back path, and independent
  loading/error states.
- Independent tasks: consolidate where it lowers transitions without creating a wall of fields.
- Dependent decisions or high-risk submission: keep the staged flow and expose progress, saved
  state, review, and final confirmation.

### Specify feedback, progress, and waiting honestly

Every material asynchronous operation shall define states for queued, active, partial, success,
failure, retry/cancel, and timeout where applicable. Status copy shall describe a real system
stage or a clear user action; it shall not invent progress. A multi-step flow shall expose its
current step and total when those values are known. A long-running operation shall define what
happens if the actor leaves, reloads, loses connectivity, or submits twice.

### Specify purpose-fit authorship

The SRS shall not say “make it premium”, “make it like Stripe”, or “make it artistic” as a
stand-alone requirement. Replace the adjective with a testable decision record:

```text
UX-THESIS: [client-specific hierarchy and intended feeling]
UX-SIGNATURE: [distinctive choice] -> [purpose it serves]
UX-REFERENCE: [principle learned] -> [surface treatment deliberately rejected]
UX-STATES: [states and platforms covered]
UX-MEASURE: [baseline, target, method, owner, review date]
UX-EVIDENCE: [render/demo/test/user evidence or NOT_ASSESSED]
```

This keeps taste in the design decision while making fit, state coverage, and evidence visible to
engineering and assurance. It also prevents a copied look from becoming an accidental product
requirement.

## Acceptance criteria patterns

Use the following shape for a requirement that crosses design and implementation:

```text
Given [actor, context, data state, and viewport]
When [observable action or system event]
Then [visible and accessible result]
And [failure/recovery or interruption behaviour]
Measured by [metric, oracle, threshold, evidence owner, and review date]
```

At minimum, cover:

- first-use and returning-user routes;
- empty, loading, error, success, partial, and permission states;
- narrow and wide layouts plus long labels/content;
- keyboard/focus and assistive technology checks where interaction is present;
- reduced-motion behaviour where motion is present;
- data definitions, stale/partial data, and user correction where a dashboard or extraction is involved.

## Decision rules

| Condition | Requirement decision | Failure avoided |
|---|---|---|
| Source data can be reused and must be corrected | Import plus editable confirmation | Trust loss and transcription waste |
| Steps are independent and the full context fits | One-page composition | Unnecessary next-button tax |
| Steps are dependent or high-risk | Guided flow with progress and resume | Invalid order and abandonment uncertainty |
| Dashboard has one urgent decision | Signal-first view with explanation and action | Equal-weight metric noise |
| Detail is shallow and context-dependent | Modal/panel with focus recovery | Context loss and inaccessible overlay |
| Visual reference is recognisable as another product | Write the principle and a new thesis | Imitation becoming a requirement |
| Evidence is unavailable | Mark `NOT_ASSESSED`, assign owner, block the relevant claim | False readiness |

## Anti-patterns

- **Screen-first requirements.** Fix: start with the actor's job, friction, outcome, and evidence.
- **“Premium” as a non-functional requirement.** Fix: decompose the word into thesis, authored
  decisions, state coverage, measurable quality, and proof.
- **Dashboard widget inventory.** Fix: map signal, explanation, action, detail, and state before
  selecting a visual encoding.
- **Universal visual thresholds.** Fix: treat scan time, card counts, or density targets as
  hypotheses tied to a named audience and task.
- **Happy-path-only UX acceptance.** Fix: add empty, failure, interruption, keyboard, responsive,
  and recovery criteria.
- **Reference-copying.** Fix: record the transferable principle and explicitly reject the copied
  surface treatment.
- **Requirements that cannot be handed off.** Fix: give each material decision an ID, owner,
  downstream consumer, oracle, and evidence location.

## Worked example

Weak requirement: “The dashboard shall look premium and show important metrics.”

Traceable requirement slice:

```text
UX-014: For a care coordinator on a 1280px desktop during a morning triage shift,
the overview shall surface overdue follow-ups with status, due date, population,
and the next available action before secondary trend detail.
Given no overdue follow-ups, the view shall explain the empty state and show how to
change the period or scope. Given stale or failed data, it shall disclose that state,
retain the last known timestamp, and provide retry or escalation.
The implementation shall preserve keyboard access, a readable narrow layout, and a
non-colour-only attention cue. Baseline and target: task comprehension and time to
identify the next action, owned by the product analyst, reviewed after the pilot.
The design record shall carry the client-specific thesis and signature choice; it
shall not copy a competitor's gradient or card arrangement.
```

The acceptance evidence is the requirement trace, representative render or running slice,
state matrix, accessibility result, and measured or explicitly unassessed user outcome.
