# imAIs — AI for Industry

AI-powered industrial monitoring system combining anomaly detection, predictive maintenance, incident reporting, and a RAG-based maintenance chatbot.

The objective is to simulate an industrial monitoring environment where operators can supervise machines, detect abnormal behavior, receive maintenance recommendations, and ask questions grounded in technical maintenance documentation.

---

## Features

- Synthetic industrial sensor data generation
- Multi-machine monitoring
- Multi-sensor monitoring:
  - temperature
  - vibration
  - pressure
  - energy consumption
- Anomaly detection
- Severity classification: HIGH / CRITICAL
- Operational risk scoring
- Predictive maintenance alerts using moving averages
- Trend-based degradation detection
- Generated incident summaries
- Historical incident logging
- RAG-based maintenance chatbot
- Source-grounded assistant responses

---

## Tech Stack

- Python
- Pandas
- NumPy
- Streamlit
- LangChain
- ChromaDB
- OpenAI API

---

## Project Structure

```text
imAIs/
│
├── app.py
├── data_simulation.py
├── anomaly_detection.py
├── predictive_maintenance.py
├── incident_reporting.py
├── maintenance_assistant.py
├── rag_assistant.py
│
├── maintenance_docs/
│   ├── temperature_maintenance.txt
│   ├── vibration_maintenance.txt
│   ├── pressure_maintenance.txt
│   └── energy_consumption_maintenance.txt
│
├── incident_history.csv
├── requirements.txt
├── README.md
└── .gitignore
