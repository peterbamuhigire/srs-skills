# Gap Analysis

Current capped score: 64/100. Target: 95+/100.

## Richness

- Add complete exemplar outputs, not only instructions.
- Convert book/source notes into skill-local decision tables and worked examples.
- Cover edge cases, failure modes, and high-stakes variants explicitly.

## Robustness

- Add negative fixtures that prove gates fail correctly.
- Make validation scripts part of normal release, not optional maintenance.
- Define ambiguity-handling rules and stop conditions per major workflow.

## World-Class Output Capability

- Ship polished end-to-end reference deliverables for each primary use case.
- Add final QA/red-team checklists with release-blocking criteria.
- Add evidence packs showing source inputs, decisions, tests, and final output.

## Architecture & Discoverability

- Fix missing frontmatter and remove/alias empty paths.
- Add a single router map generated from filesystem discovery.
- Separate engine, examples, active projects, and generated artefacts.

## Composability & Reuse

- Define cross-engine contracts and acceptance criteria.
- Create reusable templates/workbooks/scripts for repeatable outputs.
- Use shared naming and evidence conventions across skills.

## Currency & Compliance

- Add dated source registers for volatile standards.
- Assign review cadence and reviewer fields to compliance-sensitive references.
- Automate freshness checks where URLs, statutes, rates, APIs, or platforms change.

## Engine-Specific Blocking Gaps

- Several local project workspaces and generated DOCX artefacts live inside the engine tree, weakening the separation between reusable engine and client/product outputs.
- The evidence/examples layer is uneven: strong demo and gate material exists, but many skills still need representative input/output pairs and failure-mode examples.
- The engine references design, finance, and engineering catalogues well, but lacks a single cross-engine contract test proving those handoffs from a fresh checkout.
