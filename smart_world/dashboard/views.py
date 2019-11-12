from django.shortcuts import render
from .models import Sensordata
from .models import Sensors


def index(request):
    sensors = Sensors.objects.all()
    sensordata = Sensordata.objects.all()
    return render(request, "index.html", {'sensors': sensors, 'sensordata': sensordata})

def example(request):
    sensors = Sensors.objects.all()
    sensordata = Sensordata.objects.all()
    return render(request, "example.html", {'sensors': sensors, 'sensordata': sensordata})



