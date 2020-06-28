from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re

url=["https://www.ptt.cc/bbs/Gossiping/index.html"]
cookies={'over18': '1'}
headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "cookie":'_ga=GA1.2.1446506856.1481296007; __cfduid=d3f4c5e39e68abd99bb3d6ac2fe777c291545875296; over18=1'
        }
session=requests.Session()
print("-------------------第一頁-----------------------")
for i in range(10):        
        r=requests.get(url=url[-1],headers=headers,cookies=cookies)
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,features="html.parser")
        titles=soup.find_all("div",{"class":"title"})
        for title in titles:
                if title.a !=None:
                        print(title.a.get_text())
        last_page=soup.find("a",{"class":"btn wide"},string="‹ 上頁")
        url_name=last_page["href"].split("/")[-1].split(".")[0]
        last_page_url="https://www.ptt.cc/"+last_page["href"]
        url.append(last_page_url)
        print("-------------------以下%s-----------------------" % url_name)
