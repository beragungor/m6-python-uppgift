import requests

def get_live_weather(lat,lon):

    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude" : lat,
        "longitude" : lon,
        "current" : ["temperature_2m","wind_speed_10m"],
        "timezone" : "auto"
    }

    svar = requests.get(url, params=parameters)
    
    data = svar.json()
    current = data["current"]
    units = data["current_units"]

    return current["wind_speed_10m"], current["temperature_2m"]

def weatherr_checker(temp, wind_speed, humidity, nederbord):

def main():
    # wind_speed, temp = get_live_weather(59.85, 17.63)
    wind_speed = 100 
    temp = -1000
    print(f"wind speed is {wind_speed} and temprature is {temp}")

    if wind_speed > 20 or temp < -10:
        print("no bike homie, stay home u little chud")
    else:
        print("cykla bror")

main()

