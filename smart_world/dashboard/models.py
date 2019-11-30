import datetime

from django.db.models import Model, NOT_PROVIDED, DateTimeField
from django.db import models
from datetime import datetime


# Create your models here.
class SensorData(models.Model):
    sensor_ID = models.IntegerField()
    sensorValue = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = datetime.now()
            super(SensorData, self).save(*args, **kwargs)

    # x = '2014-09-23T18:43:26.692Z'
    # y = dateparse.parse_datetime(x)


class Graph(models.Model):
    availability = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = datetime.now()
            super(Graph, self).save(*args, **kwargs)

class Sensors(models.Model):
    sensor_ID = models.IntegerField()
    sensorValue = models.IntegerField()
