from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render



def home_view(request):
    context = {}
    return render(request,'home-view.html', context=context)
