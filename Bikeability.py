from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut
import requests
from account import login, register

def get_location_coords():
    geolocator = Nominatim(user_agent="Bikeability")

    while True:
        try:
            location_name = input("Your location (place, city, or address): ").strip()

            location = geolocator.geocode(location_name, timeout = 12)

            if location:
                print("\nLocation found!\n")
                print(f"Adress: {location.address}")
                print(f"Latitude: {location.latitude}")
                print(f"Longitude: {location.longitude}")

                lat = location.latitude
                lon = location.longitude
                return lat, lon

            else:
                print("\nNo location was found. Try being more specific.\n")

        except (GeocoderUnavailable, GeocoderTimedOut) as e:
            print(f"Connection error: {e}. Try checking your internet connection.")


def get_current_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current":
        ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "precipitation"],
        "wind_speed_unit": "ms", 
    }


    response = requests.get(url, params = weather_params)
    data = response.json()

    current = data["current"]
    units = data["current_units"]

    temp = current["temperature_2m"]
    humid = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]
    prec = current["precipitation"]

    print("\nThis is the current weather in that area:\n")

    print(f"Temperature: {current["temperature_2m"]} {units["temperature_2m"]}")
    print(f"Precipitation: {current["precipitation"]} {units["precipitation"]}")
    print(f"Relative humidity: {current["relative_humidity_2m"]} {units["relative_humidity_2m"]}")
    print(f"Wind speed: {current["wind_speed_10m"]} {units["wind_speed_10m"]}\n")

    return temp, humid, wind, prec


def logic(temp, humid, wind, prec):
    if wind > 8:
        answer = "Do not touch the bike"

    elif temp < 4 and humid > 85:
        answer = "Don't you DARE touch the bike"

    elif temp < 1 and prec > 0:
        answer = "no bike"

    else:
        answer = "yes go bike"

    return answer


def main():
    print("\nWelcome to Bikability!\n")
    print("What do you want to do?")
    while True:
        ans = input("    Log in (l)\n    Register (r)\n    Use Bikeability (b)\n    Quit (q)\nOption: ").strip().lower()
        if ans == "l":
            logged_in = login()
            break

        elif ans == "r":
            logged_in = register()
            break

        elif ans == "b":
            break

        elif ans == "q":
            print("Cya!")
            return
        
        else:
            print("\nPlease choose a valid option.")

    #if logged_in:
       # print("You are logged in!")

    lat, lon = get_location_coords()
    temp, humid, wind, prec = get_current_weather(lat, lon)

    answer = logic(temp, humid, wind, prec)
    print(f"\n{answer}")

main()