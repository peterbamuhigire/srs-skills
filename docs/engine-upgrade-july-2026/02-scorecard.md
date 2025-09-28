# Scorecard

Raw weighted total: 78/100. Capped audit total: 64/100. The cap is applied because this audit intentionally exposes the path from current state to 95+ rather than awarding production-certification scores.

| Dimension | Raw score | Points |
| --- | --- | --- |
| Richness | 17/20 | 17 |
| Robustness | 17/20 | 17 |
| World-Class Output Capability | 16/20 | 16 |
| Architecture & Discoverability | 11/15 | 11 |
| Composability & Reuse | 10/15 | 10 |
| Currency & Compliance | 7/10 | 7 |

## Richness

Raw score: 17/20.

The engine has 147 SKILL.md files, 260 reference-file hits, 33 template-file hits, and 10 example-file hits. This gives it substantial domain coverage, but the richness score is held back where references are not converted into reusable examples, current-source registers, or complete model outputs.

Top deficiencies:

- Several local project workspaces and generated DOCX artefacts live inside the engine tree, weakening the separation between reusable engine and client/product outputs.
- The evidence/examples layer is uneven: strong demo and gate material exists, but many skills still need representative input/output pairs and failure-mode examples.
- The engine references design, finance, and engineering catalogues well, but lacks a single cross-engine contract test proving those handoffs from a fresh checkout.

## Robustness

Raw score: 17/20.

Robustness is supported by routers/governance files (618 read), scripts/tests where present (139 script or script-like files), and explicit anti-slop or quality gates in the repository. It is limited by missing live validation, missing negative fixtures, weak automated checks, or incomplete failure-mode coverage depending on the engine.

Top deficiencies:

- Several local project workspaces and generated DOCX artefacts live inside the engine tree, weakening the separation between reusable engine and client/product outputs.
- The evidence/examples layer is uneven: strong demo and gate material exists, but many skills still need representative input/output pairs and failure-mode examples.
- The engine references design, finance, and engineering catalogues well, but lacks a single cross-engine contract test proving those handoffs from a fresh checkout.

## World-Class Output Capability

Raw score: 16/20.

The engine can produce credible specialist output in its domain, but the audit asks whether the output is indistinguishable from a top-tier firm. The current blocker is usually the same pattern: not enough finished exemplars, proof packs, rendered outputs, evaluator simulations, or audited workbooks to demonstrate repeatable excellence.

Top deficiencies:

- Several local project workspaces and generated DOCX artefacts live inside the engine tree, weakening the separation between reusable engine and client/product outputs.
- The evidence/examples layer is uneven: strong demo and gate material exists, but many skills still need representative input/output pairs and failure-mode examples.
- The engine references design, finance, and engineering catalogues well, but lacks a single cross-engine contract test proving those handoffs from a fresh checkout.

## Architecture & Discoverability

Raw score: 11/15.

The structure is discoverable enough to route by filesystem and frontmatter, but there are 0 skills missing name frontmatter and 0 missing description frontmatter. Empty directories (8) and large local project/example surfaces can also reduce routing clarity.

Top deficiencies:

- Several local project workspaces and generated DOCX artefacts live inside the engine tree, weakening the separation between reusable engine and client/product outputs.
- The evidence/examples layer is uneven: strong demo and gate material exists, but many skills still need representative input/output pairs and failure-mode examples.
- The engine references design, finance, and engineering catalogues well, but lacks a single cross-engine contract test proving those handoffs from a fresh checkout.

## Composability & Reuse

Raw score: 10/15.

Reuse is visible through references, templates, scripts, examples, cross-engine trigger blocks, and local governance. The gap is less about having reusable pieces and more about proving they compose into complete delivery workflows with stable contracts and acceptance criteria.

Top deficiencies:

- Several local project workspaces and generated DOCX artefacts live inside the engine tree, weakening the separation between reusable engine and client/product outputs.
- The evidence/examples layer is uneven: strong demo and gate material exists, but many skills still need representative input/output pairs and failure-mode examples.
- The engine references design, finance, and engineering catalogues well, but lacks a single cross-engine contract test proving those handoffs from a fresh checkout.

## Currency & Compliance

Raw score: 7/10.

Currency and compliance depend on dated source registers, official standards, live-rate or platform refresh protocols, and release gates. The score is constrained when standards are named but not tied to dated verification, reviewer sign-off, or automated freshness checks.

Top deficiencies:

- Several local project workspaces and generated DOCX artefacts live inside the engine tree, weakening the separation between reusable engine and client/product outputs.
- The evidence/examples layer is uneven: strong demo and gate material exists, but many skills still need representative input/output pairs and failure-mode examples.
- The engine references design, finance, and engineering catalogues well, but lacks a single cross-engine contract test proving those handoffs from a fresh checkout.
