from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
base_url="https://baike.baidu.com"
history=["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
for i in range(10):
    url=base_url+history[-1]
    with urlopen(url) as html:
        data=html.read().decode("utf-8")
    soup=BeautifulSoup(data,features="html.parser")
    print(i, soup.find("h1").string,": ",url)
    sub_urls=soup.find_all("a", {"target":"_blank", "href":re.compile("/item/(%.{2})+$")}) 
    if len(sub_urls) !=0:
        history.append(random.choice(sub_urls)["href"])
    else:
        history.pop()
    print(history)

