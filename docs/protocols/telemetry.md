# Telemetry Protocol Documentation

Telemetry documentation describes the data exchanged between the drone, ground station, companion computers, and monitoring tools.

## Message documentation fields

- Message name
- Direction
- Rate
- Required/optional status
- Payload fields
- Units
- Valid ranges
- Version introduced
- Compatibility notes
- Failure behavior

## Telemetry categories

- Heartbeat
- Vehicle state
- Attitude and position
- Battery and power
- Mission status
- Link quality
- Health and diagnostics
- Failsafe events
- Firmware version

## Compatibility principles

- Prefer additive changes.
- Version messages or schemas.
- Keep deprecated fields documented until removed.
- Validate tooling against sample messages.
