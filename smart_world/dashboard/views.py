from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .models import SensorData, Sensors, Graph
from .serializer import SensorDataSerializer, SensorsSerializer, GraphSerializer
from django.shortcuts import render
from django.db.models import Avg



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

    #prognose
    curr_datetime = datetime.now()
    curr_date = curr_datetime.date()
    time_diff = timedelta(days=-5)
    prog_1_week = curr_date + time_diff
    prognose = Graph.objects.filter(created_at__date=prog_1_week, availability=0)[:1]

    data = {
        'sensor': sensor,
        'empty_or_full_value': empty_or_full_value,
        'dates': date,
        'prognose': prognose
    }

    return render(request, "index.html", data)

    #prognos avg. over 3 weeks
    curr_datetime = datetime.now()
    curr_date = curr_datetime.date()

    time_diff1 = timedelta(days=-7)
    prognose2 = curr_date + time_diff1
    prognose2_filter = Graph.objects.filter(created_at__date=prognose2, availability=0)[:1]

    time_diff2 = timedelta(days=-14)
    prognose3 = curr_date + time_diff2
    prognose3_filter = Graph.objects.filter(created_at__date=prognose3, availability=0)[:1]

    time_diff3 = timedelta(days=-21)
    prognose4 = curr_date + time_diff3
    prognose4_filter = Graph.objects.filter(created_at__date=prognose4, availability=0)[:1]

    time_avg = Avg(prognose2_filter, prognose3_filter, prognose4_filter)


    data = {
        'sensor': sensor,
        'empty_or_full_value': empty_or_full_value,
        'dates': date,
        'prognose2_filter': prognose2_filter,
        'time_avg': time_avg,
        'prognose4_filter': prognose4_filter
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
