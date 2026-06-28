# Flight Controller Firmware

The flight controller coordinates sensor input, state estimation, flight modes, control loops, actuator allocation, safety monitoring, and communications.

## Main responsibilities

- Maintain attitude and position estimates
- Execute flight mode logic
- Run control loops within timing constraints
- Convert control demands to motor/servo outputs
- Enforce arming, failsafe, and geofence constraints
- Publish telemetry and logs
- Accept safe configuration updates

## Documentation checklist

Document:

- Supported vehicle types
- Supported hardware targets
- Supported firmware versions
- Flight modes and transitions
- Controller rates and priorities
- Sensor requirements
- Actuator outputs
- Parameters
- Safety constraints
- Test evidence

## Flight mode documentation

Each flight mode should include:

- Purpose
- Entry conditions
- Exit conditions
- Required sensors
- Control authority
- Operator expectations
- Failsafe interactions
- Parameters
- Known limitations

## Example mode table

| Mode | Requires GPS | Requires RC | Autonomous | Typical use |
|---|---|---|---|---|
| Manual | No | Yes | No | Pilot control |
| Stabilized | No | Yes | No | Assisted control |
| Altitude hold | No | Yes | Partial | Altitude stabilization |
| Position hold | Yes | Yes | Partial | Hovering and station keeping |
| Mission | Yes | Optional | Yes | Waypoint execution |
| Return-to-launch | Yes | Optional | Yes | Recovery behavior |
