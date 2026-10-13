
# GeoAI Urban Heat Insight Assistant
# Question-answering agent for Bengaluru heat results

from knowledge_graph import HEAT_METRICS, PROJECT_AREA


def answer_question(question):
    """Answer questions using the available project results."""
    question = question.lower().strip()

    mean_temp = HEAT_METRICS["mean_lst_celsius"]
    min_temp = HEAT_METRICS["minimum_lst_celsius"]
    max_temp = HEAT_METRICS["maximum_lst_celsius"]
    risk_area = HEAT_METRICS["potential_heat_risk_area_km2"]
    coverage = HEAT_METRICS["valid_data_coverage_percent"]
    city = PROJECT_AREA["name"]

    # Check location questions first
    if any(word in question for word in [
        "where", "location", "city", "study area", "which city"
    ]):
        return (
            f"Study area: {city}, {PROJECT_AREA['state']}, "
            f"{PROJECT_AREA['country']}."
        )

    # Temperature questions
    if "mean" in question or "average" in question:
        return f"Mean land surface temperature in {city}: {mean_temp} °C."

    if "minimum" in question or "lowest" in question:
        return f"Minimum land surface temperature: {min_temp} °C."

    if "maximum" in question or "highest" in question:
        return f"Maximum land surface temperature: {max_temp} °C."

    # Heat-risk area questions
    if "risk" in question or "heat-risk" in question or "area" in question:
        return (
            f"Estimated potential heat-risk area: {risk_area} km². "
            "This is a project estimate, not a health-risk assessment."
        )

    # Data coverage questions
    if "coverage" in question or "valid data" in question:
        return f"Valid satellite-data coverage: {coverage}%."

    return (
        "I can answer questions about mean, minimum, and maximum "
        "temperature, potential heat-risk area, data coverage, "
        "and study location."
    )


if __name__ == "__main__":
    print("GeoAI Urban Heat Insight Assistant")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nAsk a question: ")

        if question.strip().lower() == "exit":
            print("Goodbye!")
            break

        print("Assistant:", answer_question(question))
