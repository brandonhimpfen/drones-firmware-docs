# Failsafe Documentation

Failsafe behavior defines what the aircraft does when something goes wrong.

## Common failsafe triggers

- Battery low or critical
- RC link loss
- Telemetry link loss
- GPS loss
- Sensor failure
- Estimator divergence
- Geofence breach
- Mission timeout
- Motor/ESC fault
- Watchdog reset

## Failsafe documentation fields

For each trigger document:

- Detection method
- Thresholds
- Delay/debounce behavior
- Required state
- Action taken
- Operator notification
- Logs emitted
- Recovery conditions
- Test coverage

## Failsafe action examples

| Action | Typical use |
|---|---|
| Warning only | Non-critical degradation |
| Hold position | Temporary uncertainty with position estimate |
| Return-to-launch | Link loss or mission issue with valid navigation |
| Land | Battery critical or unrecoverable issue |
| Disarm | Ground-only or severe emergency condition |

Actions must be selected and validated for the vehicle type, operating environment, and regulatory context.
