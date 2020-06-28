from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode("utf-8")
soup=BeautifulSoup(html,features="html.parser")
month=soup.find_all("li", class_="month")
print(soup.title.get_text())
for m in month:
    print(m.string)

jan=soup.find("ul", {"class":"jan"})
# print(jan)
jan_d=jan.find_all("li")
# print(jan_d)
for j in jan_d:
    print(j.string)


html2=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode("utf-8")
soup2=BeautifulSoup(html2,features="html.parser")
print("\n",soup2.h1.string)
print(soup2.p.get_text())
href=soup2.find_all("a")
for h in href:
    print(h["href"]) # Tag裡找"屬性"，相當於用python字典key-value

