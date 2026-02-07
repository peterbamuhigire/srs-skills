# INVEST Criteria Validation Guide

**Purpose:** Ensure every user story is well-formed and ready for sprint planning.

INVEST is a mnemonic created by Bill Wake (2003) to evaluate user story quality:

- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

---

## I - Independent

### Definition
Stories should be **self-contained** and completable without strict dependency on other stories.

### Why It Matters
- Enables flexible sprint planning (reorder backlog without breaking dependencies)
- Reduces delays (no blocking waiting for other teams/stories)
- Improves parallelization (multiple developers can work simultaneously)

### Good Example ✅
```markdown
US-101: User Registration
US-102: User Login
US-103: Password Reset
```
Each can be developed independently.

### Bad Example ❌
```markdown
US-201: Create database schema
US-202: Build user registration (DEPENDS on US-201)
US-203: Add email validation (DEPENDS on US-202)
```
These are tightly coupled. US-203 can't start until US-201 and US-202 are done.

### How to Fix
1. **Merge dependent stories**: Combine US-201 + US-202 into one story
2. **Reorder**: Make foundational work (DB schema) part of sprint 0 setup
3. **Abstract dependencies**: Use interfaces/mocks to decouple implementation

### Exceptions
Some dependencies are unavoidable (e.g., "Login" requires "Registration"). Document them clearly but minimize cascading dependencies.

---

## N - Negotiable

### Definition
Stories describe **outcomes, not implementations**. The "how" should be negotiable during sprint planning.

### Why It Matters
- Empowers developers to choose best technical approach
- Allows flexibility if constraints change
- Encourages collaboration between PO and dev team

### Good Example ✅
```markdown
**As a** customer
**I want to** reset my password if I forget it
**So that** I can regain access to my account
```
Leaves room to choose: email link, SMS code, security questions, etc.

### Bad Example ❌
```markdown
**As a** customer
**I want to** receive a 6-digit SMS code to reset my password
**So that** I can regain access
```
Prescribes the implementation (SMS). What if SMS is expensive or unreliable?

### How to Fix
- Focus on **user needs**, not technical solutions
- Move implementation details to **acceptance criteria** as options
- Allow team to propose alternatives during planning

### Revised Example ✅
```markdown
**As a** customer
**I want to** securely reset my password
**So that** I can regain access without contacting support

**Acceptance Criteria:**
- Password reset is secure (multi-factor verification)
- User receives reset instructions within 5 minutes
- Reset link expires after 24 hours

**Technical Options (for team discussion):**
- Email link (cheapest, most common)
- SMS code (faster, requires phone number)
- Security questions (no external dependency)
```

---

## V - Valuable

### Definition
Every story must deliver **measurable value** to users or the business.

### Why It Matters
- Prevents "nice-to-have" features that waste effort
- Ensures backlog items tie to business goals
- Justifies prioritization decisions

### Good Example ✅
```markdown
**As a** store owner
**I want to** see daily sales reports
**So that** I can identify slow-moving inventory and adjust pricing

**Business Value:** Reduces inventory holding costs by 15% (per vision.md goal)
```

### Bad Example ❌
```markdown
**As a** developer
**I want to** refactor the codebase to use TypeScript
**So that** the code is more maintainable
```
This is valuable to **developers**, not users. Should be a **technical task**, not a user story.

### How to Fix
- Ask: "Would a user/customer pay for this feature?"
- Tie every story to a **business metric** (revenue, retention, cost reduction)
- Technical work should be **technical tasks** (not user stories) or embedded in feature stories

### Example: Embedding Technical Work ✅
```markdown
**As a** customer
**I want to** receive real-time order updates
**So that** I know exactly when my package will arrive

**Technical Tasks:**
- Refactor notification service to support WebSockets
- Add TypeScript types for event payloads
```

---

## E - Estimable

### Definition
The team must be able to **estimate effort** (story points or time) with reasonable confidence.

