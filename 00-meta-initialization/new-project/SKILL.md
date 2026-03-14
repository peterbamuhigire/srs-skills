# Skill: New Project Scaffold

## Trigger
User says any of: "start a new project", "create a new project",
"scaffold a project", "new client project", "initialize project"

## MANDATORY FIRST STEP
Before anything else, invoke `superpowers:brainstorming` to explore the project
intent, requirements, and design. Do NOT skip this step. Do NOT ask clarifying
questions before invoking brainstorming.

---

## How to Use the SRS-Skills Engine (PRIME Workflow)

Every skill in this engine follows the **PRIME methodology** (Kodukula & Vinueza, 2024):

| Step | What the Consultant Does | SRS-Skills Equivalent |
|------|--------------------------|----------------------|
| **P — Prepare** | Gather all project data before prompting | Populate `_context/` files with real stakeholder data, not placeholders |
| **R — Relay** | Submit the prompt with precise instructions | Invoke the SKILL.md (tell Claude: "Run the [skill name] skill") |
| **I — Inspect** | Critically evaluate AI output against objectives | Read the generated document; check it against `_context/` source files |
| **M — Modify** | Refine if output diverges from expectations | Edit the output or update `_context/` and re-invoke the skill |
| **E — Execute** | Approve and build the final artifact | Run `build-doc.sh` to produce the `.docx` |

> **Quality rule:** Never execute (build the `.docx`) without completing Inspect and Modify. The first AI output is a draft, not a deliverable.

The `_context/` directory is the **Project Input Folder (PIF)** for this project — a living repository of project-specific context that feeds every skill. The richer the PIF, the higher the quality of every generated document (Kodukula & Vinueza, 2024).

---

## Interview Protocol

After brainstorming, ask these questions ONE AT A TIME. Do not ask the next until
the previous is answered.

**Q1:** What is the project name? (This becomes the directory name — use hyphens,
e.g., `Livecare-Hospital-ERP`)

**Q2:** In 2–3 sentences, what does this software do and what problem does it solve?
(This pre-populates `_context/vision.md` and is used to deduce the domain)

**Q3:** Which methodology best fits this project?
- A) **Waterfall** — regulated industry, fixed scope, formal IEEE 830 SRS required
- B) **Agile** — iterative delivery, user stories, Scrum/Kanban
- C) **Hybrid** — formal SRS for backend/core + agile user stories for frontend/features

**Q4:** Who is the project owner / primary client contact name?

---

## Domain Deduction (NO USER INPUT REQUIRED)

After Q2, Claude analyses the project description and deduces the domain automatically
using these signals:

| If description mentions... | Deduce domain |
|---|---|
| patients, hospitals, clinics, EMR, EHR, PHI, medical, healthcare, pharmacy, nursing | `healthcare` |
| banking, payments, ledger, transactions, trading, insurance, loans, fintech, accounting | `finance` |
| students, courses, LMS, grades, enrollment, university, school, e-learning | `education` |
| inventory, POS, e-commerce, retail, products, orders, cart, warehouse (retail context) | `retail` |
| fleet, shipments, tracking, logistics, freight, warehouse (supply chain), delivery, routing | `logistics` |
| government, citizens, public services, procurement, permits, case management, municipal | `government` |

**If ambiguous (two domains equally match):** Ask the user during the brainstorming
session — e.g., "This sounds like it could be healthcare OR government — which primary
domain applies?"

**If no domain matches:** Use `other` — no domain defaults are injected; scaffold
only the directory structure and empty context files.

---

## Scaffold Actions

After the interview, Claude performs these actions in order:

### 1. Create project root
`projects/<ProjectName>/`

### 2. Create `_context/` files

**`_context/vision.md`** — pre-populate with Q2 answer:
```markdown
# Project Vision

**Project:** <ProjectName>
**Client Contact:** <Q4 answer>
**Date:** <today's date>

## Problem Statement
<Q2 answer>

## Goals
<!-- TODO: List 3–5 measurable project goals -->

## Stakeholders
<!-- TODO: List stakeholder roles and their primary needs -->

## Success Criteria
<!-- TODO: Define how project success will be measured -->
```

