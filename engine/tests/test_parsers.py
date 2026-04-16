from pathlib import Path
from engine.parsers.frontmatter import parse_frontmatter
from engine.parsers.markers import find_markers, Marker

def test_parses_yaml_frontmatter():
    body = "---\nid: FR-001\nstatus: draft\n---\n# Title\n"
    fm, content = parse_frontmatter(body)
    assert fm == {"id": "FR-001", "status": "draft"}
    assert content.startswith("# Title")

def test_returns_empty_dict_when_no_frontmatter():
    body = "# Title\nbody text"
    fm, content = parse_frontmatter(body)
    assert fm == {}
    assert content == body

def test_finds_marker_with_reason():
    body = "Some text [V&V-FAIL: missing test oracle] and more.\n[CONTEXT-GAP: stakeholders]"
    markers = find_markers(body)
    assert Marker("V&V-FAIL", "missing test oracle", 1) in markers
    assert Marker("CONTEXT-GAP", "stakeholders", 2) in markers

def test_finds_marker_without_reason():
    body = "[GLOSSARY-GAP]"
    markers = find_markers(body)
    assert markers == [Marker("GLOSSARY-GAP", "", 1)]
