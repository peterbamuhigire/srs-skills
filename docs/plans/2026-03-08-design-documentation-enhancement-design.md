# Design Documentation Enhancement — Design Document

**Date:** 2026-03-08
**Status:** Approved
**Author:** Peter Bamuhigire + Claude Opus 4.6

## Summary

Enhance design documentation and related skills based on 6 authoritative books. 5 new skills, 22 new reference files, 6 edits to existing skills across Phases 01, 02, 03, and skills/.

## Book Sources

| Book | Key Contributions |
|------|-------------------|
| Business Analysis Methodology Book | Lean Canvas, Impact Mapping, hypothesis-driven requirements |
| Design for How People Think (Whalen) | Six Minds cognitive framework, cognitive walkthroughs, experience mapping |
| System Design - The Big Archive (ByteByteGo) | Scalability patterns, distributed systems, caching, reliability |
| Systems Analysis & Design with UML (Dennis/Wixom/Tegarden) | Use case modeling, activity diagrams, OO analysis |
| The Effective Product Designer | IA, wireframing, design systems, usability testing, design handoff |
| API Design Patterns (Geewax) | LRO, batch ops, field masks, resource relationships, custom methods |

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| UX Specification | New Phase 03 skill + cognitive skill in skills/ | Spec vs implementation split |
| Scalability patterns | HLD references + dedicated infrastructure skill with gate | HLD considers scale; full doc only when needed |
| Advanced API patterns | References on existing API spec skill | Extensions to REST, not separate discipline |
| Use Case Modeling | New waterfall skill (09) | Already planned; inherently structured technique |
| Lean Canvas | New Phase 01 skill with decision gate | Distinct artifact from PRD for lean teams |
| Cognitive UX | Shared skill + cross-refs on existing UI skills | DRY, single source of truth |

## Deliverables

### New Skills (5)
1. `03-design-documentation/05-ux-specification/` — IA, wireframes, design systems, handoff
2. `03-design-documentation/06-infrastructure-design/` — Scalability, caching, reliability (decision gate)
3. `02-requirements-engineering/waterfall/09-use-case-modeling/` — UML use cases, activity diagrams
4. `01-strategic-vision/04-lean-canvas/` — Lean Canvas, Impact Mapping (decision gate)
5. `skills/cognitive-ux-framework/` — Six Minds, cognitive walkthroughs

### New References on Existing Skills (9)
- HLD: scalability-patterns.md, distributed-systems.md, caching-strategies.md
- API Spec: advanced-api-patterns.md, long-running-operations.md, batch-operations.md
- Use Case: use-case-template.md, activity-diagram-guide.md, actor-classification.md

### Edits to Existing Skills (6)
- HLD SKILL.md: add optional scalability step
- API Spec SKILL.md: add optional advanced patterns step
- webapp-gui-design/01-overview.md: cognitive UX cross-reference
- pos-sales-ui-design/SKILL.md: cognitive UX cross-reference
- healthcare-ui-design/SKILL.md: cognitive UX cross-reference
- Parent READMEs: update skill counts and listings
