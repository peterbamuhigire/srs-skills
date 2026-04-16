from pathlib import Path
import pytest
from engine.workspace import Workspace, WorkspaceNotFoundError

def test_loads_workspace_with_context_dir(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    assert ws.root == tiny_project
    assert ws.context_dir == tiny_project / "_context"
    assert (ws.context_dir / "vision.md").exists()

def test_raises_when_no_context_dir(tmp_path: Path):
    with pytest.raises(WorkspaceNotFoundError) as exc:
        Workspace.load(tmp_path)
    assert "_context" in str(exc.value)

def test_lists_all_artifacts(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    paths = sorted(p.name for p in ws.iter_artifacts())
    assert paths == ["3.2-functional-requirements.md", "glossary.md", "vision.md"]
