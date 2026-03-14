# Recommendations
**Review Date:** 2026-03-14

---

## Section A: Critical Fixes (Must Fix Before Real Consulting Use)

### A-1: Add `stakeholders.md` to the New-Project Scaffold
**What:** Add a `_context/stakeholders.md` stub to `00-meta-initialization/new-project/SKILL.md`, parallel to the existing 6 stubs (vision, features, tech_stack, business_rules, quality_standards, glossary).
**Why:** Three Phase 01 skills (Vision Statement, PRD, Business Case) list `stakeholders.md` as a **required** input and will halt on any fresh project. This is a single-file blocker.
**Standard:** IEEE 29148-2018 Section 6.2 mandates stakeholder identification before vision documentation.
**Suggested content:**
```markdown
# Stakeholders

<!-- TODO: List all stakeholder groups.
Format:
## Role Title
- **Influence:** High/Medium/Low
- **Primary Needs:** What this stakeholder needs from the system
- **Communication Preference:** How and how often to communicate
-->
```
**Complexity:** Simple (1 file edit)

---

### A-2: Add `personas.md` to the New-Project Scaffold
**What:** Add a `_context/personas.md` stub to `00-meta-initialization/new-project/SKILL.md`.
**Why:** The agile user story generation skill recommends `personas.md` and has fallback prompts when it is absent, but this creates unnecessary friction in the Phase 02 agile flow. The scaffold should provide an empty template.
**Standard:** IEEE 29148-2018 Section 6.4 — persona-driven story writing.
**Complexity:** Simple (1 file edit)

---

