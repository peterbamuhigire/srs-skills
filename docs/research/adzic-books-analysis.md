# Adzic Books: Comprehensive Analysis for SRS-Skills Engine Improvement

**Source books:**
1. Gojko Adzic & David Evans — *Fifty Quick Ideas To Improve Your Tests* (197 pages)
2. Gojko Adzic & David Evans — *Fifty Quick Ideas to Improve Your User Stories* (206 pages)
3. Gojko Adzic — *Impact Mapping* (103 pages)

**Purpose:** Extract all ideas, principles, templates, and anti-patterns to improve the SRS-Skills requirements documentation engine, mapped to pending improvements B-03, B-05, B-06, W-08, W-09, W-03, B-07, W-19, W-13, W-05.

---

## SECTION 1: Fifty Quick Ideas To Improve Your Tests

### Q1. How does Adzic define Given-When-Then and what are common violations?

**Canonical GWT structure:**

- **Given** = preconditions that existed BEFORE the action. Passive voice, past tense. Multiple Givens are permitted. Captures the state of the world before the trigger.
- **When** = the single triggering action. Active voice, present tense. There must be EXACTLY ONE When per scenario. Having two Whens means you have two scenarios.
- **Then** = postconditions — what changes in the world as a result. Passive/future-tense assertions. May be multiple Thens.

**Common violations (anti-patterns):**
- [ANTI-PATTERN] Multiple When clauses in one scenario — signals the scenario covers too many behaviors.
- [ANTI-PATTERN] Using "When" for background state (should be Given).
- [ANTI-PATTERN] Using "And" as a When (there can only be one action).
- [ANTI-PATTERN] Thens that describe implementation details rather than observable outcomes.
- [ANTI-PATTERN] Givens that specify UI state rather than business state (couples tests to interface).

**SRS-Skills mapping:** Skill 05 (Functional Requirements) must enforce the single-When rule. Skill 08 (Audit) should flag [V&V-FAIL] when a scenario has zero or multiple When clauses. → **Directly feeds W-03 (inline GWT stubs).**

---

### Ideas 1–13: Generating Test Ideas

**Idea 1 — Think about behaviour, not implementation**
- Core: Tests should describe observable business outcomes, not internal code paths.
- SRS mapping: Requirements written in stimulus-response form (CLAUDE.md rule) naturally produce testable-behavior scenarios. Requirements that reference internal architecture [V&V-FAIL] should be flagged.
- [CHECKLIST-ITEM] Verify that every "Then" clause in a GWT scenario references an externally observable state change, not an internal variable or log entry.

**Idea 2 — Use the ACC (Attribute-Component-Capability) matrix**
- Core: Whittaker/Google framework. Attributes = qualities the product must have (e.g., fast, secure, accessible). Components = structural elements (e.g., login module, payment processor). Capabilities = things the system can do (e.g., authenticate user, process payment). Cross-referencing these three axes generates a complete test coverage map.
- Template fields: `Attribute | Component | Capability | Test scenario ID`
- SRS mapping: ACC attributes map directly to FURPS+ non-functional categories. In Skill 06 (Logic Modeling), an ACC matrix appended to each functional requirement provides built-in traceability.
- [CHECKLIST-ITEM] For each Skill 05 requirement, confirm that ACC coverage exists across all relevant Capabilities.
- [TEMPLATE-FIELD] `acc_attributes`, `acc_components`, `acc_capabilities` as metadata fields on requirements.

**Idea 3 — Apply the SHADED FIGS heuristic**
- Core: A mnemonic for test scenario generation covering non-happy paths:
  - **S**cary — worst-case failure scenarios
  - **H**appy — normal successful path
  - **A**ngry — user does unexpected/hostile things
  - **D**elinquent — system misbehaves (timeouts, corrupt data)
  - **E**mbarrassing — system does something that causes PR/reputational damage
  - **D**esolate — system is empty, no data, first run
  - **F**orgetful — system loses state it should retain
  - **I**ndecisive — system can't resolve ambiguity
  - **G**reedy — resource exhaustion, system wants more than it has
  - **S**tressful — performance under load
- SRS mapping: A complete requirement (IEEE 830 Completeness) should have test scenarios for each applicable SHADED FIGS category. This is a checklist extension for Skill 08.
- [CHECKLIST-ITEM] For each functional requirement, check that at least Scary, Happy, Angry, Desolate, and Stressful paths are addressed in acceptance scenarios.

**Idea 4 — Use examples to clarify requirements**
- Core: Abstract requirements hide misunderstandings. Concrete examples force precision. "The system shall display an error" → What error? When exactly? What does the user see? Examples answer these questions.
- SRS mapping: IEEE 830 Verifiability criterion. Every requirement without at least one concrete example is unverifiable.
- [CHECKLIST-ITEM] Flag any requirement that contains no example instantiation as [V&V-FAIL: missing example].

**Idea 5 — Explore the boundaries**
- Core: Boundary condition testing (Equivalence Partitioning / Boundary Value Analysis). Test at the exact boundary, just below, and just above. For date/time: leap years, end-of-month, end-of-year, timezone edge cases. For numbers: negative, zero, max-int, float precision limits.
- SRS mapping: Requirements specifying numeric or date-based behavior MUST include boundary assertions in their acceptance criteria. → Feeds **B-03 (VERIFIABILITY-FAIL tag)**.
- [TEMPLATE-FIELD] `boundary_conditions` on functional requirements with values for: lower bound, upper bound, invalid below, invalid above.

**Idea 6 — Use personas to generate tests**
- Core: Different user types have different assumptions, error patterns, and mental models. A novice user and a power user interact with the same feature differently.
- SRS mapping: User personas defined in `_context/stakeholders.md` should be cross-referenced against scenarios in Skill 05. Each persona should have at least one scenario demonstrating their specific interaction pattern.
- [TEMPLATE-FIELD] `actor_persona` on each GWT scenario.
- → Feeds **B-07 (AUDIENCE role tags)**.

**Idea 7 — Consider using multiple levels of abstraction**
- Core: Three-layer test pyramid: business decisions layer (what the product decides), workflows layer (how the product operates), technical interactions layer (how components communicate). Tests at the wrong level are brittle or miss business intent.
- SRS mapping: Skill 05 requirements should be written at the business decisions layer. Skill 03 (Design Documentation) addresses workflow and technical layers.

**Idea 8 — Use BDD with stakeholders**
- Core: Behavior-Driven Development bridges the communication gap between business and technical. Writing scenarios WITH stakeholders (not for them) catches misalignment early.
- SRS mapping: The three-amigos model (business analyst + developer + tester) should be reflected in the review gate at Skill 05's Inspect phase (PRIME methodology).

**Idea 9 — Split complicated scenarios**
- Core: Long scenarios that exercise multiple behaviors are hard to maintain and give misleading failure signals. A scenario should test one and only one behavior.
- [ANTI-PATTERN] Scenarios with more than one When clause.
- [ANTI-PATTERN] Scenarios exceeding 5-7 step lines total.
- SRS mapping: Skill 05 should flag any scenario exceeding a complexity threshold.

