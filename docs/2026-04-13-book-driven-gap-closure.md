# Book-Driven Gap Closure

Date: 2026-04-13

## Objective

Close high-value SDLC engine gaps using the software engineering, requirements, business analysis, IoT, and production-readiness material reviewed during this pass, while keeping the repository additive and compatible with existing Claude Code and Codex workflows.

## Source-Informed Gap Themes

- Business analysis planning and governance
- Business process modeling
- Business rules analysis
- Prototype-led solution discovery
- Solution evaluation and organizational transition
- IoT system design
- Go-live readiness and launch governance

## Added Skills

### Requirements Engineering Fundamentals

- `before/04-business-analysis-planning`
- `during/08-business-process-modeling`
- `during/09-business-rules-analysis`
- `during/10-prototyping-and-solution-discovery`
- `after/12-solution-evaluation-and-transition`

### Design Documentation

- `03-design-documentation/07-iot-system-design`

### Deployment & Operations

- `06-deployment-operations/05-go-live-readiness`

## Why These Additions Matter

- They push the engine upstream into business analysis and downstream into launch control instead of stopping at requirements text generation.
- They make requirements and design execution-oriented by adding process models, rule catalogs, prototypes, transition planning, and release governance.
- They improve coverage for connected products and operationally critical launches where standard web-system documentation is not enough.

## Reduced Gaps

- The engine now has an explicit business analysis planning layer before methodology selection.
- It now models workflows and business rules directly instead of leaving them implicit inside prose requirements.
- It now supports prototype-driven discovery and solution comparison before detailed design hardens.
- It now extends beyond requirements closure into transition planning and solution evaluation.
- It now covers IoT-specific architecture and launch-readiness assessment.

## Remaining High-Value Gaps

- Deterministic enforcement and machine-checkable quality gates remain the main structural weakness.
- The pathing/runtime model still mixes legacy relative-path assumptions with the newer project-scoped workspace design.
- Hybrid synchronization, ADRs, change impact analysis, formal waivers, and requirement-to-code traceability are still underpowered or missing.
- Domain compliance still needs deeper control libraries and evidence-oriented enforcement.

## Scope Limits

- The Sommerville file supplied in Downloads appears to be a DjVu file with a `.pdf` extension, so this pass used repository analysis plus the additional EPUB material instead of direct PDF extraction.
- This was a targeted gap-closure pass, not a full redesign of every phase or every existing skill.

## Recommended Next Pass

- Add ADR tracking, change impact analysis, and baseline/delta comparison.
- Build a canonical validation kernel with machine-readable gate outputs.
- Deepen regulated-domain overlays into control-and-evidence libraries.
