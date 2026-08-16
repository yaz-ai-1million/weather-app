# Weather App 🌤️

A simple command-line weather application built with Python.

The program asks the user for a city name, finds the city's coordinates using the Open-Meteo Geocoding API, and then retrieves the current temperature using the Open-Meteo Weather API.

## Features

* 🌍 Search for a city by name
* 📍 Get the city's latitude and longitude
* 🌡️ Display the current temperature
* 🌐 Use real-time weather data from an API
* ❌ Handle cities that cannot be found
* 🛡️ Handle connection and API request errors
* 💻 Simple command-line interface

## Technologies Used

* Python
* `requests`
* JSON
* Open-Meteo API

## Project Structure

```text
Weather-App/
│
├── weather_app.py
├── requirements.txt
└── README.md
```

## Installation

First, install the required Python package:

```bash
pip install requests
```

Or, if you are using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## How to Run

Run the program with:

```bash
python weather_app.py
```

The program will ask:

```text
Enter city name:
```

Enter a city, for example:

```text
Enter city name: Gaza
```

The program will then display the current temperature:

```text
Current Temperature in Gaza: 25°C
```

## How It Works

The program works in two main steps.

### 1. Find the City

The program sends the city name to the Open-Meteo Geocoding API.

The API returns information about the city, including:

* Latitude
* Longitude

### 2. Get the Weather

The program uses the latitude and longitude to request current weather information from the Open-Meteo Weather API.

It then extracts the current temperature and displays it to the user.

## Error Handling

The program handles several possible problems:

* City not found
* Weather data unavailable
* Connection problems
* API request errors

For example:

```text
City not found.
```

or:

```text
Unable to connect to the weather service.
```

## What I Learned

Through this project, I practiced:

* Creating Python functions
* Working with external APIs
* Using the `requests` library
* Sending parameters with HTTP requests
* Reading JSON responses
* Working with dictionaries and lists
* Using `.get()`
* Handling missing data
* Using `try` and `except`
* Handling HTTP errors with `raise_for_status()`
* Working with real-world data

## API

This project uses the Open-Meteo API to retrieve geocoding and weather information.

## Future Improvements

Possible improvements for future versions:

* Display weather conditions
* Display wind speed
* Display humidity
* Add a multi-day forecast
* Add a graphical user interface
* Allow users to search for multiple cities

## Author

**Yazan**

This project was created as part of my journey to improve my Python programming skills through practical projects.
