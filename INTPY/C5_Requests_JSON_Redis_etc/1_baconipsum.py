import requests

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=5&start-with-lorem=1&format=html')
print(r.content)
print(r.content.__sizeof__())