import json

import requests
from flask import abort
from utils import _json_encode

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?"
HEADERS = {"Content-Type": "application/json"}


def city_weather(api_key, city_name):
    try:
        URL = WEATHER_URL + "appid=" + api_key + "&q=" + city_name
        get_data = requests.get(
            URL,
            headers=HEADERS,
            timeout=10).json()
        return json.loads(json.dumps(get_data, default=_json_encode))
    except requests.exceptions.Timeout:
        return abort(408, {
            "status": False,
            "message": "Request timeout"
        })