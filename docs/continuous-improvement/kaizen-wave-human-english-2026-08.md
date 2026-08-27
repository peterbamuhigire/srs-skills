# Kaizen Wave — Human English for SRS and Product Documentation

Date: 2026-08-27
Scope: requirements, UX content, user manuals, FAQs, release notes, runbooks, training, support messages, and technical documentation.

## Baseline

This language-craft screening scored 58/100; it is not a requirements, security, accessibility, or release certification. Strengths were traceability, measurable quality attributes, anti-slop controls, and UX form gates. Gaps were the absence of a local synthesis of the supplied books and no single overlay connecting technical exactness with calm, grammatical user-facing language.

## Root cause

The engine distinguished testable technical requirements from prose quality, but language guidance was mostly embedded in anti-slop and UX rules. A shared reference was needed for terminology, grammar, reader task, state copy, and proof.

## Improvement implemented

- Added `book-extractions/human-english-craft-synthesis-2026.md` with source limits, five passes, documentation register, microcopy test, grammar/lexical checks, and anti-slop questions.
- Routed it through `AGENTS.md`, `28-anti-ai-slop`, and UX content/form specification.
- Preserved IEEE/ISO, traceability, security, accessibility, and test-oracle authority; prose quality cannot make an untestable requirement pass.

## Engine-level experiment and evidence

Experiment: verify that the local reference exists and is linked from the router and two documentation gates.
Success criterion: links resolve and measurable requirement controls remain unchanged.
Result: PASS — the local reference and two documentation links resolve. User-facing improvement remains unclaimed until representative documents receive human review.

## Guardrails and rollback

On failure, remove only the new links and retain existing V&V gates. Never add casual ambiguity, fake empathy, typos, or subjective adjectives to make technical copy seem human.

## Acceptance and next review

Review one requirement set, one UX form specification, one user manual section, one FAQ, and one error-state matrix with two human reviewers. Require exact actors/states, measurable criteria, consistent terms, grammatical microcopy, recovery instructions, and zero blocking anti-slop findings. Re-audit date: 2026-09-26.
