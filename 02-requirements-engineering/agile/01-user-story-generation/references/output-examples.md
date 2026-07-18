# User-story output examples

Parent: [User Story Generation](../SKILL.md)

## Output Format Specification

### File: `projects/<ProjectName>/<phase>/<document>/user_stories.md`

```markdown
# User Story Backlog: [Project Name]

**Generated:** [Date]
**Methodology:** Agile (Scrum)
**Standards:** IEEE 29148-2018, INVEST Criteria

---

## Backlog Overview

| Metric | Value |
|--------|-------|
| Total Stories | 45 |
| Total Story Points | 187 |
| Epics | 6 |
| Critical Priority | 12 stories (63 points) |
| High Priority | 18 stories (89 points) |
| Medium Priority | 10 stories (28 points) |
| Low Priority | 5 stories (7 points) |

---

## Epic 1: User Management (25 points)

### US-001: User Registration

**As a** new customer
**I want to** create an account with email and password
**So that** I can access personalized features

**Acceptance Criteria:**
- [ ] Given I am on the registration page
      When I enter a valid email and password (min 8 chars)
      Then my account is created and I receive a confirmation email
- [ ] Given I enter an already-registered email
      When I attempt to register
      Then I see an error: "Email already in use"
- [ ] Given I enter an invalid email format
      When I attempt to register
      Then I see inline validation error before submission

**Story Points:** 3
**Priority:** Critical
**Epic:** User Management
**Dependencies:** None
**Tags:** #authentication #mvp #sprint-1

**Technical Notes:**
- Use bcrypt for password hashing (from quality_standards.md)
- Email verification via SendGrid API
- Store user in `users` table with unique email constraint

---

### US-002: User Login

[... similar format ...]

---

## Epic 2: Product Catalog (58 points)

[... continue for all epics ...]

---

## Appendix A: INVEST Compliance Report

All stories validated against INVEST criteria. No failures detected.

## Appendix B: Story Point Distribution

[Chart showing Fibonacci distribution of story points]

## Appendix C: Personas Reference

[Link to projects/<ProjectName>/_context/personas.md]
```

### File: `projects/<ProjectName>/<phase>/<document>/backlog_summary.md`

```markdown
# Backlog Summary

**Project:** [Name]
**Generated:** [Date]
**Total Estimated Effort:** 187 story points (~9.4 sprints @ 20 points/sprint)

## Sprint Recommendations

### Sprint 1 (MVP Foundation) - 20 points
- US-001: User Registration (3 pts)
- US-002: User Login (2 pts)
- US-005: Browse Products (5 pts)
- US-010: Shopping Cart (8 pts)
- US-015: Basic Checkout (2 pts)

### Sprint 2 (MVP Completion) - 21 points
[... continue ...]

## Risk Assessment

| Risk | Stories Affected | Mitigation |
|------|------------------|------------|
| Payment Gateway Integration | US-018, US-019 | Spike story in Sprint 1 to prototype |
| Performance (<200ms target) | US-005, US-006 | Load testing after Sprint 2 |

## Dependencies Graph

[Mermaid diagram showing story dependencies]
```

## Resources

- **[templates/personas.md.template](templates/personas.md.template)**: Persona definition template
- **[templates/user_story.md.template](templates/user_story.md.template)**: Single story template
- **[references/invest-criteria.md](references/invest-criteria.md)**: Detailed INVEST validation guide
- **[references/story-estimation-guide.md](references/story-estimation-guide.md)**: Story point calibration examples
- **[examples/sample-backlog.md](examples/sample-backlog.md)**: Complete example backlog

## Example: Before vs. After

### Before (from features.md)

```markdown
## Feature: User Management
Allow users to create accounts, log in, and manage their profiles.
```

### After (Generated User Stories)

```markdown
### US-001: User Registration
**As a** new customer
**I want to** create an account with email and password
**So that** I can access personalized recommendations

**Acceptance Criteria:**
- [ ] Given I am on registration page, When I enter valid email/password, Then account is created
- [ ] Given I use weak password, When I submit, Then I see validation error
- [ ] Given I use existing email, When I submit, Then I see "Email already registered"

**Story Points:** 3 | **Priority:** Critical | **Epic:** User Management

---

### US-002: User Login
[... similar format ...]

---

### US-003: Password Reset
[... similar format ...]

---

### US-004: Profile Management
[... similar format ...]
```
