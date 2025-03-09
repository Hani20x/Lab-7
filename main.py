import requests
import json

api_key = "aaee4c2668fdf2e1c5ff4db029e373d0"

city_name = "Tokyo"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    
    print(f"Погода в городе {city_name}:")
    print(f"Описание: {weather_description}")
    print(f"Температура: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Скорость ветра: {wind_speed} м/с")
else:
    print(f"Ошибка при запросе к API: {response.status_code}")