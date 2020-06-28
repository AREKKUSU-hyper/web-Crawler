from bs4 import BeautifulSoup
import requests
URL="網址"

html=requests.get(URL).text
soup=BeautifulSoup(html,features="html.parser")
img_ul=soup.find_all("ul",{"class":"photo-grid-list"})
print(len(img_ul))

import os
os.makedirs("./pics/",exist_ok=True)

for ul in img_ul:
    imgs=ul.find_all("img")
    for img in imgs:
        url=img["src"]
        r=requests.get(url,stream=True)
        image_name=url.split("/")[-1]
        with open("./pics/%s" %image_name,mode="wb") as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print("saved %s" % image_name)

