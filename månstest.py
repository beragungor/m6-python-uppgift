from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut

def get_location_coords():
    geolocator = Nominatim(user_agent="Bikeability")

    while True:
        try:
            location_name = input("Your location (place, city, or address): ").strip()

            location = geolocator.geocode(location_name)

            if location:
                print("\nLocation found!\n")
                print(f"Adress: {location.address}")
                print(f"Latitude: {location.latitude}")
                print(f"Longitude: {location.longitude}")

                lat = location.latitude
                lon = location.longitude
                return

            else:
                print("\nNo location was found. Try being more specific.\n")

        except GeocoderUnavailable or GeocoderTimedOut as e:
            print(f"Connection error: {e}. Try checking your internet connection.")

get_location_coords()