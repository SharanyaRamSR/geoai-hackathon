GeoAI Urban Heat Insight Assistant

Hackathon Project

Study Area: Bengaluru, Karnataka, India

PROJECT_NAME = "GeoAI Urban Heat Insight Assistant"
STUDY_AREA = "Bengaluru, Karnataka, India"

Results from the existing Bengaluru heat analysis

HEAT_RESULTS = {
"mean_lst_celsius": 31.65,
"minimum_lst_celsius": 21.65,
"maximum_lst_celsius": 42.52,
"potential_heat_risk_area_km2": 34.68,
"valid_data_coverage_percent": 95.01,
}

def show_project_summary():
"""Display the current GeoAI project summary."""
print("=" * 50)
print(PROJECT_NAME)
print("Study Area:", STUDY_AREA)
print("=" * 50)

print("\nLAND SURFACE TEMPERATURE")
print("Mean:", HEAT_RESULTS["mean_lst_celsius"], "°C")
print("Minimum:", HEAT_RESULTS["minimum_lst_celsius"], "°C")
print("Maximum:", HEAT_RESULTS["maximum_lst_celsius"], "°C")

print("\nPOTENTIAL HEAT-RISK ANALYSIS")
print(
    "Potential heat-risk area:",
    HEAT_RESULTS["potential_heat_risk_area_km2"],
    "km²",
)
print(
    "Valid data coverage:",
    HEAT_RESULTS["valid_data_coverage_percent"],
    "%",
)

if name == "main":
show_project_summary()
