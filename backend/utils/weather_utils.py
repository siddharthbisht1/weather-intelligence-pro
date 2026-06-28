def weather_status(temp: float) -> str:
    """
    Categorizes the weather status based on the given temperature (in Celsius).
    """
    if temp >= 40:
        return "Extreme Heat"
    elif temp >= 30:
        return "Hot"
    elif temp >= 20:
        return "Pleasant"
    else:
        return "Cold"