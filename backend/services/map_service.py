# backend/services/map_service.py
import random

def fetch_map_data(city: str):
    """
    Generates geospatial data, simulated environmental hotspots, 
    and AI insights for the requested city.
    """
    # Base coordinates dictionary
    city_coords = {
        "delhi": {"lat": 28.7041, "lng": 77.1025},
        "mumbai": {"lat": 19.0760, "lng": 72.8777},
        "dehradun": {"lat": 30.3165, "lng": 78.0322},
        "bengaluru": {"lat": 12.9716, "lng": 77.5946},
        "haldwani": {"lat": 29.2183, "lng": 79.5130},
        "chennai": {"lat": 13.0827, "lng": 80.2707},
        "kolkata": {"lat": 22.5726, "lng": 88.3639}
    }
    
    city_lower = city.lower()
    
    # Fallback to random Indian coordinates if city not in dictionary
    if city_lower in city_coords:
        lat = city_coords[city_lower]["lat"]
        lng = city_coords[city_lower]["lng"]
    else:
        lat = random.uniform(10.0, 30.0)
        lng = random.uniform(70.0, 90.0)

    # Generate localized AI Insights
    insights = [
        f"AQI levels are fluctuating near {city.capitalize()} industrial zones.",
        f"Rainfall expected to increase by {random.randint(10, 40)}% in the next 48 hours.",
        f"Wind patterns show a {random.choice(['north-easterly', 'south-westerly'])} flow.",
        f"Satellite imagery indicates cloud buildup around coordinates ({round(lat, 2)}, {round(lng, 2)})."
    ]

    # Generate simulated environmental hotspots around the city
    def generate_hotspots(count, radius=0.1):
        return [
            {
                "lat": lat + random.uniform(-radius, radius),
                "lng": lng + random.uniform(-radius, radius),
                "value": random.randint(50, 100)
            } for _ in range(count)
        ]

    return {
        "city": city.capitalize(),
        "coordinates": {"lat": lat, "lng": lng},
        "insights": insights,
        "hotspots": {
            "aqi": generate_hotspots(3),
            "wind": generate_hotspots(2),
            "rain": generate_hotspots(4)
        }
    }