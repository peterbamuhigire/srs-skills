# Waterfall SRS Generation Pipeline

This directory contains the **complete 8-phase IEEE 830-1998 compliant SRS generation pipeline** for traditional Waterfall projects.

## When to Use This Pipeline

✅ **USE for:**
- Regulated industries (medical devices, aerospace, government contracts)
- Fixed-scope, fixed-price projects with contractual SRS requirements
- Projects requiring IEEE 830, IEEE 1233, or ASTM E1340 compliance
- Systems where comprehensive upfront requirements are mandatory
- Safety-critical systems requiring formal verification and validation

❌ **DO NOT USE for:**
- Agile/Scrum projects (use `../agile/` pipeline instead)
- MVPs or rapid prototypes with evolving requirements
- Startups with high uncertainty and frequent pivots
- Projects where lightweight user stories are sufficient

## Pipeline Overview

This pipeline follows a strict sequential execution model:

```mermaid
flowchart LR
    C[Context Seed] --> S01[01 Initialize]
    S01 --> S02[02 Context Engineering]
    S02 --> S03[03 Descriptive Modeling]
    S03 --> S04[04 Interface Specification]
    S04 --> S05[05 Feature Decomposition]
    S05 --> S06[06 Logic Modeling]
    S06 --> S07[07 Attribute Mapping]
    S07 --> S08[08 Semantic Auditing]
    S08 --> O[SRS Draft + RTM]
```

## The 8 Phases

| Phase | Skill | SRS Target | Standards | Output |
|-------|-------|------------|-----------|--------|
| **01** | [Initialize SRS](01-initialize-srs/) | Grounding Data | ISO/IEC 15504, IEEE 1074 | Context templates in `../project_context/` |
| **02** | [Context Engineering](02-context-engineering/) | Section 1.0 Introduction | IEEE 830 §5.1 | Purpose, Scope, Definitions |
| **03** | [Descriptive Modeling](03-descriptive-modeling/) | Section 2.0 Overview | IEEE 830 §5.2 | System context, constraints |
| **04** | [Interface Specification](04-interface-specification/) | Section 3.1 Interfaces | IEEE 1233, ISO/IEC 25051 | External interfaces, protocols |
| **05** | [Feature Decomposition](05-feature-decomposition/) | Section 3.2 Functional Req. | IEEE 830 §5.3.1 | Stimulus/Response requirements |
| **06** | [Logic Modeling](06-logic-modeling/) | Section 3.2.x Algorithms | IEEE 1016 | LaTeX formulas, decision logic |
| **07** | [Attribute Mapping](07-attribute-mapping/) | Sections 3.3–3.6 NFRs | ISO/IEC 25010 | Performance, security, reliability |
| **08** | [Semantic Auditing](08-semantic-auditing/) | Validation & Traceability | IEEE 1012 | RTM, audit report, verification |

## Execution Instructions

### First-Time Setup

1. **Initialize project context:**
   ```
   Run skill: 02-requirements-engineering/waterfall/01-initialize-srs
   ```
   This creates `../project_context/` with 6 templates:
   - `vision.md` - Product vision and stakeholder goals
   - `features.md` - Feature catalog
   - `tech_stack.md` - Technology constraints
   - `business_rules.md` - Domain logic and business rules
   - `quality_standards.md` - NFR targets (ISO/IEC 25010)
   - `glossary.md` - IEEE 610.12 terminology

2. **Populate templates:**
   Fill each `.md` file with **measurable, specific data**. Avoid vague statements like "fast" or "secure" - use quantifiable metrics (e.g., "<200ms response time", "AES-256 encryption").

3. **Run phases 02-08 sequentially:**
   Each phase builds on the previous output. Never skip phases or run out of order.

### Sequential Execution Workflow

```bash
# Phase 02: Generate Section 1.0 (Introduction)
Run skill: 02-requirements-engineering/waterfall/02-context-engineering

# Phase 03: Generate Section 2.0 (Overall Description)
Run skill: 02-requirements-engineering/waterfall/03-descriptive-modeling

# Phase 04: Generate Section 3.1 (External Interfaces)
Run skill: 02-requirements-engineering/waterfall/04-interface-specification

# Phase 05: Generate Section 3.2 (Functional Requirements)
Run skill: 02-requirements-engineering/waterfall/05-feature-decomposition

# Phase 06: Generate Section 3.2.x (Algorithms & Data Logic)
Run skill: 02-requirements-engineering/waterfall/06-logic-modeling

# Phase 07: Generate Sections 3.3-3.6 (Non-Functional Requirements)
Run skill: 02-requirements-engineering/waterfall/07-attribute-mapping

# Phase 08: Validate SRS and generate RTM
Run skill: 02-requirements-engineering/waterfall/08-semantic-auditing
```

