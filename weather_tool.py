import os
import requests
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool
def get_weather(city: str) -> dict:
    """
    Fetch max temperature (Celsius) for Kuala Lumpur using Google Weather API.
    Returns a dict: {"temperature": float}
    """
    api_key = os.getenv("GOOGLE_WEATHER_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_WEATHER_API_KEY environment variable not set.")
    # Hardcoded coordinates for Kuala Lumpur
    latitude = 3.139
    longitude = 101.6869
    endpoint = f"https://weather.googleapis.com/v1/currentConditions:lookup?key={api_key}&location.latitude={latitude}&location.longitude={longitude}"
    resp = requests.get(endpoint)
    if resp.status_code != 200:
        raise ValueError(f"Could not fetch weather for Kuala Lumpur: {resp.text}")
    data = resp.json()
    try:
        temp = data['currentConditionsHistory']['maxTemperature']['degrees']
    except (KeyError, TypeError, IndexError):
        raise Exception("Unexpected response format from Google Weather API.")
    return {"temperature": temp}
