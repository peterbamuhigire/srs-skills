# Book-Extraction Retirement — 2026-09-24

Owner: SRS engine maintainer. Rule: "Never store book extractions" (`AGENTS.md`, `CLAUDE.md`).

## Decision

The `book-extractions/` folder (15 tracked files), `docs/research/adzic-books-analysis.md` and
`docs/ux-foundations.md` were removed with `git rm`. Every capability still used by a skill was
first rewritten as a paraphrased, task-oriented reference with an Evidence/currentness note, and
every link was repointed. The source-ingestion guardrail now fails on extraction folders,
extraction-named files and links into them.

## Disposition

| Removed file | Knowledge now lives in |
|---|---|
| `2026-09-14-requirements-architecture-synthesis.md` | `02-requirements-engineering/fundamentals/after/09-traceability-engineering/references/scenario-spine-and-requirement-contract.md` (linked from PRD, system overview, traceability, metrics, validation) |
| `human-english-craft-synthesis-2026.md`, `english-collocations-and-lexical-precision-2026-09-02.md` | `09-governance-compliance/28-anti-ai-slop/references/human-english-and-lexical-precision.md` (linked from anti-slop, UX content, `AGENTS.md`) |
| `saas-architectures-srs-extraction.md` | Already implemented: `03-design-documentation/10-saas-multi-tenancy-architecture-spec` and its references |
| `saas-email-marketing-srs-extraction.md` | Already implemented: `08-end-user-documentation/06-saas-onboarding-journey-spec`, `07-saas-lifecycle-email-strategy-doc` |
| `saas-financial-metrics-srs-extraction.md` | Already implemented: `01-strategic-vision/references/saas-metric-and-kpi-catalogue.md`, `02-requirements-engineering/13-saas-billing-and-metering-spec` (incl. revenue-recognition template) |
| `saas-operations-srs-extraction.md` | Already implemented: `12-saas-pricing-and-packaging-spec`, `01-strategic-vision/references/saas-operating-principles-charter.md`, `05-saas-customer-success-playbook` |
| `saas-playbook-walling-srs-extraction.md` | Already implemented: `10-saas-mvp-scoping-doc`, `11-saas-moat-and-defensibility-plan`, `09-governance-compliance/05-architecture-decision-records/references/saas-adr-catalogue.md` |
| `saas-sales-fundamentals-srs-extraction.md`, `saas-sales-method-ae-srs-extraction.md` | Already implemented: `08-end-user-documentation/08-saas-sales-enablement-doc-pack` and its value-quantification worksheet |
| `saas-srs-skills-audit-2026.md`, `ai-on-saas-srs-audit-2026.md`, `agent-products-srs-audit-2026.md`, `ai-incident-response-srs-audit-2026.md`, `agent-compliance-srs-audit-2026.md` | Engine gap audits whose proposed skills exist in phases 01 to 09 (some consolidated into references); open items carried forward below |
| `docs/research/adzic-books-analysis.md` | `02-requirements-engineering/agile/01-user-story-generation/references/story-splitting-patterns.md`; `02-requirements-engineering/agile/02-acceptance-criteria/references/scenario-quality-rules.md`; impact mapping already in `01-strategic-vision/04-lean-canvas/references/` |
| `docs/ux-foundations.md` | `03-design-documentation/05-ux-specification/references/ux-requirements-foundations.md` (WCAG 2.1 corrected to 2.2; "7 plus or minus 2" caps withdrawn) |

The embedded copy of the UX digest in `docs/superpowers/plans/2026-05-04-srs-skills-uiux-phase2.md`
was replaced with a historical note.

## Open backlog carried forward (engine-authored, no book content)

- Compliance packs not yet built: PCI DSS agent controls, FedRAMP/StateRAMP, EU DORA, SOC 1 for billing-touching agents, agent insurance and indemnity language.
- Agent family: agent observability spec, simulator/synthetic-environment spec, fine-tuning/distillation change control, standalone multi-agent coordination ADR catalogue.
- AI incidents: joint primary-and-fallback provider degradation, AI-plus-security incident coordination, customer-harm and liability posture, rolled-up AI-incident KPIs for the responsible-AI review.
- AI on SaaS: AI vendor/procurement assessment pack, fine-tune lineage and approval gate, bias and fairness evaluation deep-dive.
- SaaS: vertical regulatory packs, multi-tenant FinOps, marketplace/app-store docs, contract doc pack (legal handoff), multi-region data residency runbook, tenant migration playbooks (silo/pool/pod).

Each item needs a Digital Research currentness check before it becomes a skill or reference.

## Re-audit

Re-run `python -X utf8 scripts/source_ingestion_guardrail.py` on every skill change. Re-audit by
2026-10-24 that no new extraction-like digest has entered `docs/`.
