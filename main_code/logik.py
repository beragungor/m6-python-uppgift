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

def weather_no_bike_only(temp, wind_speed,nederbord):
    anledningar_att_inte_cykla = {
        "fly to air, too much wind" : wind_speed > 20,
        "straight up as freeze" : temp < -20,
        "det regnar för mycket" : nederbord > 0,
    }
    
    definitiv_no = []

    for meddelande, det_inte_bra in anledningar_att_inte_cykla.items():
        if det_inte_bra == True:
            definitiv_no.append(meddelande)
    
    if definitiv_no:
        print("no bike homie. Reasons:",",".join(definitiv_no))
    else:
        print("cykla bror")
#
# def main():
#     # wind_speed, temp = get_live_weather(59.85, 17.63)
#     wind_speed = 100 
#     temp = -1000
#     print(f"wind speed is {wind_speed} and temprature is {temp}")
#
#     if wind_speed > 20 or temp < -10:
#         print("no bike homie, stay home u little chud")
#     else:
#         print("cykla bror")
#
# main()
#
weather_no_bike_only(-100, 100, 100)


