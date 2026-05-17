#incident_reporting.py

def generate_incident_summary(machine, sensor_selected, sensor_alerts, risk_score):
    if len(sensor_alerts) == 0 or risk_score <= 40:
        return (
            f"{machine} shows normal {sensor_selected} behavior. "
            f"Current risk score: {risk_score}/100. "
            "No immediate maintenance action is required."
        )

    main_severity = sensor_alerts["severity"].value_counts().idxmax()

    if risk_score > 80:
        urgency = "Immediate maintenance inspection recommended."
    elif risk_score > 40:
        urgency = "Maintenance review recommended within 24h."
    else:
        urgency = "No immediate maintenance action is required."

    if sensor_selected == "temperature":
        issue = "thermal stress, overheating, cooling inefficiency, excessive load, or lubrication degradation"
        action = "inspect the cooling system, airflow, lubrication level, and recent machine load conditions"

    elif sensor_selected == "vibration":
        issue = "mechanical instability, bearing wear, shaft misalignment, imbalance, or rotating component degradation"
        action = "inspect bearings, shaft alignment, rotating components, and mechanical fixation points"

    elif sensor_selected == "pressure":
        issue = "pressure instability, valve malfunction, pipe obstruction, leakage, or pressure regulation failure"
        action = "inspect valves, pipes, seals, pressure regulators, and possible flow restrictions"

    elif sensor_selected == "energy_consumption":
        issue = "abnormal energy usage, motor stress, inefficient operating mode, overload, or increased mechanical resistance"
        action = "review motor behavior, load conditions, operating mode, energy consumption pattern, and mechanical resistance"

    else:
        issue = "abnormal machine behavior"
        action = "perform a general maintenance inspection"

    return (
        f"{machine} shows elevated {sensor_selected} risk, with {len(sensor_alerts)} alerts detected. "
        f"The main severity level is {main_severity}. "
        f"This may indicate {issue}. "
        f"Current risk score: {risk_score}/100. "
        f"Recommended action: {action}. "
        f"{urgency}"
    )


def save_incident_history(alerts_df, path="incident_history.csv"):
    alerts_df.to_csv(path, index=False)
