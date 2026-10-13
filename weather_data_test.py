import requests

def get_live_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Define the exact metrics you want to retrieve
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "timezone": "auto"
    }
    
    try:
        # timeout=10 prevents the script from hanging if the network drops
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() 
        
        data = response.json()
        current = data["current"]
        units = data["current_units"]
        
        print(f"Temperature: {current['temperature_2m']}{units['temperature_2m']}")
        print(f"Humidity: {current['relative_humidity_2m']}{units['relative_humidity_2m']}")
        print(f"Wind Speed: {current['wind_speed_10m']} {units['wind_speed_10m']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

# Example coordinates for Uppsala
get_live_weather(59.8588, 17.6389)
