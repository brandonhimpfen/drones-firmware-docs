# Firmware Release Readiness Checklist

## Documentation

- [ ] Release notes are complete
- [ ] Firmware manifest is complete
- [ ] Parameter catalog is updated
- [ ] Hardware compatibility matrix is updated
- [ ] Known issues are documented
- [ ] Rollback procedure is documented

## Testing

- [ ] Unit tests passed
- [ ] Integration tests passed
- [ ] SITL tests passed
- [ ] Bench tests passed
- [ ] HIL tests passed, if required
- [ ] Flight tests passed, if required
- [ ] Failsafe tests passed

## Safety

- [ ] Failsafe changes reviewed
- [ ] Geofence behavior reviewed
- [ ] Arming checks reviewed
- [ ] Battery thresholds reviewed
- [ ] Critical parameters reviewed

## Release artifacts

- [ ] Firmware binary produced
- [ ] Checksums produced
- [ ] Manifest produced
- [ ] Artifacts stored in release location
- [ ] Rollback artifact available
