import urequests as requests
import json

print('\nDEMO#1: getting test webpage...')
data = {
    "ticker": "sten",
    "open": 1,
    "close": 2,
    "volume": 3
}

r = requests.post('http://172.20.10.2:8000/stocks/post', json=data)
#print(r)
print(r.content)
#print(r.text)
print('\n\nDEMO#3: getting public IP...')

#  r = urequests.get('http://127.0.0.1:8000/stocks/post/')
#  r.close()

