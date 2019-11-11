import urequests 
import sys
import time
import machine
from machine import Pin, Timer

echo = Pin(Pin.exp_board.G7, mode=Pin.IN)
trigger = Pin(Pin.exp_board.G8, mode=Pin.OUT)
trigger(0)

chrono = Timer.Chrono()

while True:

    chrono.reset()

    trigger(1)
    time.sleep_us(10)
    trigger(0)

    while echo() == 0:
        pass

    chrono.start()

    while echo() == 1:
        pass

    chrono.stop()

    distance = chrono.read_us() / 58.0

    print(round(distance, 2), "cm")
    
    time.sleep(5)
    if distance < 15: 
        userdata = "vol"
        r = urequests.post('http://172.20.10.2/Parkeergarage/get.php?value='+userdata)
    else: 
        datauser = "leeg"
        r = urequests.post('http://172.20.10.2/Parkeergarage/get.php?value='+datauser)
    r.close()
 


