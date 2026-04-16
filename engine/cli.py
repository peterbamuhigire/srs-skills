"""Engine CLI."""
from __future__ import annotations
import sys
from datetime import date
from pathlib import Path
import click
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.base import GateRegistry
from engine.checks.markers import NoUnresolvedFailMarkersGate
from engine.waivers import WaiverRegister
from engine.reporters.markdown import render_markdown
from engine.reporters.junit import render_junit
from engine.reporters.sarif import render_sarif

def _default_registry() -> GateRegistry:
    reg = GateRegistry()
    reg.register(NoUnresolvedFailMarkersGate())
    # Plan 02 will register phase gates here.
    return reg

@click.group()
def main() -> None:
    """srs-skills validation kernel."""

@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--junit", type=click.Path(), default=None)
@click.option("--sarif", type=click.Path(), default=None)
@click.option("--markdown", "md_path", type=click.Path(), default=None)
def validate(project: str, junit: str | None, sarif: str | None, md_path: str | None) -> None:
    """Validate a project workspace and exit non-zero on blocking findings."""
    workspace = Workspace.load(Path(project))
    graph = ArtifactGraph.build(workspace)
    findings = FindingCollection()
    _default_registry().run_all(graph, findings)
    waivers = WaiverRegister.load(workspace.root / "_registry" / "waivers.yaml")
    waived, remaining_list = waivers.apply(findings, today=date.today())
    remaining = FindingCollection()
    remaining.extend(remaining_list)
    md = render_markdown(remaining, waived, project=workspace.root.name)
    if md_path:
        Path(md_path).write_text(md, encoding="utf-8")
    if junit:
        Path(junit).write_text(render_junit(remaining), encoding="utf-8")
    if sarif:
        Path(sarif).write_text(render_sarif(remaining), encoding="utf-8")
    if remaining.is_blocking:
        click.echo("ENGINE CONTRACT: FAIL")
        for f in remaining:
            click.echo(f"- [{f.severity.name}] {f.gate_id}: {f.message}")
        sys.exit(1)
    click.echo("ENGINE CONTRACT: PASS")

if __name__ == "__main__":
    main()
