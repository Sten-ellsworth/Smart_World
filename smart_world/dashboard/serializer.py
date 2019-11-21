from rest_framework import serializers
from .models import sensorData
from .models import sensors


class sensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensorData
        fields = '__all__'


class sensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensors
        fields = '__all__'
