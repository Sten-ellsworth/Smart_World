from network import WLAN      # For operation of WiFi network
import time                   # Allows use of time.sleep() for delays
import pycom                  # Base library for Pycom devices

import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code

# BEGIN SETTINGS
# These need to be change to suit your environment
RANDOMS_INTERVAL = 5000 # milliseconds
last_random_sent_ticks = 0  # milliseconds

# Wireless network
WIFI_SSID = "iPhone van Sten"
WIFI_PASS = "Praag1234" # No this is not our regular password. :)


# END SETTINGS

# RGBLED
# Disable the on-board heartbeat (blue flash every 4 seconds)
# We'll use the LED to respond to messages 
pycom.heartbeat(False)
time.sleep(0.1) # Workaround for a bug.
                # Above line is not actioned if another
                # process occurs immediately afterwards
print("connecting to wifi")
pycom.rgbled(0xff0000)  # Status red = not working

# WIFI
# We need to have a connection to WiFi for Internet access
# Code source: https://docs.pycom.io/chapter/tutorials/all/wlan.html

wlan = WLAN(mode=WLAN.STA)
wlan.connect(WIFI_SSID, auth=(WLAN.WPA2, WIFI_PASS), timeout=5000)

while not wlan.isconnected():    # Code waits here until WiFi connects
    machine.idle()

print("Connected to Wifi")
pycom.rgbled(0xffd7000) # Status orange: partially working

