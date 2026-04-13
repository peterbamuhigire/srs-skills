# IoT Architecture Checklist

Use this checklist to pressure-test IoT design outputs before baselining them.

## System Scope

- Define every device class and its job in the product.
- Separate device, gateway, edge, cloud, and operator responsibilities.
- State what must still work during connectivity loss or partial platform outage.

## Connectivity

- Name the protocols in use such as MQTT, HTTP, CoAP, BLE, LoRaWAN, Zigbee, or cellular.
- Explain why each protocol fits power, latency, bandwidth, and deployment constraints.
- Define buffering, ordering, retry, and duplicate-handling behavior.

## Security

- Specify how devices are provisioned and authenticated.
- Define credential storage, rotation, and revocation rules.
- State encryption expectations for telemetry, commands, logs, and stored data.
- Clarify trust boundaries between device firmware, edge gateways, cloud services, and operator consoles.

## Device Lifecycle

- Define onboarding, registration, and environment assignment.
- Define configuration management and secret distribution.
- Define OTA rollout waves, rollback criteria, and failure recovery.
- Define retirement and secure wipe expectations.

## Operations

- Identify fleet health metrics, alert conditions, and diagnostics collection.
- Clarify who handles field failures, network-provider failures, and cloud-service failures.
- State spare capacity, maintenance windows, and support workflows.

## Design Heuristics

- Prefer local autonomy for actions that are safety-critical or latency-sensitive.
- Keep message contracts versioned from the beginning.
- Separate customer-visible product behavior from internal telemetry and control channels.
- Design the fleet as an operating system problem, not just an API problem.