**Idea 10 — Write assertions first**
- Core: Identifies what "done" means before discovering how to get there. Prevents gold-plating. Mirrors Test-Driven Development but at the requirements level.
- SRS mapping: This is the canonical justification for the stimulus-response pattern in CLAUDE.md. The response (Then) must be written before the implementation details. → Feeds **B-03 (VERIFIABILITY-FAIL tag)** and **B-05 (phase gate exit criteria)**.
- [CHECKLIST-ITEM] Skill 05 review gate: confirm the Then clause was written before the Given/When were fully elaborated.

**Idea 11 — Give tests meaningful names**
- Core: Test names should describe the scenario, not the input. "User with expired card attempting purchase" not "Test_3_17_b". Scannable by a non-technical reader.
- Template: `[Actor] [action] [context/condition]` e.g., "Premium user cancels subscription during trial period"
- SRS mapping: Requirement IDs in SRS should follow a similar naming convention for human readability.

**Idea 12 — Avoid pesticide paradox: vary test data**
- Core: Running the same tests with the same data repeatedly gives diminishing returns. Varied data (especially boundary and equivalence partition data) improves coverage.
- SRS mapping: Acceptance scenarios should specify data categories, not just one fixed example value.
- [CHECKLIST-ITEM] Each scenario should reference a data class (e.g., "any valid UK postcode") not a single hardcoded value (e.g., "SW1A 1AA") unless the specific value is the point.

**Idea 13 — Apply testing heuristics to interface structure**
- Core: Elisabeth Hendrickson's Test Heuristics Cheat Sheet. For text: too long, too short, Unicode, special chars. For numbers: negative, zero, boundary. For dates: leap year, timezone, DST transitions.
- → Directly informs boundary_conditions template field from Idea 5.

---

### Ideas 14–28: Designing Good Checks

**Idea 14 — Describe context, not procedure**
- Core: Scenarios should describe the context in which something happens, not the steps to set up that context. "Given a customer with an overdue balance" not "Given the tester clicked Customers, then clicked New, then entered...".
- [ANTI-PATTERN] Procedural Givens that describe UI navigation rather than system state.
- SRS mapping: Skill 05 scenarios written procedurally will fail the ASTM E1340 verifiability check.

**Idea 15 — Use the right level of precision**
- Core: Too much precision makes tests brittle (pixel coordinates, exact SQL); too little makes them unverifiable (vague assertions like "the page loads"). Target the business-level observable outcome.
- [ANTI-PATTERN] Assertions that reference pixel positions, database table names, or API response codes in a business-facing specification.
- SRS mapping: Feeds **B-03 (VERIFIABILITY-FAIL tag)** — if the assertion is too vague to generate a pass/fail test, tag it.

**Idea 16 — Test-driving specification: use examples to specify**
- Core: Specification by Example — precise examples prevent ambiguity better than prose descriptions. Executable specifications are living documentation.
- Three C's of executable specifications:
  - **Conciseness** — no noise, every word earns its place
  - **Completeness** — all cases covered, no edge cases omitted
  - **Coherence** — examples form a consistent, non-contradictory set

**Idea 17 — Balance three competing forces**
- Core: Tests must balance coverage (completeness) vs. speed (fast feedback) vs. confidence (accuracy). Over-optimizing one degrades others. Choose the balance explicitly for each test suite.
- SRS mapping: Skill 08 audit phase should document the chosen balance and justify it.

**Idea 18 — Write assertions first** (reinforcement of Idea 10)
- Core: Start with "what does success look like?" before writing preconditions or actions.

**Idea 19 — Split technical and business checks**
- Core: Business-facing scenarios (GWT) belong in the requirements; technical assertions (unit tests, performance benchmarks) belong in a separate layer. Mixing them creates noise and cognitive overhead.
- SRS mapping: Skill 05 (business checks) and Skill 06 (logic modeling, which may include technical assertions) should remain clearly separate.

**Idea 20 — Don't automate manual tests**
- Core: Manual exploratory tests and automated regression tests serve different purposes. Converting a manual test script into an automated test loses the exploratory intent.
- [ANTI-PATTERN] Copying manual test scripts verbatim into automated test suites.

**Idea 21 — Create tests that explain intent**
- Core: Tests double as documentation. A readable test explains WHY a behavior exists, not just WHAT it does.

**Idea 22 — Use tables for data-driven tests**
- Core: When the same scenario applies to multiple input/output pairs, use a table rather than repeating the scenario multiple times.
- Template: `| Input condition | Expected output | Notes |`
- [TEMPLATE-FIELD] `scenario_table` as an optional structured field on requirements with multiple data-driven assertions.

**Idea 23 — Separate test components clearly**
- Core: Given/When/Then delineation must be unambiguous. If any clause is missing, the scenario is incomplete.

**Idea 24 — Test what the system IS, not how it does it**
- Core: Specification tests should verify externally observable outcomes, not internal implementation paths. Avoids coupling specifications to implementation.

**Idea 25 — Consider negative tests**
- Core: For every "should do X," there should be a corresponding "should NOT do Y" scenario for boundary enforcement.
- [CHECKLIST-ITEM] Every requirement with a "shall" must have at least one rejection/error scenario.

**Idea 26 — Test in layers**
- Core: Business layer (GWT), workflow layer (integration), technical layer (unit). Each has a purpose and a right tool.

**Idea 27 — Manage flaky tests actively**
- Core: A test that sometimes passes and sometimes fails is worse than no test — it trains teams to ignore failures. Track and eliminate flakiness systematically.
- [ANTI-PATTERN] Marking a failing test as "known issue" without a resolution deadline.

**Idea 28 — Balance three competing forces** (already covered at Idea 17)

---

### Ideas 29–38: Improving Testability

**Idea 29 — Design for testability**
- Core: Testability is a first-class architectural concern, not an afterthought. Hard-to-test systems have hidden dependencies and poor observability.
- SRS mapping: Skill 03 (Design Documentation) should include a testability analysis section. A system with no testability requirements is incomplete.

**Idea 30 — Improve observability**
- Core: The system must expose enough state to verify its own behavior. This includes: audit logs, status APIs, event streams, monitoring endpoints.
- [TEMPLATE-FIELD] `observability_mechanism` on each functional requirement — specifies how the Then clause can be verified.

**Idea 31 — Improve controllability**
- Core: The system must accept test inputs cleanly (e.g., injectable test data, configurable time, stub external services). Hard-coded dependencies destroy controllability.

**Idea 32 — Reduce coupling for testability**
- Core: Tight coupling makes tests fragile. Loose coupling allows components to be verified in isolation.

**Idea 33 — Avoid shared test state**
- Core: Tests that depend on prior test state are ordering-dependent and produce misleading results.
- [ANTI-PATTERN] Tests that assume a specific database state created by a previous test run.

**Idea 34 — Make tests repeatable**
- Core: A test must produce the same result every time, given the same initial conditions. Non-repeatable tests are unreliable.

**Idea 35 — Separate infrastructure from logic**
- Core: Business logic should be testable without infrastructure (databases, message queues, external APIs). Infrastructure testing is a separate concern.

**Idea 36 — Use stubs and mocks appropriately**
- Core: Mocks verify interaction (did the method get called?). Stubs provide canned responses. Overuse of mocks creates tests that verify the mock, not the behavior.
- [ANTI-PATTERN] Mocking the system under test.

**Idea 37 — Create a test data strategy**
- Core: Test data should be managed systematically. Categories: minimal (just enough to run the scenario), boundary (edge cases), negative (invalid data).
- [TEMPLATE-FIELD] `test_data_strategy` on test suites with values: minimal | boundary | negative | realistic | production-derived.
- → Feeds **W-09 (defect resolution)** — defects found in production but not in test may indicate a test data strategy gap.

