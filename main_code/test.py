# test kod för att göra request genom att använda api.open-meteo.com 
#
import requests

def get_live_weather(lat,lon):

    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude" : lat,
        "longitude" : lon,
        "current" : ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "timezone" : "auto"
    }

    svar = requests.get(url, params=parameters)
    
    data = svar.json()
    current = data["current"]
    units = data["current_units"]

    print(current["temperature_2m"], units["temperature_2m"])
    print(current["relative_humidity_2m"], units["relative_humidity_2m"])
    print(current["wind_speed_10m"], units["wind_speed_10m"])


get_live_weather(59.3, 18.06)
