from django.shortcuts import render
from .models import Sensordata


def index(request):
    sensordata = Sensordata.objects.all()
    return render(request, "index.html", {'sensordata': sensordata})


def data(request):
    sensordata = Sensordata.objects.all()
    return render(request, "data.html", {'sensordata': sensordata})