**Idea 38 — Isolate external dependencies**
- Core: External systems (payment gateways, email providers, third-party APIs) should be stubbable for test purposes.

---

### Ideas 39–50: Managing Large Test Suites

**Idea 39 — Make developers responsible for tests**
- Core: Testing is not a separate QA phase. Developers own their tests. Shared ownership prevents the "throw it over the wall" anti-pattern.
- SRS mapping: Each requirement in Skill 05 should have a named owner responsible for its acceptance test.

**Idea 40 — Avoid organising by work items**
- Core: Tests organized by story/ticket become orphaned or misleading after the story closes. Organize by functional area instead.
- [ANTI-PATTERN] Test suite organized as: `test_story_123.feature`, `test_story_456.feature`
- → Directly maps to User Stories Book Idea 50 (Throw stories away after delivery).

**Idea 41 — Version control tests with code**
- Core: Tests that are not in version control are not trustworthy. Tests and code must be co-versioned.
- SRS mapping: Skill 05 acceptance scenarios should be stored in version control alongside the SRS document, not in a separate ticketing tool.

**Idea 42 — Gallery of examples**
- Core: A browsable library of test examples that non-technical stakeholders can read and validate. Makes specifications living documentation.
- SRS mapping: This is the executable specification library. Skill 05 output should be publishable as a gallery.

**Idea 43 — Decouple coverage from implementation**
- Core: Coverage metrics (line coverage, branch coverage) measure test execution, not test quality. A test that exercises every line but makes no assertions has 100% line coverage and zero value.
- [ANTI-PATTERN] Using code coverage as a proxy for requirement coverage.
- SRS mapping: Requirement coverage (which requirements have corresponding acceptance tests?) is more valuable than code coverage.

**Idea 44 — Avoid strict coverage targets**
- Core: Arbitrary coverage percentages (e.g., "95% line coverage") drive gaming behavior. Teams write trivial tests to hit the number.
- [ANTI-PATTERN] Blocking deployment on a coverage threshold without requirement-level coverage verification.

**Idea 45 — Measure test half-life**
- Core: Half-life = the time after which 50% of a set of tests have been modified. High half-life indicates stable, valuable tests. Low half-life indicates fragile, brittle tests tied to implementation details.
- [TEMPLATE-FIELD] `test_half_life` on test suites as a stability metric.
- SRS mapping: Acceptance scenarios with low half-life should be reviewed for specification quality.
- → Feeds **B-05 (phase gate exit criteria)** — a test suite with declining half-life signals specification instability that should trigger a re-inspect gate.

**Idea 46 — Optimise for reading**
- Core: Tests that are hard to read are hard to maintain. Optimize scenario structure for a human reader, not for a test runner.

**Idea 47 — Name tests for SEO (discoverability)**
- Core: Test names should be searchable by relevant business terms. A test named "customer_registration_with_expired_card" is findable. "Test_003" is not.

**Idea 48 — Explain purpose in introduction**
- Core: Each test suite/feature file should have an introduction paragraph explaining WHAT the suite covers and WHY it exists.
- [TEMPLATE-FIELD] `suite_purpose` narrative field at the top of each test suite.

**Idea 49 — Split just-in-case tests**
- Core: Some tests exist for edge cases that almost never occur. Separate these into a "low-frequency" suite that runs less often, to keep the main feedback loop fast.

**Idea 50 — Let the chaos monkey out**
- Core: Deliberately inject failures (kill processes, exhaust memory, introduce network latency) to test system resilience. Chaos engineering at the specification level means explicitly writing requirements for recovery scenarios.
- SRS mapping: NFR requirements for reliability (Skill 07 Attribute Mapping) should include chaos-monkey style acceptance criteria: "The system shall recover from [failure type] within [time] without [data loss condition]."

---

### Summary: Tests Book — Key Answers to Specified Questions

**Q2. What specific templates/formats does Adzic recommend for test documentation?**
- GWT format with single-When rule enforced
- ACC matrix: `Attribute | Component | Capability | Scenario ID`
- Data-driven tables: `Input | Expected Output | Notes`
- Feature file header: `Suite purpose narrative + Tags + Scenarios`
- Test name convention: `[Actor] [action] [context]`

**Q3. How does Adzic handle test data management?**
- Test data categories: minimal, boundary, negative, realistic, production-derived
- Each scenario should reference a DATA CLASS (equivalence partition), not a single hardcoded value
- External data sources should be stubbable and version-controlled
- [TEMPLATE-FIELD] `test_data_strategy` enum per suite

**Q4. What is his view on traceability between tests and requirements?**
- Tests must be organized by FUNCTIONAL AREA, not by work item/story
- Requirement ID on every test scenario for bidirectional traceability
- After delivery, tests should be re-filed under functional area — story reference is discarded
- Feature maps (hierarchical mind maps with hyperlinks) as navigation aids
- Version control is the authoritative audit trail

**Q5. What anti-patterns does he identify in test documentation?**
Per the extraction above, key anti-patterns are:
- Multiple When clauses in one scenario
- Procedural Givens (UI navigation instead of system state)
- Organizing tests by stories/tickets
- Strict numeric coverage targets driving gaming
- Tests with too-precise implementation detail in assertions
- Shared test state across test runs

**Q6. How does he address acceptance criteria specification?**
- Acceptance criteria = a set of GWT scenarios covering: Happy path, key error paths, boundary conditions
- Written BEFORE implementation (assertion-first approach)
- Must be agreed by three-amigos (business + developer + tester)
- Acceptance = ALL scenarios pass AND scenarios have been verified against real user outcomes post-delivery

**Q7. What is his recommended approach to NFR testing?**
- NFRs are not "non-functional" — they ARE functional, just measured on a sliding scale
- Use QUPER model: utility breakpoint, differentiation point, saturation point
- NFR assertions should specify the acceptable range, not a single number
- Chaos monkey scenarios for reliability NFRs
- Performance NFRs should specify both the threshold AND the architectural barrier where more investment is required

---

## SECTION 2: Fifty Quick Ideas to Improve Your User Stories

### Q1. What is Adzic's recommended story format, and when should it be abandoned?

**Canonical format:** "As a [role], I want [feature] so that [benefit]" — BUT this is a starting point, not a law.

