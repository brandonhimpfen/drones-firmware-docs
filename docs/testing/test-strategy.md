# Firmware Test Strategy

Drone firmware requires layered validation. No single test type is enough.

## Test layers

| Layer | Purpose |
|---|---|
| Static analysis | Detect style, type, security, and complexity issues |
| Unit tests | Validate isolated logic |
| Integration tests | Validate module interactions |
| Simulation/SITL | Validate behavior in simulated environments |
| Bench tests | Validate firmware on real hardware without flight |
| HIL tests | Validate firmware with hardware and simulated environment |
| Flight tests | Validate controlled real-world behavior |
| Regression tests | Prevent previously fixed issues from returning |

## Test documentation fields

Each test should document objective, setup, firmware version, parameters, hardware, steps, expected result, observed result, logs, pass/fail status, and reviewer.

See [`schemas/test-report.schema.json`](../../schemas/test-report.schema.json).
