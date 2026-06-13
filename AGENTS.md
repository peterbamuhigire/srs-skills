# Repository Agents Guide

This repository is a dual-compatible skill system for Claude Code and Codex. The portable unit is any directory that contains a `SKILL.md`.

## Purpose

- Preserve the existing Claude Code workflow defined in [CLAUDE.md](/C:/wamp64/www/srs-skills/CLAUDE.md).
- Expose the same skills to Codex through predictable `SKILL.md` frontmatter, local references, and repo-level routing rules.
- Keep portable skill entrypoints under `skills/<skill-name>/SKILL.md`.

## Skill Families

- Portable skills live under `skills/skills/<category>/<skill-name>/SKILL.md` (the `skills/` directory is a git submodule whose internal `skills/` namespace is grouped into 15 categories — see the "Skill Categories" section in `CLAUDE.md`). Methodology-selection skills such as `00-meta-initialization` live at the outer numbered-phase roots (e.g. `01-strategic-vision/`).
- Root directories are reserved for project documentation and repository-level folders such as `docs/`, `skills/` (submodule), and `projects/`, plus operational folders (`engine/`, `templates/`, `scripts/`, `domains/`) where relevant.
- Domain packs live under `domains/`. They are not skills by themselves; use them as context sources when a task is domain-specific.

## Baseline Routing

- New client-documentation or methodology-selection requests: start with `skills/00-meta-initialization`.
- SDLC document generation or review: route to the relevant numbered phase skill first, then load supporting domain references from `domains/<domain>/`.
- General software engineering work: start with `skills/skills/sdlc-meta/world-class-engineering`, then add the narrowest relevant skills.
- Skill authoring or upgrades inside this repository: use `skills/skills/sdlc-meta/skill-writing`.
- Word or `.docx` output quality work: use `skills/skills/product-business/professional-word-output`.
- BDS programme intake, selection, monitoring, or donor dashboard requirements: use `skills/skills/product-business/bds-intake-and-monitoring-system-spec`.
- E-commerce platform, payment, API, AI, data-protection, or integration audit requirements: use `skills/skills/architecture/ecommerce-platform-audit-requirements`.
- Anti-AI-slop pre-ship gate: run `09-governance-compliance/28-anti-ai-slop` on every generated SRS/spec/doc/code artefact before delivery (MANDATORY).
- Slop analysis/audit: `09-governance-compliance/29-ai-slop-audit` auto-runs whenever the user asks to analyse, review, evaluate, audit, critique, or de-slop any spec, requirement, document, system, or codebase, or asks "does this look AI-generated?".

## Cross-Engine Handoffs

- Proposal to SRS: consume proposal scope, win themes, assumptions, exclusions, service promises, commercial options, and support commitments as discovery inputs. Convert them into requirements, acceptance criteria, traceability, risks, and evidence obligations before implementation starts.
- Website proposal to SRS: when a premium website includes portal, SaaS, ecommerce, AI, integration, data, compliance, or operational workflow scope, create SRS/PRD artefacts before website delivery commits to build details.
- SRS to implementation: hand off signed PRD/SRS, HLD/LLD, API/database specs, ADRs, UX/content/form specs, RTM, test strategy, deployment guide, go-live readiness, and customer adoption/support plan to the master engineering engine.
- SRS to website delivery: hand off sitemap-affecting requirements, content/form requirements, accessibility and performance constraints, launch criteria, analytics events, and support obligations to the website engine.
- Implementation to maintenance/support: require runbooks, release notes, service levels, escalation rules, known issues, training materials, and feedback loops before closing Phase 06.

## Working Rules

- Treat each `SKILL.md` as the execution entrypoint and its local `references/`, `templates/`, `logic.prompt`, `protocols/`, and helper scripts as supporting assets.
- Prefer the closest local instructions over broad repo-level assumptions.
- Keep changes additive and in place. Preserve existing Claude-facing prompts, terminology, and invocation patterns unless they are actually broken.
- Do not duplicate logic between `SKILL.md` and reference files when a short link is enough.
- When a skill has both concise metadata and a longer body, use metadata for routing and the body for execution detail.

## Pathing Model

