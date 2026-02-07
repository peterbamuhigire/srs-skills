# SDLC-Docs-Engine Project Brief

## What Is This?

**SDLC-Docs-Engine** (v3.0) is an AI-powered, standards-driven documentation generator that creates **comprehensive, IEEE/ISO-compliant documentation** across all phases of software development.

**Think of it as:** A portable "Documentation Engine" that lives in your project's `skills/` directory, reads your project context, and generates professional documentation for **Waterfall, Agile, or Hybrid** methodologies.

---

## What's New in v3.1?

**AI-Assisted Development Skills** (February 2026) - New skills that enhance Claude Code's ability to help you develop software:

- ✅ **ai-assisted-development**: Orchestrate multiple AI agents (30-75% faster through parallelization)
- ✅ **ai-error-prevention**: 7 strategies to catch Claude's mistakes early (saves 50-75% of tokens)
- ✅ **orchestration-best-practices**: The 10 Commandments of Orchestration
- ✅ **ai-error-handling**: 5-layer validation stack for AI-generated code
- ✅ **Reference guides**: Prompting patterns, orchestration patterns, encoding patterns into skills

## What Was New in v3.0?

Previously called **SRS-Skills** (focused only on IEEE 830 SRS generation), v3.0 expanded to support:

- ✅ **Multi-Methodology Support**: Waterfall (IEEE 830 SRS) + Agile (User Stories) + Hybrid
- ✅ **23 Document Types**: PRD, SRS, User Stories, HLD, LLD, API Specs, Test Plans, Runbooks, Manuals, Compliance Docs
- ✅ **10 SDLC Phases**: From strategic vision to governance/compliance
- ✅ **Methodology Detection**: Automatic project analysis and recommendation (Phase 00)
- ✅ **Backward Compatible**: Existing Waterfall SRS pipeline preserved

---

## How It Works

### 1. Install as Submodule

```bash
git submodule add https://github.com/peterbamuhigire/srs-skills.git skills
cd skills
```

### 2. Select Methodology

```bash
Run skill: 00-meta-initialization
```

The engine scans your project and recommends Waterfall, Agile, or Hybrid based on:
- Regulatory requirements (FDA, FAA, HIPAA)
- Project type (startup, enterprise, government)
- Development pace (commit frequency, sprint structure)
- Team structure and size

### 3. Generate Documentation

**For Waterfall:**
```bash
Run: 02-requirements-engineering/waterfall/01-initialize-srs
# ... run phases 02-08 sequentially
Output: SRS_Draft.md (IEEE 830), Traceability_Matrix.md, Audit_Report.md
```

**For Agile:**
```bash
Run: 02-requirements-engineering/agile/01-user-story-generation
Output: user_stories.md, story_map.mmd, backlog_summary.md
```

### 4. Expand to Other Phases

```bash
Run: 03-design-documentation/01-high-level-design
Run: 05-testing-documentation/02-test-plans
Run: 06-deployment-operations/02-runbook-generation
```

---

## What Can It Generate?

### Requirements Documentation
- **Waterfall**: IEEE 830 SRS (8-phase pipeline)
- **Agile**: INVEST-compliant user stories with acceptance criteria

### Design Documentation
- High-Level Design (HLD) - IEEE 1016
- Low-Level Design (LLD) - IEEE 1016
- API Specifications - OpenAPI 3.0
- Database Design - ERDs, schema docs

### Testing Documentation
- Test Strategy - IEEE 829
- Test Plans & Test Cases
- Test Reports

### Operational Documentation
- Deployment Guides
- Runbooks (SRE best practices)
- Monitoring & IaC Documentation

### Agile Artifacts
- Sprint Planning Documents
- Definition of Done (DoD)
- Definition of Ready (DoR)
- Retrospectives

### End-User Documentation
- User Manuals - ISO 26514
- Installation Guides
- FAQs & Troubleshooting

### Governance & Compliance
- Requirements Traceability Matrix (RTM) - IEEE 1012
- Audit Reports - IEEE 1012 V&V
- Compliance Docs (GDPR, HIPAA, SOC2)

---

## Architecture Overview

```
sdlc-docs-engine/
├── 00-meta-initialization/          # START HERE: Methodology selection
├── 01-strategic-vision/             # PRD, vision statements
├── 02-requirements-engineering/
│   ├── waterfall/                   # IEEE 830 SRS (8 phases)
│   └── agile/                       # User stories, backlog
├── 03-design-documentation/         # HLD, LLD, API specs
├── 04-development-artifacts/        # Technical specs, code docs
├── 05-testing-documentation/        # Test strategy, plans, cases
├── 06-deployment-operations/        # Deployment guides, runbooks
├── 07-agile-artifacts/              # Sprint planning, DoD, DoR
├── 08-end-user-documentation/       # User manuals, FAQs
├── 09-governance-compliance/        # Traceability, audits, compliance
└── skills/                          # 25+ domain-specific patterns
```

**Stateless Design:**
- Skills live in `skills/` (submodule)
- Project data in `../project_context/` (parent project)
- Generated docs in `../output/` (parent project)
- No project-specific data commits to submodule

---

