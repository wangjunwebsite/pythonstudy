import requests

from lxml import etree

html = requests.get('https://t-openscenic.ybsjyyn.com')


print(html.text)


html/body/script[4]