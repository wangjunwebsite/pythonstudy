import requests

# get方式
url = 'http://httpbin.org/get'
data = {
    'value': 'key',
    '123': '456',
    'fasf': 'fsaaf'
}

response = requests.get(url, data)
print(response.text)

# post方式
url = 'http://httpbin.org/post'
data = {
    'value': 'key',
    '123': '456',
    'fasf': 'fsaaf'
}

response = requests.post(url, data)
#返回类型为json的格式
print(response.json())
