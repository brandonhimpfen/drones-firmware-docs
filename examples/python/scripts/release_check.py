import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from drone_fw.manifest import load_json
from drone_fw.release import release_readiness

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: release_check.py <manifest.json>")
    result = release_readiness(load_json(sys.argv[1]))
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["ready"] else 1)
if __name__ == "__main__": main()
