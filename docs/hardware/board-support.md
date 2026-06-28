# Board Support Documentation

Board support documentation connects firmware behavior to specific hardware targets.

## Board support table

| Field | Description |
|---|---|
| Board name | Human-readable name |
| Target ID | Build/flash identifier |
| MCU | Processor family and variant |
| Sensors | Built-in IMU, barometer, magnetometer, etc. |
| Buses | I2C, SPI, UART, CAN, USB |
| Outputs | PWM, DShot, GPIO, payload channels |
| Storage | Flash, SD, FRAM, EEPROM |
| Bootloader | Version and update path |

## Compatibility expectations

Each firmware release should identify supported boards and minimum bootloader versions.
