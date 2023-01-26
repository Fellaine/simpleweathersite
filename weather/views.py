from django.shortcuts import render
import json
import urllib.request
from weather.api_key import api_key


def weather_view(request, *args, **kwargs):
    res = urllib.request.urlopen(
        f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q=pidhorodne&days=7&aqi=no"
        "&alerts=no").read() # reqesting data
    json_data = json.loads(res) # parse json to dict
    data = {
        "city": str(json_data["location"]["name"]),
        "temperature": str(json_data["current"]["temp_c"])
    } # getting current weather
    forecast = {}
    for day in json_data["forecast"]["forecastday"]:
        tmp = [day["day"]["avgtemp_c"], day["day"]["maxtemp_c"]]
        forecast[day["date"]] = tmp # getting forecast
    context = {'object': data, "forecast": forecast}
    return render(request, "weather.html", context)