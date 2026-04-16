# Skill-Local Path Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Convert every skill-local file (SKILL.md, prompts, references, helpers) under `00-meta-initialization/` through `09-governance-compliance/` from the legacy relative shorthand `../project_context/` and `../output/` to the canonical `projects/<ProjectName>/_context/` and `projects/<ProjectName>/<phase>/` model. Add a deterministic CI check that blocks future drift. Closes Gap #2.

**Architecture:** A two-phase migration. (1) An audit pass produces a CSV of every legacy reference. (2) A bulk edit pass rewrites them, preserving the alias-aware compatibility wording where the file's intent is to document the alias relationship. A new kernel rule (`engine/checks/legacy_paths.py`) inspects every committed skill file and flags any naked legacy reference that isn't inside an `<!-- alias-block -->` HTML comment.

**Tech Stack:** Python (kernel + audit script), Grep for the audit, Edit tool for the rewrites.

---

## File Structure

```
engine/checks/legacy_paths.py        # CI rule
engine/tests/test_check_legacy_paths.py
scripts/audit_skill_paths.py         # one-shot audit + report generator
docs/migration/skill-paths-2026-04-16.csv   # the audit output
docs/migration/skill-paths-2026-04-16.md    # human-readable summary
```

Plus modifications to N skill files (count produced by the audit; expected ~50–80 SKILL.md files).

---

### Task 1: Audit script

**Files:**

- Create: `scripts/audit_skill_paths.py`

- [ ] **Step 1: Write the script**

```python
#!/usr/bin/env python3
"""Find every legacy ../project_context/ and ../output/ reference in skill files."""
from __future__ import annotations
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY = re.compile(r"\.\./project_context/|\.\./output/")
ALIAS_HINT = re.compile(r"\balias\b", re.IGNORECASE)

SKILL_DIRS = [
    "00-meta-initialization", "01-strategic-vision",
    "02-requirements-engineering", "03-design-documentation",
    "04-development-artifacts", "05-testing-documentation",
    "06-deployment-operations", "07-agile-artifacts",
    "08-end-user-documentation", "09-governance-compliance",
]

def main(out_csv: Path) -> int:
    rows = []
    for d in SKILL_DIRS:
        for path in (ROOT / d).rglob("*.md"):
            try:
                body = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for lineno, line in enumerate(body.splitlines(), start=1):
                if not LEGACY.search(line):
                    continue
                marked_alias = ALIAS_HINT.search(body) is not None
                rows.append({
                    "file": str(path.relative_to(ROOT)),
                    "line": lineno,
                    "snippet": line.strip()[:160],
                    "alias_documented_in_file": marked_alias,
                })
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["file", "line", "snippet", "alias_documented_in_file"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} legacy references written to {out_csv}")
    return 0

if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else (ROOT / "docs/migration/skill-paths-2026-04-16.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    sys.exit(main(out))
```

- [ ] **Step 2: Run the audit and inspect the CSV**

```bash
python scripts/audit_skill_paths.py
```

Expected output: a count and the CSV path.

- [ ] **Step 3: Commit script + audit output**

```bash
git add scripts/audit_skill_paths.py docs/migration/skill-paths-2026-04-16.csv
git commit -m "chore(migration): audit legacy ../project_context and ../output references"
```

---

### Task 2: Generate human-readable migration plan

**Files:**

- Create: `docs/migration/skill-paths-2026-04-16.md`

- [ ] **Step 1: Read the CSV** and group by file. For each file, document one of three actions:

  - **REWRITE** — the file uses the legacy path as a substantive instruction (most common). Replace with `projects/<ProjectName>/_context/` or `projects/<ProjectName>/<phase>/`.
  - **WRAP** — the file documents the alias relationship intentionally. Wrap the legacy reference in:

    ```html
    <!-- alias-block start -->
    Legacy alias: `../project_context/` → `projects/<ProjectName>/_context/`
    <!-- alias-block end -->
    ```

  - **DELETE** — the reference is dead documentation (e.g., copied template that no skill currently invokes). Remove the line entirely.