**When to abandon the format:**
- When the story has multiple levels of value (the format forces you to pick one — don't; list all levels instead)
- When the role is the system itself (describe the behavior change instead)
- When the story is about organizational learning, not a user feature
- When forcing the format generates argument rather than discussion — use it as a discussion token, not a contract

**Core principle:** The story format exists to generate CONVERSATION, not to be a specification. A story is "a promise to have a conversation." The specification comes from the three-amigos discussion, not from the story card.

---

### Ideas 1–8: Creating Stories

**Idea 1 — Tell stories, don't write them**
- Core: Stories are conversation tokens, not specifications. The card is a reminder, not a contract.
- [ANTI-PATTERN] Treating the story format as a complete specification that developers implement without discussion.
- SRS mapping: The `_context/` PIF files are the specification, not the story titles.

**Idea 2 — Don't worry about format**
- Core: Don't spend time arguing about format. Stories can be written in any form that enables conversation.
- SRS mapping: Requirements engineering (Skill 02) should not reject input because it's not in the "right" story format.

**Idea 3 — Describe behaviour change**
- Core: The best stories describe how a USER'S BEHAVIOR will change after delivery, not what the software will do. "Users will be able to X" vs. "The system will provide X."
- Template: "In order to [behaviour change], [who] will [do differently]."
- [TEMPLATE-FIELD] `behaviour_change` as a mandatory field in Skill 05 requirements.
- → Feeds **B-07 (AUDIENCE role tags)**.

**Idea 4 — Describe system change**
- Core: When the system itself changes behavior (e.g., automated alerts, background jobs), describe what PREVIOUSLY REQUIRED HUMAN ACTION is now automated.
- SRS mapping: System-initiated requirements should specify the eliminated manual step.

**Idea 5 — Survivable experiments**
- Core: Stories as hypotheses. Frame stories as experiments that the organization can survive if they prove wrong. "We believe [feature] will cause [behaviour change]. We will know this when [measurable signal]."
- [TEMPLATE-FIELD] `hypothesis`, `success_signal` on stories/requirements.
- → Feeds **B-05 (phase gate exit criteria)** — exit criteria should include outcome measurement.

**Idea 6 — Generic roles**
- Core: "As a user" is usually too vague. Identify specific user segments. But don't over-specify — a role that applies to 2% of users shouldn't drive the majority of requirements.
- [ANTI-PATTERN] "As a user" in every story — the role adds no information.
- SRS mapping: User roles defined in `_context/stakeholders.md` should map to specific story actors.

**Idea 7 — Zone of control**
- Core: Distinguish between what the system CONTROLS (within your scope) and what it only INFLUENCES (behaviour of external actors). Don't write requirements for what you can't control.
- [ANTI-PATTERN] Requirements stating the system "will ensure users do X" when the system can only make X easier, not mandatory.
- SRS mapping: Requirements that specify user behavior as a SHALL should be reviewed — they may be in the sphere of influence, not control.
- → Feeds **B-03 (VERIFIABILITY-FAIL tag)** — requirements outside the zone of control cannot have a deterministic pass/fail test.

**Idea 8 — Best before date**
- Core: Some stories have a shelf life. A story that made sense in Q1 may be irrelevant in Q4. Add explicit expiry signals to stories that are time-sensitive.
- [TEMPLATE-FIELD] `best_before` or `expiry_trigger` on time-sensitive requirements.

---

### Ideas 9–19: Planning with Stories

**Idea 9 — Set deadlines as a planning tool, not punishment**
- Core: Deadlines clarify scope. "What can we deliver by [date]?" is more productive than "When will feature X be done?" Deadlines should serve as scope-reduction levers.

**Idea 10 — Hierarchical backlogs**
- Core: Goals → Impacts → Stories → Tasks. Never prioritise at the story level when you haven't aligned at the goals/impacts level first.
- Template: Impact map hierarchy (Why → Who → How → What) maps directly to this.
- → Directly feeds **W-05 (Cost of Delay prioritization)** — prioritize at the impact level.

**Idea 11 — Group by impact**
- Core: Stories are grouped under the impact they contribute to, not by feature area or component. A story that doesn't map to an impact is either orphaned or a fake story.
- [ANTI-PATTERN] Backlog with no impact hierarchy — pure flat list of feature stories.
- SRS mapping: Skill 02 (Requirements Engineering) should map every functional requirement to a business impact from `_context/goals.md`.

**Idea 12 — Story map**
- Core: Jeff Patton's story map: activities across the top (user's workflow), stories vertically below each activity (details), releases as horizontal slices. Enables "walking the map" to verify completeness and identify the minimum viable slice.
- SRS mapping: Skill 02 output could include a narrative story map summary.

**Idea 13 — CREATE funnel**
- Core: Wendel behavioral model for designing behavior-change features. Cue / Reaction / Evaluation / Ability / Timing / Execution. If any step fails, the behavior change fails.
- SRS mapping: Behavior-change requirements should be validated against the CREATE funnel. A feature that provides Ability but fails at Cue will not change behavior.
- [CHECKLIST-ITEM] For each behavior-change requirement, verify that the system addresses all six CREATE stages, or explicitly document which stages are outside scope.

**Idea 14 — Global concerns (FURPS+)**
- Core: Non-functional requirements that cut across all stories. Performance, reliability, security, maintainability, usability. These must be stated once as global constraints, not repeated per story.
- SRS mapping: Skill 07 (Attribute Mapping) captures these. They should be documented in `_context/nfr-defaults.md` and injected via `[DOMAIN-DEFAULT]` blocks.
- → Feeds **B-06 (GLOSSARY-GAP tag)** — if an NFR term is used without a metric, flag it.

**Idea 15 — Stages of growth (Lean Analytics)**
- Core: Alistair Croll/Yoskovitz Lean Analytics stages: Empathy → Stickiness → Virality → Revenue → Scale. At each stage, different metrics matter and different features should be prioritized.
- SRS mapping: Requirements engineering should identify the project's current growth stage and filter requirements accordingly.

**Idea 16 — Purpose Alignment Model**
- Core: Classify features as: Differentiating (invest heavily), Parity (must-have, minimal investment), Partner (outsource), Who cares (eliminate).
- [TEMPLATE-FIELD] `purpose_alignment` enum: differentiating | parity | partner | none on requirements.
- → Feeds **W-05 (Cost of Delay prioritization)**.

**Idea 17 — Stakeholder chart**
- Core: Map stakeholders by interest vs. influence. High influence/high interest: manage closely. High influence/low interest: keep satisfied. Low influence/high interest: keep informed. Low/low: monitor.
- [TEMPLATE-FIELD] Stakeholder register fields: `name | role | influence_level | interest_level | engagement_strategy`.
- → Feeds **W-13 (stakeholder register upgrade)**.

**Idea 18 — Name milestones**
- Core: Milestones should have memorable names that communicate their business impact, not just dates. "Payment processing live" not "Milestone 3."
- SRS mapping: Phase gates in Skill 05 should have meaningful names tied to business capabilities delivered.

**Idea 19 — Focus on user segments for milestones**
- Core: Each milestone should target a specific user segment and deliver complete value to them, rather than delivering incomplete value to all users.
- → Feeds **W-05 (Cost of Delay prioritization)** and **B-05 (phase gate exit criteria)**.

---

### Ideas 20–28: Discussing Stories

**Idea 20 — Low-tech discussion tools**
- Core: Index cards, whiteboards, and sticky notes outperform digital tools for story discussion because they enable tactile, spatial reasoning and prevent premature formalization.
- SRS mapping: `_context/` files represent the digitized output of low-tech discussions, not the discussions themselves.

**Idea 21 — Imagine the demonstration**
- Core: Before writing acceptance criteria, ask: "What would we show in a sprint review to prove this story is done?" If you can't picture the demonstration, the story is not ready to discuss.
- [CHECKLIST-ITEM] Skill 05 review gate: can the reviewer picture a concrete, time-limited demonstration of each requirement?
- → Feeds **B-05 (phase gate exit criteria)**.

**Idea 22 — Diverge and merge**
- Core: Split the group into independent smaller teams to generate ideas/scenarios in parallel (diverge), then come together to compare (merge). Suppresses groupthink and produces more diverse scenarios than open discussion.
- SRS mapping: Elicitation workshops should use diverge/merge structure. Capture dissenting scenarios, not just consensus.
- → Feeds **W-19 (elicitation techniques)**.

