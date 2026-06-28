# Firmware Update Protocol

Firmware update documentation should make update, verification, rollback, and recovery behavior clear.

## Update phases

1. Pre-update compatibility check
2. Artifact transfer
3. Integrity verification
4. Signature verification, when supported
5. Install or stage image
6. Reboot into new firmware
7. Post-update health check
8. Rollback if required

## Documentation requirements

- Supported update channels
- Required bootloader version
- Image format
- Manifest fields
- Checksum algorithm
- Power loss behavior
- Recovery procedure
- Rollback procedure
- User-visible status messages
