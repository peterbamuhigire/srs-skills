"""Generate a canonical golden-path example project.

Mirrors engine/tests/test_cli.py::_seed_clean_project so each emitted
project passes `python -m engine validate`. Content strings are
domain-flavoured via the name/title/domain_label inputs; the file
structure is identical across examples.

Usage:
    python scripts/seed_example_project.py <slug> <domain_label> "<Project Title>" <control_id>

Slug is the directory name under 00-meta-initialization/new-project/examples/.
domain_label is the value written into _context/domain.md (e.g. healthcare).
control_id is the one control selected in _registry/controls.yaml; it must
belong to the domain's control register and its category's
`must_appear_in` patterns must be satisfied by the artefacts this seeder
writes (encryption + access_control are safe because the seeder always
creates 03-design-documentation/04-database-design/ and
05-testing-documentation/test-plan/).
"""
from __future__ import annotations
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "00-meta-initialization" / "new-project" / "examples"


def emit(slug: str, domain_label: str, title: str, control_id: str) -> Path:
    target = EXAMPLES / slug
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)

    # _context (Phase 01 + ControlsCheck)
    ctx = target / "_context"
    ctx.mkdir()
    (ctx / "vision.md").write_text(
        f"# Vision\n{title} delivers measurable outcomes for {domain_label} operators.\n"
        f"- **BG-001** Deliver measurable outcomes through the {title} platform.\n",
        encoding="utf-8",
    )
    (ctx / "stakeholders.md").write_text(
        f"# Stakeholders\n- {title} Operations Office.\n",
        encoding="utf-8",
    )
    (ctx / "features.md").write_text(
        f"# Features\n- F-1 Submit Record -- driven by {title} Operations Office\n",
        encoding="utf-8",
    )
    (ctx / "glossary.md").write_text(
        "# Glossary\n- **Record:** a primary business artifact tracked by the system.\n",
        encoding="utf-8",
    )
    (ctx / "methodology.md").write_text(
        "---\nmethodology: waterfall\n---\n"
        "# Methodology\nFormal phase-gated delivery with signed baselines.\n",
        encoding="utf-8",
    )
    (ctx / "domain.md").write_text(
        f"# Domain\ndomain: {domain_label}\n",
        encoding="utf-8",
    )
    # quality-standards.md is required by ObligationsCheck whenever a
    # domain is declared. We leave the framework list empty so no
    # obligation matches (keeping the example dependency-free while still
    # demonstrating the file's existence).
    (ctx / "quality-standards.md").write_text(
        "# Quality Standards\nFrameworks applicable to this example: none. "
        "Edit this file to declare the regulatory frameworks that apply "
        "to your project; the engine's ObligationsCheck matches framework "
        "names by substring.\n",
        encoding="utf-8",
    )

    # Phase 03 design
    design = target / "03-design-documentation"
    (design / "adr").mkdir(parents=True)
    (design / "adr" / "ADR-001-use-postgres.md").write_text(
        "# ADR-001 Use Postgres\nContext, decision, consequences.\n",
        encoding="utf-8",
    )
    (design / "03-api-specification").mkdir(parents=True)
    (design / "03-api-specification" / "claims-api.md").write_text(
        "# Claims API\n- `POST /claims` returns 201.\n",
        encoding="utf-8",
    )
    (design / "04-database-design").mkdir(parents=True)
    (design / "04-database-design" / "schema.md").write_text(
        f"# Schema\nTable `claims` has PRIMARY KEY `id`. "
        f"Encryption-at-rest per control {control_id}.\n",
        encoding="utf-8",
    )
    (design / "threat-model.md").write_text(
        "# Threat Model\nSTRIDE analysis.\n", encoding="utf-8"
    )

    # Phase 02 requirements (needed by ControlsCheck evidence patterns for
    # consent + access_control categories across domains)
    reqs = target / "02-requirements-engineering" / "srs"
    reqs.mkdir(parents=True)
    (reqs / "3.2-functional-requirements.md").write_text(
        f"# 3.2 Functional Requirements\n"
        f"- **FR-001** traces to BG-001: the system shall authenticate "
        f"users. Verified by TC-001. Evidences control {control_id}.\n",
        encoding="utf-8",
    )

    # Phase 03 UX specification (needed for consent-category evidence)
    (design / "05-ux-specification").mkdir(parents=True)
    (design / "05-ux-specification" / "ui-spec.md").write_text(
        f"# UX Specification\nConsent capture flow per control {control_id}.\n",
        encoding="utf-8",
    )

    # Phase 06 incident-response (needed for incident_response evidence)
    (ops_path_early := target / "06-deployment-operations" / "incident-response").mkdir(parents=True, exist_ok=True)
    (ops_path_early / "playbook.md").write_text(
        f"# Incident Response Playbook\nReferenced by control {control_id}.\n",
        encoding="utf-8",
    )

    # Phase 04 development
    dev = target / "04-development"
    dev.mkdir()
    (dev / "coding-standards.md").write_text(
        "# Coding Standards\nUse Black.\n", encoding="utf-8"
    )
    (dev / "env-setup.md").write_text(
        "# Env Setup\nPrerequisites: Python 3.11. Install: pip install -r "
        "requirements.txt. Verify: pytest.\n",
        encoding="utf-8",
    )
    (target / "CONTRIBUTING.md").write_text(
        "# Contributing\nPR process.\n", encoding="utf-8"
    )

    # Phase 05 testing
    testing = target / "05-testing-documentation"
    testing.mkdir()
    (testing / "29119-deterministic-checks.md").write_text(
        "# 29119 Deterministic Checks\nApplied.\n", encoding="utf-8"
    )
    (testing / "test-completion-report.md").write_text(
        "# Test Completion\nTested FR-001 with result PASS.\n",
        encoding="utf-8",
    )
    (testing / "test-plan").mkdir()
    (testing / "test-plan" / "tc.md").write_text(
        "---\n"
        "phase: '05'\n"
        "inputs: []\n"
        "expected_results: []\n"
        "requirement_trace: []\n"
        "---\n"
        f"- **TC-001** covers FR-001 and verifies control {control_id}\n",
        encoding="utf-8",
    )
    (testing / "coverage-matrix.md").write_text(
        "# Coverage Matrix\n| FR | TC |\n|---|---|\n| FR-001 | TC-001 |\n",
        encoding="utf-8",
    )

    # Phase 06 deployment & operations
    ops = target / "06-deployment-operations"
    ops.mkdir(exist_ok=True)
    (ops / "deployment-guide.md").write_text(
        "# Deployment Guide\nSteps... Rollback: revert release tag. "
        "Change window: Saturday 22:00-02:00.\n",
        encoding="utf-8",
    )
    (ops / "runbook.md").write_text(
        "# Runbook\nEscalation: page on-call via PagerDuty.\n",
        encoding="utf-8",
    )
    (ops / "monitoring.md").write_text(
        "# Monitoring\nSLO: 99.9% availability; SLI: error rate; "
        "SLA: 99% uptime.\n",
        encoding="utf-8",
    )
    (ops / "infrastructure.md").write_text(
        "# Infrastructure\nSee IR diagram: "
        "![incident response flow](./ir.png)\n",
        encoding="utf-8",
    )
    (ops / "go-live-readiness.md").write_text(
        "# Go-Live Readiness\n- [x] Backups configured\n"
        "- [x] Runbook complete\n- [x] Monitoring live\n",
        encoding="utf-8",
    )

    # Phase 07 agile artifacts
    agile = target / "07-agile-artifacts"
    agile.mkdir()
    (agile / "definition-of-ready.md").write_text(
        "# DoR\nItems ready when scope clear and BG-001 linked.\n",
        encoding="utf-8",
    )
    (agile / "definition-of-done.md").write_text(
        "# DoD\nDone when security review complete and compliance checked.\n",
        encoding="utf-8",
    )
    (agile / "sprint-plan.md").write_text(
        "# Sprint Plan\n- **US-001** Login flow (owner: peter)\n",
        encoding="utf-8",
    )
    (agile / "retrospective.md").write_text(
        "# Retro\n- **A-001** Automate release pipeline "
        "owner: peter due: 2026-06-01\n",
        encoding="utf-8",
    )
    (agile / "velocity.md").write_text(
        "# Velocity\nsprint-01 delivered 23 points; "
        "sprint-02 delivered 29 points.\n",
        encoding="utf-8",
    )

    # Phase 08 end-user documentation
    users = target / "08-end-user-documentation"
    users.mkdir()
    (users / "user-manual.md").write_text(
        "# User Manual\nHow to submit a claim: "
        "![submit screen](./submit.png)\n",
        encoding="utf-8",
    )
    (users / "release-notes.md").write_text(
        "# Release Notes v1.0\n- FR-001 implemented.\n",
        encoding="utf-8",
    )
    (users / "faq.md").write_text(
        "# FAQ\n"
        "## How do I sign up?\nA.\n"
        "## How do I log in?\nA.\n"
        "## How do I reset my password?\nA.\n"
        "## How do I export data?\nA.\n"
        "## How do I contact support?\nA.\n",
        encoding="utf-8",
    )

    # Phase 09 governance
    gov = target / "09-governance-compliance"
    gov.mkdir()
    (gov / "audit-report.md").write_text(
        f"# Audit Report\nphase01: PASS. phase03: PASS. phase05: PASS. "
        f"Control {control_id} selected and evidenced.\n",
        encoding="utf-8",
    )
    (gov / "risk-register.md").write_text(
        "# Risk Register\n- **R-001** Dependency on third-party API "
        "-- linked to FR-001.\n",
        encoding="utf-8",
    )

    # _registry selections so ControlsCheck + ObligationsCheck pass
    reg = target / "_registry"
    reg.mkdir()
    (reg / "controls.yaml").write_text(
        f"selected:\n  - id: {control_id}\n",
        encoding="utf-8",
    )

    # README (kept separate from the kernel-verified file set)
    (target / "README.md").write_text(
        f"# {title}\n\n"
        f"**Domain:** {domain_label}\n\n"
        f"**Methodology:** Waterfall (change in `_context/methodology.md` "
        f"if your project uses Agile or Hybrid).\n\n"
        f"## What this example demonstrates\n\n"
        f"A minimal but kernel-passing project workspace for the "
        f"{domain_label} domain. Every phase directory contains the "
        f"smallest file set that satisfies the nine registered gates.\n\n"
        f"## How to use as a starter\n\n"
        f"```bash\n"
        f"cp -r 00-meta-initialization/new-project/examples/{slug} "
        f"projects/<YourProject>\n"
        f"python -m engine validate projects/<YourProject>\n"
        f"```\n\n"
        f"Then customise `_context/vision.md`, `_context/stakeholders.md`, "
        f"and `_context/features.md` with real project content.\n",
        encoding="utf-8",
    )
    return target


def main() -> None:
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(2)
    slug, domain_label, title, control_id = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    out = emit(slug, domain_label, title, control_id)
    print(f"Wrote example to {out}")


if __name__ == "__main__":
    main()
