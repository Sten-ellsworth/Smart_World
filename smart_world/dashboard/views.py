from django.shortcuts import render
from .models import Sensors


def index(request):
    sensors = Sensors.objects.all()
    return render(request, "index.html", {'sensors': sensors})


def example(request):
    sensors = Sensors.objects.all()
    return render(request, "example.html", {'sensors': sensors})


