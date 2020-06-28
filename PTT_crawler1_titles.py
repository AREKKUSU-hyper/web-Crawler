import urllib.request as req
url="https://www.ptt.cc/bbs/C_Chat/index.html"
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data, "html.parser")
# print(root.title.string)

# titles=root.find("div", class_="title")
# print(titles.a.string)

titles=root.find_all("div", class_="title")
with open("C_Chat.txt", mode="w", encoding="utf-8") as file:
    for title in titles:
        if title.a !=None:
            file.write(title.a.string+"\n")
