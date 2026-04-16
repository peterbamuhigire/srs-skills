import json
from pathlib import Path
from xml.etree import ElementTree as ET
from engine.findings import Finding, FindingCollection, Severity
from engine.reporters.markdown import render_markdown
from engine.reporters.junit import render_junit
from engine.reporters.sarif import render_sarif

def _coll() -> FindingCollection:
    c = FindingCollection()
    c.add(Finding("phase01.x", Severity.HIGH, "broken", Path("a.md"), 3))
    c.add(Finding("phase01.x", Severity.LOW, "warn", Path("b.md"), 5))
    return c

def test_markdown_lists_each_finding():
    out = render_markdown(_coll(), waived=[], project="demo")
    assert "phase01.x" in out
    assert "broken" in out
    assert "demo" in out

def test_junit_has_one_testcase_per_gate():
    out = render_junit(_coll())
    root = ET.fromstring(out)
    cases = root.findall(".//testcase")
    assert {c.get("name") for c in cases} == {"phase01.x"}
    assert root.findall(".//failure")

def test_sarif_is_valid_json():
    out = render_sarif(_coll())
    obj = json.loads(out)
    assert obj["version"] == "2.1.0"
    assert obj["runs"][0]["results"][0]["ruleId"] == "phase01.x"
