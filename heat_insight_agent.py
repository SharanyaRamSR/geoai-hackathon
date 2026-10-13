
# GeoAI Urban Heat Insight Assistant
# Retrieves Bengaluru heat metrics directly from FalkorDB.

import os
from falkordb import FalkorDB


def connect_to_graph():
    host = os.environ.get("FALKORDB_HOST")
    password = os.environ.get("FALKORDB_PASSWORD")
    username = os.environ.get("FALKORDB_USERNAME", "geoai")
    port = int(os.environ.get("FALKORDB_PORT", "61018"))

    if not host or not password:
        raise RuntimeError(
            "Set FALKORDB_HOST and FALKORDB_PASSWORD "
            "as environment variables before running."
        )

    db = FalkorDB(
        host=host,
        port=port,
        username=username,
        password=password,
        ssl=False,
        socket_timeout=10,
        socket_connect_timeout=10,
    )

    return db.select_graph("geoai_heat_insights")


def get_graph_data(graph):
    result = graph.query("""
        MATCH (s:StudyArea {name: 'Bengaluru'})
              -[:HAS_METRIC]->(m:HeatMetric)
        RETURN m.name, m.value, m.unit
    """)

    metrics = {}
    for name, value, unit in result.result_set:
        metrics[name] = {"value": value, "unit": unit}

    if not metrics:
        raise RuntimeError(
            "No heat metrics found in the FalkorDB graph."
        )

    return metrics



def answer_question(question, metrics, city="Bengaluru"):
    question = question.lower().strip()

    if "summary" in question or "overall heat" in question:
        summary = [
            ("Mean LST", "Mean LST"),
            ("Minimum LST", "Minimum LST"),
            ("Maximum LST", "Maximum LST"),
            ("High-Heat Area", "High-Heat Area"),
            ("Potential Heat-Risk Area", "Potential Heat-Risk Area"),
            ("Valid Data Coverage", "Valid Data Coverage"),
        ]

        lines = ["Bengaluru Urban Heat Summary:"]
        for label, key in summary:
            metric = metrics[key]
            lines.append(
                f"{label}: {metric['value']} {metric['unit']}"
            )

        return "\n".join(lines)

    if any(word in question for word in [
        "where", "location", "city", "which city"
    ]):
        return f"Study area: {city}, Karnataka, India."

    if "coverage" in question or "valid data" in question:
        m = metrics["Valid Data Coverage"]
        return f"Valid satellite-data coverage: {m['value']}{m['unit']}."

    if "90th" in question or "percentile" in question or "threshold" in question:
        m = metrics["90th Percentile LST Threshold"]
        return f"90th percentile LST threshold: {m['value']} {m['unit']}."

    if "minimum" in question or "lowest" in question:
        m = metrics["Minimum LST"]
        return f"Minimum land surface temperature: {m['value']} {m['unit']}."

    if "maximum" in question or "highest" in question:
        m = metrics["Maximum LST"]
        return f"Maximum land surface temperature: {m['value']} {m['unit']}."

    if "mean" in question or "average" in question:
        m = metrics["Mean LST"]
        return f"Mean land surface temperature in {city}: {m['value']} {m['unit']}."

    if "high-heat" in question or "high heat" in question:
        m = metrics["High-Heat Area"]
        return f"High-heat area: {m['value']} {m['unit']}."

    if "risk" in question or ("area" in question and "total" not in question):
        m = metrics["Potential Heat-Risk Area"]
        return (
            f"Estimated potential heat-risk area: "
            f"{m['value']} {m['unit']}. "
            "This is a project estimate, not a health-risk assessment."
        )

    if "total" in question or "study area size" in question:
        m = metrics["Total Study Area"]
        return f"Total study area: {m['value']} {m['unit']}."

    return (
        "I can answer questions about mean, minimum, and maximum "
        "temperature, high-heat area, potential heat-risk area, "
        "the 90th percentile threshold, data coverage, and study area."
    )

if __name__ == "__main__":
    try:
        graph = connect_to_graph()
        metrics = get_graph_data(graph)
        print("GeoAI Urban Heat Insight Assistant")
        print("Connected to FalkorDB successfully.")
        print("Type 'exit' to stop.")

        while True:
            question = input("\nAsk a question: ")

            if question.strip().lower() == "exit":
                print("Goodbye!")
                break

            try:
                print("Assistant:", answer_question(question, metrics))
            except KeyError as error:
                print("Required metric missing from graph:", error)

    except Exception as error:
        print("Could not start the assistant:", error)
