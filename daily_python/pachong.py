from urllib import request  # 发起请求
from urllib import parse  # parse处理post数据
import socket
import urllib

# url = 'http://www.baidu.com'
#
# response = request.urlopen(url, timeout=1)
#
# print(response.read().decode('utf-8'))

#
# data = bytes(parse.urlencode({'world': 'hello'}), encoding='utf8')
#
# # post方式有data
# response = request.urlopen('http://www.infoq.cn', data=data)
#
# # print(response.read().decode('utf-8'))
#
# # get无data
# response2 = request.urlopen('http://httpbin.org', timeout=0.1)
#
# print(response2.read().decode('utf-8'))

try:
    response2 = request.urlopen('http://httpbin.org', timeout=1)
    print(response2.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time Out')