### A-3: Verify and Document the `logic.prompt` / Python Script Situation for Waterfall Skills 01–04
**What:** For each of the 4 thin waterfall SKILL.md wrappers (`01-initialize-srs`, `02-context-engineering`, `03-descriptive-modeling`, `04-interface-specification`), determine whether the `logic.prompt` and Python scripts exist and are functional. If they exist, add a note at the top of the SKILL.md: "If your environment cannot run Python, Claude can execute this skill directly by reading the step-by-step instructions below: [...]". If they don't exist, the SKILL.md must be expanded to embed the execution logic directly (matching Phase 01 skill depth).
**Why:** A consultant who cannot run Python (e.g., using Claude.ai without a code interpreter) has no fallback for 4 of the 8 core SRS generation skills.
**Standard:** IEEE 830-1998 — the SRS pipeline must be executable end-to-end.
**Complexity:** Medium (4 files, each requiring 100–150 lines of step-by-step instruction if scripts don't exist)

---

### A-4: Review All 9 Unreviewed Fundamentals Skills
**What:** Read and rate `02-requirements-engineering/fundamentals/before/03-brd-generation/SKILL.md` through `after/11-requirements-reuse/SKILL.md`.
**Why:** These skills form the pre-SRS layer of the pipeline. If any are stubs or missing, the BRD and requirements analysis workflow is broken for clients who need pre-elicitation work.
**Standard:** IEEE 29148-2018 Sections 6.3–6.8.
**Complexity:** Simple to Medium (review only; fixes depend on findings)

---

## Section B: Skill Strengthening Priorities (Ranked)

### B-1: Expand Waterfall Skill SKILL.md Files to Match Phase 01 Quality
**Rank:** 1 (Highest)
**Current state:** Skills 01–04 are 28–35 line wrappers. Skills 05–09 are full implementations.
**Target state:** All 8 skills should be self-contained: explicit step-by-step instructions, output section templates with placeholder content, common pitfalls, verification checklist.
**Pattern to follow:** `05-feature-decomposition/SKILL.md` (35 lines vs needed ~150 lines), Phase 01 Vision Statement (168 lines — the gold standard).
**Standard:** IEEE 830-1998 requires every requirement to be verifiable; the SKILL.md must be verifiable independently.

---

### B-2: Add "Before vs. After" Example Sections to Phase 02 Waterfall Skills
**Rank:** 2
**Current state:** Only `01-user-story-generation/SKILL.md` has a concrete before/after example.
**Target state:** Each waterfall SRS skill should include a mini-example showing what a correctly generated SRS section looks like for one representative feature. Even 10 lines of example output dramatically improves consultant output quality.
**Standard:** IEEE 830 Annex A — example SRS structures.
**Complexity:** Simple (1 section per skill, 8 skills)

---

### B-3: Add Agile-Compatible Path to Phase 05 Test Strategy
**Rank:** 3
**Current state:** `01-test-strategy/SKILL.md` requires `HLD.md` and `SRS_Draft.md`, both of which are waterfall artifacts.
**Target state:** Add an agile-compatible execution path: "If `SRS_Draft.md` is absent, read `user_stories.md` and `acceptance_criteria.md` as the test scope source. If `HLD.md` is absent, derive architecture context from `tech_stack.md`."
**Standard:** IEEE 829-2008 permits test strategy to be scoped to the available artifacts.
**Complexity:** Simple (1 file, ~20 lines added)

---

### B-4: Add Document Version Control Section to Phase 02 Skills
**Rank:** 4
**Current state:** No skill addresses versioning of generated documents.
**Target state:** Add a "Document Management" section to `01-initialize-srs/SKILL.md` covering: version numbering convention (`1.0-DRAFT → 1.0-REVIEW → 1.0-APPROVED`), change log entry format, and where approved documents are archived.
**Standard:** IEEE 830-1998 Section 4.3.7 Modifiability; ISO/IEC 15504 baseline management.
**Complexity:** Simple (1 file edit)

---

### B-5: Standardize Skill Frontmatter Across All Skills
**Rank:** 5
**Current state:** SKILL.md frontmatter varies: some have `name` and `description`; the Phase 09 skills use `Name` (capitalized) in the frontmatter. Some skills have no frontmatter at all.
**Target state:** Define a standard frontmatter schema:
```yaml
---
name: kebab-case-skill-name
phase: "02-requirements-engineering/waterfall"
description: One sentence summary
standard: IEEE 830-1998
version: 1.0.0
last_updated: YYYY-MM-DD
---
```
**Why:** Consistent frontmatter enables automated tooling (skill registries, roadmap generators).
**Complexity:** Simple (1 template, ~50 file edits)

---

## Section C: Missing Skills That Should Be Added

### C-1: Stakeholder Requirements Specification (SRS Supplement)
**What:** A skill that transforms the stakeholder register and elicitation log directly into formal stakeholder requirements statements, bridging the fundamentals layer to the waterfall SRS Skill 01.
**Why:** Currently there is a gap: the fundamentals layer produces `stakeholder_register.md` and `elicitation_log.md`, but there is no skill that synthesizes these into the structured `vision.md`, `features.md`, `business_rules.md` formats that the waterfall SRS skills require. The consultant must do this manually.
**Standard:** IEEE 29148-2018 Section 6.4 — Stakeholder Requirements Specification.
**Complexity:** Medium (1 new skill, ~180 lines)

---

### C-2: Change Request Management Skill
**What:** A skill that handles updates to an existing SRS — logs the change request, identifies impacted requirements, updates the affected SRS sections, and regenerates the traceability matrix delta.
**Why:** The repo has zero guidance on what happens after the SRS is approved and a client changes scope. In real consulting engagements, change management is where documentation debt accumulates fastest.
**Standard:** IEEE 830-1998 Section 4.3.7; ISO/IEC 15504 change management.
**Complexity:** Complex (new skill + integration with Phase 09 traceability)

---

### C-3: Hybrid Methodology SRS-to-Agile Bridge Skill
**What:** A skill that reads a completed SRS and generates a seed backlog of user stories, providing an automated bridge from waterfall requirements to agile execution.
**Why:** The 00-meta-initialization skill recommends Hybrid for many projects but there is no skill that executes the handoff from waterfall SRS to agile sprint planning.
**Standard:** IEEE 29148-2018 permits hybrid approaches; SAFe Program Increment planning.
**Complexity:** Medium (1 skill, ~200 lines)

---

### C-4: Glossary Maintenance Skill
**What:** A skill that scans all generated documents for undefined terms, cross-references against `_context/glossary.md`, and produces a list of terms needing definition or inconsistent usages needing harmonization.
**Why:** CLAUDE.md instructs using IEEE 610.12-1990 terminology but there is no active enforcement mechanism. Terminology drift across a 10-document project is a real quality risk.
**Standard:** IEEE 610.12-1990; IEEE 830 Section 4.1 (unambiguity).
**Complexity:** Simple (1 skill, ~100 lines)

---

## Section D: Infrastructure Improvements

### D-1: Create a Sample Project Under `projects/`
**What:** Build a minimal complete example project (e.g., a "library book loan system" or "clinic appointment system") with all `_context/` files populated and at least Phase 01–02–09 output documents generated.
**Why:** New consultants have no way to calibrate "what good looks like." A reference project demonstrates the expected depth and density of context files, and shows what a professional SRS section looks like when the skills are executed correctly.
**Complexity:** Complex (requires running 8+ skills on a real example)

---

### D-2: Add `manifest.md` Generation to Phase Skills
**What:** Each document-generating skill should write or update a `manifest.md` file in the document's output directory listing the section files in the correct assembly order.
**Why:** The build-doc protocol in CLAUDE.md says "use `manifest.md` if present, otherwise sort `*.md` files alphabetically." Alphabetical sort breaks when section numbers are inconsistent (e.g., `10-introduction.md` sorts before `2-scope.md`). Automating manifest creation removes this failure mode.
**Standard:** Document management best practice.
**Complexity:** Simple per skill (5 lines added to Step N of each skill's write instruction)

---

### D-3: Add `.env.example` to Templates
**What:** Add a `templates/env.example` file documenting the environment variables needed by the `scripts/build-doc.sh` script and any project-specific variables.
**Why:** The DEPENDENCIES.md tracks runtime dependencies but there is no template showing a consultant what environment variables to set for the build pipeline.
**Complexity:** Simple (1 file)

---

### D-4: Verify That All Referenced `references/*.md` Files Exist
**What:** Systematically check every `references/` path cited in every SKILL.md and confirm the files exist and contain substantive content.
**Why:** Skills reference dozens of auxiliary files (e.g., `references/scalability-patterns.md`, `references/lean-canvas-guide.md`, `references/interview-guide.md`). If any are absent, the skill instruction is a dead link.
**Standard:** ISO/IEC 15504 process completeness.
**Complexity:** Medium (audit pass, 30–50 files to verify)

---

## Section E: Domain Knowledge Gaps

### E-1: Verify and Expand Finance Domain `nfr-defaults.md`
**What:** Confirm `domains/finance/references/nfr-defaults.md` exists. If not, create it. If it exists, verify it has the same quality level as healthcare: each NFR must include a `Verifiability:` subsection with a specific, executable test.
**Why:** Finance is the second most common consulting domain after healthcare. PCI-DSS, SOX, and AML/KYC requirements are highly specific and clients expect them to be correct.
**Standard:** PCI-DSS v4.0, SOX Section 302/404, FFIEC guidelines.
**Key NFRs needed:** PCI-DSS encryption at rest (AES-256), tokenization for cardholder data, SOX audit trail, dual-authorization for financial transactions, fraud detection thresholds.
**Complexity:** Medium (8–12 NFR entries with verifiability criteria)

---

### E-2: Verify and Expand Government Domain `nfr-defaults.md`
**What:** Confirm `domains/government/references/nfr-defaults.md` quality level.
**Why:** Government projects face FISMA, FedRAMP, Section 508 accessibility, and often procurement-specific requirements. These are highly regulated and a wrong assumption could cause a compliance failure.
**Standard:** FISMA, NIST SP 800-53, FedRAMP Moderate, Section 508 WCAG.
**Key NFRs needed:** FedRAMP authorization controls, FIPS 140-2 cryptography, Section 508 accessibility, FISMA incident reporting within 1 hour.
**Complexity:** Medium (10–15 NFR entries)

---

### E-3: Add Industry-Specific Feature Templates to Non-Healthcare Domains
**What:** The healthcare domain has feature-level templates (`features/patient-management.md`, `features/appointment-scheduling.md` etc.). Confirm or create equivalent feature files for finance, education, retail, logistics, and government.
**Why:** Feature templates allow the scaffold to pre-populate `_context/features.md` with domain-standard features, dramatically reducing consultant setup time for common domain projects.
**Standard:** Domain best practices.
**Complexity:** Complex (5 domains × 4–6 features each = 20–30 files)

---

### E-4: Add `personas.md` Domain Defaults
**What:** For each domain, create default personas appropriate for that industry (e.g., healthcare: `Clinical Nurse`, `Attending Physician`, `Medical Records Clerk`, `Patient`).
**Why:** The agile user story generation skill requires `personas.md`. Without domain-specific persona defaults, every consultant must author personas from scratch. Domain defaults could be injected at scaffold time alongside NFRs.
**Standard:** IEEE 29148-2018 Section 6.4 (persona-based story writing).
**Complexity:** Simple per domain (1 file per domain, 10–15 personas)