**`_context/features.md`** — stub with guidance:
```markdown
# Feature List

<!-- TODO: List all features with a brief description each.
Format:
## Feature Name
Brief description of what this feature does and the business value it delivers.
-->
```

**`_context/tech_stack.md`**:
```markdown
# Technology Stack

<!-- TODO: Specify the technologies, frameworks, and infrastructure.
Example:
- Backend: PHP 8.2 / Laravel 10
- Frontend: React 18 / TypeScript
- Database: MySQL 8.0
- Infrastructure: AWS EC2, S3, RDS
-->
```

**`_context/business_rules.md`**:
```markdown
# Business Rules

<!-- TODO: Define the domain-specific rules and constraints.
Example:
- A patient cannot have more than one active appointment per time slot
- Invoices cannot be deleted after 30 days
-->
```

**`_context/quality_standards.md`**:
```markdown
# Quality Standards

<!-- TODO: Define measurable quality targets.
Example:
- Response time: 95th percentile < 500ms under 1,000 concurrent users
- Uptime: 99.9% monthly
- Security: OWASP Top 10 compliance
-->
```

**`_context/glossary.md`**:
```markdown
# Glossary

<!-- TODO: Define project-specific terms using IEEE 610.12-1990 format.
Format:
**Term:** Definition
-->
```

**`_context/stakeholders.md`**:
```markdown
# Stakeholders

<!-- TODO: List all stakeholder groups. Required by Phase 01 skills (Vision Statement, PRD, Business Case).
Format:
## Role Title
- **Influence:** High / Medium / Low
- **Interest:** High / Medium / Low
- **Primary Needs:** What this stakeholder needs from the system
- **Key Concerns:** Risks or constraints they care about
- **Communication Preference:** How and how often to communicate
-->
```

**`_context/personas.md`**:
```markdown
# User Personas

<!-- TODO: Define user personas for the system. Required by Phase 02 Agile user story generation.
Format:
## Persona Name (Role)
- **Age / Background:** Brief demographic context
- **Goals:** What they are trying to accomplish
- **Pain Points:** Current frustrations this system should solve
- **Tech Comfort:** Low / Medium / High
- **Typical Workflow:** Step-by-step description of how they currently do the task
-->
```

**`_context/domain.md`** — copy content from `domains/<deduced-domain>/INDEX.md`
and prepend:
```markdown
# Domain Profile: <DomainName>
> Auto-populated from domains/<domain>/INDEX.md at scaffold time.
> Domain deduced from project description. Review and remove sections not applicable.
```

If domain is `other`, create:
```markdown
# Domain Profile: Other / Custom
> No standard domain matched. Define domain-specific requirements manually.
```

### 3. Create Phase Directories

Create all 9 phase directories with document subdirectories based on methodology:

**Waterfall methodology** — create all document dirs across all phases.
**Agile methodology** — skip `01-srs/` in Phase 02; create `02-user-stories/` instead.
**Hybrid** — create both `01-srs/` and `02-user-stories/` in Phase 02.

Phase directory → document subdirectories mapping:

```
01-strategic-vision/         → 01-prd/, 02-vision-statement/, 03-business-case/
02-requirements-engineering/ → 01-srs/ and/or 02-user-stories/, 03-stakeholder-analysis/
03-design-documentation/     → 01-hld/, 02-lld/, 03-api-spec/, 04-database-design/, 05-ux-spec/
04-development-artifacts/    → 01-technical-spec/, 02-coding-guidelines/
05-testing-documentation/    → 01-test-strategy/, 02-test-plan/, 03-test-report/
06-deployment-operations/    → 01-deployment-guide/, 02-runbook/
07-agile-artifacts/          → 01-sprint-planning/, 02-dod/, 03-dor/
08-end-user-documentation/   → 01-user-manual/, 02-installation-guide/, 03-faq/
09-governance-compliance/    → 01-traceability-matrix/, 02-audit-report/, 03-compliance/, 04-risk-assessment/
```