- [ ] **Step 2: Author the file**

```markdown
# Skill-Local Path Migration — 2026-04-16

Source: `skill-paths-2026-04-16.csv` (N references in M files).

## Per-file actions

| File | Action | Notes |
|---|---|---|
| `02-requirements-engineering/waterfall/01-initialize-srs/SKILL.md` | REWRITE | Replace 4 references in steps 2 and 5 |
| `03-design-documentation/01-high-level-design/SKILL.md` | REWRITE | 2 references in the "Inputs" section |
| `00-meta-initialization/new-project/references/path-aliases.md` | WRAP | This file *documents* the alias relationship — wrap, do not rewrite |
| ... | | |
```

(Fill the table from the CSV. The audit count determines how many rows.)

- [ ] **Step 3: Commit**

---

### Task 3: Bulk migration — REWRITE files

For each file marked REWRITE in Task 2:

- [ ] **Step 1: Read the file**

- [ ] **Step 2: Apply the substitutions** using the Edit tool (one Edit per file is fine because the substitutions are deterministic):

  - `../project_context/` → `projects/<ProjectName>/_context/`
  - `../project_context` → `projects/<ProjectName>/_context`
  - `../output/` → `projects/<ProjectName>/<phase>/<document>/`
  - `../output` → `projects/<ProjectName>/<phase>/<document>`

  Where the original file used `<phase>` or `<document>` as a literal placeholder, keep it. Where it referenced a specific phase like `srs/`, expand to `projects/<ProjectName>/02-requirements-engineering/srs/`.

- [ ] **Step 3: Verify the file still parses** (Pandoc dry-run if it's a candidate for `build-doc.sh`):

```bash
pandoc -t docx --reference-doc=templates/reference.docx -o /tmp/check.docx <file> && rm /tmp/check.docx
```

- [ ] **Step 4: Commit each batch of ~10 files** with a focused message, e.g.:

```bash
git add 02-requirements-engineering/waterfall/
git commit -m "refactor(skills): migrate Waterfall SRS skills to canonical pathing"
```

---

### Task 4: WRAP files

For each WRAP file:

- [ ] **Step 1: Locate the alias mention.**

- [ ] **Step 2: Wrap with the HTML comment block** shown in Task 2.

- [ ] **Step 3: Commit one batch.**

---

### Task 5: DELETE references

For each DELETE entry:

- [ ] **Step 1: Confirm the reference is unused** by grepping the file's section for any other consumers.

- [ ] **Step 2: Delete the line(s) and any orphan heading they leave behind.**

- [ ] **Step 3: Commit one batch.**

---

### Task 6: Legacy-paths CI check

**Files:**

- Create: `engine/checks/legacy_paths.py`
- Create: `engine/tests/test_check_legacy_paths.py`

The check scans skill files (not project workspaces) and raises a Finding for any legacy reference that is **not** inside an `<!-- alias-block ... -->` HTML comment.

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from engine.findings import FindingCollection
from engine.checks.legacy_paths import LegacyPathCheck

def test_passes_when_only_alias_block_legacy(tmp_path: Path):
    f = tmp_path / "SKILL.md"
    f.write_text("# Skill\n<!-- alias-block start -->\n`../project_context/`\n<!-- alias-block end -->\n")
    findings = FindingCollection()
    LegacyPathCheck().scan_file(f, findings)
    assert len(findings) == 0

def test_flags_naked_legacy_reference(tmp_path: Path):
    f = tmp_path / "SKILL.md"
    f.write_text("# Skill\nUse the file at ../project_context/vision.md\n")
    findings = FindingCollection()
    LegacyPathCheck().scan_file(f, findings)
    assert len(findings) == 1
```

- [ ] **Step 2: Implement**

```python
"""Legacy-path scanner for skill files."""
from __future__ import annotations
import re
from pathlib import Path
from engine.findings import Finding, FindingCollection, Severity

_LEGACY = re.compile(r"\.\./project_context/|\.\./output/")
_ALIAS_OPEN = re.compile(r"<!--\s*alias-block\s+start\s*-->", re.IGNORECASE)
_ALIAS_CLOSE = re.compile(r"<!--\s*alias-block\s+end\s*-->", re.IGNORECASE)

class LegacyPathCheck:
    gate_id = "kernel.legacy_skill_paths"

    def scan_file(self, path: Path, findings: FindingCollection) -> None:
        body = path.read_text(encoding="utf-8")
        in_alias = False
        for lineno, line in enumerate(body.splitlines(), start=1):
            if _ALIAS_OPEN.search(line):
                in_alias = True
                continue
            if _ALIAS_CLOSE.search(line):
                in_alias = False
                continue
            if in_alias:
                continue
            if _LEGACY.search(line):
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"Legacy path reference outside alias-block: {line.strip()[:120]}",
                    location=path, line=lineno,
                ))