## Standards Compliance

All documentation aligns with industry standards:

- **IEEE 830-1998**: Software Requirements Specifications
- **IEEE 1233-1998**: System Requirements Development
- **IEEE 1012-2016**: Verification and Validation
- **IEEE 1016-2009**: Software Design Descriptions
- **IEEE 29148-2018**: Requirements Engineering
- **IEEE 829**: Software Test Documentation
- **ISO/IEC 25010**: Software Product Quality
- **ISO 26514**: User Documentation
- **OpenAPI 3.0**: API Documentation

---

## Key Features

### 🎯 Methodology-Agnostic
Choose Waterfall, Agile, or Hybrid based on your project needs.

### 📊 Standards-Driven
Every document maps to specific IEEE/ISO standards with clause references.

### 🔁 Iterative & Idempotent
Re-run skills when context changes; they'll update without losing work.

### 🔍 Verification & Validation
Built-in IEEE 1012 auditing ensures correctness, completeness, consistency.

### 🧩 Domain Skills Integration
25+ reusable patterns (multi-tenant, GIS, security, UI/UX) enhance documentation.

### 📝 Token-Efficient
500-line hard limit on all `.md` files ensures AI comprehension and low cost.

---

## Use Cases

### Use Case 1: Medical Device SRS (Waterfall)

**Scenario:** FDA-regulated medical device requires IEEE 830 SRS

**Workflow:**
1. Run `00-meta-initialization` → Detects "FDA", recommends Waterfall
2. Run `02-requirements-engineering/waterfall/01-initialize-srs`
3. Populate context files (`vision.md`, `features.md`, `business_rules.md`)
4. Run phases 02-08 sequentially
5. Output: Complete SRS + Traceability Matrix + Audit Report

**Timeline:** 4-6 weeks

---

### Use Case 2: Startup MVP (Agile)

**Scenario:** E-commerce startup needs rapid iteration with user stories

**Workflow:**
1. Run `00-meta-initialization` → Detects "MVP", recommends Agile
2. Run `01-strategic-vision/01-prd-generation` → Lightweight PRD
3. Run `02-requirements-engineering/agile/01-user-story-generation`
4. Output: User Stories + Story Map + Sprint-ready backlog

**Timeline:** 1-2 sprints

---

### Use Case 3: Enterprise SaaS (Hybrid)

**Scenario:** SaaS platform with regulated backend + agile frontend

**Workflow:**
1. Run `00-meta-initialization` → Detects microservices, recommends Hybrid
2. Backend: Run `02-requirements-engineering/waterfall/` → SRS for payment service
3. Frontend: Run `02-requirements-engineering/agile/` → User stories for UI
4. Shared: Run `03-design-documentation/01-high-level-design` → Unified architecture

**Timeline:** 3-4 weeks

---

## Migration from v2.x

Existing SRS-Skills users:

**Old structure:**
```
01-initialize-srs/
02-context-engineering/
... (at root level)
```

**New structure (v3.0):**
```
02-requirements-engineering/waterfall/01-initialize-srs/
02-requirements-engineering/waterfall/02-context-engineering/
... (moved to waterfall subdirectory)
```

**Backward compatible:** Legacy paths still work with deprecation notices.

See `docs/MIGRATION_V2_TO_V3.md` for complete migration guide.

---

## Quick Reference

| Task | Command | Output |
|------|---------|--------|
| **Select Methodology** | `00-meta-initialization` | `methodology.md`, `doc_roadmap.md` |
| **Waterfall SRS** | `02-requirements-engineering/waterfall/01-initialize-srs` | IEEE 830 SRS |
| **Agile User Stories** | `02-requirements-engineering/agile/01-user-story-generation` | User story backlog |
| **High-Level Design** | `03-design-documentation/01-high-level-design` | HLD with C4 diagrams |
| **Test Plans** | `05-testing-documentation/02-test-plans` | IEEE 829 test plans |
| **Traceability** | `09-governance-compliance/01-traceability-matrix` | RTM + audit report |

---

## Roadmap

### v3.0 (Current - 2026-02-07)
- ✅ Multi-methodology support
- ✅ 10 SDLC phases (00-09)
- ✅ Agile user story generation
- ✅ Methodology detection (Phase 00)

### v3.1 (Planned - Q1 2026)
- ⏳ Design documentation skills (HLD, LLD, API specs)
- ⏳ Testing documentation skills
- ⏳ Agile story mapping & backlog prioritization

### v3.2 (Planned - Q2 2026)
- ⏳ Deployment & operations skills
- ⏳ End-user documentation skills
- ⏳ Compliance documentation (GDPR, HIPAA, SOC2)

---

## Support & Resources

- **GitHub:** https://github.com/peterbamuhigire/srs-skills
- **Issues:** https://github.com/peterbamuhigire/srs-skills/issues
- **Full Documentation:** See `README.md` in root
- **AI Assistant Guide:** See `CLAUDE.md` for AI-specific protocols

---

**Built with precision. Powered by standards. Designed for portability.**

**Version:** 3.0.0
**Last Updated:** 2026-02-07
**Maintained by:** Peter Bamuhigire
