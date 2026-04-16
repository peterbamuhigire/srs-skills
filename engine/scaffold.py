"""engine new-project scaffolding."""
from __future__ import annotations
import shutil
from pathlib import Path
from typing import Optional


EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "00-meta-initialization" / "new-project" / "examples"


def scaffold(project_root: Path, methodology: str, domain: str, example: Optional[str]) -> None:
    """Create project_root, optionally seeded from an example.

    Post-processes _context/methodology.md to set `methodology: <methodology>`.
    """
    project_root = Path(project_root).resolve()
    if project_root.exists():
        raise FileExistsError(f"{project_root} already exists")
    project_root.mkdir(parents=True)
    if example:
        src = EXAMPLES_DIR / example
        if not src.is_dir():
            raise FileNotFoundError(f"Example '{example}' not found in {EXAMPLES_DIR}")
        for item in src.iterdir():
            if item.name == "README.md":
                continue  # don't copy the example readme
            if item.is_dir():
                shutil.copytree(item, project_root / item.name)
            else:
                shutil.copy2(item, project_root / item.name)
    else:
        (project_root / "_context").mkdir()
        (project_root / "_context" / "vision.md").write_text("# Vision\n", encoding="utf-8")
        (project_root / "_context" / "stakeholders.md").write_text("# Stakeholders\n", encoding="utf-8")
        (project_root / "_context" / "features.md").write_text("# Features\n", encoding="utf-8")
        (project_root / "_context" / "glossary.md").write_text("# Glossary\n", encoding="utf-8")
    # Always (re)write methodology.md with the chosen methodology
    methodology_path = project_root / "_context" / "methodology.md"
    methodology_path.parent.mkdir(exist_ok=True)
    methodology_path.write_text(
        f"---\nmethodology: {methodology}\ndomain: {domain}\n---\n# Methodology\n",
        encoding="utf-8",
    )
    # Seed _registry/ if not present; for hybrid, seed baseline-trace.yaml; for all, seed controls.yaml.
    reg = project_root / "_registry"
    reg.mkdir(exist_ok=True)
    controls_path = reg / "controls.yaml"
    if not controls_path.exists():
        controls_path.write_text(
            "# Populate from domains/{}/controls/control-register.yaml\nselected: []\n".format(domain),
            encoding="utf-8",
        )
    if methodology == "hybrid":
        bt = reg / "baseline-trace.yaml"
        if not bt.exists():
            bt.write_text("baseline: []\nstories: []\n", encoding="utf-8")
    # Domain.md for ControlsCheck
    domain_path = project_root / "_context" / "domain.md"
    if not domain_path.exists():
        domain_path.write_text(f"# Domain\ndomain: {domain}\n", encoding="utf-8")
