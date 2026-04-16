from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph, Artifact

def test_builds_graph_from_workspace(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    graph = ArtifactGraph.build(ws)
    titles = sorted(a.title for a in graph.artifacts)
    assert "Functional Requirements" in titles
    assert "Vision" in titles

def test_finds_artifact_by_phase(tiny_project: Path):
    graph = ArtifactGraph.build(Workspace.load(tiny_project))
    in_phase_02 = list(graph.in_phase("02"))
    assert len(in_phase_02) == 1
    assert in_phase_02[0].title == "Functional Requirements"

def test_extracts_requirement_ids(tiny_project: Path):
    graph = ArtifactGraph.build(Workspace.load(tiny_project))
    art = next(graph.in_phase("02"))
    assert sorted(art.identifiers) == ["FR-001", "FR-002"]
