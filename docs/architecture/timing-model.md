# Timing Model

Drone firmware depends on predictable execution timing. Documentation should make timing assumptions visible.

## Timing table template

| Task | Rate | Deadline | Priority | Failure impact |
|---|---:|---:|---|---|
| IMU sampling | 1 kHz | 1 ms | High | Estimator instability |
| Attitude estimator | 250 Hz | 4 ms | High | Poor attitude state |
| Rate controller | 400 Hz | 2.5 ms | High | Control degradation |
| Telemetry publish | 10-50 Hz | Best effort | Medium | Reduced observability |
| Log writer | 10-100 Hz | Best effort | Low | Data loss risk |

## Jitter documentation

Document acceptable jitter for control-critical tasks. Include how jitter is measured, which logs expose it, and what thresholds trigger investigation.

## Watchdog expectations

Describe watchdog timeout values, heartbeat sources, reset behavior, and post-reset diagnostics.
