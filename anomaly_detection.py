#anomaly_detection.py

import pandas as pd


def get_severity(sensor, value):
    if sensor == "temperature":
        if value >= 600:
            return "CRITICAL"
        elif value > 500:
            return "HIGH"

    elif sensor == "vibration":
        if value >= 60:
            return "CRITICAL"
        elif value > 55:
            return "HIGH"

    elif sensor == "pressure":
        if value >= 9:
            return "CRITICAL"
        elif value > 8:
            return "HIGH"

    elif sensor == "energy_consumption":
        if value >= 900:
            return "CRITICAL"
        elif value > 850:
            return "HIGH"

    return "NORMAL"


def generate_diagnosis(sensor):
    if sensor == "temperature":
        return "Possible overheating. Check cooling system, load level, and lubrication."
    if sensor == "vibration":
        return "Possible mechanical instability. Check bearings, alignment, and rotating components."
    if sensor == "pressure":
        return "Possible pressure abnormality. Inspect valves, pipes, and regulation system."
    if sensor == "energy_consumption":
        return "Possible abnormal load or inefficiency. Check motor behavior and operating mode."

    return "No diagnosis available."


def detect_sensor_anomalies(df):
    alerts = []

    for _, row in df.iterrows():
        for sensor in ["temperature", "vibration", "pressure", "energy_consumption"]:
            value = row[sensor]
            severity = get_severity(sensor, value)

            if severity != "NORMAL":
                alerts.append({
                    "timestamp": row["timestamp"],
                    "machine_id": row["machine_id"],
                    "sensor": sensor,
                    "value": round(value, 4),
                    "severity": severity,
                    "diagnosis": generate_diagnosis(sensor)
                })

    return pd.DataFrame(alerts)
