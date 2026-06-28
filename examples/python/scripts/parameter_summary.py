import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from drone_fw.manifest import load_json
from drone_fw.parameters import summarize_parameters, high_risk_parameters

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: parameter_summary.py <parameter-catalog.json>")
    catalog = load_json(sys.argv[1])
    print(json.dumps(summarize_parameters(catalog), indent=2))
    high = high_risk_parameters(catalog)
    if high:
        print("High-risk parameters:")
        for p in high: print(f"- {p['name']}: {p['description']}")
if __name__ == "__main__": main()
