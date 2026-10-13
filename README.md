Bengaluru Urban Heat Island Detection Using GeoAI

Project Overview

Bengaluru Urban Heat Insight Assistant is a GeoAI project that combines satellite-based remote sensing, geospatial analysis, artificial intelligence, and knowledge graphs to identify high-temperature areas in Bengaluru, Karnataka, India.

The project analyses Land Surface Temperature (LST) to identify potential urban heat hotspots and supports the interpretation of geospatial results through an AI-assisted workflow.

Problem Statement

Rapid urbanisation, reduced vegetation, and changes in land cover can contribute to elevated surface temperatures in cities. Identifying high-heat areas helps researchers, urban planners, and communities better understand urban heat patterns.

This project explores how GeoAI can make satellite-derived heat information easier to analyse and interpret.

Objectives

- Analyse satellite-derived Land Surface Temperature across Bengaluru.
- Identify areas with relatively high surface temperatures.
- Apply geospatial analysis to understand the spatial distribution of heat.
- Organise relevant project knowledge using a graph database.
- Develop an AI-assisted interface for answering questions about urban heat insights.

Technology Stack

- Google Earth Engine: Satellite data access and geospatial processing.
- Google Colab: Python-based analysis and experimentation.
- Python: Data processing and application development.
- GeoAI and Remote Sensing: Environmental analysis and heat hotspot identification.
- FalkorDB: Graph database for representing connected project knowledge.
- AI Agent: Interpreting user questions and providing context-aware urban heat insights.
- GitHub: Project source code and documentation.

Methodology

1. Study Area Selection: Define Bengaluru as the geographical area of interest.
2. Satellite Data Processing: Access and process relevant satellite-derived environmental data.
3. Land Surface Temperature Analysis: Generate and inspect LST results.
4. Heat Hotspot Identification: Apply a percentile-based threshold to identify relatively high-temperature pixels.
5. Geospatial Visualisation: Display temperature patterns and potential high-heat areas on a map.
6. Results Extraction: Summarise relevant metrics and export analytical results.
7. Knowledge Graph Integration: Represent relevant concepts and relationships in FalkorDB.
8. AI-Assisted Insights: Connect the analysis and knowledge layer to support natural-language exploration of urban heat information.

Key Features

- Satellite-based urban heat analysis.
- Identification of potential high-heat areas.
- Map-based visualisation of Land Surface Temperature.
- Percentile-based hotspot thresholding.
- Exportable analytical results.
- Graph-based knowledge representation.
- AI-assisted interpretation of urban heat information.

Expected Impact

The project demonstrates how remote sensing, GIS, knowledge graphs, and AI agents can work together to make urban environmental information more accessible.

Potential applications include urban planning, heat-risk screening, environmental monitoring, and identifying areas for further investigation.

Limitations

Land Surface Temperature is not the same as near-surface air temperature. A detected hotspot does not, by itself, establish human heat exposure or health risk.

The results depend on satellite data quality, acquisition dates, spatial resolution, processing choices, and the selected hotspot threshold. Additional ground measurements and demographic information would be needed for detailed heat-risk assessment.

Repository Structure

- "README.md" — Project overview and documentation.
- "geoai_assistant.py" — GeoAI assistant application.
- "knowledge_graph.py" — Knowledge graph functionality.
- "heat_insight_agent.py" — Urban heat insight agent.
- "requirements.txt" — Python dependencies.

Future Improvements

- Integrate additional satellite and environmental datasets.
- Improve knowledge graph coverage and retrieval.
- Validate satellite-derived temperature patterns using independent observations.
- Incorporate population and land-use information for more detailed heat-risk analysis.
- Expand the AI assistant with evidence-grounded answers and interactive geospatial insights.

Conclusion

Bengaluru Urban Heat Island Detection Using GeoAI demonstrates a workflow for combining satellite-derived temperature analysis with graph-based knowledge and AI-assisted interpretation. The project aims to support more accessible, data-informed understanding of urban heat patterns.

---

Project Domain: GeoAI | Remote Sensing | GIS | Artificial Intelligence | Knowledge Graphs

Study Area: Bengaluru, Karnataka, India
