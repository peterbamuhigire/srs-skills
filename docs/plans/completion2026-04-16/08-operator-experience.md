# Operator Experience Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Reduce the engine's dependence on senior human operators by adding pre-flight diagnostics, golden-path scaffolds, autofill prompts for `[CONTEXT-GAP]` markers, and a worked example next to every skill so a junior consultant can produce defensible output. Closes Gap #10.

**Architecture:** Three additions on top of the kernel. (1) `engine doctor` — a pre-flight that checks Python version, Pandoc availability, submodule init, and project workspace shape, and prints actionable fixes. (2) `engine scaffold` — a guided `new-project` wrapper that pre-populates `_context/` with detailed prompts. (3) Per-skill `examples/` directory containing one minimal, valid input + expected output. The new-project flow optionally clones a chosen example into the freshly scaffolded project so the junior operator sees what "good" looks like.

**Tech Stack:** Python (CLI), markdown.

---

## File Structure

```
engine/
├── doctor.py
├── scaffold.py
├── tests/
│   ├── test_doctor.py
│   └── test_scaffold.py

00-meta-initialization/new-project/
├── examples/
│   ├── healthcare-saas/
│   │   ├── _context/
│   │   │   ├── vision.md
│   │   │   ├── stakeholders.md
│   │   │   ├── features.md
│   │   │   ├── glossary.md
│   │   │   └── methodology.md
│   │   └── README.md
│   ├── finance-erp/
│   ├── education-lms/
│   └── uganda-public-sector/
└── prompts/
    └── context-gap-fillers.md

<phase>/<skill>/examples/        # per-skill worked example, see Task 4
```

---

### Task 1: `engine doctor` pre-flight

**Files:**

- Create: `engine/doctor.py`
- Create: `engine/tests/test_doctor.py`
- Modify: `engine/cli.py` (add `doctor` subcommand)

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from click.testing import CliRunner
from engine.cli import main

