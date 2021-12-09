from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



# Create your views here.
def location(request):
    g = GeoIP2()
    ip = get_client_ip(request)
    test = g.city(f'{ip}')
    return HttpResponse(test)

# def weather(request):
#     return HttpResponse(HTML_STRING)

