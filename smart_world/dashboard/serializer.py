from rest_framework import serializers
from .models import SensorData
from .models import Sensors
from .models import Graph


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'

<<<<<<< Updated upstream
class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = '__all__'
=======
>>>>>>> Stashed changes
