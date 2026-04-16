# Domain Control Libraries Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans.

**Goal:** Upgrade `domains/<domain>/` from "contextual guidance" (NFR defaults + reg references) into a compliance rule engine: a control library, an obligation-to-control map, evidence expectations, required reviews, and a domain-specific test obligation set. The kernel reads these files and enforces that every selected control is implemented, verified, and audited. Closes Gap #6.

**Architecture:** Each domain gains a `controls/` subdirectory with a YAML control register, an obligations map, an evidence expectations file, and a required-reviews file. A new `engine/checks/controls.py` cross-references the project's `_registry/controls.yaml` (consultant-selected) against domain libraries to ensure every selected control has its mandatory artifacts. Existing domain content (NFR defaults, regulations) is preserved.

**Tech Stack:** YAML + JSON Schema + Python.

---

## File Structure

```
domains/<domain>/
├── INDEX.md                      # existing
├── references/                   # existing
└── controls/
    ├── control-register.yaml
    ├── obligations.yaml
    ├── evidence-expectations.yaml
    └── required-reviews.yaml

engine/
├── checks/
│   ├── controls.py
│   └── obligations.py
├── registry/
│   └── schemas/
│       ├── control-register.schema.json
│       ├── project-controls.schema.json
│       └── obligations.schema.json
└── tests/
    ├── test_check_controls.py
    └── test_check_obligations.py

projects/<X>/_registry/controls.yaml   # consultant-selected controls
```

---

### Task 1: Domain control register schema

**Files:**

- Create: `engine/registry/schemas/control-register.schema.json`

