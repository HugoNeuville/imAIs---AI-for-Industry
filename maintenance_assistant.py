#maintenance_assistant.py

def maintenance_assistant(question):
    question = question.lower()

    if "temperature" in question or "overheating" in question:
        return (
            "High temperature may indicate overheating, insufficient cooling, excessive load, "
            "or lubrication issues. Check cooling systems, lubrication levels, airflow, and recent load changes."
        )

    elif "vibration" in question or "bearing" in question:
        return (
            "High vibration may indicate bearing wear, misalignment, imbalance, or rotating component degradation. "
            "Inspect bearings, shaft alignment, and rotating parts."
        )

    elif "pressure" in question:
        return (
            "Pressure abnormalities may indicate valve issues, pipe obstruction, leaks, or regulation problems. "
            "Inspect valves, pipes, seals, and pressure control systems."
        )

    elif "energy" in question or "consumption" in question:
        return (
            "High energy consumption may indicate abnormal load, motor stress, inefficient operating mode, "
            "or mechanical resistance. Review motor behavior, load conditions, and recent operating changes."
        )

    else:
        return (
            "I can help with temperature, vibration, pressure, and energy consumption issues. "
            "Try asking about one of these sensor anomalies."
        )