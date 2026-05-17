#predictive_maintenance.py

def calculate_risk_score(alerts):
    if len(alerts) == 0:
        return 0

    high_count = len(alerts[alerts["severity"] == "HIGH"])
    critical_count = len(alerts[alerts["severity"] == "CRITICAL"])

    score = high_count * 10 + critical_count * 40

    return min(score, 100)


def add_predictive_features(filtered_data, sensor_selected, window=20):
    df = filtered_data.copy()

    ma_column = f"{sensor_selected}_ma"
    trend_column = f"{sensor_selected}_trend"
    prediction_column = f"{sensor_selected}_prediction_alert"
    trend_alert_column = f"{sensor_selected}_trend_alert"

    df[ma_column] = df[sensor_selected].rolling(window=window).mean()

    threshold = df[ma_column].mean() + df[ma_column].std()

    df[prediction_column] = df[ma_column] > threshold
    df[trend_column] = df[ma_column].diff()
    df[trend_alert_column] = (
        (df[ma_column] > threshold) &
        (df[trend_column] > 0)
    )

    return df, ma_column, trend_column, prediction_column, trend_alert_column

