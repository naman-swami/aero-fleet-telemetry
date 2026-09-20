import pytest
from src.avionics_engine import AvionicsTelemetryEngine

def test_egt_degradation_alert():
    engine = AvionicsTelemetryEngine()
    res = engine.evaluate_egt_margin(current_egt_deg_c=930.0, redline_egt_deg_c=940.0, baseline_egt_deg_c=890.0)
    assert res["egt_margin_c"] == 10.0
    assert res["maintenance_status"] == "CRITICAL_MAINTENANCE_REQUIRED"
    assert "ATA 72" in res["recommended_ata_chapter"]
