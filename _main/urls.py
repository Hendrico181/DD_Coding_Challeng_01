"""_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weather_locator.views import index
from notes.views import *


urlpatterns = [
    path('', index),
    path('notes/', notes_home_view),
    path('notes/create', note_create_view),
    path('notes/<int:id>/', note_detail_view),
    path('notes/<int:id>/edit', note_edit_view),
    path('notes/<int:id>/delete', delete_view),
    path('admin/', admin.site.urls),
]
