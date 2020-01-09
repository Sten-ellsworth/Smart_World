import urequests 
import sys
import time
import json
import ujson
import machine


class ApiConnection:
  
    def __init__(self, sensor_value, sensor):
        
        self.distance = sensor_value
        self.sensor = sensor

    def addSensorValue(self):

        if self.distance < 10: 

          data = {
          "sensor_ID": self.sensor,
          "sensorValue": 0,
          }
  
          r = urequests.post("http://172.20.10.2:8080/sensor_data/post/", json=data)
          r.close()
          put = urequests.put("http://172.20.10.2:8080/sensor/put/"+ str(self.sensor)+ "/", json=data)
          put.close()
        else: 
          
          data = {
          "sensor_ID": self.sensor,
          "sensorValue": 1,
          }
 
          r = urequests.post("http://172.20.10.2:8080/sensor_data/post/", json=data)
          r.close()
          put = urequests.put("http://172.20.10.2:8080/sensor/put/"+ str(self.sensor)+ "/", json=data)
          put.close()
