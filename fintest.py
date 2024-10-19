import base64
import json
import requests

with open('test.py', 'rb') as f:
    data1 = f.read()
fb64 = base64.b64encode(data1).decode('utf-8')

with open('ldata_demo.csv', 'rb') as f:
    data2 = f.read()
db64 = base64.b64encode(data2).decode('utf-8')

payload = {
    'fname': 'test.py',
    'fdata': fb64,
    'dname': 'ldata_demo.csv',
    'ddata': db64
}

response = requests.post('http://127.0.0.1:5000/train-model', json=payload)
print(response.json())