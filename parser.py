# token for openweather api
import datetime
from pprint import pprint

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
        feels_temp = json_data["main"]["feels_like"]
        humidity = json_data["main"]["humidity"]
        pressure = json_data["main"]["pressure"]
        wind_speed = json_data["wind"]["speed"]
        return f"Date and time: {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n" \
               f"Your location: {city}\n" \
               f"Weather: {weather_desc}\n" \
               f"Current temperature: {curr_temp}\n" \
               f"Minimal temperature: {min_temp}, maximal temperature: {max_temp}\n" \
               f"Temperature feels like: {feels_temp}\n" \
               f"Humidity: {humidity}\n" \
               f"Pressure: {pressure}\n" \
               f"Wind Speed: {wind_speed}"



    except KeyError:
        print("Please, check name of a city you entered")


def main():
    city = input()
    print(get_weather(city, weather_token))


if __name__ == '__main__':
    main()
