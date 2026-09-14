# Hospitality, hotel and restaurant Kaizen - 2026-09-14

## Change

Added a hospitality domain pack and operating-model SRS skill. It separates
hotel and restaurant requirements while defining explicit contracts for guest,
folio, room charge, inventory, event, payment, finance, audit and reporting
integration. Each requirement now has actor, state, failure path, control,
tenant/property scope, oracle, evidence, owner and status.

## Evidence discipline

Maduuka source and reference documents were inspected as implementation evidence
surfaces, not proof of live readiness. Code, schema, screenshots and reference
docs are classified separately from executable integration, device, recovery,
render and UAT evidence. Current law, tax, privacy, food safety and payment
claims require current companion sources.

## Experiment and gate

Hypothesis: scenario/state/oracle requirements will reduce “screen exists” false
passes in hospitality audits. Measure orphan requirements, missing failure tests,
tenant-isolation defects and retest time in the Maduuka audit. Rollback by
removing the domain route; retain existing SRS routes. Next review: 2026-10-14.
