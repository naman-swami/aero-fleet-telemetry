import json
import argparse
from src.avionics_engine import AvionicsTelemetryEngine

def main():
    parser = argparse.ArgumentParser(description="Aero Fleet Telemetry CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated engine EGT margin trend audit")
    args = parser.parse_args()

    engine = AvionicsTelemetryEngine()
    report = engine.evaluate_egt_margin(current_egt_deg_c=912.0, redline_egt_deg_c=940.0, baseline_egt_deg_c=880.0)
    print("="*60)
    print(" AEROTELEMETRY AVIONICS HEALTH AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
