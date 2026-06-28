# Parameters and Configuration

Firmware parameters define behavior. Poorly documented parameters can create unsafe or unreproducible aircraft behavior.

## Parameter documentation fields

Each parameter should include:

- Name
- Type
- Default value
- Allowed range
- Units
- Description
- Safety impact
- Restart requirement
- Version introduced
- Version deprecated, if applicable
- Related parameters
- Test coverage

## Parameter risk levels

| Risk level | Meaning | Review expectation |
|---|---|---|
| Low | Logging, UI, or non-control setting | Standard review |
| Medium | Affects behavior but not direct stability | Firmware + test review |
| High | Affects control, arming, failsafe, motor output, or geofence | Safety + firmware + flight test review |

## Configuration principles

- Defaults should be safe for supported hardware.
- Unit conventions must be explicit.
- Invalid values should fail closed.
- Dangerous changes should require review or guarded tooling.
- Parameter migrations should be documented across releases.

See [`schemas/parameter-catalog.schema.json`](../../schemas/parameter-catalog.schema.json).
