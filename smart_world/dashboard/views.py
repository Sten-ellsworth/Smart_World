from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timedelta

from .serializer import GraphSerializer, SensorDataSerializer, SensorsSerializer
from .models import Graph, SensorData, Sensors


def index(request):
    # this value gets all of the data out off the database
    sensor = Sensors.objects.all()
    # this value gets all of empty values out off the database
    empty_or_full_value = Sensors.objects.filter(sensorValue=1)
    # graph query with date
    if not request.GET:
        curr_datetime = datetime.now()
        curr_date = curr_datetime.date()
        time_diff = timedelta(days=-1)
        req_date_time = curr_date + time_diff

        date = Graph.objects.filter(created_at__date=req_date_time)


    else:
        input_date = request.GET['date']
        date = Graph.objects.filter(created_at__date=input_date)

    # prognose average
    # curr_datetime = datetime.now() # define current date with time
    curr_date = curr_datetime.date()  # define current date with time


    time1 = timedelta(days=-13)
    prog_01_week = curr_date + time1
    prognose1 = Graph.objects.filter(created_at__date=prog_01_week, availability=0)[:1]

    print(time1, "1")

    time2 = timedelta(weeks=-1)  # time difference of 1 week
    prog_02_week = curr_date + time2  # prognose of 2nd week with data from the previous week
    prognose2 = Graph.objects.filter(created_at__date=prog_02_week, availability=0)[:1]  # look into the database for availability = 0

    for prog2 in prognose2:
        time2 = datetime.strftime(prog2.created_at, "%I:%M %p") # formatting time with hours and minutes (AM & PM)

    print(time2, "2")

    time3 = timedelta(days=-13)  # time difference of 2 weeks
    prog_03_week = curr_date + time3  # prognose with the data from 3 weeks ago
    prognose3 = Graph.objects.filter(created_at__date=prog_03_week, availability=0)[:1] # look into the database for availability = 0

    for prog3 in prognose3:
        time3 = datetime.strftime(prog3.created_at, "%I:%M %p") # formatting time with hours and minutes (AM & PM)

    print(time3, "3")

    a = datetime.strptime(str(time2), "%I:%M %p")  # parse string to time in the same format
    b = datetime.strptime(str(time3), "%I:%M %p")  # parse string to time in the same format

    subtract = (a - b) / 2  # substract time2 - time3 and devide it by 2 to get the average in minutes
    print(subtract, "43")

    time_avg_1 = b + subtract  # get the average by getting the time difference from subtract and add it to time3
    print(time_avg_1.timestamp(), "correct")

    data = {
        'sensor': sensor,
        'empty_or_full_value': empty_or_full_value,
        'dates': date,
        'time_avg_1': time_avg_1
    }

    return render(request, "index.html", data)


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
    sensor_data = SensorData.objects.all()  # this value gets all of the data out off the database
    serializer = SensorDataSerializer(sensor_data, many=True)  # serialize the data to JSON format for the API
    return Response(serializer.data)  # return JSON serialized data


@api_view(['GET', 'PUT'])  # GET and PUT the data from and to the database
def detailList(request, pk):  # retrieve or update a code
    try:
        sensor_data = SensorData.objects.get(pk=pk)  # get specific pk = primary key
    except SensorData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # retrieve data from the database, path('sensor_data/<int:pk>, views.detailList
        serializer = SensorDataSerializer(sensor_data)  # serialize the data to JSON form for the API
        return Response(serializer.data)  # return JSON serialized data

    elif request.method == 'PUT':  # update data from the database, path('sensor_data/put/<int:pk>'
        serializer = SensorDataSerializer(sensor_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])  # create a new object in the database
def postList(request):
    if request.method == 'POST':  # create object in database, path('sensor_data/post/', views.postList
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
