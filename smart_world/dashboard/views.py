from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import sensorData, sensors
from .serializer import sensorDataSerializer, sensorsSerializer
from django.shortcuts import render
# from .models import Sensors


# def index(request):
#     # this value gets all of the data out off the database
#     sensors = Sensors.objects.all()
#     # this value gets all of empty values out off the database
#     empty_or_full_value = Sensors.objects.filter(sensorvalue=1)
#     return render(request, "index.html", {'sensors': sensors, 'empty_or_full_value': empty_or_full_value})
#
#
# def example(request):
#     sensors = Sensors.objects.all()
#     return render(request, "example.html", {'sensors': sensors})


def index(request):
    return render(request, "index.html")


@api_view(['GET'])
def getList(request):
    sensor_data = sensorData.objects.all()
    serializer = sensorDataSerializer(sensor_data, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def detailList(request, pk):
    try:
        sensor_data = sensorData.objects.get(pk=pk)
    except sensorData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = sensorDataSerializer(sensor_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = sensorDataSerializer(sensor_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postList(request):
    if request.method == 'POST':
        serializer = sensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def sensorList(request):
    sensor = sensors.objects.all()
    serializer = sensorsSerializer(sensor, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def sensorDetail(request, pk):
    try:
        sensor = sensors.objects.get(pk=pk)
    except sensors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = sensorsSerializer(sensor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = sensorDataSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sensorPost(request):
    if request.method == 'POST':
        serializer = sensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
