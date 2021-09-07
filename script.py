import requests
from pyquery import  PyQuery
base_url='https://www.google.com/search?q=site:leader.ir/fa/subtitle&rlz=1C1GCEA_enIR887IR887&sxsrf' \
         '=AOaemvJDf9CzrmZtmaMKQ_Is8f4Soq0WZw:1630928850415&filter=0&biw=1536&bih=763 '
response=requests.get(base_url)
# print(response.content)
b=open('index.html','w')
b.write(response.text)
dom=PyQuery(response.content)
a=dom('div.kCrYT > a')

# print(a,type(a))
for i in a:
    j=PyQuery(i)
    print(j.attr('href'))