```

- [ ] **Step 3: Register in `engine/cli.py`** behind a new subcommand `validate-skills`:

```python
@main.command("validate-skills")
def validate_skills() -> None:
    """Scan skill files for legacy path references."""
    from engine.checks.legacy_paths import LegacyPathCheck
    findings = FindingCollection()
    chk = LegacyPathCheck()
    for d in ["00-meta-initialization", "01-strategic-vision", "02-requirements-engineering",
              "03-design-documentation", "04-development-artifacts", "05-testing-documentation",
              "06-deployment-operations", "07-agile-artifacts", "08-end-user-documentation",
              "09-governance-compliance"]:
        for p in Path(d).rglob("*.md"):
            chk.scan_file(p, findings)
    if findings.is_blocking:
        for f in findings:
            click.echo(f"- {f.location}:{f.line} {f.message}")
        sys.exit(1)
    click.echo("SKILLS OK: no legacy path references outside alias-blocks.")
```

- [ ] **Step 4: Add to CI workflow**

In `.github/workflows/engine.yml`, add a step:

```yaml
      - run: python -m engine validate-skills
```

- [ ] **Step 5: Verify pass + commit**

```bash
python -m engine validate-skills
pytest engine/tests/test_check_legacy_paths.py -v
git add engine/checks/legacy_paths.py engine/cli.py engine/tests/test_check_legacy_paths.py .github/workflows/engine.yml
git commit -m "feat(engine): add legacy-paths scanner and validate-skills CLI command"
```

---

### Task 7: Update CLAUDE.md to remove the "alias compatibility" disclaimer

**Files:**

- Modify: `CLAUDE.md`

The current "Relative Alias Compatibility" line in the Directory Logic section becomes redundant once the migration is complete. Replace it with a stricter statement.

- [ ] **Step 1: Find the line**

```
- **Relative Alias Compatibility:** Existing skill bodies may still mention `../project_context/` and `../output/`. Treat these as shorthand aliases to the active project's canonical workspace, not as a competing path model.
```

- [ ] **Step 2: Replace with**

```
- **Pathing:** Skill files MUST use the canonical `projects/<ProjectName>/_context/` and `projects/<ProjectName>/<phase>/` paths. Legacy `../project_context/` references are only permitted inside `<!-- alias-block start --> ... <!-- alias-block end -->` HTML comments and are enforced by `python -m engine validate-skills`.
```

- [ ] **Step 3: Commit**

---

## Self-Review

1. **Spec coverage:** All ~50–80 skill files migrated; CI check `kernel.legacy_skill_paths` prevents regression.
2. **Placeholder scan:** None.
3. **Reversibility:** Each REWRITE/WRAP/DELETE batch is its own commit; can be reverted independently.
4. **CI proof:** The `validate-skills` step will fail any PR that introduces a naked legacy reference.
