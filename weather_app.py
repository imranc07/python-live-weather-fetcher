"""
📌 Problem Statement
Create a Python script that fetches and displays live weather info for a city 
using the OpenWeatherMap API and saves the extracted data into a JSON file.
"""

import requests
import json
from datetime import datetime


def get_weather(city):
    # API setup
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Fetch temperature in Celsius
    }

    # Send request to OpenWeather API
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract relevant weather details
        weather_info = {
            "city": city,
            "temperature (C)": data['main']['temp'],
            "feels_like (C)": data['main']['feels_like'],
            "humidity (%)": data['main']['humidity'],
            "condition": data['weather'][0]['description'].capitalize(),
            "wind_speed (m/s)": data['wind']['speed'],
            "pressure (hPa)": data['main']['pressure'],
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Print formatted weather report
        print(f"\nWeather report for {city}:")
        print(f"🌡️  Temperature: {weather_info['temperature (C)']} ℃")
        print(f"🤔 Feels Like: {weather_info['feels_like (C)']} ℃")
        print(f"💧 Humidity: {weather_info['humidity (%)']} %")
        print(f"☁️  Condition: {weather_info['condition']}")
        print(f"💨 Wind Speed: {weather_info['wind_speed (m/s)']} m/s")
        print(f"🧭 Pressure: {weather_info['pressure (hPa)']} hPa")
        print(f"📅 Data Fetched At: {weather_info['fetched_at']}")

        # Save extracted info as JSON
        with open(f"{city}_weather.json", "w", encoding="utf-8") as f:
            json.dump(weather_info, f, indent=4)

        print(f"✅ Weather data saved in {city}_weather.json")

    else:
        # Handle invalid city names or API errors
        print("City not found or error fetching data.")


# --- Option 1: Fetch weather for a single city (user input) ---
# Uncomment below lines to enable user input mode
# city_from_user = input("Enter your city name: ")
# get_weather(city_from_user)


# --- Option 2: Fetch weather for multiple predefined cities ---
cities = ["Mumbai", "Delhi", "London", "New York"]
for city in cities:
    get_weather(city)
