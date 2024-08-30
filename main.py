import requests
from pprint import pprint

API_Key = 'cdec918a5ef51f5c3ad6611f76704f17'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q=" +city

weather_data = requests.get(base_url).json()

pprint(weather_data)