**Idea 23 — Three amigos**
- Core: The minimum effective team for a story discussion is one business person + one developer + one tester. The three roles together cover: business intent, technical feasibility, and edge case discovery.
- The goal is to stop when everyone has ENOUGH INFORMATION to start, not when they have ALL information.
- [CHECKLIST-ITEM] Every requirement entering Skill 05 should have a documented three-amigos sign-off.
- → Feeds **W-19 (elicitation techniques)**.

**Idea 24 — Measure alignment using feedback exercises**
- Core: Gary Klein's "Sources of Power" feedback exercise. At the end of a discussion, someone poses a difficult boundary condition and everyone writes their expected outcome independently. If answers diverge, the group is NOT aligned and the discussion should continue.
- Open-ended question design: "What happens next?" not "Who wins?"
- SRS mapping: Alignment exercises can be documented as part of the elicitation record in `_context/elicitation_log.md`.
- → Feeds **W-19 (elicitation techniques)**.

**Idea 25 — Play the devil's advocate**
- Core: Explicitly assign someone to argue AGAINST a story before detailed analysis begins. This surfaces: wrong target user, wrong solution, wrong assumption about user need. The devil's advocate challenges: the user need, the user segment, and the proposed solution.
- [CHECKLIST-ITEM] For each requirement: has someone challenged the user need, the segment, and the solution independently?

**Idea 26 — Divide responsibility for defining stories**
- Core: Business stakeholders specify the "In order to" (benefit) and "As a" (role) parts. Delivery team proposes OPTIONS for the "I want" (solution) part. Both sides evaluate options together.
- [ANTI-PATTERN] Business stakeholders specifying the technical solution without delivery team input.
- SRS mapping: The `_context/` files (populated by business stakeholders) should document GOALS AND IMPACTS, not implementation choices.

**Idea 27 — Split business and technical discussions**
- Core: Run business discussion with stakeholders first. Let them leave. Then run the technical design discussion with the delivery team. Mixing them causes either business user disengagement or technical over-specification by non-technical people.
- SRS mapping: This is the basis for separating Skill 02 (Requirements Engineering) from Skill 03 (Design Documentation) as distinct phases.

**Idea 28 — Investigate value on multiple levels**
- Core: Most stories have a chain of value: user benefit → user engagement → revenue → business sustainability. Capture the whole chain. When forced to pick one level for the story format, list all levels and then pick the highest one that is still meaningful.
- Template: `Direct user benefit → Indirect user benefit → Organizational benefit → Strategic benefit`
- SRS mapping: Skill 01/02 should document the full value chain from `_context/goals.md` through to user stories.

**Idea 29 — Discuss sliding-scale measurements with QUPER**
- Core: For NFRs measured on a scale (performance, capacity, security), define three breakpoints:
  - **Utility breakpoint**: below this, the product is useless
  - **Differentiation point**: above this, the product has competitive advantage
  - **Saturation point**: above this, improvements provide no market value
  - Also map architectural **barriers** (the cost cliffs where further improvement requires major rework)
- Choose RANGES not single numbers. Start with the failure condition (utility breakpoint — the worst acceptable value) and work up.
- [TEMPLATE-FIELD] `quper_utility`, `quper_differentiation`, `quper_saturation`, `quper_current_barrier` on NFR requirements.
- → Directly feeds **B-06 (GLOSSARY-GAP tag)** — any performance/capacity NFR without QUPER breakpoints is under-specified.

---

### Ideas 30–50: Splitting Stories + Managing Iterative Delivery

**Idea 30 — Start with the outputs** (Chris Matts principle)
- Core: The value of any IT system is in its OUTPUTS, not its inputs. For rewrites, slice by reports/outputs first, not by data entry screens. "Instead of the log-in screen, think about the reports."
- [ANTI-PATTERN] Legacy rewrite plan that starts with user registration, metadata entry, and data capture — delivering no visible output for months.
- SRS mapping: Skill 05 requirement ordering should prioritize output-producing requirements over input-collecting requirements.

**Idea 31 — Walking skeleton on crutches**
- Core: Extend Cockburn's walking skeleton by delivering UI early on a simplified back-end ("crutches"), then iteratively replacing the back end without changing the UI. Users get value sooner; the team validates UI assumptions before building the real infrastructure.
- Examples: Google Analytics crutch instead of database reporting; JotForm instead of database-backed registration; S3 storage instead of enterprise DMS.

**Idea 32 — Narrow the customer segment**
- Core: Instead of giving everyone 2% of what they need, give 2% of users 100% of what they need. Find a user segment where a significant slice of complexity can be dropped (tax rules for UK-only trades, security for open-source projects, etc.).
- Template dimensions for narrowing: territory, age, technical proficiency, location, occupation, transaction type, department.

**Idea 33 — Split by examples of usefulness**
- Core: For large technical migrations (platform rewrites, database changes), don't slice by technical component — slice by specific examples of how the final result would be useful to someone. Each example that depends only on a small part of the full solution becomes a story.
- MindMup Canvas→SVG example: embedded maps (read-only, no interaction), first-visit experience (small maps, basic functions), CSS styling (low-hanging fruit for opt-in), etc.

**Idea 34 — Split by capacity**
- Core: Deliver the system at a lower capacity first. Lower capacity often requires significantly simpler architecture (no load balancing, no authentication, no clustering). Progressive capacity increase drives progressive architecture improvement.
- Capacity dimensions: file size, session length, number of users, concurrent sessions, number of items per user.

**Idea 35 — Dummy to dynamic**
- Core: Hard-code reference data first (currency lists, country codes, product types), then connect dynamically in a follow-up story. Avoids being blocked on legacy system access during early delivery.
- [ANTI-PATTERN] Blocking a story because the dynamic data source isn't accessible yet.

**Idea 36 — Simplify outputs**
- Core: Save to Excel before saving to the data warehouse. Store plain text before integrating the reporting engine. Skip masking/encryption initially if the risk is manageable for the first limited release.
- Strategies: (1) one format instead of many, (2) insecure storage before secure, (3) transient before persistent, (4) intermediate output before final destination.

**Idea 37 — Split learning from earning**
- Core: Research/investigation stories are LEARNING stories (goal: enough info for a planning decision, time-boxed). Feature delivery stories are EARNING stories (goal: user value).
- Learning story acceptance criteria: what information do stakeholders need to approve next steps? How much time are they willing to invest in getting it?
- [ANTI-PATTERN] "As a developer, I want to understand how the API works" — not a valid user story; should be a time-boxed learning story with a defined information output.
- SRS mapping: Skill 04 (Development Artifacts) should accommodate learning stories as spike records with bounded time and defined information deliverables.

**Idea 38 — Extract basic utility**
- Core: Deliver something that WORKS (can complete the critical task) before making it EASY (usable). Utility before usability. For internal systems only — not suitable for consumer products.
- Strategies: single execution only (no batch), simple text fields (no widgets), manual initiation (no queues).
- CRITICAL: Communicate explicitly to stakeholders that the first cut sacrifices usability. Failure to do so risks contract cancellation (the slot machine example).

