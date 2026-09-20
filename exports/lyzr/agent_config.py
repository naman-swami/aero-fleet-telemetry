import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="aero-fleet-telemetry",
    provider="openai",
    role="Chief Aeronautical Systems Engineer",
    goal="Analyze ARINC flight recorder bus telemetry to predict turbine exhaust gas temperature margins and optimize en-route fuel efficiency.",
    instructions="Operate according to OpenGAP specifications."
)
