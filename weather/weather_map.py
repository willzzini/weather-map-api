import json

import requests
from flask import abort
from utils import _json_encode, format_data

WEATHER_URL = "http://api.openweathermap.org/data/2.5/"
HEADERS = {"Content-Type": "application/json"}


def city_weather(api_key, city_name):
    try:
        URL = WEATHER_URL + 'weather?' + "appid=" + api_key + "&q=" + city_name
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


def city_weather_forecast(api_key, city_name):
    try:
        URL = WEATHER_URL + 'forecast?' + "appid=" + api_key + "&q=" + city_name
        get_data = requests.get(
            URL,
            headers=HEADERS,
            timeout=10).json()
        data = format_data(json.loads(json.dumps(get_data, default=_json_encode)))

        return json.loads(json.dumps(get_data, default=_json_encode))
    except requests.exceptions.Timeout:
        return abort(408, {
            "status": False,
            "message": "Request timeout"
        })