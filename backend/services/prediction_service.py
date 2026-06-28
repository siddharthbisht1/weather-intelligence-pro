import random

# ==========================================
# AI Prediction Service (Mock)
# ==========================================

def get_prediction(city: str):
    predicted_temperature = round(
        random.uniform(20, 45),
        2
    )

    predicted_aqi = round(
        random.uniform(50, 300),
        2
    )

    # ======================================
    # Pollution Trend
    # ======================================

    pollution_trends = [
        "Increasing",
        "Stable",
        "Decreasing"
    ]

    pollution_trend = random.choice(
        pollution_trends
    )

    # ======================================
    # Risk Level
    # ======================================

    if predicted_aqi <= 100:
        risk_level = "Low"

    elif predicted_aqi <= 200:
        risk_level = "Moderate"

    else:
        risk_level = "High"

    # ======================================
    # Future Weather Insights
    # ======================================

    if predicted_temperature > 35:
        insight = (
            "High temperature expected. "
            "Stay hydrated."
        )

    else:
        insight = (
            "Normal weather conditions expected."
        )

    return {
        "city": city,
        "predicted_temperature": predicted_temperature,
        "predicted_aqi": predicted_aqi,
        "pollution_trend": pollution_trend,
        "risk_level": risk_level,
        "insight": insight
    }