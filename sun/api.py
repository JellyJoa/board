import requests
import json

url = ''
res = requests.get(url)
text = res.text

d = json.loads(text)
print(d)