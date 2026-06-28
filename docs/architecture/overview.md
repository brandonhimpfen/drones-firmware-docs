# Firmware Architecture Overview

Drone firmware is typically organized around deterministic control, reliable sensing, actuator output, communication, logging, and safety supervision.

## Reference architecture

```text
Bootloader
  ↓
Board initialization
  ↓
Device drivers and buses
  ↓
Sensor acquisition and filtering
  ↓
State estimation
  ↓
Flight mode manager
  ↓
Control loops
  ↓
Mixer / actuator allocation
  ↓
ESC / servo / payload outputs
```

Cross-cutting services include logging, telemetry, health monitoring, parameter storage, firmware update handling, watchdog supervision, and failsafe management.

## Documentation boundaries

Document each subsystem with:

- Purpose and scope
- Inputs and outputs
- Timing expectations
- Parameters
- Failure behavior
- Test coverage
- Version history

## Real-time considerations

Firmware documentation should explicitly describe deadlines and rates. For example, sensor sampling, estimator updates, attitude control, position control, actuator output, telemetry publishing, and log flushing may all run at different frequencies.

## Safety-critical paths

Safety-critical paths should be documented in diagrams and prose. Examples include arming checks, failsafe triggers, emergency stop handling, geofence enforcement, battery protection, motor output limiting, and watchdog reset behavior.
