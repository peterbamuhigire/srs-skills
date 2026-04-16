# Skill-Local Path Migration — 2026-04-16

Source: `skill-paths-2026-04-16.csv` (678 references in 122 files).

## Summary

- **REWRITE**: 117 files — legacy paths are substantive instructions to be replaced with canonical `projects/<ProjectName>/...` paths.
- **WRAP**: 5 files — legacy paths document the alias relationship and should be preserved inside `<!-- alias-block ... -->` HTML comments.
- **DELETE**: 0 files — no dead/orphan references were identified during the audit.

## Per-file actions

| File | Action | Ref count | Notes |
|---|---|---|---|
| `00-meta-initialization/README.md` | REWRITE | 6 | Path references inside the context-seeding header comments and bullet lists. |
| `00-meta-initialization/SKILL.md` | REWRITE | 11 | Input path references across Inputs and Outputs sections. |
| `01-strategic-vision/01-prd-generation/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `01-strategic-vision/01-prd-generation/SKILL.md` | REWRITE | 11 | Input path references and output write paths. |
| `01-strategic-vision/02-business-case/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `01-strategic-vision/02-business-case/SKILL.md` | REWRITE | 8 | Input path references in skill body. |
| `01-strategic-vision/03-vision-statement/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `01-strategic-vision/03-vision-statement/SKILL.md` | REWRITE | 10 | Input path references in skill body. |
| `01-strategic-vision/04-lean-canvas/README.md` | REWRITE | 6 | Input and output path references. |
| `01-strategic-vision/04-lean-canvas/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `01-strategic-vision/README.md` | WRAP | 1 | Documents the alias relationship intentionally (phase-level README). |
| `02-requirements-engineering/README.md` | REWRITE | 1 | Legacy shorthand inside an example command block. |
| `02-requirements-engineering/agile/01-user-story-generation/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/agile/02-acceptance-criteria/README.md` | REWRITE | 3 | Input path references and output write paths. |
| `02-requirements-engineering/agile/02-acceptance-criteria/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/agile/03-story-mapping/README.md` | REWRITE | 2 | Input path references to user stories and epic breakdown. |
| `02-requirements-engineering/agile/03-story-mapping/SKILL.md` | REWRITE | 5 | Input path references in skill body. |
| `02-requirements-engineering/agile/04-backlog-prioritization/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `02-requirements-engineering/agile/04-backlog-prioritization/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/agile/README.md` | WRAP | 1 | Documents the alias relationship intentionally (phase-level README). |
| `02-requirements-engineering/fundamentals/README.md` | REWRITE | 2 | Inputs and Outputs section headers reference legacy aliases. |
| `02-requirements-engineering/fundamentals/after/08-requirements-management/SKILL.md` | REWRITE | 11 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/after/09-traceability-engineering/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/after/10-requirements-metrics/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/after/11-requirements-reuse/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/after/12-solution-evaluation-and-transition/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/before/01-stakeholder-analysis/SKILL.md` | REWRITE | 7 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/before/02-elicitation-toolkit/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/before/03-brd-generation/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/before/04-business-analysis-planning/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/during/04-requirements-analysis/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/during/05-conceptual-data-modeling/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/during/06-requirements-patterns/SKILL.md` | REWRITE | 8 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/during/06-requirements-patterns/references/crud-matrix.md` | REWRITE | 3 | Path references inside the CRUD-matrix reference doc. |
| `02-requirements-engineering/fundamentals/during/07-requirements-validation/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/during/08-business-process-modeling/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/during/09-business-rules-analysis/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `02-requirements-engineering/fundamentals/during/10-prototyping-and-solution-discovery/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `02-requirements-engineering/waterfall/01-initialize-srs/SKILL.md` | REWRITE | 6 | Output write paths for the SRS scaffold. |
| `02-requirements-engineering/waterfall/02-context-engineering/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `02-requirements-engineering/waterfall/02-context-engineering/SKILL.md` | REWRITE | 3 | Path references in skill body. |
| `02-requirements-engineering/waterfall/03-descriptive-modeling/README.md` | REWRITE | 2 | Input path references to `vision.md`, `features.md`, `quality_standards.md`. |
| `02-requirements-engineering/waterfall/03-descriptive-modeling/SKILL.md` | REWRITE | 3 | Input path references in skill body. |
| `02-requirements-engineering/waterfall/04-interface-specification/README.md` | REWRITE | 1 | Input path reference to context files. |
| `02-requirements-engineering/waterfall/04-interface-specification/SKILL.md` | REWRITE | 2 | Input path references. |
| `02-requirements-engineering/waterfall/05-feature-decomposition/README.md` | REWRITE | 1 | Input path reference to `features.md` and `quality_standards.md`. |
| `02-requirements-engineering/waterfall/05-feature-decomposition/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `02-requirements-engineering/waterfall/06-logic-modeling/README.md` | REWRITE | 1 | Input path reference to business rules and tech stack. |
| `02-requirements-engineering/waterfall/06-logic-modeling/SKILL.md` | REWRITE | 2 | Input path references. |
| `02-requirements-engineering/waterfall/07-attribute-mapping/README.md` | REWRITE | 1 | Input path reference to quality standards and tech stack. |
| `02-requirements-engineering/waterfall/07-attribute-mapping/SKILL.md` | REWRITE | 3 | Input path references. |
| `02-requirements-engineering/waterfall/08-semantic-auditing/README.md` | REWRITE | 1 | Audit target path reference to `SRS_Draft.md`. |
| `02-requirements-engineering/waterfall/08-semantic-auditing/SKILL.md` | REWRITE | 1 | Input path reference. |
| `02-requirements-engineering/waterfall/09-use-case-modeling/README.md` | REWRITE | 7 | Input path references and output write paths. |
| `02-requirements-engineering/waterfall/09-use-case-modeling/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `02-requirements-engineering/waterfall/README.md` | WRAP | 1 | Documents the alias relationship intentionally (phase-level README). |
| `03-design-documentation/01-high-level-design/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `03-design-documentation/01-high-level-design/SKILL.md` | REWRITE | 12 | Input path references in skill body. |
| `03-design-documentation/02-low-level-design/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `03-design-documentation/02-low-level-design/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `03-design-documentation/03-api-specification/README.md` | REWRITE | 3 | Input path references to SRS, HLD, and tech stack. |
| `03-design-documentation/03-api-specification/SKILL.md` | REWRITE | 11 | Input path references and output write paths. |
| `03-design-documentation/04-database-design/README.md` | REWRITE | 1 | Output write path for the database design doc. |
| `03-design-documentation/04-database-design/SKILL.md` | REWRITE | 15 | Input path references in skill body. |
| `03-design-documentation/05-ux-specification/README.md` | REWRITE | 9 | Input/output path references in tables and steps. |
| `03-design-documentation/05-ux-specification/SKILL.md` | REWRITE | 14 | Input path references in skill body. |
| `03-design-documentation/06-infrastructure-design/README.md` | REWRITE | 7 | Input path references and output write paths. |
| `03-design-documentation/06-infrastructure-design/SKILL.md` | REWRITE | 13 | Input path references in skill body. |
| `03-design-documentation/07-iot-system-design/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `03-design-documentation/README.md` | WRAP | 1 | Documents the alias relationship intentionally (phase-level README). |
| `04-development-artifacts/01-technical-specification/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `04-development-artifacts/01-technical-specification/SKILL.md` | REWRITE | 12 | Input path references and output write paths. |
| `04-development-artifacts/02-coding-guidelines/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `04-development-artifacts/02-coding-guidelines/SKILL.md` | REWRITE | 11 | Input path references and output write paths. |
| `04-development-artifacts/03-dev-environment-setup/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `04-development-artifacts/03-dev-environment-setup/SKILL.md` | REWRITE | 11 | Input path references and output write paths. |
| `04-development-artifacts/04-contribution-guide/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `04-development-artifacts/04-contribution-guide/SKILL.md` | REWRITE | 9 | Input path references and output write paths. |
| `04-development-artifacts/README.md` | REWRITE | 3 | Upstream/Inputs/Outputs bullets reference legacy aliases. |
| `05-testing-documentation/01-test-strategy/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `05-testing-documentation/01-test-strategy/SKILL.md` | REWRITE | 12 | Input path references and output write paths. |
| `05-testing-documentation/02-test-plan/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `05-testing-documentation/02-test-plan/SKILL.md` | REWRITE | 12 | Input path references and conditional inputs. |
| `05-testing-documentation/03-test-report/README.md` | REWRITE | 2 | Input path references to `Test_Plan.md`. |
| `05-testing-documentation/03-test-report/SKILL.md` | REWRITE | 8 | Input path references in skill body. |
| `05-testing-documentation/README.md` | REWRITE | 3 | Upstream/Inputs/Outputs bullets reference legacy aliases. |
| `06-deployment-operations/01-deployment-guide/README.md` | REWRITE | 2 | Input path references in skill body. |
| `06-deployment-operations/01-deployment-guide/SKILL.md` | REWRITE | 12 | Input path references and output write paths. |
| `06-deployment-operations/02-runbook/README.md` | REWRITE | 2 | Input path references in skill body. |
| `06-deployment-operations/02-runbook/SKILL.md` | REWRITE | 11 | Input path references and output write paths. |
| `06-deployment-operations/03-monitoring-setup/README.md` | REWRITE | 2 | Input path references in skill body. |
| `06-deployment-operations/03-monitoring-setup/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `06-deployment-operations/04-infrastructure-docs/README.md` | REWRITE | 2 | Input path references in skill body. |
| `06-deployment-operations/04-infrastructure-docs/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `06-deployment-operations/05-go-live-readiness/SKILL.md` | REWRITE | 3 | Input path references and output write paths. |
| `06-deployment-operations/README.md` | WRAP | 1 | Documents the alias relationship intentionally (phase-level README). |
| `07-agile-artifacts/01-sprint-planning/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `07-agile-artifacts/01-sprint-planning/SKILL.md` | REWRITE | 12 | Input path references in skill body. |
| `07-agile-artifacts/02-definition-of-done/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `07-agile-artifacts/02-definition-of-done/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `07-agile-artifacts/03-definition-of-ready/README.md` | REWRITE | 2 | Input path references and output write paths. |
| `07-agile-artifacts/03-definition-of-ready/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `07-agile-artifacts/04-retrospective-template/README.md` | REWRITE | 2 | Input path references in skill body. |
| `07-agile-artifacts/04-retrospective-template/SKILL.md` | REWRITE | 8 | Input path references and output write paths. |
| `07-agile-artifacts/README.md` | REWRITE | 1 | Inputs/Outputs bullet references legacy aliases. |
| `08-end-user-documentation/01-user-manual/README.md` | REWRITE | 2 | Input path references in skill body. |
| `08-end-user-documentation/01-user-manual/SKILL.md` | REWRITE | 13 | Input path references and output write paths. |
| `08-end-user-documentation/02-installation-guide/README.md` | REWRITE | 2 | Input path references in skill body. |
| `08-end-user-documentation/02-installation-guide/SKILL.md` | REWRITE | 10 | Input path references and output write paths. |
| `08-end-user-documentation/03-faq/README.md` | REWRITE | 2 | Input path references in skill body. |
| `08-end-user-documentation/03-faq/SKILL.md` | REWRITE | 11 | Input path references in skill body. |
| `08-end-user-documentation/04-release-notes/README.md` | REWRITE | 2 | Input path references in skill body. |
| `08-end-user-documentation/04-release-notes/SKILL.md` | REWRITE | 10 | Input path references in skill body. |
| `08-end-user-documentation/README.md` | REWRITE | 1 | Inputs/Outputs bullet references legacy aliases. |
| `09-governance-compliance/01-traceability-matrix/README.md` | REWRITE | 4 | Path references in the Inputs and Review sections. |
| `09-governance-compliance/01-traceability-matrix/SKILL.md` | REWRITE | 8 | Input path references in skill body. |
| `09-governance-compliance/02-audit-report/README.md` | REWRITE | 4 | Path references in the Inputs and Review sections. |
| `09-governance-compliance/02-audit-report/SKILL.md` | REWRITE | 7 | Input path references in skill body. |
| `09-governance-compliance/03-compliance-documentation/README.md` | REWRITE | 4 | Path references in the Inputs and Review sections. |
| `09-governance-compliance/03-compliance-documentation/SKILL.md` | REWRITE | 6 | Input path references in skill body. |
| `09-governance-compliance/04-risk-assessment/README.md` | REWRITE | 3 | Path references in the Inputs and Review sections. |
| `09-governance-compliance/04-risk-assessment/SKILL.md` | REWRITE | 8 | Input path references in skill body. |

## Substitution rules for REWRITE

When rewriting a file:

- `../project_context/` → `projects/<ProjectName>/_context/`
- `../project_context` → `projects/<ProjectName>/_context`
- `../output/` → `projects/<ProjectName>/<phase>/<document>/`
- `../output` → `projects/<ProjectName>/<phase>/<document>`

Where the original used `<phase>` or `<document>` as a placeholder, keep the placeholder verbatim. Where the original referenced a specific phase path such as `srs/`, expand to the concrete phase directory (for example, `projects/<ProjectName>/02-requirements-engineering/srs/`).

Phase-to-directory mapping for expansion:

- `01-strategic-vision/` artifacts write under `projects/<ProjectName>/01-strategic-vision/<document>/`.
- `02-requirements-engineering/` artifacts (including `SRS_Draft.md`) write under `projects/<ProjectName>/02-requirements-engineering/srs/` or the document directory resolved from `00-meta-initialization/new-project/SKILL.md`.
- `03-design-documentation/` artifacts write under `projects/<ProjectName>/03-design-documentation/<document>/`.
- `04-development-artifacts/` artifacts write under `projects/<ProjectName>/04-development-artifacts/<document>/`.
- `05-testing-documentation/` artifacts write under `projects/<ProjectName>/05-testing-documentation/<document>/`.
- `06-deployment-operations/` artifacts write under `projects/<ProjectName>/06-deployment-operations/<document>/`.
- `07-agile-artifacts/` artifacts write under `projects/<ProjectName>/07-agile-artifacts/<document>/`.
- `08-end-user-documentation/` artifacts write under `projects/<ProjectName>/08-end-user-documentation/<document>/`.
- `09-governance-compliance/` artifacts write under `projects/<ProjectName>/09-governance-compliance/<document>/`.

## Substitution rules for WRAP

Wrap the legacy reference in an HTML comment block so the canonical form and the legacy alias both remain visible, and so the `kernel.legacy_skill_paths` check skips the block:

```html
<!-- alias-block start -->
Legacy alias: `../project_context/` → `projects/<ProjectName>/_context/`
Legacy alias: `../output/` → `projects/<ProjectName>/<phase>/<document>/`
<!-- alias-block end -->
```

The existing prose above or below the alias block remains in canonical form. The wrap only covers the sentence that explicitly names the legacy shorthand.

## Files marked WRAP — inventory

| File | Line | Snippet |
|---|---|---|
| `01-strategic-vision/README.md` | 31 | `Existing skill-local references to ../project_context/ and ../output/ are compatibility aliases into the active project workspace, not a second architecture.` |
| `02-requirements-engineering/agile/README.md` | 5 | `The canonical runtime workspace for this pipeline is projects/<ProjectName>/. References inside older skill-local files to ../project_context/ and ../output/ should be interpreted as compatibility aliases into that active project workspace.` |
| `02-requirements-engineering/waterfall/README.md` | 5 | `The canonical runtime workspace for this pipeline is projects/<ProjectName>/. References inside older skill-local files to ../project_context/ and ../output/ should be interpreted as aliases into that active project workspace.` |
| `03-design-documentation/README.md` | 43 | `Existing skill-local references to ../project_context/ and ../output/ are compatibility aliases into the active project workspace.` |
| `06-deployment-operations/README.md` | 37 | `Existing skill-local references to ../project_context/ and ../output/ are compatibility aliases into the active project workspace.` |

## Files marked DELETE — inventory

None. Every audited legacy reference is either a substantive skill instruction (REWRITE) or a deliberate alias declaration (WRAP). No orphan or dead references were identified.
