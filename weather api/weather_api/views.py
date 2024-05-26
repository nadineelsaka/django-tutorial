from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    api_url = "api.openweathermap.org/data/2.5/weather?q=Egypt&appid=0c42f7f6b53b244c78a418f4f181282a/"
    # city_name = "Egypt"
    # url = api_url + city_name
    response = requests.get(api_url)
    content = response.json()
    city_weather = {
        'city': 'Egypt',
        'temperature': content['main']['temp'],
        'description': content['weather'][0]['description'],
        'icon': content['weather'][0]['icon']
    }
    return render(request, 'weather.html', city_weather)
