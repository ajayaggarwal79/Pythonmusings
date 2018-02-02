import json, urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    address = input('Enter URL: ')
    if len(address) < 1:
        break
    address="http://py4e-data.dr-chuck.net/comments_42.json"

url = address
print('Retrieving', url)
uh = urllib.request.urlopen(address).read()
print('Retrieved', len(uh), 'characters')
print(uh.decode())
#tree = ET.fromstring(data)

info = json.loads(uh)
print('User count:', len(info))
##
##for item in info:
##    print('Name', item['name'])
##    print('Id', item['id'])
##    print('Attribute', item['x'])
