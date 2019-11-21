import datetime

from django.db.models import Model, NOT_PROVIDED, DateTimeField
from django.db import models

# Create your models here.
class sensorData(models.Model):
    sensorValues = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    sensor_ID = models.IntegerField()

    def save(self):
        if self.created_at == None:
            self.created_at = datetime.now()
            super(sensorData, self).save()

class sensors(models.Model):
    sensor_ID = models.IntegerField()
    sensorValue = models.IntegerField()
