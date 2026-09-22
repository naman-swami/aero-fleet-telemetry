# Federal Aviation Airworthiness Standards & Turbofan Telemetry

## 1. Regulatory Authority & Operational Framework
Aero Fleet Telemetry monitors commercial turbofan engine health parameters under:
- **Federal Aviation Regulations (14 CFR Part 121: Operating Requirements: Domestic, Flag, and Supplemental Operations)**
- **FAA Advisory Circular AC 120-113 (Engine Condition Monitoring Programs)**
- **ICAO Annex 6 (Operation of Aircraft) Part I — International Commercial Air Transport**

---

## 2. Turbofan Engine Health Formulations & Limits
The condition monitoring engine (`telemetry/turbine_vibration_engine.py`) models twin-spool high-bypass turbofan architectures (e.g., CFM International CFM56-7B, LEAP-1B, and GE90 series).

### A. Exhaust Gas Temperature (EGT) Margin Deterioration
EGT is the primary indicator of high-pressure turbine (HPT) blade efficiency and thermal degradation:

$$\Delta EGT_{\text{margin}} = EGT_{\text{redline}} - \left( EGT_{\text{takeoff}} + \Delta T_{\text{ambient}} \right)$$

- **New / Overhauled Engine**: $\Delta EGT_{\text{margin}} \in [40^{\circ}\text{C}, 65^{\circ}\text{C}]$.
- **Advisory Threshold**: $\Delta EGT_{\text{margin}} < 20^{\circ}\text{C}$ (schedule performance restoration wash).
- **Critical Limit**: $\Delta EGT_{\text{margin}} < 15^{\circ}\text{C}$ (mandates on-wing borescope inspection of HPT Stage 1 blades within 10 flight cycles).

### B. Dual-Spool Shaft Vibration RMS
Rotor unbalance is monitored independently across Low-Pressure ($N1$, fan and booster) and High-Pressure ($N2$, compressor and HPT) shafts:

$$Vib_{\text{peak}} = \sqrt{Vib_x^2 + Vib_y^2} \quad [\text{Inches per Second (IPS)}]$$

- **Nominal Operating Vibration**: $0.2 - 1.2\text{ IPS}$.
- **Cautionary Advisory**: $> 2.0\text{ IPS}$.
- **Cockpit Exceedance Alarm**: $> 2.5\text{ IPS}$ sustained for $> 10\text{ seconds}$ triggers an automatic in-flight pilot notification.

---

## 3. Aircraft Maintenance Manual (AMM) Escalation Procedures
When flight data exceedance is confirmed from Quick Access Recorder (QAR) feeds:
1. **AMM Task 72-00-00-200-801**: Immediate borescope inspection of combustor liner, nozzle guide vanes, and HPT blades for thermal cracks or coating spallation.
2. **Oil Debris Analysis**: Quantitative magnetic chip detector inspection for ferromagetic particulate accumulation.
3. **Master Minimum Equipment List (MMEL)**: Evaluation of dispatch capability for subsequent flight legs.
