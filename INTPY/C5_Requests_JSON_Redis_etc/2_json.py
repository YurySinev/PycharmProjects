import requests
import json

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)
#
# for i in texts:
#     print(i[:50], '\n')

print() #--------------------------------------------------------------

r = requests.get('https://api.github.com')
d = json.loads(r.content)
print(type(d))
print(d['following_url'])

# отправка данных в формате JSON:

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(data))
print(r.content)



