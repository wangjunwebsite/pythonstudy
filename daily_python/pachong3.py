import requests
import re

url = 'http://www.cnu.cc/selectedPage'
content = requests.get(url)
# print(content.text)

pattern = re.compile(r'<a href="(.*?)".*?workBody">(.*?)</div>')
results = re.findall(pattern,content.text)

print(results)

# for result in results:
#     url , name = results
#
# print(url,re.sub('\s','',name))