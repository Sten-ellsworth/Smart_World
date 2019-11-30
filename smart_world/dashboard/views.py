from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import SensorData, Sensors, Graph
from .serializer import SensorDataSerializer, SensorsSerializer, GraphSerializer, ChartFilter
from django.shortcuts import render



def index(request):
    # this value gets all of the data out off the database
    sensor = Sensors.objects.all()
    # this value gets all of empty values out off the database
    empty_or_full_value = Sensors.objects.filter(sensorValue=1)
    # graph query with date

    if not request.GET:
        curr_datetime = datetime.now()
        curr_date = curr_datetime.date()

        date = Graph.objects.filter(created_at__date=curr_date)


    else:
        input_date = request.GET['date']
        date = Graph.objects.filter(created_at__date=input_date)

    data = {
        'sensor': sensor,
        'empty_or_full_value': empty_or_full_value,
        'dates': date
    }

    return render(request, "index.html", data)

# def search(request):
#
#     if not request.GET:
#         curr_datetime = datetime.now()
#         curr_date = curr_datetime.date()
#
#         date = Graph.objects.filter(created_at__date=curr_date)
#
#
#     else:
#         input_date = request.GET['date']
#         date = Graph.objects.filter(created_at__date=input_date)
#
#     return render(request, 'index.html', {'dates': date}) # dit in de view


@api_view(['GET'])
def getGraph(request):
    graph = Graph.objects.all()
    serializer = GraphSerializer(graph, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postGraph(request):
    if request.method == 'POST':
        serializer = GraphSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getList(request):
    sensor_data = SensorData.objects.all()
    serializer = SensorDataSerializer(sensor_data, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def detailList(request, pk):
    try:
        sensor_data = SensorData.objects.get(pk=pk)
    except SensorData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SensorDataSerializer(sensor_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SensorDataSerializer(sensor_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postList(request):
    if request.method == 'POST':
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
