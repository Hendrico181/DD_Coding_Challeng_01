import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import urllib


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        # ip = urllib.request.urlopen('https://ident.me/').read().decode('utf8')
    return ip


def index(request):
    g = GeoIP2
    ip = get_client_ip(request)
    print("AAAAAAAAAAAAAAAAAA",ip)
    # city = g.city(f'{ip}')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c17f80b8977a3ca05b570bd7a5b8679c'
    location = g.city(f'{ip}')
    city = location['city']

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context=context)
