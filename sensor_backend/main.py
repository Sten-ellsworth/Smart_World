import urequests 
import sys
import time
import machine
from machine import Pin, Timer
from hcsr04 import HCSR04
import time
import _thread

sensor1 = HCSR04(Pin.exp_board.G8, Pin.exp_board.G7)
# sensor2 = HCSR04(Pin.exp_board.G16, Pin.exp_board.G15)


def print_distance():
    while True:
        if sensor1.distance_cm() < 15: 
        sensordata = '0'
        sensor = '1'
        r = urequests.post('http://172.20.10.2:8080/Parkeergarage/get.php?value='+sensordata+'&sensor='+sensor)
    else: 
        sensordata = '1'
        sensor = '1'
        r = urequests.post('http://172.20.10.2:8080/Parkeergarage/get.php?value='+sensordata+'&sensor='+sensor)
    r.close()
        print("sensor1:", sensor1.distance_cm())
        time.sleep(2)
    

# th = _thread.start_new_thread(print_distance, ())

print_distance()
