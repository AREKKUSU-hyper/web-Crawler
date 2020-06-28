from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
base_url="https://baike.baidu.com"
history=["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

# select the last sub_url in history, print the title and url
url=base_url+history[-1]
with urlopen(url) as html:
    data=html.read().decode("utf-8")
soup=BeautifulSoup(data,features="html.parser")
print(soup.find("h1").string,": ",url)
# find all sub_urls for baidu baike, randomly select a sub_urls and store it in history.
# if no valid sub link is found, then pop last url in history.
sub_urls=soup.find_all("a", {"target":"_blank", "href":re.compile("/item/(%.{2})+$")}) 
print(len(sub_urls))
print(sub_urls[0])
print(sub_urls[0]["href"])
if len(sub_urls) !=0:
    history.append(random.choice(sub_urls)["href"])
    # history.append(random.sample(sub_urls,1)[0]["href"])
else:
    history.pop() # pop默认最后一个元素
print(history)