def test_doctor_reports_pandoc_missing(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("PATH", "")  # hide every binary
    rc = CliRunner().invoke(main, ["doctor"])
    assert rc.exit_code != 0
    assert "pandoc" in rc.output.lower()
    assert "install" in rc.output.lower() or "fix:" in rc.output.lower()

def test_doctor_passes_in_healthy_env():
    rc = CliRunner().invoke(main, ["doctor"])
    # Will pass if developer ran setup; only assertion: human-readable section headings.
    assert "Python" in rc.output
    assert "Pandoc" in rc.output
```

- [ ] **Step 2: Implement**

```python
"""engine doctor: pre-flight diagnostics."""
from __future__ import annotations
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable, List

@dataclass
class Check:
    name: str
    fn: Callable[[], tuple[bool, str]]
    fix_hint: str

def _check_python() -> tuple[bool, str]:
    ok = sys.version_info >= (3, 11)
    return ok, f"Python {sys.version.split()[0]}"

def _check_pandoc() -> tuple[bool, str]:
    p = shutil.which("pandoc")
    if not p:
        return False, "pandoc not on PATH"
    out = subprocess.check_output([p, "--version"], text=True).splitlines()[0]
    return True, out

def _check_engine_imports() -> tuple[bool, str]:
    try:
        import engine.cli as _  # noqa
        return True, "engine package importable"
    except Exception as exc:  # pragma: no cover
        return False, f"engine import failed: {exc}"

def _check_submodule() -> tuple[bool, str]:
    from pathlib import Path
    skills = Path("skills")
    if not skills.is_dir():
        return False, "skills/ submodule directory not present"
    if not any(skills.iterdir()):
        return False, "skills/ submodule is empty (run `git submodule update --init`)"
    return True, "skills submodule populated"

CHECKS: List[Check] = [
    Check("Python ≥ 3.11", _check_python, "Install Python 3.11 or newer."),
    Check("Pandoc available", _check_pandoc, "Install Pandoc: https://pandoc.org/installing.html"),
    Check("Engine package", _check_engine_imports, "Run `pip install -e .[dev]` from repo root."),
    Check("Skills submodule", _check_submodule, "Run `git submodule update --init --recursive`."),
]

def run() -> int:
    failed = 0
    for chk in CHECKS:
        ok, detail = chk.fn()
        status = "OK " if ok else "FAIL"
        print(f"[{status}] {chk.name}: {detail}")
        if not ok:
            print(f"      fix: {chk.fix_hint}")
            failed += 1
    if failed:
        print(f"\n{failed} check(s) failed.")
        return 1
    print("\nAll checks passed.")
    return 0
```

- [ ] **Step 3: Wire CLI**

```python
@main.command()
def doctor() -> None:
    """Run pre-flight diagnostics."""
    from engine.doctor import run
    sys.exit(run())
```

- [ ] **Step 4: Verify pass + commit**

```bash
pytest engine/tests/test_doctor.py -v
git add engine/doctor.py engine/cli.py engine/tests/test_doctor.py
git commit -m "feat(engine): add doctor pre-flight command"
```

---

### Task 2: Context-gap autofill prompts

**Files:**

- Create: `00-meta-initialization/new-project/prompts/context-gap-fillers.md`

The most common operator failure is leaving `[CONTEXT-GAP: <topic>]` markers unresolved. This file provides one short, opinionated prompt per topic so the consultant can paste into the LLM, get a draft, and edit.

- [ ] **Step 1: Author the file**

```markdown
# Context-Gap Fillers

When the validation kernel reports `[CONTEXT-GAP: <topic>]`, paste the matching prompt below into a fresh assistant chat. Edit the placeholders. Drop the result into `_context/<file>.md`.

## stakeholders

> "I am writing the Stakeholders section of an SRS for a {one-line project description}. The deployment is in {country/region} for {industry}. List 6–10 distinct stakeholder roles, each with: a one-sentence role description, the primary outcome they want, and one constraint they impose on the system. Format as a markdown bullet list. Use the **Bold-then-detail** convention."

## features

> "I am writing the Features section of an SRS for {one-line project description}. The Vision is: {paste vision.md content}. List 8–15 features. Each feature: an `F-N` ID, a 4-word name, one driving stakeholder (must match a stakeholder we already wrote), one measurable success outcome. No vague adjectives."

## glossary

> "I am writing the Glossary for an SRS in the {industry} domain operating in {country/region}. Identify every domain-specific term used in the following text and provide an unambiguous, single-sentence definition for each. Use **Term:** definition format. Source: {paste vision.md + features.md}."

## quality-standards

> "Generate the Quality Standards file for an SRS that targets the following compliance frameworks: {list, e.g. Uganda DPPA 2019, PCI-DSS v4.0}. For each framework, list 3–5 measurable quality attributes the system must meet, with the framework clause referenced in brackets. No vague adjectives."

## methodology

> "We are using the {Waterfall|Agile|Hybrid} methodology. The change-control body is {name}. Sprint cadence: {N weeks, or N/A}. Baseline lock cadence: {date or condition}. Generate methodology.md."
```

- [ ] **Step 2: Reference from CLAUDE.md** — add a line to the V&V SOP: "When the kernel reports `[CONTEXT-GAP: <topic>]`, the consultant SHOULD consult `00-meta-initialization/new-project/prompts/context-gap-fillers.md` before authoring from scratch."

- [ ] **Step 3: Commit**

---

### Task 3: Golden-path example projects

**Files:**

- Create: `00-meta-initialization/new-project/examples/healthcare-saas/_context/{vision,stakeholders,features,glossary,methodology}.md`
- Create: `00-meta-initialization/new-project/examples/healthcare-saas/README.md`
- Repeat for `finance-erp/`, `education-lms/`, `uganda-public-sector/`

Each example is a minimal but **kernel-passing** `_context/` set: 1 vision paragraph, 4 stakeholders, 6 features, 12 glossary terms, methodology.md. They serve as fillable templates and as kernel test fixtures.

- [ ] **Step 1: Author the four examples** — keep each file under 60 lines.

- [ ] **Step 2: Author each README.md** — explains the example's domain assumptions, regulatory context, and which compliance bundle it pre-selects.

- [ ] **Step 3: Add a CI test** that runs `python -m engine validate <example>` against each example and asserts PASS:

`engine/tests/test_examples_validate.py`:

```python
from pathlib import Path
import subprocess
import sys
import pytest

EXAMPLES = sorted(Path("00-meta-initialization/new-project/examples").iterdir())

@pytest.mark.parametrize("example", EXAMPLES, ids=lambda p: p.name)
def test_example_passes_engine_validation(example: Path):
    rc = subprocess.call([sys.executable, "-m", "engine", "validate", str(example)])
    assert rc == 0, f"Example {example.name} fails validation"
```

- [ ] **Step 4: Commit**

---

### Task 4: Per-skill worked examples

For every skill SKILL.md, add a sibling `examples/` directory containing **one** worked example consisting of:

- `inputs/` — minimal `_context/` slice the skill consumes
- `expected-output/` — the markdown the skill is expected to produce
- `README.md` — one paragraph explaining what makes this example representative

This is bulk work but mechanical. The audit script from Plan 04 Task 1 enumerates every SKILL.md; pair its output with this task.

- [ ] **Step 1: Pick the 10 most-used skills** (per the existing `skill_overview.md` registry). Examples to ship in this iteration:

  1. `01-strategic-vision/01-prd-generation/`
  2. `02-requirements-engineering/waterfall/01-initialize-srs/`
  3. `02-requirements-engineering/agile/01-user-story-generation/`
  4. `03-design-documentation/01-high-level-design/`
  5. `03-design-documentation/04-database-design/`
  6. `05-testing-documentation/02-test-plan/`
  7. `06-deployment-operations/04-runbook/`
  8. `07-agile-artifacts/02-definition-of-done/`
  9. `09-governance-compliance/01-traceability-matrix/`
  10. `09-governance-compliance/03-compliance/`

- [ ] **Step 2: For each skill** — create `examples/representative/` with the three files above. Reuse fragments from `examples/healthcare-saas/_context/` so the same input fixtures power many examples.

- [ ] **Step 3: Add a SKILL.md update** — append "## Worked example" section pointing to `examples/representative/`.

- [ ] **Step 4: Commit per skill** so each commit is reviewable in isolation.

---

### Task 5: `engine new-project` wrapper

**Files:**

- Create: `engine/scaffold.py`
- Create: `engine/tests/test_scaffold.py`
- Modify: `engine/cli.py`

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from click.testing import CliRunner
from engine.cli import main

def test_new_project_creates_canonical_workspace(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    rc = CliRunner().invoke(main, [
        "new-project", "TestProject",
        "--methodology", "hybrid",
        "--domain", "uganda",
        "--example", "uganda-public-sector",
    ])
    assert rc.exit_code == 0, rc.output
    project = tmp_path / "projects" / "TestProject"
    assert (project / "_context" / "vision.md").exists()
    assert (project / "_context" / "methodology.md").read_text().lower().count("hybrid") >= 1
    assert (project / "_registry" / "controls.yaml").exists()
    assert (project / "_registry" / "baseline-trace.yaml").exists()
```

- [ ] **Step 2: Implement** — copy the chosen example into `projects/<Name>/`, then post-process `methodology.md` to set the requested methodology, and run `python -m engine sync <Name>` to populate the registries.

- [ ] **Step 3: CLI wiring**

```python
@main.command("new-project")
@click.argument("name")
@click.option("--methodology", type=click.Choice(["waterfall", "agile", "hybrid"]), required=True)
@click.option("--domain", required=True)
@click.option("--example", default=None, help="Optional example to clone as starting point.")
def new_project(name: str, methodology: str, domain: str, example: str | None) -> None:
    from engine.scaffold import scaffold
    scaffold(Path("projects") / name, methodology, domain, example)
    click.echo(f"Scaffolded projects/{name}.")
```

- [ ] **Step 4: Update CLAUDE.md** — under "New Project Protocol" add: "After the brainstorming session captures the 5 answers, run `python -m engine new-project <Name> --methodology <m> --domain <d> --example <e>`. The brainstorm chooses `<e>` from the available golden-path examples; the kernel handles the scaffolding mechanics."

- [ ] **Step 5: Commit**

---

### Task 6: Two-line documentation polish

**Files:**

- Modify: `SETUP_GUIDE.md`
- Modify: `README.md`

- [ ] **Step 1: SETUP_GUIDE.md** — add to the "Quick Start" section the literal commands a brand-new operator runs:

```bash
git clone --recurse-submodules https://github.com/peterbamuhigire/srs-skills.git
cd srs-skills
pip install -e ".[dev]"
python -m engine doctor
python -m engine new-project Acme --methodology waterfall --domain healthcare --example healthcare-saas
python -m engine validate projects/Acme
```

- [ ] **Step 2: README.md** — add a "Junior operator quick path" callout at the top of the existing usage section, linking to SETUP_GUIDE.md.

- [ ] **Step 3: Commit**

---

## Self-Review

1. **Spec coverage:** Pre-flight (Task 1), context-gap autofill (Task 2), golden-path examples (Tasks 3 + 5), per-skill worked examples (Task 4), one-line scaffold command (Task 5). Junior operator path is a single command.
2. **Placeholder scan:** None.
3. **Verifiability:** `test_examples_validate.py` keeps every shipped example green forever.
4. **Operator load:** Tasks 1–5 reduce the cognitive load required at every entry point — install, start a project, fill a gap, see what good looks like.
