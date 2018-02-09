"""
Script to read in JSON and extract a value in one of the JSON files
The value will then be summed and returned.
"""


import json, urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address=input("enter URL: ")

if len(address) <1:
    address="http://py4e-data.dr-chuck.net/comments_60177.json"

 

url = address

#print('Retrieving', url)

uh = urllib.request.urlopen(address).read()

print('Retrieved', len(uh), 'characters')

#print(uh.decode())

 

info = json.loads(uh)

#print('User count:', len(info))


acc=0
for item in info['comments']:
    acc=acc+int(item['count'])
print("sum", acc)
    

