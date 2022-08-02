import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url=input("Enter the URL:")
data=urllib.request.urlopen(url)
a=data.read()
tree=ET.fromstring(a)
result=tree.findall('comments/comment')
count=0
sum=0
for item in result:
    x=int(item.find('count').text)
    count=count+1
    sum=sum+x
print("Count:",count)
print("Sum:",sum)