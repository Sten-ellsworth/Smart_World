from rest_framework import serializers
import django_filters
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

class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = '__all__'

class ChartFilter(django_filters.FilterSet):
    created_at = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Graph
        fields = ['created_at']