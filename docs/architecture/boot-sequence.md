# Boot Sequence

The boot sequence defines how the drone moves from reset to operational readiness.

## Recommended boot stages

1. Reset vector and bootloader entry
2. Firmware image validation
3. Hardware board identification
4. Clock, memory, and peripheral initialization
5. Parameter storage mount
6. Sensor bus discovery
7. Driver startup
8. Safety supervisor startup
9. Communication link startup
10. Pre-arm health checks
11. Ready state

## Documentation requirements

For each stage document:

- Expected duration
- Blocking dependencies
- Error handling
- Log messages
- Recovery behavior
- User-visible indicators

## Boot failure examples

| Failure | Expected behavior | Documentation required |
|---|---|---|
| Invalid firmware image | Stay in bootloader or rollback | Recovery and reflash procedure |
| Sensor missing | Prevent arming unless optional | Sensor requirement table |
| Parameter corruption | Load defaults or safe backup | Parameter recovery procedure |
| Battery below threshold | Prevent arming | Battery safety thresholds |
| Watchdog reset loop | Enter degraded/recovery state | Diagnostic collection process |