### Why It Matters
- Enables sprint planning (can we fit this in the sprint?)
- Identifies unclear requirements (if team can't estimate, story is too vague)
- Helps predict release dates

### Good Example ✅
```markdown
**As a** customer
**I want to** filter products by price range ($0-$50, $50-$100, etc.)
**So that** I can find affordable options quickly

**Acceptance Criteria:**
- Price filter appears in sidebar
- Selecting a range updates product list in <1 second
- Filter persists across page navigation

**Estimate:** 5 story points (clear scope, known tech stack)
```

### Bad Example ❌
```markdown
**As a** customer
**I want to** have a great shopping experience
**So that** I enjoy using the app
```
Too vague to estimate. What is "great"? What features are included?

### How to Fix
- **Add specificity**: Break down vague goals into concrete features
- **Provide context**: Link to mockups, technical specs, or similar features
- **Remove unknowns**: Spike stories for research before estimating

### Example: Using Spike Stories
```markdown
**Spike:** Research payment gateway options (Stripe vs. PayPal)
**Time-box:** 4 hours
**Output:** Decision document with cost/complexity comparison

**Then estimate:**
US-301: Integrate [chosen gateway] for checkout (5 points)
```

---

## S - Small

### Definition
Stories should be **small enough to complete within one sprint** (typically 1-2 weeks).

### Why It Matters
- Reduces risk (large stories are unpredictable)
- Enables faster feedback (demo at end of sprint)
- Improves accuracy (small estimates are more reliable)

### Rule of Thumb
- **1-3 story points:** Ideal (fits in sprint with buffer)
- **5-8 story points:** Acceptable (needs careful planning)
- **13+ story points:** Too large (split into smaller stories)

### Good Example ✅
```markdown
US-401: Display product reviews (3 points)
US-402: Add review submission form (5 points)
US-403: Implement review moderation (8 points)
```
Each fits in one sprint.

### Bad Example ❌
```markdown
US-501: Build complete review system (21 points)
```
This is an **epic**, not a story. Takes multiple sprints.

### How to Fix: Vertical Slicing
Split by **end-to-end functionality**, not technical layers.

**Bad (Horizontal Slicing):** ❌
- US-501a: Create review database schema
- US-501b: Build review API
- US-501c: Create review UI

No user value until all 3 are done.

**Good (Vertical Slicing):** ✅
- US-401: Display existing reviews (read-only) → **User can see reviews**
- US-402: Submit new review → **User can leave feedback**
- US-403: Moderate reviews → **Admin can filter spam**

Each delivers incremental value.

---

## T - Testable

### Definition
Every story must have **clear, verifiable acceptance criteria** with pass/fail outcomes.

### Why It Matters
- Prevents misunderstandings ("done" means different things to PO vs. dev)
- Enables automated testing (QA can write tests from criteria)
- Provides Definition of Done for the story

### Good Example ✅
```markdown
**As a** customer
**I want to** search products by keyword
**So that** I can find items quickly

**Acceptance Criteria:**
- [ ] Given I enter "laptop" in search box, When I press Enter, Then I see all products containing "laptop" in title/description
- [ ] Given I enter "xyz123nonexistent", When I search, Then I see "No results found"
- [ ] Given search returns >50 results, When I scroll to bottom, Then next 50 results load (pagination)
- [ ] Performance: Search completes in <500ms for 95% of queries (testable via load testing)
```

### Bad Example ❌
```markdown
**Acceptance Criteria:**
- Search works correctly
- Results are relevant
- Performance is good
```
Not testable. What does "correctly" mean? What is "good" performance?

### How to Fix: Use Given-When-Then Format
```
Given [precondition/context]
When [action/trigger]
Then [expected outcome]
```

**Example:**
```markdown
- [ ] Given I am a logged-in user
      When I click "Add to Cart"
      Then the cart icon shows updated count
- [ ] Given my cart has 5 items
      When I remove 1 item
      Then the count decreases to 4
```

### Non-Functional Testability
For NFRs (performance, security, usability):

```markdown
**Performance:**
- [ ] API response time <200ms (95th percentile) → Testable via load testing tools

**Security:**
- [ ] Passwords hashed with bcrypt → Testable via code review + penetration test

**Usability:**
- [ ] Checkout completes in <3 clicks → Testable via user testing sessions
```

---

## INVEST Validation Checklist

Use this checklist for every user story:

- [ ] **Independent:** Can this story be completed without blocking on others?
- [ ] **Negotiable:** Does it describe outcome, not implementation?
- [ ] **Valuable:** Does it deliver measurable value to users/business?
- [ ] **Estimable:** Can the team estimate it with confidence?
- [ ] **Small:** Can it be completed in one sprint?
- [ ] **Testable:** Are acceptance criteria clear and verifiable?

**Scoring:**
- 6/6 ✅ Ready for sprint planning
- 4-5/6 ⚠️ Needs refinement
- <4/6 ❌ Return to backlog, rework before planning

---

## Common INVEST Failures & Fixes

### Failure 1: Epic Disguised as Story
**Problem:** Story is too large (>13 points)
**Fix:** Split using vertical slicing (see "S - Small" section)

### Failure 2: Technical Task Disguised as Story
**Problem:** No user value (e.g., "Refactor database schema")
**Fix:** Convert to technical task under a related feature story

### Failure 3: Vague Acceptance Criteria
**Problem:** Criteria like "works correctly" or "is fast"
**Fix:** Use Given-When-Then format with measurable outcomes

### Failure 4: Too Many Dependencies
**Problem:** Story blocked by 3+ other stories
**Fix:** Merge dependent stories or use mocks/stubs to decouple

### Failure 5: Implementation Details in Story
**Problem:** Story prescribes specific technology (e.g., "Use React hooks")
**Fix:** Move tech details to acceptance criteria as constraints, not requirements

---

## Example: Story Refinement Using INVEST

### Original Story (Poor INVEST Compliance)
```markdown
**As a** user
**I want to** have authentication
**So that** the system is secure

**Acceptance Criteria:**
- Login works
- Users can register
```

**INVEST Score:** 2/6 ❌
- ❌ Independent: Combines login + registration (should be separate)
- ❌ Negotiable: Too vague
- ❌ Valuable: No clear user benefit
- ❌ Estimable: Can't estimate without more detail
- ❌ Small: Too large (covers multiple features)
- ❌ Testable: "Login works" is not specific

### Refined Stories (INVEST Compliant)

#### Story 1: User Registration
```markdown
**As a** new customer
**I want to** create an account with email and password
**So that** I can save my preferences and order history

**Acceptance Criteria:**
- [ ] Given I am on registration page, When I enter valid email/password (min 8 chars), Then account is created
- [ ] Given I enter weak password (<8 chars), When I submit, Then I see error: "Password must be at least 8 characters"
- [ ] Given I use existing email, When I submit, Then I see error: "Email already registered"
- [ ] Given successful registration, When account is created, Then I receive confirmation email within 5 minutes

**Story Points:** 3
**Priority:** Critical
```

**INVEST Score:** 6/6 ✅

#### Story 2: User Login
```markdown
**As a** registered customer
**I want to** log in with my email and password
**So that** I can access my account

**Acceptance Criteria:**
- [ ] Given I enter correct credentials, When I submit, Then I am redirected to dashboard
- [ ] Given I enter wrong password, When I submit, Then I see error: "Invalid credentials"
- [ ] Given I enter unregistered email, When I submit, Then I see error: "No account found"
- [ ] Given 3 failed login attempts, When I try 4th time, Then account is locked for 15 minutes

**Story Points:** 2
**Priority:** Critical
**Dependencies:** US-001 (Registration must exist first)
```

**INVEST Score:** 6/6 ✅

---

## References

- **Bill Wake (2003):** "INVEST in Good Stories, and SMART Tasks"
- **IEEE Std 29148-2018:** Requirements Engineering (Section 6.4.5)
- **Mike Cohn (2004):** "User Stories Applied"
- **Agile Alliance:** User Story Standards

---

**Last Updated:** 2026-02-07
