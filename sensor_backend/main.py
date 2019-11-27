import urequests 
import sys
import time
import machine
from machine import Pin, Timer
from hcsr04 import HCSR04
from apiconnection import Graph
from apiconnection import ApiConnection
import time
import _thread

sensorconnection1 = HCSR04(Pin.exp_board.G8, Pin.exp_board.G7)
# sensorconnection2 = HCSR04(Pin.exp_board.G16, Pin.exp_board.G15)


def print_distance():
    while True:
        print("sensor1:", sensorconnection1.distance_cm())
        
        
        sensorApi1 = ApiConnection(sensorconnection1.distance_cm(), 1)
        sensorApi2 = ApiConnection(sensorconnection1.distance_cm(), 2)


        sensorApi1.addSensorValue()
        sensorApi2.addSensorValue()
        
        time.sleep(1)


def graphtoner(): 
    while True: 
        if sensorconnection1.distance_cm() < 15: 
            value1 = 0
        else: 
            value1 = 1 

        if sensorconnection1.distance_cm() < 15: 
            value2 = 0
        else: 
            value2 = 1 


        values = value1 + value2 
        print(values)
        graph = Graph(values)

        graph.addParkingAvailable()
        time.sleep(1)


# th = _thread.start_new_thread(graphtoner, ())


# th = _thread.start_new_thread(print_distance, ())

print_distance()
