# Sensor Documentation

Sensor documentation should describe how raw measurements become trusted state inputs.

## Sensors commonly documented

- IMU / accelerometer / gyroscope
- Magnetometer
- Barometer
- GNSS / GPS
- Rangefinder
- Optical flow
- Airspeed sensor
- Battery monitor

## Required details

- Driver name
- Bus and address
- Sampling rate
- Calibration process
- Units
- Filtering
- Failure detection
- Failsafe interaction
- Log fields
- Test method

## Sensor health states

| State | Meaning |
|---|---|
| Present | Device detected |
| Calibrated | Calibration data available |
| Healthy | Data within expected range |
| Degraded | Data usable with caution |
| Failed | Data unavailable or unsafe |
