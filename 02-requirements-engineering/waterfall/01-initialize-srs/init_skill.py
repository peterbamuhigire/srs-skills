"""Seed the parent project with IEEE/ISO context templates and prepare the output folder."""

import shutil
from pathlib import Path
import sys

MODULE_ROOT = Path(__file__).resolve().parent
PARENT_ROOT = MODULE_ROOT.parent
PROJECT_CONTEXT = PARENT_ROOT / "project_context"
OUTPUT_DIR = PARENT_ROOT / "output"
TEMPLATES_DIR = MODULE_ROOT / "templates"


def prompt_action() -> str:
    print("../project_context/ already exists.")
    print("Choose an action:")
    print("  M -> Maintenance Mode (add missing templates without deleting data)")
    print("  C -> Clean (delete directory and rebuild from bundled templates)")

    while True:
        selection = input("Action (M/C): ").strip().lower()
        if selection in ("m", "maintenance", "maintenance mode"):
            return "maintenance"
        if selection in ("c", "clean"):
            return "clean"
        print("Please type M for Maintenance Mode or C for Clean.")


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def copy_templates(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError("templates/ directory is missing inside the skill module.")

    for template in sorted(source.iterdir()):
        if not template.is_file():
            continue
        target = destination / template.name
        if target.exists():
            print(f"Keeping existing {target.name} (already present).")
            continue
        shutil.copy2(template, target)
        print(f"Created {target.relative_to(PARENT_ROOT)}.")


def main() -> None:
    action = None
    if PROJECT_CONTEXT.exists():
        action = prompt_action()
        if action == "clean":
            shutil.rmtree(PROJECT_CONTEXT)
            print("Cleaned ../project_context/; rebuilding templates.")
        else:
            print("Maintenance Mode selected; adding missing templates only.")
    ensure_directory(PROJECT_CONTEXT)
    ensure_directory(OUTPUT_DIR)
    copy_templates(TEMPLATES_DIR, PROJECT_CONTEXT)
    print("../output/ is ready for downstream skills.")
    print("The quality of the final SRS depends entirely on the technical density of these files. Avoid vague language; provide specific numbers and models.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Initialization failed: {exc}")
        sys.exit(1)
