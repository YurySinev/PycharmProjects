import requests
import json

r = requests.get('https://baconipsum.com/api/?type=all-meat')
texts = json.loads(r.content)
print(type(texts))

for text in texts:
    print(text[:50],'\n')

print("*" * 50, '\n')
r = requests.get('http://api.github.com')
d = json.loads(r.content)
print(type(d))
print(d['following_url'])

print("*" * 50, '\n')

r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r.content)

print("*" * 50, '\n')

data = {'key' : 'value'}

r = requests.post('https://httpbin.org/post', json = json.dumps(data))
print(r.content)