### 3b. Create `manifest.md` Stubs

For each document subdirectory created above, also create a `manifest.md` file with this template:

```markdown
# Document Manifest
# List section files in assembly order, one per line.
# Lines starting with # are comments and are excluded from the build.
# If this file is absent, build-doc.sh sorts *.md files alphabetically.
#
# Example:
# 01-introduction.md
# 02-scope.md
# 03-requirements.md
```

This file is empty by default. Claude will populate it with the correct section order when generating sections for this document.

### 4. Inject Domain Defaults

If domain is not `other`:
- Read `domains/<domain>/references/nfr-defaults.md`
- Copy all `[DOMAIN-DEFAULT]` blocks into:
  - `02-requirements-engineering/01-srs/06-nfr.md` (waterfall/hybrid)
  - `02-requirements-engineering/02-user-stories/01-epics.md` (agile/hybrid — as tagged notes)

### 5. Print Scaffold Summary

```
Project scaffolded: projects/<ProjectName>/

Domain deduced: <domain> (from project description)

_context/ status:
  ✓ vision.md            — pre-populated from interview
  ✓ domain.md            — <domain> baseline injected
  ○ features.md          — TODO: add feature list
  ○ tech_stack.md        — TODO: specify technologies
  ○ business_rules.md    — TODO: define business rules
  ○ quality_standards.md — TODO: set quality targets
  ○ glossary.md          — TODO: add project terminology
  ○ stakeholders.md     — TODO: add stakeholder register (required by Phase 01)
  ○ personas.md         — TODO: define user personas (required by Phase 02 Agile)

Domain defaults injected: <N> [DOMAIN-DEFAULT] requirements
  → 02-requirements-engineering/01-srs/06-nfr.md

Next step: Fill in _context/ files, then say:
  "generate PRD for <ProjectName>"
  "generate SRS for <ProjectName>"
```

---

## Build Document Protocol

When user says "build the [document]" (e.g., "build the SRS", "build the PRD"):

1. Resolve the document directory from the document name using the table below
2. Check for `manifest.md` — if present use it; otherwise sort `*.md` by filename
3. Run: `bash scripts/build-doc.sh <doc-dir> <OutputName>`
4. Report the output path to the user

### Document Name → Directory Mapping

| User says | Directory | Output filename |
|---|---|---|
| "build the PRD" | `01-strategic-vision/01-prd/` | `PRD.docx` |
| "build the vision statement" | `01-strategic-vision/02-vision-statement/` | `VisionStatement.docx` |
| "build the business case" | `01-strategic-vision/03-business-case/` | `BusinessCase.docx` |
| "build the SRS" | `02-requirements-engineering/01-srs/` | `SRS_Draft.docx` |
| "build the user stories" | `02-requirements-engineering/02-user-stories/` | `UserStories.docx` |
| "build the HLD" | `03-design-documentation/01-hld/` | `HLD.docx` |
| "build the LLD" | `03-design-documentation/02-lld/` | `LLD.docx` |
| "build the API spec" | `03-design-documentation/03-api-spec/` | `APISpec.docx` |
| "build the database design" | `03-design-documentation/04-database-design/` | `DatabaseDesign.docx` |
| "build the test plan" | `05-testing-documentation/02-test-plan/` | `TestPlan.docx` |
| "build the deployment guide" | `06-deployment-operations/01-deployment-guide/` | `DeploymentGuide.docx` |
| "build the user manual" | `08-end-user-documentation/01-user-manual/` | `UserManual.docx` |
| "build the risk assessment" | `09-governance-compliance/04-risk-assessment/` | `RiskAssessment.docx` |
| "build the traceability matrix" | `09-governance-compliance/01-traceability-matrix/` | `TraceabilityMatrix.docx` |
