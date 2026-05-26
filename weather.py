import os
import sys
import requests
from tkinter import messagebox

def get_api_key():
    # Check if .env exists next to the .exe
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    env_path = os.path.join(base_path, '.env')
    
    if not os.path.exists(env_path):
        # Create .env file with instructions
        with open(env_path, 'w') as f:
            f.write("# Add your OpenWeatherMap API key below\n")
            f.write("WEATHER_API_KEY=\n")
        messagebox.showinfo("API Key Required", 
            "Please open the .env file next to this app and add your OpenWeatherMap API key.\n"
            "Get a free key from: https://home.openweathermap.org/api_keys")
        return None
    
    with open(env_path, 'r') as f:
        for line in f:
            if line.startswith("WEATHER_API_KEY="):
                key = line.strip().split("=", 1)[1]
                if key and not key.startswith("#"):
                    return key
    return None

API_KEY = get_api_key()

def get_weather(city):
    if not API_KEY:
        return None, "API key missing. Please set it in the .env file."
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},LK&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return None, data.get("message", "City not found")
        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "description": data["weather"][0]["description"].capitalize(),
            "temperature": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather, None
    except Exception as e:
        return None, str(e)