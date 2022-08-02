import urllib.request,urllib.parse,urllib.error
import json

link=input("Enter location:")
print("Retrieving", link)

data=urllib.request.urlopen(link).read().decode()
print("Retrieved",len(data),"characters")

try:
    js=json.loads(data)
except:
    js=None

count=0
sum=0

for item in js['comments']:
    count=count+1
    sum=sum+int(item['count'])

print("Count:",count)
print("Sum:",sum)
