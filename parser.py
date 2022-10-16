# token for openweather api
import datetime
#from pprint import pprint

import requests

weather_token = '22d38e4b789796c92e6e4fe65846ff67'

def get_weather(city, weather_token):
    try:
        request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"
        )
        json_data = request.json()
        # pprint(json_data)
        city = json_data["name"]
        weather_desc = json_data["weather"][0]["main"]
        curr_temp = json_data["main"]["temp"]
        max_temp = json_data["main"]["temp_max"]
        min_temp = json_data["main"]["temp_min"]
        fills_temp = json_data["main"]["feels_like"]
        humidity = json_data["main"]["humidity"]
        pressure = json_data["main"]["pressure"]
        wind_speed = json_data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(json_data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(json_data["sys"]["sunset"])

    except:
        print("Please, check name of a city you entered")


def main():
    city = input()
    get_weather(city, weather_token)


if __name__ == '__main__':
    main()
