# 🌤️ Weather Info Fetcher

## 📌 Problem Statement
Create a Python script that fetches and displays live weather info for a city using the OpenWeatherMap API and saves the extracted data into a JSON file.

---

## 📖 Features
- Fetches **live weather data** from OpenWeatherMap API.
- Displays formatted weather information including:
  - 🌡️ Temperature
  - 🤔 Feels Like temperature
  - 💧 Humidity
  - ☁️ Condition
  - 💨 Wind Speed
  - 🧭 Pressure
  - 📅 Timestamp when data was fetched
- Saves extracted weather data into a **JSON file** per city.
- Supports **single city (user input)** and **multiple cities (predefined list)**.

---

## ⚙️ Requirements
- Python 3.x
- `requests` library
- OpenWeatherMap API key (get one for free: [https://openweathermap.org/api](https://openweathermap.org/api))

Install dependencies:
```bash
pip install requests
```
---

🚀 Setup & Run Instructions

- Clone or download the project folder.

- Open terminal/command prompt and navigate to the project folder.

- Replace the placeholder API key in weather.py with your own OpenWeatherMap API key.

- Run the script:
```bash
python weather_app.py
```
- Check the output:
- Terminal will display formatted weather reports.
- JSON files (e.g., Delhi_weather.json) will be saved automatically in the same folder.

---

## 🚀 Usage

### Option 1: Single City (User Input)
Uncomment these lines in the script:
```python
city_from_user = input("Enter your city name: ")
get_weather(city_from_user)
```

### Option 2: Multiple Cities (Predefined List)
Modify the list in the script:
```python
cities = ["Mumbai", "Delhi", "London", "New York"]
for city in cities:
    get_weather(city)
```

---

## 📂 Project Structure
```
Weather-Info-Fetcher/
│-- weather.py            # Main Python script
│-- README.md             # Documentation
│-- Mumbai_weather.json   # Example saved weather data
│-- Delhi_weather.json    # Example saved weather data
│-- London_weather.json   # Example saved weather data
│-- New York_weather.json # Example saved weather data
```

---

## 💾 Output Example (Saved JSON)
Example saved JSON (`Delhi_weather.json`):
```json
{
    "city": "Delhi",
    "temperature (C)": 29.08,
    "feels_like (C)": 33.09,
    "humidity (%)": 71,
    "condition": "Scattered clouds",
    "wind_speed (m/s)": 3.31,
    "pressure (hPa)": 1005,
    "fetched_at": "2025-09-07 00:17:21"
}
```

---

## 🖥️ Sample Terminal Output
Below is an example of the formatted weather report displayed in the terminal:

```
Weather report for Delhi:
🌡️  Temperature: 29.08 ℃
🤔 Feels Like: 33.09 ℃
💧 Humidity: 71 %
☁️  Condition: Scattered clouds
💨 Wind Speed: 3.31 m/s
🧭 Pressure: 1005 hPa
📅 Data Fetched At: 2025-09-07 00:17:21
✅ Weather data saved in Delhi_weather.json
```

---

## 📝 Notes
- Replace the placeholder API key in the script with your own key.
- Make sure you have a stable internet connection while running the script.

---

✅ Developed as part of a Python automation learning exercise.
