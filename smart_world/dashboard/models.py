from django.db import models

# Create your models here.

class Sensordata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sensorvalues = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sensordata'


class Sensors(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sensor_1 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sensors'

