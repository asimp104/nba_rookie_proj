import requests

URL = 'http://127.0.0.1:5000/predict'

headers = {'Content-Type': 'application/json'}

data = {'input': [2.7,
 2.0,
 0.7,
 2.8,
 82.0,
 1.7,
 3.0,
 1.1,
 81.1,
 34.1,
 0.0,
 1.0,
 112.0,
 2.11,
 1.0,
 2015.0,
 1.0,
 0.24113475177304963,
 0.5822462615335667]}

r = requests.get(URL, headers=headers, json=data)

print(r.json())
        
 




