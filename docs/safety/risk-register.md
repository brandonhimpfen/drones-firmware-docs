# Firmware Risk Register

A firmware risk register tracks hazards, mitigations, validation evidence, and ownership.

## Risk fields

- Risk ID
- Hazard description
- Cause
- Impact
- Affected subsystem
- Likelihood
- Severity
- Mitigation
- Verification method
- Owner
- Status

## Example risks

| Risk | Mitigation |
|---|---|
| Incorrect motor order | Motor mapping tests and visual diagrams |
| Parameter migration error | Versioned migration tests |
| Sensor failure during flight | Health monitoring and failsafe behavior |
| Firmware update interruption | Bootloader recovery and rollback |
| Timing overrun | Runtime monitoring and regression tests |
