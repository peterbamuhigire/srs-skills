# SRS engine comprehensive Kaizen review: 2026-09-08

## Frame and evidence boundary

Audience: SRS engine maintainer and release reviewer. Decision: whether the
current local changes can be committed to `main`, and which evidence gaps must
remain open. Scope: this SRS engine checkout, its routers, validation kernel,
tests, and the pending Java requirements overlay.

No client workspace, rendered DOCX, deployment, production system, or
stakeholder approval was assessed. Those outcomes cannot be inferred from
repository tests.

## Currentness review

| Claim | Source and scope | Dates | Freshness, support and decision |
|---|---|---|---|
| `gpt-6-astra` is OpenAI's most capable model for complex reasoning, coding, computer use, research and document creation; public API token prices are $10 input and $50 output per 1M tokens. | [OpenAI GPT-6 Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra), Tier 1 primary source. Scope: public model positioning, supported reasoning efforts and API pricing. | Exact model ID verified; the page displays no publication date. Accessed and verified 2026-09-08; review 2026-10-08. | `time-sensitive`, `verified` for the stated public scope. The active runtime catalogue exposes an Astra reviewer role. No measured latency or repository-specific quality comparison was found, so those checks are `NOT ASSESSED`. Retain Astra for orchestration/review; do not infer a live root-model switch. |
| `gpt-5.6-luna` is the cost-sensitive, high-volume option; public API token prices are $0.20 input and $1.20 output per 1M tokens. | [OpenAI GPT-5.6 Luna model page](https://developers.openai.com/api/docs/models/gpt-5.6-luna), Tier 1 primary source. Scope: public model positioning, supported reasoning efforts and API pricing. | Exact model ID verified; the page displays no publication date. Accessed and verified 2026-09-08; review 2026-10-08. | `time-sensitive`, `verified` for the stated public scope. The active runtime catalogue and role configuration expose Luna execution roles. No measured latency or task-quality benchmark was found, so those checks are `NOT ASSESSED`. Retain Luna for bounded execution. |
| Sol and Terra are available candidates: Sol targets complex professional work at $4/$20 per 1M input/output tokens; Terra balances intelligence and cost at $2/$12. | [OpenAI GPT-5.6 Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol) and [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra) model pages, Tier 1 primary sources. Scope: public positioning and API pricing. | Exact model IDs verified; the pages display no publication dates. Accessed and verified 2026-09-08; review 2026-10-08. | `time-sensitive`, `verified` for the stated public scope. Neither public description proves a better repository-specific quality/cost/latency outcome than the Astra/Luna split. Retain the pins pending a controlled comparison. |
| This Codex configuration selects `gpt-5.6-sol` for the root and Luna for configured execution roles; the active runtime catalogue also exposes Astra and Luna roles. | Active Codex configuration, configured role metadata and runtime tool catalogue. Scope: this account and session environment only. | Observed and verified 2026-09-08; review after any configuration or runtime-catalogue change. | `context-bound`, `verified` for configuration and role availability. The policy check reports root drift. Its authorised bounded repair refused to overwrite user restrictions in the `default` role, so adoption remains open and no broader configuration rewrite is permitted. |
| The Java overlay requires current platform evidence but does not select a Java, framework, server or driver version. | `02-requirements-engineering/references/java-enterprise-requirements-overlay.md` and the Chwezi Dev Engine `docs/source-registers/java-enterprise.md` register. | Reviewed 2026-09-08; recheck on each project decision. | `context-bound`, `verified` as a requirements boundary. Project compatibility and lifecycle conclusions remain `NOT ASSESSED`. |

Model-policy decision: retain Astra for root/reviewer work and Luna for bounded
execution. Do not replace either pin with Sol or Terra without a controlled
task-fit comparison. The running root remains Sol, and the helper's failed
bounded repair does not prove that a model changed.

## Frozen baseline

Observed before this cycle:

- `validate_skill_engine.py`: 157 active skills, one template, zero findings.
- `routing_smoke_test.py`: 52/52 fixtures, top-three precision 1.000.
- `validate_engine.py`: engine contract passed.
- `python -m engine validate-skills`: no legacy project-path findings.
- `source_ingestion_guardrail.py`: zero findings.
- Full tests with repository addopts disabled: 236 passed, 2 skipped.
- Default `pytest` invocation: `NOT ASSESSED` for coverage because
  `pytest-cov` is not installed in this environment.
- Active Claude routing and retained documentation still referenced removed
  home-directory engine mirrors.
- `WaiverRegister.load` accepted duplicate IDs, blank strings, ambiguous field
  types, and scopes capable of leaving the project workspace. The `waive` CLI
  could write those invalid records.

## Evidence scorecard

Scores are equal-weight reviewer judgements tied to the evidence named below;
they are not standards certification.

| Dimension | Baseline | Re-measure | Evidence and remaining deficiency |
|---|---:|---:|---|
| Doctrine | 92 | 92 | `AGENTS.md`, skill-authoring standard, and Kaizen contract are explicit; stakeholder adoption is not assessed. |
| Taxonomy and routing | 88 | 95 | 157/157 structural contracts and 52/52 routes pass; home-mirror routes were replaced with the canonical `www` path. |
| Skill depth | 90 | 91 | Java elicitation, analysis, validation, traceability, strategy, and transition routes share one overlay; representative product execution is not assessed. |
| Applied proof | 86 | 95 | Negative waiver tests increased the suite from 236 to 255 passing tests; the configured 90% coverage gate passes at 95.93%. |
| Standards currency | 80 | 82 | Official model and local-runtime evidence are separated; Java project versions still require claim-level verification. |
| Output readiness | 84 | 85 | Engine and source gates pass; no rendered document was reviewed. |
| Accessibility and inclusion | 80 | 80 | Existing routes are present; no representative accessibility artefact or user evidence was reviewed. |
| Production and handoff | 78 | 80 | Runtime-safety and transition contracts exist; live rollout, recovery, and stakeholder handoff are not assessed. |
| Hygiene | 86 | 94 | Broken cross-engine link, stale engine paths, unsupported token-savings text, and stale roadmap wording were corrected. |
| Safety and integrity | 84 | 94 | Waiver schema, date types, IDs, scope containment, and write-before-validation behavior now have negative tests. |

Baseline raw score: `84.8/100`. Re-measured raw score: `88.8/100`.
Published score under the portfolio rule: `min(88.8, 65) = 65/100`.
Target `95/100` is not achieved.

## Selected experiments and standardisation

### KZ-2026-09-08-01: waiver integrity

- Root cause: waiver input relied on Python/YAML coercion and accepted fields
  without a repository-bound schema.
- Hypothesis: rejecting malformed records before matching or writing will stop
  invalid approvals from suppressing findings or poisoning future runs.
- Change owner: SRS engine maintainer.
- Changes: typed register shape, required and allowed fields, nonblank text,
  unique IDs, controlled date parsing, repository-relative scope validation,
  1-90 day CLI duration, non-applicability outside that window, and validation
  before mutation.
- Failure cases: malformed YAML, falsey or non-mapping root/item, non-list
  collection, blank reason, boolean date, duplicate ID, parent traversal,
  absolute path, drive-qualified path, backslash path, zero-day approval and
  overlong approval.
- Acceptance: focused waiver/Phase 09/CLI tests and the full engine suite pass.
- Rollback: revert the waiver and test changes together; do not retain a CLI
  that writes fields the loader rejects.
- Result: standardised in `engine/waivers.py` and `engine/cli.py` with tests.

### KZ-2026-09-08-02: canonical engine routing

- Root cause: host-specific runtime mirrors were treated as engine sources.
- Hypothesis: routing both Codex and Claude to the
  [Chwezi Dev Engine](https://github.com/peterbamuhigire/chwezi-dev-engine)
  by engine identity removes duplicate repositories, avoids machine-specific
  paths and prevents stale instruction loading.
- Change owner: engine maintainer.
- Changes: active routers, contributor command, setup guide, retained source
  provenance, and historical conformance references now use the canonical path.
- Acceptance: repository search returns no `.agents/skills`, `.agents/doctrine`,
  or `.claude/skills` engine route; structural and routing gates pass.
- Rollback: restore the path edits only if a runtime proves it cannot read the
  canonical checkout and record that capability gap first.
- Result: standardised across the retained SRS documentation set.

## Validation and ship gate

- Structural, routing, engine-contract, legacy-path, and source-ingestion gates:
  pass.
- Full behavioural suite: 255 passed, 2 skipped with `-o addopts=''`.
- Configured suite: 255 passed, 2 skipped; total coverage 95.93%, above the
  required 90% threshold.
- Java project execution, load, failover, recovery, licensing, and stakeholder
  review: `NOT ASSESSED`.
- Render, accessibility user test, and production handoff: `NOT ASSESSED`.
- Anti-slop review: `A` on assessed text/code criteria, with 0 blocking
  findings. Added prose contains no banned filler, placeholder section or
  machine-specific engine checkout path; code checks cover normal and failure
  behaviour. The numeric genericness score is `NOT ASSESSED` because no
  repository-native scorer is available. Visual checks are not applicable to
  this text/code change.

## Backlog to 95/100

| Priority | Gap and action | Owner and review | Acceptance evidence and stop rule |
|---|---|---|---|
| P1 | Reconcile the root Astra pin with the preserved `default` role restrictions; do not replace the role file wholesale. | Peter Bamuhigire; 2026-09-15 | The bounded policy check passes, a newly started session reports the intended root model, and the existing restrictions remain present. Stop if the helper cannot prove preservation. |
| P1 | Execute one representative SRS project chain from requirement through failed-path test, rendered deliverable, approval, and handoff. | Project owner; 2026-09-22 | Trace IDs, test results, render review, stakeholder decision, and rollback evidence exist. |
| P2 | Reconcile remaining historical README capability and count statements against dated release evidence. | Documentation owner; 2026-09-22 | Each current claim has a source/evidence locator or is explicitly historical/not assessed. |

Next re-audit: 2026-09-22. The published score remains capped at 65 until then,
and the 95 target remains a plan rather than a readiness claim.
