from __future__ import annotations
import hashlib, json
from pathlib import Path

REQUIRED = {"name", "version", "target", "artifact", "checksum", "build"}

def load_json(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)

def validate_manifest(data: dict) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED - set(data)
    if missing:
        errors.append(f"Missing required fields: {', '.join(sorted(missing))}")
    checksum = data.get("checksum", {})
    if checksum.get("algorithm") not in {"sha256", "sha512"}:
        errors.append("checksum.algorithm must be sha256 or sha512")
    value = checksum.get("value", "")
    if checksum.get("algorithm") == "sha256" and len(value) != 64:
        errors.append("sha256 checksum value should be 64 hex characters")
    if checksum.get("algorithm") == "sha512" and len(value) != 128:
        errors.append("sha512 checksum value should be 128 hex characters")
    artifact = data.get("artifact", {})
    if not artifact.get("filename"):
        errors.append("artifact.filename is required")
    if not artifact.get("format"):
        errors.append("artifact.format is required")
    return errors

def file_checksum(path: str | Path, algorithm: str = "sha256") -> str:
    h = hashlib.new(algorithm)
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