**Idea 39 — Slice the hamburger**
- Core: Facilitation technique for all-or-nothing use cases:
  1. List technical components (the "layers" of the hamburger)
  2. Define quality attributes for each component
  3. List options at different quality levels for each component
  4. Remove unsatisfactory options
  5. Remove options that don't create useful technical slices
  6. Choose a vertical slice
- Any vertical cut delivers some value to some users. Each subsequent improvement targets one layer.

**Idea 40 — Don't push everything into stories**
- Core: Infrastructure work, server setup, library upgrades, CI pipeline improvements are NOT user stories. Manage them with a dedicated time budget (e.g., 20% of each sprint), not as fake stories with acceptance criteria.
- [ANTI-PATTERN] "As a QA I want automated log reports" formatted as a user story competing with external-value stories.
- [TEMPLATE-FIELD] Separate `internal_work_budget` at team level, not story-level tracking.

**Idea 41 — Budget instead of estimate**
- Core: Replace "how long will this take?" with "by when do you need it, and what can you afford?" The delivery team then designs a solution to fit those constraints.
- Technique: Extreme-range questions — "What is the least value that would make this worthwhile? What value would make everyone say it was totally worth it?"
- [ANTI-PATTERN] Long-term commitment to scope based on rough story estimates — false precision that eliminates adaptive planning benefit.

**Idea 42 — Avoid numeric story sizes**
- Core: Story points invite misuse for long-term planning and cross-team comparison. Use non-numeric sizes: S/M/L, Goldilocks (too big/just right/too small), or qualitative comparisons to reference stories.
- [ANTI-PATTERN] Adding up story points for release-date predictions without calculating confidence intervals.

**Idea 43 — Estimate capacity by rolling number of stories**
- Core: Use rolling average of similarly-sized stories delivered per iteration (not story points, just count). Valid only for short-term iteration planning, not cross-team comparison or long-term commitment.

**Idea 44 — Estimate capacity based on analysis time**
- Core: Time-box the story discussion session (e.g., 3 hours total, 20 minutes per story, max 2 diverge-merge cycles). Only take into the iteration what you could discuss within the time box.
- Applicability: Works best when business complexity dominates; not applicable when technical complexity dominates.

**Idea 45 — Pick impacts instead of prioritizing stories**
- Core: Business stakeholders pick IMPACTS (the next most important behavior change for a user segment) not individual stories. The delivery team then selects stories that fit the chosen impact and the available budget.
- [ANTI-PATTERN] Flat prioritized backlog where stakeholders rank 50 stories with no impact hierarchy.
- → Directly feeds **W-05 (Cost of Delay prioritization)** — Cost of Delay should be measured at the IMPACT level.

**Idea 46 — Never say "no" — say "not now"**
- Core: Maintain a hierarchical backlog (impact maps or story maps). When a new idea arrives, ask whether it changes the current objective. If not, defer it to the next objective review. If it's truly critical, it replaces the current objective (sprint cancellation level event).
- Governance: Low-friction channel (regular product council) for normal priority changes. High-friction channel (CIO approval or full council vote) for mid-cycle changes.

**Idea 47 — Split UX from consistency work**
- Core: Major UX redesign = learning story (time-boxed research + prototype with mini-team). Consistency maintenance = checklist applied per story by developers with designer periodic reviews.
- [TEMPLATE-FIELD] `ux_checklist_applied: true/false` on delivery stories. Designer maintains the checklist; developers apply it per story.

**Idea 48 — Get end-users to opt in to large UI changes**
- Core: Run old and new interfaces in parallel. Give users a compelling reason to switch first (a single new capability not available in the old UI). Make the switch reversible. Phase out the old interface gradually.
- SRS mapping: For large interface redesigns, plan requirements in two groups: incentive story (the compelling reason to opt in) + migration stories (coverage expansion).

**Idea 49 — Check outcomes with real users**
- Core: There is a difference between software providing the CAPABILITY to do something and users ACTUALLY doing it. After delivery, check that the expected behavior change materialized.
- Write stories that are testable for outcome AFTER delivery: "We will know this worked if [measurable signal observed in production]."
- [TEMPLATE-FIELD] `outcome_check_mechanism` on requirements: specifies how post-delivery success will be measured.
- → Feeds **B-05 (phase gate exit criteria)** — a phase should not close until outcome metrics from the previous phase's requirements have been reviewed.

**Idea 50 — Throw stories away after delivery**
- Core: After a story is delivered, migrate its acceptance criteria to a functional-area-based specification structure. The story itself is discarded. Tests and specs organized by story become a historical record (unusable for understanding current behavior).
- Organization model: Work in progress → organized by story then by function. Delivered functionality → organized by function only.
- Feature maps: hierarchical mind maps of functionality with hyperlinks to current specs.
- → Directly feeds **W-08 and W-09 (defect resolution protocol)** — defects filed against stories after delivery should be re-categorized by functional area.

---

### Summary: User Stories Book — Key Answers to Specified Questions

**Q1. What acceptance criteria format does he recommend?**
GWT scenarios (behavior-focused, assertion-first), written in three-amigos session, organized by functional area. No single acceptance criteria format is mandated — the goal is shared understanding.

**Q2. How does he advise splitting stories?**
8 splitting patterns in order of preference:
1. Narrow customer segment
2. Split by examples of usefulness
3. Split by capacity
4. Start with outputs (slice by deliverable)
5. Dummy to dynamic
6. Simplify outputs
7. Learning from earning (spike)
8. Basic utility (last resort)
Hamburger technique: facilitation tool when other patterns fail.

**Q3. What NFR approach does he recommend?**
- Global concerns as cross-cutting constraints (FURPS+)
- QUPER model for sliding-scale NFRs (utility/differentiation/saturation breakpoints + architectural barriers)
- Defined at milestone/impact level, not story level
- Applied consistently via `[DOMAIN-DEFAULT]` blocks in SRS-Skills

**Q4. How does he handle story dependencies?**
- Hierarchical backlog: impacts → stories → tasks
- Stories should be independent at their own level; dependencies map to impact-level sequencing
- Splitting techniques exist precisely to eliminate dependencies by narrowing scope

**Q5. What does he say about "ready" vs "done"?**
- Ready: three-amigos analysis complete, acceptance criteria clear enough to picture a demonstration, story can be time-boxed
- Done: all GWT scenarios pass AND outcome has been checked with real users (Idea 49)
- "Throw it away": documentation migrated from story-organized to feature-organized

**Q6. Anti-patterns in story writing:**
- "As a user" with no specificity
- Fully specified solution in the "I want" (business decides implementation)
- Requirements in the sphere of influence, not zone of control
- Flat backlog with no impact hierarchy
- Long-term story-point estimates as commitments
- Stories for infrastructure/internal work
- Tests organized by story ticket after delivery

**Q7. How does he map stories to business value?**
Impact mapping (Why→Who→How→What). Stories map to the "What" level. Business value lives at the "Why" level. Pick impacts before picking stories.

**Q8. What elicitation techniques does he recommend?**
- Three amigos (business + developer + tester)
- Diverge and merge (independent generation, then joint synthesis)
- Feedback exercises (Gary Klein alignment check)
- Devil's advocate (challenge user need, segment, and proposed solution)
- Story mapping (Jeff Patton)
- QUPER workshops for NFRs
- CREATE funnel for behavior-change requirements
→ All feed **W-19 (elicitation techniques)**.

---

## SECTION 3: Impact Mapping

