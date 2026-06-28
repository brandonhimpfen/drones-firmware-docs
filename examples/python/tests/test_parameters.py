from drone_fw.parameters import summarize_parameters, high_risk_parameters

def test_summary():
    catalog = {"parameters":[{"name":"A","type":"number","risk":"high","restart_required":True},{"name":"B","type":"boolean","risk":"low"}]}
    s = summarize_parameters(catalog)
    assert s["count"] == 2
    assert s["risk_counts"]["high"] == 1
    assert len(high_risk_parameters(catalog)) == 1
