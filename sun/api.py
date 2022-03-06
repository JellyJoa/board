import requests

url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido'
params ={'serviceKey' : '서비스키' }

response = requests.get(url, params=params)
print(response.content)