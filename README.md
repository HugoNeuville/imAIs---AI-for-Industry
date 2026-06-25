# Industrial Monitoring AI System

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
├── screenshots/
│   ├── dashboard_overview.png
│   ├── temperature_monitoring.png
│   ├── risk_dashboard.png
│   ├── predictive_alerts.png
│   ├── incident_summary.png
│   └── rag_chatbot.png
│
├── incident_history.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/HugoNeuville/imAIs---AI-for-Industry.git
cd imAIs---AI-for-Industry
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your OpenAI API key:

### PowerShell

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### Windows CMD

```cmd
set OPENAI_API_KEY=your_api_key_here
```

---

## How to Run

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal.

---

## Screenshots

### Dashboard Overview

<img width="747" height="697" alt="dashboard_overview" src="https://github.com/user-attachments/assets/4e2cf1f8-c933-4339-8c30-c70e9ed84709" />

---

### Temperature Monitoring

<img width="757" height="677" alt="temperature_monitoring" src="https://github.com/user-attachments/assets/0a3a6a6e-63f4-4b08-944f-34d8c280ddc2" />

---

### Risk Dashboard

<img width="761" height="712" alt="risk_dashboard" src="https://github.com/user-attachments/assets/e171743d-4b33-4009-af44-e5102b561ccf" />

---

### Predictive Maintenance Alerts

<img width="747" height="817" alt="predictive_maintenance_alerts" src="https://github.com/user-attachments/assets/d5c5e344-6515-4a65-b33a-0810ddfb2a6f" />

---

### Incident Summary

<img width="742" height="826" alt="incident_summary" src="https://github.com/user-attachments/assets/023ea909-7e07-4c19-875f-fe369de3fcfd" />

---

### RAG Maintenance Chatbot

<img width="737" height="470" alt="rag_chatbot" src="https://github.com/user-attachments/assets/cd195e7d-6fea-4d33-9c21-375e0df22af9" />

---

## Current Status

This is the first working version of the system.

The current version focuses on:

- simulated industrial telemetry
- anomaly detection
- operational risk monitoring
- predictive maintenance logic
- incident reporting
- RAG-based operator assistance
- dashboard-based industrial supervision

---

## Roadmap

### V2 — Machine Learning Anomaly Detection

- Add Isolation Forest
- Add anomaly scoring
- Compare ML-based and rule-based anomaly detection

### V3 — Time-Series Forecasting

- Forecast sensor evolution
- Predict future abnormal behavior
- Add maintenance lead-time estimation

### V4 — Backend Architecture

- Add FastAPI backend
- Separate backend and dashboard
- Add API endpoints

### V5 — Database Integration

- Replace CSV logging with SQLite or PostgreSQL
- Store telemetry and chatbot logs

### V6 — Deployment

- Dockerize the application
- Add deployment documentation
- Prepare cloud deployment

---

## Author

Built by Hugo Neuville as an applied AI engineering project focused on industrial monitoring, operational AI, predictive maintenance, and intelligent maintenance assistance.
