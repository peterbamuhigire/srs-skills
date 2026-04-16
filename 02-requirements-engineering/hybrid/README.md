# Hybrid Skills

Use this directory when the project follows Water-Scrum-Fall, or a similar hybrid pattern, where a Waterfall requirements baseline is executed through Agile sprints. See `docs/hybrid-operating-model.md` for the full taxonomy and operating contract.

## When to use Hybrid

A project belongs here when all of the following are true:

- A formal requirements baseline must be locked and change-controlled before execution.
- Iterative delivery (sprints) is used to implement that baseline.
- Traceability between each sprint increment and the baseline must remain auditable.

If no baseline exists, use the skills under `../agile/`. If no iterative execution exists, use `../waterfall/`.

## Available Skills

| Skill | Purpose | Output |
|---|---|---|
| [hybrid-synchronization](hybrid-synchronization/) | Lock the Water-Scrum-Fall contract: emit methodology, baseline trace, and DoR/DoD definitions that quote baseline IDs verbatim. | `_context/methodology.md`, `_registry/baseline-trace.yaml`, `07-agile-artifacts/definitions/dor-dod.md` |

## Related Pipelines

- Agile skills live in `../agile/`.
- Waterfall skills live in `../waterfall/`.
- The `HybridSyncGate` in `engine/gates/hybrid.py` enforces the contract deterministically.
