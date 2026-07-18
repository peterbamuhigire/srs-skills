# Contributing to the SRS skills engine

Active skills live under the numbered phase roots. Discover them from the filesystem; do not use a cached README table as the catalogue authority.

## Change a skill

1. Read `AGENTS.md`, `CLAUDE.md`, and [the local authoring standard](docs/skill-authoring-standard.md).
2. Start new entrypoints from [the skill template](templates/skill/SKILL.md). Keep the directory name and frontmatter `name` identical.
3. Preserve the skill's domain workflow, examples, references, terminology, and project pathing. Add domain decisions and evidence contracts from real context, not generic compatibility text.
4. Update [routing fixtures](tests/routing-fixtures.json) when a description, trigger, exclusion, or neighbour boundary changes.
5. For finance-touching content, run the finance doctrine quality gate. For human-facing content, apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` before release.

## Required checks

```powershell
python -X utf8 scripts/validate_skill_engine.py --baseline tests/skill-quality-baseline.json
python -X utf8 scripts/routing_smoke_test.py
python -X utf8 scripts/validate_engine.py
python -m engine validate-skills
pytest --cov=engine --cov-fail-under=90
git diff --check
```

Run the canonical quick validator for each changed skill directory:

```powershell
python -X utf8 C:\Users\Peter\.claude\skills\skills\sdlc-meta\skill-writing\scripts\quick_validate.py <skill-directory>
```

The baseline must remain empty. Do not add findings to it. A deliberate active-skill or template-count change requires an evidence-backed routing decision, updated fixtures, and an explicit baseline count update in the same change.

## Release procedure

1. Fetch `origin` and confirm local `main` is not behind `origin/main`.
2. Run the full checks above and inspect the complete diff for unrelated files, secrets, caches, and broken references.
3. Stage only intended files and review the staged stat plus representative skill, validator, fixture, and documentation diffs.
4. Commit once with a message that states the release outcome.
5. Push without force. Verify `HEAD` and `origin/main` resolve to the same commit and the worktree is clean.