- The canonical project workspace model is `projects/<ProjectName>/...`.
- The source of truth for project context is `projects/<ProjectName>/_context/`.
- Every project workspace must include the DOCX export contract: `projects/<ProjectName>/export/`, `projects/<ProjectName>/export-docs.ps1`, and `projects/<ProjectName>/export-docs.sh`. Generated Word deliverables remain in their phase folders, then the export script copies all `.docx` files into `export/` for delivery.
- Existing skill-local references such as `../project_context/` and `../output/` should be treated as execution aliases into the active project workspace, not as a separate architecture.
- Root documentation should prefer the canonical model described in [docs/pathing-model.md](/C:/wamp64/www/srs-skills/docs/pathing-model.md).

## Quality Bar

- Outputs must be specific, grounded in local context, and appropriate for production or delivery review.
- Do not invent missing requirements or hidden project context.
- Use local standards, checklists, and references before falling back to generic knowledge.
- If a skill points to upstream or downstream skills, respect that sequence unless the user explicitly narrows the task.
- Premium, world-class quality is the default for this engine. SRS, PRD, UX, architecture, and business-case outputs must support premium products and serious clients by default, not commodity or lowest-cost positioning.
- Premium requirements must make value visible through product packaging, simple usable UX, buyer proof, service quality, content/SEO authority where relevant, pricing power, and high-value sales/proposal assets.
- When a project targets cheap, vague, low-trust, or sub-premium work, treat it as a poor-fit engagement. Recommend narrowing scope to a premium deliverable, raising discovery/quality requirements, or declining the work rather than lowering the SRS quality bar.
- Use `01-strategic-vision/07-premium-product-positioning` whenever buyer trust, executive adoption, high-ticket pricing, affluent/elite users, or premium product experience matters.
- No generated artefact ships if it reads as AI slop. Run `09-governance-compliance/28-anti-ai-slop` as the pre-ship gate: every section must carry a concrete `_context/`-grounded element, every quality attribute a defined IEEE-982.1 / ISO 25010 metric, every requirement a deterministic test oracle, and no hallucinated API, package, or citation. Use the banned-vocabulary list and the SRS/spec avoidance block.

## Document and Spreadsheet Tooling

- Before promising `.docx`, `.pdf`, `.xlsx`, application registers, scoring matrices, budgets, monitoring dashboards, reports, or annexes, check whether document and spreadsheet tooling is available.
- Prefer built-in Codex/Claude document and spreadsheet plugins where available. If unavailable, use local Python libraries such as `openpyxl`, `XlsxWriter`, `pandas`, `python-docx`, `docxtpl`, `docxcompose`, `pypandoc`, `markdown`, `PyMuPDF`, `pypdf`, `pdfplumber`, and `reportlab`.
- Check binaries such as `pandoc`, LibreOffice/`soffice`, `wkhtmltopdf`, and `tesseract` when conversion or OCR is needed.
- Run a minimal DOCX/XLSX smoke test on a new machine before production export.
- Never claim a generated Word, PDF, or Excel file exists unless it was actually written and opened or validated.

## Compatibility Notes

- `CLAUDE.md` remains the Claude-specific root protocol and should not be replaced by this file.
- `AGENTS.md` provides Codex-facing baseline behavior and repository routing.
- `SKILL.md` files carry a portable metadata contract so both assistants can identify use conditions, inputs, workflow expectations, quality gates, anti-patterns, outputs, and references from the standard `skills/<skill-name>/SKILL.md` layout.


## Finance & Accounting Trigger

Load `doctrine/accounting-finance-doctrine.md` whenever the user's request, the artefact being generated, or the code being edited touches **any** of:

- Money flows: sales, purchases, payments, refunds, credit notes, expenses
- Stock and inventory
- Payroll
- Tax (VAT, PAYE, WHT, NSSF, income tax, customs, excise, EFRIS, eTIMS)
- Grants, donations, donor restrictions
- Banking, mobile money, POS, card settlement, cash drawer
- Fixed assets
- Financial reports, management accounts, statutory returns
- Chart of Accounts, journals, ledger, posting services, period state, audit trail
- Reconciliation, close, migration, opening balances
- Internal controls, audit, evidence packs
- Any IFRS or IFRS for SMEs section

When the trigger fires:

1. Read `doctrine/accounting-finance-doctrine.md`.
2. Read the relevant doctrine reference file under `doctrine/references/`.
3. Read the relevant skill `SKILL.md` under `skills/finance/`.
4. Apply the **finance & accounting quality gate** from `doctrine/governance/finance-accounting-quality-gate.md`.
5. Record the gate run in the artefact manifest.

The `finance-module-audit` skill (at `skills/finance/finance-module-audit/`) auto-runs whenever the user asks to analyse, review, audit, build, propose, or replace any software system with even a slight finance element.