### Expected Outputs

After completing all 8 phases, you will have:

- **`../output/SRS_Draft.md`**: Complete IEEE 830-compliant SRS document
- **`../output/Traceability_Matrix.md`**: Requirements traceability matrix (IEEE 1012)
- **`../output/Audit_Report.md`**: Verification and validation report

## Re-running Phases (Iterative Updates)

**Idempotency Rule:** Phases 02–07 are designed to be re-runnable.

### When Context Changes

| Changed File | Re-run Phases | Reason |
|--------------|---------------|--------|
| `vision.md` | 02, 08 | Vision affects introduction and traceability |
| `features.md` | 05, 06, 07, 08 | Features drive functional and NFR requirements |
| `tech_stack.md` | 03, 04, 08 | Tech stack affects system description and interfaces |
| `business_rules.md` | 06, 08 | Business rules directly map to logic models |
| `quality_standards.md` | 07, 08 | Quality standards define NFRs |

### Maintenance Mode

When re-running skills on an existing SRS:

1. **Phase 01** has a `--maintenance` flag:
   ```
   Run skill: 01-initialize-srs with --maintenance flag
   ```
   This adds missing templates without overwriting existing files.

2. **Phases 02-07** will prompt before overwriting:
   - `[APPEND]` - Add new version while keeping old content
   - `[PATCH]` - Update specific lines only
   - `[OVERWRITE]` - Replace entire section (use cautiously)

3. **Always re-run Phase 08** after any changes to validate consistency.

## Verification Gateways

Each phase has built-in quality checks:

- **Phase 02-07:** Verify input files exist before execution
- **Phase 05:** Validate all requirements follow Stimulus/Response pattern
- **Phase 06:** Ensure all LaTeX formulas are syntactically correct
- **Phase 07:** Check all NFRs have measurable acceptance criteria
- **Phase 08:** Full IEEE 830 conformance audit (Correctness, Unambiguous, Complete, Consistent, Verifiable)

## Common Pitfalls

❌ **Running phases out of order**
- Each phase depends on previous outputs. Always execute sequentially.

❌ **Vague context files**
- "The system should be fast" → ❌
- "The system shall respond within 200ms for 95% of API requests" → ✅

❌ **Skipping Phase 08**
- Phase 08 is mandatory. It validates all previous phases and generates the RTM.

❌ **Using this pipeline for Agile projects**
- If your project is Agile, use `../agile/` pipeline instead.

## Standards Compliance

This pipeline implements:

- **IEEE Std 830-1998**: Software Requirements Specifications
- **IEEE Std 1233-1998**: System Requirements Development
- **IEEE Std 610.12-1990**: Software Engineering Terminology
- **IEEE Std 1012-2016**: Verification and Validation
- **IEEE Std 1016-2009**: Software Design Descriptions (for logic modeling)
- **ASTM E1340-96**: Rapid Prototyping of Computerized Systems
- **ISO/IEC 15504**: Process Assessment Framework
- **ISO/IEC 25010**: Software Product Quality Model

## Migration from Legacy Structure

**Previous users:** If you previously used skills at the root level (`01-initialize-srs`, etc.), those have been moved here. Update your workflows to reference the new paths:

```bash
# Old (deprecated)
Run skill: 01-initialize-srs

# New (current)
Run skill: 02-requirements-engineering/waterfall/01-initialize-srs
```

## Related Pipelines

- **Agile Requirements:** `../agile/` - User stories, story mapping, backlog management
- **Use Case Modeling:** `../waterfall/09-use-case-modeling/` (coming soon)
- **Design Documentation:** `../../03-design-documentation/` - HLD, LLD, API specs

## Support

For issues specific to this pipeline:
1. Check the `SKILL.md` in each phase directory
2. Review `skill_overview.md` at project root for input/output mappings
3. Consult `CLAUDE.md` for AI assistant protocols
4. Ensure `DEPENDENCIES.md` runtime requirements are met

---

**Last Updated:** 2026-02-07
**Pipeline Version:** 3.0.0
**Maintained by:** Peter Bamuhigire
