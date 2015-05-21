#-*-encoding:utf-8-*-


import requests
import json

r=requests.post("http://127.0.0.1/index.php",data=json.dumps({'some': 'data'}))
print(r.json()[0])
print(r.txt())
