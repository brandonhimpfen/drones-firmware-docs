# Command Protocol Documentation

Command documentation should define what commands exist, when they are accepted, and what safety checks apply.

## Command fields

- Command name
- Required permissions
- Accepted modes
- Required health state
- Parameters
- Acknowledgement behavior
- Timeout behavior
- Rejection reasons
- Audit/log fields

## Safety-sensitive commands

Commands that arm, disarm, change modes, change mission state, modify parameters, update firmware, or alter geofence behavior require explicit documentation and test coverage.
