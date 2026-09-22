# Aero Fleet Telemetry & Turbofan Health Monitor

> **FAA Part 121 Predictive Maintenance & Engine Condition Monitoring (ECM)**  
> Tracking Exhaust Gas Temperature (EGT) Margin Degradation and Dual-Spool Shaft Vibration.

---

### Aircraft Engine Health Formulations

1. **EGT Margin Degradation ($^{\circ}\text{C}$)**:
   $$\Delta EGT_{margin} = EGT_{redline} - \left( EGT_{takeoff} + \Delta T_{ambient} \right)$$
   *Threshold*: $\Delta EGT_{margin} < 15^{\circ}\text{C}$ mandates immediate engine combustor borescope inspection.

2. **Dual-Spool Vibration RMS**:
   Evaluates Low-Pressure ($N1$) and High-Pressure ($N2$) shaft rotor unbalance:
   $$Vib_{peak} = \sqrt{Vib_x^2 + Vib_y^2} \quad [\text{Inches per Second (IPS)}]$$
   *Threshold*: $Vib > 2.5\text{ IPS}$ generates automatic flight crew cockpit advisory.

---

### Quick Access Recorder (QAR) Ingestion

```console
$ python avionics.py --demo
======================================================================
AIRCRAFT ENGINE HEALTH TELEMETRY: Tail #N782AA (CFM56-7B)
Flight Phase: STEP-CLIMB (FL350 -> FL390)
======================================================================
* Left Engine (#1):  EGT Margin = 28.4°C | N1 Vib = 0.8 IPS (NOMINAL)
* Right Engine (#2): EGT Margin = 11.2°C | N1 Vib = 2.9 IPS (EXCEEDANCE)
======================================================================
[ACTION REQUIRED] Airworthiness Alert Issued:
- AMM Task 72-00-00-200-801: Borescope Inspection of HPT Stage 1 Blades
- Schedule maintenance at destination gate within 4 flight cycles.
```

---

### Telemetry CLI Execution

```bash
# Parse benchmark flight telemetry stream
python avionics.py --demo

# Run avionics calculation test suite
pytest tests/ -v
```

Engine operating envelopes and FAA airworthiness directives are documented in [AIRWORTHINESS_DIRECTIVES.md](AIRWORTHINESS_DIRECTIVES.md).
