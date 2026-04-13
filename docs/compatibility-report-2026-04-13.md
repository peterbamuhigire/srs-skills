# Dual Compatibility Upgrade Report

## Summary

This repository already supported Claude Code well, but its skill corpus was not consistently shaped for a second assistant runtime. The main issues were inconsistent `SKILL.md` structure, one missing YAML frontmatter block, uneven signaling for inputs and outputs, and the absence of a Codex-oriented root instruction file.

The upgrade keeps the existing directory layout and Claude workflows intact. Compatibility is layered on top through repo-level `AGENTS.md` guidance and a portable frontmatter metadata contract added to each `SKILL.md`.

## What Was Wrong

- The repository had 256 `SKILL.md` files with mixed formats across two major families.
- Only 1 skill lacked YAML frontmatter, but many skills exposed inputs, workflow, outputs, and anti-patterns through inconsistent headings.
- There was no Codex-native repository entrypoint comparable to the existing Claude protocol in `CLAUDE.md`.
- Some skills assumed Claude-centric invocation patterns without a compact machine-readable contract for other agents.

## What Was Improved

- Added a root `AGENTS.md` that explains repository purpose, routing, baseline working rules, and compatibility expectations.
- Added `skills/AGENTS.md` to clarify the general-purpose library behavior and composition rules.
- Added a portable `metadata` contract to every `SKILL.md` so each skill now exposes:
  - use conditions
  - do-not-use conditions
  - required inputs
  - workflow expectations
  - quality standards
  - anti-patterns
  - outputs
  - references
- Repaired the one `SKILL.md` that lacked YAML frontmatter.
- Added a repeatable migration script at [scripts/upgrade_dual_compat_skills.py](/C:/wamp64/www/srs-skills/scripts/upgrade_dual_compat_skills.py) so the portability layer can be re-applied or audited later.

## Why These Changes Matter

- Claude Code keeps using existing `SKILL.md` bodies, prompts, and phase structure without forced relocation.
- Codex now has a stable, compact contract in each skill file and a repo-level routing guide, which reduces ambiguity during skill selection.
- Future maintenance is simpler because compatibility rules live alongside the repo rather than in a separate duplicated system.

## Optional Next Steps

- Tighten a few of the longest skills so they stay comfortably below the repository's preferred 500-line guideline even after metadata additions.
- Extend the lightweight validator in `skills/skill-writing/scripts/quick_validate.py` to verify the new metadata contract.
- Add targeted nested `AGENTS.md` files only where a subtree has genuinely different operating rules.
