# Firmware Release Process

Firmware releases should be reproducible, test-backed, documented, and reversible.

## Release stages

1. Scope freeze
2. Code freeze
3. Manifest generation
4. Static checks
5. Unit tests
6. Simulation tests
7. Bench tests
8. Hardware-in-the-loop tests
9. Controlled flight tests
10. Release notes review
11. Artifact signing/checksums
12. Release publication
13. Post-release monitoring

## Release artifact set

- Firmware binary
- Firmware manifest
- Checksums
- Parameter catalog
- Hardware compatibility matrix
- Release notes
- Test report summary
- Known issues
- Rollback procedure

## Release readiness gates

A release should not proceed if:

- Required tests are missing or failing
- Failsafe behavior changed without review
- Parameter changes are undocumented
- Hardware compatibility is unclear
- Rollback path is untested
- Known critical issues are unresolved

Use [`checklists/release-readiness.md`](../../checklists/release-readiness.md).
