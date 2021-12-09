from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render



def home_view(request):
    context = {}
    HTML_STRING = render_to_string('home-view.html', context = context)
    return HttpResponse(HTML_STRING)
