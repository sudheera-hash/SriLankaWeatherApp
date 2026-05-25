import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# OpenWeatherMap base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city"""
    try:
        # Make API request
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check if city was found
        if data["cod"] != 200:
            return None, "City not found. Please check the name."

        # Extract the data we need
        weather_info = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"]
        }

        return weather_info, None

    except Exception as e:
        return None, "Something went wrong. Check your internet connection."