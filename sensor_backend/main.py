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

sensorconnection1 = HCSR04(Pin.exp_board.G6, Pin.exp_board.G7) # ports of expantion board 
sensorconnection2 = HCSR04(Pin.exp_board.G12, Pin.exp_board.G11)
sensorconnection3 = HCSR04(Pin.exp_board.G16, Pin.exp_board.G15)


def sensors():
    while True:
        sensor1 = sensorconnection1.distance_cm()
        sensor2 = sensorconnection2.distance_cm()
        sensor3 = sensorconnection3.distance_cm()

        sensorApi1 = ApiConnection(sensor1, 1) # give to values to the class ApiConnection. 
        sensorApi2 = ApiConnection(sensor2, 2) # value 1 is the distance, value 2 is which sensor
        sensorApi3 = ApiConnection(sensor3, 3)

        print("sensor1:", sensor1)
        time.sleep(1)
        print("sensor2:", sensor2)
        time.sleep(1)
        print("sensor3:", sensor3)

        sensorApi1.addSensorValue()# loops the value through the function addSensorValue
        time.sleep(1) 
        sensorApi2.addSensorValue()
        time.sleep(1) 
        sensorApi3.addSensorValue()
        time.sleep(1)

        if sensor1 < 10: 
            value1 = 0
        else: 
            value1 = 1 

        if sensor2 < 10: 
            value2 = 0
        else: 
            value2 = 1 

        if sensor3 < 10: 
            value3 = 0
        else: 
            value3 = 1 


        values = value1 + value2 + value3
        print(values)
        graph = Graph(values)

        graph.addParkingAvailable()
        time.sleep(5)
        


_thread.start_new_thread(sensors, ())
time.sleep(1)

# _thread.start_new_thread(graphtoner, ())






