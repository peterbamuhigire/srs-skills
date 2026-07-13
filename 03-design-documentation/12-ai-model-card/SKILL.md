---
name: 12-ai-model-card
description: Use when a production AI feature needs a version-specific model card covering purpose, data, evaluation, limitations, bias, intended use, prohibited use and operational pins; use AI architecture for system design and evaluation artefacts as evidence inputs.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# AI Model Card Skill
<!-- dual-compat-start -->
## Use When

- A feature/model/prompt configuration is ready for release review or material update.

## Do Not Use When

- Do not use for an unevaluated experiment or to copy a provider card as proof of the deployed system.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Deployed configuration pins and provider evidence | AI architecture, prompt registry and provider sources | Required | Stop if the deployable cannot be identified reproducibly. |
| Evaluation, red-team, data and incident evidence | Current project evidence | Required | Mark each missing check `not assessed` and block certification claims. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Versioned AI Model Card through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Versioned AI Model Card to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Versioned AI Model Card | Users, buyers, risk reviewers, auditors and operations | Every claim cites deployment-specific evidence; limitations and prohibited uses are explicit; missing assessments are not reported as passes. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Versioned AI Model Card draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence describes deployed feature and version | Include with source/date | Card remains auditable |
| Only provider-level evidence exists | Qualify applicability and require system evaluation | Generic claims do not certify the product |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Copying the provider model card. Fix: document the deployed feature, prompts, retrieval and controls.
- Omitting limitations. Fix: name measured and unassessed failure modes.
- Reporting an eval score without dataset/date. Fix: cite both and the version pin.
- Calling bias mitigated without subgroup evidence. Fix: report scope and residual risk.
- Using the card as a compliance certificate. Fix: state evidence and reviewer authority precisely.

## References

- [Model card template](references/ai-model-card-template.md)
- [AI Architecture neighbour](../11-ai-architecture-spec/SKILL.md)
<!-- dual-compat-end -->




## Overview

Produces the per-feature model card that buyers, auditors, and Responsible-AI reviewers will read. Anchored in Mitchell et al. (2019) and the EU AI Act Annex IV technical documentation requirements.

## Core Instructions

### Step 1: Identify the artefact under cardification

A model card refers to a deployed combination: { feature, base model + version, prompt registry tag, retrieval index version, post-processing rules }. Pin all four.

### Step 2: Purpose section

Describe what the feature does, who uses it, what decisions it informs, and the buyer outcome. Reference the AI FR ID.

### Step 3: Training and grounding data summary

For hosted base models, cite the provider's training-data disclosure with a date. For our retrieval data, summarise: sources (cite the AI Data Spec), volumes, languages, freshness, exclusions. For fine-tunes, list training set, size, labelling provenance, holdout set.

### Step 4: Evaluation metrics

Attach the most recent eval report for the feature: golden-set pass rate, factuality, abstention precision, citation rate, hallucination rate, judge-LLM score, latency P95, cost per call. Each metric carries the date and the eval set ID.

### Step 5: Red-team summary

Latest red-team result by category: prompt injection, jailbreak, data exfiltration, cross-tenant leak, PII surfacing, hallucination probe, bias surfacing. Pass / fail per category; any open finding with severity and remediation date.

### Step 6: Limitations

List known limitations as concrete failure modes:

- Knowledge cutoff date for the base model.
- Languages or locales not yet evaluated.
- Domain edge cases the eval set under-represents.
- Latency degradation conditions.

### Step 7: Bias notes and mitigations

List bias risks identified (gender, race, age, disability, geography, language) and the mitigation in place (eval set composition, abstain rule, content filter, human-in-the-loop).

### Step 8: Intended use and out-of-scope use

Intended use: business contexts the feature supports. Out-of-scope: contexts where it must not be used (e.g. medical decisions, legal advice, hiring, lending). Mirror the safety rules in the PRD spec.

### Step 9: Operational pins

Model + version, prompt registry tag, retrieval index version, gateway config tag, content-filter version, eval suite tag.

### Step 10: EU AI Act Annex IV cross-walk

Map each Annex IV element to the section of this model card that satisfies it:

| Annex IV item | Where covered |
|----------------|----------------|
| General description of the AI system | Purpose |
| Elements of the AI system and process of its development | Training/Grounding + Operational Pins |
| Data sets used | Training/Grounding + AI Data Spec |
| Validation and testing procedures | Evaluation + Red-team |
| Risk management measures | Limitations + Bias + Operational Pins |
| Human oversight | Intended Use + AI FR clause |
| Changes through the lifecycle | Versioning section |

### Step 11: Write the card

`Model_Card_<feature>_v<version>.md`. Date-stamped. Owner named.

## Standards

- Mitchell et al. (2019) Model Cards for Model Reporting
- EU AI Act Annex IV
- NIST AI RMF MEASURE
- ISO/IEC 42001
