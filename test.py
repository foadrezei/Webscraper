import requests
from pyquery import PyQuery

url='https://www.leader.ir/fa/media/play/22318'
response=requests.get(url)
# print(response.content)
dom=PyQuery(response.content)
a=dom('video source').attr('src')
# print(a)
root_url='https://www.leader.ir'
root_url+=a
# print(root_url)

print(dom)