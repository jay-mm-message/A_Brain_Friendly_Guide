import json
import requests
import configparser
import logging

def getWeather():

    url = "http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"

    response = requests.get(url)
    weather_data = json.loads(response.text)

    print("weather_data: ", weather_data)

def main():
    getWeather()

if __name__ == "__main__":
    main()

 #"lon": 121.57, "lat": 25.04
