from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2

g = GeoIP2()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



# Create your views here.
def location(request):
    ip = get_client_ip()
    HTML_STRING = f'''
    <p>{g.city(f'{ip}')}</p>
    '''
    return HttpResponse(HTML_STRING)

# def weather(request):
#     return HttpResponse(HTML_STRING)

