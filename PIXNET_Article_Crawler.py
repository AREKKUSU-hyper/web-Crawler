from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os
os.makedirs("./art/",exist_ok=True)

base="https://帳號.pixnet.net/blog/category/0"
with urlopen(base) as html:
    home=html.read().decode("utf-8")
soup=BeautifulSoup(home,features="html.parser")
art_urls=soup.find_all("div", {"class":"article"})
for art_url in art_urls:
    h2=art_url.find("h2")
    urls=h2.find_all("a", {"href": re.compile("https://帳號.*")})
    for url in urls:
        article_name=url.string
        article=requests.get(url["href"])
        article.encoding='utf-8'
        innersoup=BeautifulSoup(article.text,features="html.parser")
        article_text=innersoup.find("div",class_="article-content-inner").get_text()
        print(article_name+": "+url["href"])
        print(article_text)
        print("-----------------------------------------------------------")
        with open("./art/%s.doc" % article_name,mode="wb+") as file:
            file.write(article_text.encode("utf-8")) 
        print("Saved %s" % article_name)

        
