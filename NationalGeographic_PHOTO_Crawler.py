from bs4 import BeautifulSoup
import requests
URL="http://www.ngchina.com.cn/animals/"

html=requests.get(URL).text
soup=BeautifulSoup(html,features="html.parser")
img_ul=soup.find_all("ul",class_="img_list")
print(len(img_ul))

import os
os.makedirs("./img/",exist_ok=True) # create a folder for these pictures

for ul in img_ul:
    imgs=ul.find_all("img")
    for img in imgs:
        url=img["src"]
        img_name=url.split("/")[-1]
        r=requests.get(url,stream=True)
        with open("./img/%s" % img_name,mode="wb") as file:
            for chunk in r.iter_content(chunk_size=128):
                file.write(chunk)
            print("Saved %s" % img_name)








