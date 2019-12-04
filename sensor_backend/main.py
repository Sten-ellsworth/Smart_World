import urequests 
import sys
import time
import machine
from machine import Pin, Timer
from hcsr04 import HCSR04
from graph import Graph
from apiconnection import ApiConnection
import time
import _thread

sensorconnection1 = HCSR04(Pin.exp_board.G13, Pin.exp_board.G12) # ports of expantion board 
sensorconnection2 = HCSR04(Pin.exp_board.G9, Pin.exp_board.G8)
sensorconnection3 = HCSR04(Pin.exp_board.G16, Pin.exp_board.G15)

def print_distance():
    while True:
        print("sensor1:", sensorconnection1.distance_cm())
        print("sensor2:", sensorconnection2.distance_cm())
        print("sensor3:", sensorconnection3.distance_cm())

         
        sensorApi1 = ApiConnection(sensorconnection1.distance_cm(), 1) # give to values to the class ApiConnection. 
        sensorApi2 = ApiConnection(sensorconnection2.distance_cm(), 2) # value 1 is the distance, value 2 is which sensor
        sensorApi3 = ApiConnection(sensorconnection3.distance_cm(), 3)


        sensorApi1.addSensorValue() # loops the value through the function addSensorValue
        sensorApi2.addSensorValue()
        sensorApi3.addSensorValue()
        
        time.sleep(10)


def graphtoner(): 
    while True: 
        if sensorconnection1.distance_cm() < 15: 
            value1 = 0
        else: 
            value1 = 1 

        if sensorconnection2.distance_cm() < 15: 
            value2 = 0
        else: 
            value2 = 1 

        if sensorconnection3.distance_cm() < 15: 
            value3 = 0
        else: 
            value3 = 1 


        values = value1 + value2 + value3
        print(values)
        graph = Graph(values)

        graph.addParkingAvailable()
        time.sleep(11)


_thread.start_new_thread(print_distance, ())
time.sleep(1)

_thread.start_new_thread(graphtoner, ())





