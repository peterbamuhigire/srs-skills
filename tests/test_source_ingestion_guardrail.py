import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/source_ingestion_guardrail.py"
SPEC = importlib.util.spec_from_file_location("source_ingestion_guardrail", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE  # dataclasses resolve their module at class creation
SPEC.loader.exec_module(MODULE)


def codes(root):
    return sorted(f.code for f in MODULE.scan(root))


def write(root, rel, text="x"):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_clean_tree_passes(tmp_path):
    write(tmp_path, "01-phase/skill/SKILL.md", "[ref](references/topic.md)")
    write(tmp_path, "docs/plan.md", "We retired the `book-extractions/` folder.")
    assert codes(tmp_path) == []


def test_extraction_folder_fails(tmp_path):
    write(tmp_path, "book-extractions/notes.md")
    assert codes(tmp_path) == ["book-extraction-folder"]


def test_book_study_folder_fails(tmp_path):
    write(tmp_path, "docs/book-study/ch1.md")
    assert codes(tmp_path) == ["book-extraction-folder"]


def test_extraction_filename_fails(tmp_path):
    write(tmp_path, "docs/research/some-books-analysis.md")
    write(tmp_path, "references/saas-srs-extraction.md")
    assert codes(tmp_path) == ["book-extraction-file", "book-extraction-file"]


def test_markdown_link_to_extraction_fails(tmp_path):
    write(tmp_path, "01-phase/skill/SKILL.md", "See [x](../../book-extractions/y.md).")
    write(tmp_path, "docs/log.md", "See [x](../book-extractions/y.md).")
    assert codes(tmp_path) == ["book-extraction-link", "book-extraction-link"]


def test_backticked_file_path_fails_outside_docs_only(tmp_path):
    write(tmp_path, "01-phase/skill/SKILL.md", "- `book-extractions/y.md` source")
    write(tmp_path, "docs/history.md", "- removed `book-extractions/y.md`")
    assert codes(tmp_path) == ["book-extraction-link"]


def test_projects_workspace_is_not_scanned_for_links(tmp_path):
    write(tmp_path, "projects/Client/notes.md", "[x](book-extractions/y.md)")
    assert codes(tmp_path) == []