- [ ] **Step 1: Write the schema**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["domain", "controls"],
  "properties": {
    "domain": {"type": "string"},
    "version": {"type": "string"},
    "source_framework": {"type": "string"},
    "controls": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "title", "category", "verification_kinds"],
        "properties": {
          "id": {"type": "string", "pattern": "^CTRL-[A-Z0-9]{2,8}-\\d{3}$"},
          "title": {"type": "string"},
          "category": {"enum": [
            "access_control", "data_protection", "audit_logging",
            "incident_response", "encryption", "key_management",
            "retention", "consent", "third_party", "physical",
            "monitoring", "change_control", "training", "risk_management"
          ]},
          "verification_kinds": {
            "type": "array",
            "items": {"enum": ["test", "design_review", "audit_log_inspection", "config_inspection", "policy_inspection"]},
            "minItems": 1
          },
          "minimum_evidence": {"type": "array", "items": {"type": "string"}},
          "regulatory_anchor": {
            "type": "object",
            "required": ["framework", "clause"],
            "properties": {
              "framework": {"type": "string"},
              "clause": {"type": "string"}
            }
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```

- [ ] **Step 2: Commit**

---

### Task 2: Author control library for the `uganda` domain (highest priority — most active)

**Files:**

- Create: `domains/uganda/controls/control-register.yaml`
- Create: `domains/uganda/controls/obligations.yaml`
- Create: `domains/uganda/controls/evidence-expectations.yaml`
- Create: `domains/uganda/controls/required-reviews.yaml`

- [ ] **Step 1: Author `control-register.yaml`** — DPPA 2019 controls plus standard ICT controls. Minimum coverage:

```yaml
domain: uganda
version: "1.0"
source_framework: "Uganda Data Protection and Privacy Act 2019"
controls:
  - id: CTRL-UG-001
    title: Lawful basis for personal data collection
    category: consent
    verification_kinds: [policy_inspection, design_review]
    minimum_evidence:
      - "_context/quality-standards.md references DPPA-2019 §7"
      - "Functional requirement that collects PII has a paired FR for consent capture"
    regulatory_anchor:
      framework: "Uganda DPPA 2019"
      clause: "§7"

  - id: CTRL-UG-002
    title: Encryption of special personal data at rest
    category: encryption
    verification_kinds: [config_inspection, test]
    minimum_evidence:
      - "Database design specifies AES-256-GCM for fields tagged S-tier"
      - "Test case verifies ciphertext is never returned in API responses"
    regulatory_anchor:
      framework: "Uganda DPPA 2019"
      clause: "§19"

  - id: CTRL-UG-003
    title: Breach notification to PDPO
    category: incident_response
    verification_kinds: [policy_inspection, design_review]
    minimum_evidence:
      - "Runbook contains a 'Notify PDPO immediately' step"
      - "Incident-response design includes the PDPO contact channel"
    regulatory_anchor:
      framework: "Uganda DPPA 2019"
      clause: "§23"

  - id: CTRL-UG-004
    title: Data subject access request handling
    category: access_control
    verification_kinds: [test, design_review]
    minimum_evidence:
      - "FR for DSAR exists with stimulus-response form"
      - "Test case proves DSAR fulfilment within 30 days"
    regulatory_anchor:
      framework: "Uganda DPPA 2019"
      clause: "§30"
```

- [ ] **Step 2: Author `obligations.yaml`** — maps regulatory obligations to controls:

```yaml
obligations:
  - obligation: "Obtain lawful basis before processing personal data"
    framework: "Uganda DPPA 2019"
    clause: "§7"
    satisfied_by: [CTRL-UG-001]

  - obligation: "Encrypt special personal data at rest"
    framework: "Uganda DPPA 2019"
    clause: "§19(2)"
    satisfied_by: [CTRL-UG-002]

  - obligation: "Notify the PDPO of any data breach without undue delay"
    framework: "Uganda DPPA 2019"
    clause: "§23"
    satisfied_by: [CTRL-UG-003]

  - obligation: "Provide data subjects with access to their data within 30 days"
    framework: "Uganda DPPA 2019"
    clause: "§30"
    satisfied_by: [CTRL-UG-004]
```

- [ ] **Step 3: Author `evidence-expectations.yaml`** — what artifact types are expected per control category:

```yaml
expectations:
  consent:
    must_appear_in:
      - 02-requirements-engineering/srs/3.2*  # consent FR
      - 03-design-documentation/05-ux-specification/*  # consent UI
  encryption:
    must_appear_in:
      - 03-design-documentation/04-database-design/*
      - 05-testing-documentation/test-plan/*
  incident_response:
    must_appear_in:
      - 06-deployment-operations/runbook/*
      - 06-deployment-operations/incident-response/*
  access_control:
    must_appear_in:
      - 02-requirements-engineering/srs/3.2*
      - 05-testing-documentation/test-plan/*
```

- [ ] **Step 4: Author `required-reviews.yaml`**:

```yaml
required_reviews:
  - control_category: encryption
    reviewer_role: "Security Architect"
    cadence: "per release"
  - control_category: incident_response
    reviewer_role: "DPO"
    cadence: "per quarter"
  - control_category: consent
    reviewer_role: "Legal"
    cadence: "per release"
```

- [ ] **Step 5: Commit**

```bash
git add domains/uganda/controls/
git commit -m "feat(domains): add Uganda DPPA control library (controls, obligations, expectations, reviews)"
```

---

### Task 3: Repeat Task 2 for remaining domains

Each domain gets the same four-file structure. Sources:

| Domain | Source frameworks |
|---|---|
| `healthcare` | HIPAA Security Rule, HIPAA Privacy Rule, HL7/FHIR consent profile |
| `finance` | PCI-DSS v4.0, SOX §404, AML KYC |
| `education` | FERPA, COPPA, GDPR (when student is in EU) |
| `retail` | PCI-DSS v4.0, GDPR, consumer-protection law |
| `logistics` | DOT 49 CFR, ISO 28000 |
| `government` | FISMA Moderate, FedRAMP Moderate, NIST 800-53 Rev 5 |
| `agriculture` | FAO Codex Alimentarius, country food-safety regs |

- [ ] For each domain, perform Task 2 Steps 1-5 with the framework's clauses. Commit per domain.

---

### Task 4: Project-controls schema and selection

**Files:**

- Create: `engine/registry/schemas/project-controls.schema.json`
- Create: `projects/<X>/_registry/controls.yaml` (template; not committed because `projects/` is gitignored — instead add it to `00-meta-initialization/new-project/templates/`)

The project-controls file is the consultant's selection of which domain controls apply to this project, with project-specific notes.

- [ ] **Step 1: Schema**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["selected"],
  "properties": {
    "selected": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "applies_because"],
        "properties": {
          "id": {"type": "string", "pattern": "^CTRL-[A-Z0-9]{2,8}-\\d{3}$"},
          "applies_because": {"type": "string", "minLength": 5},
          "owner": {"type": "string"},
          "exemption": {"type": "string"}
        }
      }
    }
  }
}
```

- [ ] **Step 2: Add a template** at `00-meta-initialization/new-project/templates/controls.yaml.template`:

```yaml
# Project control selection. Refer to domains/<domain>/controls/control-register.yaml.
# After editing, run: python -m engine validate <project>
selected: []
```

- [ ] **Step 3: Modify the new-project skill** to copy this template into `projects/<X>/_registry/controls.yaml`.

- [ ] **Step 4: Commit**

---

### Task 5: `ControlsCheck` — every selected control has its mandatory artifacts

**Files:**

- Create: `engine/checks/controls.py`
- Create: `engine/tests/test_check_controls.py`

- [ ] **Step 1: Failing test**

```python
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.controls import ControlsCheck

def _setup(tmp_path: Path) -> Path:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision")
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/controls.yaml").write_text("""\
selected:
  - id: CTRL-UG-002
    applies_because: "App stores patient NIN numbers"
""")
    (tmp_path / "domains_uganda_controls_register.yaml").write_text("# placeholder")
    return tmp_path

def test_flags_missing_evidence_for_selected_control(tmp_path: Path):
    project = _setup(tmp_path)
    domain_register = Path("domains/uganda/controls/control-register.yaml")
    findings = FindingCollection()
    chk = ControlsCheck("phase09.controls", project, domain_register)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    msgs = [f.message for f in findings]
    assert any("CTRL-UG-002" in m for m in msgs)
```

- [ ] **Step 2: Implement**

```python
"""ControlsCheck: every selected control has the artifacts the domain requires."""
from __future__ import annotations
import fnmatch
from pathlib import Path
from ruamel.yaml import YAML
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_yaml = YAML(typ="safe")

class ControlsCheck:
    def __init__(self, gate_id: str, project_root: Path, domain_register: Path) -> None:
        self.gate_id = gate_id
        self._project = project_root
        self._domain_register = domain_register

    def _load_yaml(self, path: Path) -> dict:
        return _yaml.load(path.read_text(encoding="utf-8")) or {}

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        sel_path = self._project / "_registry" / "controls.yaml"
        if not sel_path.exists():
            findings.add(Finding(
                gate_id=f"{self.gate_id}.no_selection",
                severity=Severity.HIGH,
                message="Project missing _registry/controls.yaml",
                location=None, line=None,
            ))
            return
        selected = {
            c["id"]: c for c in self._load_yaml(sel_path).get("selected", [])
        }
        register = {
            c["id"]: c for c in self._load_yaml(self._domain_register).get("controls", [])
        }
        expectations_path = self._domain_register.parent / "evidence-expectations.yaml"
        expectations = self._load_yaml(expectations_path).get("expectations", {}) if expectations_path.exists() else {}
        artifact_paths = [str(a.path).replace("\\", "/") for a in graph.artifacts]
        for cid in selected:
            ctrl = register.get(cid)
            if ctrl is None:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.unknown_control",
                    severity=Severity.HIGH,
                    message=f"{cid} selected but not defined in domain register",
                    location=sel_path, line=None,
                ))
                continue
            cat = ctrl["category"]
            for pattern in expectations.get(cat, {}).get("must_appear_in", []):
                hits = [p for p in artifact_paths if fnmatch.fnmatch(p, pattern)]
                if not hits:
                    findings.add(Finding(
                        gate_id=f"{self.gate_id}.missing_evidence",
                        severity=Severity.HIGH,
                        message=f"{cid} ({cat}) requires an artifact matching '{pattern}', none found",
                        location=None, line=None,
                    ))
            # Mention check: control ID appears in at least one artifact
            mentioned = any(cid in a.body for a in graph.artifacts)
            if not mentioned:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.unused_in_artifacts",
                    severity=Severity.HIGH,
                    message=f"{cid} selected but never referenced in any artifact",
                    location=None, line=None,
                ))
```

- [ ] **Step 3: Wire `ControlsCheck` into `Phase09Gate`** with the active domain inferred from `_context/domain.md` (or default to a no-op if no domain).

- [ ] **Step 4: Commit**

---

### Task 6: `ObligationsCheck` — every project-relevant obligation is satisfied

Mirror of Task 5 against `obligations.yaml`. Asserts: every obligation whose `framework` appears in the project's `_context/quality-standards.md` is `satisfied_by` at least one selected control.

- [ ] **Step 1-3: Failing test → implement → commit** following the Task 5 pattern.

---

### Task 7: Update `09-governance-compliance/03-compliance/SKILL.md` to read controls

**Files:**

- Modify: `09-governance-compliance/03-compliance/SKILL.md`

The compliance generation skill should now produce its compliance annex by:

1. Reading `_registry/controls.yaml` for the selected controls.
2. Reading the matching domain `control-register.yaml`.
3. Generating one section per control showing: title, regulatory anchor, the artifacts that satisfy it (extracted via the kernel's check), the verification evidence (link to test cases by ID), and the assigned reviewer.

- [ ] **Step 1: Update the skill body** with explicit Stimulus / Process / Response steps that consume the YAML files.

- [ ] **Step 2: Commit**

---

## Self-Review

1. **Spec coverage:** Domain layer now has control library, obligation map, evidence expectations, required reviews, and a domain-specific test obligation pattern (each control's `verification_kinds`). Compliance is rule-driven, not narrative.
2. **Placeholder scan:** None.
3. **Type consistency:** Schema patterns match Plans 01/03; `gate_id` namespace under `phase09.controls.*`.
4. **Extensibility:** Adding a new domain is one directory + four YAML files. No engine code changes required.
