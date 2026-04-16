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
def doctor() -> None:
    """Run pre-flight diagnostics."""
    from engine.doctor import run
    sys.exit(run())


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
    from engine.gates.hybrid import HybridSyncGate
    HybridSyncGate(workspace.root).evaluate(graph, findings)
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

@main.command("validate-skills")
def validate_skills() -> None:
    """Scan skill files for legacy path references."""
    from engine.checks.legacy_paths import LegacyPathCheck
    findings = FindingCollection()
    chk = LegacyPathCheck()
    for d in ["00-meta-initialization", "01-strategic-vision", "02-requirements-engineering",
              "03-design-documentation", "04-development-artifacts", "05-testing-documentation",
              "06-deployment-operations", "07-agile-artifacts", "08-end-user-documentation",
              "09-governance-compliance"]:
        for p in Path(d).rglob("*.md"):
            chk.scan_file(p, findings)
    if findings.is_blocking:
        for f in findings:
            click.echo(f"- {f.location}:{f.line} {f.message}")
        sys.exit(1)
    click.echo("SKILLS OK: no legacy path references outside alias-blocks.")

@main.group()
def baseline() -> None:
    """Baseline snapshot / diff commands."""


@baseline.command("snapshot")
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--label", required=True)
def baseline_snapshot(project: str, label: str) -> None:
    """Snapshot current identifier hashes under the project's baseline-delta dir."""
    from engine.baseline import snapshot, save_snapshot
    ws = Workspace.load(Path(project))
    graph = ArtifactGraph.build(ws)
    snap = snapshot(graph, label=label)
    out_dir = ws.root / "09-governance-compliance" / "07-baseline-delta"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{label}.yaml"
    save_snapshot(snap, out)
    click.echo(
        f"Wrote baseline {label} with {len(snap.entries)} entries to {out}"
    )


@baseline.command("diff")
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.argument("old_label")
@click.argument("new_label")
def baseline_diff(project: str, old_label: str, new_label: str) -> None:
    """Print added, removed, and modified identifiers between two baselines."""
    from engine.baseline import load_snapshot, diff
    base = Path(project) / "09-governance-compliance" / "07-baseline-delta"
    old = load_snapshot(base / f"{old_label}.yaml")
    new = load_snapshot(base / f"{new_label}.yaml")
    d = diff(old, new)
    click.echo(f"Added: {len(d['added'])}")
    for x in d["added"]:
        click.echo(f"  + {x}")
    click.echo(f"Removed: {len(d['removed'])}")
    for x in d["removed"]:
        click.echo(f"  - {x}")
    click.echo(f"Modified: {len(d['modified'])}")
    for x in d["modified"]:
        click.echo(f"  ~ {x}")


@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--gate", required=True)
@click.option("--scope", default="*")
@click.option("--reason", required=True)
@click.option("--approver", required=True)
@click.option("--days", type=int, default=30, show_default=True)
def waive(project: str, gate: str, scope: str, reason: str,
          approver: str, days: int) -> None:
    """Append a new waiver to the project's _registry/waivers.yaml."""
    from datetime import date, timedelta
    from ruamel.yaml import YAML
    if days > 90:
        click.echo(f"ERROR: --days must be <= 90 (got {days})", err=True)
        sys.exit(1)
    yaml = YAML()
    ws = Workspace.load(Path(project))
    reg_dir = ws.root / "_registry"
    reg_dir.mkdir(exist_ok=True)
    waivers_path = reg_dir / "waivers.yaml"
    if waivers_path.exists():
        data = yaml.load(waivers_path.read_text(encoding="utf-8")) or {"waivers": []}
    else:
        data = {"waivers": []}
    existing_ids = {w.get("id", "") for w in data.get("waivers", []) or []}
    n = 1
    while f"WAIVE-{n:03d}" in existing_ids:
        n += 1
    new_id = f"WAIVE-{n:03d}"
    today = date.today()
    expires = today + timedelta(days=days)
    entry = {
        "id": new_id,
        "gate": gate,
        "scope": scope,
        "reason": reason,
        "approver": approver,
        "approved_on": today.isoformat(),
        "expires_on": expires.isoformat(),
    }
    data.setdefault("waivers", []).append(entry)
    with waivers_path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f)
    click.echo(f"Added {new_id} to {waivers_path} (expires {expires})")


@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--gate", required=True, help="e.g. phase02, phase06, phase09")
@click.option("--signer", required=True)
@click.option("--role", required=True)
@click.option("--artifact", "artifacts", multiple=True, required=True,
              help="Repeat --artifact for each file in the signed-off set")
@click.option("--comment", default="")
def signoff(project: str, gate: str, signer: str, role: str,
            artifacts: tuple[str, ...], comment: str) -> None:
    """Append a sign-off entry to _registry/sign-off-ledger.yaml."""
    from datetime import date
    from ruamel.yaml import YAML
    yaml = YAML()
    ws = Workspace.load(Path(project))
    reg_dir = ws.root / "_registry"
    reg_dir.mkdir(exist_ok=True)
    ledger_path = reg_dir / "sign-off-ledger.yaml"
    if ledger_path.exists():
        data = yaml.load(ledger_path.read_text(encoding="utf-8")) or {"sign_offs": []}
    else:
        data = {"sign_offs": []}
    entry = {
        "gate": gate,
        "signer": signer,
        "role": role,
        "signed_on": date.today().isoformat(),
        "artifact_set": list(artifacts),
    }
    if comment:
        entry["comment"] = comment
    data.setdefault("sign_offs", []).append(entry)
    with ledger_path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f)
    click.echo(
        f"Signed off {gate} by {signer} ({role}) on {entry['signed_on']}"
    )


@main.command()
@click.argument("project", type=click.Path(exists=True, file_okay=False))
@click.option("--out", type=click.Path(), required=True)
def pack(project: str, out: str) -> None:
    """Build an evidence pack ZIP of _context, _registry, and 09-governance-compliance."""
    from engine.pack import build_evidence_pack
    build_evidence_pack(Path(project), Path(out))
    click.echo(f"Wrote evidence pack to {out}")


if __name__ == "__main__":
    main()
