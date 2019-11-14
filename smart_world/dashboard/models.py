from django.db import models

# Create your models here.


class Datasensor(models.Model):
    sensor_id = models.IntegerField(db_column='sensor_ID')  # Field name made lowercase.
    sensorvalues = models.IntegerField()
    timer = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'datasensor'



class Sensors(models.Model):
    sensor_id = models.AutoField(db_column='sensor_ID', primary_key=True)  # Field name made lowercase.
    sensorvalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensors'


