from django.shortcuts import render
from .models import Sensors


def index(request):
    # this value gets all of the data out off the database
    sensors = Sensors.objects.all()
    # this value gets all of empty values out off the database
    empty_or_full_value = Sensors.objects.filter(sensorvalue=1)
    return render(request, "index.html", {'sensors': sensors, 'empty_or_full_value': empty_or_full_value})


def example(request):
    sensors = Sensors.objects.all()
    return render(request, "example.html", {'sensors': sensors})


