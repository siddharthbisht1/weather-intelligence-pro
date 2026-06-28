import random

# ==========================================
# Water Quality Service
# ==========================================

def get_water_quality(city: str):
    ph = round(random.uniform(6.5, 8.5), 2)

    dissolved_oxygen = round(
        random.uniform(5.0, 10.0),
        2
    )

    turbidity = round(
        random.uniform(1.0, 5.0),
        2
    )

    water_temperature = round(
        random.uniform(15.0, 30.0),
        2
    )

    # ======================================
    # Determine Quality
    # ======================================

    if (
        6.5 <= ph <= 8.5
        and dissolved_oxygen >= 6
        and turbidity <= 3
    ):
        quality_status = "Good"

    elif (
        6.0 <= ph <= 9.0
        and dissolved_oxygen >= 4
    ):
        quality_status = "Moderate"

    else:
        quality_status = "Poor"

    return {
        "city": city,
        "ph": ph,
        "dissolved_oxygen": dissolved_oxygen,
        "turbidity": turbidity,
        "water_temperature": water_temperature,
        "quality_status": quality_status
    }