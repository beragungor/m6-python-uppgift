from enter_city_get_weather import get_city_coordinates, get_live_weather 

print("Hello World!")


if __name__ == "__main__":
    input_city_name = input("Give me the city name: ")

    koordinater = get_city_coordinates(input_city_name)

    if koordinater is not None:

        lat, long = koordinater
        get_live_weather(lat, long)
    else:
        print(f"Kunde inte hitta koordinater för staden {input_city_name}.")
