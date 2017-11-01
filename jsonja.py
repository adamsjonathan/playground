import json
import urllib.request, urllib.parse, urllib.error
url = input('Enter url:')
data = urllib.request.urlopen(url).read()
info = json.loads(data)
count=0
for item in info['comments']:
    count+=(item['count'])
print (count)
