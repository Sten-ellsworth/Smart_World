from django.shortcuts import render
from .models import Sensordata
from .models import Sensors


def index(request):
    sensors = Sensors.objects.all()
    return render(request, "index.html", {'sensors': sensors})


