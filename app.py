#app.py

import streamlit as st

from data_simulation import generate_industrial_dataset
from anomaly_detection import detect_sensor_anomalies
from predictive_maintenance import calculate_risk_score, add_predictive_features
from incident_reporting import generate_incident_summary, save_incident_history
from maintenance_assistant import maintenance_assistant
from rag_assistant import ask_maintenance_assistant


st.title("imAIs - Industrial Monitoring AI System")

industrial_data = generate_industrial_dataset()
alerts_df = detect_sensor_anomalies(industrial_data)
save_incident_history(alerts_df)

machine = st.selectbox(
    "Select Machine",
    industrial_data["machine_id"].unique()
)

filtered_data = industrial_data[
    industrial_data["machine_id"] == machine
]

machine_alerts = alerts_df[
    alerts_df["machine_id"] == machine
]

st.subheader("Incident Reports")
st.write("Total Alerts", len(machine_alerts))
st.dataframe(machine_alerts[["timestamp", "machine_id", "sensor", "value", "severity"]])

sensor_selected = st.selectbox(
    "Select Sensor",
    ["temperature", "vibration", "pressure", "energy_consumption"]
)

sensor_alerts = machine_alerts[
    machine_alerts["sensor"] == sensor_selected
]

st.subheader("Machine KPIs")

col1, col2, col3 = st.columns(3)

col1.metric(f"{sensor_selected.title()} Alerts", len(sensor_alerts))
col2.metric(f"Max {sensor_selected}", round(filtered_data[sensor_selected].max(), 2))
col3.metric(f"Average {sensor_selected}", round(filtered_data[sensor_selected].mean(), 2))

st.subheader(f"{sensor_selected.title()} Monitoring")
st.line_chart(filtered_data.set_index("timestamp")[sensor_selected])

st.subheader(f"{sensor_selected.title()} Alerts")
st.dataframe(sensor_alerts)

risk_score = calculate_risk_score(sensor_alerts)

st.metric("Risk Score", f"{risk_score}/100")

if risk_score >= 80:
    st.error("Critical operational risk - immediate inspection recommended.")
elif risk_score >= 40:
    st.warning("Elevated operational risk - maintenance review recommended.")
else:
    st.success("Normal operational condition.")

predictive_data, ma_column, trend_column, prediction_column, trend_alert_column = add_predictive_features(
    filtered_data,
    sensor_selected
)

st.line_chart(
    predictive_data.set_index("timestamp")[
        [sensor_selected, ma_column]
    ]
)

predicted_failures = predictive_data[
    predictive_data[prediction_column] == True
]

st.subheader(f"Predictive Maintenance Alerts — {sensor_selected}")

st.dataframe(
    predicted_failures[
        ["timestamp", sensor_selected, ma_column]
    ]
)

trend_alerts = predictive_data[
    predictive_data[trend_alert_column] == True
]

st.subheader(f"Trend-Based Predictive Alerts — {sensor_selected}")

st.dataframe(
    trend_alerts[
        ["timestamp", sensor_selected, ma_column, trend_column]
    ]
)

if len(trend_alerts) > 0:
    st.warning(
        f"{sensor_selected} trend increasing — preventive maintenance review recommended."
    )
else:
    st.success(
        f"No increasing {sensor_selected} risk trend detected."
    )

st.subheader("Generated Incident Summary")

summary = generate_incident_summary(
    machine,
    sensor_selected,
    sensor_alerts,
    risk_score
)

st.info(summary)

st.subheader("RAG Maintenance Chatbot")

if "rag_messages" not in st.session_state:
    st.session_state.rag_messages = []
    
if st.button("Clear chatbot"):
    st.session_state.rag_messages = []
    st.rerun()

for message in st.session_state.rag_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

        if message["role"] == "assistant" and "sources" in message:
            st.caption(
                "Sources: " + ", ".join(message["sources"])
            )

user_question = st.chat_input("Ask a maintenance question")

if user_question:
    st.session_state.rag_messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.write(user_question)

    answer, sources = ask_maintenance_assistant(
        user_question,
        st.session_state.rag_messages
    )

    st.session_state.rag_messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources
    })

    with st.chat_message("assistant"):
        st.write(answer)
        st.caption(
            "Sources: " + ", ".join(sources)
        )
