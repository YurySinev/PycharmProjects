import requests
import json

r = requests.post('https://httpbin.org/post', data={'key' : 'value'})
print(r.content)