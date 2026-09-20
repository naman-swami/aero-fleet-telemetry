# Explainability — aero-fleet-telemetry

## Decision Reasoning
AeroTelemetry models thermodynamic cycle efficiencies, comparing observed pressure ratios and turbine temperatures against nominal OEM performance baselines.

## Data Sources and Inputs Used
ARINC 429/717 flight data recorders, ACARS real-time engine health telemetry, FAA airworthiness directives, and OEM maintenance manuals.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, aero-fleet-telemetry assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, aero-fleet-telemetry will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, aero-fleet-telemetry explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
aero-fleet-telemetry actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Air Traffic Control: Cannot authorize flight level or course deviations without ATC clearance.
- Physical Inspection: Cannot perform hands-on visual or physical borescope maintenance directly.
- Aircraft Design: Cannot modify FAA-certified aircraft flight envelope limits or structural tolerances.
- Emergency Response: In-flight emergency piloting decisions remain under sole command of the Captain.

## Uncertainty Quantification Approach
When sensor telemetry exhibits intermittent packet dropouts during severe atmospheric turbulence, AeroTelemetry flags sensor unreliability and reverts to moving-average trend baselines.
