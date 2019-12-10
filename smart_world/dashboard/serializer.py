from rest_framework import serializers
from .models import SensorData, Sensors, Graph

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'


class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = '__all__'

