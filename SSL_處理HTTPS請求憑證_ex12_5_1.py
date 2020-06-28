# Another Ver.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def findUrl(url,position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    return tags[position].get('href',None)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count_str = input('Enter count - ')
count = int(count_str)

position_str = input('Enter position - ')
position = int(position_str)-1

for i in range(count):
    if i==0:
        url_now = input('Enter - ')
        print(url_now)
        url_now = findUrl(url_now,position)
        print(url_now)
    else:
        url_now = findUrl(url_now,position) 
        print(url_now)