### Q1. What are the four levels of an impact map and how are they defined?

**Level 1 — WHY (The Goal)**
- The business objective being pursued. Must be SMART: Specific, Measurable, Action-oriented, Realistic, Timely.
- [ANTI-PATTERN] Vague goal: "improve the website." Specific goal: "increase conversion rate from free to paid by 20% in Q4."
- Positioned at the center of the mind map.
- The WHY must be a business outcome, NOT a software feature. "Launch mobile app" is not a why. "Increase daily active users by 30%" is.

**Level 2 — WHO (The Actors)**
- All actors who can cause or prevent the goal from being reached. Includes: direct users, indirect beneficiaries, adversaries (who might actively prevent the goal), and bystanders (who might be impacted negatively and thus create resistance).
- [ANTI-PATTERN] WHO that lists only direct software users and ignores adversaries and gatekeepers.
- Key question: "Who can help us achieve this goal? Who can block us? Who will be affected?"

**Level 3 — HOW (The Impacts)**
- The behavior changes we want to cause in the actors. How do we need actors to behave differently for the goal to be achieved?
- Impacts are changes to actor behavior, NOT software features. "Customers will invite friends" is an impact. "Add refer-a-friend button" is not.
- [ANTI-PATTERN] HOW level that lists software deliverables rather than actor behavior changes.
- Each WHO should have at least one HOW.

**Level 4 — WHAT (The Deliverables)**
- The software features and other deliverables that will cause the HOW impacts.
- WHAT items are justified by and must trace back to a HOW impact.
- [ANTI-PATTERN] WHAT deliverables with no corresponding HOW (orphaned features that produce no impact).

---

### Q2. How does Impact Mapping relate to requirements/stories?

**Direct mapping to SRS structure:**
- WHY → Section 1.2 Business Goals (Skill 01 vision.md)
- WHO → Section 1.3 Stakeholder Register (Skill 01, W-13)
- HOW → Section 2 System Overview / Functional Context (Skill 03)
- WHAT → Section 3 Functional Requirements (Skill 05)

**Impact Mapping as a backlog filter:**
- A WHAT item with no HOW connection is a candidate for deletion.
- A HOW with no WHAT coverage is a gap.
- A WHAT item that maps to multiple HOWs may be over-valued (or it correctly addresses multiple behavior changes).

**Story-level connection:**
- User stories should map to the WHAT level.
- Impact prioritization: pick the HOW (impact) with highest business leverage, then select WHATs that support it.
- Scope changes: when a new WHAT is proposed, trace it back to a HOW and then to a WHY. If the chain doesn't connect, reject it.

**Scope boundary:** The impact map defines scope. Deliverables not on the map are out of scope. New requirements that can't be traced to a HOW→WHY chain should be challenged.

---

### Q3. How does Adzic define "impact" and distinguish it from "deliverable"?

**Impact:** A change in the behavior of an actor (WHO) that contributes to achieving the business goal (WHY). Impacts exist in the world, not in the software. They describe what people will DO differently.

**Deliverable:** A software feature or artifact that is intended to cause or enable an impact. Deliverables exist in the software, not in the world.

**The critical distinction:** You can build the deliverable perfectly and still fail to achieve the impact (because the impact depends on actor behavior, which is in the sphere of influence, not the zone of control). This is why post-delivery outcome checks (User Stories Book Idea 49) are mandatory.

**Anti-pattern:** Conflating deliverable with impact — "We delivered the feature, therefore we achieved the goal." This is the root cause of the Maslow quality pyramid problem: software that works, works well, is usable, and is even useful — but still fails to be successful because it didn't cause the intended behavior change.

---

### Q4. How does he connect impact mapping to iterative delivery and user stories?

**Three connections:**
1. **Prioritization driver:** Choose the next HOW to target (not the next WHAT). The impact drives the sprint/iteration objective.
2. **Scope management:** Any proposed WHAT that doesn't support the current HOW is deferred until the HOW changes.
3. **Done definition:** The iteration is done when the targeted HOW (behavior change) is measurably occurring, not when the WHAT items are delivered.

**Milestone model:** Each milestone delivers one measurable HOW impact to one clearly defined WHO segment. Not "Feature X and Feature Y are live" but "Segment Z is now doing behavior B at rate R."

---

### Q5. How are impact maps created? (7-Step Process)

**Step 1 — Define the business goal (WHY)**
- Use SMART criteria. Challenge vague goals. If stakeholders can't agree on a SMART goal, the project is not ready to start.
- [ANTI-PATTERN] Proceeding without a SMART goal because "everyone knows what we're doing."

**Step 2 — Define the actors (WHO)**
- Brainstorm all actors using the four categories: direct users, indirect beneficiaries, adversaries, bystanders.
- Don't forget non-human actors: time, external systems, market forces.

**Step 3 — Define the impacts (HOW)**
- For each actor, ask: "How does this actor's behavior need to change for us to achieve the WHY?"
- Also ask: "What behavior from this actor would block the WHY?"
- Impacts should be verifiable behavior changes, not feelings or attitudes.

**Step 4 — Define the deliverables (WHAT)**
- For each HOW, brainstorm software and non-software deliverables that could cause that impact.
- Non-software deliverables are valid: training, process changes, pricing changes, partnerships.

**Step 5 — Fit the measurements**
- For each HOW, define how you will know the impact has occurred. What is the measurable signal?
- Without measurements, the impact map is a picture, not a plan.

**Step 6 — Prioritize**
- Pick the WHOs and HOWs with the highest leverage relative to the WHY.
- Discard or defer low-leverage HOWs and their associated WHATs.

**Step 7 — Rinse and repeat**
- After each delivery milestone, revisit the impact map. Check which HOWs have materialized. Update the map to reflect new learning. Add or remove branches as the business context changes.

---

### Q6. How does Impact Mapping handle scope management?

**Scope is defined by the HOW level, not the WHAT level.**
- Adding a feature (WHAT) expands scope only if it maps to a new HOW.
- If a new WHAT supports an existing HOW more efficiently than the current planned WHAT, it replaces (not adds to) the scope.
- [ANTI-PATTERN] Scope defined as a list of features (WHATs) with no connection to HOW or WHY — any new feature request then appears to be "additional scope" rather than a replacement.

**The minimal scope principle:** Deliver the minimum WHATs needed to cause the targeted HOW impacts. Everything beyond that is gold-plating or premature optimization.

**Scope reduction trigger:** If the HOW (impact) materializes before all planned WHATs are delivered, stop. The goal has been achieved with less effort than planned.

---

### Q7. What anti-patterns does Adzic identify in impact mapping?

1. **[ANTI-PATTERN] WHY as a feature:** "Launch mobile app" instead of "Increase DAU by 30%." Feature launch is not a business goal.
2. **[ANTI-PATTERN] HOW as features:** "Add refer-a-friend button" at the HOW level — should be "customers will invite friends."
3. **[ANTI-PATTERN] Orphaned WHATs:** Deliverables that don't map to any HOW. These should be eliminated.
4. **[ANTI-PATTERN] Single-actor maps:** Maps that only show direct users, missing adversaries and gatekeepers.
5. **[ANTI-PATTERN] Immutable maps:** Treating the impact map as a contract rather than a living plan. Maps should be updated after every milestone.
6. **[ANTI-PATTERN] Unmeasured impacts:** HOWs without a measurement mechanism are aspirations, not plans.
7. **[ANTI-PATTERN] Feature-level prioritization:** Prioritizing the WHAT backlog without first agreeing on the HOW priority.
8. **[ANTI-PATTERN] Big bang delivery:** Planning to deliver all WHATs before checking whether any HOWs have materialized.

