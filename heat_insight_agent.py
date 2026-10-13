GeoAI Urban Heat Insight Assistant

Question-answering agent for Bengaluru heat-analysis results

from knowledge_graph import HEAT_METRICS, PROJECT_AREA

def answer_question(question):
"""Answer questions using the available GeoAI project results."""

question = question.lower()

mean_temp = HEAT_METRICS["mean_lst_celsius"]
min_temp = HEAT_METRICS["minimum_lst_celsius"]
max_temp = HEAT_METRICS["maximum_lst_celsius"]
risk_area = HEAT_METRICS["potential_heat_risk_area_km2"]
coverage = HEAT_METRICS["valid_data_coverage_percent"]
city = PROJECT_AREA["name"]

if any(word in question for word in ["mean", "average"]):
    return (
        f"The mean land surface temperature for {city} "
        f"in this analysis is {mean_temp} °C."
    )

elif "minimum" in question or "lowest" in question:
    return (
        f"The minimum land surface temperature recorded "
        f"in this analysis is {min_temp} °C."
    )

elif "maximum" in question or "highest" in question:
    return (
        f"The maximum land surface temperature recorded "
        f"in this analysis is {max_temp} °C."
    )

elif "risk" in question or "area" in question:
    return (
        f"The estimated potential heat-risk area is "
        f"{risk_area} km². This is a project-specific "
        "estimate, not a health-risk assessment."
    )

elif "coverage" in question or "valid data" in question:
    return (
        f"The valid satellite-data coverage reported "
        f"for this analysis is {coverage}%."
    )

elif "city" in question or "location" in question or "bengaluru" in question:
    return (
        f"The study area is {city}, "
        f"{PROJECT_AREA['state']}, {PROJECT_AREA['country']}."
    )

else:
    return (
        "I can answer questions about mean, minimum, and "
        "maximum land surface temperature, potential "
        "heat-risk area, data coverage, and study location. "
        "Please ask about one of these topics."
    )

if name == "main":
print("GeoAI Urban Heat Insight Assistant")
print("Type 'exit' to stop.")

while True:
    question = input("\nAsk a question: ")

    if question.strip().lower() == "exit":
        print("Goodbye!")
        break

    print("\nAssistant:", answer_question(question))
