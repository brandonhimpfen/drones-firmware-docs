# Drones Firmware Docs

Production-oriented firmware documentation for drones, UAV platforms, flight controllers, embedded subsystems, telemetry links, and Python-based tooling.

This repository is designed as a complete in-repo documentation handbook for teams building, reviewing, testing, maintaining, or operating drone firmware. It focuses on practical engineering documentation rather than marketing material.

> **Safety note:** Drone firmware controls real aircraft. Use this repository as documentation guidance, not as a substitute for qualified engineering review, regulatory compliance, flight testing, or safety certification.

## What this repo contains

- Firmware architecture documentation
- Flight controller subsystem documentation
- Sensor, actuator, power, and communication documentation
- Firmware lifecycle and release process guidance
- Safety, failsafe, and pre-flight documentation templates
- Test plans for unit, integration, bench, HIL, SITL, and flight testing
- Python examples for telemetry parsing, configuration validation, log analysis, and release checks
- JSON schemas for firmware manifests, parameter catalogs, and test reports
- Contributor, governance, security, and documentation standards

## Intended audience

This repository is useful for:

- Drone firmware engineers
- Robotics engineers
- Embedded systems teams
- UAV platform maintainers
- Test and validation engineers
- Technical writers documenting firmware behavior
- Open-source drone tooling maintainers
- Research labs building autonomous aerial platforms

## Repository structure

```text
drones-firmware-docs/
├── docs/                  # Main documentation handbook
│   ├── architecture/       # System architecture and firmware design
│   ├── firmware/           # Firmware modules, parameters, builds, releases
│   ├── hardware/           # Hardware-facing firmware docs
│   ├── protocols/          # Telemetry, command, logging, update protocols
│   ├── testing/            # Test strategy and validation docs
│   ├── safety/             # Safety, failsafe, geofence, risk docs
│   ├── operations/         # Field operations and maintenance docs
│   └── reference/          # Glossary, templates, decision records
├── examples/python/        # Python tooling examples
├── schemas/                # JSON schemas for documentation artifacts
├── checklists/             # Practical review and release checklists
└── .github/                # GitHub templates and CI
```

## Start here

Read the handbook in this order:

1. [Documentation principles](docs/README.md)
2. [Firmware architecture overview](docs/architecture/overview.md)
3. [Flight controller documentation](docs/firmware/flight-controller.md)
4. [Parameters and configuration](docs/firmware/parameters.md)
5. [Safety and failsafe documentation](docs/safety/failsafe.md)
6. [Testing strategy](docs/testing/test-strategy.md)
7. [Release process](docs/firmware/release-process.md)

## Example Python tools

The `examples/python` folder includes small, dependency-light utilities that demonstrate documentation-supporting workflows:

- Validate firmware manifests
- Parse parameter catalogs
- Summarize telemetry logs
- Check release readiness
- Generate test report summaries

Run tests:

```bash
cd examples/python
python -m pytest
```

Run a sample release check:

```bash
python scripts/release_check.py ../../sample-firmware-manifest.json
```

## Design goals

This repo is intentionally:

- **Docs-first:** documentation is the product.
- **Production-minded:** templates assume real review, testing, release, and maintenance workflows.
- **Platform-neutral:** applicable to custom firmware, PX4-like systems, ArduPilot-like systems, research drones, and proprietary stacks.
- **Safety-aware:** emphasizes traceability, failsafe documentation, operational limits, and test evidence.
- **Maintainable:** structured so teams can copy, extend, version, and review docs like code.

## Non-goals

This repository does not provide:

- Complete flight firmware
- Instructions for bypassing drone safety systems
- Weapons, payload targeting, or harmful-use guidance
- Regulatory legal advice
- A replacement for certification, field testing, or professional engineering review

## License

MIT. See [LICENSE](LICENSE).
