# Pathing Model

This repository uses a **single canonical workspace model**:

- Project root: `projects/<ProjectName>/`
- Context root: `projects/<ProjectName>/_context/`
- Generated artifact root: `projects/<ProjectName>/...` under the active phase and document workspace
- Skill entrypoint root: `skills/<skill-name>/SKILL.md`

## Canonical Rule

When repository-level documentation describes where project data lives, it should use the `projects/<ProjectName>/...` form.

Examples:

- `projects/<ProjectName>/_context/vision.md`
- `projects/<ProjectName>/_context/tech_stack.md`
- `projects/<ProjectName>/02-requirements-engineering/...`
- `projects/<ProjectName>/03-design-documentation/...`

## Relative Alias Rule

Many existing `SKILL.md`, `README.md`, `logic.prompt`, and helper files still use:

- `../project_context/`
- `../output/`

These are **execution aliases**, not a second architecture.

Interpret them as:

- `../project_context/` -> the active project's canonical context root, `projects/<ProjectName>/_context/`
- `../output/` -> the active project's generated artifact location for the current workflow or shared artifact set

Use the relative form inside skill-local instructions when preserving established behavior is important. Use the canonical `projects/<ProjectName>/...` form in root documentation, architecture notes, migration guidance, and repository-level analysis. Repository skill references should use `skills/<skill-name>/SKILL.md`.

## Documentation Guidance

- Root docs should describe the canonical workspace model first.
- Skill-local docs may keep relative paths for backward compatibility, but should not imply that `../project_context/` is the source of truth.
- When both forms appear in the same document, explicitly state that the relative paths are aliases to the canonical project workspace.

## Why This Exists

The repository evolved from a simpler relative-path execution model into a project-scoped workspace model. The compatibility goal is:

- keep existing skill bodies usable
- avoid forced directory restructuring
- make the real runtime model clear for Claude Code and Codex

This file is the pathing contract that root documentation should follow.
