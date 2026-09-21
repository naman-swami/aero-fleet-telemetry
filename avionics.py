import argparse
import json
import os
from telemetry.turbine_vibration_engine import TurbineTelemetryEngine

def main():
    parser = argparse.ArgumentParser(description="Aero Fleet Telemetry CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample turbine telemetry stream")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "flight_logs", "engine_telemetry_stream.json")

    if args.demo:
        with open(data_file, "r") as f:
            flights = json.load(f)
        print("=== AERO FLEET TURBINE HEALTH MONITORING REPORT ===\n")
        for fl in flights:
            res = TurbineTelemetryEngine.evaluate_engine_health(
                egt_celsius=fl["egt_celsius"],
                egt_redline=fl["egt_redline_celsius"],
                n1_vib=fl["n1_vibration_ips"],
                n2_vib=fl["n2_vibration_ips"],
                oil_psi=fl["oil_pressure_psi"]
            )
            print(f"Flight: {fl['flight_id']} | Aircraft: {fl['tail_number']}")
            print(f"  EGT: {fl['egt_celsius']} C (Margin: {res['egt_margin_celsius']} C)")
            print(f"  Status: {res['airworthiness_status']} | Recommendation: {res['recommendation']}")
            for a in res["alerts"]:
                print(f"    * [{a['severity']}] {a['type']}: {a['desc']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
