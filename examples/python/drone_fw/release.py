from __future__ import annotations
from .manifest import validate_manifest

RELEASE_BLOCKERS = [
    "manifest_errors",
    "known_critical_issues",
    "missing_compatibility",
]

def release_readiness(manifest: dict) -> dict:
    errors = validate_manifest(manifest)
    known_issues = manifest.get("known_issues", [])
    compatibility = manifest.get("compatibility")
    blockers = []
    if errors:
        blockers.append("manifest_errors")
    if any("critical" in str(issue).lower() for issue in known_issues):
        blockers.append("known_critical_issues")
    if not compatibility:
        blockers.append("missing_compatibility")
    return {"ready": not blockers, "blockers": blockers, "manifest_errors": errors}
