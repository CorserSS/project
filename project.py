import requests
import json

city = str(input('Введите город\n'))
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
min_temperature = round(weather_data['main']['temp_min'])
max_temperature = round(weather_data['main']['temp_max'])

print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')
print('Минимальная температура:', str(min_temperature), '°C')
print('Максимальная температура:', str(max_temperature), '°C')