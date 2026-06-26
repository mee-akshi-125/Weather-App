import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("YOUR_API_KEY")

if not API_KEY:
    print("Error: OPENWEATHER_API_KEY not found in .env file")
    exit()

city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print("\nWeather Details")
        print("----------------------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print(f"Error {response.status_code}: {data.get('message', 'Unknown error')}")
except Exception as e:
    print(f"Error: {e}")