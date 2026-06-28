from __future__ import annotations
from collections import Counter

def summarize_parameters(catalog: dict) -> dict:
    params = catalog.get("parameters", [])
    risks = Counter(p.get("risk", "unknown") for p in params)
    types = Counter(p.get("type", "unknown") for p in params)
    restart_required = sum(1 for p in params if p.get("restart_required"))
    return {"count": len(params), "risk_counts": dict(risks), "type_counts": dict(types), "restart_required": restart_required}

def high_risk_parameters(catalog: dict) -> list[dict]:
    return [p for p in catalog.get("parameters", []) if p.get("risk") == "high"]
