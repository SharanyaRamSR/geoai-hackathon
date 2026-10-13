Knowledge Graph for GeoAI Urban Heat Insight Assistant

Prepared for later integration with FalkorDB

PROJECT_AREA = {
"name": "Bengaluru",
"state": "Karnataka",
"country": "India",
"type": "StudyArea",
}

HEAT_METRICS = {
"mean_lst_celsius": 31.65,
"minimum_lst_celsius": 21.65,
"maximum_lst_celsius": 42.52,
"potential_heat_risk_area_km2": 34.68,
"valid_data_coverage_percent": 95.01,
}

Graph nodes represent entities and measured project results.

NODES = [
{
"id": "bengaluru",
"label": "StudyArea",
"properties": PROJECT_AREA,
},
{
"id": "lst_mean",
"label": "HeatMetric",
"properties": {
"name": "Mean Land Surface Temperature",
"value": HEAT_METRICS["mean_lst_celsius"],
"unit": "°C",
},
},
{
"id": "lst_min",
"label": "HeatMetric",
"properties": {
"name": "Minimum Land Surface Temperature",
"value": HEAT_METRICS["minimum_lst_celsius"],
"unit": "°C",
},
},
{
"id": "lst_max",
"label": "HeatMetric",
"properties": {
"name": "Maximum Land Surface Temperature",
"value": HEAT_METRICS["maximum_lst_celsius"],
"unit": "°C",
},
},
{
"id": "heat_risk_area",
"label": "HeatRiskMetric",
"properties": {
"name": "Potential Heat-Risk Area",
"value": HEAT_METRICS["potential_heat_risk_area_km2"],
"unit": "km²",
},
},
]

Relationships connect the study area to its results.

EDGES = [
{
"source": "bengaluru",
"relationship": "HAS_METRIC",
"target": "lst_mean",
},
{
"source": "bengaluru",
"relationship": "HAS_METRIC",
"target": "lst_min",
},
{
"source": "bengaluru",
"relationship": "HAS_METRIC",
"target": "lst_max",
},
{
"source": "bengaluru",
"relationship": "HAS_HEAT_RISK_ESTIMATE",
"target": "heat_risk_area",
},
]

def show_graph_summary():
"""Display the knowledge graph structure."""
print("GEOAI KNOWLEDGE GRAPH")
print("Study area:", PROJECT_AREA["name"])
print("Number of nodes:", len(NODES))
print("Number of relationships:", len(EDGES))

print("\nNODES")
for node in NODES:
    print("-", node["id"], "|", node["label"])

print("\nRELATIONSHIPS")
for edge in EDGES:
    print(
        edge["source"],
        "-[" + edge["relationship"] + "]->",
        edge["target"],
    )

if name == "main":
show_graph_summary()
