import os
import pytest
from telemetry.turbine_vibration_engine import TurbineTelemetryEngine

def test_nominal_engine_airworthy():
    res = TurbineTelemetryEngine.evaluate_engine_health(
        egt_celsius=650.0, egt_redline=725.0, n1_vib=0.3, n2_vib=0.3, oil_psi=50.0
    )
    assert res["airworthiness_status"] == "AIRWORTHY"
    assert res["egt_margin_celsius"] == 75.0
    assert res["active_alerts_count"] == 0

def test_critical_egt_grounding():
    res = TurbineTelemetryEngine.evaluate_engine_health(
        egt_celsius=720.0, egt_redline=725.0, n1_vib=1.2, n2_vib=0.4, oil_psi=50.0
    )
    assert res["airworthiness_status"] == "AOG_GROUNDED"
    assert res["egt_margin_celsius"] == 5.0
    types = [a["type"] for a in res["alerts"]]
    assert "EGT_MARGIN_DEPLETION" in types
    assert "HIGH_ROTOR_VIBRATION" in types
