from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode("utf-8")
soup=BeautifulSoup(html,features="html.parser")
img_links=soup.find_all("img",  {"src":re.compile(".*?\.jpg")})
# print(img_links)
for link in img_links:
    print(link["src"])
print("--------------------------------")
course_links=soup.find_all("a", {"href":re.compile("https://.*")})
for link in course_links:
    print(link["href"])

