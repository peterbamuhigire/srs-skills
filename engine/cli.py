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
    from engine.gates.phase01 import Phase01Gate
    from engine.gates.phase02 import Phase02Gate
    from engine.gates.phase03 import Phase03Gate
    from engine.gates.phase04 import Phase04Gate
    from engine.gates.phase05 import Phase05Gate
    from engine.gates.phase06 import Phase06Gate
    from engine.gates.phase07 import Phase07Gate
    from engine.gates.phase08 import Phase08Gate
    from engine.gates.phase09 import Phase09Gate
    reg = GateRegistry()
    reg.register(NoUnresolvedFailMarkersGate())
    reg.register(Phase01Gate())
    reg.register(Phase02Gate())
    reg.register(Phase03Gate())
    reg.register(Phase04Gate())
    reg.register(Phase05Gate())
    reg.register(Phase06Gate())
    reg.register(Phase07Gate())
    reg.register(Phase08Gate())
    reg.register(Phase09Gate())
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

@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
def sync(project: str) -> None:
    """Populate _registry/identifiers.yaml and _registry/glossary.yaml."""
    from engine.sync import sync as do_sync
    ws = Workspace.load(Path(project))
    ids, gloss, errors = do_sync(ws)
    if errors:
        for e in errors:
            click.echo(e)
        sys.exit(1)
    reg_dir = ws.root / "_registry"
    reg_dir.mkdir(exist_ok=True)
    ids.save(reg_dir / "identifiers.yaml")
    gloss.save(reg_dir / "glossary.yaml")
    click.echo(f"Wrote {len(ids)} identifiers and {len(gloss)} glossary terms.")

if __name__ == "__main__":
    main()
