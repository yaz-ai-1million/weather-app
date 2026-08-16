import requests

def get_weather(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params)
    return response.json()
data = get_weather("Gaza")
print(data)

location = data.get("results", [])[0] if data.get("results") else None
if location:
    latitude = location["latitude"]
    longitude = location["longitude"]
    print(f"Latitude: {latitude}, Longitude: {longitude}")

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_response = requests.get(weather_url, params={"latitude": latitude, "longitude": longitude ,"current_weather": True})
    print(weather_response.json())

    weather_data = weather_response.json()
    current_weather = weather_data.get("current_weather", {})
    print(f"Current Weather: {current_weather}")
