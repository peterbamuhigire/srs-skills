# Repository Agents Guide

This repository is a dual-compatible skill system for Claude Code and Codex. The portable unit is any directory that contains a `SKILL.md`.

## Purpose

- Preserve the existing Claude Code workflow defined in [CLAUDE.md](/C:/wamp64/www/srs-skills/CLAUDE.md).
- Expose the same skills to Codex through predictable `SKILL.md` frontmatter, local references, and repo-level routing rules.
- Keep skills in place. Do not relocate them unless a path is actually broken.

## Skill Families

- Phase-based SDLC skills live at the repository root in directories such as `00-meta-initialization/`, `01-strategic-vision/`, and `02-requirements-engineering/`. These generate or review lifecycle documents for client workspaces.
- General-purpose engineering skills live under `skills/`. These are reusable technical and product skills for architecture, implementation, security, UX, data, operations, and planning.
- Domain packs live under `domains/`. They are not skills by themselves; use them as context sources when a task is domain-specific.

## Baseline Routing

- New client-documentation or methodology-selection requests: start with `00-meta-initialization`.
- SDLC document generation or review: route to the relevant numbered phase skill first, then load supporting domain references from `domains/<domain>/`.
- General software engineering work: start with `skills/world-class-engineering`, then add the narrowest relevant skills.
- Skill authoring or upgrades inside this repository: use `skills/skill-writing`.
- Word or `.docx` output quality work: use `professional-word-output` or `skills/professional-word-output`, depending on which path the current workflow already references.

## Working Rules

- Treat each `SKILL.md` as the execution entrypoint and its local `references/`, `templates/`, `logic.prompt`, `protocols/`, and helper scripts as supporting assets.
- Prefer the closest local instructions over broad repo-level assumptions.
- Keep changes additive and in place. Preserve existing Claude-facing prompts, terminology, and invocation patterns unless they are actually broken.
- Do not duplicate logic between `SKILL.md` and reference files when a short link is enough.
- When a skill has both concise metadata and a longer body, use metadata for routing and the body for execution detail.

## Pathing Model

- The canonical project workspace model is `projects/<ProjectName>/...`.
- The source of truth for project context is `projects/<ProjectName>/_context/`.
- Existing skill-local references such as `../project_context/` and `../output/` should be treated as execution aliases into the active project workspace, not as a separate architecture.
- Root documentation should prefer the canonical model described in [docs/pathing-model.md](/C:/wamp64/www/srs-skills/docs/pathing-model.md).

## Quality Bar

- Outputs must be specific, grounded in local context, and appropriate for production or delivery review.
- Do not invent missing requirements or hidden project context.
- Use local standards, checklists, and references before falling back to generic knowledge.
- If a skill points to upstream or downstream skills, respect that sequence unless the user explicitly narrows the task.

## Compatibility Notes

- `CLAUDE.md` remains the Claude-specific root protocol and should not be replaced by this file.
- `AGENTS.md` provides Codex-facing baseline behavior and repository routing.
- `SKILL.md` files now carry a portable metadata contract so both assistants can identify use conditions, inputs, workflow expectations, quality gates, anti-patterns, outputs, and references without changing directory layout.
