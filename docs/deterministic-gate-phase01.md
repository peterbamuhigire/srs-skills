# Phase 01 Deterministic Gate

Use this checklist before declaring strategic vision outputs complete. The purpose is to make Phase 01 reviewable against IEEE 29148 and business-governance expectations instead of relying on narrative quality alone.

1. **Canonical Inputs**
   - `projects/<ProjectName>/_context/vision.md`, `stakeholders.md`, `features.md`, and `glossary.md` exist and contain no unresolved `<!-- TODO -->` placeholders.
   - If any skill-local workflow still refers to `../project_context/`, treat it as an alias to `projects/<ProjectName>/_context/`.

2. **Vision-to-Requirement Readiness**
   - Vision Statement defines business problem, target users, constraints, and success measures.
   - PRD decomposes scope into concrete capabilities and clearly separates in-scope, out-of-scope, and assumptions.
   - Business Case includes investment rationale, expected value, delivery risks, and decision triggers.

3. **Clause-Level Anchoring**
   - Vision and PRD sections cite the relevant IEEE 29148 clauses or equivalent planning references where claims are normative.
   - Every strategic objective is uniquely identifiable so it can be traced into Phase 02 requirements.

4. **Deterministic Closure**
   - No unresolved `[CONTEXT-GAP]`, `[GLOSSARY-GAP]`, or `[V&V-FAIL]` markers remain without owner and next action.
   - A reviewer can map every major capability in the PRD to at least one item in `features.md`.

5. **Exit Evidence**
   - Record the Phase 01 gate outcome in the project evidence log before requirements generation starts.
