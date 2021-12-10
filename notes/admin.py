from django.contrib import admin

# Register your models here.
from .models import Note


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Note)
