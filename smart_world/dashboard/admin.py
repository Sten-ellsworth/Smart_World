from django.contrib import admin
from .models import SensorData, Sensors

# Register your models here.
admin.site.register(SensorData)
admin.site.register(Sensors)
