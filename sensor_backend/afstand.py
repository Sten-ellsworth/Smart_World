# import pycom
# import _thread
# import sys
# import time
# import machine
# from machine import Pin, Timer

# def distance():
#     echo = Pin(Pin.exp_board.G7, mode=Pin.IN)
#     trigger = Pin(Pin.exp_board.G8, mode=Pin.OUT)
#     trigger(0)

#     chrono = Timer.Chrono()

#     while True:

#         chrono.reset()

#         trigger(1)
#         time.sleep_us(10)
#         trigger(0)

#         while echo() == 0:
#             pass

#         chrono.start()

#         while echo() == 1:
#             pass

#         chrono.stop()

#         distance = chrono.read_us() / 58.0

#         print(round(distance, 2), "cm")
#         time.sleep(5)
#     return distance

# distance = distance()
# print(distance)