---

### Q8. How does Impact Mapping connect to stakeholder communication?

**Three key stakeholder roles (Part II of the book):**
1. **The visionary:** Holds the WHY. Responsible for SMART goal definition. Must be accessible during delivery to adjust the WHY if market conditions change.
2. **The business analyst/product owner:** Holds the WHO and HOW levels. Responsible for maintaining the map, prioritizing impacts, and connecting delivery to business outcomes.
3. **The delivery team:** Holds the WHAT level. Responsible for proposing, building, and measuring the WHATs that cause the targeted HOWs.

**Stakeholder communication principle:** Business stakeholders should only be asked to make decisions at the WHY and HOW levels. Decisions at the WHAT level belong to the delivery team (unless WHAT choices have significant business trade-offs).

**Investment framing (not cost framing):** Present the impact map as an investment portfolio. Each HOW branch is a potential investment. Stakeholders choose which investments to fund based on expected return (WHY achievement).

**Meeting structure using impact maps:**
- Map walks: walk each branch of the map to check alignment. High disagreement on a branch = misalignment that must be resolved before delivery.
- Milestone reviews: show which HOW branches have materialized. Show evidence (measurements). Discuss which branch to target next.

---

### Q9. What templates does Impact Mapping provide?

**Core impact map structure (mind map):**
```
[WHY: SMART business goal]
  └── [WHO: Actor 1]
  │     └── [HOW: Behavior change 1]
  │     │     └── [WHAT: Deliverable A]
  │     │     └── [WHAT: Deliverable B]
  │     └── [HOW: Behavior change 2]
  │           └── [WHAT: Deliverable C]
  └── [WHO: Actor 2]
        └── [HOW: Behavior change 3]
              └── [WHAT: Deliverable D]
```

**Measurement table (fits alongside the map):**
```
HOW (Impact) | Success indicator | Measurement mechanism | Baseline | Target
```

**Investment framing template:**
```
WHY (goal): [SMART statement]
Current investment: [time + cost to date]
Expected return: [measurable business outcome]
Next milestone: [WHO segment + HOW impact + target date]
Evidence of progress: [current measurements]
```

---

## Cross-Cutting Summary: Improvements Mapped to Pending Work Items

### B-03: VERIFIABILITY-FAIL tag
**Sources:** Tests Book Ideas 5, 10, 15; User Stories Book Idea 7
- A requirement is VERIFIABILITY-FAIL when: (a) no boundary conditions are defined for numeric/date inputs; (b) the Then clause is too vague to generate a pass/fail test; (c) the requirement is in the sphere of influence, not zone of control; (d) no measurement mechanism exists for an impact-level requirement.
- Tag format: `[V&V-FAIL: verifiability — {reason}: {remedy}]`
- Reasons: missing-boundary | vague-assertion | uncontrolled-outcome | no-measurement-mechanism

### B-05: Phase gate exit criteria
**Sources:** Tests Book Idea 45 (test half-life); User Stories Book Ideas 5, 19, 21, 49; Impact Mapping Steps 5 and 7
- Phase gates should require: (a) all acceptance scenarios passing; (b) outcome check initiated (production measurement mechanism in place); (c) test suite half-life above threshold (not declining); (d) impact map updated to reflect actual materialized HOWs.
- Exit criteria template: `✓ All GWT scenarios pass | ✓ Outcome measurement deployed | ✓ Impact map updated | ✓ Test half-life ≥ N days`

### B-06: GLOSSARY-GAP tag
**Sources:** User Stories Book Idea 14 (FURPS+), Idea 29 (QUPER); Impact Mapping measurement step
- Tag any NFR term used without an IEEE 982.1 metric AND without a QUPER breakpoint definition.
- Tag format: `[CONTEXT-GAP: glossary — {term} lacks metric definition; add QUPER breakpoints: utility | differentiation | saturation]`

### W-03: Inline GWT stubs
**Sources:** Tests Book — canonical GWT definition, Ideas 1, 10, 14, 23
- GWT stubs should enforce: single When; passive-voice Given; observable Then; one scenario per behavior.
- Stub template to inject into Skill 05 output:
  ```
  Given [precondition in past/passive voice]
  When [single triggering action in present active voice]
  Then [observable outcome in future passive voice]
  [boundary_conditions: ]
  [test_data_strategy: ]
  [observability_mechanism: ]
  ```

### B-07: AUDIENCE role tags
**Sources:** Tests Book Idea 6 (personas); User Stories Book Ideas 3, 6, 17, 26
- Tag each requirement with the actor persona from the stakeholder register.
- Format: `[AUDIENCE: {persona_name} | influence: {H/M/L} | interest: {H/M/L}]`
- Sources of personas: `_context/stakeholders.md` stakeholder chart.

### W-08 / W-09: Defect resolution protocol
**Sources:** User Stories Book Idea 50 (throw stories away); Tests Book Idea 40 (organize by functional area)
- Post-delivery defects should be filed against FUNCTIONAL AREAS, not against stories.
- Resolution protocol: (1) identify functional area, (2) check existing GWT scenarios for coverage, (3) if no scenario covers the defect, write a new GWT scenario FIRST (test-first), (4) fix the defect, (5) re-file the test under the functional area.
- [ANTI-PATTERN] Defect linked to a closed story ticket as its only specification reference.

### W-13: Stakeholder register upgrade
**Sources:** User Stories Book Idea 17 (stakeholder chart); Impact Mapping WHO level (adversaries, bystanders)
- Upgrade `_context/stakeholders.md` to include: `name | role | influence_level (H/M/L) | interest_level (H/M/L) | engagement_strategy | impact_map_role (visionary/analyst/delivery/adversary/bystander) | HOW_impacts_affected`

### W-19: Elicitation techniques
**Sources:** User Stories Book Ideas 22, 23, 24, 25; Impact Mapping creation process
- Document elicitation sessions in `_context/elicitation_log.md` using:
  - Session type: three-amigos | diverge-merge | feedback-exercise | devil's-advocate | QUPER-workshop | impact-mapping-session
  - Participants and roles
  - Key decisions reached
  - Open questions remaining (→ CONTEXT-GAP flags)
  - Alignment score (from feedback exercise if conducted)

### W-05: Cost of Delay prioritization
**Sources:** User Stories Book Ideas 10, 11, 15, 16, 45; Impact Mapping priority step
- Cost of Delay should be estimated at the HOW (impact) level, not the WHAT (story) level.
- Use QUPER differentiation point as a proxy for competitive urgency (before differentiation point, delays are costly; after saturation point, delays are irrelevant).
- Purpose Alignment Model (differentiating/parity/partner/none) as a priority filter.
- Lean Analytics stage as a maturity filter (empathy/stickiness/virality/revenue/scale).

---

*End of analysis. All 50 ideas from each of the two "Fifty Quick Ideas" books have been extracted. The full Impact Mapping framework has been documented. Cross-references to SRS-Skills pending improvements (B-03, B-05, B-06, W-03, W-08, W-09, W-13, W-19, W-05, B-07) are embedded throughout.*
