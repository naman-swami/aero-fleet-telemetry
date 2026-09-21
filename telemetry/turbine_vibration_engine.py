"""
Turbine Engine Health & Telemetry Diagnostics Engine
Evaluates Exhaust Gas Temperature (EGT) margin erosion, spool vibration levels, and airworthiness status.
"""
from typing import Dict, Any

class TurbineTelemetryEngine:
    @staticmethod
    def evaluate_engine_health(
        egt_celsius: float,
        egt_redline: float,
        n1_vib: float,
        n2_vib: float,
        oil_psi: float
    ) -> Dict[str, Any]:
        egt_margin = round(egt_redline - egt_celsius, 1)

        alerts = []
        if egt_margin < 15.0:
            alerts.append({"type": "EGT_MARGIN_DEPLETION", "severity": "CRITICAL", "desc": "EGT margin critically low. Hot section deterioration imminent."})
        elif egt_margin < 30.0:
            alerts.append({"type": "EGT_MARGIN_EROSION", "severity": "WARNING", "desc": "EGT margin deteriorating. Schedule water wash."})

        if n1_vib > 1.0 or n2_vib > 1.0:
            alerts.append({"type": "HIGH_ROTOR_VIBRATION", "severity": "HIGH", "desc": "Rotor shaft imbalance detected exceeding 1.0 ips limit."})

        if oil_psi < 40.0:
            alerts.append({"type": "LOW_OIL_PRESSURE", "severity": "CRITICAL", "desc": "Lube oil pressure below safe operating threshold."})

        airworthy = len([a for a in alerts if a["severity"] == "CRITICAL"]) == 0

        return {
            "egt_margin_celsius": egt_margin,
            "airworthiness_status": "AIRWORTHY" if airworthy else "AOG_GROUNDED",
            "active_alerts_count": len(alerts),
            "alerts": alerts,
            "recommendation": "RETURN_TO_SERVICE" if airworthy else "UNSCHEDULED_MAINTENANCE_REQUIRED"
        }
