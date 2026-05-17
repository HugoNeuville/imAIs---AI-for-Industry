#data_simulation.py

import pandas as pd
import numpy as np
import random as rd


def generate_machine_data(machine_id, n_points=1000, n_anomalies=5):
    temperature = np.random.normal(350, 50, n_points)
    vibration = np.random.normal(40, 5, n_points)
    pressure = np.random.normal(5, 1, n_points)
    energy_consumption = np.random.normal(700, 50, n_points)

    anomaly_indices = rd.sample(range(n_points), n_anomalies)

    for index in anomaly_indices:
        anomaly_type = rd.choice([
            "temperature",
            "vibration",
            "pressure",
            "energy_consumption"
        ])

        if anomaly_type == "temperature":
            temperature[index] = rd.randint(400, 800)
        elif anomaly_type == "vibration":
            vibration[index] = rd.randint(45, 80)
        elif anomaly_type == "pressure":
            pressure[index] = rd.randint(6, 10)
        elif anomaly_type == "energy_consumption":
            energy_consumption[index] = rd.randint(750, 1000)

    return pd.DataFrame({
        "timestamp": pd.date_range(start="2026-01-01", periods=n_points, freq="min"),
        "machine_id": machine_id,
        "temperature": temperature,
        "vibration": vibration,
        "pressure": pressure,
        "energy_consumption": energy_consumption
    })


def generate_industrial_dataset(n_machines=5, n_points=1000, n_anomalies=5):
    machines = []

    for i in range(1, n_machines + 1):
        machine_id = f"MACHINE_{i:02d}"
        machines.append(generate_machine_data(machine_id, n_points, n_anomalies))

    return pd.concat(machines, ignore_index=True)
