import machine
import settings
from network import WLAN

wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan() # Scan all SSID networks
print('WLAN init')
for net in nets:
    if net.ssid == "iPhone van Sten":
        wlan.connect(net.ssid, auth=(net.sec, "Praag1234"), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # Save power while waiting
        print('WLAN connection succeeded!')
        break