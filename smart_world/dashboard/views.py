from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData, Sensors
from .serializer import SensorDataSerializer, SensorsSerializer
from rest_framework import status, generics
from .models import SensorData, Sensors
from .serializer import SensorDataSerializer, SensorsSerializer
from django.shortcuts import render
from django.http import JsonResponse


def index(request): #path('', include(dashboard.urls)
    sensor = Sensors.objects.all()  # this value gets all of the data out off the database
    empty_or_full_value = Sensors.objects.filter(sensorValue=1) # this value gets all of empty values out off the database
    return render(request, "index.html", {'sensor': sensor, 'empty_or_full_value': empty_or_full_value}) #return the request of index.html


def getList(request):
    sensor_data = SensorData.objects.all() # this value gets all of the data out off the database
    serializer = SensorDataSerializer(sensor_data, many=True) #serialize the data to JSON format for the API
    return Response(serializer.data) #return JSON serialized data


@api_view(['GET', 'PUT']) #GET and PUT the data from and to the database
def detailList(request, pk): #retrieve or update a code
    try:
        sensor_data = SensorData.objects.get(pk=pk) #get specific pk = primary key
    except SensorData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': #retrieve data from the database, path('sensor_data/<int:pk>, views.detailList
        serializer = SensorDataSerializer(sensor_data) #serialize the data to JSON form for the API
        return Response(serializer.data) #return JSON serialized data

    elif request.method == 'PUT': #update data from the database, path('sensor_data/put/<int:pk>'
        serializer = SensorDataSerializer(sensor_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST']) #create a new object in the database
def postList(request):
    if request.method == 'POST': #create object in database, path('sensor_data/post/', views.postList
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def sensorList(request):
    sensor = Sensors.objects.all()
    serializer = SensorsSerializer(sensor, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sensorList(request):
    sensor = Sensors.objects.all()
    serializer = SensorsSerializer(sensor, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def sensorDetail(request, sensor_id):
    try:
        sensor_id = Sensors.objects.get(sensor_ID=sensor_id)
    except Sensors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SensorsSerializer(sensor_id)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SensorsSerializer(sensor_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sensorPost(request):
    if request.method == 'POST':
        serializer = SensorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
