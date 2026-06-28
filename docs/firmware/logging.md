# Logging

Firmware logs are essential for debugging, validation, incident review, and release confidence.

## Log categories

- Boot logs
- Health status
- Sensor samples
- Estimator states
- Controller outputs
- Actuator commands
- Battery and power status
- Communication link status
- Failsafe events
- Parameter changes
- Firmware update events

## Log documentation fields

For each log field document name, type, units, rate, source module, valid range, and interpretation notes.

## Logging quality principles

- Log safety events explicitly.
- Include firmware version and parameter hash.
- Avoid ambiguous units.
- Do not overload fields across versions without migration notes.
- Maintain sample logs for tooling tests.
