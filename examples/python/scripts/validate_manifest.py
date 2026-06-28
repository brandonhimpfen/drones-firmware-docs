import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from drone_fw.manifest import load_json, validate_manifest

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_manifest.py <manifest.json>")
    errors = validate_manifest(load_json(sys.argv[1]))
    if errors:
        print("Manifest validation failed:")
        for e in errors: print(f"- {e}")
        raise SystemExit(1)
    print("Manifest validation passed.")
if __name__ == "__main__": main()
