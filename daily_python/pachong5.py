from bs4 import BeautifulSoup

import requests

from fake_useragent import UserAgent

ua = UserAgent()

headers = {'User_Agent': ua.chrome}

url = 'https://new.qq.com/ch/antip/'

response = requests.get(url,headers = headers)

soup = BeautifulSoup(response.text,'lxml')

soups = soup.find_all('div',class_="lazyload-placeholder")

print(soups)